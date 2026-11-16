---
ticker: CSPR
name: Casper Network
chain: casper
contract: "native"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 1
  liquidity_market: 4
  product_development: 5
  adoption_customers: 2
  security_audits: 4
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: Jul 2024 security breach; validators halted the chain from 27 to 31 Jul 2024 to stop unauthorized transfers"
  mint_path_live: "yes: 8% yearly inflation (6% stakers, 2% to the Casper Association) plus a one-time 4.76B CSPR (33%) issuance minted 23 Mar 2026"
  team_wallet_to_exchange_during_pump: "not tested (Association wallets not retrievable without a CSPR.cloud key); the Association disclosed ~250M CSPR for market liquidity plus OTC placements"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "unknown"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Nothing to measure; holders are paid in dilution."
pump_day_price_source: "Gate CSPR/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.0018761
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CSPR · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Casper is a Proof-of-Stake Layer 1 run by the Swiss Casper Association. In Feb 2026, validators approved **CVV008**, which on 23 Mar 2026 **minted 4.76B new CSPR in one go (+33%)** for the Association. 1.30B unlocked at once and **433M more unlocks every quarter until Mar 2028**. On top of that, base inflation stays at **8% a year**, now with 2% routed to the Association. The Association says ~250M CSPR would go to "market liquidity" plus OTC deals. There is no tracked revenue or DeFi TVL, and a Jul 2024 breach forced a four-day chain halt. The price is down **99.9% from ATH and 72% in a year**. Revenue trips the hard gate.

