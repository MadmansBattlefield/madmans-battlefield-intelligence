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
  team_wallet_to_exchange_during_pump: "none found: 13.2% wallet's Kraken deposits were not on pump days and it is not linked to Chintai"
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
  - address: "0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b"
    label: "Likely Chintai treasury Safe (12.0%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham: transfers to Chintai Nexus"
  - address: "0x6bf83042c941a74cb5902908e892f0114e549e5a"
    label: "Unlabelled wallet with Kraken deposits (13.2%)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham; Etherscan token transfers"
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

**Summary:** Chintai is a tokenization platform for financial institutions that says it is licensed in Singapore. No fee or revenue record on DefiLlama and none published by the project was found. Platform fees are not shown to reach CHEX. On Ethereum a likely Chintai treasury Safe holds 12.0% and an unlabelled wallet 13.2% that made Kraken deposits in Oct 2026, outside pump days; Etherscan labels an 8.4% holder Kraken 245. CHEX had 81 pump days in a year (Gate) and is down 73%. The Revenue gate fails.

**🚨 Top warning:** **Very volatile, with a large wallet selling to Kraken:** 81 of 360 days were pump days. The unlabelled 13.2% wallet [`0x6bf8…9e5a`](https://etherscan.io/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) sent ~243k CHEX to a Kraken deposit address on 10, 11, 13 and 14 Oct 2026 (not pump days). It receives repeated fresh mints, but no on-chain link to Chintai's treasury Safe was found, so attribution is low confidence. The 12.0% Safe [`0xe4ff…a14b`](https://etherscan.io/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) is likely Chintai's treasury.

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

- Safe [`0xe4ff…a14b`](https://etherscan.io/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) (12.0%) sends CHEX to the Arkham-labelled **Chintai Nexus** entity and to other wallets in 5M tranches ([Arkham](https://arkm.com/explorer/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b)), so it is likely Chintai's treasury [medium confidence].
- [`0x6bf8…9e5a`](https://etherscan.io/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) (13.2%) has no entity label ([Arkham](https://arkm.com/explorer/address/0x6bf83042c941a74cb5902908e892f0114e549e5a)). It has received ~168M CHEX in repeated mints from the zero address since Feb 2025 ([token transfers](https://etherscan.io/token/0x9ce84f6a69986a83d92c324df10bc8e64771030f?a=0x6bf83042c941a74cb5902908e892f0114e549e5a)), which fits a bridge-in or distribution wallet, but it has no direct transfers with the Chintai Safe. Low confidence.
- [`0x7daf…6f83`](https://etherscan.io/address/0x7dafba1d69f6c01ae7567ffd7b046ca03b706f83) 8.39% is Etherscan-labelled Kraken 245 (exchange custody).
- Score: **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No team wallet is published; the 12.0% Safe is likely Chintai's treasury (Arkham b24).
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass.

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate CHEX_USDT UTC daily closes.

- **Pump-day test of the 13.2% wallet (16 Nov 2026):** Gate CHEX_USDT found 81 pump days in 360. The wallet's deposits to the Kraken deposit address [`0x12e7…54b4`](https://etherscan.io/address/0x12e744de35c287e92bb3544d1fb2e32fa30b54b4) ([Arkham label](https://arkm.com/explorer/address/0x12e744de35c287e92bb3544d1fb2e32fa30b54b4)) were 23.5k on 10 Oct, 23.5k on 11 Oct, 98.4k on 13 Oct and 98.2k on 14 Oct 2026 ([transfers](https://etherscan.io/token/0x9ce84f6a69986a83d92c324df10bc8e64771030f?a=0x6bf83042c941a74cb5902908e892f0114e549e5a)). None of 5–20 Oct 2026 was a pump day. On pump days (2 Sep and 23–24 Sep 2026) it sent CHEX only to unlabelled addresses.
- Because the wallet is not linked on-chain to the Chintai treasury Safe and its Kraken deposits fell outside pump days, this is not a proven team sale. **one_hop_sale_status: none_found.** Selling stays **4**.

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
| Team wallet → exchange during a pump | ⚪ None found: the 13.2% wallet's Kraken deposits were not on pump days, and it is not linked to Chintai |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xe4ff…a14b`](https://etherscan.io/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) | Likely Chintai treasury Safe (12.0%) | [Arkham](https://arkm.com/explorer/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b): transfers to Chintai Nexus | medium | no | Holdings: likely treasury |
| [`0x6bf8…9e5a`](https://etherscan.io/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) | Unlabelled wallet with Kraken deposits (13.2%) | [Arkham](https://arkm.com/explorer/address/0x6bf83042c941a74cb5902908e892f0114e549e5a); Etherscan token transfers | low | no | None: not linked to Chintai on-chain |
| [`0x7daf…6f83`](https://etherscan.io/address/0x7dafba1d69f6c01ae7567ffd7b046ca03b706f83) | Kraken 245 | Etherscan public name tag | medium | no | None: exchange custody |

## 📚 Sources

- [Tier A] [CoinGecko `chex-token`](https://www.coingecko.com/en/coins/chex-token): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate CHEX_USDT UTC daily closes via `scripts/pump_day_test.py` (81 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x9ce84f6a69986a83d92c324df10bc8e64771030f#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0xe4ff…a14b](https://arkm.com/explorer/address/0xe4ff3d0a785eb33d2092638982dec9ba4a44a14b) · [0x6bf8…9e5a](https://arkm.com/explorer/address/0x6bf83042c941a74cb5902908e892f0114e549e5a) · [0x7daf…6f83](https://arkm.com/explorer/address/0x7dafba1d69f6c01ae7567ffd7b046ca03b706f83) | B | 16 Nov 2026 |
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
