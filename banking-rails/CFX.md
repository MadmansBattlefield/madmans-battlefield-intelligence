---
ticker: CFX
name: Conflux
chain: conflux
contract: "native"
overall_score: 3.9
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 4
  product_development: 6
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes, PoW 0.4 CFX a block plus 3.26% PoS interest (~1.8% a year net, Tier B)"
  team_wallet_to_exchange_during_pump: "no: published founder lock addresses have had no outflows since Mar 2025"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "unknown; launch-era fund contracts reportedly hold ~3.0B CFX [Unverified]"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Revenue is negligible at the token's scale; no burn, buyback or fee share."
pump_day_price_source: "Gate CFX/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.03432468
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CFX · Overall grade **3.9 / 10 · ❌ FAIL**

**Summary:** Conflux is a hybrid PoW/PoS layer 1 with an EVM side-chain (eSpace). Supply is uncapped: **5.83B CFX issued, of which 572.96M sit at the null address (burned)**, leaving ~5.26B circulating, with 971.8M staked (ConfluxScan supply API). Net issuance is now low, about 1.8% a year, after a governance vote halved PoW rewards to 0.4 CFX a block on 7 Apr 2026. But there is **no meaningful fee revenue**: DefiLlama lists no Conflux chain fees, chain TVL is $5.8M, and only 37% of base fees are burned. The founders' published 2021 lock addresses are empty; the last large outflow was in Mar 2025. Development is active (v3.1.1, Oct 2026). Revenue trips the hard gate.

**🚨 Top warning:** A $180M chain with $5.8M of TVL and no fee revenue tracked. Value depends entirely on the foundation and ecosystem funds, which reportedly still hold ~3.0B CFX in launch-era contracts (≈57% of circulating) and pay out ~49M CFX a quarter [Tier B, single source → Unverified]. The price is −61% in a year and −98% from ATH.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CFX · Conflux · 3.9 / 10 · ❌ FAIL

