#!/usr/bin/env python3
"""Генерирует /.well-known/vnish-global.json - машинное доказательство состава сети.

Один и тот же файл на трёх доменах: три сайта, Wikidata, GitHub, Zenodo concept DOI
и текущий digest каталога. Дизайна и клиентского пути не касается, страницы не меняет.
Пустые идентификаторы означают «сущность ещё не создана» и в файл не попадают.
"""
import json, os, hashlib
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = json.load(open(os.path.join(HERE, "IDENTIFIERS.json"), encoding="utf-8"))
cat = open(os.path.join(HERE, "data/current/catalog.json"), encoding="utf-8").read()
doc = json.loads(cat)
payload = {
    "network": "VNISH GLOBAL",
    "principle": "Three independent sites. Each publishes the full catalog and serves its own downloads.",
    "sites": [s.split("//")[1] for s in doc["network"]["sites"]],
    "catalog": {
        "name": doc["name"],
        "dataset_schema_version": doc["dataset_schema_version"],
        "counts": {k: doc["counts"][k] for k in ("models", "builds", "routes")},
        "firmware_versions": doc["counts"]["firmware_versions"],
        "digest_sha256": hashlib.sha256(cat.encode()).hexdigest(),
    },
    "identifiers": {k: v for k, v in ids.items() if v and k != "note"},
    "release": doc["release"],
    "updated": doc["updated"],
}
out = os.path.join(HERE, "well-known", "vnish-global.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w", encoding="utf-8").write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print("готово:", out)
print(json.dumps(payload, ensure_ascii=False, indent=2)[:520])
