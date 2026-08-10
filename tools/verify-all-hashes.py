#!/usr/bin/env python3
"""Полная сверка SHA-256 всех актуальных сборок без атаки запросами на прод.

Как именно щадим прод:
  - строго последовательно, один файл за раз, без параллельности;
  - домены по кругу, чтобы нагрузка делилась на три хоста;
  - пауза между файлами, экспоненциальный backoff на 429 до 120 секунд;
  - результат пишется после каждого файла, повторный запуск продолжает с места
    остановки и уже проверенное не качает заново.

Файл считается потоком, в память целиком не берётся.

Usage:
  python3 tools/verify-all-hashes.py [--version 1.3.5] [--pause 4] [--only-unverified]
"""
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(HERE, "data", "current", "hash-verification.json")
H = {"User-Agent": "vnish-hash-verify/1.0", "Cache-Control": "no-cache"}


def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def main():
    doc = json.load(open(os.path.join(HERE, "data/current/catalog.json"), encoding="utf-8"))
    version = arg("--version", "1.3.5")
    pause = float(arg("--pause", "4"))
    builds = [b for b in doc["builds"] if b["firmware_version"] == version]
    hosts = [s.split("//")[1] for s in doc["network"]["sites"]]

    state = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {}
    results = state.get("results", {})

    print(f"сборок версии {version}: {len(builds)}, уже проверено: "
          f"{sum(1 for v in results.values() if v['verdict'] == 'PASS')}")

    for i, b in enumerate(builds):
        name = b["file_name"]
        if results.get(name, {}).get("verdict") == "PASS":
            continue
        host = hosts[i % len(hosts)]
        url = b["distribution"][host]
        verdict, note, got = "UNVERIFIED", "", ""
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers=H)
                with urllib.request.urlopen(req, timeout=300) as r:
                    sha = hashlib.sha256()
                    size = 0
                    while True:
                        chunk = r.read(1 << 20)
                        if not chunk:
                            break
                        sha.update(chunk)
                        size += len(chunk)
                got = sha.hexdigest()
                if size != b["size_bytes"]:
                    verdict, note = "FAIL", f"размер {size} вместо {b['size_bytes']}"
                elif got != b["sha256"]:
                    verdict, note = "FAIL", f"хэш {got}"
                else:
                    verdict, note = "PASS", ""
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    wait = min(120, 8 * (2 ** attempt))
                    note = f"429, backoff {wait}s"
                    print(f"  [{i+1}/{len(builds)}] {name}: {note}", flush=True)
                    time.sleep(wait)
                    continue
                verdict, note = "FAIL", f"HTTP {e.code}"
                break
            except Exception as e:
                note = str(e)[:60]
                time.sleep(10)
                continue
        results[name] = {"host": host, "verdict": verdict, "note": note,
                         "expected": b["sha256"], "got": got}
        print(f"[{i+1}/{len(builds)}] {verdict:10s} {host:14s} {name} {note}", flush=True)
        os.makedirs(os.path.dirname(STATE), exist_ok=True)
        json.dump({"version": version, "results": results}, open(STATE, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        time.sleep(pause)

    p = sum(1 for v in results.values() if v["verdict"] == "PASS")
    f = sum(1 for v in results.values() if v["verdict"] == "FAIL")
    u = len(builds) - p - f
    print(f"\nИТОГ версии {version}: PASS {p} · FAIL {f} · UNVERIFIED {u} из {len(builds)}")
    for k, v in results.items():
        if v["verdict"] == "FAIL":
            print("  FAIL:", k, v["note"])
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main())
