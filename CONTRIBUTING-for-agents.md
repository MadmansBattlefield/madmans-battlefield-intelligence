# Notes for AI agents

This repository is a public research tree. Follow these rules when reading or proposing changes.

## Read first

1. [llms.txt](llms.txt)
2. [data/index.json](data/index.json)
3. [sources.md](sources.md) for the verification rule
4. Daily numbers from `daily/YYYY-MM-DD.json`, not from memory

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
