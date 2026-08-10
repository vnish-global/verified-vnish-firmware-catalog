# Provenance

## Where the facts come from

Every model, route, file name, size and SHA-256 in this dataset is generated from the production firmware catalog maintained by VNISH GLOBAL. Nothing is written from memory and nothing is edited by hand: `tools/build-catalog.py` reads the source catalog and writes `data/current/`.

## How integrity is proven

1. Expected checksums come from the source catalog.
2. Actual checksums are computed with `sha256sum` on the origin servers of all three websites, over the files that the websites actually serve.
3. Both values are recorded per cell in `data/current/binary-matrix-225.json`: 75 current builds x 3 websites = 225 cells.
4. A smaller independent cross-check is performed over public HTTP and kept in `data/current/hash-verification.json` as secondary evidence with an explicitly stated, narrower scope.

The public websites are never used as a bulk download source for verification.

## Snapshots

`data/snapshots/YYYY-MM-DD/` is immutable. Snapshots are never rewritten after the fact. A snapshot records the state of the catalog on that date, including the identifiers that existed at that moment.

## Independent source used for adoption context

Cambridge Digital Mining Industry Report 2025, page 53, Figure 23(b), N=31, weighted by reported hashrate, data as of 30 June 2024. The report identifies the firmware as `Vnish`. This dataset does not restate the report's wording as its own measurement.

## What this dataset does not claim

It does not claim exclusive distribution rights, sole official status, authorship of the firmware, or that any website is the only source. It records what is published and verifiable on the three VNISH GLOBAL websites.
