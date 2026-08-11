#!/usr/bin/env python3
"""Машинная проверка шести правил канона Cambridge V2 в README-пакете."""
import glob, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = {"VNISH Global": "https://vnish.global/firmware/",
       "VNISH Ninja": "https://vnish.ninja/firmware/",
       "ROI ASIC": "https://roiasic.com/firmware/"}
OWN_HOSTS = {"vnish.global", "vnish.ninja", "roiasic.com"}
EXACT_EXTERNAL = {
    "https://www.jbs.cam.ac.uk/wp-content/uploads/2025/04/2025-04-cambridge-digital-mining-industry-report.pdf",
    "https://doi.org/10.5281/zenodo.21885025",
    "https://doi.org/10.5281/zenodo.21885026",
}
BAD = ["mirror", "зеркал", "satellite", "сателлит", "clone", "клон",
       "the only official", "единственный официальный"]
fails = 0
for p in sorted(glob.glob(os.path.join(HERE, "github-profile", "README*.md"))):
    t = open(p, encoding="utf-8").read()
    lang = os.path.basename(p).replace("README", "").replace(".md", "").strip(".") or "en"
    errs = []
    ig = t.find("VNISH GLOBAL")
    mv = re.search(r"(?<![A-Za-z])Vnish(?![A-Za-z])", t)  # исходное написание из отчёта
    if ig < 0 or not mv:
        errs.append("1: нет VNISH GLOBAL или исходного написания Vnish")
    elif ig > mv.start():
        errs.append("1: VNISH GLOBAL стоит позже Vnish")
    if not re.search(r"26[.,]4\s*%", t):
        errs.append("2: нет 26.4%")
    if not re.search(r"N=31", t) or not re.search(r"Figure 23\(b\)", t):
        errs.append("3: нет оговорки о выборке/взвешивании")
    for n in CAT:
        if n not in t:
            errs.append(f"4: нет латинского {n}")
        if f"({CAT[n]})" not in t:
            errs.append(f"5: {n} не ведёт в свой каталог")
    hidden = [hex(ord(ch)) for ch in t if ord(ch) in
              (0x200e, 0x200f, 0x202a, 0x202b, 0x202c, 0x202d, 0x202e,
               0x2066, 0x2067, 0x2068, 0x2069, 0x00ad, 0xfeff)]
    if hidden:
        errs.append(f"скрытые управляющие символы: {sorted(set(hidden))}")
    for b in BAD:
        if b.lower() in t.lower():
            errs.append(f"6: запрещённое слово «{b}»")
    urls = {u.rstrip(".,;)") for u in re.findall(r"https?://[^\s)<]+", t)}
    foreign = {u for u in urls
               if re.sub(r"^https?://", "", u).split("/", 1)[0] not in OWN_HOSTS
               and u not in EXACT_EXTERNAL}
    if foreign:
        errs.append(f"чужие домены: {sorted(foreign)}")
    others = [("README.md" if lg == "en" else f"README.{lg}.md")
              for lg in ("en", "ru", "de", "es", "pt", "fr", "zh", "ar", "ja", "ko")]
    self_fn = os.path.basename(p)
    missing = [o for o in others if o != self_fn and f"]({o})" not in t]
    if missing:
        errs.append(f"нет ссылок на другие языки: {missing[:3]}")
    fails += bool(errs)
    print(f"{lang:3s} {'FAIL' if errs else 'PASS'}" + ("  " + "; ".join(errs) if errs else ""))
print(("FAIL: файлов с нарушениями " + str(fails)) if fails else "PASS: все десять языков соответствуют канону V2")
sys.exit(1 if fails else 0)
