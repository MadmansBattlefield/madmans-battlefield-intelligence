---
ticker: ORAI
name: Oraichain
chain: oraichain
contract: "native coin (Oraichain); 0x4c11249814f11b9346808179cf06e71ac328c1b5 (Ethereum, mostly burned); 0xa325ad6d9c92b55a3fc5ad7e412b1518f96441c0 (BNB Chain)"
overall_score: 3.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 4
  adoption_customers: 3
  security_audits: 1
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: 8-9 Aug 2026 unauthorized ORAI mint through an EVM cross-chain path; chain halted and restored; ~3.9M attacker ORAI traced to MEXC and KuCoin, return unresolved"
  mint_path_live: "yes: 7% annual inflation; on-chain supply 19.94M is above the 19.78M max in the docs"
  team_wallet_to_exchange_during_pump: "not proven: Cosmos chain with unlabelled top holders; not traced"
  entity_concentration: "top 4 liquid accounts hold ~2.6M ORAI (13%), owners unlabelled"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The Quant Terminal fee isn't charged and the 30% buyback starts only at $1,000 a day of revenue, so revenue does not reach holders."
pump_day_price_source: "MEXC ORAIUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.318253
price_source: "CoinGecko, 16 Nov 2026 ~10:05 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ORAI · Overall grade **3.0 / 10 · ❌ FAIL**

**Summary:** Oraichain is a Cosmos-based "AI layer 1" that has pivoted to an AI quant-trading terminal. In August 2026 an attacker used a flaw in its EVM cross-chain path to mint unauthorised ORAI, and the chain was halted and rebuilt. About 3.9M attacker ORAI reached MEXC and KuCoin, and getting it back is still unresolved. Supply on the chain now sits above the documented maximum and grows 7% a year. The network earns nothing yet: the planned terminal fee isn't being charged. The revenue gate fails.

**🚨 Top warning:** **an unauthorised-mint exploit in Aug 2026.** On 8–9 Aug, a flaw in the EVM cross-chain transfer path let an attacker mint ORAI. The network was halted and restored, but about **3.9M attacker ORAI** (~$1.2M today, roughly 20% of supply) was traced to MEXC and KuCoin, and freezing and returning it is still unresolved ([Oraichain announcement](https://tg.me/oraichain_official/1767), [Bridge Incident Registry](https://bir.badjoke-lab.com/incident/oraichain-2026-evm-cross-chain-unauthorized-mint/)). On-chain supply is now **19.94M**, above the 19.78M max in Oraichain's docs. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 1/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ORAI · Oraichain · 3.0 / 10 · ❌ FAIL

> **One line:** An AI-pivot Cosmos chain with no revenue, 7% inflation and an unresolved 2026 minting exploit.

| 📊 Market (CoinGecko, 16 Nov 2026 ~10:05 AM MST) | 🔗 Chain (Oraichain LCD and scan.orai.io) |
|---|---|
| **Price** $0.3183 | **Supply on chain** 19,938,591 ORAI (docs max 19,779,272) |
| **24h / 7d / 30d** 🟢 +5.1% / 🟢 +3.7% / 🔴 −37.3% | **Inflation** 7.00% a year |
| **Market cap** $6.19M · **FDV** $6.29M | **Staked** 5.65M ORAI bonded |
| **24h volume** $0.13M (MEXC $58k, Bittime $30k, KuCoin $25k, Gate, Crypto.com) | **Top liquid holders** 909k, 581k, 576k, 542k ORAI (unlabelled) |
| **ATH** $105.76 (19 Feb 2021) · now −99.7% | |
| **Pump days** 54 in the last year (MEXC ORAIUSDT; largest +121.6% on 17 Feb 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- Nothing yet. A 0.01% Quant Terminal fee isn't being charged, and buybacks (30% of revenue) start only once revenue reaches $1,000 a day ([Oraichain FAQ](https://oraichain.notion.site/Oraichain-H1-2026-Roadmap-FAQs-2fb248af3290802bb43dfb6c73c5c21e)). **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The Quant Terminal fee isn't charged and the 30% buyback starts only at $1,000 a day of revenue, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- An active team, but strategy keeps changing (the 2025 token consolidation in proposal 319). A post-exploit security patch shipped as a binary only, with no source code [Tier B, one source].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- The DAO treasury holds 161,550 ORAI ([proposal 319](https://scan.orai.io/proposals/319)). The top liquid accounts are unlabelled. Proposal 319 allocated 1.5M ORAI to the Quant Terminal and 1M to block rewards.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Oraichain is a Cosmos chain with no public exchange labels, and the top holders aren't identified, so this wasn't traced. With 54 pump days in the year → **not proven, 4.**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC ORAIUSDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 7% inflation, about 1.4M ORAI a year, and supply now above the documented maximum.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.13M a day. MEXC and KuCoin are also where the attacker's ORAI went.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Quant Terminal, AI agents and DeFi apps, all small.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Little sign of demand beyond trading.

## 🛡️ Security & audits · 1/10 · ❌ FAIL

- Unauthorised minting in Aug 2026, a chain halt and restoration, with attacker funds still outstanding ([announcement](https://tg.me/oraichain_official/1767)). **1.**

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Freezes or returns of the attacker's funds, and the Quant Terminal fee switch.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Unauthorised mint, 8–9 Aug 2026 |
| Team wallet → exchange during a pump | ⚪ Not proven (not traced) |
| Live mint path | 🔴 7% inflation; supply above documented max |
| Entity concentration | 🟡 Top 4 liquid accounts ~13%, unlabelled |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Top four liquid accounts (Cosmos) | Unlabelled | scan.orai.io; no Arkham coverage | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): not used: Arkham does not cover the Oraichain Cosmos chain
- [Tier A] [Oraichain update on the Aug 8–9 incident](https://tg.me/oraichain_official/1767), [Proposal 319](https://scan.orai.io/proposals/319), [H1 2026 roadmap FAQ](https://oraichain.notion.site/Oraichain-H1-2026-Roadmap-FAQs-2fb248af3290802bb43dfb6c73c5c21e)
- [Tier A] Oraichain LCD (supply, inflation, staking pool) and scan.orai.io account rankings
- [Tier B] [Bridge Incident Registry](https://bir.badjoke-lab.com/incident/oraichain-2026-evm-cross-chain-unauthorized-mint/), [Phemex Academy](https://phemex.com/academy/oraichain)
- [Tier A] CoinGecko `oraichain-token` (market, venues); pump days from MEXC ORAIUSDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Unauthorised mint, ~3.9M ORAI to MEXC and KuCoin | [Oraichain](https://tg.me/oraichain_official/1767), [registry](https://bir.badjoke-lab.com/incident/oraichain-2026-evm-cross-chain-unauthorized-mint/) | A+B | 16 Nov 2026 |
| Supply 19.94M, inflation 7% | Oraichain LCD `supply/by_denom`, `mint/inflation` | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owners of the top four liquid accounts** | Ask Oraichain or check scan.orai.io labels; Arkham does not cover the Oraichain Cosmos chain (16 Nov 2026) | Free |
| 2 | **Outcome of the MEXC and KuCoin freeze requests** | Follow Oraichain announcements | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
