---
ticker: CTC
name: Creditcoin (CTC, ERC-20 G-CRE)
chain: ethereum
contract: "0xa3ee21c306a700e682abcdfe9baa6a08f3820419"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 5
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
  team_wallet_to_exchange_during_pump: "not tested: issuer wallets unpublished"
  one_hop_sale_status: none_found
  entity_concentration: "~86% of the ERC-20 in Upbit and Bithumb custody (exchange, not insider)"
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
    label: "Upbit: Cold Wallet (72.8%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0x43fddf6aa37848e87bb176407dafef2b8ca20a8a"
    label: "Bithumb: Hot Wallet (13.1%)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham entity label + Etherscan tag 'Bithumb 434'"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CTC · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** Creditcoin is a layer-1 for recording credit and lending history, developed by Gluwa. The exchange-traded CTC is an Ethereum ERC-20 (G-CRE) that converts to the native coin. No fee or revenue record on DefiLlama and none published by the project was found. On Ethereum the 72.8% and 13.1% holders of the ERC-20 are the Upbit cold wallet and a Bithumb hot wallet (Arkham, 16 Nov 2026), so the concentration is exchange custody; Gluwa's own wallets are still unpublished. CTC is down 80% in a year. The Revenue gate fails.

**🚨 Top warning:** **About 86% of the ERC-20 CTC (G-CRE) sits on two Korean exchanges, not with insiders:** [`0xca4d…7527`](https://etherscan.io/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) 72.8% is the Upbit cold wallet ([Arkham](https://arkm.com/explorer/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527)) and [`0x43fd…0a8a`](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) 13.1% is a Bithumb hot wallet ([Arkham](https://arkm.com/explorer/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a); Etherscan tag "Bithumb 434"). Gluwa's own wallets are still unpublished, so insider selling cannot be tested.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
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


# 🪪 CTC · Creditcoin (CTC, ERC-20 G-CRE) · 3.7 / 10 · ❌ FAIL

> **One line:** A credit-history chain whose token earns nothing and whose ERC-20 supply sits mostly on Upbit and Bithumb.

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

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

- [`0xca4d…7527`](https://etherscan.io/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) (72.8%) is **Upbit: Cold Wallet**, fed only by Upbit hot wallets ([Arkham](https://arkm.com/explorer/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527), entity label, read 16 Nov 2026). Exchange custody is not insider holding.
- [`0x43fd…0a8a`](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) (13.1%) is a **Bithumb hot wallet** that sweeps Bithumb deposit addresses ([Arkham](https://arkm.com/explorer/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a); Etherscan tag "Bithumb 434", [Etherscan](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a)).
- So the large unexplained concentration flagged earlier was exchange custody. Gluwa's team and treasury wallets are still not mapped; the native-chain holdings were not read.
- Score: **5**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The two large ERC-20 wallets are Upbit and Bithumb custody (Arkham b24), not insiders; Gluwa's own wallets are unpublished.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass, including in the Arkham batch b24 read (16 Nov 2026).

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
| Team wallet → exchange during a pump | ⚪ Not tested: issuer wallets unpublished |
| Entity concentration | 🟡 ~86% of the ERC-20 in Upbit and Bithumb custody (exchange, not insider) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xca4d…7527`](https://etherscan.io/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) | Upbit: Cold Wallet (72.8%) | [Arkham](https://arkm.com/explorer/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) entity label | medium | no | Holdings: exchange custody, not insider |
| [`0x43fd…0a8a`](https://etherscan.io/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) | Bithumb: Hot Wallet (13.1%) | [Arkham](https://arkm.com/explorer/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) entity label + Etherscan tag "Bithumb 434" | high | yes | Holdings: exchange custody, not insider |

## 📚 Sources

- [Tier A] [CoinGecko `creditcoin-2`](https://www.coingecko.com/en/coins/creditcoin-2): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate CTC_USDT UTC daily closes via `scripts/pump_day_test.py` (27 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0xa3ee21c306a700e682abcdfe9baa6a08f3820419#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0xca4d…7527](https://arkm.com/explorer/address/0xca4d316e78ae09c026fde872b1fa1fece7ee7527) · [0x43fd…0a8a](https://arkm.com/explorer/address/0x43fddf6aa37848e87bb176407dafef2b8ca20a8a) | B | 16 Nov 2026 |
| Market data and venues | [CoinGecko `creditcoin-2`](https://www.coingecko.com/en/coins/creditcoin-2) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0xa3ee21c306a700e682abcdfe9baa6a08f3820419) · [holders](https://etherscan.io/token/0xa3ee21c306a700e682abcdfe9baa6a08f3820419#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Gluwa team and treasury wallets** | Resolved: the 72.8% and 13.1% wallets are Upbit and Bithumb (Arkham b24). Next: ask Gluwa for its own wallets | Free |
| 2 | **Native-chain team wallets** | Ask the Creditcoin Foundation to publish them | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
