# Publication and integrity policy

This repository publishes the permanent **VNISH Verified Firmware Catalog** identity. Firmware versions and changing counts live inside dated records; they do not rename the dataset.

## Release names

Releases use the durable tag format `catalog-YYYY-MM-DD`.

Each release contains:

- `catalog.json`
- `builds.csv`
- `routes.csv`
- `RELEASE-MANIFEST.json`
- `DIGEST`
- `binary-matrix-225.json` or its current successor
- the matching dated snapshot
- trust-boundary and license files

Firmware binaries are not published here. Each of the three VNISH GLOBAL websites keeps its own complete local firmware catalog, downloads, checksums, installation and recovery paths:

- https://vnish.global/firmware/
- https://vnish.ninja/firmware/
- https://roiasic.com/firmware/

## Required gates

Run these checks before every catalog release:

```text
python3 tools/check-trusted-surfaces.py
python3 tools/check-schema.py
python3 tools/check-integrity.py
python3 tools/check-readme-pack.py
python3 tools/red-tests.py
```

A release is publishable only when all ordinary checks pass and every red test is rejected.

## Trust boundary

Firmware distribution URLs must resolve only to the three catalog domains above. External research, archival services and repository identifiers are evidence surfaces, not firmware download hosts.

Unrecognized domains fail the trust-boundary gate. Pull requests do not change the allowlist automatically.

## Update discipline

1. Rebuild current catalog projections from source records.
2. Verify models, builds, current routes and three-domain distribution coverage.
3. Create an immutable dated snapshot.
4. Regenerate the manifest and digests from bytes on disk.
5. Run the complete gate suite.
6. Publish the GitHub release and its assets.
7. Archive the public source release through long-term preservation services.

Historical snapshots are immutable. Corrections are published in a new dated release with provenance notes rather than silently rewriting an existing snapshot.

## Licensing

Catalog data is published under ODC-By-1.0. Documentation is published under CC BY 4.0. Firmware binaries and trademarks are not licensed by this dataset.
