---
ticker: BKN
name: Brickken
chain: ethereum
contract: "0xfc209eeba3d744aa741cc5c2a73ebf9c977b5f82"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 5
  adoption_customers: 4
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: holders unlabelled"
  one_hop_sale_status: none_found
  entity_concentration: "~62% of the ERC-20 in three unlabelled wallets (low confidence)"
price_usd: 0.069522
price_source: "CoinGecko `brickken`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "MEXC BKNUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x366ea78b24ed81bafae37f2b0b4c63b3f24bf0bd"
    label: "Unlabelled Safe (30%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan"
  - address: "0x8f523d7e1acbbc6d0e3ca19b7d8c1981b346ceb8"
    label: "Unlabelled EOA (18.91%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan"
  - address: "0x0e35e6dac22669be00d73072e4cebaa9550dadd3"
    label: "Unlabelled Safe (12.7%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan"
  - address: "0x9642b23ed1e01df1092b92641051881a322f5d4e"
    label: "MEXC 16"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan public name tag"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BKN · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** Brickken sells a tokenization toolkit for businesses. No fee or revenue record on DefiLlama and none published by the project was found. Its software income is company revenue. Two unlabelled Safes hold 30% and 12.7% of the Ethereum supply and an unlabelled EOA 18.9%; Etherscan labels a 6.7% holder MEXC 16. BKN is down 40% in a year. The Revenue gate fails.

**🚨 Top warning:** **~62% of the Ethereum supply sits in three unlabelled wallets:** Safe [`0x366e…f0bd`](https://etherscan.io/address/0x366ea78b24ed81bafae37f2b0b4c63b3f24bf0bd) 30%, [`0x8f52…ceb8`](https://etherscan.io/address/0x8f523d7e1acbbc6d0e3ca19b7d8c1981b346ceb8) 18.91% (EOA) and Safe [`0x0e35…add3`](https://etherscan.io/address/0x0e35e6dac22669be00d73072e4cebaa9550dadd3) 12.7%. Probably company or vesting wallets, but unlabelled, so low confidence.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BKN · Brickken · 3.4 / 10 · ❌ FAIL

> **One line:** A tokenization-software company's token with no claim on its income.

| 📊 Market (CoinGecko `brickken`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.0695 | **ERC-20 holders** 1,196 |
| **7d / 30d / 1y** 🔴 −3.8% / 🔴 −29.1% / 🔴 −39.5% | **Top** Safe 30% · EOA 18.9% · Safe 12.7% |
| **Market cap** $6.99M · **FDV** $10.5M | **Supply** 100M circulating / 150M max |
| **24h volume** $45.9k (top venues: MEXC $39.7k, Uniswap V4 (Ethereum) $5.63k, Uniswap V4 (Ethereum) $1.45k) |  |
| **ATH** $1.39 (2024-03-28) |  |
| **Pump days** 51 of 360 days (MEXC BKNUSDT UTC daily closes); latest 2026-09-27, 2026-09-28 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found. Brickken's software fees are company revenue.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Brickken, Barcelona ([site](https://brickken.com/)); repo at [github.com/Brickken](https://github.com/Brickken).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Safe [`0x366e…f0bd`](https://etherscan.io/address/0x366ea78b24ed81bafae37f2b0b4c63b3f24bf0bd) 30%, [`0x8f52…ceb8`](https://etherscan.io/address/0x8f523d7e1acbbc6d0e3ca19b7d8c1981b346ceb8) 18.91% (EOA) and Safe [`0x0e35…add3`](https://etherscan.io/address/0x0e35e6dac22669be00d73072e4cebaa9550dadd3) 12.7% are unlabelled. [`0x9642…5d4e`](https://etherscan.io/address/0x9642b23ed1e01df1092b92641051881a322f5d4e) 6.7% is Etherscan-labelled MEXC 16. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The large holders are unlabelled and no team wallet is published.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC BKNUSDT UTC daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 100M of 150M circulating; 50M still to unlock.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~$46k a day, mostly MEXC.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Token Suite product live; public repo.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Client counts are self-reported [Tier B].

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- EU (Spain) company; no enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Remaining 50M unlock; schedule not verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: holders unlabelled |
| Entity concentration | 🔴 ~62% in three unlabelled wallets |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x366e…f0bd`](https://etherscan.io/address/0x366ea78b24ed81bafae37f2b0b4c63b3f24bf0bd) | Unlabelled Safe (30%) | Ethplorer + Etherscan | low | no | None: cannot move Holdings or Selling |
| [`0x8f52…ceb8`](https://etherscan.io/address/0x8f523d7e1acbbc6d0e3ca19b7d8c1981b346ceb8) | Unlabelled EOA (18.91%) | Ethplorer + Etherscan | low | no | None: cannot move Holdings or Selling |
| [`0x0e35…add3`](https://etherscan.io/address/0x0e35e6dac22669be00d73072e4cebaa9550dadd3) | Unlabelled Safe (12.7%) | Ethplorer + Etherscan | low | no | None: cannot move Holdings or Selling |
| [`0x9642…5d4e`](https://etherscan.io/address/0x9642b23ed1e01df1092b92641051881a322f5d4e) | MEXC 16 | Etherscan public name tag | medium | no | None: exchange custody |

## 📚 Sources

- [Tier A] [CoinGecko `brickken`](https://www.coingecko.com/en/coins/brickken): price, supply, venues and description, read 16 Nov 2026
- [Tier A] MEXC BKNUSDT UTC daily closes via `scripts/pump_day_test.py` (51 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0xfc209eeba3d744aa741cc5c2a73ebf9c977b5f82#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `brickken`](https://www.coingecko.com/en/coins/brickken) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0xfc209eeba3d744aa741cc5c2a73ebf9c977b5f82) · [holders](https://etherscan.io/token/0xfc209eeba3d744aa741cc5c2a73ebf9c977b5f82#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the two Safes and the 18.9% EOA** | Read the Safes' signers; Arkham entity lookup | Free / Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
