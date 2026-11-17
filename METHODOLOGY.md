---
title: Methodology
last_updated: 2026-11-17
timezone: MST
layout_version: 3
disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell. Not the work of a licensed fiduciary.
---

# 📐 Methodology

**Research only. Not financial advice.** Not a recommendation to buy, sell, or hold any token, and not the work of a licensed fiduciary. Times in this repository are in **MST**. Pump-day candles are **UTC** daily closes, as pre-registered below.

This page is the desk's scoring rulebook. The [cover sheet](banking-rails/COVER.md) is the shorter introduction. The 16 Nov 2026 upgrades on this page **do not re-score already published reports**. They apply to reports first published, or substantively updated, on or after that date, and they add a machine-readable layer next to the Markdown that is already live.

---

## 🧮 The v3 scorecard

- Each of the **11 sections** is scored **0–10** from the evidence on the page.
- **6 or more = section PASS.** Under 6 = FAIL. "Not proven" counts as a fail.
- **Overall** is a weighted average over **15** weight points:

| Section | Key | Weight |
|---|---|:---:|
| 💰 Revenue | `revenue` | ×3 |
| 📉 Selling behavior | `selling_behavior` | ×2 |
| 🪙 Foundation / team holdings | `insider_holdings` | ×1.5 |
| 💧 Liquidity & market | `liquidity_market` | ×1.5 |
| 🏛️ Foundation & team | `foundation_team` | ×1 |
| 📊 Tokenomics & supply | `tokenomics_supply` | ×1 |
| 🧑‍💻 Product & development | `product_development` | ×1 |
| 🤝 Adoption & customers | `adoption_customers` | ×1 |
| 🛡️ Security & audits | `security_audits` | ×1 |
| ⚖️ Regulatory | `regulatory` | ×1 |
| 📅 Catalysts & calendar | `catalysts` | ×1 |

Overall PASS needs **6.0 or more**.

- **Hard gates:** if Revenue or Selling is **3 or below**, the overall verdict is FAIL even if the average is higher. The gate key for Selling is `selling_behavior`.
- **Selling "not proven"** is scored **4**. Fair-launch coins with no team wallets may score Selling 6–7 when the trail has been checked and nothing showed up.

### Verification rule

A fact is **verified** only with **1 Tier A** source or **2 independent Tier B** outlets. See [sources.md](sources.md). Everything else is labelled **[Unverified]**.

---

## 1. Versioned, machine-readable data layer

Every published v3 report has a companion JSON file at `data/reports/<TICKER>.json`, validated against [data/schema/report.v1.json](data/schema/report.v1.json).

The JSON holds section scores, the overall score and gates, parseable key numbers, evidence links (transaction and address URLs), pump-day flags noted in the report, retrieval and read dates, a **SHA-256** of the source Markdown, and `schema_version: report.v1`.

Regenerate it from the published Markdown only:

```
python3 scripts/extract_reports.py
python3 scripts/validate_reports.py
python3 scripts/build_data_layer.py
```

`scripts/build_data_layer.py` also rebuilds history, base rates, the public address list, review flags, and the dead list. It reads **only git-tracked** files under `banking-rails/`. Untracked drafts are ignored.

Scores in the JSON are copied from the published report. The extractor does not invent a new grade.

---

## 2. Arkham label confidence

Every on-chain attribution recorded in the JSON has two required fields:

- `confidence`: `high`, `medium`, or `low`
- `independent_corroboration`: `yes` is stored as `true` when a second independent source (an explorer name tag, an official doc, a governance spell, or equivalent) supports the same label

**Rule, effective 16 Nov 2026 for new or updated reports:** only a verified entity label with on-chain proof, or a second independent source, can move a Selling or Holdings score. Prediction labels and unlabelled attributions **cannot** move those scores by themselves. They may be described in the report, and they leave Selling at **4** (not proven) unless something stronger is also on the page.

Published scores were **not** changed in this pass. Cases the extractor could parse as relying on a weak label, or as looking inconsistent with that rule, are listed in [REVIEW-FLAGS.md](REVIEW-FLAGS.md) for review.

Confidence used in the backfill:

| Confidence | What it means |
|---|---|
| High | Entity label plus on-chain proof, or the same label from a second independent source |
| Medium | A single Tier B entity or exchange label (including an Arkham entity label) with no second source parsed |
| Low | Unlabelled, or a prediction-style label, with no independent corroboration |

