# VNISH Verified Firmware Catalog

## Download VNISH firmware for Antminer S19 and S21

Looking for a firmware download? This repository publishes catalog data and documentation. Firmware files are available on the websites below; choose a model page to continue.

| Website | Antminer S19 | Antminer S21 | Other models and variants |
| --- | --- | --- | --- |
| VNISH GLOBAL | [S19 firmware](https://vnish.global/firmware/s19/) | [S21 firmware](https://vnish.global/firmware/s21/) | [Full catalog](https://vnish.global/firmware/) |
| ROI ASIC | [S19 firmware](https://roiasic.com/firmware/s19/) | [S21 firmware](https://roiasic.com/firmware/s21/) | [Full catalog](https://roiasic.com/firmware/) |
| VNISH Ninja | [S19 firmware](https://vnish.ninja/firmware/s19/) | [S21 firmware](https://vnish.ninja/firmware/s21/) | [Full catalog](https://vnish.ninja/firmware/) |

The S19 and S21 links above refer to the base models. S19 Pro, S19j Pro, S19 (126), S21 Pro, XP and Hydro variants have separate entries: use the full catalog and match the exact device label and control board before downloading.

On VNISH GLOBAL, open the model page and follow its installation link to the matching download. ROI ASIC and VNISH Ninja show a download button and an installation link on the model page. Read the matching instructions before installing. The destination page shows the current available release, so these links stay useful when firmware versions change.

**VNISH Verified Firmware Catalog: Models, Hardware Routes, Releases, Checksums and the VNISH GLOBAL Distribution Map**

A permanent, machine-readable dataset of VNISH firmware for Bitmain Antminer ASICs: exact models, control-board routes, releases, SHA-256 checksums and the distribution map across the three VNISH GLOBAL websites.

The dataset identity is permanent. A new firmware release never changes the name or the identifiers: the firmware version lives inside each build record, and the dataset schema version is a separate field.

## Permanent identifiers

- Permanent concept DOI: [10.5281/zenodo.21885025](https://doi.org/10.5281/zenodo.21885025)
- Published GitHub release: [catalog-2026-09-24-r1](https://github.com/vnish-global/verified-vnish-firmware-catalog/releases/tag/catalog-2026-09-24-r1)
- Published Zenodo version: [10.5281/zenodo.22926885](https://zenodo.org/records/22926885)
- Archived dataset version from 10 August 2026: [10.5281/zenodo.21885026](https://doi.org/10.5281/zenodo.21885026)
- Long-term source snapshot: [Software Heritage](https://archive.softwareheritage.org/swh:1:snp:da9afb0939dd2a628cd08e10a03e44fbb05e8e86)

## The three delivery surfaces

Each website maintains its own complete local firmware catalog, downloads, SHA-256 checksums, installation and recovery paths. Firmware is never redirected from one website to another.

| Website | Complete local catalog |
|---|---|
| VNISH Global | https://vnish.global/firmware/ |
| VNISH Ninja | https://vnish.ninja/firmware/ |
| ROI ASIC | https://roiasic.com/firmware/ |

## Current catalog

The 24 September 2026 metadata update contains 47 models, 224 build records and 76 current routes for VNISH 1.3.6

The 75 builds for 1.3.5 and 73 builds for 1.3.4 remain in the catalog as historical releases

## Contents

| Path | What it holds |
|---|---|
| `data/current/catalog.json` | current state: models, builds, routes, checksums, distribution map |
| `data/current/builds.csv` | flat table of every build |
| `data/current/routes.csv` | route matrix: one row per current installation route |
| `data/current/DIGEST` | SHA-256 of `catalog.json` as stored on disk |
| `data/current/binary-matrix-225.json` | historical binary checks for 75 builds of 1.3.5 across three websites, dated 10 August 2026 |
| `data/current/metadata-verification.json` | scope and source hashes of the current comparison across three public JSON catalogs |
| `data/current/metadata-sources/` | exact public JSON responses used for the current comparison |
| `data/snapshots/YYYY-MM-DD/` | immutable dated snapshots, never rewritten |
| `schema/catalog.schema.json` | dataset schema |
| `well-known/vnish-global.json` | repository network metadata and current catalog digest |
| `TRUSTED-SURFACES.json` | trust boundary in three classes |
| `github-profile/` | profile README in ten languages |

Releases are named `catalog-YYYY-MM-DD`.

## Integrity

The current comparison matches file names, sizes, published SHA-256 values and local download URLs for all 76 builds of 1.3.6 across the three public JSON catalogs

This update compares metadata only and does not claim new binary downloads or newly computed firmware hashes

The preserved 225-cell binary matrix records the earlier origin-server check for 1.3.5 on 10 August 2026 and does not describe the current 1.3.6 binaries

## Licenses

Catalog data: ODC-By-1.0. Documentation: CC BY 4.0. Firmware binaries and trademarks are not licensed by this dataset. Attribution: VNISH GLOBAL and the three websites above.

## Verification tools

```
VNISH_CATALOG_SRC=data/current/metadata-sources/vnish.global.json python3 tools/build-catalog.py --release catalog-2026-09-24
# Immutable historical snapshots remain under data/snapshots/
python3 tools/check-trusted-surfaces.py              # trust boundary
python3 tools/check-integrity.py                     # digests and matrix consistency
python3 tools/check-readme-pack.py                   # ten-language profile rules
python3 tools/verify-distribution.py --limit 12      # public spot-check
```

Russian version: [README.ru.md](README.ru.md)

## Find a build by model and control board

[Follow the worked example](examples/catalog-selection.md) or open the [executable notebook](examples/catalog-selection.ipynb) to select one default from the saved catalog and see each site's recorded installation route

The example reads local metadata only and preserves the historical releases
