---
ticker: AMP
name: Amp
chain: ethereum
contract: "0xff20817765cb7f73d4bde2e66e067e58d11095c2"
overall_score: 4.2
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 7
  liquidity_market: 4
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "no open mint: new AMP only via the one-way Flexacoin (FXC) swap, which caps supply just under 100B"
  team_wallet_to_exchange_during_pump: "not tested (Flexa treasury wallets are not published); the one large exchange send found (200M, 30 Apr 2026) was a Gemini cold-to-hot wallet move, not a sale"
  treasury_in_single_key_wallets: "unknown (Flexa treasury wallets not published)"
price_usd: 0.00053114
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### AMP · Overall grade **4.2 / 10 · ❌ FAIL**

**Summary:** Amp is the collateral token behind Flexa's crypto payments network. Holders stake AMP into pools that guarantee merchant payments. Supply is fixed (99.72B of a ~100B cap) and there is no open mint. But AMP earns **no checkable revenue**: DefiLlama tracks no fees for Flexa, and Flexa does not publish payment volumes. Collateral in the pools **fell ~4.5% from late Sep to early Nov 2026**. About **9.94B AMP (10% of supply) is outside circulating supply**, presumably Flexa's treasury, in wallets that are not published. The price is down **99.6% from ATH and 78% in a year**. Revenue trips the hard gate.