---

## 3. Pre-registered pump-day test and disclosure quality

These parameters are pre-registered as of **16 Nov 2026**. They are not changed after the fact to fit a coin.

| Parameter | Rule |
|---|---|
| Candle | Daily close |
| Timezone | **UTC** |
| Look-back | Close today versus the close **5** calendar days earlier |
| Threshold | Today's close is at least **10%** above that earlier close |
| Formula | `close(t) >= close(t - 5 calendar days) × 1.10` |

### Price-source hierarchy

Use the first source that returns a usable UTC daily-close series for the token's most liquid listed market. State the source in the report and in the JSON (`pump_day_test.price_source`).

1. Binance USDT (or USD) daily klines, when reachable
2. Gate.io
3. MEXC
4. KuCoin
5. Kraken
6. CoinGecko daily closes, **last resort**, and only when named. If CoinGecko's series is known to be wrong for that token (spikes, missing days), it is not used.

A desk in a region where Binance returns HTTP 451 should skip to the next source rather than invent a close. Prefer exchange klines in the order above: **Gate, then MEXC, then KuCoin**. The public re-runner is [scripts/pump_day_test.py](scripts/pump_day_test.py); see [REPRODUCE.md](REPRODUCE.md).

**CoinGecko date convention:** CoinGecko `market_chart` daily points are stamped 00:00 UTC on day D with the price at the start of day D, which is the UTC close of day **D-1**. Any CoinGecko path must label that point as the close of D-1 and must drop a partial current-day tick. Exchange klines are already stamped as that UTC day's candle, and do not need this shift. `scripts/pump_day_test.py` applies the convention when `--exchange coingecko` is used.

### ATH after a rename, split or migration

When a token is renamed, split, or migrated and a market-data vendor opens a new listing (so its ATH field starts over), carry the predecessor's ATH at the conversion ratio and show **both** figures: the new listing's ATH, and the predecessor ATH expressed in today's units, with the drawdown from the predecessor. Do not quote only the new listing's ATH.

### Disclosure-quality sub-score

When a team, foundation, or treasury-linked wallet sells (or funds a wallet that sells) on a pump day, the report also records a disclosure-quality sub-score:

| Value | Meaning |
|---|---|
| `formal_announcement` | A dated official blog, governance vote, filing, or transparency report published the sale or program |
| `buried_disclosure` | A partial, late, or easy-to-miss mention (a footnote, a later report, a passing sentence) |
| `silence` | No disclosure found |
| `not_applicable` | No pump-day sale was found, or Selling is not proven |
| `unclear` | A sale is described, but the disclosure status could not be parsed cleanly |

### Extra penalty for undisclosed pump-day sales

**Effective for reports first published or substantively updated on or after 16 Nov 2026.** Already published reports are **not** re-scored.

After the ordinary Selling score is set, a **proven** pump-day sale whose disclosure quality is `silence` has **2 points** subtracted from Selling, floored at 0, and **cannot be scored above 3**. That trips the Selling hard gate. `pump_day_undisclosed_penalty_applied` is set to `true` only when this penalty is actually applied. Backfilled JSON for older reports leaves that field `false`.


### Amendment, 16 Nov 2026: when a one-hop transfer counts as a proven sale

A one-hop transfer (project wallet → exchange deposit, or project wallet → fresh wallet → exchange deposit) can be a legitimate payout, a market-making loan or custody. It counts as a **proven sale** only if at least one of these holds:

- **(a)** the receiving exchange account is attributed to the team or project with medium or high confidence;
- **(b)** there is on-chain or exchange evidence that the tokens were actually sold, such as a DEX swap, an on-chain return of proceeds, or a filing or statement;
- **(c)** the project has published no plausible reason for the movement, after a cheap check of its official docs, governance and blog for payroll, grants, contributor payouts, market-making loans, custody or OTC.

If a plausible published reason exists and neither (a) nor (b) holds, the sale is **not proven**: Selling scores **4**, with no silence penalty, and the report cites the reason. The silence penalty applies only to proven sales. This amendment was applied to every report whose proven sale rested on a one-hop link.