> **One line:** Mature engineering and modest inflation, but no revenue and a huge foundation-controlled float.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (ConfluxScan supply API, 16 Nov 2026) |
|---|---|
| **Price** $0.0343 · 24h / 7d / 30d 🔴 +2.0% / −18.2% / −36.3% · 1y −61.0% | **Total issued** 5,828,594,817 CFX · no cap |
| **Market cap** $180.4M · rank #166 | **Burned (null address)** 572,964,411 CFX |
| **24h volume** $3.35M: BloFin $1.00M, HTX $0.70M, Binance $0.59M, OKX $0.39M | **Staked** 971,790,994 CFX · eSpace 336.6M |
| **ATH** $1.70 (26 Mar 2021) · now −98.0% | **DefiLlama chain TVL** $5.82M |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama chain fees / revenue | Not listed | [Tier A] api.llama.fi `/summary/fees/conflux` |
| Base fee burned | 37% (63% shared with miners) | [Tier A] [Conflux forum, Round 20 parameters](https://forum.conflux.fun/t/conflux-network-key-parameters-round-20-voting-results-to-take-effect-soon/23506) |
| Fees burned, 10 Aug – 8 Nov 2026 | 1,439 CFX (~$50) | [Tier B, single → Unverified] [MrNasDog](https://mrnasdog.com/research/cfx) |

**What it means:** no revenue at the scale of the token. **1 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Revenue is negligible at the token's scale; no burn, buyback or fee share.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- The Conflux Foundation and core team ship regular releases (v3.1.1 mainnet and testnet in Oct 2026; [monthly report](https://confluxnetwork.medium.com/monthly-progress-report-october-2026-93338db112f3), Tier A).
- Parameters are set by periodic on-chain governance votes (Round 20 passed 6 Feb 2026).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Genesis allocation (5B CFX) | Share | Unlock |
|---|---:|---|
| Genesis team (founders, foundation staff, advisors) | 36% | 4 years |
| Ecosystem fund | 40% | 4 years; unused portions partly burned |
| Private investors | 16% | 2 years |
| Community fund | 8% | 4 years |

*Source: [Tier A] [Conflux economic model, Medium](https://medium.com/conflux-network/conflux-networks-economic-model-pre-mined-token-distribution-and-proportions-f92fe00696ea).*

- **Published founder lock addresses (2021) are now empty** (Conflux RPC `cfx_getBalance`, 16 Nov 2026). For example, [`cfx:acfb4d…0e19`](https://confluxscan.org/address/cfx:acfb4d6pxc662y8uus8b4kea4g37cfurzymz4z0e19) released [65.78M CFX on 28 May 2022](https://confluxscan.org/transaction/0xae48dfd6337ac1c45ae321518388466a0a6d781f6a6edb18677dc3fc8cf40c8c). The 13 addresses together hold 174k CFX today.
- Launch-era fund contracts reportedly still hold 1,348M, 552M, 303M, 105M and 665M CFX (~2.97B) [Tier B, single → Unverified]. Their addresses could not be retrieved because the ConfluxScan holder ranking isn't public.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate CFX/USDT daily closes (UTC): 36 pump days in the last 365.*

- None of the 13 published founder lock addresses moved CFX in the last 365 days. The last large outflow was [3.58M CFX from cfx:aaryuw… on 21 Mar 2025](https://confluxscan.org/transaction/0xb94d1171c669ee353d2221b04b4dc3cddace1468a9e1972574e52897c2f00e65).
- The fund contracts' monthly payouts (~49M CFX a quarter to one staking wallet, Tier B) could not be pump-tested without their addresses.

**What it means:** no evidence of insider pump selling, but the biggest pools are untested. **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate CFX/USDT daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- No cap. PoW reward cut from 0.8 to 0.4 CFX a block from 7 Apr 2026; PoS interest 3.26% [Tier A forum].
- 572.96M CFX burned to date (null address, Tier A), mostly one-off ecosystem-fund burns (latest 76M in May 2025, Tier B).
- Net issuance ~1.8% a year (23.16M CFX in 90 days, Tier B).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $3.35M of 24h volume on a $180M cap (1.9%), spread across BloFin, HTX, Binance and OKX.
- −98% from the 2021 ATH; −61% in a year.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Core + eSpace chain; v3.1.1 security and stability release (22 Oct 2026); AxCNH stablecoin incentives on Unitus Finance [Tier A monthly report].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Chain TVL $5.82M (DefiLlama). Ecosystem incentives are paid in CFX (175k CFX for Unitus in Oct 2026).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No chain exploit found in this pass. v3.1.1 fixed possible node panics and memory issues [Tier B ×2: Conflux forum via Blockchain.News; monthly report].

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found against CFX. The project markets itself to regulated Chinese-yuan stablecoin use (AxCNH). Policy shifts are a two-way risk.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Periodic | Next parameter governance vote (reward / burn ratios) |
| Unscheduled | Further ecosystem-fund burns (none announced) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None in 365d (published founder locks) |
| Live mint path | 🟡 ~1.8% a year protocol issuance |
| Treasury in single-key wallets | 🟡 Unknown; ~3.0B in fund contracts [Unverified] |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Published founder lock addresses | Conflux founders | Project publication + chain | high | yes | None: no outflows since Mar 2025 |
| Largest pools | Untested | — | low | no | Selling stays 5 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- Arkham does not cover Conflux (Core Space or eSpace), so no Arkham labels were available for the CFX wallets; attribution rests on ConfluxScan and Conflux's own publications
- [Tier A] ConfluxScan `/statistics/supply` and `/account/cfx/transfers`; Conflux RPC `cfx_getBalance`, read 16 Nov 2026
- [Tier A] [Conflux economic model](https://medium.com/conflux-network/conflux-networks-economic-model-pre-mined-token-distribution-and-proportions-f92fe00696ea) · [Ecosystem fund update and founder locks](https://medium.com/conflux-network/ecosystem-funds-update-8bb1cbce80b8) · [Round 20 parameters](https://forum.conflux.fun/t/conflux-network-key-parameters-round-20-voting-results-to-take-effect-soon/23506) · [Oct 2026 report](https://confluxnetwork.medium.com/monthly-progress-report-october-2026-93338db112f3)
- [Tier B] [MrNasDog CFX supply](https://mrnasdog.com/research/cfx) · [Blockchain.News](https://blockchain.news/news/cfx-block-rewards-halved-conflux-supply-cut-april-2026)
- [Tier A] CoinGecko `conflux-token` (16 Nov 2026 8:34 AM MST); DefiLlama chains; Gate CFX/USDT daily candles

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 572.96M CFX burned; 971.8M staked | [ConfluxScan supply API](https://api.confluxscan.org/statistics/supply) | A | 16 Nov 2026 |
| Founder lock released 65.78M (2022) | [tx](https://confluxscan.org/transaction/0xae48dfd6337ac1c45ae321518388466a0a6d781f6a6edb18677dc3fc8cf40c8c) | A | 16 Nov 2026 |
| Last large founder-lock outflow, Mar 2025 | [tx](https://confluxscan.org/transaction/0xb94d1171c669ee353d2221b04b4dc3cddace1468a9e1972574e52897c2f00e65) | A | 16 Nov 2026 |
| PoW reward halved, Apr 2026 | [forum](https://forum.conflux.fun/t/conflux-network-key-parameters-round-20-voting-results-to-take-effect-soon/23506) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Attribution of the CFX wallets** | Arkham does not cover Conflux. Use ConfluxScan name tags, or ask the Conflux Foundation to publish its fund and team addresses | Free |
| 2 | **Fund-contract addresses** | Pull the top CFX holders from the ConfluxScan web UI and pump-test the monthly payout wallet | Free |
| 3 | **Fee income** | Sum the 30-day base fees from ConfluxScan daily stats | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
