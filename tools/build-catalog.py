#!/usr/bin/env python3
"""Сборка постоянной сущности каталога VNISH GLOBAL из боевого каталога прошивок.

Приказ шефа 10.08: каталог больше не привязан к версии 1.3.5. Постоянное имя,
постоянные идентификаторы (GitHub, Zenodo concept DOI, Wikidata Q), внутри -
`data/current/` как актуальное состояние и `data/snapshots/YYYY-MM-DD/` как
неизменяемые исторические снимки. Версия прошивки живёт в строке конкретной
сборки, версия схемы датасета - отдельным полем. Новый релиз прошивки не меняет
имя и идентичность проекта.

Источник фактов один: trunk/api/v1/firmware-catalog.json. Ничего по памяти.

Usage:
  python3 tools/build-catalog.py                 # пересобрать data/current
  python3 tools/build-catalog.py --snapshot      # плюс неизменяемый снимок на сегодня
"""
import csv
import hashlib
import re
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# путь к боевому каталогу задаётся переменной окружения, внутренняя структура
# рабочей машины в публичный репозиторий не попадает
SRC = os.environ.get("VNISH_CATALOG_SRC",
                     os.path.join(HERE, "data", "source", "firmware-catalog.json"))

TITLE = ("VNISH Verified Firmware Catalog: Models, Hardware Routes, Releases, "
         "Checksums and the VNISH GLOBAL Distribution Map")
SCHEMA_VERSION = "1.0.0"
SITES = ["https://vnish.global", "https://vnish.ninja", "https://roiasic.com"]


