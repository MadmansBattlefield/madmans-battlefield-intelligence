---
ticker: CHEX
name: Chintai
chain: ethereum
contract: "0x9ce84f6a69986a83d92c324df10bc8e64771030f"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 5
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
price_usd: 0.00903336
price_source: "CoinGecko `chex-token`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "Gate CHEX_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x6bf83042c941a74cb5902908e892f0114e549e5a"
    label: "Unlabelled EOA (13.22%)"
    confidence: low
    independent_corroboration: false
    basis: "Ethplorer + Etherscan"
  - address: "0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b"
    label: "Unlabelled Safe (12.01%)"
    confidence: low
    independent_corroboration: false
    basis: "Etherscan getsourcecode"
  - address: "0x7dafba1d69f6c01ae7567ffd7b046ca03b706f83"
    label: "Kraken 245"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan public name tag"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CHEX · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** Chintai is a tokenization platform for financial institutions that says it is licensed in Singapore. No fee or revenue record on DefiLlama and none published by the project was found. Platform fees are not shown to reach CHEX. On Ethereum an unlabelled EOA holds 13.2% and an unlabelled Safe 12.0%; Etherscan labels an 8.4% holder Kraken 245. CHEX had 81 pump days in a year (Gate) and is down 73%. The Revenue gate fails.

**🚨 Top warning:** **Very volatile, with large unlabelled holders:** 81 of 360 days were pump days, and [`0x6bf8…9e5a`](https://etherscan.io/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) 13.22% (EOA) plus a 12.01% Safe [`0xe4ff…a14b`](https://etherscan.io/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) are unlabelled. Low confidence; for the Arkham batch.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CHEX · Chintai · 3.5 / 10 · ❌ FAIL

> **One line:** A licensed-tokenization pitch whose token has no claim on platform income.

| 📊 Market (CoinGecko `chex-token`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00903 | **ERC-20 holders** 9,213 |
| **7d / 30d / 1y** 🔴 −6.5% / 🔴 −8.9% / 🔴 −72.9% | **Top** `0x6bf8…9e5a` 13.22% (EOA) · `0xe4ff…a14b` 12.01% (Safe) |
| **Market cap** $11.3M · **FDV** $11.3M | **Supply** 1.25B circulating |
| **24h volume** $150k (top venues: Bitunix $69.5k, MEXC $59.8k, Gate $5.53k) |  |
| **ATH** $0.804 (2024-12-16) |  |
| **Pump days** 81 of 360 days (Gate CHEX_USDT UTC daily closes); latest 2026-10-30, 2026-11-01 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found. Chintai's platform income is company revenue.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Chintai ([site](https://chintai.io/)); repo at [github.com/chintai-platform](https://github.com/chintai-platform/chexchexchex). The Singapore licence is self-described [Unverified].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0x6bf8…9e5a`](https://etherscan.io/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) 13.22% (EOA) and the Safe [`0xe4ff…a14b`](https://etherscan.io/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) 12.01% are unlabelled. [`0x7daf…6f83`](https://etherscan.io/address/0x7dafba1d69f6c01ae7567ffd7b046ca03b706f83) 8.39% is Etherscan-labelled Kraken 245. Not proven → **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The large holders are unlabelled and no team wallet is published.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass. No Arkham pass was run.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate CHEX_USDT UTC daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- 1.25B circulating; multi-chain (Ethereum, BSC, Base, Solana).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- ~$0.15M a day, led by Bitunix and MEXC.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Public repo; platform live.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Institutional clients are self-reported [Tier B].

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found in this pass.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Claims a Singapore licence [Unverified]; no enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None verified.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested: holders unlabelled |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. No Arkham pass was run for this report, so every attribution that rests on an unlabelled wallet is low confidence. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x6bf8…9e5a`](https://etherscan.io/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) | Unlabelled EOA (13.22%) | Ethplorer + Etherscan | low | no | None: cannot move Holdings or Selling |
| [`0xe4ff…a14b`](https://etherscan.io/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) | Unlabelled Safe (12.01%) | Etherscan getsourcecode | low | no | None |
| [`0x7daf…6f83`](https://etherscan.io/address/0x7dafba1d69f6c01ae7567ffd7b046ca03b706f83) | Kraken 245 | Etherscan public name tag | medium | no | None: exchange custody |

## 📚 Sources

- [Tier A] [CoinGecko `chex-token`](https://www.coingecko.com/en/coins/chex-token): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate CHEX_USDT UTC daily closes via `scripts/pump_day_test.py` (81 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x9ce84f6a69986a83d92c324df10bc8e64771030f#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Market data and venues | [CoinGecko `chex-token`](https://www.coingecko.com/en/coins/chex-token) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x9ce84f6a69986a83d92c324df10bc8e64771030f) · [holders](https://etherscan.io/token/0x9ce84f6a69986a83d92c324df10bc8e64771030f#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the 13.2% EOA and 12.0% Safe** | Arkham entity lookup; read the Safe's signers on Etherscan | Arkham / Free |
| 2 | **Licence** | Check the MAS Financial Institutions Directory for Chintai | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
