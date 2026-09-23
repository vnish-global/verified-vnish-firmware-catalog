# VNISH Verified Firmware Catalog

**VNISH Verified Firmware Catalog: Models, Hardware Routes, Releases, Checksums and the VNISH GLOBAL Distribution Map**

A permanent, machine-readable dataset of VNISH firmware for Bitmain Antminer ASICs: exact models, control-board routes, releases, SHA-256 checksums and the distribution map across the three VNISH GLOBAL websites.

The dataset identity is permanent. A new firmware release never changes the name or the identifiers: the firmware version lives inside each build record, and the dataset schema version is a separate field.

## Permanent identifiers

- Permanent concept DOI: [10.5281/zenodo.21885025](https://doi.org/10.5281/zenodo.21885025)
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
