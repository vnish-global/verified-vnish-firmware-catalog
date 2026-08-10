#!/usr/bin/env python3
"""CI: цифры пакета не могут противоречить друг другу и подделываться.

Понятие «текущая сборка» берётся из `is_default == true`, а не из номера версии:
новый релиз прошивки не требует правки кода.

Проверяется:
  1. DIGEST совпадает с байтами catalog.json в current и в каждом снимке;
  2. digest в well-known равен digest текущего каталога;
  3. len(cells) == cells_expected == cells_computed, счётчики пересчитываются из cells;
  4. набор доменов матрицы точно равен network.sites;
  5. на каждом домене ровно один уникальный файл на каждую текущую сборку, дублей нет;
  6. expected каждой ячейки равен SHA соответствующей сборки в catalog.json;
  7. actual == expected, match == true, verdict == PASS;
  8. builds.csv - точная проекция всех build-записей;
  9. routes.csv - точная проекция всех is_default записей;
 10. частичная выборка помечена как вторичная.
"""
import csv
import glob
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errs = []


def digest_of(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def load(p):
    return json.load(open(p, encoding="utf-8"))


cur_dir = os.path.join(HERE, "data/current")
doc = load(os.path.join(cur_dir, "catalog.json"))
sites = [s.split("//")[1] for s in doc["network"]["sites"]]
current = [b for b in doc["builds"] if b.get("is_default")]

# 1. digest в current и снимках
for d in [cur_dir] + sorted(glob.glob(os.path.join(HERE, "data/snapshots/*"))):
    cat, dg = os.path.join(d, "catalog.json"), os.path.join(d, "DIGEST")
    if not os.path.exists(cat):
        continue
    want = open(dg).read().split()[0] if os.path.exists(dg) else None
    got = digest_of(cat)
    if want != got:
        errs.append(f"DIGEST не совпадает в {os.path.relpath(d, HERE)}: записано {want}, факт {got}")

# 2. well-known
wk = os.path.join(HERE, "well-known/vnish-global.json")
if os.path.exists(wk):
    if load(wk)["catalog"].get("digest_sha256") != digest_of(os.path.join(cur_dir, "catalog.json")):
        errs.append("digest в well-known не равен digest каталога")

# 3-7. матрица
m = load(os.path.join(cur_dir, "binary-matrix-225.json"))
cells = m.get("cells", [])
expect = len(current) * len(sites)
if not (len(cells) == m.get("cells_expected") == m.get("cells_computed") == expect):
    errs.append(f"матрица: ячеек в файле {len(cells)}, заголовок "
                f"{m.get('cells_expected')}/{m.get('cells_computed')}, ожидалось {expect}")
if {c.get("domain") for c in cells} != set(sites):
    errs.append(f"домены матрицы не равны сети: {sorted({c.get('domain') for c in cells})}")

by_sha = {b["file_name"]: b["sha256"] for b in current}
seen = set()
for c in cells:
    key = (c.get("domain"), c.get("file"))
    if key in seen:
        errs.append(f"дубль ячейки: {key}")
        break
    seen.add(key)
    exp = by_sha.get(c.get("file"))
    if exp is None:
        errs.append(f"в матрице файл вне текущих сборок: {c.get('file')}")
        break
    if c.get("expected_sha256") != exp:
        errs.append(f"expected не равен каталогу: {c.get('file')} на {c.get('domain')}")
        break
    if c.get("actual_sha256") != c.get("expected_sha256") or not c.get("match") \
            or c.get("verdict") != "PASS":
        errs.append(f"ячейка не подтверждена: {c.get('domain')} {c.get('file')}")
        break
for d in sites:
    files = [c["file"] for c in cells if c.get("domain") == d]
    if len(files) != len(current) or set(files) != set(by_sha):
        errs.append(f"на домене {d} покрытие не полное: {len(files)} из {len(current)}")

p = sum(1 for c in cells if c.get("verdict") == "PASS")
f = sum(1 for c in cells if c.get("verdict") == "FAIL")
if m.get("pass") != p or m.get("fail") != f or m.get("unverified") != expect - len(cells):
    errs.append(f"счётчики в заголовке не сходятся с ячейками: заявлено "
                f"{m.get('pass')}/{m.get('fail')}, факт {p}/{f}")

# 8-9. CSV как точные проекции
def csv_rows(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def compare_rows(rows, records, key, fields, label):
    """CSV обязан совпадать с каталогом по СОДЕРЖИМОМУ, а не по одному идентификатору:
    подмена SHA внутри csv раньше проходила гейт насквозь."""
    by_key = {r[key]: r for r in records}
    if sorted(r[key] for r in rows) != sorted(by_key):
        errs.append(f"{label}: набор {key} не совпадает с каталогом "
                    f"({len(rows)} строк против {len(by_key)} записей)")
        return
    for r in rows:
        rec = by_key[r[key]]
        for f in fields:
            if str(r.get(f, "")) != str(rec.get(f, "")):
                errs.append(f"{label}: строка {r[key]} расходится по полю {f}: "
                            f"в csv {r.get(f)!r}, в каталоге {rec.get(f)!r}")
                return


b_csv = os.path.join(cur_dir, "builds.csv")
r_csv = os.path.join(cur_dir, "routes.csv")
if not os.path.exists(r_csv):
    errs.append("нет routes.csv")
else:
    fields = ["model_id", "route_id", "firmware_version", "file_name", "sha256", "size_bytes"]
    compare_rows(csv_rows(b_csv), doc["builds"], "build_id", fields, "builds.csv")
    rrows = csv_rows(r_csv)
    compare_rows(rrows, current, "route_id",
                 ["model_id", "firmware_version", "file_name", "sha256", "size_bytes"], "routes.csv")
    if len({r["route_id"] for r in rrows}) != len(current):
        errs.append(f"routes.csv: уникальных маршрутов {len({r['route_id'] for r in rrows})}, "
                    f"текущих сборок {len(current)}")

# манифест релиза: даты не null, хэши и размеры совпадают с файлами на диске
man_p = os.path.join(cur_dir, "RELEASE-MANIFEST.json")
if not os.path.exists(man_p):
    errs.append("нет RELEASE-MANIFEST.json")
else:
    man = load(man_p)
    for k in ("release", "updated"):
        if not man.get(k):
            errs.append(f"в манифесте пустое поле {k}")
        if not doc.get(k):
            errs.append(f"в каталоге пустое поле {k}")
    if man.get("release") != doc.get("release") or man.get("updated") != doc.get("updated"):
        errs.append("манифест и каталог расходятся по release/updated")
    for fn, meta in man.get("files", {}).items():
        fp = os.path.join(cur_dir, fn)
        if not os.path.exists(fp):
            errs.append(f"манифест ссылается на отсутствующий файл {fn}")
            continue
        if digest_of(fp) != meta.get("sha256"):
            errs.append(f"манифест: SHA файла {fn} не совпадает с фактическим")
        if os.path.getsize(fp) != meta.get("size_bytes"):
            errs.append(f"манифест: размер файла {fn} не совпадает с фактическим")
    for need in ("catalog.json", "builds.csv", "routes.csv"):
        if need not in man.get("files", {}):
            errs.append(f"манифест не покрывает {need}")

if os.path.exists(wk) and load(wk).get("updated") != doc.get("updated"):
    errs.append("well-known и каталог расходятся по updated")

# codemeta обещает ассеты релиза: они обязаны существовать и быть покрыты манифестом
cm = os.path.join(HERE, "codemeta.json")
if os.path.exists(cm):
    promised = [d["contentUrl"].rsplit("/", 1)[-1] for d in load(cm).get("distribution", [])]
    man_files = set(load(man_p).get("files", {})) if os.path.exists(man_p) else set()
    for fn in promised:
        if not os.path.exists(os.path.join(cur_dir, fn)):
            errs.append(f"codemeta обещает файл, которого нет: {fn}")
        elif fn not in man_files:
            errs.append(f"codemeta обещает {fn}, но манифест релиза его не покрывает")

# 10. вторичная выборка
hv = os.path.join(cur_dir, "hash-verification.json")
if os.path.exists(hv):
    h = load(hv)
    if "superseded_by" not in h or "scope" not in h:
        errs.append("частичная выборка не помечена как вторичная")

if doc["counts"]["models"] != len(doc["models"]) or doc["counts"]["builds"] != len(doc["builds"]):
    errs.append("счётчики каталога не совпадают с содержимым")

if errs:
    print("FAIL:")
    for e in errs:
        print("  ", e)
    sys.exit(1)
print(f"PASS: моделей {doc['counts']['models']} · сборок {len(doc['builds'])} · "
      f"текущих сборок {len(current)} · матрица {p}/{expect} · CSV сходятся")