**🚨 Top warning:** no measurable value flows to the token, and the treasury is a black box. The Anvil **CollateralVault** [`0x5d27…675f`](https://etherscan.io/address/0x5d2725fde4d7aa3388da4519ac0449cc031d675f) holds 20.68B AMP of staked collateral, but no fee figure is attached to it. Flexa says it has sold "nearer to 1%" of its treasury on the open market since 2018 ([Tier B, quoted on r/AMPToken](https://www.reddit.com/r/AMPToken/comments/1suqdu6/this_quote_needs_to_be_shouted_from_the_top_of_a/)). Without published wallets, that cannot be checked.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 AMP · Amp · 4.2 / 10 · ❌ FAIL

> **One line:** A fixed-supply collateral token with a real payments company behind it, but no visible revenue for holders, shrinking collateral, and an unpublished treasury.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.00053114 | **Total supply** 99.72B AMP of a ~100B cap |
| **24h / 7d / 30d** 🔴 −2.0% / −17.1% / −27.5% · 1y −77.9% | **Circulating** 89.78B (CoinGecko), so 9.94B is outside circulation |
| **Market cap** $47.67M · **FDV** $52.95M | **CollateralVault** [`0x5d27…675f`](https://etherscan.io/address/0x5d2725fde4d7aa3388da4519ac0449cc031d675f) 20.68B AMP |
| **24h volume** $10.34M (Binance, BtcTurk, BTCC) | **Flexa: Staking** [`0x706D…C578`](https://etherscan.io/address/0x706d7f8b3445d8dfc790c524e3990ef014e7c578) 1.68B (older pools) |
| **ATH** $0.1208 (16 Jun 2021) · now −99.6% | **Holders** 102,803 (Blockscout) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol fees / revenue | **Not tracked.** DefiLlama lists Flexa Payments with $892k TVL and no fee adapter | [Tier A] [DefiLlama protocol](https://api.llama.fi/protocol/flexa) |
| Flexa payment volume | **Not published** | [Tier B] [Tapbit](https://www.tapbit.com/en/learn/article/amp-collateral-anvil-value-capture-20261103) |
| Holder income | Pool rewards to collateral stakers; size not disclosed | — |

**What it means:** No revenue can be checked. **2, which trips the Revenue gate.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Flexa (a private US company) built AMP with ConsenSys in 2020. It handed stewardship of the Amp ecosystem to the Acronym Foundation in 2023, and that team built Anvil, the collateral protocol under Capacity v3 [Tier B ×2: [Phemex Academy](https://phemex.com/academy/what-is-amp-flexas-payment-collateral-token), [Tapbit](https://www.tapbit.com/en/learn/article/amp-collateral-anvil-value-capture-20261103)].
- Founders Fund led a $5M purchase of **ANVL** (Anvil's token, not AMP) in Oct 2026 [Tier B, Tapbit], so the investor upside sits in a different token.
- New CEO in Jun 2026; European (SEPA) launch in Jul 2026 [Tier B].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | AMP | Notes |
|---|---:|---|
| Anvil CollateralVault [`0x5d27…675f`](https://etherscan.io/address/0x5d2725fde4d7aa3388da4519ac0449cc031d675f) | 20.68B | Staked user collateral, not a team wallet. [Arkham](https://intel.arkm.com/explorer/address/0x5d2725fde4d7aa3388da4519ac0449cc031d675f): **Anvil: CollateralVault** (verified contract); it does not show who controls upgrades |
| Non-circulating supply | ~9.94B | Total 99.72B minus circulating 89.78B; presumably Flexa's treasury; **wallets not published** [Unverified] |
| **Exchange custody, not the team** | ~30.4B | Arkham labels [`0xcD0C…F7C3`](https://intel.arkm.com/explorer/address/0xcd0c5310f150c820c0b0f01e0b7b0d42a940f7c3) (12.1B) and [`0x0C7B…4e9e`](https://intel.arkm.com/explorer/address/0x0c7bcb6e267d1ab436a7373243fc668e13f44e9e) (3.9B) **Coinbase: Cold Wallet**, [`0x9FcC…D3fD`](https://intel.arkm.com/explorer/address/0x9fcca33a3925f66570bf863d586ff50a508cd3fd) (4.4B) **Coinbase Prime Custody**, and their funder [`0xa9d1…3e43`](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) (1.3B) **Coinbase: Hot Wallet**. [`0x15Da…b0d7`](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) (3.9B) is **Revolut: Cold Wallet**; [`0xAd8a…26F0`](https://intel.arkm.com/explorer/address/0xad8ae4e49e764e95c786d4f9cb0110c2a15126f0) (4.0B) is **Gemini: Cold Wallet** and [`0x5f65…e932`](https://intel.arkm.com/explorer/address/0x5f65f7b609678448494de4c87521cdf6cef1e932) (1.0B) **Gemini: Hot Wallet**, not a Flexa treasury |

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate AMP/USDT daily closes (UTC): 25 of the last 365 days were pump days.*

| Day (UTC) | Route | AMP | 5-day change | Pump? |
|---|---|---:|---:|---|
| 30 Apr 2026 | Gemini Cold Wallet `0xAd8a…26F0` → Gemini 9 / Gemini Hot Wallet `0xF517…` ([tx](https://etherscan.io/tx/0xf7c683f6a70191f256d4af711fd9fb06fe77c5b1c0eee5995e84a4f3bb15c367)) | 200,000,000 | +0.7% | No; an internal Gemini move |

- **Correction ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the only large exchange send found was not "unattributed". Arkham labels the sender a Gemini cold wallet and the receiver a Gemini hot wallet, so it was Gemini moving its own custody, not a sale. The 3.9–12.1B holders are Coinbase, Revolut and Gemini custody wallets, so none of them is a team wallet either.
- Flexa's treasury wallets are not published, so **no team wallets were pump-tested**. Flexa says it has funded itself "almost exclusively through private sales of Amp to accredited investors" [Tier B quote, unverified].

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- 99.72B of ~100B issued. New AMP is minted only by swapping in Flexacoin (FXC), with ~279.7M FXC left. There is no burn, pause or freeze function; a ConsenSys Diligence audit (Jun 2020) found two major issues, both fixed [Tier B, [Phemex Academy](https://phemex.com/academy/what-is-amp-flexas-payment-collateral-token)].
- No inflation. The overhang is the ~9.94B outside circulation.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $10.3M of 24h volume on a $47.7M cap (22% turnover), led by Binance TRY/USDT and BtcTurk.
- −99.6% from ATH, −78% in a year.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Capacity v3 on Anvil (Feb 2025); SEPA rollout to 37 countries (Jul 2026). Flexa's newsroom posted nothing from Jul to mid-Oct 2026 [Tier B, Phemex Academy].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Capacity collateral fell from ~20.78B to ~19.84B AMP between late Sep and early Nov 2026 [Tier B, Tapbit]. On-chain, the vault holds 20.68B today (Blockscout). No payment-volume data.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. The contract is audited (ConsenSys Diligence, 2020). Collateral release takes 12–24 hours [Tier B].

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. AMP was among the tokens named in the SEC's 2022 insider-trading complaint against a former Coinbase employee [Unverified in this pass].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| TBA | Flexa "Terminal" product; European merchant data |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not tested (treasury unpublished) |
| Live mint path | 🟢 Only the FXC swap (~279.7M left) |
| Treasury in single-key wallets | 🟡 Unknown |

## 📚 Sources

- [Tier A] Etherscan v2 API `tokentx` for the top unlabelled holders, read 16 Nov 2026 ~8:45 AM MST; Blockscout holders, counters and contract names
- [Tier A] DefiLlama `flexa` protocol; CoinGecko `amp-token` (16 Nov 2026 8:34 AM MST); Gate AMP/USDT daily candles
- [Tier B] [Phemex Academy](https://phemex.com/academy/what-is-amp-flexas-payment-collateral-token) · [Tapbit](https://www.tapbit.com/en/learn/article/amp-collateral-anvil-value-capture-20261103) · [r/AMPToken quote](https://www.reddit.com/r/AMPToken/comments/1suqdu6/this_quote_needs_to_be_shouted_from_the_top_of_a/)
- [Tier B] Etherscan name tags (Gemini 9, Flexa: Staking, BtcTurk 13, eToro 4, Binance cold wallets)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Coinbase Cold Wallet, Coinbase Prime Custody, Coinbase Hot Wallet, Revolut Cold Wallet, Gemini Cold and Hot Wallet, Anvil CollateralVault (links in Holdings)
- [Unverified] Flexa treasury wallets and sales; payment volumes; SEC mention

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Vault holds 20.68B AMP | [CollateralVault](https://etherscan.io/address/0x5d2725fde4d7aa3388da4519ac0449cc031d675f) | A | 16 Nov 2026 |
| 200M AMP Gemini cold → Gemini hot on a non-pump day | [tx, 30 Apr 2026](https://etherscan.io/tx/0xf7c683f6a70191f256d4af711fd9fb06fe77c5b1c0eee5995e84a4f3bb15c367) · [Arkham label](https://intel.arkm.com/explorer/address/0xad8ae4e49e764e95c786d4f9cb0110c2a15126f0) | A + B | 16 Nov 2026 |
| No fee tracking for Flexa | [DefiLlama](https://api.llama.fi/protocol/flexa) | A | 16 Nov 2026 |
| Collateral fell ~4.5% Sep→Nov 2026 | [Tapbit](https://www.tapbit.com/en/learn/article/amp-collateral-anvil-value-capture-20261103) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the CollateralVault upgrades** | Arkham (16 Nov 2026) labels the vault but not its admin. Read the proxy admin on Etherscan and ask Anvil [Unverified] | Free |
| 2 | **Where are the ~9.94B non-circulating AMP?** | Ask Flexa, or ask CoinGecko which wallets it excludes | Free |
| 3 | **Payment volume and pool rewards** | Ask Flexa for monthly settlement volume | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
