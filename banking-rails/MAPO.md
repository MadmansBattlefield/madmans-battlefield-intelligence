---
ticker: MAPO
name: MAP Protocol
chain: ethereum
contract: "0x7046933234a82af77f14625e8d0fa9bcc5044a7e"
overall_score: 3.3
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
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
  team_wallet_to_exchange_during_pump: "not tested: holders unlabelled"
  one_hop_sale_status: none_found
  entity_concentration: "~92% of the ERC-20 in three unlabelled EOAs (low confidence)"
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
    label: "Unlabelled EOA (49.93% of ERC-20)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan getsourcecode"
  - address: "0xbddf646c54576be4573636e7fe328168dd107738"
    label: "Unlabelled EOA (24.26% of ERC-20)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan getsourcecode"
  - address: "0x4a83b4917a8a4ea4dcb40efb44944a2880447466"
    label: "Unlabelled EOA (18.07% of ERC-20)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan getsourcecode"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MAPO · Overall grade **3.3 / 10 · ❌ FAIL**

**Summary:** MAP Protocol is a cross-chain interoperability chain; MAPO is its native coin, with ERC-20 and BEP-20 versions. No fee or revenue record on DefiLlama and none published by the project was found. Only 335 addresses hold the Ethereum version, and three unlabelled wallets hold ~92% of it. Those owners are low confidence and do not move the scores. MAPO is down 79% in a year. The Revenue gate fails.

**🚨 Top warning:** **Three unlabelled wallets hold ~92% of the Ethereum MAPO:** [`0x687c…459e`](https://etherscan.io/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) 49.93% (EOA), [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) 24.26% (EOA) and [`0x4a83…7466`](https://etherscan.io/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) 18.07% (EOA). They may be bridge or exchange reserves; this is low confidence and goes to the Arkham batch.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
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


# 🪪 MAPO · MAP Protocol · 3.3 / 10 · ❌ FAIL

> **One line:** A cross-chain chain with no holder revenue, a thin ERC-20 and unlabelled reserves.

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

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0x687c…459e`](https://etherscan.io/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) 49.93% (EOA), [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) 24.26% (EOA) and [`0x4a83…7466`](https://etherscan.io/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) 18.07% (EOA) are unlabelled. Low confidence, so not used; not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The large ERC-20 holders are unlabelled, and native-chain team wallets are unpublished.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

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
| Team wallet → exchange during a pump | ⚪ Not tested: holders unlabelled |
| Entity concentration | 🔴 ~92% of the ERC-20 in three unlabelled EOAs |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x687c…459e`](https://etherscan.io/address/0x687c802162e79ad95309df8eedcb8e814c7f459e) | Unlabelled EOA (49.93% of ERC-20) | Ethplorer + Etherscan getsourcecode | low | no | None: cannot move Holdings or Selling |
| [`0xbddf…7738`](https://etherscan.io/address/0xbddf646c54576be4573636e7fe328168dd107738) | Unlabelled EOA (24.26% of ERC-20) | Ethplorer + Etherscan getsourcecode | low | no | None: cannot move Holdings or Selling |
| [`0x4a83…7466`](https://etherscan.io/address/0x4a83b4917a8a4ea4dcb40efb44944a2880447466) | Unlabelled EOA (18.07% of ERC-20) | Ethplorer + Etherscan getsourcecode | low | no | None: cannot move Holdings or Selling |

## 📚 Sources

- [Tier A] [CoinGecko `marcopolo`](https://www.coingecko.com/en/coins/marcopolo): price, supply, venues and description, read 16 Nov 2026
- [Tier A] MEXC MAPOUSDT UTC daily closes via `scripts/pump_day_test.py` (25 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x7046933234a82af77f14625e8d0fa9bcc5044a7e#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
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
