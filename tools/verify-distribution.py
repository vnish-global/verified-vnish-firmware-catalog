#!/usr/bin/env python3
"""Проверяет карту распространения: файл каждой сборки доступен на каждом сайте сети.

Правило шефа: загрузки Ninja остаются на Ninja, ROI на ROI, Global на Global.
Значит утверждение «полный набор на каждом» обязано быть правдой побайтово.
HEAD сверяет статус и размер с каталогом; --full N дополнительно качает N файлов
на домен и сверяет SHA-256. Между запросами пауза: хостинг отдаёт 429 на пачку.

Usage: python3 tools/verify-distribution.py [--version 1.3.5] [--limit N] [--full N]
"""
import hashlib, json, os, sys, time, urllib.error, urllib.request
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
doc = json.load(open(os.path.join(HERE, "data/current/catalog.json"), encoding="utf-8"))
# текущая сборка определяется признаком is_default, номер версии не зашит
ver = sys.argv[sys.argv.index("--version") + 1] if "--version" in sys.argv else None
limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 0
full = int(sys.argv[sys.argv.index("--full") + 1]) if "--full" in sys.argv else 0
H = {"User-Agent": "vnish-verify-distribution", "Cache-Control": "no-cache"}
builds = ([b for b in doc["builds"] if b["firmware_version"] == ver] if ver
          else [b for b in doc["builds"] if b.get("is_default")])
ver = ver or "current (is_default)"
if limit:
    builds = builds[:limit]
bad, ok, ratelimited, unchecked = [], 0, 0, []
for b in builds:
    for host, url in b["distribution"].items():
        done = False
        for attempt in range(3):
            try:
                r = urllib.request.urlopen(urllib.request.Request(url, headers=H, method="HEAD"), timeout=40)
                size = int(r.headers.get("Content-Length") or 0)
                if size != b["size_bytes"]:
                    bad.append((host, b["file_name"], f"размер {size} вместо {b['size_bytes']}"))
                else:
                    ok += 1
                done = True
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    ratelimited += 1
                    time.sleep(4 + attempt * 4)
                    continue
                bad.append((host, b["file_name"], f"HTTP {e.code}"))
                done = True
                break
            except Exception as e:
                bad.append((host, b["file_name"], str(e)[:40]))
                done = True
                break
        if not done:
            # ретраи исчерпаны: это НЕ «проверено», молча терять такие пары нельзя
            unchecked.append((host, b["file_name"], "лимит запросов, не проверено"))
        time.sleep(0.7)
print(f"версия {ver}: проверено пар файл-домен {ok + len(bad)}, совпало {ok}, "
      f"расхождений {len(bad)}, не проверено из-за лимита {len(unchecked)}, "
      f"попаданий в лимит {ratelimited}")
for x in unchecked[:10]:
    print("  НЕ ПРОВЕРЕНО:", x)
for x in bad[:10]:
    print("  ", x)
if full:
    print(f"\nполная сверка SHA-256, по {full} файлов на домен:")
    for host in doc["network"]["sites"]:
        h = host.split("//")[1]
        for b in builds[:full]:
            url = b["distribution"][h]
            try:
                data = urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=180).read()
                got = hashlib.sha256(data).hexdigest()
                print(f"  {h:14s} {b['file_name']:44s} {'СОВПАЛ' if got == b['sha256'] else 'РАСХОЖДЕНИЕ ' + got[:16]}")
            except Exception as e:
                print(f"  {h:14s} {b['file_name']:44s} ошибка {str(e)[:40]}")
            time.sleep(1)
sys.exit(1 if bad else 0)
