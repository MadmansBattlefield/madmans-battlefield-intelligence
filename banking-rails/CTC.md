---
ticker: CTC
name: Creditcoin (CTC, ERC-20 G-CRE)
chain: ethereum
contract: "0xa3ee21c306a700e682abcdfe9baa6a08f3820419"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 5
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: issuer wallets unlabelled"
  one_hop_sale_status: none_found
  entity_concentration: "~86% of the ERC-20 in two unlabelled EOAs (low confidence)"
price_usd: 0.067413
price_source: "CoinGecko `creditcoin-2`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found; staking rewards are issuance."
pump_day_price_source: "Gate CTC_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xca4d316e78ae09c026fde872b1fa1fece7ee7527"
    label: "Unlabelled EOA (72.8% of ERC-20)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan eth_getCode"
  - address: "0x43fddf6aa37848e87bb176407dafef2b8ca20a8a"
    label: "Unlabelled EOA (13.1%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CTC · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** Creditcoin is a layer-1 for recording credit and lending history, developed by Gluwa. The exchange-traded CTC is an Ethereum ERC-20 (G-CRE) that converts to the native coin. No fee or revenue record on DefiLlama and none published by the project was found. On Ethereum one unlabelled wallet holds 72.8% of the ERC-20 supply and a second holds 13.1%. Their owners are not labelled, so they are low confidence and do not move the scores. CTC is down 80% in a year. The Revenue gate fails.

**🚨 Top warning:** **Two unlabelled wallets hold ~86% of the ERC-20 supply:** [`0xca4d…7527`](https://etherscan.io/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) 72.82% (EOA) and [`0x43fd…0a8a`](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) 13.06% (EOA). They are probably issuer or bridge reserves, but nothing on-chain labels them, so this is low confidence and goes to the Arkham batch.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CTC · Creditcoin (CTC, ERC-20 G-CRE) · 3.6 / 10 · ❌ FAIL

> **One line:** A credit-history chain whose token earns nothing and whose ERC-20 supply sits in two unlabelled wallets.

| 📊 Market (CoinGecko `creditcoin-2`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.0674 | **ERC-20 holders** 852,184 |
| **7d / 30d / 1y** 🔴 −14.9% / 🔴 −27.0% / 🔴 −80.0% | **Top wallet** `0xca4d…7527` 72.8% (EOA) |
| **Market cap** $37M · **FDV** $40.4M | **Second** `0x43fd…0a8a` 13.1% (EOA) |
| **24h volume** $1.16M (top venues: HTX $701k, Upbit $285k, Bithumb $123k) | **Supply** 550M circulating / 600M total |
| **ATH** $8.67 (2021-03-13) |  |
| **Pump days** 27 of 360 days (Gate CTC_USDT UTC daily closes); latest 2026-09-25, 2026-10-27 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found; staking rewards are issuance.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Developed by Gluwa with the Creditcoin Foundation ([site](https://creditcoin.org/)); code at [github.com/gluwa/Creditcoin](https://github.com/gluwa/Creditcoin).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0xca4d…7527`](https://etherscan.io/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) 72.82% (EOA) and [`0x43fd…0a8a`](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) 13.06% (EOA) are plain EOAs with no label. They could be the issuer's conversion reserve or an exchange. Low confidence, so not used; not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The two large ERC-20 wallets are unlabelled; outflows were not traced to labelled exchanges.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate CTC_USDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 550M circulating of 600M total (CoinGecko). The ERC-20 is a vesting/bridge representation of the native coin, so on-chain concentration may reflect conversion reserves.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

- ~$1.2M a day, led by HTX, Upbit and Bithumb (KRW).

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Public repo; the chain is live. Usage metrics were not found on DefiLlama.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No independent loan-volume figure was found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found; heavy Korean-exchange trading.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- None verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: issuer wallets unlabelled |
| Entity concentration | 🔴 ~86% of the ERC-20 in two unlabelled EOAs |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xca4d…7527`](https://etherscan.io/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) | Unlabelled EOA (72.8% of ERC-20) | Ethplorer + Etherscan eth_getCode | low | no | None: cannot move Holdings or Selling |
| [`0x43fd…0a8a`](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) | Unlabelled EOA (13.1%) | Ethplorer | low | no | None |

## 📚 Sources

- [Tier A] [CoinGecko `creditcoin-2`](https://www.coingecko.com/en/coins/creditcoin-2): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate CTC_USDT UTC daily closes via `scripts/pump_day_test.py` (27 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0xa3ee21c306a700e682abcdfe9baa6a08f3820419#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `creditcoin-2`](https://www.coingecko.com/en/coins/creditcoin-2) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0xa3ee21c306a700e682abcdfe9baa6a08f3820419) · [holders](https://etherscan.io/token/0xa3ee21c306a700e682abcdfe9baa6a08f3820419#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the 72.8% and 13.1% wallets** | Arkham entity lookup; compare with Gluwa's published conversion addresses | Arkham |
| 2 | **Native-chain team wallets** | Ask the Creditcoin Foundation to publish them | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
