# Notes for AI agents

This repository is a public research tree. Follow these rules when reading or proposing changes.

## Read first

1. [llms.txt](llms.txt)
2. [data/index.json](data/index.json)
3. [METHODOLOGY.md](METHODOLOGY.md) for the scoring rules
4. [sources.md](sources.md) for the verification rule
5. Daily numbers from `daily/YYYY-MM-DD.json`, and token scores from `data/reports/<TICKER>.json`, not from memory

## Verification

- Mark a claim **verified** only if it has one Tier A source or is carried by two Tier B outlets.
- Everything else is **unverified**.
- Public contract and mint addresses are fine. Do not add personal wallet addresses.
- Times are in **MST**. Convert source timestamps that are in UTC or another zone.

## Privacy (do not violate)

Do not add:

- Personal names, locations, emails, or anything that identifies a private individual
- Portfolio totals, position sizes, quantities, acquisition costs, profit and loss, cash balances, or second-person wording about a private book
- Private spreadsheet links or identifiers
- Private keys, seed phrases, or exchange credentials

Write market intel: "ROUTER main-pool liquidity was $45,800," not language that implies a reader holds the token.

## Adding a daily report

1. Write `daily/YYYY-MM-DD.json` with `date`, `timezone` (`MST`), `majors`, `watchlist`, `pools`, `hacks`, `news` (each item needs `source` and `verified`), and `calendar`.
2. Write a matching `daily/YYYY-MM-DD.md`.
3. Update `data/index.json`.
4. Add the new paths to `llms.txt`.
5. Run the maintainer's private privacy scrub and keep it green.

## Adding or editing a token note

Keep the sections: what it is, chain and contracts, key risks, recent events, sources. Label unverified items. Do not copy in private dossier headers or portfolio context.

## Adding or updating a v3 scored report

1. Follow [METHODOLOGY.md](METHODOLOGY.md). Do not silently drop a failing report from the ranking; move it only with a dated entry in [DEAD.md](DEAD.md).
2. Write the Markdown under `banking-rails/<TICKER>.md` with v3 front matter.
3. From the repository root, run `python3 scripts/build_data_layer.py` and `python3 scripts/validate_reports.py`. That rebuilds `data/reports/<TICKER>.json` from the published Markdown. Do not hand-edit the JSON to change a score.
4. Run `python3 scripts/build_all_projects.py` so the catalog and ranking overlay stay in sync.
5. Extract **only** git-tracked published reports. Untracked drafts must not be added to `data/reports/`.
6. Selling and Holdings on a new or updated report should go through the dual-review process in the methodology. If the two scores differ by 2 or more points, publish a note from the [RECONCILIATION.md](RECONCILIATION.md) template.
7. Run the maintainer's private privacy scrub and keep it green. Do not add local machine paths, private worksheets, personal names, or portfolio data.
