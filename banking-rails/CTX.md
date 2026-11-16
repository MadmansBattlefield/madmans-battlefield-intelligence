---
ticker: CTX
name: Cryptex Finance
chain: ethereum
contract: "0x321c2fe4446c7c963dc41dd58879af648838f98d"
overall_score: 3.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 1
  product_development: 4
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: no exchange USDT series; holders unlabelled"
  one_hop_sale_status: none_found
  entity_concentration: "~45% in two unlabelled EOAs (low confidence)"
price_usd: 0.361322
price_source: "CoinGecko `cryptex-finance`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No automatic burn, buyback or fee share to CTX was verified."
pump_day_price_source: "not run (no Gate, MEXC, KuCoin or Kraken USDT series)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x97f70ed4a8e606c6f6ae578ee27c4e3fadbc81aa"
    label: "Unlabelled EOA (32.79%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan"
  - address: "0x9c50d0d2053eebd48e6edaf1c2e39bb1d503b9bf"
    label: "Unlabelled EOA (12.22%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CTX · Overall grade **3.2 / 10 · ❌ FAIL**

**Summary:** CTX governs Cryptex, issuer of the TCAP crypto-market-cap index token. No fee or revenue record on DefiLlama and none published by the project was found. One unlabelled wallet holds 32.8% of supply and another 12.2%. Trading is thin (~$31k a day, mostly Coinbase). CTX is down 68% in a year. The Revenue gate fails.

**🚨 Top warning:** **One unlabelled wallet holds a third of supply:** [`0x97f7…81aa`](https://etherscan.io/address/0x97f70ed4a8e606c6f6ae578ee27c4e3fadbc81aa) 32.79% (EOA), plus [`0x9c50…b9bf`](https://etherscan.io/address/0x9c50d0d2053eebd48e6edaf1c2e39bb1d503b9bf) 12.22% (EOA). Possibly the DAO treasury, but unlabelled, so low confidence.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CTX · Cryptex Finance · 3.2 / 10 · ❌ FAIL

> **One line:** A small DeFi governance token with no holder revenue and concentrated supply.

| 📊 Market (CoinGecko `cryptex-finance`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.361 | **ERC-20 holders** 3,239 |
| **7d / 30d / 1y** 🔴 −9.8% / 🔴 −27.8% / 🔴 −68.4% | **Top** `0x97f7…81aa` 32.79% · `0x9c50…b9bf` 12.22% |
| **Market cap** $3.49M · **FDV** $3.61M | **Supply** 9.65M of 10M |
| **24h volume** $31.4k (top venues: Coinbase Exchange $29.4k, Aero Slipstream (Ethereum) $1.4k, Gemini $650) |  |
| **ATH** $44.1 (2021-09-13) |  |
| **Pump days** not tested: no Gate, MEXC or KuCoin USDT series |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No automatic burn, buyback or fee share to CTX was verified.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Cryptex Finance ([site](https://cryptex.finance/)); repos at [github.com/cryptexfinance](https://github.com/cryptexfinance).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0x97f7…81aa`](https://etherscan.io/address/0x97f70ed4a8e606c6f6ae578ee27c4e3fadbc81aa) 32.79% (EOA) and [`0x9c50…b9bf`](https://etherscan.io/address/0x9c50d0d2053eebd48e6edaf1c2e39bb1d503b9bf) 12.22% (EOA) are unlabelled; [`0x2de5…9cdd`](https://etherscan.io/address/0x2de5ae18750fbf82821212194d59acc989469cdd) 7.68% is a proxy contract (purpose not read). Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No exchange USDT series for the pump test; the large holders are unlabelled.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not run (no Gate, MEXC, KuCoin or Kraken USDT series).

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- 10M max, 9.65M circulating.

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- ~$31k a day, mostly Coinbase.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Public repos; activity modest.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- TCAP usage is small; no figure verified.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

- None verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: no exchange USDT series; holders unlabelled |
| Entity concentration | 🔴 ~45% in two unlabelled EOAs |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x97f7…81aa`](https://etherscan.io/address/0x97f70ed4a8e606c6f6ae578ee27c4e3fadbc81aa) | Unlabelled EOA (32.79%) | Ethplorer + Etherscan | low | no | None: cannot move Holdings or Selling |
| [`0x9c50…b9bf`](https://etherscan.io/address/0x9c50d0d2053eebd48e6edaf1c2e39bb1d503b9bf) | Unlabelled EOA (12.22%) | Ethplorer + Etherscan | low | no | None: cannot move Holdings or Selling |

## 📚 Sources

- [Tier A] [CoinGecko `cryptex-finance`](https://www.coingecko.com/en/coins/cryptex-finance): price, supply, venues and description, read 16 Nov 2026
- [Tier A] `scripts/pump_day_test.py`: no Gate, MEXC, KuCoin or Kraken USDT series returned on 16 Nov 2026
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x321c2fe4446c7c963dc41dd58879af648838f98d#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `cryptex-finance`](https://www.coingecko.com/en/coins/cryptex-finance) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x321c2fe4446c7c963dc41dd58879af648838f98d) · [holders](https://etherscan.io/token/0x321c2fe4446c7c963dc41dd58879af648838f98d#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Pump test** | Use Coinbase CTX-USD daily candles in `scripts/pump_day_test.py` | Free |
| 2 | **Who controls the 32.8% wallet** | Compare with Cryptex's published treasury; Arkham lookup | Free / Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
