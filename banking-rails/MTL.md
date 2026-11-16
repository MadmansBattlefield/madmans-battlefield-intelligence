---
ticker: MTL
name: Metal DAO
chain: ethereum
contract: "0xf433089366899d83a9f26a773d59ec7ecf30355e"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 5
  adoption_customers: 4
  security_audits: 5
  regulatory: 4
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: holders unlabelled"
  one_hop_sale_status: none_found
  entity_concentration: "~79% of the ERC-20 in two unlabelled EOAs (low confidence)"
price_usd: 0.220448
price_source: "CoinGecko `metal`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Holding MTL gives Metal Pay fee discounts, which is a utility, not revenue. No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "Gate MTL_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xaefd771ebcd045675006f466818f371721746573"
    label: "Unlabelled EOA (61.14% of ERC-20)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan getsourcecode"
  - address: "0x1a653e69fd7a4fbbff359026dd3aa1de1d5eee65"
    label: "Unlabelled EOA (18.12% of ERC-20)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan getsourcecode"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MTL · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** Metal DAO's MTL governs the Metal Dollar (XMD) and gives fee discounts in the Metal Pay app; it also has a Metal L2 version. No fee or revenue record on DefiLlama and none published by the project was found. On Ethereum one unlabelled wallet holds 61% of the ERC-20 and another holds 18%. They are low confidence and do not move the scores. MTL is down 47% in a year. The Revenue gate fails.

**🚨 Top warning:** **Two unlabelled wallets hold ~79% of the Ethereum MTL:** [`0xaefd…6573`](https://etherscan.io/address/0xaefd771ebcd045675006f466818f371721746573) 61.14% (EOA) and [`0x1a65…ee65`](https://etherscan.io/address/0x1a653e69fd7a4fbbff359026dd3aa1de1d5eee65) 18.12% (EOA). They may be company, bridge or exchange wallets; low confidence, so they go to the Arkham batch.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MTL · Metal DAO · 3.5 / 10 · ❌ FAIL

> **One line:** A payments-app token with discounts but no revenue reaching holders.

| 📊 Market (CoinGecko `metal`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.22 | **ERC-20 holders** 10,963 |
| **7d / 30d / 1y** 🔴 −9.4% / 🔴 −18.3% / 🔴 −47.5% | **Top wallet** `0xaefd…6573` 61.14% (EOA) |
| **Market cap** $20.7M · **FDV** $20.7M | **Supply** 94M circulating |
| **24h volume** $360k (top venues: HTX $592k, Binance $97.6k, Pionex $89.1k) |  |
| **ATH** $17 (2018-06-20) |  |
| **Pump days** 15 of 360 days (Gate MTL_USDT UTC daily closes); latest 2026-09-25, 2026-09-26 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found. Metal Pay's company income does not reach MTL.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Holding MTL gives Metal Pay fee discounts, which is a utility, not revenue. No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Metal Pay / Metal DAO ([site](https://www.metalpay.com/)); code at [github.com/MetalPay](https://github.com/MetalPay).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0xaefd…6573`](https://etherscan.io/address/0xaefd771ebcd045675006f466818f371721746573) 61.14% (EOA) and [`0x1a65…ee65`](https://etherscan.io/address/0x1a653e69fd7a4fbbff359026dd3aa1de1d5eee65) 18.12% (EOA) are unlabelled. Low confidence, so not used; not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The large ERC-20 holders are unlabelled and no company wallet is published.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate MTL_USDT UTC daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 94M circulating, no further issuance per CoinGecko.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- ~$0.36M a day, led by HTX, Binance and Pionex.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Metal Pay app live; Metal L2 launched.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- App usage is self-reported only [Tier B].

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- US company; no token enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: holders unlabelled |
| Entity concentration | 🔴 ~79% of the ERC-20 in two unlabelled EOAs |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xaefd…6573`](https://etherscan.io/address/0xaefd771ebcd045675006f466818f371721746573) | Unlabelled EOA (61.14% of ERC-20) | Ethplorer + Etherscan getsourcecode | low | no | None: cannot move Holdings or Selling |
| [`0x1a65…ee65`](https://etherscan.io/address/0x1a653e69fd7a4fbbff359026dd3aa1de1d5eee65) | Unlabelled EOA (18.12% of ERC-20) | Ethplorer + Etherscan getsourcecode | low | no | None: cannot move Holdings or Selling |

## 📚 Sources

- [Tier A] [CoinGecko `metal`](https://www.coingecko.com/en/coins/metal): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate MTL_USDT UTC daily closes via `scripts/pump_day_test.py` (15 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0xf433089366899d83a9f26a773d59ec7ecf30355e#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `metal`](https://www.coingecko.com/en/coins/metal) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0xf433089366899d83a9f26a773d59ec7ecf30355e) · [holders](https://etherscan.io/token/0xf433089366899d83a9f26a773d59ec7ecf30355e#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the 61% and 18% wallets** | Arkham entity lookup | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
