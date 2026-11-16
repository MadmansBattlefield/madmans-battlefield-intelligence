---
ticker: SHPING
name: Shping
chain: ethereum
contract: "0x7c84e62859d0715eb77d1b1c4154ecd6abb21bec"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 2
  product_development: 6
  adoption_customers: 5
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no; fixed 10B supply minted at creation in 2018"
  team_wallet_to_exchange_during_pump: "yes: a deployer-funded company wallet deposited 152M SHPING (~$149k) to Gate and MEXC on 8 pump days since Nov 2025; the cash-out mechanism is only a buried mention, with no sale reporting"
  one_hop_sale_status: not_proven
  entity_concentration: "the labelled deployer still holds 5.94B (59.4%)"
price_usd: 0.00041027
price_source: "CoinGecko, 16 Nov 2026 ~12:30 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "none; app and brand revenue stays with the operating company"
pump_day_price_source: "Gate SHPING_USDT daily closes (UTC); Binance unavailable (451), Gate is next in the hierarchy"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x52a6de898366662724725e206d8fe350fe535a03"
    label: "Shping: Deployer"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan name tag plus on-chain proof: this address created the token contract"
  - address: "0xb2242f32aa8751d1a754e5ccd8eee904cd21c915"
    label: "company operating wallet (inferred)"
    confidence: high
    independent_corroboration: true
    basis: "4.01B of its 4.19B SHPING inflows came from the labelled deployer in 31 transfers, the latest on 14 Nov 2026"
  - address: "0x1a545fffadf2f4c3cb34a222756632dd31814cca"
    label: "Gate Deposit"
    confidence: medium
    independent_corroboration: false
    basis: "Etherscan name tag; Arkham also labels it Gate Deposit and shows it forwarding to the Gate hot wallet; the Gate account owner is not identified"
  - address: "0x2b902bbd97f3e0cb90dd9cc07ccc60d4d16c11ae"
    label: "MEXC deposit (forwards to MEXC 16)"
    confidence: medium
    independent_corroboration: true
    basis: "forwards to an Etherscan-labelled MEXC wallet; Arkham labels it MEXC Deposit"
  - address: "0xbb107e9b60d0655a6635b79a39647514d6d57472"
    label: "Coinbase Prime Custody (1.31B SHPING)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham entity label; funded by another Coinbase Prime Custody wallet"
  - address: "0x3243ce0cd2c1ab53d24ccb58caf0c82ac9846132"
    label: "Coinbase-associated address (734M SHPING)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham shows it funded from the Coinbase hot wallet; no more specific label"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SHPING · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** Shping is an Australian shopping-rewards app. Users earn SHPING coins for uploading receipts and writing reviews and can cash out to Australian dollars or crypto. The company sells the app to brands, but none of that revenue reaches token holders. The deployer wallet still holds 59% of supply and has fed a company operating wallet 4.01B SHPING. That wallet sent 609M SHPING (~$520k) to exchange deposit addresses in the last 12 months, including 152M on 8 pump days. Both hard gates fail.

