---
ticker: FXS
name: Frax (prev. FXS)
chain: ethereum
contract: "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0"
overall_score: 4.6
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 7
  adoption_customers: 5
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: none found
  mint_path_live: "yes, by governance: FIP-441 (passed 5 Feb 2026) caps supply at 143M and pre-mints 43M FRAX for team-run budgets, FPIS redemptions and the legacy-FRAX wind-down; on-chain execution of the pre-mint not confirmed"
  team_wallet_to_exchange_during_pump: "small: the Comptroller Safe swapped 13,794 WFRAX to frxUSD via CoW Protocol on 21 Jan 2026 (+46% over 5 days); its 469k WFRAX of 2026 sales are otherwise steady monthly spends"
  treasury_in_single_key_wallets: "no (the Comptroller is a 3-of-5 Safe)"
price_usd: 0.209061
price_source: "CoinGecko, 16 Nov 2026 8:20 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### FXS · Overall grade **4.6 / 10 · ❌ FAIL**

**Summary:** Frax renamed FXS to **FRAX** in 2025 and made it the gas token of its own Layer 2, Fraxtal. The protocol is real and busy (frxUSD stablecoin, frxETH, Fraxlend, Fraxswap), with **$8.9M of fees and $476k of revenue over the last year** on DefiLlama. But almost none of that reaches the token: DefiLlama tracks **$0 of holder revenue**, and governance only allows "up to 10%" to veFRAX. In Feb 2026, FIP-441 fixed supply at **143M** and pre-minted **43M FRAX** for team-run budgets, which is **+43% over the 99.7M ERC20 supply**. The price is down **99.5% from ATH and 78% in a year**. No hard gate trips, but the average fails.

