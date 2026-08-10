#!/usr/bin/env python3
"""CI: допустимы только точные адреса из трёх классов доверия.

Домен сам по себе прав не даёт. `github.com` и `zenodo.org` проходят только с
нашим префиксом: чужой репозиторий или чужая запись отклоняются.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(HERE, "TRUSTED-SURFACES.json"), encoding="utf-8"))
own = set(cfg["class_1_download_domains"]["domains"])
exact = set(cfg["class_2_independent_sources"]["urls"])
prefixes = tuple(cfg["class_3_our_external_accounts"]["allowed_url_prefixes"])
neutral_exact_prefix = ("https://schema.org/", "https://creativecommons.org/licenses/",
                        "https://opendatacommons.org/licenses/", "https://spdx.org/licenses/",
                        "https://json-schema.org/draft/",
                        "https://doi.org/10.5281/")
URL = re.compile(r"https?://[^\s)\"\'<>\]]+")
bad = {}
for root, dirs, files in os.walk(HERE):
    dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
    for fn in files:
        if not fn.endswith((".json", ".md", ".csv", ".txt", ".py", ".yml", ".yaml", ".cff", ".html")):
            continue
        p = os.path.join(root, fn)
        if os.path.basename(p) == "TRUSTED-SURFACES.json":
            continue
        for m in URL.finditer(open(p, encoding="utf-8", errors="replace").read()):
            url = m.group(0).rstrip(".,;)")
            if url in exact or url.startswith(prefixes) or url.startswith(neutral_exact_prefix):
                continue
            host = re.sub(r"^https?://", "", url).split("/")[0].lower()
            if host in own:
                continue
            bad.setdefault(url, set()).add(os.path.relpath(p, HERE))
if bad:
    print("FAIL: адреса вне трёх классов доверия")
    for u, fs in sorted(bad.items())[:20]:
        print(f"  {u}  ({len(fs)} файл(ов), например {sorted(fs)[0]})")
    sys.exit(1)
print("PASS: все адреса точно внутри трёх классов доверия")
