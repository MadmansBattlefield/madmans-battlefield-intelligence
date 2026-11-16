---
ticker: WIREX
name: Wirex Token (WXT)
chain: ethereum
contract: "0xa02120696c7b8fe16c09c749e4598819b2b0e915 (Ethereum); WXT-GASBLVHS5FOABSDNW5SPPH3QRJYXY5JHA2AOA2QHH2FJLZBRXSG4SWXT (Stellar)"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 2
  product_development: 5
  adoption_customers: 4
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no new minting found; 10B total, ~2.3B circulating"
  team_wallet_to_exchange_during_pump: "not proven: the mint line last deposited to OKX in Nov 2023 (status 1); none in the last year at 30M+ WXT; Wirex custodial wallets unknown"
  entity_concentration: "yes: ~77% of supply outside circulation (platform reserve, team, R&D allocations)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Card, exchange and subscription revenue stays with Wirex; WXT pays discounts and cashback and has no verified burn, so revenue does not reach holders."
pump_day_price_source: "Gate WXT_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x20483d8e79dc03c021bd3371843078a5e8f4e8b3"
    label: "Wirex: Deployer"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain deployment"
  - address: "0x0b1772dfcad147cd256f7a654866aeed5bc60cc6"
    label: "Wirex: Gnosis Safe Proxy (mint recipient)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + null-address mints on-chain"
  - address: "0x2f13d388b85e0ecd32e7c3d7f36d1053354ef104"
    label: "Wirex: Hot Wallet"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + funding from the Wirex Safe"
  - address: "0xc0d93c69a2ef846388e69f7ee7c21668501e7849"
    label: "Wirex: Cold Wallet; Wirex"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x93ab7ca84b7210b0ba30ccc9b555d48adb9518bd"
    label: "Wirex: Cold Wallet; Wirex"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xd5589ca4b2e25d790b8bd0ae44cf3bbc6b3ebef3"
    label: "Unlabelled; funded only by Wirex hot wallets"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.00028267
price_source: "CoinGecko, 16 Nov 2026 ~9:45 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### WIREX · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** WXT is the rewards and tier token of Wirex, a UK crypto-card fintech. It launched on Stellar through a 2019 IEO and was later issued on Ethereum as well. Holding WXT gets users fee discounts and higher-tier cashback. Wirex moved customers to its new Wirex One app in mid-2026, and WXT balances moved with them. Token holders get no share of Wirex revenue. About 77% of supply is outside circulation, and the token trades only on Gate. The revenue gate fails.

**🚨 Top warning:** **one venue and a large overhang.** Gate accounts for nearly all of the ~$287k daily volume, and only ~2.3B of the 10B supply circulates. Wirex's whitepaper reserved at least 49% as a platform reserve, 17% for the team, 14% for R&D and 11% for partnerships ([whitepaper](https://resources.cryptocompare.com/asset-management/558/1692800901692.pdf)), and no current breakdown of what's left was found. Note: WEEX exchange's token also uses the ticker WXT. Its buybacks and burns are **not** Wirex's. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 WIREX · Wirex Token (WXT) · 3.5 / 10 · ❌ FAIL

