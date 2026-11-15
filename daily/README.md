# Daily market intel

One report per date, in two files:

- `YYYY-MM-DD.md` — readable brief
- `YYYY-MM-DD.json` — machine-readable tape

Times are in **MST**. These are public market snapshots (CoinGecko, DexScreener, DefiLlama Hacks, vetted RSS) plus, for some later dates, a desk compilation of public prints and confirmed headlines.

JSON fields: `date`, `timezone`, `as_of`, `source`, `majors`, `watchlist`, `pools`, `hacks`, `news` (each item has `source` and `verified`), `calendar`, and optional `market_notes`.

A news item is `verified: true` only when it has a Tier A source or was corroborated by a second Tier B outlet. Everything else is unverified.

Dates with no file are dates without a saved public snapshot, not a claim that nothing happened.

Research only. Not financial advice. Not a fiduciary.

See [data/index.json](../data/index.json) for the full list.