Each report records the outcome in the front-matter field `one_hop_sale_status` (`proven`, `not_proven` or `none_found`), next to `team_wallet_to_exchange_during_pump`. That transfer flag only says a transfer happened; read `one_hop_sale_status` to see whether it counts as a sale. A later budget or program post that does not cover the specific sale is not disclosure of it; the sale stays `silence`.

---

## 4. Revenue is locked to token-holder accrual

Company revenue is not token revenue.

**The "reaches holders" test is binary and mandatory** on new or updated reports. It is `yes` only when at least one of the following is **on-chain, automatic, and already executed**:

- a burn paid from protocol fees or an automatic buy-and-burn
- an automatic buyback paid from protocol fees or revenue
- staking yield paid from protocol fees
- a fee share paid to holders

Promises, roadmaps, optional company buybacks, and "governance can vote to spend the treasury" do not count until they execute as an automatic, on-chain mechanism. A section pass on Revenue (6 or more) requires this test to be `yes`. A Revenue score of 4 or 5 can still describe a real business, but only if the report is explicit that holders do not yet have a live claim.

Published scores were **not** changed in this pass. Reports whose published Revenue score looks inconsistent with the test, as parsed from the text, are listed in [REVIEW-FLAGS.md](REVIEW-FLAGS.md).

---

## 5. Dual, blind review of Selling and Holdings

Selling and Holdings are the two highest-weight sections after Revenue, and they are the fraud-adjacent questions. On new or updated reports they should be scored twice.

1. Two independent scorers (two analysts, or one analyst and one agent, or two agents with isolated context) each score Selling and Holdings **without seeing the other's score**.
2. If the two scores on a section differ by **2 or more points**, a public reconciliation note is required. Use the [RECONCILIATION.md](RECONCILIATION.md) template and link it from the report.
3. The published section score is the agreed figure after reconciliation, or the shared figure when they already agree.
4. Schema fields live under `review.dual_review`. Existing reports are stored as `status: not_run`. **No dual reviews were run in this pass.**

---

## 6. Time-series and base rates

- [HISTORY.md](HISTORY.md) and [data/history.json](data/history.json) record each published report's scores by git version, backfilled from this repository's history.
- [BASE-RATES.md](BASE-RATES.md) and [data/base-rates.json](data/base-rates.json) publish, across the current published set: the pass rate, how many reports fail the Revenue gate, how many fail the Selling gate, how many have a proven pump-day sale, how many are "not proven," and the holder-accrual split.

These tables make a single coin easier to read against the rest of the set. They are rebuilt from the published files; they are not a new investigation.

---

## 7. Negative controls and the dead list

[DEAD.md](DEAD.md) is the dated "moved to dead" list. **A published v3 report that fails is never removed from [RANKING.md](banking-rails/RANKING.md) in silence.** It stays until a dated entry is added to the dead list with a reason.

Unscored pipeline names can move to the dead list for an official shutdown, an unfixed exploit, a wind-down, or a documented dying-market skip. The dying-market skip used for [ELK](DEAD.md) is: market cap under $1M **and** 24h volume under $10k, as of a dated public market read. That rule is **not** applied automatically to every thin name on the All Projects scan.

Five already-scored reports at the bottom of the ranking are labelled as **negative controls** in [DEAD.md](DEAD.md): ROUTER, H, COTI, SPA, and EDEL. Their scores are not changed. They are calibration points for later methodology reviews.

---

## 8. Reproducibility

[REPRODUCE.md](REPRODUCE.md) lists the public RPC, explorer, and market APIs this desk uses, and how to re-run the pump-day test. The public addresses examined in published reports — extracted only from evidence links already on the page — are in [data/public-addresses.json](data/public-addresses.json).

Private worksheets, local machine paths, and unpublished drafts are not part of this tree.

---

## How to rebuild

From the repository root:

```
python3 scripts/build_data_layer.py
python3 scripts/build_all_projects.py
python3 scripts/validate_reports.py
python3 scripts/pump_day_test.py --exchange mexc --pair TICKERUSDT --start 2025-11-16 --end 2026-11-16
```

---

## Disclaimer

This is **research only**. It is **not financial advice**, **not a recommendation to buy, sell, or hold** any token, and **not the work of a licensed fiduciary**. Scores can change when the chain, the filings, or the product change. Read the sources. Do your own work.
