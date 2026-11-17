---
ticker: HBAR
name: Hedera
chain: hedera
contract: "native (Hedera, token id 0.0.0 / HBAR)"
overall_score: 5.5
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 7
  insider_holdings: 6
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 8
  product_development: 7
  adoption_customers: 5
  security_audits: 7
  regulatory: 8
  catalysts: 5
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none
  council_release_vs_mirror_mismatch: open
  staking_reward_account_runway_under_1y: watch
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees are tiny and staking rewards are paid mostly from treasury-funded accounts, not fees."
pump_day_price_source: "Gate HBAR_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (25 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.058034
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-17
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### HBAR · Overall grade **5.5 / 10 · ❌ FAIL**

**Summary:** Well-governed and unusually transparent about its treasury, with 25 named council node operators, but the network takes in only ~$268k a year in fees, none of which is burned, and the council still controls ~5.7B HBAR with a large ecosystem release forecast for Q4 2026.

**⚠️ Top warning:** The Council still controls **~5.67B HBAR (11.35%) unreleased**, forecasts a **~3.83B ecosystem release in Q4 2026**, and discloses releases only by quarter and category, not by wallet, so pump-day selling can't be tested. Fees (~$268k/yr) are not burned. Check it: [mirror-node supply](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply) · [Council treasury report](https://hederacouncil.org/treasury) · [`treasury 0.0.2 on HashScan`](https://hashscan.io/mainnet/account/0.0.2) · [DefiLlama fees](https://defillama.com/chain/hedera).

**Sections passed: 7 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 8/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (2 ≤ 3).*

---


# 🪪 HBAR · Hedera · 5.5 / 10 · ❌ FAIL

> **One line:** Well-governed and unusually transparent about its treasury, with 25 named council node operators, but the network takes in only ~$268k a year in fees, none of which is burned, and the council still controls ~5.7B HBAR with a large ecosystem release forecast for Q4 2026.

