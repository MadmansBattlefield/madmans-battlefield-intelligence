---
ticker: METAL
name: Metal Blockchain
chain: ethereum
contract: "0x294559fa758c88d639fd085751e463fee7806eab"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 1
  product_development: 4
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found in this pass"
  team_wallet_to_exchange_during_pump: "not tested: team wallets unpublished"
  one_hop_sale_status: none_found
  own_venue_volume: "~99.8% of reported volume on Metal X"
price_usd: 0.09757
price_source: "CoinGecko `metal-blockchain`, 16 Nov 2026 ~3:00 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No burn, buyback, fee share or fee-funded staking yield was found."
pump_day_price_source: "MEXC METALUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xda5f0891426d5ddbdd8c5f0b88a604e9062c7347"
    label: "Proton Blockchain reserve / bridge (98.5% of ERC-20)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### METAL · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Metal Blockchain is an Avalanche-derived layer-0 from the Metallicus group (Metal Pay). No fee or revenue record on DefiLlama and none published by the project was found. Almost all of its reported $404k daily volume is on Metal X, the group's own exchange (METAL/XMD); MEXC shows about $1k. On Ethereum, 98.5% of the ERC-20 is a Proton Blockchain reserve or bridge (Arkham, 16 Nov 2026), so free float there is ~1.5%. The Revenue gate fails.

**🚨 Top warning:** **Volume is almost entirely on the issuer group's own venue.** CoinGecko attributes ~$403k of ~$404k daily volume to Metal X (METAL/XMD), with ~$1k on MEXC. Independent liquidity is close to zero.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 METAL · Metal Blockchain · 3.1 / 10 · ❌ FAIL

> **One line:** An Avalanche-style chain whose market is almost entirely its own group's exchange.

| 📊 Market (CoinGecko `metal-blockchain`, 16 Nov 2026 ~3:00 PM MST) | 🔗 Chain |
|---|---|
| **Price** $0.0976 | **Supply** 508M circulating / 667M max |
| **7d / 30d / 1y** 🔴 −4.0% / 🔴 −11.4% / 🔴 −54.2% | **ERC-20 top wallet** `0xda5f…7347` 98.5% (EOA) |
| **Market cap** $49.5M · **FDV** $65M | **Main venue** Metal X (issuer group) |
| **24h volume** $404k (top venues: Metal X $403k, MEXC $948, Uniswap V4 (Ethereum) $87) |  |
| **ATH** $1.65 (2022-09-12) |  |
| **Pump days** 25 of 360 days (MEXC METALUSDT UTC daily closes); latest 2026-08-30, 2026-11-13 |  |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- No fee or revenue record on DefiLlama and none published by the project was found.

**What it means:** **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No burn, buyback, fee share or fee-funded staking yield was found.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Metallicus group (Metal Pay, Metal X, XPR Network) ([site](https://metalblockchain.org/)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- The ERC-20's 98.5% holder [`0xda5f…7347`](https://etherscan.io/address/0xda5f0891426d5ddbdd8c5f0b88a604e9062c7347) is labelled **Proton Blockchain** by Arkham ([Arkham](https://arkm.com/explorer/address/0xda5f0891426d5ddbdd8c5f0b88a604e9062c7347)) and also holds 9.67B XPR. It is the affiliated XPR Network chain's reserve or bridge for METAL, linked to Metal Pay (Metallicus), so it is not free float and not a sale overhang on Ethereum.
- That leaves ~1.5% of the ERC-20 as free float. The team's holdings on the native XPR-chain METAL are not mapped, so Holdings stays not proven.
- Score: **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Team wallets are not published.
- No exchange-labelled deposit from a disclosed team or treasury wallet on a pump day was found in this pass, including in the Arkham batch b24 read (16 Nov 2026).

**What it means:** Not proven → **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC METALUSDT UTC daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 508M circulating of 667M max (CoinGecko).

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- ~$404k a day, ~$403k of it on Metal X (METAL/XMD), the group's own venue; MEXC ~$1k; Uniswap ~$87. Score **1**.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Code at [github.com/metalblockchain](https://github.com/metalblockchain).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No independent usage figures found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Metal Pay is a US money-transmitter group [Unverified]; no enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None found.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not tested |
| Volume on own venue | 🔴 ~99.8% of volume on the issuer group's Metal X |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Entity labels below come from Arkham batch b24 (signed-in read on 16 Nov 2026, page 1 of transfers): an Arkham label alone is medium confidence; an Etherscan name tag that agrees makes it high. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xda5f…7347`](https://etherscan.io/address/0xda5f0891426d5ddbdd8c5f0b88a604e9062c7347) | Proton Blockchain reserve / bridge (98.5% of ERC-20) | [Arkham](https://arkm.com/explorer/address/0xda5f0891426d5ddbdd8c5f0b88a604e9062c7347) entity label | medium | no | Holdings: affiliated-chain reserve, not free float |

## 📚 Sources

- [Tier A] [CoinGecko `metal-blockchain`](https://www.coingecko.com/en/coins/metal-blockchain): price, supply, venues and description, read 16 Nov 2026
- [Tier A] MEXC METALUSDT UTC daily closes via `scripts/pump_day_test.py` (25 pump days of 360); Binance returned HTTP 451, so the hierarchy fell through to this venue
- [Tier A] Token contract and [holders](https://etherscan.io/token/0x294559fa758c88d639fd085751e463fee7806eab#balances) on the chain explorer; top holders from the Ethplorer API; contract or EOA status from Etherscan v2 `eth_getCode`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Entity labels for the top holders (Arkham batch b24) | [0xda5f…7347](https://arkm.com/explorer/address/0xda5f0891426d5ddbdd8c5f0b88a604e9062c7347) | B | 16 Nov 2026 |
| Market data and venues | [CoinGecko `metal-blockchain`](https://www.coingecko.com/en/coins/metal-blockchain) | A | 16 Nov 2026 |
| Token contract and holders | [contract](https://etherscan.io/token/0x294559fa758c88d639fd085751e463fee7806eab) · [holders](https://etherscan.io/token/0x294559fa758c88d639fd085751e463fee7806eab#balances) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Independent volume** | Compare Metal X trades with outside venues | Free |
| 2 | **Owner of the 98.5% ERC-20 wallet** | Arkham lookup | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior. Under the 16 Nov 2026 one-hop amendment, a transfer to an exchange counts as a sale only with a team-attributed exchange account, evidence of a sale, or no plausible published reason.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
