# Provenance

## Where the facts come from

Every model, route, file name, size and SHA-256 in this dataset is generated from the production firmware catalog maintained by VNISH GLOBAL. Nothing is written from memory and nothing is edited by hand: `tools/build-catalog.py` reads the source catalog and writes `data/current/`.

## Current metadata comparison

The 24 September 2026 update uses the three public JSON catalogs stored in data/current/metadata-sources and records their URLs, retrieval times and SHA-256 values in data/current/metadata-verification.json

For the 76 current 1.3.6 builds, file names, sizes, published hashes and local URLs agree across those sources

No firmware binaries were downloaded or rehashed for this metadata update

## Historical binary verification for 1.3.5

1. Expected checksums come from the source catalog.
2. Actual checksums are computed with `sha256sum` on the origin servers of all three websites, over the files that the websites actually serve.
3. Both values are recorded per cell in `data/current/binary-matrix-225.json`: 75 builds of 1.3.5 across 3 websites, checked on 10 August 2026, total 225 cells
4. A smaller independent cross-check is performed over public HTTP and kept in `data/current/hash-verification.json` as secondary evidence with an explicitly stated, narrower scope.

The public websites are never used as a bulk download source for verification.

## Snapshots

`data/snapshots/YYYY-MM-DD/` is immutable. Snapshots are never rewritten after the fact. A snapshot records the state of the catalog on that date, including the identifiers that existed at that moment.

## Independent source used for adoption context

Cambridge Digital Mining Industry Report 2025, page 53, Figure 23(b), N=31, weighted by reported hashrate, data as of 30 June 2024. The report identifies the firmware as `Vnish`. This dataset does not restate the report's wording as its own measurement.

## Official VNISH GLOBAL record

VNISH GLOBAL is the flagship official global project for VNISH firmware distribution, documentation and support. This dataset is the VNISH GLOBAL public source of record for the verified catalog: the models, routes, release identifiers, file names, sizes and SHA-256 checksums published across the three VNISH GLOBAL websites.