ℹ️ **Adapted for a council-governed layer-1.** "Revenue" = network fees and where they go. "Foundation" = Hedera Council (LLC) plus Hashgraph / HBAR Foundation. "Holdings / Selling" = the Council's unreleased treasury and its quarterly releases.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (Hedera public mirror node, 14 Nov 2026) |
|---|---|
| **Price** $0.058034 | **Total supply** 50,000,000,000 HBAR (fixed; [mirror supply](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply)) |
| **24h / 7d / 30d** 🔴 −8.3% / −13.7% / −30.7% | **Released (mirror)** 44,327,140,680 (88.65%) → **unreleased 5,672,859,320 (11.35%)** |
| **Market cap** $2.57B · **FDV** $2.90B | **Staked** 13.46B HBAR (26.9% of supply) |
| **24h volume** $70.73M | **Staking reward account** [`0.0.800`](https://hashscan.io/mainnet/account/0.0.800) 125,190,011 HBAR · paying ~445,110 HBAR/day |
| **ATH** $0.5692 (15 Sep 2021) · now −90% | **Consensus nodes** 25 (council members) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $409 | [Tier A] [DefiLlama `hedera`](https://defillama.com/chain/hedera), 14 Nov 2026 |
| 30-day fees | $14,562 | [Tier A] DefiLlama |
| 12-month fees | $267,982 | [Tier A] DefiLlama |
| All-time fees | $1,234,396 | [Tier A] DefiLlama |
| Revenue to holders (burn / buyback) | **$0** — no burn | [Tier A] DefiLlama |
| Where fees go | Node accounts and fee account [`0.0.98`](https://hashscan.io/mainnet/account/0.0.98) (3,356,566 HBAR now), feeding node ([`0.0.801`](https://hashscan.io/mainnet/account/0.0.801)) and staking ([`0.0.800`](https://hashscan.io/mainnet/account/0.0.800)) reward accounts | [Tier A] mirror node · Hedera docs |

**What it means:** Fees are priced in tiny fixed USD amounts, so even heavy use earns very little: about $268k in a year on a $2.6B asset. Staking rewards are paid mostly from treasury-funded accounts, not from fees.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees are tiny and staking rewards are paid mostly from treasury-funded accounts, not fees.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Hedera Council (Hedera Hashgraph LLC) | Governs the network and treasury; changing total supply needs **unanimous** consent (LLCA § 8.4) | [Tier A] [hederacouncil.org/treasury](https://hederacouncil.org/treasury) |
| Node operators (25, live mirror read) | LG, Swirlds, Nomura, Google, Zain, Magalu, DLA Piper, Tata Communications, IBM, Deutsche Telekom, Dentons, Australian Payments Plus, EDF, Shinhan Bank, Chainlink Labs, LSE, IIT Madras, Ubisoft, Aberdeen, Mondelēz, BitGo, Arrow Electronics, Nairobi Securities Exchange, Blockchain for Energy, Repsol | [Tier A] mirror node [`network/nodes`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/nodes) |
| Treasury decisions | Council's Treasury Management and Token Economics Committee; HBAR may not leave the treasury without majority council (or delegated board) approval | [Tier A] Council report · HBAR economics paper |
| Code | Open-sourced as Hiero (Linux Foundation) — `hiero-ledger/hiero-consensus-node` pushed 14 Nov 2026, v0.78.1 on 22 Oct 2026 | [Tier A] GitHub |

**What it means:** Named, large organisations run the nodes and vote on treasury moves, with a written supply rule. Control is still a closed club rather than open validators.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

**Council allocation of all 50B HBAR** ([Tier A] Council treasury report, data as of 6 Nov 2026):

| Category | HBAR | % |
|---|---:|---:|
| Initial Development Costs & Licensing | 3,882,948,559 | 7.77% |
| Purchase Agreements (SAFTs, TPAs) | 12,698,348,449 | 25.40% |
| Network Governance & Operations (incl. 780M board reserves, allocated not distributed) | 8,116,201,648 | 16.23% |
| Ecosystem & Open Source Development | 25,302,501,344 | 50.61% |
| Unallocated | 0 | 0% |

| Live check | Value | Source |
|---|---:|---|
| Unreleased per mirror node | 5,672,859,320 (11.35%) | [Tier A] mirror [`network/supply`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply) |
| Unreleased per Council table | 2,129,217,000 (4.26%) — released 47,870,783k incl. Q4 2026 column marked **"Actl/Fcst"** | [Tier A] [Council report](https://hederacouncil.org/treasury) |
| Gap | ~3.54B HBAR — close to the 3.828B Q4 ecosystem release the Council **forecasts**; it does not show as released on-chain yet | Calculated |
| Account [`0.0.2`](https://hashscan.io/mainnet/account/0.0.2) (main treasury) | 16,630,126 HBAR | [Tier A] [mirror](https://mainnet-public.mirrornode.hedera.com/api/v1/balances?account.id=0.0.2) |
| Hedera Foundation grant | 3.5B HBAR received Feb 2025 | [Unverified] one secondary source |

**What it means:** The Council publishes its whole allocation and updates it quarterly, which few projects do. About 5.7B HBAR (11%) is still under council control on-chain today.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **25 of 361 days** were pump days, including 21–29 Sep 2026 (up to +34.9% on 29 Sep).

| Quarter | Released (kilobars, Council table) | Main categories | Pump days in quarter |
|---|---:|---|---|
| Q2 2026 (Actl) | 186,745k total governance/ops; ecosystem 0 | Council Operations 151,517k | 30 May, 1 Jun, 16 Jun… |
| Q3 2026 (Actl) | Released supply 43,495,165k → 43,853,019k (**+357.9M**) | Council Operations 301,792k · Ecosystem 40,000k | 21–29 Sep cluster |
| Q4 2026 (Actl/Fcst) | → 47,870,783k (**+4.02B**) | Ecosystem 3,828,000k · Council Ops 153,504k · Coin Plan 36,000k | none so far |

- Releases are disclosed by category and quarter, **not by date or recipient wallet**. Whether recipients sold during the Sep 2026 pump cluster was not traced.
- No council treasury → exchange transfer was identified in this pass.

**What it means:** Better disclosure than most, but quarterly totals can't be matched against pump days, and Q3 releases fell in a quarter with a big pump. Not proven clean → fail.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate HBAR_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (25 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Supply | 50B fixed (unanimous council vote to change) | [Tier A] Council |
| Released | 88.65% (mirror) · CoinGecko circulating 44.33B matches the mirror | [Tier A] / [Tier B] |
| Staking rewards | ~445,110 HBAR/day from 0.0.800 (125.19M balance → ~9 months of runway at this rate unless topped up) | [Tier A] mirror `network/stake` · calculated |
| Upcoming | Up to ~3.8B HBAR (~8.6% of circulating) ecosystem release forecast for Q4 2026 | [Tier A] Council forecast |

## 💧 Liquidity & market · 8/10 · ✅ PASS

- $70.73M 24h volume; major CEX listings; Canary HBAR ETF trades in the US (mid-2026 filing: ~$46M fair value vs ~$106M cost — a fact about the fund) [Tier A SEC EDGAR, 10 Oct 2026 pass].

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Hiero consensus node releases monthly; EVM-compatible smart contracts; Hedera Consensus Service and token service live [Tier A GitHub / docs].

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- Council members are node operators, not proof of paying usage. Fee data (~$400/day) shows little paid activity in dollar terms.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- No HBAR-protocol hack in this series. Coinbase delayed HBAR sends on 5 Nov 2026 (exchange issue, resolved) [Tier A Coinbase Status]. A smart-contract-service exploit in March 2023 is past history with an official post-mortem.

## ⚖️ Regulatory · 8/10 · ✅ PASS

- **US:** SEC Release 33-11412 (issued 17 Mar 2026, effective 23 Mar 2026, joined by the CFTC) names **Hedera (HBAR)** as an example of a **digital commodity**, which is not a security ([Tier A] [govinfo](https://www.govinfo.gov/content/pkg/FR-2026-03-23/html/2026-05635.htm)). HBAR originally sold under SAFTs / regulated swap contracts (per Council report). US ETF listed with SEC filings. No current enforcement found.
- **Correction, 17 Nov 2026:** Regulatory **6 → 8** after Release 33-11412 was applied. Overall **5.3 → 5.5**. Still FAIL on the revenue gate.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Q4 2026 | Forecast ecosystem release ~3.83B HBAR | Supply ↑ (watch mirror `released_supply`) |
| Monthly | Hiero node releases | Product |
| Next quarterly Council treasury update | ~early Dec 2026 / Jan 2027 | Disclosure |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Council table vs mirror-node released supply | 🟡 Open (~3.54B gap, likely forecast vs actual): [mirror](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply) vs [Council table](https://hederacouncil.org/treasury) |
| Staking reward account under 1 year of runway | 🟡 Watch (~9 months at current payout): [`0.0.800`](https://hashscan.io/mainnet/account/0.0.800) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Hedera Council treasury releases | Hedera Council | Quarterly disclosures | high | yes | Selling stays 5: totals cannot be matched to pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Hedera public mirror node (`mainnet-public.mirrornode.hedera.com`): [`network/supply`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply), [`network/nodes`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/nodes), [`network/stake`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/stake), balances of [`0.0.2`](https://hashscan.io/mainnet/account/0.0.2) / [`0.0.98`](https://hashscan.io/mainnet/account/0.0.98) / [`0.0.800`](https://hashscan.io/mainnet/account/0.0.800) / [`0.0.801`](https://hashscan.io/mainnet/account/0.0.801) (HashScan); 14 Nov 2026 ~12:30 PM MST
- [Tier A] [Hedera Council treasury report](https://hederacouncil.org/treasury), data as of 6 Nov 2026
- [Tier A] [DefiLlama fees `hedera`](https://defillama.com/chain/hedera), 14 Nov 2026
- [Tier A] [CoinGecko `hedera-hashgraph`](https://www.coingecko.com/en/coins/hedera-hashgraph) price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] GitHub [`hiero-ledger/hiero-consensus-node`](https://github.com/hiero-ledger/hiero-consensus-node) · SEC EDGAR (Canary HBAR ETF, from 10 Oct 2026 pass) · Coinbase Status
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): **Hedera is not supported** (account [`0.0.2` on Arkham](https://intel.arkm.com/explorer/address/0.0.2) returns "Something went wrong / Couldn't load portfolio"), and there is **no Hedera Council or Hedera Foundation entity** ([`/explorer/entity/hedera`](https://intel.arkm.com/explorer/entity/hedera) = not found) (search returned only individual social accounts). The Q3 2026 release recipients and pump-day selling stay untested. No score change
- [Unverified] Hedera Foundation 3.5B grant date

## 🔗 Evidence trail

*Strongest findings first. Hedera is not supported by Arkham, so evidence is the public mirror node (each link opens the live read), HashScan and the Council's own report.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Unreleased supply 5,672,859,320 HBAR (11.35%) per mirror node | [`network/supply`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply) | A | 14 Nov 2026 ~12:30 PM MST |
| Council table shows only 2.13B unreleased incl. Q4 2026 "Actl/Fcst" column; ~3.54B gap ≈ the 3.828B Q4 ecosystem forecast | [Council treasury report](https://hederacouncil.org/treasury) · [mirror supply](https://mainnet-public.mirrornode.hedera.com/api/v1/network/supply) | A | 14 Nov 2026 |
| Q3 2026 released +357.9M HBAR in a quarter with the 21–29 Sep pump cluster; recipients not disclosed by wallet | [Council treasury report](https://hederacouncil.org/treasury) | A | 14 Nov 2026 |
| Fees ~$268k in 12 months, no burn | [DefiLlama](https://defillama.com/chain/hedera) | A | 14 Nov 2026 |
| Staking reward account holds 125.2M HBAR, paying ~445k/day (~9 months runway) | [`0.0.800 on HashScan`](https://hashscan.io/mainnet/account/0.0.800) · [mirror stake](https://mainnet-public.mirrornode.hedera.com/api/v1/network/stake) | A | 14 Nov 2026 |
| 25 named council node operators | [`network/nodes`](https://mainnet-public.mirrornode.hedera.com/api/v1/network/nodes) | A | 14 Nov 2026 |
| Arkham: Hedera unsupported; no Council/Foundation entity | [0.0.2 on Arkham](https://intel.arkm.com/explorer/address/0.0.2) · [entity search](https://intel.arkm.com/explorer/entity/hedera) | B | 15 Nov 2026 ~11:05 AM MST |

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Council releases vs pump days.** Quarterly release totals cannot be matched to the 21–29 Sep 2026 pump days | Match Hedera Council treasury account transfers on HashScan to the Gate pump-day list | Free |
| 2 | **Staking reward account runway** | Read account 0.0.800 balance on HashScan each quarter | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
