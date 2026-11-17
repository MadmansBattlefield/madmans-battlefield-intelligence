---
ticker: SKEY
name: Skey Network
chain: ethereum
contract: "0x06a01a4d579479dd5d884ebf61a31727a3d8d442"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 1
  product_development: 4
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: 1B minted 2020, ~74M burned"
  team_wallet_to_exchange_during_pump: "not proven: a Skey-labelled split wallet sent 5.5M SKEY to a KuCoin deposit on 8 Dec 2025 and 11 Jan 2026 (not pump days); an unlabelled distributor it funds sent 4.5M (28 Nov 2025) and 1.5M (6 Jan 2026) to the same deposit on pump days"
  one_hop_sale_status: none_found
  entity_concentration: "yes: ~506M SKEY (~55% of supply) still sits in wallets split from the 700M company wallet"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "A SkeyDPP-funded buyback is on the 2026 roadmap only, so revenue does not reach holders."
pump_day_price_source: "CoinGecko SKEY daily closes, re-run 17 Nov 2026 with scripts/pump_day_test.py (42 of 360 days); midnight stamps labelled as the close of the prior UTC day; last resort (BingX history from Jul 2026)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xcdc41c48b4685102c4e6c9de50b6e9367429e7a6"
    label: "Skey Network"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain 700M deployer allocation and 2022 split"
  - address: "0x4718178ebc45994aad24531c59752d84770c0f56"
    label: "Skey Network"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain 700M deployer allocation and 2022 split"
  - address: "0x29c37a3f88dd39a098ecec16e66e785c155e8b00"
    label: "Skey Network"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain 700M deployer allocation and 2022 split"
  - address: "0xc74256c178282e7bf6e697177aeb901aa02e20c9"
    label: "Skey Network"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain 700M deployer allocation and 2022 split"
  - address: "0xb448c31db943aafc8abf2aa49abdd2fa76fe2981"
    label: "Skey Network"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain 700M deployer allocation and 2022 split"
  - address: "0x013ca139cd701ad530aed2b8327966d1ba5221cf"
    label: "Unlabelled split wallet (first funder Skey Network)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + on-chain split"
  - address: "0x8dead771da2a454a615cc38e51f7b12b30993753"
    label: "Unlabelled distributor"
    confidence: low
    independent_corroboration: false
    basis: "Etherscan flows"
  - address: "0x1c486b2deed7a34b442616ef50e8b6f86b6ce11d"
    label: "KuCoin Deposit"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x32eef6c0ab7267e474051351e8c82066d93f4948"
    label: "KuCoin (53.3M SKEY)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.00082538
price_source: "CoinGecko, 16 Nov 2026 ~10:05 AM MST"
last_updated: 2026-11-17
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SKEY · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** Skey Network is a small Polish-founded IoT company building digital product passports, AI integrations and product tokenisation. SKEY is its ERC-20 token. The deployer sent 700M of the 1B supply to one company wallet, which was split into eight wallets in Aug 2022. Those wallets still hold about 55% of supply. One of them sent 5.5M SKEY to KuCoin in the last year, and a wallet they fund sent more on pump days. The company plans to fund buybacks from its product-passport business, but that's still on the roadmap. Trading is almost entirely on BingX. The revenue gate fails.