**🚨 Top warning:** recapitalisation by dilution. Supply is now **20.20B** ([CSPR.live API](https://api.cspr.live/supply)), after the [4,763,091,158 CSPR issuance](https://www.casper.network/news/casper-2-2-0-goes-live-on-mainnet). Its unlock schedule adds ~433M CSPR (~$0.8M at today's price) to the Association's spendable float every quarter. The next unlock is due 23 Dec 2026.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 1/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CSPR · Casper Network · 3.1 / 10 · ❌ FAIL

> **One line:** A Layer 1 that printed a third more supply to pay for growth, still inflates 8% a year, and shows no revenue.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (CSPR.live API, 16 Nov 2026) |
|---|---|
| **Price** $0.0018761 | **Total supply** 20,200,657,772 CSPR |
| **24h / 7d / 30d** 🟢 +0.8% / 🔴 −8.1% / −20.9% · 1y −72.4% | **Circulating** 17,469,725,584 |
| **Market cap** $32.84M · **FDV** $37.98M | **Issuance** 8.0%/yr (6.0% staking, 2.0% "ecosystem sustain") |
| **24h volume** $9.48M (Gate, OKX, HTX, Bithumb, Bybit) | **One-time mint** 4,763,091,158 CSPR (23 Mar 2026) |
| **ATH** $1.33 (11 May 2021) · now −99.9% | **DeFi TVL** not listed on DefiLlama |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees / revenue | **Not tracked** (no DefiLlama fee or chain listing) | [Tier A] DefiLlama |
| Staker income | 6%/yr new issuance | [Tier A] [CSPR.live API](https://api.cspr.live/supply) |

**What it means:** Nothing to measure; holders are paid in dilution. **1, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Nothing to measure; holders are paid in dilution.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- The Casper Association (Switzerland) stewards the network. Validators vote on proposals: CVV008 passed with 70.9% participation and 89.3% in favour ([Casper](https://www.casper.network/news/governance-vote-008-passes-securing-validator-economics-and-network-sustainability)).
- Quarterly reports exist (Q2 and Q3 2026) but sit behind a wallet-connect login ([reporting portal](https://reporting.casper.network/reports)).
- Spending on exchanges, stablecoins, bridges, liquidity, G&A and more is **exempt from votes** under CVV008 ([forum](https://forum.casper.network/t/cvv008-proposal-securing-validator-economics-and-network-sustainability/1567)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Holder | CSPR | Notes |
|---|---:|---|
| Association (CVV008 issuance) | 4.76B minted | 1.30B unlocked 23 Mar 2026; 433M a quarter after that [Tier A] |
| Association (2% inflation) | ~400M a year | [Tier A API] |
| Older treasury | **Not found** | Supply minus circulating is 2.73B (13.5%) |
| Wallet addresses | **Not found** | The Association promised "clearly labeled wallets ... transparently disclosed", but no list was retrievable here |

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Gate CSPR/USDT daily closes (UTC): 38 of the last 365 days were pump days.*

- **Selling is planned and disclosed:** "Initial movements, including approximately 250 million CSPR, will support market liquidity", plus "structured OTC agreements" ([Casper 2.2.0 post](https://www.casper.network/news/casper-2-2-0-goes-live-on-mainnet)).
- **Not pump-tested:** the Association's wallets could not be pulled (the CSPR.cloud API needs a key).

**What it means:** Known sell pressure with unknown timing, so **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate CSPR/USDT daily closes.

## 📊 Tokenomics & supply · 1/10 · ❌ FAIL

- **+33% one-time mint** (4.76B), **plus 8%/yr** inflation with no cap ([CVV008](https://forum.casper.network/t/cvv008-proposal-securing-validator-economics-and-network-sustainability/1567)).
- Quarterly unlocks of 433M run to 23 Mar 2028.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $9.5M of 24h volume on a $32.8M cap (29% turnover) on Gate, OKX, HTX, Bithumb and Bybit.
- −99.9% from ATH, −72% in a year.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Casper 2.0/2.1/2.2, the CSPR.trade DEX, liquid staking, and an EVM bridge in audit ([Casper](https://www.casper.network/news/governance-vote-008-passes-securing-validator-economics-and-network-sustainability)).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No DefiLlama chain TVL. Enterprise pilots (e.g. a parking MVP) are not quantified.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- **Jul 2024 breach:** validators paused block production on 27 Jul 2024 to stop unauthorized transfers, and the network resumed on 31 Jul after a patch ([Casper incident update](https://www.casper.network/news/casper-blockchain-security-update-incident-contained-and-recovery-efforts-underway) · [Cointelegraph](https://cointelegraph.com/news/casper-network-halts-operations-security-breach)).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. Casper publishes a MiCA white paper/report (site footer) [Unverified].

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 23 Dec 2026 | ~433M CSPR unlock to the Association |
| Quarterly to 23 Mar 2028 | Further 433M unlocks |
| TBA | EVM bridge launch; exchange and stablecoin integrations |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Jul 2024 breach and chain halt |
| Team wallet → exchange during a pump | 🟡 Not tested; liquidity sales disclosed |
| Live mint path | 🔴 8%/yr plus the one-time 33% |
| Treasury in single-key wallets | 🟡 Unknown |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Casper Association wallets | Not published | — | low | no | Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [CSPR.live supply API](https://api.cspr.live/supply), read 16 Nov 2026 ~9:20 AM MST
- [Tier A] [Casper 2.2.0 post](https://www.casper.network/news/casper-2-2-0-goes-live-on-mainnet) · [Vote 008 result](https://www.casper.network/news/governance-vote-008-passes-securing-validator-economics-and-network-sustainability) · [CVV008 forum](https://forum.casper.network/t/cvv008-proposal-securing-validator-economics-and-network-sustainability/1567) · [Reporting portal](https://reporting.casper.network/reports) · [2024 incident update](https://www.casper.network/news/casper-blockchain-security-update-incident-contained-and-recovery-efforts-underway)
- [Tier B] [Cointelegraph](https://cointelegraph.com/news/casper-network-halts-operations-security-breach)
- [Tier A] CoinGecko `casper-network` (16 Nov 2026 8:34 AM MST); Gate CSPR/USDT daily candles
- Arkham does not cover Casper (16 Nov 2026), so no Casper accounts could be looked up
- [Unverified] Association wallet addresses, sales timing, contents of the quarterly reports

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 4.76B CSPR minted; 433M quarterly unlocks; 250M for liquidity | [Casper 2.2.0](https://www.casper.network/news/casper-2-2-0-goes-live-on-mainnet) | A | 16 Nov 2026 |
| Supply 20.20B; 8% issuance split 6/2 | [CSPR.live API](https://api.cspr.live/supply) | A | 16 Nov 2026 |
| Spending categories exempt from votes | [CVV008](https://forum.casper.network/t/cvv008-proposal-securing-validator-economics-and-network-sustainability/1567) | A | 16 Nov 2026 |
| Jul 2024 breach and halt | [Casper](https://www.casper.network/news/casper-blockchain-security-update-incident-contained-and-recovery-efforts-underway) · [Cointelegraph](https://cointelegraph.com/news/casper-network-halts-operations-security-breach) | A + B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which wallets belong to the Casper Association** | Arkham does not cover Casper. Get the "clearly labeled" Association wallets from the Association or CSPR.live, then trace them on CSPR.live | Free |
| 2 | **Liquidity and OTC sales timing** | Trace the operational wallet with a CSPR.cloud API key and pump-test it | Free API key |
| 3 | **Quarterly report contents** | Connect a wallet to the reporting portal and read the Q2/Q3 2026 reports | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
