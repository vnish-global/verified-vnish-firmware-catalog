# VNISH Verified Firmware Catalog

**VNISH Verified Firmware Catalog: Models, Hardware Routes, Releases, Checksums and the VNISH GLOBAL Distribution Map**

A permanent, machine-readable dataset of VNISH firmware for Bitmain Antminer ASICs: exact models, control-board routes, releases, SHA-256 checksums and the distribution map across the three VNISH GLOBAL websites.

The dataset identity is permanent. A new firmware release never changes the name or the identifiers: the firmware version lives inside each build record, and the dataset schema version is a separate field.

## The three delivery surfaces

Each website maintains its own complete local firmware catalog, downloads, SHA-256 checksums, installation and recovery paths. Firmware is never redirected from one website to another.

| Website | Complete local catalog |
|---|---|
| VNISH Global | https://vnish.global/firmware/ |
| VNISH Ninja | https://vnish.ninja/firmware/ |
| ROI ASIC | https://roiasic.com/firmware/ |

## Contents

| Path | What it holds |
|---|---|
| `data/current/catalog.json` | current state: models, builds, routes, checksums, distribution map |
| `data/current/builds.csv` | flat table of every build |
| `data/current/routes.csv` | route matrix: one row per current installation route |
| `data/current/DIGEST` | SHA-256 of `catalog.json` as stored on disk |
| `data/current/binary-matrix-225.json` | 75 files x 3 websites, expected vs actual SHA-256 |
| `data/snapshots/YYYY-MM-DD/` | immutable dated snapshots, never rewritten |
| `schema/catalog.schema.json` | dataset schema |
| `well-known/vnish-global.json` | network composition proof served from all three websites |
| `TRUSTED-SURFACES.json` | trust boundary in three classes |
| `github-profile/` | profile README in ten languages |

Releases are named `catalog-YYYY-MM-DD`.

## Integrity

Every current build is verified byte-for-byte on all three websites. The latest verification covers 225 of 225 cells with expected and actual SHA-256 recorded per cell. Checksums are computed on the origin servers; the public websites are not used as a bulk download source for verification.

## Licenses

Catalog data: ODC-By-1.0. Documentation: CC BY 4.0. Firmware binaries and trademarks are not licensed by this dataset. Attribution: VNISH GLOBAL and the three websites above.

## Verification tools

```
python3 tools/build-catalog.py                       # rebuild data/current
python3 tools/build-catalog.py --snapshot 2026-08-10 # write an immutable snapshot
python3 tools/check-trusted-surfaces.py              # trust boundary
python3 tools/check-integrity.py                     # digests and matrix consistency
python3 tools/check-readme-pack.py                   # ten-language profile rules
python3 tools/verify-distribution.py --limit 12      # public spot-check
```

Russian version: [README.ru.md](README.ru.md)