**🚨 Top warning:** **one exchange and a 55% company stash.** About $140k a day trades almost entirely on BingX, and ~506M SKEY sits in eight wallets split from the 700M company wallet in Aug 2022 ([split tx](https://etherscan.io/tx/0x0e0ba1f74835528334b295eb1f11168b88ef9fea636da5254dfb365c8dcc5b89)). Most have been dormant, but at ~$0.42M they're worth three times a day's trading volume. Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SKEY · Skey Network · 3.4 / 10 · ❌ FAIL

> **One line:** A tiny IoT company token on a single exchange, with half its supply in dormant company wallets.

| 📊 Market (CoinGecko, 16 Nov 2026 ~10:05 AM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.0008254 | **Supply** 925.96M after burns (1B minted 2020) |
| **24h / 7d / 30d** ⚪ −0.3% / 🔴 −2.4% / 🔴 −37.7% | **Company line** deployer → `0xcdc4…e7a6` (700M) → eight wallets (Aug 2022) |
| **Market cap** $0.67M · **FDV** $0.83M | **Largest holders** 120M, 100M, 80M, 50M, 43.6M, 42.5M, 40M, 30M (company line) |
| **24h volume** $0.14M (BingX SKEY/USDT; Uniswap ~$1) | |
| **ATH** $0.558 (18 Mar 2021) · now −99.9% | |
| **Pump days** 5 since 6 Jul 2026 (BingX SKEY-USDT, the only series available; largest +18.8% on 20 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No token revenue. A buyback funded by SkeyDPP revenue is on the 2026 roadmap only ([white paper 2.6](https://skey.network/white-papers/SkeyNetwork-WP-EN-LATEST.pdf)). **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** A SkeyDPP-funded buyback is on the 2026 roadmap only, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- A small company, about 1–10 staff [Unverified]. It showed SkeyDPP and SkeyAI at CES 2026 ([Skey blog](https://skeynetwork.medium.com/ces-2026-were-in-las-vegas-showing-the-future-of-blockchain-085487d3870f)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- In Sep 2020 the deployer sent 700M SKEY to `0xcdc4…e7a6` ([tx](https://etherscan.io/tx/0x955a316e1d29bdc56082e491c8f2afc624ae0e7a67d6869d1e086114230e4113)), which burned 70.7M in 2022 and split the rest into eight wallets. ~506M still sits there, ~55% of supply.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced the deployer, the company wallet and the top ten holders two hops out, for transfers of 10M SKEY or more. The only exchange deposits were 50M to ProBit in Nov–Dec 2020. None of 10M+ in the last year. BingX prices only go back to Jul 2026, so earlier pump days in the window can't be checked.
- **Arkham (16 Nov 2026)** labels the company wallet [0xcdc4…e7a6](https://intel.arkm.com/explorer/address/0xcdc41c48b4685102c4e6c9de50b6e9367429e7a6) and its split wallets [0x29c3…8b00](https://intel.arkm.com/explorer/address/0x29c37a3f88dd39a098ecec16e66e785c155e8b00), [0xc742…20c9](https://intel.arkm.com/explorer/address/0xc74256c178282e7bf6e697177aeb901aa02e20c9), [0xb448…2981](https://intel.arkm.com/explorer/address/0xb448c31db943aafc8abf2aa49abdd2fa76fe2981) and [0x4718…0f56](https://intel.arkm.com/explorer/address/0x4718178ebc45994aad24531c59752d84770c0f56) **Skey Network**. Below the 10M threshold, 0x4718 sent **2.5M SKEY on 8 Dec 2025** ([tx](https://etherscan.io/tx/0x1924d01568418b7276ac0f34f72e42ef19e88254e34c46f5b4cee6b81dd1214d)) and **3M on 11 Jan 2026** ([tx](https://etherscan.io/tx/0x2b3c8b6469db79679e291e09ec6603cdbb3ae7519236e7ea9ad876b064d45092)) to KuCoin Deposit [0x1c48…e11d](https://intel.arkm.com/explorer/address/0x1c486b2deed7a34b442616ef50e8b6f86b6ce11d) (−16.4% and −1.2% on CoinGecko closes, not pump days).
- 0x4718 and the unlabelled split wallet [0x013c…21cf](https://intel.arkm.com/explorer/address/0x013ca139cd701ad530aed2b8327966d1ba5221cf) (first funded by the company wallet) sent ~167M SKEY to the unlabelled wallet [0x8dea…3753](https://intel.arkm.com/explorer/address/0x8dead771da2a454a615cc38e51f7b12b30993753), which sent 74.8M to the same KuCoin deposit over time, including 34.0M in the window. Of that, **4.5M on 28 Nov 2025** (+43.9%; e.g. [tx](https://etherscan.io/tx/0x74b06d515af7e38f885ed35b9c6732780349592d9ce326cb973fdba4efad54fd)) and **1.5M on 6 Jan 2026** (+19.2%, [tx](https://etherscan.io/tx/0x9c3a410c3fd12754e6a71ed320fe5ef9283c5df4c186327e28dfdf1587534eba)) fell on pump days. The pump days use CoinGecko daily closes (re-run 17 Nov 2026, midnight-stamp convention: **42 of 360 days**), the last resort, because BingX history starts in Jul 2026 and KuCoin, Gate and MEXC no longer list SKEY. 28 Nov 2025 (+43.9%) and 6 Jan 2026 (+19.2%) remain pump days.
- 0x8dea is unlabelled, so under the 16 Nov 2026 rule it cannot carry a pump-day sale on its own. The labelled wallet's own deposits missed pump days, so Selling is **not proven: 6 → 4**. Arkham labels [0x32ee…4948](https://intel.arkm.com/explorer/address/0x32eef6c0ab7267e474051351e8c82066d93f4948) (53.3M SKEY) **KuCoin**, an exchange wallet, not an insider. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from CoinGecko SKEY daily closes, re-run 17 Nov 2026 with the midnight-stamp convention (42 of 360 days; last resort; BingX from Jul 2026).

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed supply with ~74M burned so far ([skey.network](https://skey.network/) shows 75M) and no unlocks. But the company's 55% could be released at will.

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- Effectively one venue, BingX, at $140k a day. Market cap is $0.67M.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Digital product passports, AI and IoT integrations, and tokenised consumer products through Go2NFT.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- The company claims 200,000+ tokenised products and 70+ brands [Unverified: company figures].

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- 2020–21 IEO and presale. No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- An EU product-passport rollout and the planned buyback.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: labelled company wallet → KuCoin off pump days; a funded unlabelled wallet → KuCoin on 2 pump days |
| Live mint path | 🟢 None |
| Entity concentration | 🔴 ~55% in company-line wallets |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xcdc4…e7a6](https://intel.arkm.com/explorer/address/0xcdc41c48b4685102c4e6c9de50b6e9367429e7a6), [0x4718…0f56](https://intel.arkm.com/explorer/address/0x4718178ebc45994aad24531c59752d84770c0f56), [0x29c3…8b00](https://intel.arkm.com/explorer/address/0x29c37a3f88dd39a098ecec16e66e785c155e8b00), [0xc742…20c9](https://intel.arkm.com/explorer/address/0xc74256c178282e7bf6e697177aeb901aa02e20c9), [0xb448…2981](https://intel.arkm.com/explorer/address/0xb448c31db943aafc8abf2aa49abdd2fa76fe2981) | Skey Network | Arkham + on-chain 700M deployer allocation and 2022 split | high | yes (on-chain) | Holdings; Selling (off-pump KuCoin deposits) |
| [0x013c…21cf](https://intel.arkm.com/explorer/address/0x013ca139cd701ad530aed2b8327966d1ba5221cf) | Unlabelled split wallet (first funder Skey Network) | Arkham + on-chain split | medium | on-chain flows only | None alone |
| [0x8dea…3753](https://intel.arkm.com/explorer/address/0x8dead771da2a454a615cc38e51f7b12b30993753) | Unlabelled distributor | Etherscan flows | low | no | Cannot move Selling alone; Selling 6 → 4 (not proven) |
| [0x1c48…e11d](https://intel.arkm.com/explorer/address/0x1c486b2deed7a34b442616ef50e8b6f86b6ce11d) | KuCoin Deposit | Arkham | medium | no | Exchange deposit |
| [0x32ee…4948](https://intel.arkm.com/explorer/address/0x32eef6c0ab7267e474051351e8c82066d93f4948) | KuCoin (53.3M SKEY) | Arkham | medium | no | Holdings: exchange, not insider |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the company wallet, its split wallets, the KuCoin deposit and the KuCoin wallet; dates from Etherscan
- [Tier A] [Skey white paper 2.6 (Dec 2025)](https://skey.network/white-papers/SkeyNetwork-WP-EN-LATEST.pdf), [skey.network](https://skey.network/), [CES 2026 post](https://skeynetwork.medium.com/ces-2026-were-in-las-vegas-showing-the-future-of-blockchain-085487d3870f)
- [Tier A] Etherscan transfers and holders for `0x06a0…d442`
- [Tier A] CoinGecko `skey-network` (market, venues); pump days from BingX SKEY-USDT daily closes (only 134 days available)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 700M to company wallet | [tx](https://etherscan.io/tx/0x955a316e1d29bdc56082e491c8f2afc624ae0e7a67d6869d1e086114230e4113) | A | 16 Nov 2026 |
| 120M split, Aug 2022 | [tx](https://etherscan.io/tx/0x0e0ba1f74835528334b295eb1f11168b88ef9fea636da5254dfb365c8dcc5b89) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Pump days from Nov 2025 to Jul 2026** | Another exchange's SKEY history | Free |
| 2 | **Who controls `0x8dea…3753`** (fed ~167M by Skey wallets; KuCoin deposits on pump days) | Ask Skey Network; Arkham shows no label | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
