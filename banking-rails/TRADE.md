---
ticker: TRADE
name: Polytrade
chain: ethereum
contract: "0x6e5970dbd6fc7eb1f29c6d2edf2bc4c36124c0c1 (also Polygon, BNB Chain, Base, Arbitrum)"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: fixed 100M supply, fully unlocked 19 Aug 2026"
  team_wallet_to_exchange_during_pump: "not proven: the wallet named poly-trade.eth sent 1.0M and 2.3M TRADE to a KuCoin deposit on 8 and 9 Dec 2025 (+41.5% and +45.1% days), ~$207k; Arkham does not tie it to Polytrade (self-set ENS name, low confidence), and its two funding Safes carry only generic labels"
  entity_concentration: "67.7M (68%) sits in the Ethereum-Polygon bridge; the Polygon-side holders aren't traced"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Holding TRADE gives no claim on marketplace fees and buybacks are only an intent, so revenue does not reach holders."
pump_day_price_source: "KuCoin TRADE-USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x142aafa73c530652882e9a1e649db7e81299858c"
    label: "poly-trade.eth (self-set ENS name)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xcd982a503070ae0cebb404cf23ca8a00dee7ff7e"
    label: "Generic Gnosis Safes (funded poly-trade.eth)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x8be0fc5b051a0b110b4d23c9eeb04906b9212cba"
    label: "Generic Gnosis Safes (funded poly-trade.eth)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xc8b4b6785d5aa23f31037003abeba528f103cebd"
    label: "Polytrade Finance: Gnosis Safe Proxy"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x520763c1ebda04dac9a6077a41ccc703ff22a9f8"
    label: "LockReleaseTokenPool (verified contract)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan verified source"
  - address: "0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf"
    label: "Polygon: ERC20 Bridge (67.66M TRADE)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
price_usd: 0.02016
price_source: "CoinGecko, 16 Nov 2026 ~10:10 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TRADE · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** Polytrade runs a marketplace for tokenised real-world assets (invoices, bonds, collectibles). TRADE is a fixed 100M-supply token that has been fully unlocked since August 2026. Holding it gives no claim on platform fees, and buybacks are only described as an intent. The Ethereum wallet named poly-trade.eth sent 3.3M TRADE to KuCoin across two pump days in December 2025, but nothing ties that wallet to Polytrade beyond a self-set ENS name. TRADE is down 99% from its peak and trades about $160k a day. The revenue gate fails; selling is "not proven".

