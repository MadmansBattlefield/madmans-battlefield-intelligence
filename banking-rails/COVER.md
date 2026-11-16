---
title: Banking rails cover sheet
layout_version: 3
scored_reports: 113
last_updated: 2026-11-16
timezone: MST
disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell. Not the work of a licensed fiduciary.
---

# 🏦 Banking rails — cover sheet

**Research only. Not financial advice.** Not a recommendation to buy or sell, and not the work of a licensed fiduciary. No trades are recommended or placed from these reports. Times are in **MST**.

This sheet explains why the reports exist, how they are scored, and what is checked in each section. Start here, then read the [ranking](RANKING.md) and the individual token files.

---

## 🎯 Why this research exists

A lot of tokens around digital settlement, payroll, tokenized assets (RWA), and payments (PayFi) are sold as if they were real businesses. Some are. Many are not.

These reports try to answer two questions first, then everything else:

1. **Does the coin actually generate money** — and does any of that money reach the token, not just the company?
2. **Who is in charge, how many coins do they hold, and do they sell into pump events?**

The point is to separate a real business with verifiable cash flow from a story, a listing, or a governance coupon that earns nothing. Marketing claims, influencer threads, and self-reported volume do not count until they are backed by a primary source.

This is market research, not a portfolio, not a tip sheet, and not a score of "which coin to buy."

---

## 🧭 Methodology

The research questions, source rules, pump test, and treasury questions come from the **Real Rails project plan** (sections 4–6: scoring, treasury badge rules, and what a coin report contains). The grade on these reports is the **v3 scorecard** described below — an 11-section, 0–10 weighted score — not the plan's older 0–100 first-pass triage script.

### 🔎 Sources and the verification rule

Primary sources only, in this order:

- On-chain reads (RPC, explorers, verified contract source, DEX and pool APIs)
- Official docs, blogs, token pages, and project GitHub
- Audits and official post-mortems
- Filings and registers (SEC EDGAR, company registries, court dockets, regulator sites, reserve attestations)

A fact is **verified** only with **1 Tier A** source or **2 Tier B** outlets (reputable journalism that quotes primary material). See [sources.md](../sources.md). Everything else is labeled **[Unverified]**. Unknowns say **"Not found"** and what would answer them. Influencer posts and social claims are leads only.

### 🧮 How the v3 score works

- Each of the **11 sections** is scored **0–10** from the evidence on the page.
- **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** is a weighted average:

| Section | Weight |
|---|:---:|
| 💰 Revenue | ×3 |
| 📉 Selling behavior | ×2 |
| 🪙 Foundation / team holdings | ×1.5 |
| 💧 Liquidity & market | ×1.5 |
| Every other section | ×1 |

Weights sum to **15**. Overall PASS needs **6.0 or more**.

- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL even if the average is higher. A token that does not make money, or whose insiders sell into pumps, does not pass.
- **Pump day** = a daily close at least **10% above** the close five days earlier. A team, foundation, or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. This is the plan's treasury pump-dump test, applied as a section score and a hard gate.

Each report opens with YAML front matter (for search tools and AI agents), then a **quick review card** (overall grade, a one-line summary, and pass/fail for every section), then the full data for every section, red lines, and sources. Nothing material is left in a footnote.

---

## 🔎 What we looked at

Every scored report uses the same 11 sections. The header of each section shows the score and whether it passed or failed. The body shows every figure we have, with a source on the line.

### 💰 1. Revenue — Does it make money?

The most important section. We check product pricing, on-chain receipts or fee events, DefiLlama fees and revenue (30-day and all-time), TVL where it exists, burns and buybacks, any contractual claim the token has on cash flow, and whether usage is paid in the token or in a stablecoin. A company that makes money while the token earns nothing is scored on the token, not the company.

### 🏛️ 2. Foundation & team — Who is in charge?

Legal entity and registry filings, directors and founders (named and verified vs. unverified), GitHub organizations and last commits, multisig signers and time locks, and disclosed investors. A missing company, an unfilled legal template, or a founder who quietly left the team page is written down as such.

### 🪙 3. Foundation / team holdings — How many coins do they hold?

Live wallet and escrow balances versus official allocations, locked vs. liquid, vesting cliffs, claimable-but-unclaimed amounts, and the share of supply insiders can move today. We re-read the chain; we do not reuse a marketing pie chart as a live figure.

### 📉 4. Selling behavior — Do insiders sell into pumps?

The pump-day test above, plus any team, foundation, or treasury route to an exchange or to a wallet that then sold, and whether those moves were disclosed. "No two-label team-to-exchange deposit found" is not the same as a pass if wallets were never published or liquidity was pulled without notice.

### 📊 5. Tokenomics & supply

Total and circulating supply, mint / freeze / pause / blacklist / upgrade authority, unlock calendars vs. on-chain locks, burns, and whether the live code matches the docs.

### 💧 6. Liquidity & market

