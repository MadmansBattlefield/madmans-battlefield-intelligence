---
ticker: MDT
name: Measurable Data Token
chain: ethereum
contract: "0x814e0908b12a99fecf5bc101bb5d0b8b5cdf7d26"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 4
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
  team_wallet_to_exchange_during_pump: "not tested: no exchange price series; team wallets unpublished"
  one_hop_sale_status: none_found
  entity_concentration: "DWF Labs 18.1% (market maker); Coinbase Prime 16.3%"
price_usd: 0.00410684
price_source: "CoinGecko `measurable-data-token`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or staking yield was found."
pump_day_price_source: "not run (no Gate, MEXC, KuCoin or Kraken USDT series)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xa14567cbd5090a6b469390e7d33b10cffa70c5b3"
    label: "DWF Labs, market maker (18.1%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4"
    label: "Coinbase Prime Custody (16.3%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43"
    label: "Coinbase: Hot Wallet (9.3%)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
  - address: "0xf977814e90da44bfa03b6295a0616a897441acec"
    label: "Binance: Cold Wallet 20"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan public name tag"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### MDT · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** MDT is the token of a data-exchange project whose products (rewards apps) are self-reported. No fee or revenue record on DefiLlama and none published by the project was found. The top holder is the market maker DWF Labs (18.1%, from a project lockup contract), followed by Coinbase Prime custody (16.3%) and Binance (5.3%). Trading is thin (~$90k a day, mostly Coinbase). MDT is down 71% in a year. The Revenue gate fails.

**🚨 Top warning:** **The top holder is the market maker DWF Labs** ([`0xa145…c5b3`](https://etherscan.io/address/0xa14567cbd5090a6b469390e7d33b10cffa70c5b3), 18.1%), which received 196M MDT from the project's MDTExchangeLockup contract about 3 years ago. The next largest are Coinbase Prime custody [`0x4f4d…0ca4`](https://etherscan.io/address/0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4) 16.3% and the Coinbase hot wallet (9.3%). No exchange price series was available for the pump test.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
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


# 🪪 MDT · Measurable Data Token · 3.1 / 10 · ❌ FAIL

> **One line:** A dormant-looking data token with no revenue, thin trading and a market maker as top holder.

| 📊 Market (CoinGecko `measurable-data-token`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.00411 | **ERC-20 holders** 30,720 |
| **7d / 30d / 1y** 🔴 −5.2% / 🔴 −40.4% / 🔴 −71.4% | **Top wallets** 18.1% / 16.3% (EOAs) |
| **Market cap** $4.11M · **FDV** $4.11M | **Supply** 1B, fully circulating |
| **24h volume** $90.4k (top venues: Coinbase Exchange $88.4k, Uniswap V4 (Ethereum) $1.19k, Uniswap V3 (Ethereum) $822) |  |
| **ATH** $0.168 (2021-12-25) |  |
| **Pump days** not tested: no Gate, MEXC or KuCoin USDT series |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Measurable Data Token ([site](https://mdt.io)); repo at [github.com/measurabledatatoken](https://github.com/measurabledatatoken/-).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- [`0xa145…c5b3`](https://etherscan.io/address/0xa14567cbd5090a6b469390e7d33b10cffa70c5b3) (18.1%) is **DWF Labs** ([Arkham](https://arkm.com/explorer/address/0xa14567cbd5090a6b469390e7d33b10cffa70c5b3)), a market maker. It received 196M MDT from the project's MDTExchangeLockup contract ~3 years ago, so this is a team-allocated market-making inventory. Market-maker flows are not team sales unless a sale is shown.
- [`0x4f4d…0ca4`](https://etherscan.io/address/0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4) (16.3%) is **Coinbase Prime Custody** ([Arkham](https://arkm.com/explorer/address/0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4)); the Coinbase hot wallet [`0xa9d1…3e43`](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) holds 9.3% ([Arkham](https://arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43)); [`0xf977…acec`](https://etherscan.io/address/0xf977814e90da44bfa03b6295a0616a897441acec) 5.31% is Etherscan-labelled Binance: Cold Wallet 20. Exchange custody is not insider holding.
- Measurable Data's own team wallets are not mapped.
- Score: **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- No Gate, MEXC, KuCoin or Kraken USDT series returned, so no pump days were tested; the top holder is DWF Labs, a market maker (Arkham b24).
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass, including in the Arkham batch b24 read (16 Nov 2026).

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not run (no Gate, MEXC, KuCoin or Kraken USDT series).

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- 1B supply, fully circulating.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~$90k a day, almost all on Coinbase.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- The public repo shows little recent activity.

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
| Team wallet → exchange during a pump | ⚪ Not tested: no exchange price series; team wallets unpublished |
| Entity concentration | 🟡 DWF Labs 18.1% (market maker); Coinbase Prime 16.3% |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xa145…c5b3`](https://etherscan.io/address/0xa14567cbd5090a6b469390e7d33b10cffa70c5b3) | DWF Labs, market maker (18.1%) | [Arkham](https://arkm.com/explorer/address/0xa14567cbd5090a6b469390e7d33b10cffa70c5b3) entity label | medium | no | Holdings: team-allocated market-maker inventory |
| [`0x4f4d…0ca4`](https://etherscan.io/address/0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4) | Coinbase Prime Custody (16.3%) | [Arkham](https://arkm.com/explorer/address/0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4) entity label | medium | no | Holdings: exchange custody, not insider |
| [`0xa9d1…3e43`](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | Coinbase: Hot Wallet (9.3%) | [Arkham](https://arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) entity label | medium | no | Holdings: exchange custody, not insider |
| [`0xf977…acec`](https://etherscan.io/address/0xf977814e90da44bfa03b6295a0616a897441acec) | Binance: Cold Wallet 20 | Etherscan public name tag | medium | no | None: exchange custody, not insider |

## 📚 Sources

- [Tier A] [CoinGecko `measurable-data-token`](https://www.coingecko.com/en/coins/measurable-data-token): price, supply, venues and description, read 16 Nov 2026
- [Tier A] `scripts/pump_day_test.py`: no Gate, MEXC, KuCoin or Kraken USDT series returned on 16 Nov 2026
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x814e0908b12a99fecf5bc101bb5d0b8b5cdf7d26#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0xa145…c5b3](https://arkm.com/explorer/address/0xa14567cbd5090a6b469390e7d33b10cffa70c5b3) · [0x4f4d…0ca4](https://arkm.com/explorer/address/0x4f4d8f2ea3c7f7ab2dcd3e521cec535fcd8f0ca4) · [0xa9d1…3e43](https://arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) · [0xf977…acec](https://arkm.com/explorer/address/0xf977814e90da44bfa03b6295a0616a897441acec) | B | 16 Nov 2026 |
| Market data and venues | [CoinGecko `measurable-data-token`](https://www.coingecko.com/en/coins/measurable-data-token) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x814e0908b12a99fecf5bc101bb5d0b8b5cdf7d26) · [holders](https://etherscan.io/token/0x814e0908b12a99fecf5bc101bb5d0b8b5cdf7d26#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Pump test** | Find an exchange daily series (Coinbase MDT-USD candles) and run `scripts/pump_day_test.py` | Free |
| 2 | **Who controls the 18.1% and 16.3% wallets** | Arkham entity lookup | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
