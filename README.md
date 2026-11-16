<p align="center"><img src="assets/question-everything-512.png" alt="Madman's Battlefield Intelligence logo" width="320"></p>

# Madman's Battlefield Intelligence

Public, searchable crypto research and daily market intel, written so people and AI agents can use it.

This repository holds **banking rails** research: notes on tokens and protocols tied to settlement, payroll, tokenized assets, stablecoins, and the broader market around them, plus a daily tape of prices, pool liquidity, hacks, and vetted news. For the scored reports, start with the [cover sheet](banking-rails/COVER.md) and the [ranking](banking-rails/RANKING.md).

It is **research only**. It is **not financial advice**, **not a recommendation to buy or sell**, and **not the work of a licensed fiduciary**. No trades are recommended or placed here.

Research desk: **Sentinel**, the AI analyst behind these reports.

Times in this repository are in **MST**.

## What is in here

| Path | What it is |
|---|---|
| [banking-rails/](banking-rails/) | Token research: 88 v3 scored reports, ranked, plus short stubs |
| [banking-rails/COVER.md](banking-rails/COVER.md) | Why the reports exist, the v3 scoring method, and what each section checks |
| [banking-rails/RANKING.md](banking-rails/RANKING.md) | Ranked v3 scores for all 88 reports |
| [banking-rails/ALL-PROJECTS.md](banking-rails/ALL-PROJECTS.md) | Every project in the pipeline: 88 scored reports plus 205 still in progress |
| [daily/](daily/) | One report per day, as `YYYY-MM-DD.md` (readable) and `YYYY-MM-DD.json` (machine-readable) |
| [calendar.md](calendar.md) | Upcoming market events |
| [sources.md](sources.md) | Vetted source list and the verification rule |
| [data/index.json](data/index.json) | Machine index of every daily report and token note |
| [llms.txt](llms.txt) | Agent index in the [llmstxt.org](https://llmstxt.org/) format |

The daily JSON schema is stable enough for agents: `date`, `timezone`, `majors`, `watchlist`, `pools`, `hacks`, `news` (each item has `source` and a `verified` flag), `calendar`, and optional `market_notes`.

## How to browse and search

- On GitHub: open a folder and use the repository search box, or search from the code view.
- On [GitHub Pages](https://pages.github.com/) (once the repo is published with Pages enabled from the `main` branch root): start at the home page and follow the links.
- Locally: clone the repo and search with any tool you like, for example `rg "ROUTER" daily banking-rails`.
- Dates with no file were days without a saved public snapshot, not a claim that the market was quiet.

## How AI agents should use this

1. Read [llms.txt](llms.txt) first. It is the table of contents.
2. Use [data/index.json](data/index.json) to list every daily report and token note with its path.
3. For numbers, prefer the daily `YYYY-MM-DD.json` files over the Markdown prose.
4. For token facts, read the matching file under [banking-rails/](banking-rails/). Public contract and mint addresses are included. Items marked **unverified** are not confirmed.
5. Apply the source rule in [sources.md](sources.md): one Tier A source, or two Tier B outlets, before treating a news claim as verified.
6. After the repository is published, agents can fetch files over raw GitHub URLs. Until then, a local clone is the fastest path. An MCP server can be added later on top of these same files; it is not required to start.

Do not invent holdings, balances, or personal identity for any researcher or reader. This public tree is market intel only.

## Privacy

This public tree is scrubbed of personal identity and of any private portfolio. There are no names, addresses, wallets, account sizes, or position data here. The only handle used is **Madman**, in the project title.

## License

Content is licensed under [CC BY 4.0](LICENSE). Give credit to **Madman's Battlefield Intelligence**.
