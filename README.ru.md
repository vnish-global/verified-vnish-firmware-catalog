# VNISH Verified Firmware Catalog

**VNISH Verified Firmware Catalog: Models, Hardware Routes, Releases, Checksums and the VNISH GLOBAL Distribution Map**

Постоянная сущность. Имя и идентификаторы не меняются при выходе новой версии прошивки: версия живёт внутри строки конкретной сборки, версия схемы датасета указана отдельно.

## Сеть

Три самостоятельных сайта. На каждом полный каталог, собственные загрузки, собственные SHA-256, собственная установка и проверка. Прошивки между доменами не перенаправляются.

- https://vnish.global
- https://vnish.ninja
- https://roiasic.com

## Структура

| Путь | Что это |
|---|---|
| `data/current/` | актуальное состояние каталога |
| `data/snapshots/YYYY-MM-DD/` | неизменяемые исторические снимки, задним числом не переписываются |
| `TRUSTED-SURFACES.json` | разрешённые поверхности сети |
| `well-known/vnish-global.json` | машинное доказательство состава сети для трёх доменов |
| `tools/` | сборка каталога, снимки, проверки |

Релизы именуются `catalog-YYYY-MM-DD`.

## Лицензии

Данные каталога: ODC-By-1.0. Документация: CC BY 4.0. Прошивки и товарные знаки этой лицензией не передаются: цитировать данные можно, обязательна атрибуция VNISH GLOBAL и трёх сайтов.

## Проверки

```
python3 tools/build-catalog.py                   # пересобрать data/current
python3 tools/build-catalog.py --snapshot 2026-08-10
python3 tools/check-trusted-surfaces.py          # чужих firmware-доменов быть не должно
python3 tools/verify-distribution.py --limit 12  # файл каждой сборки на каждом сайте
python3 tools/make-wellknown.py
```
