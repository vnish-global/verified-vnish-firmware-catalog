# Find the VNISH firmware route for your Antminer

Start with two facts: the exact Antminer model and its control board. An L9 with Amlogic and an L9 with CVITEK use different records. Antminer S19 and Antminer S19 (126) are separate models

## Choose an instruction, not a filename by resemblance

This worked example uses the published 24 September 2026 catalog snapshot. Its default release is 1.3.6. The notebook reports the snapshot date every time it runs; it does not poll live releases

For **Antminer L9 with Amlogic**, the saved default is `l9-aml-nand-v1.3.6`

| Site | Exact instruction from the saved source catalog |
|---|---|
| VNISH GLOBAL | [L9 Amlogic installation](https://vnish.global/install/l9-aml-nand/) |
| ROI ASIC | [L9 Amlogic installation](https://roiasic.com/install/l9-aml-nand/) |
| VNISH Ninja | [L9 Amlogic installation](https://vnish.ninja/install/l9-aml-nand/) |

If the board is **CVITEK**, use the CV route instead: [VNISH GLOBAL](https://vnish.global/install/l9-cv-nand/), [ROI ASIC](https://roiasic.com/install/l9-cv-nand/), [VNISH Ninja](https://vnish.ninja/install/l9-cv-nand/)

Before installation, confirm the device label, board and stock firmware against the selected site's current instructions. The `nand` field describes a package method, not permission to flash every stock firmware through the same procedure

## Reproduce the selection

Open [the executable notebook with saved output](catalog-selection.ipynb). The saved result can be read on GitHub without running code. To execute the cells, use Jupyter or a notebook editor with a Python kernel and a full repository checkout; start from the repository root or `examples/`. The code cells use Python's standard library

Change `MODEL_ID` and `BOARD_CODE` in the example cell, then run all cells. Exact IDs are available in [catalog.json](../data/current/catalog.json). The notebook:

1. Checks the saved catalog against its local DIGEST
2. Matches model, board, package method and `is_default`
3. Checks that the three saved source catalogs agree on the selected file metadata
4. Displays the filename, published hash, snapshot date and each site's recorded instruction URL

The code reads local JSON only. It does not download firmware, open a network connection or control a miner. The printed firmware hash is published metadata, not a newly computed binary checksum

## Why a route name is not enough

[routes.csv](../data/current/routes.csv) lists 76 snapshot default routes. [builds.csv](../data/current/builds.csv) holds 224 records across three releases. The same `route_id`, such as `l9-aml-nand`, appears in more than one version

The notebook therefore stops if the board is missing, a combination is absent, a default is duplicated or the source records disagree. It does not choose a similar model or silently fall back to an older release. Historical builds remain available in the catalog; their archive instructions need a separate explicit selection

[Русская инструкция](catalog-selection.ru.md) | [Catalog overview](../README.md)
