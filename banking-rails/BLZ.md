---
ticker: BLZ
name: Bluzelle
chain: ethereum
contract: "0x5732046a883704404f284ce41ffadd5b007fd668"
overall_score: 3.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 5
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 2
  product_development: 3
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: team wallets unpublished"
  one_hop_sale_status: none_found
  entity_concentration: "~52% in Coinbase and Revolut custody (exchange, not insider)"
price_usd: 0.00670671
price_source: "CoinGecko `bluzelle`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "Gate BLZ_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xf98e5cc1635ee69e451f43bfd913249b0da22028"
    label: "Coinbase custody (21.0%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0x15da7556d5ed888306839bed06f868aeaedcb0d7"
    label: "Revolut: Cold Wallet (19.9%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43"
    label: "Coinbase: Hot Wallet (11.4%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BLZ · Overall grade **3.2 / 10 · ❌ FAIL**

**Summary:** Bluzelle began as a decentralized database and now markets a gaming and DePIN chain. No fee or revenue record on DefiLlama and none published by the project was found. The three largest Ethereum holders (~52% of the ERC-20) are Coinbase and Revolut custody (Arkham, 16 Nov 2026), not insiders. Trading is thin (~$51k a day). BLZ is down 64% in a year. The Revenue gate fails.

**🚨 Top warning:** **About 52% of the ERC-20 is exchange or broker custody, not insiders:** Coinbase [`0xf98e…2028`](https://etherscan.io/address/0xf98e5cc1635ee69e451f43bfd913249b0da22028) 21.0%, the Revolut cold wallet [`0x15da…b0d7`](https://etherscan.io/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) 19.9% and the Coinbase hot wallet [`0xa9d1…3e43`](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) 11.4% (Arkham labels, read 16 Nov 2026). Bluzelle's own wallets are still unpublished.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BLZ · Bluzelle · 3.2 / 10 · ❌ FAIL

> **One line:** A pivoting infrastructure token with no revenue and thin trading.

| 📊 Market (CoinGecko `bluzelle`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00671 | **ERC-20 holders** 28,910 |
| **7d / 30d / 1y** 🔴 −15.3% / 🔴 −29.1% / 🔴 −64.2% | **Top wallets** 20.96% / 19.91% / 11.43% (EOAs) |
| **Market cap** $3.26M · **FDV** $3.35M | **Supply** 487M circulating / 500M |
| **24h volume** $51.4k (top venues: Coinbase Exchange $24.1k, Uniswap V2 (Ethereum) $8.44k, Uniswap V2 (Ethereum) $8.25k) |  |
| **ATH** $0.783 (2018-02-09) |  |
| **Pump days** 28 of 360 days (Gate BLZ_USDT UTC daily closes); latest 2026-09-27, 2026-09-28 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Bluzelle ([site](https://bluzelle.com/)); founded 2014 in Singapore.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

- [`0xf98e…2028`](https://etherscan.io/address/0xf98e5cc1635ee69e451f43bfd913249b0da22028) (21.0%) is a **Coinbase** custody wallet fed only by the Coinbase hot wallet ([Arkham](https://arkm.com/explorer/address/0xf98e5cc1635ee69e451f43bfd913249b0da22028)).
- [`0x15da…b0d7`](https://etherscan.io/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) (19.9%) is **Revolut: Cold Wallet** ([Arkham](https://arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7)), and [`0xa9d1…3e43`](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) (11.4%) is **Coinbase: Hot Wallet** ([Arkham](https://arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43)). Exchange custody is not insider holding.
- Bluzelle team and treasury wallets are not mapped.
- Score: **5**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- The large holders are Coinbase and Revolut custody (Arkham b24); no team wallet is published.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass, including in the Arkham batch b24 read (16 Nov 2026).

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate BLZ_USDT UTC daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- 487M circulating of 500M.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~$51k a day: Coinbase, Uniswap V2, KuCoin, Kraken.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- Repo activity is low; the product focus has shifted several times.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No independent usage figure.

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
| Team wallet → exchange during a pump | ⚪ Not tested: team wallets unpublished |
| Entity concentration | 🟢 ~52% in Coinbase and Revolut custody (exchange, not insider) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xf98e…2028`](https://etherscan.io/address/0xf98e5cc1635ee69e451f43bfd913249b0da22028) | Coinbase custody (21.0%) | [Arkham](https://arkm.com/explorer/address/0xf98e5cc1635ee69e451f43bfd913249b0da22028) entity label | medium | no | Holdings: exchange custody, not insider |
| [`0x15da…b0d7`](https://etherscan.io/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) | Revolut: Cold Wallet (19.9%) | [Arkham](https://arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) entity label | medium | no | Holdings: broker custody, not insider |
| [`0xa9d1…3e43`](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | Coinbase: Hot Wallet (11.4%) | [Arkham](https://arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) entity label | medium | no | Holdings: exchange custody, not insider |

## 📚 Sources

- [Tier A] [CoinGecko `bluzelle`](https://www.coingecko.com/en/coins/bluzelle): price, supply, venues and description, read 16 Nov 2026
- [Tier A] Gate BLZ_USDT UTC daily closes via `scripts/pump_day_test.py` (28 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x5732046a883704404f284ce41ffadd5b007fd668#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0xf98e…2028](https://arkm.com/explorer/address/0xf98e5cc1635ee69e451f43bfd913249b0da22028) · [0x15da…b0d7](https://arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) · [0xa9d1…3e43](https://arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | B | 16 Nov 2026 |
| Market data and venues | [CoinGecko `bluzelle`](https://www.coingecko.com/en/coins/bluzelle) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x5732046a883704404f284ce41ffadd5b007fd668) · [holders](https://etherscan.io/token/0x5732046a883704404f284ce41ffadd5b007fd668#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the three large wallets** | Arkham entity lookup | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