Pool depth, who controls the LP and whether it is locked, 24h volume, CEX and DEX listings, and — where we can read it — buy-side cash in the main pool and estimated sell impact.

### 🧑‍💻 7. Product & development

What is actually live vs. late, partial, or abandoned; GitHub activity (repos pushed in the last 90 days, last push); and whether the flagship product still exists.

### 🤝 8. Adoption & customers

Named partners and customers, split into confirmed (the other party or a primary record says so), partly confirmed, false, and unverified. Paying usage beats a logo board.

### 🛡️ 9. Security & audits

Confirmed incidents, audit scope and what was actually fixed, upgrade keys (multisig vs. a single plain key), and restitution that landed on-chain vs. a promise.

### ⚖️ 10. Regulatory

Licences and registrations on a regulator's own register, filings, court dockets, and the difference between a notification and an approval. "Not checked this pass" fails until it is checked. Paperwork is not a licence.

### 📅 11. Catalysts & calendar

Dated unlocks, releases, court dates, product milestones, and open items, with a note on whether they add supply, legal risk, or genuine product news.

Reports also carry **🚩 red lines** that are token-specific (for example a liquidity floor, a hack, a mint role, or a paying-customer deadline). Those sit under the sections and in the YAML front matter. They can trip even when the overall grade is already a fail.

---

## 📋 What is scored so far

All 113 tokens in this folder have a full v3 report: [BTC](BTC.md), [ETH](ETH.md), [LINK](LINK.md), [SKY](SKY.md), [SOL](SOL.md), [AERO](AERO.md), [CC](CC.md), [SYRUP](SYRUP.md), [ARB](ARB.md), [XLM](XLM.md), [ENA](ENA.md), [BNKR](BNKR.md), [AVAX](AVAX.md), [TAO](TAO.md), [REUSD](REUSD.md), [JST](JST.md), [HBAR](HBAR.md), [ZRO](ZRO.md), [BP](BP.md), [XMR](XMR.md), [XRP](XRP.md), [ADA](ADA.md), [BCH](BCH.md), [ALGO](ALGO.md), [APT](APT.md), [ZEC](ZEC.md), [QUAI](QUAI.md), [DOT](DOT.md), [INV](INV.md), [DASH](DASH.md), [ONDO](ONDO.md), [CELO](CELO.md), [API3](API3.md), [SOLV](SOLV.md), [BTT](BTT.md), [WAN](WAN.md), [CARDS](CARDS.md), [QNT](QNT.md), [FXS](FXS.md), [MNT](MNT.md), [CFG](CFG.md), [HUMA](HUMA.md), [RVN](RVN.md), [ICP](ICP.md), [RLC](RLC.md), [RED](RED.md), [ZBCN](ZBCN.md), [TRAC](TRAC.md), [REQ](REQ.md), [AMP](AMP.md), [ETC](ETC.md), [XVG](XVG.md), [SEI](SEI.md), [TFUEL](TFUEL.md), [DUSK](DUSK.md), [BAND](BAND.md), [EWT](EWT.md), [HTX](HTX.md), [KAIA](KAIA.md), [PHA](PHA.md), [CFX](CFX.md), [INJ](INJ.md), [MBG](MBG.md), [ZK](ZK.md), [TRB](TRB.md), [ZAMA](ZAMA.md), [ROSE](ROSE.md), [XDC](XDC.md), [NIGHT](NIGHT.md), [ZANO](ZANO.md), [W](W.md), [ASTR](ASTR.md), [HASH](HASH.md), [AXL](AXL.md), [PLUME](PLUME.md), [XPL](XPL.md), [SUI](SUI.md), [CRO](CRO.md), [MOCA](MOCA.md), [IOTX](IOTX.md), [ZEN](ZEN.md), [KAIO](KAIO.md), [CPOOL](CPOOL.md), [HYPER](HYPER.md), [SHX](SHX.md), [VELO](VELO.md), [PROPC](PROPC.md), [ZKC](ZKC.md), [ZKP](ZKP.md), [OM](OM.md), [PUNDIX](PUNDIX.md), [POLYX](POLYX.md), [S](S.md), [ZIG](ZIG.md), [STBL](STBL.md), [SHARE](SHARE.md), [YELLOW](YELLOW.md), [KAVA](KAVA.md), [PACT](PACT.md), [EXA](EXA.md), [HONEY](HONEY.md), [CSPR](CSPR.md), [TLOS](TLOS.md), [XDB](XDB.md), [JASMY](JASMY.md), [SERV](SERV.md), [MASQ](MASQ.md), [EDEL](EDEL.md), [SPA](SPA.md), [SWCH](SWCH.md), [COTI](COTI.md), [H](H.md), [ROUTER](ROUTER.md).

---

## ⚠️ Disclaimer

This is **research only**. It is **not financial advice**, **not a recommendation to buy, sell, or hold** any token, and **not the work of a licensed fiduciary**. Scores can change when the chain, the filings, or the product change. Read the sources. Do your own work.