**🚨 Top warning:** **a project-named wallet sent tokens to KuCoin on pump days; its owner is unproven.** The wallet `0x142a…858c` carries the ENS name **poly-trade.eth**. It was funded with 36M TRADE in July 2024. It sent **1,000,000 TRADE on 8 Dec 2025** ([tx](https://etherscan.io/tx/0x2ffb4b2aa36304e9461bcc84180f757aab31d8815730d88cc5e0e47172d01d87), status 1) and **2,300,000 TRADE on 9 Dec 2025** ([tx](https://etherscan.io/tx/0x34fb413e1a1bcb91f7a38b7c06a91867a6ce6dbf2964020f0025defcb096312b), status 1) to a KuCoin deposit address. Those days closed +41.5% and +45.1% on KuCoin, and the transfers were worth about $207k. **Alternative:** the ENS name is set by the wallet owner and Polytrade hasn't published this address, so the company link is [Unverified]. Even without it, the revenue gate fails. Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TRADE · Polytrade · 3.7 / 10 · ❌ FAIL

> **One line:** An RWA marketplace token with no fee capture, and a project-named wallet that sold into pumps.

| 📊 Market (CoinGecko, 16 Nov 2026 ~10:10 AM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.02016 | **Supply** 100M, fully unlocked since 19 Aug 2026 |
| **24h / 7d / 30d** 🔴 −9.2% / 🔴 −1.3% / 🔴 −59.2% | **Polygon bridge** holds 67.7M on Ethereum |
| **Market cap** $2.02M · **FDV** $2.02M | **poly-trade.eth** now 1.01M; its relay `0x5207…a9f8` holds 3.30M |
| **24h volume** ~$0.16M (KuCoin $86k, MEXC $57k, PancakeSwap $17k) | |
| **ATH** $3.03 (1 Apr 2024) · now −99.3% | |
| **Pump days** 69 in the last year (KuCoin TRADE-USDT; largest +77.1% on 6 Dec 2025) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- The platform charges fees on its marketplace ([polytrade.finance](https://polytrade.finance/), [Edge docs](https://edge.polytrade.app/docs)). Holding TRADE gives no claim on them, and buybacks are only described as an intent. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Holding TRADE gives no claim on marketplace fees and buybacks are only an intent, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- A registered company that publishes its leadership by role. A wallet carrying the project's name sold into pumps (see Selling).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Team 17% of supply. 67.7M of Ethereum supply sits in the Polygon bridge, and the Polygon-side holders aren't traced. The poly-trade.eth line still holds ~4.3M.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced the minter and the top holders two hops out, for transfers of 500k TRADE or more. 16 exchange deposits; 3 in the window, all from poly-trade.eth to KuCoin: 0.95M (17 Nov 2025), 1.0M (8 Dec, +41.5%) and 2.3M (9 Dec, +45.1%). All have status 1. Two fell on pump days, worth ~$207k.
- **Arkham (16 Nov 2026):** [0x142a…858c](https://intel.arkm.com/explorer/address/0x142aafa73c530652882e9a1e649db7e81299858c) shows only the ENS name poly-trade.eth, which the owner sets; no Polytrade entity label (low confidence). Its 36M and 4.6M TRADE came from two Safes, [0xcd98…ff7e](https://intel.arkm.com/explorer/address/0xcd982a503070ae0cebb404cf23ca8a00dee7ff7e) and [0x8be0…2cba](https://intel.arkm.com/explorer/address/0x8be0fc5b051a0b110b4d23c9eeb04906b9212cba), which Arkham labels only as generic Gnosis Safes (their signer is an individual-labelled ENS wallet). One hop earlier, 0xcd98 received 21M from [Polytrade Finance: Gnosis Safe Proxy](https://intel.arkm.com/explorer/address/0xc8b4b6785d5aa23f31037003abeba528f103cebd), the one Polytrade-labelled wallet, in the 2021 distribution. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- Under the 16 Nov 2026 rule a low-confidence label cannot move Selling on its own, and the funding Safes are not labelled as Polytrade's, so the pump-day deposits are **not proven: 3 → 4.** **Alternative:** if Polytrade confirms poly-trade.eth or the two Safes as its own, Selling returns to 3 (gate fails) and the overall to 3.5.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from KuCoin TRADE-USDT UTC daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- 100M fixed supply, fully unlocked since 19 Aug 2026. No emissions remain.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $0.16M a day, mostly KuCoin and MEXC.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- The RWA marketplace and the Edge product are live.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No published volume or fee figures for 2026.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- No dated catalyst.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: poly-trade.eth → KuCoin, 3.3M TRADE on 8–9 Dec 2025 (pump days); owner unlabelled |
| Live mint path | 🟢 No: fixed supply, fully unlocked |
| Entity concentration | 🟡 68% in the Polygon bridge; Polygon side untraced |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x142a…858c](https://intel.arkm.com/explorer/address/0x142aafa73c530652882e9a1e649db7e81299858c) | poly-trade.eth (self-set ENS name) | Arkham | low | no | Selling 3 → 4 (cannot hold the gate on its own) |
| [0xcd98…ff7e](https://intel.arkm.com/explorer/address/0xcd982a503070ae0cebb404cf23ca8a00dee7ff7e), [0x8be0…2cba](https://intel.arkm.com/explorer/address/0x8be0fc5b051a0b110b4d23c9eeb04906b9212cba) | Generic Gnosis Safes (funded poly-trade.eth) | Arkham | low | no | None |
| [0xc8b4…cebd](https://intel.arkm.com/explorer/address/0xc8b4b6785d5aa23f31037003abeba528f103cebd) | Polytrade Finance: Gnosis Safe Proxy | Arkham | medium | no | None (one hop earlier, 2021) |
| [0x5207…a9f8](https://intel.arkm.com/explorer/address/0x520763c1ebda04dac9a6077a41ccc703ff22a9f8) | LockReleaseTokenPool (verified contract) | Arkham + Etherscan verified source | high | yes | None |
| [0x40ec…bbdf](https://intel.arkm.com/explorer/address/0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf) | Polygon: ERC20 Bridge (67.66M TRADE) | Arkham + Etherscan | high | yes | Holdings: bridge, not team |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): poly-trade.eth, its two funding Safes, the Polytrade-labelled Safe, the token pool and the Polygon bridge
- [Tier A] [polytrade.finance](https://polytrade.finance/), [Polytrade Edge docs](https://edge.polytrade.app/docs)
- [Tier B] tokenomics.com TRADE allocation and unlock schedule
- [Tier A] Etherscan transfers, holders and the ENS name for `0x142a…858c`
- [Tier A] CoinGecko `polytrade` (market, venues); pump days from KuCoin TRADE-USDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| poly-trade.eth → KuCoin 1.0M, 8 Dec 2025 | [tx](https://etherscan.io/tx/0x2ffb4b2aa36304e9461bcc84180f757aab31d8815730d88cc5e0e47172d01d87) | A | 16 Nov 2026 |
| poly-trade.eth → KuCoin 2.3M, 9 Dec 2025 | [tx](https://etherscan.io/tx/0x34fb413e1a1bcb91f7a38b7c06a91867a6ce6dbf2964020f0025defcb096312b) | A | 16 Nov 2026 |
| poly-trade.eth → KuCoin 0.95M, 17 Nov 2025 | [tx](https://etherscan.io/tx/0x18079ef4288e3735e36cbee38042c87913aec46fa7cbfa7b6a6cf78844509b49) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Confirm poly-trade.eth is a Polytrade wallet** | Arkham (16 Nov 2026): ENS name only, funding Safes generic. Ask Polytrade to confirm or deny | Free |
| 2 | **Polygon-side holders** (67.7M bridged) | PolygonScan API needs a paid tier | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