**🚨 Top warning:** dilution is pre-approved and the team spends it. FIP-441 ([forum](https://gov.frax.finance/t/fip-441-frax-1-token-1-mission-1-vision/3826)) allows **23M FRAX of yearly budgets the team "retains discretion" over**, plus 10M for FPIS redemptions and 10M to defend the legacy-FRAX peg. Meanwhile, the **Frax Comptroller** Safe [`0xB174…3f27`](https://etherscan.io/address/0xb1748c79709f4ba2dd82834b8c82d4a505003f27) sold **469k WFRAX for stablecoins** through CoW Protocol in Jan–Nov 2026, including [13,794 WFRAX on 21 Jan 2026](https://etherscan.io/tx/0x5dd3efa075db569d8401535242494ee96b9cbaf77533704e7a253dba51258b7a), a day when the price was 46% above its close five days earlier. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 FXS · Frax (prev. FXS) · 4.6 / 10 · ❌ FAIL

> **One line:** A real DeFi stack with real fees, but the token captures almost none of them, 43M new tokens are pre-approved for team budgets, and the price has fallen 78% in a year.

| 📊 Market (CoinGecko, 16 Nov 2026 8:20 AM MST) | 🔗 On-chain (Ethereum + Fraxtal, 16 Nov 2026) |
|---|---|
| **Price** $0.209061 | **ERC20 FXS** [`0x3432…64d0`](https://etherscan.io/token/0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0) supply 99,681,496; 18,644 holders (Blockscout) |
| **24h / 7d / 30d** 🔴 −3.1% / −10.5% / −26.9% · 1y −78.5% | **Locked in the Fraxtal bridge** [`0x36cb…6f6D`](https://etherscan.io/address/0x36cb65c1967a0fb0eee11569c51c2f2aa1ca6f6d) 54,564,614 (Etherscan: "Fraxtal: Optimism Portal Proxy") |
| **Market cap** $19.56M · **FDV** $20.84M | **veFXS** [`0xc841…c5b0`](https://etherscan.io/address/0xc8418af6358ffdda74e09ca9cc3fe03ca6adc5b0) 14,426,204 |
| **24h volume** $330k (Binance, MEXC, Bithumb, WEEX) | **Comptroller** 3-of-5 Safe [`0xB174…3f27`](https://etherscan.io/address/0xb1748c79709f4ba2dd82834b8c82d4a505003f27) 2,848,699 FXS |
| **ATH** $42.80 (12 Jan 2022) · now −99.5% | **Supply cap** 143M (FIP-441) |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, last 12 months | **$8.90M** ($687k last 30 days) | [Tier A] [DefiLlama fees](https://api.llama.fi/summary/fees/frax-finance?dataType=dailyFees) |
| Protocol revenue, last 12 months | **$476k** ($36k last 30 days) | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/frax-finance?dataType=dailyRevenue) |
| Revenue to token holders | **$0 tracked**; FIP-441 allows "up to 10% of eligible net protocol revenue" to veFRAX, reviewed every six months | [Tier A] [DefiLlama](https://api.llama.fi/summary/fees/frax-finance?dataType=dailyHoldersRevenue) · [FIP-441](https://gov.frax.finance/t/fip-441-frax-1-token-1-mission-1-vision/3826) |
| Price / revenue | ≈ **41×** ($19.56M cap ÷ $476k) | Calculated |
| Burn Engine | 100% of the 8% frxETH fee buys and burns FRAX from Q4 2026; frxETH made $53.4k of fees in Q3 (~$214k a year, ≈1.1% of market cap) | [Tier B] [TokenPost](https://www.tokenpost.com/news/technology/56133) + [Leviathan News](https://leviathannews.xyz/333694/frax-launches-burn-engine-to-buy-back-and-burn-frax-using-frxeth-protocol-revenue) |

**What it means:** The revenue is real and checkable, unlike most coins in this list. But it is small against the market cap, and FIP-441 explicitly puts frxUSD growth ahead of "near-term value extraction" for holders. **4**: above the gate, below a pass.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Company | Frax launched in Dec 2020. FIP-441 splits intellectual-property ownership between the Frax DAO and Frax Inc. / the core team | [Tier A] [FIP-441](https://gov.frax.finance/t/fip-441-frax-1-token-1-mission-1-vision/3826) |
| Governance | veFXS Snapshot votes; FIP-441 passed 5 Feb 2026 with 29.66M veFXS for and 0.08 against | [Tier A] [Frax update #32](https://news.frax.com/p/frax-finance-biweekly-project-update-db3) · [Tier B] [Caper wiki](https://caper.network/wiki/daos/stablecoins/frax-finance) |
| Disclosure | Public forum, biweekly updates and quarterly reports; the Comptroller wallet is labelled on Etherscan | [Tier A] [news.frax.com](https://news.frax.com/) |
| Weak spot | Votes are near-unanimous (0.08 against), and the gauge sunset promised for 2026 had not been voted on by late Sep 2026 | [Tier B] [Caper wiki](https://caper.network/wiki/daos/stablecoins/frax-finance) |

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | Amount | Notes |
|---|---:|---|
| Fraxtal bridge (Optimism Portal) [`0x36cb…6f6D`](https://etherscan.io/address/0x36cb65c1967a0fb0eee11569c51c2f2aa1ca6f6d) | 54.56M FXS | FXS locked to back native FRAX on Fraxtal; not a team wallet [Tier A label + RPC] |
| veFXS [`0xc841…c5b0`](https://etherscan.io/address/0xc8418af6358ffdda74e09ca9cc3fe03ca6adc5b0) | 14.43M FXS | Holder locks; migrating to veFRAX on Fraxtal |
| **Frax Comptroller** [`0xB174…3f27`](https://etherscan.io/address/0xb1748c79709f4ba2dd82834b8c82d4a505003f27) (3-of-5 Safe) | 2.85M FXS + WFRAX + 1.81M native FRAX on Fraxtal | Treasury and spending wallet. FIP-441 says it held 6.4M FRAX for FPIS redemptions [Tier A] |
| FIP-441 pre-mint | **43M FRAX** | Team-run budgets, FPIS redemptions and the legacy-FRAX peg. **Where it sits and whether it was minted is [Unverified]** |
| Unlabelled EOAs | 0.9–2.2M each | Seven EOAs in the top 15 ([`0xe0dd…2f5f`](https://etherscan.io/address/0xe0dd07b181ca77ed9063821b4d2d28a85f722f5f), [`0x12D7…1100`](https://etherscan.io/address/0x12d7df4910d3dc0867cc7720e3bec6260b4b1100), [`0xdc87…2A6a`](https://etherscan.io/address/0xdc87397165b4f0f6d586f1bf60fa37494a362a6a) …); owners not known |

- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [the Comptroller](https://intel.arkm.com/explorer/address/0xb1748c79709f4ba2dd82834b8c82d4a505003f27) is labelled **Frax Finance: Comptroller** (multisig, 2.849M FXS); [`0x36cb…`](https://intel.arkm.com/explorer/address/0x36cb65c1967a0fb0eee11569c51c2f2aa1ca6f6d) is the **Fraxtal Optimism Portal** (54.6M FXS, ordinary bridge flows) and [`0xc841…`](https://intel.arkm.com/explorer/address/0xc8418af6358ffdda74e09ca9cc3fe03ca6adc5b0) is **veFXS** (14.4M). None of the large unlabelled holders ([`0xe0dd…`](https://intel.arkm.com/explorer/address/0xe0dd07b181ca77ed9063821b4d2d28a85f722f5f) 2.19M, [`0x12d7…`](https://intel.arkm.com/explorer/address/0x12d7df4910d3dc0867cc7720e3bec6260b4b1100) 2.07M, [`0xdc87…`](https://intel.arkm.com/explorer/address/0xdc87397165b4f0f6d586f1bf60fa37494a362a6a) 1.70M, [`0x6fcf…`](https://intel.arkm.com/explorer/address/0x6fcfee4f14eafa723d90ad4b282757c5fe3d92ee) 1.42M, [`0xd8b4…`](https://intel.arkm.com/explorer/address/0xd8b42cebc82607226f68a5373d99f54b397f886a) 1.20M, [`0xd53e…`](https://intel.arkm.com/explorer/address/0xd53e50c63b0d549f142a2dcfc454501aaa5b7f3f) 1.05M, [`0x602d…`](https://intel.arkm.com/explorer/address/0x602d9abd5671d24026e2ca473903ff2a9a957407) 0.66M) carries a Frax or team label. Their histories look like veFXS lockers and DeFi traders (`0xd8b4` was filled by `0x12d7`, so the two are one holder). Owners stay [Unverified].

**What it means:** The visible treasury is small and in a multisig. But up to 43M new FRAX (≈2.2× today's free float held by the Comptroller) is earmarked for the team to spend. **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Pump test uses Gate FRAX/USDT (formerly FXS) daily closes (UTC). 31 of the last 365 days were pump days. Ethereum flows of the Comptroller were tested.*

| Day (UTC) | Route | Amount | 5-day change | Pump? |
|---|---|---:|---:|---|
| 21 Jan 2026 | Comptroller → CoW Protocol: **13,794 WFRAX → 14,346 frxUSD** ([tx](https://etherscan.io/tx/0x5dd3efa075db569d8401535242494ee96b9cbaf77533704e7a253dba51258b7a)) | 13,794 | +46.3% | **Yes** |
| Jan–Nov 2026 | Comptroller → CoW Protocol, WFRAX → USDC / USDT / frxUSD, every month | 469,100 total (~18k–78k a month) | mixed | 1 of the swaps |
| 18–22 Jan 2026 | Comptroller → CoW Protocol: FXS → WFRAX, 1:1 (e.g. [200k on 21 Jan](https://etherscan.io/tx/0x98ddce5d6ec988b286df29de327458f6500015262e02c84f2c275636c0a2cc93), [43k on 18 Jan](https://etherscan.io/tx/0x5f02d7fc115203c671eb470b769ab78714618aeb70ff91fd92534d64ede8c4a0)) | 4.4M in Jan–Feb | +21% to +58% | Pump days, but **a token conversion, not a sale** |

- **Odos, not a budget wallet:** the Comptroller's 1.0M FXS to [`0x3650…`](https://intel.arkm.com/explorer/address/0x365084b05fa7d5028346bd21d842ed0601bab5b8) on 16 Jan 2026 went to a contract Arkham labels **Odos (DEX aggregator)** ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)). Each of the three transfers ([300k](https://etherscan.io/tx/0x43c7e952e5d520ab4b33737c3b1b879a8c3aab193ef4efe70c22af91ca68db08), [300k](https://etherscan.io/tx/0x05da6f205e90dfbdf742784d1ed69833c7458467698b14f5d9a7f87b77bb7ef8), [400k](https://etherscan.io/tx/0x22f3b121bd47fc83d25daadff8fb4776319d8816e9792909f6f7a66ec8fec11e)) returned WFRAX to the Comptroller in the same transaction (1,009,238 WFRAX in total), so it is the same FXS→WFRAX conversion. 16 Jan was not a pump day (Gate close −5.0% vs five days earlier).
- The FXS→WFRAX swaps looked like a 4.4M dump at first. The same transactions return WFRAX 1:1 to the Comptroller, so they are a migration, not a sale.

**What it means:** The treasury sells a steady ~$40–80k of FRAX a month for stablecoins, in line with FIP-441's spending budgets. One small sale (~$14k) landed on a pump day, five days before FIP-441 was posted. **4**: proven but small, so above the gate.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **Cap 143M** against 99.7M ERC20 supply and 93.6M circulating. The 43M pre-mint is spending headroom: up to 4M a year to Mar 2028, then falling to 2M ([FIP-441](https://gov.frax.finance/t/fip-441-frax-1-token-1-mission-1-vision/3826)).
- The 3% perpetual tail emission was removed, and Fraxtal gas fees are now recycled rather than burned.
- The Burn Engine is the only offset, at roughly 1% of market cap a year.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $330k of 24h volume on a $19.56M cap (1.7% turnover). Rank #774.
- −99.5% from ATH, −78.5% over a year, −27% in 30 days; near its all-time low ($0.2049).

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Fraxtal (an OP-Stack Layer 2 with FRAX as gas), frxUSD and sfrxUSD, frxETH, Fraxlend and Fraxswap are all live ([DefiLlama child protocols](https://api.llama.fi/summary/fees/frax-finance?dataType=dailyFees)).
- Active governance pipeline, including FIP-448 (FPI wind-down) and FIP-450/451 (sfrxUSD strategies) [Tier B] [Caper wiki](https://caper.network/wiki/daos/stablecoins/frax-finance).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- $8.9M of yearly fees shows real users. frxETH holds ~$120M TVL [Tier B ×2: [DefiEdge](https://defiedge.com/defi/frax-finance-routes-frxeth-fees-to-programmed-frax-buyba-63c63d44), [Phemex](https://phemex.com/news/article/frax-finance-launches-frax-burn-engine-using-protocol-revenue-for-buybacks-and-burns-103395)].
- Usage does not translate into token demand: WFRAX has only 1,020 holders on Ethereum (Blockscout).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of the FRAX token or the core contracts found in this pass. The treasury is a 3-of-5 Safe (Tier A `getThreshold()`).
- Bridge risk: 54.6M FXS sit in the Fraxtal Optimism Portal.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. frxUSD is a US-dollar stablecoin, so stablecoin rules apply to the main growth product [Unverified].

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Q4 2026 | Burn Engine starts buying FRAX with frxETH fees [Tier B ×2] |
| 2026 (late) | Promised vote to sunset the FXS gauges [Tier A FIP-441] |
| Apr 2027 | Year-3 budget of up to 4M FRAX opens |
| Every 6 months | veFRAX revenue-share review |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 One small Comptroller swap (13,794 WFRAX) on a pump day ([tx](https://etherscan.io/tx/0x5dd3efa075db569d8401535242494ee96b9cbaf77533704e7a253dba51258b7a)) |
| Live mint path | 🔴 43M pre-mint approved by governance; execution [Unverified] |
| Treasury in single-key wallets | 🟢 No (3-of-5 Safe) |

## 📚 Sources

- [Tier A] Etherscan v2 API `tokentx` for the Comptroller (FXS, WFRAX and stablecoins), read 16 Nov 2026 ~8:30–8:45 AM MST; Ethereum RPC `getThreshold()`, `getOwners()`; Fraxtal balance via Etherscan v2 (chain 252)
- [Tier A] Blockscout FXS holders and counters; WFRAX token page
- [Tier B] Etherscan name tags ("Fraxtal: Optimism Portal Proxy", "Frax Finance: veFXS Token", "Frax Finance: Comptroller", "CoW Protocol: GPv2Settlement")
- [Tier A] [FIP-441 forum post](https://gov.frax.finance/t/fip-441-frax-1-token-1-mission-1-vision/3826) · [Frax biweekly update #32](https://news.frax.com/p/frax-finance-biweekly-project-update-db3)
- [Tier A] DefiLlama fees / revenue / holders revenue for `frax-finance`
- [Tier B] [Caper wiki](https://caper.network/wiki/daos/stablecoins/frax-finance) · [TokenPost](https://www.tokenpost.com/news/technology/56133) · [Leviathan News](https://leviathannews.xyz/333694/frax-launches-burn-engine-to-buy-back-and-burn-frax-using-frxeth-protocol-revenue) · [DefiEdge](https://defiedge.com/defi/frax-finance-routes-frxeth-fees-to-programmed-frax-buyba-63c63d44)
- [Tier A] CoinGecko `frax-share` (16 Nov 2026 8:20 AM MST); Gate FRAX/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): entity labels for the Comptroller, Fraxtal portal, veFXS and Odos; no team label on the top unlabelled EOAs (links in Holdings and Selling)
- [Tier A] Etherscan v2 API `tokentx` for the 16 Jan 2026 Odos transactions; Gate FRAX/USDT close for 11 and 16 Jan 2026
- [Unverified] Execution and location of the 43M pre-mint; owners of the large unlabelled EOAs; Fraxtal-native treasury flows

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 143M cap, 43M pre-mint, team budget discretion, up to 10% to veFRAX | [FIP-441](https://gov.frax.finance/t/fip-441-frax-1-token-1-mission-1-vision/3826) | A | 16 Nov 2026 |
| FIP-441 passed 5 Feb 2026 | [Frax update #32](https://news.frax.com/p/frax-finance-biweekly-project-update-db3) | A | 16 Nov 2026 |
| Comptroller pump-day WFRAX → frxUSD swap | [tx, 21 Jan 2026](https://etherscan.io/tx/0x5dd3efa075db569d8401535242494ee96b9cbaf77533704e7a253dba51258b7a) | A | 16 Nov 2026 |
| FXS → WFRAX conversions are 1:1 | [200k, 21 Jan 2026](https://etherscan.io/tx/0x98ddce5d6ec988b286df29de327458f6500015262e02c84f2c275636c0a2cc93) · [43k, 18 Jan 2026](https://etherscan.io/tx/0x5f02d7fc115203c671eb470b769ab78714618aeb70ff91fd92534d64ede8c4a0) | A | 16 Nov 2026 |
| Comptroller is a 3-of-5 Safe | [Safe](https://etherscan.io/address/0xb1748c79709f4ba2dd82834b8c82d4a505003f27#readProxyContract) | A | 16 Nov 2026 |
| 54.56M FXS in the Fraxtal bridge | [Optimism Portal](https://etherscan.io/address/0x36cb65c1967a0fb0eee11569c51c2f2aa1ca6f6d) | A | 16 Nov 2026 |
| $476k revenue, $0 holder revenue | [revenue](https://api.llama.fi/summary/fees/frax-finance?dataType=dailyRevenue) · [holders](https://api.llama.fi/summary/fees/frax-finance?dataType=dailyHoldersRevenue) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Owners of the large unlabelled FRAX wallets and the Comptroller signers** | Arkham (16 Nov 2026) gives no entity for the seven top-15 EOAs and does not show the Safe signers' identities. Ask Frax for its budget-wallet list [Unverified] | Free |
| 2 | **Was the 43M pre-mint executed, and where is it?** | Check Fraxtal mint events and Comptroller balances on fraxscan.com; ask Frax for the budget wallet list | Free |
| 3 | **Fraxtal-native treasury sales** | Trace the Comptroller and budget wallets on Fraxtal and pump-test them | Free / API |
| 4 | **Burn Engine delivery** | Watch for the first FRAX burns in Q4 2026 and compare them with frxETH fees | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
