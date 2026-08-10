#!/usr/bin/env python3
"""CI: catalog.json обязан соответствовать schema/catalog.schema.json.

Валидатор без внешних зависимостей: проверяет ровно то, что схема требует,
чтобы CI не зависел от установки пакетов на раннере.
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
doc = json.load(open(os.path.join(HERE, "data/current/catalog.json"), encoding="utf-8"))
sch = json.load(open(os.path.join(HERE, "schema/catalog.schema.json"), encoding="utf-8"))
errs = []
for k in sch["required"]:
    if k not in doc:
        errs.append(f"нет обязательного поля {k}")
c = doc.get("counts", {})
for k in ("models", "builds", "routes"):
    if not isinstance(c.get(k), int) or c[k] < 1:
        errs.append(f"counts.{k} должен быть целым числом больше нуля, получено {c.get(k)!r}")
sites = sch["properties"]["builds"]["items"]["properties"]["distribution"]["propertyNames"]["enum"]
for b in doc.get("builds", []):
    if not re.fullmatch(r"[0-9a-f]{64}", b.get("sha256", "")):
        errs.append(f"неверный SHA-256 у {b.get('build_id')}: {b.get('sha256')!r}")
        break
    if not isinstance(b.get("size_bytes"), int) or b["size_bytes"] < 1:
        errs.append(f"неверный size_bytes у {b.get('build_id')}")
        break
    d = b.get("distribution", {})
    if len(d) != 3 or set(d) != set(sites):
        errs.append(f"distribution у {b.get('build_id')} должен содержать ровно три хоста сети, получено {sorted(d)}")
        break
if doc.get("network", {}).get("name") != "VNISH GLOBAL":
    errs.append("network.name должен быть VNISH GLOBAL")
if errs:
    print("FAIL по схеме:")
    for e in errs:
        print("  ", e)
    sys.exit(1)
print(f"PASS по схеме: {len(doc['builds'])} сборок, SHA-256 64 символа, distribution ровно из трёх хостов")
