---
ticker: MAPO
name: MAP Protocol
chain: ethereum
contract: "0x7046933234a82af77f14625e8d0fa9bcc5044a7e"
overall_score: 3.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: Map Labs-linked wallets show no MAPO exchange sends on page 1"
  one_hop_sale_status: none_found
  entity_concentration: "~42% of the ERC-20 in Map Labs-linked wallets; 49.9% Coinone"
price_usd: 0.00076055
price_source: "CoinGecko `marcopolo`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "MEXC MAPOUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x687c802162e79ad95309df8eedcb8e814c7f459e"
    label: "Coinone (49.9%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0xbddf646c54576be4573636e7fe328168dd107738"
    label: "Map Labs-linked (24.3%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham related-entity label"
  - address: "0x4a83b4917a8a4ea4dcb40efb44944a2880447466"
    label: "Map Labs-linked deployer/LP wallet (18.1%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + 10 ETH funding from 0xbddf…7738"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MAPO · Overall grade **3.2 / 10 · ❌ FAIL**

**Summary:** MAP Protocol is a cross-chain interoperability chain; MAPO is its native coin, with ERC-20 and BEP-20 versions. No fee or revenue record on DefiLlama and none published by the project was found. Only 335 addresses hold the Ethereum version, and Coinone custody holds 49.9% while two Map Labs-linked wallets hold ~42% (Arkham, 16 Nov 2026). MAPO is down 79% in a year. The Revenue gate fails.

**🚨 Top warning:** **About 42% of the Ethereum MAPO is in wallets linked to Map Labs:** [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) 24.3% (Arkham ties it to Map Labs) and [`0x4a83…7466`](https://etherscan.io/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) 18.1% (funded from [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738)). The 49.9% holder [`0x687c…459e`](https://etherscan.io/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) is the exchange Coinone. The Map Labs-linked wallet has made Binance deposits, but in USDT, not MAPO.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 MAPO · MAP Protocol · 3.2 / 10 · ❌ FAIL

> **One line:** A cross-chain chain with no holder revenue, a thin ERC-20 and ~42% of it in Map Labs-linked wallets.

| 📊 Market (CoinGecko `marcopolo`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.000761 | **ERC-20 holders** 335 |
| **7d / 30d / 1y** 🔴 −21.4% / 🔴 −38.2% / 🔴 −79.3% | **Top wallet** `0x687c…459e` 49.93% (EOA) |
| **Market cap** $4.72M · **FDV** $7.38M | **Supply** 6.2B circulating / 10B max |
| **24h volume** $316k (top venues: HTX $227k, MEXC $152k, Bithumb $73.2k) |  |
| **ATH** $0.273 (2021-04-09) |  |
| **Pump days** 25 of 360 days (MEXC MAPOUSDT UTC daily closes); latest 2026-09-25, 2026-09-26 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- MAP Protocol ([site](https://www.mapprotocol.io/)); code at [github.com/mapprotocol](https://github.com/mapprotocol). CoinGecko lists it in the DWF Labs portfolio.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- [`0x687c…459e`](https://etherscan.io/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) (49.9%) is **Coinone** ([Arkham](https://arkm.com/explorer/address/0x687c802162e79ad95309df8eedcb8e814c7f459e)). Exchange custody is not insider holding.
- [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) (24.3%) is linked to **Map Labs** by Arkham ([Arkham](https://arkm.com/explorer/address/0xbddf646c54576be4573636e7fe328168dd107738)); it sent ~100k USDT twice to a Binance deposit address and received ~100k USDT from Kraken, but no MAPO went to an exchange on page 1.
- [`0x4a83…7466`](https://etherscan.io/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) (18.1%) is an old deployer or LP-operator wallet funded with 10 ETH from [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) ([Arkham](https://arkm.com/explorer/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466)).
- So roughly 42% of the ERC-20 sits with Map Labs-linked wallets: a large insider concentration.
- Score: **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The Map Labs-linked wallets sent no MAPO to an exchange on Arkham's page 1 (their Binance deposits were USDT); native-chain team wallets are unpublished.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass, including in the Arkham batch b24 read (16 Nov 2026).

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC MAPOUSDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 6.2B circulating of a 10B max; 3.8B still to enter circulation.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$0.3M a day, led by HTX and MEXC.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Public repos; relay chain live.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No independent bridge-volume figure was found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Remaining 3.8B supply to unlock; schedule not verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: Map Labs-linked wallets show no MAPO exchange sends on page 1 |
| Entity concentration | 🔴 ~42% of the ERC-20 in Map Labs-linked wallets; 49.9% Coinone |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x687c…459e`](https://etherscan.io/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) | Coinone (49.9%) | [Arkham](https://arkm.com/explorer/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) entity label | medium | no | Holdings: exchange custody, not insider |
| [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) | Map Labs-linked (24.3%) | [Arkham](https://arkm.com/explorer/address/0xbddf646c54576be4573636e7fe328168dd107738) related-entity label | medium | no | Holdings: insider-linked |
| [`0x4a83…7466`](https://etherscan.io/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) | Map Labs-linked deployer/LP wallet (18.1%) | [Arkham](https://arkm.com/explorer/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) + 10 ETH funding from 0xbddf…7738 | medium | no | Holdings: insider-linked |

## 📚 Sources

- [Tier A] [CoinGecko `marcopolo`](https://www.coingecko.com/en/coins/marcopolo): price, supply, venues and description, read 16 Nov 2026
- [Tier A] MEXC MAPOUSDT UTC daily closes via `scripts/pump_day_test.py` (25 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x7046933234a82af77f14625e8d0fa9bcc5044a7e#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0x687c…459e](https://arkm.com/explorer/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) · [0xbddf…7738](https://arkm.com/explorer/address/0xbddf646c54576be4573636e7fe328168dd107738) · [0x4a83…7466](https://arkm.com/explorer/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) | B | 16 Nov 2026 |
| Market data and venues | [CoinGecko `marcopolo`](https://www.coingecko.com/en/coins/marcopolo) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x7046933234a82af77f14625e8d0fa9bcc5044a7e) · [holders](https://etherscan.io/token/0x7046933234a82af77f14625e8d0fa9bcc5044a7e#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the three large ERC-20 wallets** | Arkham entity lookup | Arkham |
| 2 | **Unlock schedule for the remaining 3.8B** | Read MAP Protocol's tokenomics page and match it to native-chain transfers | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