> **One line:** A fintech rewards token with no revenue share, one exchange and ~77% of supply still held back.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:45 AM MST) | 🔗 Chain (Etherscan, Stellar Horizon) |
|---|---|
| **Price** $0.0002827 | **Supply** ~2.30B circulating of 10B total |
| **24h / 7d / 30d** 🟢 +2.1% / 🔴 −22.9% / 🔴 −35.7% | **Ethereum top unlabelled holders** `0xd558…bef3` 1.0B, `0xc0d9…7849` 461M |
| **Market cap** $0.65M · **FDV** $2.83M | **Stellar** 6,328 trustlines holding 0.70B WXT |
| **24h volume** $0.29M (Gate WXT/USDT ~$287k; StellarTerm $441) | |
| **ATH** $0.0373 (18 Apr 2021) · now −99.2% | |
| **Pump days** 11 in the last year (Gate WXT_USDT; largest +16.6% on 18 Apr and 8 Jun 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Wirex earns card, exchange and subscription revenue, but WXT holders get no cut. The token pays out discounts and cashback, which is a cost. The whitepaper promised reserve burns, but I found no verified burn record for Wirex's WXT. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Card, exchange and subscription revenue stays with Wirex; WXT pays discounts and cashback and has no verified burn, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- An operating, regulated fintech with a public leadership team. It's in the middle of a platform move to Wirex One, which users say was poorly communicated ([Wirex support on Reddit](https://www.reddit.com/r/wirexappofficial/comments/1u6wwnm/wirex_one_clarification/)) [Tier B].

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Allocation: ≥49% platform reserve, 17% team, 14% R&D, 11% partnerships, 5% seed, ≤4% public ([whitepaper](https://resources.cryptocompare.com/asset-management/558/1692800901692.pdf)). About 77% is still outside circulation.
- Arkham labels [0xc0d9…7849](https://intel.arkm.com/explorer/address/0xc0d93c69a2ef846388e69f7ee7c21668501e7849) **Wirex: Cold Wallet** (461M WXT) and [0x93ab…18bd](https://intel.arkm.com/explorer/address/0x93ab7ca84b7210b0ba30ccc9b555d48adb9518bd) **Wirex** (134.1M WXT). [0xd558…bef3](https://intel.arkm.com/explorer/address/0xd5589ca4b2e25d790b8bd0ae44cf3bbc6b3ebef3) (1.0B WXT on Etherscan) is unlabelled, but all its WXT came from Wirex hot wallets, so it looks like a Wirex operating wallet [Unverified]. At least ~1.6B WXT on Ethereum sits in Wirex-labelled or Wirex-funded wallets. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced the Ethereum mint line (`0x2048…` → `0x0b17…` → `0x2f13…`) and the top 15 holders two hops out, for transfers of 30M WXT or more. The last exchange deposits were in 2021–2023: `0x2f13…` sent 136.5M WXT to OKX on 29–30 Nov 2023 ([tx](https://etherscan.io/tx/0x09db9098165d8a9a22c84466b4b155c93df1a4cf0e017f4c0c7e470ecfbbfacc), status 1). Nothing in the last year. But Wirex's in-app custodial wallets can't be seen, so **not proven, 4.**
- **Arkham (16 Nov 2026)** confirms the mint line is Wirex's: [0x2048…e8b3](https://intel.arkm.com/explorer/address/0x20483d8e79dc03c021bd3371843078a5e8f4e8b3) is **Wirex: Deployer**; [0x0b17…0cc6](https://intel.arkm.com/explorer/address/0x0b1772dfcad147cd256f7a654866aeed5bc60cc6) is **Wirex: Gnosis Safe Proxy** and shows mints from the null address (6B and 1.3B about five years ago, 1.3B about four years ago) plus 2B from the deployer, sent on to **Wirex: Hot Wallet** [0x2f13…f104](https://intel.arkm.com/explorer/address/0x2f13d388b85e0ecd32e7c3d7f36d1053354ef104). So the 2023 OKX deposits came from a Wirex-labelled hot wallet (outside the window). The hot wallet's latest page shows stablecoin and ETH flows with Circle, Binance and Bridge.xyz, and no WXT. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate WXT_USDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 7.7B WXT, 3.3× today's float, sits in reserve and allocations with no published release schedule.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- About $287k a day, almost all on Gate. The market cap is $0.65M.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- WXT tiers and cashback inside the Wirex One app, which runs the company's card and payments business.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Usage is tied to Wirex's customer base. No on-chain usage figures.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found for the token or its contracts.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- 2019 IEO by a Wirex subsidiary. Wirex operates under e-money and other licences.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- None dated. The Wirex One migration is done.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (custodial wallets unseen; mint line clean in window) |
| Live mint path | 🟢 None found |
| Entity concentration | 🔴 ~77% outside circulation |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x2048…e8b3](https://intel.arkm.com/explorer/address/0x20483d8e79dc03c021bd3371843078a5e8f4e8b3) | Wirex: Deployer | Arkham + on-chain deployment | high | yes (on-chain) | Confirms the mint line |
| [0x0b17…0cc6](https://intel.arkm.com/explorer/address/0x0b1772dfcad147cd256f7a654866aeed5bc60cc6) | Wirex: Gnosis Safe Proxy (mint recipient) | Arkham + null-address mints on-chain | high | yes (on-chain) | Confirms the mint line |
| [0x2f13…f104](https://intel.arkm.com/explorer/address/0x2f13d388b85e0ecd32e7c3d7f36d1053354ef104) | Wirex: Hot Wallet | Arkham + funding from the Wirex Safe | high | yes (on-chain) | 2023 OKX deposits are Wirex's; outside the window |
| [0xc0d9…7849](https://intel.arkm.com/explorer/address/0xc0d93c69a2ef846388e69f7ee7c21668501e7849), [0x93ab…18bd](https://intel.arkm.com/explorer/address/0x93ab7ca84b7210b0ba30ccc9b555d48adb9518bd) | Wirex: Cold Wallet; Wirex | Arkham | medium | no | Holdings concentration confirmed; score unchanged |
| [0xd558…bef3](https://intel.arkm.com/explorer/address/0xd5589ca4b2e25d790b8bd0ae44cf3bbc6b3ebef3) | Unlabelled; funded only by Wirex hot wallets | Arkham | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the deployer, the Wirex Safe, the hot and cold wallets and the largest unlabelled holder
- [Tier A] [WXT whitepaper](https://resources.cryptocompare.com/asset-management/558/1692800901692.pdf)
- [Tier A] Etherscan transfers and holders for `0xa021…e915`; Stellar Horizon asset stats
- [Tier B] [Wirex support post on Wirex One migration](https://www.reddit.com/r/wirexappofficial/comments/1u6wwnm/wirex_one_clarification/)
- [Tier A] CoinGecko `wirex` (market, venues); pump days from Gate WXT_USDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Mint line → OKX, Nov 2023 | [tx](https://etherscan.io/tx/0x09db9098165d8a9a22c84466b4b155c93df1a4cf0e017f4c0c7e470ecfbbfacc), [tx](https://etherscan.io/tx/0x4c1e44a191094a4808bdacd5460997a5fc1082ee0df5a5430cdb5555706b566c) | A | 16 Nov 2026 |
| Allocation | [whitepaper](https://resources.cryptocompare.com/asset-management/558/1692800901692.pdf) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Role of `0xd558…bef3` (1.0B)** | Arkham (16 Nov 2026): unlabelled but funded only by Wirex hot wallets; `0xc0d9…7849` is a Wirex cold wallet. Ask Wirex to publish its reserve wallets | Free |
| 2 | **Current reserve and team balances** | Ask Wirex | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
