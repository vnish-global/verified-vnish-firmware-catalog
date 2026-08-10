#!/usr/bin/env python3
"""Красные тесты: каждый обязан валить гейт ненулевым кодом.

Проверяем ровно те подмены, на которых гейт раньше давал ложный зелёный.
Работаем на копии дерева, оригинал не трогаем.
"""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(root):
    r = subprocess.run([sys.executable, os.path.join(root, "tools/check-integrity.py")],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else ""


def mutate(name, fn):
    tmp = tempfile.mkdtemp(prefix="vnish-red-")
    root = os.path.join(tmp, "repo")
    shutil.copytree(HERE, root, ignore=shutil.ignore_patterns(".git"))
    fn(root)
    code, last = run(root)
    shutil.rmtree(tmp, ignore_errors=True)
    ok = code != 0
    print(f"  {'OK ' if ok else 'ПРОВАЛ'} {name}: код {code} · {last[:90]}")
    return ok


def load(root, rel):
    return json.load(open(os.path.join(root, rel), encoding="utf-8"))


def save(root, rel, d):
    json.dump(d, open(os.path.join(root, rel), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


M = "data/current/binary-matrix-225.json"


def t_deleted(root):
    d = load(root, M); d["cells"].pop(0); save(root, M, d)


def t_duplicated(root):
    d = load(root, M); d["cells"][1] = dict(d["cells"][0]); save(root, M, d)


def t_fake_pair(root):
    d = load(root, M); z = "0" * 64
    d["cells"][0]["expected_sha256"] = z; d["cells"][0]["actual_sha256"] = z; save(root, M, d)


def t_foreign_domain(root):
    d = load(root, M); d["cells"][0]["domain"] = "vnish.com"; save(root, M, d)


def t_fake_counters(root):
    d = load(root, M); d["pass"] = 999; save(root, M, d)


def t_future_release(root):
    """Появилась default-сборка новой версии, а доказательства остались старые.
    Гейт обязан это заметить БЕЗ правки кода: текущая сборка берётся из is_default."""
    import hashlib
    p = os.path.join(root, "data/current/catalog.json")
    d = json.load(open(p, encoding="utf-8"))
    old = [b for b in d["builds"] if b.get("is_default")][0]
    new = dict(old)
    new["build_id"] = old["route_id"] + "-vNEXT"
    new["firmware_version"] = "9.9.9"
    new["file_name"] = old["file_name"].replace(old["firmware_version"], "9.9.9")
    new["sha256"] = "a" * 64
    new["is_default"] = True
    for b in d["builds"]:
        if b["build_id"] == old["build_id"]:
            b["is_default"] = False
    d["builds"].append(new)
    d["counts"]["builds"] = len(d["builds"])
    open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    open(os.path.join(root, "data/current/DIGEST"), "w").write(
        hashlib.sha256(open(p, "rb").read()).hexdigest() + "  catalog.json\n")


def t_stale_routes(root):
    p = os.path.join(root, "data/current/routes.csv")
    lines = open(p, encoding="utf-8").read().splitlines()
    open(p, "w", encoding="utf-8").write("\n".join(lines[:-1]) + "\n")


def t_csv_sha(root):
    """Подмена SHA внутри builds.csv: раньше проходила гейт, потому что сверялись только ID."""
    fp = os.path.join(root, "data/current/builds.csv")
    lines = open(fp, encoding="utf-8").read().splitlines()
    parts = lines[1].split(",")
    parts[-1] = "b" * 64
    lines[1] = ",".join(parts)
    open(fp, "w", encoding="utf-8").write("\n".join(lines) + "\n")


def t_csv_sha_with_manifest(root):
    """Самый коварный случай: SHA подменён в builds.csv И манифест пересчитан под него.
    Поймать может только сверка содержимого csv с каталогом."""
    import hashlib
    fp = os.path.join(root, "data/current/builds.csv")
    lines = open(fp, encoding="utf-8").read().splitlines()
    parts = lines[1].split(",")
    parts[-1] = "d" * 64
    lines[1] = ",".join(parts)
    open(fp, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    mp = os.path.join(root, "data/current/RELEASE-MANIFEST.json")
    m = json.load(open(mp, encoding="utf-8"))
    m["files"]["builds.csv"] = {"sha256": hashlib.sha256(open(fp, "rb").read()).hexdigest(),
                                "size_bytes": os.path.getsize(fp)}
    json.dump(m, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def t_manifest_hash(root):
    """Манифест обещает не тот хэш, что у файла на диске."""
    fp = os.path.join(root, "data/current/RELEASE-MANIFEST.json")
    m = json.load(open(fp, encoding="utf-8"))
    m["files"]["builds.csv"]["sha256"] = "c" * 64
    json.dump(m, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def t_null_updated(root):
    """Пустая дата в каталоге: именно она молча уезжала в манифест и well-known."""
    fp = os.path.join(root, "data/current/catalog.json")
    d = json.load(open(fp, encoding="utf-8"))
    d["updated"] = None
    open(fp, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    import hashlib
    open(os.path.join(root, "data/current/DIGEST"), "w").write(
        hashlib.sha256(open(fp, "rb").read()).hexdigest() + "  catalog.json\n")


print("красные тесты целостности:")
results = [
    mutate("удалённая ячейка", t_deleted),
    mutate("дублированная ячейка", t_duplicated),
    mutate("выдуманный парный SHA (64 нуля)", t_fake_pair),
    mutate("чужой домен в матрице", t_foreign_domain),
    mutate("подделанные счётчики", t_fake_counters),
    mutate("устаревший routes.csv", t_stale_routes),
    mutate("будущий релиз со старыми доказательствами", t_future_release),
    mutate("подменённый SHA внутри builds.csv", t_csv_sha),
    mutate("подменённый SHA в csv + пересчитанный манифест", t_csv_sha_with_manifest),
    mutate("манифест обещает чужой хэш", t_manifest_hash),
    mutate("пустая дата updated", t_null_updated),
]
print(f"\n{'PASS' if all(results) else 'FAIL'}: {sum(results)} из {len(results)} подмен отклонены гейтом")
sys.exit(0 if all(results) else 1)
