---
title: Review flags
generated_at: 2026-11-16 14:20 MST
timezone: MST
disclaimer: Research only. Not financial advice. Scores on this page were not changed.
---

# 🚩 Review flags

**Research only. Not financial advice.** Times are in **MST**.

Scores were not changed. These are review lists parsed from the published Markdown. A flag means a human (or a later dual review) should look at that section, not that the published score is automatically wrong.

The rules these flags apply are in [METHODOLOGY.md](METHODOLOGY.md). Machine-readable copy: [data/review-flags.json](data/review-flags.json).

## 1. Selling or Holdings may have used a low-confidence label alone

Rule: only a verified entity label with on-chain proof, or a second independent source, can move a Selling or Holdings score. Prediction labels and unlabelled attributions cannot move those scores by themselves.

**6 report(s) flagged.**

| Ticker | Selling | Holdings | Why |
|---|---:|---:|---|
| [API3](banking-rails/API3.md) | 1 | 6 | Selling failed, and the report links the flow to the team or treasury through an unlabelled or prediction attribution with no independent corroboration.<br>An Arkham team, foundation or entity label in Selling or Holdings has no second independent source parsed from the report, and that section failed or records a score change. |
| [COTI](banking-rails/COTI.md) | 2 | 2 | Selling failed, and the report links the flow to the team or treasury through an unlabelled or prediction attribution with no independent corroboration. |
| [HYPER](banking-rails/HYPER.md) | 2 | 3 | Selling failed, and the report links the flow to the team or treasury through an unlabelled or prediction attribution with no independent corroboration. |
| [W](banking-rails/W.md) | 3 | 3 | Selling failed, and the report links the flow to the team or treasury through an unlabelled or prediction attribution with no independent corroboration. |
| [XPL](banking-rails/XPL.md) | 1 | 3 | Selling failed, and the report links the flow to the team or treasury through an unlabelled or prediction attribution with no independent corroboration. |
| [ZBCN](banking-rails/ZBCN.md) | 1 | 4 | Selling failed, and the report links the flow to the team or treasury through an unlabelled or prediction attribution with no independent corroboration. |

## 2. Selling or Holdings cites an Arkham label with no second source parsed

These are not automatically wrong. Exchange and entity labels from Arkham are Tier B. The new rule asks for on-chain proof of the label, or a second independent source, before that label can move Selling or Holdings. They are listed so a later review can confirm or downgrade them. Scores were left as published.

**3 report(s) flagged.**

| Ticker | Selling | Holdings |
|---|---:|---:|
| [API3](banking-rails/API3.md) | 1 | 6 |
| [CPOOL](banking-rails/CPOOL.md) | 2 | 4 |
| [JASMY](banking-rails/JASMY.md) | 2 | 3 |

## 3. Revenue score looks inconsistent with the holder-accrual test

The test is binary: an on-chain, automatic burn, buyback, staking yield from fees, or fee share that has already executed. Promises do not count. A report is listed when Revenue is 4 or higher and the test is **no**, when Revenue is a pass (6 or more) and the test is not **yes**, or when the test is **yes** and Revenue still trips the hard gate. Scores were left as published.

**3 report(s) flagged.**

| Ticker | Revenue | Reaches holders | Mechanisms | Notes (from the report) |
|---|---:|---|---|---|
| [QNT](banking-rails/QNT.md) | 4 | no | — | The company makes real, audited money and is profitable. The token gets no share of it. Paying in QNT is optional and nothing forces buying, so ~$2.3B of market cap sits on top of a ~£11.5M-a-year software business th... |
| [REUSD](banking-rails/REUSD.md) | 7 | unclear | — | ## 💰 Revenue — Does it make money? · 7/10 · ✅ PASS - Yield comes from reinsurance premiums and collateral return: SOFR + 250 bps off-chain, sUSDe + 250 bps on-chain ([About reUSD](https://docs.re.xyz/products/about-re... |
| [SOLV](banking-rails/SOLV.md) | 4 | no | buyback, fee_share | The business is real and cheap on a sales multiple, but the token has no claim on revenue and no live buyback. SOLV's uses are governance, staking and fee discounts. **4**: better than a zero-revenue token, but it doe... |

---

## Disclaimer

This is **research only**. It is **not financial advice** and not a recommendation to buy, sell, or hold any token. A flag is a request for review, not a new score.