**🚨 Top warning:** **the company wallet keeps sending coins to exchanges, including on pump days.** The Etherscan-tagged "Shping: Deployer" [`0x52a6…5a03`](https://etherscan.io/address/0x52a6de898366662724725e206d8fe350fe535a03) (the address that created the contract) funded operating wallet [`0xb224…c915`](https://etherscan.io/address/0xb2242f32aa8751d1a754e5ccd8eee904cd21c915) with 4.01B SHPING. Since 16 Nov 2025 that wallet has sent **609M SHPING (~$520k)** to Gate, Poloniex and MEXC deposit addresses. **152M (~$149k) went on 8 pump days**, e.g. [22.0M to Gate on 26 Sep 2026](https://etherscan.io/tx/0x562125817b5ae0eff4e85fc324ba444a595c0ac2e78f9f835f118d57c0e86423). Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SHPING · Shping · 3.5 / 10 · ❌ FAIL

> **One line:** A real rewards app whose company wallet sells SHPING into the market, pump days included; holders get none of the revenue.

| 📊 Market (CoinGecko, 16 Nov 2026 ~12:30 PM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.000410 | **Supply** 10B, fixed |
| **24h / 7d / 30d** 🔴 −5.9% / 🔴 −16.5% / 🔴 −31.4% | **Deployer** 5.94B (59.4%) |
| **Market cap** not reported · **FDV** $4.10M | **Next holders** 1.31B, 734M, 338M (Coinbase Prime custody; Coinbase-funded; unlabelled) |
| **24h volume** ~$15.4k (Coinbase USD $15.0k, Gate $403) | **Gate deposit wallet** 80M |
| **ATH** $0.1023 (20 Jan 2022) · now −99.6% | |
| **Pump days** 19 in the last year (Gate SHPING_USDT; largest +31.7% on 20 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- Shping earns money from brands that pay to reach app users. That is company revenue, not token revenue: no burn, buyback, fee share or staking yield.

**What it means:** none of it reaches holders. **Holder test: no** (no on-chain mechanism). **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- Run by an Australian private company (Shping Holdings, Melbourne), with leadership named on its site; described here by role only. The app is live with 300k+ users, a Coinbase cash-out integration (Sep 2024), a New Zealand launch (Oct 2026) and a Google product-ratings feed (Jul 2026) [Tier B, company posts].

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

- The Etherscan-tagged **Shping: Deployer** [`0x52a6…5a03`](https://etherscan.io/address/0x52a6de898366662724725e206d8fe350fe535a03) still holds **5.94B SHPING (59.4%)**.
- **Attribution confidence:** high (Etherscan name tag plus on-chain proof: it created the contract). The next three holders are not counted as company-controlled. Arkham labels the 1.31B holder [0xbb10…7472](https://intel.arkm.com/explorer/address/0xbb107e9b60d0655a6635b79a39647514d6d57472) **Coinbase Prime Custody**, fed by another Prime custody wallet. The 734M holder [0x3243…6132](https://intel.arkm.com/explorer/address/0x3243ce0cd2c1ab53d24ccb58caf0c82ac9846132) was funded from [Coinbase: Hot Wallet](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43), the "busy intermediary", and carries no more specific label. The 338M holder is unlabelled. Exchange custody or exchange funding does not show company control, and the report has no other proof, so none of them moves this score. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- The company said early on that a large incentive reserve would fund user rewards ([token-sale one-pager](https://tokensale.shping.com/assets/shping_coin_one_pager_en.pdf)). Score 2 for 59% held by one company-controlled wallet.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

- **Trail:** deployer [`0x52a6…5a03`](https://etherscan.io/address/0x52a6de898366662724725e206d8fe350fe535a03) → operating wallet [`0xb224…c915`](https://etherscan.io/address/0xb2242f32aa8751d1a754e5ccd8eee904cd21c915) (4.01B in 31 transfers, 2018 to 14 Nov 2026) → exchange deposit addresses.
- **Last 12 months (16 Nov 2025 – 16 Nov 2026):** 446M to Gate deposit [`0x1a54…4cca`](https://etherscan.io/address/0x1a545fffadf2f4c3cb34a222756632dd31814cca) (30 transfers), 120M to two Poloniex deposits and 42M to MEXC-forwarding deposits, for **609M SHPING ≈ $520k** at each day's close.
- **What the attribution rests on:** the deployer-to-operating-wallet link is on-chain and direct (one hop; 4.01B of the wallet's 4.19B inflows in 31 transfers over eight years), not an Arkham label. Arkham labels the deployer [Shping](https://intel.arkm.com/explorer/address/0x52a6de898366662724725e206d8fe350fe535a03) and shows it still sending to the operating wallet (74.2M two days before this read), but gives [0xb224…c915](https://intel.arkm.com/explorer/address/0xb2242f32aa8751d1a754e5ccd8eee904cd21c915) no label of its own. Arkham confirms [0x1a54…4cca](https://intel.arkm.com/explorer/address/0x1a545fffadf2f4c3cb34a222756632dd31814cca) as a **Gate Deposit** forwarding to Gate's hot wallet and [0x2b90…11ae](https://intel.arkm.com/explorer/address/0x2b902bbd97f3e0cb90dd9cc07ccc60d4d16c11ae) as a **MEXC Deposit**. Whose Gate account is credited is not shown [Unverified], but a deposit address belongs to one exchange account, so the coins left company control on arrival. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).
- **Pump days:** 152M (~$149k) was deposited on 8 pump days. Every transfer below has status 1:

| Date (UTC) | Pump | SHPING | ≈ USD | Tx |
|---|---|---|---|---|
| 8 Jan 2026 | +23.1% | 11.0M to Gate + 11.0M to MEXC | $55k | [Gate](https://etherscan.io/tx/0x604569ff066f30c3679ff2fcb932cf651170d27e7b7a740e77f27f6f11ee2f86) · [MEXC](https://etherscan.io/tx/0x6203737cf913b51cb0dfab80ae9409c4f7334aa6dd4f4afee04f64e5737792f2) |
| 7 Mar 2026 | +20.1% | 12.6M to Gate | $19k | [tx](https://etherscan.io/tx/0xae889ab951f1badbd99aea008862f5a0dca5d97f2048286e96ca885dd004513c) |
| 21 Aug 2026 | +26.4% | 16.0M to Gate | $10k | [tx](https://etherscan.io/tx/0xfef7fd2f9c78e50bd5afe9f7e6cf4930c5c6b308ff7fcb6160d3089320e3de7d) |
| 22 Aug 2026 | +16.5% | 17.1M to Gate | $9k | [tx](https://etherscan.io/tx/0x0cf06cdcc1b7d78fefcdd1ac4f6a248ec1fbf214f872004ad52f3e1234a73c7c) |
| 24 Aug 2026 | +12.0% | 19.1M to Gate | $10k | [tx](https://etherscan.io/tx/0xe9dd35d70100b48f72c3ba0c53cc227654df59a82a791116c3d6dd8a41f01b4b) |
| 26 Sep 2026 | +23.3% | 36.6M to Gate | $26k | [tx 1](https://etherscan.io/tx/0x3ec1baf1ab1985a967635cf1cde5033aba034a91273030d585959c580d77c6c7) · [tx 2](https://etherscan.io/tx/0x562125817b5ae0eff4e85fc324ba444a595c0ac2e78f9f835f118d57c0e86423) |
| 30 Sep 2026 | +14.9% | 28.7M to Gate | $19k | [tx 1](https://etherscan.io/tx/0x47a516302d96e565706fc1c95bff22e1a55d6960962f8c89a13285fda210e063) · [tx 2](https://etherscan.io/tx/0xe3f6f42b531955a6bdf9f74cbfebd14e58803a596653c0d0169f04817fc0c835) |

- **Attribution confidence:** sender high (deployer-funded, with on-chain proof); Gate and MEXC deposit labels medium (Etherscan tag or forwarding pattern only). A deposit isn't a recorded sale, but repeated deposits to one Gate account over four years point to a seller.
- **Alternative:** the company may be converting coins to pay members who cash out to Australian dollars. That is still company selling into the market.
- **Disclosure quality:** buried. A Sep 2024 [company post](https://shping.com/australias-first-rewards-program-to-offer-cryptocurrency-cash-outs/) says members can convert coins to AUD, which implies company conversions, but no sale schedule, amounts or wallet are published. Under the 16 Nov 2026 one-hop amendment this published cash-out program is a plausible reason for the deposits, and no team-attributed exchange account or sale evidence exists, so Selling is **4 (not proven)**, with no penalty and no hard gate.

- **One-hop amendment (16 Nov 2026):** Shping published a plausible reason: its [company post](https://shping.com/australias-first-rewards-program-to-offer-cryptocurrency-cash-outs/) says rewards members can convert coins to AUD, so operating-wallet deposits to exchanges fit funding those cash-outs. Neither (a) nor (b) holds: no exchange account is attributed to the team, and no swap, proceeds return or statement shows a sale. Under the amended rule Selling scores **4 (not proven)** with no silence penalty; this replaces the earlier score and penalty described above.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 10B fixed supply, all minted in 2018. Circulating supply isn't reported by CoinGecko. With 59% in the deployer, the free float depends on how fast the company releases coins.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- About $15k a day, almost all on Coinbase's USD pair; Gate trades a few hundred dollars.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The app works and ships features (receipt scanning, reviews, cash-outs, NZ launch).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- 300k+ app users claimed [Tier B]. The token mostly moves between the company, users and exchanges.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- A simple 2018 ERC-20 contract. No exploit found.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Australian company. No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- NZ expansion and brand deals. No token-specific catalyst.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: 152M (~$149k) on 8 pump days; buried disclosure |
| Live mint path | 🟢 None; fixed supply |
| Entity concentration | 🔴 Deployer 59.4% |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): entity labels for the deployer, operating wallet, Gate and MEXC deposits, the Coinbase hot wallet and the 1.31B and 734M holders
- [Tier A] Etherscan: token holders, contract creation, deployer and operating-wallet transfers (linked above)
- [Tier A] [Shping cash-out post](https://shping.com/australias-first-rewards-program-to-offer-cryptocurrency-cash-outs/), [token-sale one-pager](https://tokensale.shping.com/assets/shping_coin_one_pager_en.pdf)
- [Tier A] CoinGecko `shping` (market, venues); pump days from Gate SHPING_USDT daily closes (UTC), per the price-source hierarchy (Binance unavailable; Gate's pair is thin)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Deployer created the contract and holds 59.4% | [contract creation](https://etherscan.io/tx/0x96c6c3af8fa91be1e1cd732766793b66157283256775aa0c5516c6e7546e6d83) · [`0x52a6…5a03`](https://etherscan.io/address/0x52a6de898366662724725e206d8fe350fe535a03) | A | 16 Nov 2026 |
| Deployer funded the operating wallet with 4.01B | [`0xb224…c915`](https://etherscan.io/address/0xb2242f32aa8751d1a754e5ccd8eee904cd21c915) | A | 16 Nov 2026 |
| Pump-day deposits (table in Selling) | Gate deposit [`0x1a54…4cca`](https://etherscan.io/address/0x1a545fffadf2f4c3cb34a222756632dd31814cca) · MEXC deposit [`0x2b90…11ae`](https://etherscan.io/address/0x2b902bbd97f3e0cb90dd9cc07ccc60d4d16c11ae) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Is the Gate deposit the company's own account?** | Arkham (16 Nov 2026) confirms a Gate deposit but not the account owner; ask Shping | Free |
| 2 | **Who owns the 734M and 338M holders?** | Arkham (16 Nov 2026): 1.31B is Coinbase Prime custody and 734M was funded from the Coinbase hot wallet; ask Shping whether either is its custody account | Free |
| 3 | **Does Shping report coin conversions?** | Ask the company for a conversion log | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
