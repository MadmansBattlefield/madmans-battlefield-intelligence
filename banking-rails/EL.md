---
ticker: EL
name: ELYSIA
chain: ethereum
contract: "0x2781246fe707bb15cee3e5ea354e2154a2877b16"
overall_score: 3.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 3
  adoption_customers: 2
  security_audits: 5
  regulatory: 4
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not proven: large holders unlabelled"
  one_hop_sale_status: none_found
  entity_concentration: "~90% in three unlabelled addresses (low confidence)"
price_usd: 0.00124646
price_source: "CoinGecko `elysia`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "Gate EL_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x1b1318c3ec104799de21e4ce2284c3de52a1e452"
    label: "Unlabelled EOA (67.6%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + eth_getCode"
  - address: "0x796bdc018d9a903acca191e6cae6bb300c662674"
    label: "Gnosis Safe (12.6%)"
    confidence: low
    independent_corroboration: false
    basis: "Etherscan ContractName"
  - address: "0xed5d35dc902c543b33496f6feae27b7866525b4f"
    label: "Gnosis Safe (10.3%)"
    confidence: low
    independent_corroboration: false
    basis: "Etherscan ContractName"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EL · Overall grade **3.0 / 10 · ❌ FAIL**

**Summary:** ELYSIA is a 2021-era real-estate tokenization platform. No fee or revenue record on DefiLlama and none published by the project was found. One unlabelled wallet holds 67.6% of EL and two Safes hold 12.6% and 10.3%, so ~90% sits in three addresses that are not labelled. The token is down 98% from its 2021 high. The Revenue gate fails.

**🚨 Top warning:** **~90% of supply sits in three unlabelled addresses**: [`0x1b13…e452`](https://etherscan.io/address/0x1b1318c3ec104799de21e4ce2284c3de52a1e452) 67.6% (EOA), Safe [`0x796b…2674`](https://etherscan.io/address/0x796bdc018d9a903acca191e6cae6bb300c662674) 12.59% (Gnosis Safe) and Safe [`0xed5d…5b4f`](https://etherscan.io/address/0xed5d35dc902c543b33496f6feae27b7866525b4f) 10.29% (Gnosis Safe). The contract owner `0x8acf…76c4` is also the deployer. None is labelled, so this is low confidence.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EL · ELYSIA · 3.0 / 10 · ❌ FAIL

> **One line:** A real-estate token with no measurable revenue and ~90% of supply in three unlabelled wallets.

| 📊 Market (CoinGecko `elysia`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00125 | **Holders** 2,775 |
| **7d / 30d / 1y** 🔴 −6.7% / 🔴 −22.2% / 🔴 −50.6% | **Top** `0x1b13…e452` 67.6% (EOA) |
| **Market cap** $8.48M · **FDV** $8.48M | **Safes** 12.6% + 10.3% |
| **24h volume** $515k (top venues: MEXC $233k, Gate $171k, XT.COM $111k) | **Owner/deployer** `0x8acf…76c4` |
| **ATH** $0.0691 (2021-04-01) |  |
| **Pump days** 40 of 360 days (Gate EL_USDT UTC daily closes); latest 2026-10-08, 2026-10-12 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- ELYSIA ([site](https://elysia.land)); the operating entity and team were not verified in this pass.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0x1b13…e452`](https://etherscan.io/address/0x1b1318c3ec104799de21e4ce2284c3de52a1e452) 67.6% (EOA), [`0x796b…2674`](https://etherscan.io/address/0x796bdc018d9a903acca191e6cae6bb300c662674) 12.59% (Safe), [`0xed5d…5b4f`](https://etherscan.io/address/0xed5d35dc902c543b33496f6feae27b7866525b4f) 10.29% (Safe). Unlabelled, so low confidence; not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The large holders are unlabelled.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate EL_USDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 6.80B circulating of 7B max; ~90% in three addresses.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$0.5M a day on MEXC, Gate and XT.COM; on-chain liquidity is negligible (~$275 a day on Uniswap).

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- Code at [github.com/elysia-dev](https://github.com/elysia-dev); recent activity not verified.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No current property or user figures found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- Real-estate tokens are securities-like in most places; no licence found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None found.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: holders unlabelled |
| Entity concentration | 🔴 ~90% in three unlabelled addresses |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x1b13…e452`](https://etherscan.io/address/0x1b1318c3ec104799de21e4ce2284c3de52a1e452) | Unlabelled EOA (67.6%) | Ethplorer + eth_getCode | low | no | None |
| [`0x796b…2674`](https://etherscan.io/address/0x796bdc018d9a903acca191e6cae6bb300c662674) | Gnosis Safe (12.6%) | Etherscan ContractName | low | no | None |
| [`0xed5d…5b4f`](https://etherscan.io/address/0xed5d35dc902c543b33496f6feae27b7866525b4f) | Gnosis Safe (10.3%) | Etherscan ContractName | low | no | None |

## 📚 Sources

- [Tier A] [CoinGecko `elysia`](https://www.coingecko.com/en/coins/elysia): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate EL_USDT UTC daily closes via `scripts/pump_day_test.py` (40 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x2781246fe707bb15cee3e5ea354e2154a2877b16#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `elysia`](https://www.coingecko.com/en/coins/elysia) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x2781246fe707bb15cee3e5ea354e2154a2877b16) · [holders](https://etherscan.io/token/0x2781246fe707bb15cee3e5ea354e2154a2877b16#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owners of the three large addresses** | Arkham lookup; ask ELYSIA to publish treasury wallets | Arkham |
| 2 | **Mint or owner powers** | Read the verified contract for owner-only functions | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
