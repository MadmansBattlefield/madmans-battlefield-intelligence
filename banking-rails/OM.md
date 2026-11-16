---
ticker: OM
name: MANTRA (formerly OM)
chain: mantra-chain
contract: "native coin (MANTRA Chain); legacy ERC20 OM 0x3593d125a4f7849a1b059e64f4517a86dd60c95d"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 4
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes: 3% yearly staking inflation up to a 10B MANTRA cap"
  team_wallet_to_exchange_during_pump: "not proven: native-chain treasury wallets not traced"
  entity_concentration: "Association 12.8% plus core contributors 16.9% of genesis (vesting)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee record exists and nothing reaches holders."
pump_day_price_source: "the daily closes cited in the body"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.002296
price_source: "CoinGecko, 16 Nov 2026 ~8:52 AM MST (per MANTRA; 1 OM = 4 MANTRA)"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### OM · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** MANTRA is a Cosmos-based layer 1 pitched for real-world assets. At block 13,000,000 (around 2 Mar 2026), each OM was split into 4 MANTRA, and the ticker changed. The chain holds **$0.49M** of DeFi TVL. I found no fee or revenue data, so the revenue gate fails. MANTRA is down 91% from the listing-day high it set right after the split. Most volume is on a single Korean exchange.

**🚨 Top warning:** almost nothing is built on a $15.6M chain. DefiLlama shows **$494k** of TVL on MANTRA Chain. With no published fees, there is nothing on-chain that supports the token's value. I could not trace treasury and contributor wallets on the native chain, so the selling check is not proven. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 OM · MANTRA · 3.4 / 10 · ❌ FAIL

> **One line:** An RWA chain with half a million dollars of TVL and no published revenue.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:52 AM MST) | 🔗 Chain ([MANTRA tokenomics docs](https://docs.mantrachain.io/mantra-tokenomics), [DefiLlama](https://defillama.com/chain/MANTRA), 16 Nov 2026) |
|---|---|
| **Price** $0.002296 per MANTRA (≈ $0.0092 per old OM) | **Genesis** 1,777,777,776 OM = 7.11B MANTRA |
| **24h / 7d / 30d** ⚪ +0.6% / 🔴 −22.0% / 🔴 −41.2% | **Total** 8.38B · **Max** 10B MANTRA |
| **Market cap** $15.6M · **FDV** $19.2M | **Circulating** 6.80B (68%) |
| **24h volume** $2.08M (Upbit $1.50M, Hotcoin, CoinW, Bithumb, Binance $0.22M) | **DeFi TVL** $494k (DefiLlama, 15 Nov 2026) |
| **ATH** $0.02627 (4 Mar 2026) · now −91.3% | **Inflation** 3% per year (docs) |
| **Pump days** 24 in the last year (largest +43.5% on 16 Feb 2026; split week 3–9 Mar excluded) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- DefiLlama has no fee record for MANTRA, and the project publishes none. Chain TVL is $494k. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee record exists and nothing reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- The MANTRA Chain Association is the issuer. Leaders are described by role only. In Apr 2025, OM fell about 90% in a few hours; the project blamed forced liquidations on exchanges (Tier B, outside the 1-year window).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- At genesis: Association 12.8% (ecosystem 2.1%, pre-seed 5.6%, seed 5.1%), core contributors 16.9% (30-month cliff, then 30 months linear), airdrops 2.8% (docs). Native wallet balances were not read [Unverified].

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Treasury and contributor wallets are on MANTRA Chain. I ran no native-chain trace, so this is **not proven → 4.** Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) labels the Ethereum contract [0x3593…c95d](https://intel.arkm.com/explorer/address/0x3593d125a4f7849a1b059e64f4517a86dd60c95d) **MANTRA: MANTRA Token (OM)** but shows no Association or contributor wallets, and MANTRA Chain is not an Arkham-supported network. This still needs a MANTRA Chain explorer API.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from the daily closes cited in the body.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 68% circulating, with 3% yearly inflation up to the 10B cap. Core-contributor tokens start unlocking once the 30-month cliff ends [Unverified date: ~2027].

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About 72% of volume is on Upbit. Binance MANTRA pairs opened on 4 Mar 2026, and price has fallen 91% since.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- A Cosmos SDK chain with CosmWasm, live since 2024. It ran the token split upgrade at block 13,000,000.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- $494k of TVL. No independent RWA issuance volume found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No chain exploit found. Audit reports were not reviewed.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement against the Association found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- The contributor cliff ends (~2027), and inflation continues.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (native chain not traced) |
| Live mint path | 🟠 3% yearly inflation |
| Entity concentration | 🟠 ~30% of genesis to the Association and contributors |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| MANTRA treasury on MANTRA Chain | Not traced | — | low | no | Selling stays 4 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] [MANTRA tokenomics docs](https://docs.mantrachain.io/mantra-tokenomics) (genesis split, 1:4 split, vesting)
- [Tier A] [DefiLlama MANTRA chain TVL](https://defillama.com/chain/MANTRA)
- [Tier A] CoinGecko `mantra`; pump days from Binance OMUSDT (÷4) to 2 Mar 2026, then MANTRAUSDT
- [Tier B] Press coverage of the Apr 2025 crash
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): OM token contract labelled MANTRA; no Association wallets found; MANTRA Chain not covered

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 1:4 split, genesis allocation, vesting | [docs](https://docs.mantrachain.io/mantra-tokenomics) | A | 16 Nov 2026 |
| TVL $494k | [DefiLlama](https://defillama.com/chain/MANTRA) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Association and contributor wallet flows to exchanges** | Arkham does not cover MANTRA Chain. Use a public MANTRA explorer or ask the Association for its addresses | Free |
| 2 | **Chain fee revenue** | Sum the native fees from a chain indexer | Free |
| 3 | **Pump-day test on exchange prices.** No Gate, MEXC, KuCoin or Kraken USDT series with a full year was returned on 16 Nov 2026 (Binance blocks this region) | Re-run scripts/pump_day_test.py on the first exchange in the price-source order that lists the token | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