def load_ids():
    """Постоянные идентификаторы. Пустые значения означают «ещё не создано»."""
    p = os.path.join(HERE, "IDENTIFIERS.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    return {"github": "", "zenodo_concept_doi": "", "wikidata": "Q140965808"}


def build(date=None, release=None, snapshot=False):
    # Дата обязательна: раньше она молча оставалась null и попадала в каталог,
    # манифест и well-known. Берём из параметра или из имени релиза catalog-YYYY-MM-DD.
    if not date and release:
        m = re.fullmatch(r"catalog-(\d{4}-\d{2}-\d{2})", release)
        if m:
            date = m.group(1)
    if not date:
        raise SystemExit("нужна дата: --release catalog-YYYY-MM-DD или явная дата снимка")
    src = json.load(open(SRC, encoding="utf-8"))
    ids = load_ids()
    models = {m["id"]: m for m in src["models"]}

    builds = []
    for b in src["builds"]:
        m = models[b["model_id"]]
        builds.append({
            "build_id": b["id"],
            "model_id": b["model_id"],
            "model_name": m["name"],
            "manufacturer": m.get("manufacturer"),
            "series": m.get("series"),
            "control_board": b["board_platform"]["label"],
            "control_board_code": b["board_platform"]["code"],
            "install_method": b["install_method"],
            "route_id": b["route_id"],
            # версия прошивки - свойство строки сборки, а не всего датасета
            "firmware_version": b["version"],
            "channel": b["channel"],
            "is_default": b.get("is_default", False),
            "superseded_by": b.get("superseded_by"),
            "file_name": b["file_name"],
            "size_bytes": b["size_bytes"],
            "sha256": b["sha256"],
            # карта распространения: файл доступен на каждом сайте сети, на своём хосте
            "distribution": {s.split("//")[1]: s + b["download_path"] for s in SITES},
        })

    versions = sorted({b["firmware_version"] for b in builds}, reverse=True)
    doc = {
        "name": TITLE,
        "short_name": "VNISH Verified Firmware Catalog",
        "dataset_schema_version": SCHEMA_VERSION,
        "release": release or (f"catalog-{date}" if date else None),
        "updated": date,
        "identifiers": {k: v for k, v in ids.items() if v.get("status") == "live"},
        "planned_identifiers": {k: v for k, v in ids.items() if v.get("status") == "planned"},
        "network": {
            "name": "VNISH GLOBAL",
            "sites": SITES,
            "principle": ("Each site publishes the full set of verified builds and serves "
                          "its own downloads. No cross-domain redirects for firmware."),
        },
        "counts": {
            "models": len(models),
            "builds": len(builds),
            "routes": len({b["route_id"] for b in builds}),
            "firmware_versions": versions,
            "builds_by_firmware_version": {
                v: sum(1 for b in builds if b["firmware_version"] == v) for v in versions},
        },
        "license": {"data": "ODC-By-1.0", "documentation": "CC-BY-4.0",
                    "note": "Firmware binaries and trademarks are not licensed by this dataset."},
        "models": [{"model_id": k, **{x: y for x, y in v.items() if x != "id"}}
                   for k, v in models.items()],
        "builds": builds,
    }

    out_dir = os.path.join(HERE, "data", "current")
    if snapshot:
        # дата релиза нужна всегда, а режим снимка задаётся отдельно:
        # раньше эти два понятия были склеены и current молча не пересобирался
        out_dir = os.path.join(HERE, "data", "snapshots", date)
        if os.path.exists(out_dir):
            print(f"снимок {date} уже существует, исторические снимки не переписываются")
            return None
    os.makedirs(out_dir, exist_ok=True)

    payload = json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=False)
    open(os.path.join(out_dir, "catalog.json"), "w", encoding="utf-8").write(payload + "\n")

    cols = ["build_id", "model_id", "model_name", "manufacturer", "series", "control_board",
            "install_method", "route_id", "firmware_version", "channel", "file_name",
            "size_bytes", "sha256"]
    with open(os.path.join(out_dir, "builds.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for b in builds:
            w.writerow(b)

    # routes.csv - проекция ТЕКУЩИХ сборок. Текущая определяется признаком is_default,
    # а не номером версии: следующий релиз не требует правки кода.
    rcols = ["route_id", "model_id", "model_name", "control_board", "control_board_code",
             "install_method", "firmware_version", "file_name", "sha256", "size_bytes"]
    current = [b for b in builds if b.get("is_default")]
    with open(os.path.join(out_dir, "routes.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rcols, extrasaction="ignore")
        w.writeheader()
        for b in sorted(current, key=lambda x: x["route_id"]):
            w.writerow(b)

    # digest считаем по БАЙТАМ файла на диске, иначе он не совпадёт с тем,
    # что посчитает любой проверяющий через sha256sum catalog.json
    cat_path = os.path.join(out_dir, "catalog.json")
    digest = hashlib.sha256(open(cat_path, "rb").read()).hexdigest()
    open(os.path.join(out_dir, "DIGEST"), "w").write(digest + "  catalog.json\n")
    manifest = {
        "release": doc["release"],
        "updated": doc["updated"],
        "dataset_schema_version": SCHEMA_VERSION,
        "counts": doc["counts"],
        "current_builds": len(current),
        "files": {},
    }
    for fn in ("catalog.json", "builds.csv", "routes.csv"):
        fp = os.path.join(out_dir, fn)
        manifest["files"][fn] = {
            "sha256": hashlib.sha256(open(fp, "rb").read()).hexdigest(),
            "size_bytes": os.path.getsize(fp)}
    json.dump(manifest, open(os.path.join(out_dir, "RELEASE-MANIFEST.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print(f"{out_dir}: моделей {len(models)}, сборок {len(builds)}, "
          f"версий {','.join(versions)}, digest {digest[:16]}")
    return digest


if __name__ == "__main__":
    rel = sys.argv[sys.argv.index("--release") + 1] if "--release" in sys.argv else None
    if not rel:
        sys.exit("укажи релиз: --release catalog-YYYY-MM-DD")
    d = build(release=rel)
    if "--snapshot" in sys.argv:
        date = [a for a in sys.argv if a.startswith("2")][0] if any(
            a.startswith("2") for a in sys.argv) else None
        if not date:
            sys.exit("укажи дату снимка явно: --snapshot 2026-08-10")
        build(date, release=rel or f"catalog-{date}", snapshot=True)
