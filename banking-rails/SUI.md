---
ticker: SUI
name: Sui
chain: sui
contract: "0x2::sui::SUI (native)"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 2
  selling_behavior: 2
  tokenomics_supply: 3
  liquidity_market: 7
  product_development: 7
  adoption_customers: 4
  security_audits: 4
  regulatory: 7
  catalysts: 5
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "no chain exploit; three mainnet halts on 28-29 May 2026 (upgrade bugs, postmortem published); Cetus app hack $223M in May 2025 (validators froze ~$160M)"
  treasury_to_exchange_during_pump: "no direct foundation-to-exchange send found"
  treasury_funded_wallet_to_exchange_during_pump: "yes (foundation 0x341f… funded 0x7f3b… with 310.6M SUI in 2023; via 0xbe90…/0x7f66… it fed Binance deposit 0x457f…, which put 166.0M SUI into Binance 1 in the last 12 months, 67.6M (≈ $72M) on pump days, e.g. 12.39M on 21 Aug 2026 +25.8%; foundation said in 2023 these were partner tokens under lock-up)"
  mint_path_live: "no (supply fixed at 10,000,000,000; read 16 Nov 2026)"
  undisclosed_allocation: "yes (52.2% of supply 'allocated after 2030', recipients not disclosed)"
price_usd: 0.713076
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SUI · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** Sui is a fast, well-built chain with three US ETFs and real developer activity. As a token, though, it barely earns anything: about $2.5M a year of gas fees, of which ~$0.6M is kept, on a $2.95B market cap ($7.1B fully diluted). One wallet, widely reported as the Sui Foundation's, still controls about 1.65B staked SUI (16.5% of supply). In the last year the wallet chain it funded sent 166M SUI through one Binance deposit address, 67.6M of it on pump days. More than half of all SUI (52.2%) is "allocated after 2030" to undisclosed recipients. Both the Revenue and the Selling gates fail.

**🚨 Top warning (red line):** The wallet reported as the **Sui Foundation's**, [`0x341f…fae1`](https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1), sent **310,595,908 SUI** to [`0x7f3b…39e4`](https://suiscan.xyz/mainnet/account/0x7f3b918653aacd4289b7e471aea588b34d497df0e1540c2d22eadacccd3239e4) on 16 Jun 2023 ([tx](https://suiscan.xyz/mainnet/tx/FdvGyjbAUUxwqHi1TzyoNWvSWocBSD6BhewNzi9Ssiq1)). In the last 12 months that wallet sent 85.9M to the transit wallet [`0xbe90…0aa8`](https://suiscan.xyz/mainnet/account/0xbe90dbe25c747f23e7b93f8948f240a90aa106597b7dab0b33e852b0b1950aa8), which fed [`0x457f…15e7`](https://suiscan.xyz/mainnet/account/0x457fd3e8295543c23cfc2182b33247338cb04ddf43d0afa02a34591fd67415e7). That address sweeps everything into **Binance 1** [`0x9350…9cbd`](https://suiscan.xyz/mainnet/account/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd): **166.0M SUI in 12 months, 67.6M (≈ $72M) on pump days.** On the **21 Aug 2026 pump day (+25.8%)**, `0xbe90…` sent 12.38M SUI to `0x457f…` in 65 transfers ([e.g.](https://suiscan.xyz/mainnet/tx/7PVDC5bPZiA1kq29GHDfLsWaPJm9Te6ngBTmTXeDS99t)), and `0x457f…` passed 12.39M to Binance the same day ([e.g.](https://suiscan.xyz/mainnet/tx/HAVg1gBoF9Dt2EgSZ93kGCdWSMzvjZFGa7PEGiHhnqpG)). **Second warning:** `0x341f…` also funded [`0x7f66…3bfb`](https://suiscan.xyz/mainnet/account/0x7f6626f0787309355b4b85de40596f5b096050eab5b9061dcb9001df961b3bfb) directly with 16.3M SUI on 18 Mar 2026 ([tx](https://suiscan.xyz/mainnet/tx/EvjjwGD6y4zJN9j57mvgiDTQ14Fk8Lujr9VMuNSyz9By)). That wallet sent 72.2M SUI to the same Binance deposit, including ~17.5M on 21–23 Sep 2026 (+46% to +18%). In 2023 the foundation said this route held "infrastructure partners" tokens under lock-up, not insider sales ([Cointelegraph via TradingView](https://www.tradingview.com/news/cointelegraph:8ed5311c3094b:0-sui-foundation-denies-it-sold-locked-staking-rewards-on-binance/)). Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 2/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SUI · Sui · 3.7 / 10 · ❌ FAIL

> **One line:** Strong technology and Wall Street access, but almost no fee revenue, a foundation wallet holding a sixth of supply, half the supply parked with undisclosed post-2030 recipients, and a foundation-funded wallet chain that keeps feeding Binance, often on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (Sui GraphQL, epoch 1313, 16 Nov 2026) |
|---|---|
| **Price** $0.713076 | **Total supply** `coinMetadata(SUI).supply` = **10,000,000,000** exactly |
| **24h / 7d / 30d** 🔴 −2.85% / −13.5% / −28.7% · 1y −58.5% | **Circulating** 4.139B (41.4%) per CoinGecko / DefiLlama |
| **Market cap** $2.951B · **FDV** $7.131B | **Foundation wallet** [`0x341f…`](https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1) 1,652,301,633 SUI staked in 110 stake objects + 6 liquid |
| **24h volume** $252.8M | **Binance deposit** [`0x457f…`](https://suiscan.xyz/mainnet/account/0x457fd3e8295543c23cfc2182b33247338cb04ddf43d0afa02a34591fd67415e7) → Binance 1: 166.0M SUI in 12 months |
| **ATH** $5.35 (4 Jan 2025) · now −86.7% | **TVL** $368.5M (DefiLlama; peak $2.64B, Oct 2025) |
| **Pump days, last 365** 41 (CoinGecko closes) | **Next unlocks** ~2.1M (28 Nov) and ~19–21M (30 Nov – 3 Dec 2026) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Sui gas fees, 30d / 1y | $77,886 / $2,484,953 | [Tier A] [DefiLlama Sui](https://defillama.com/chain/Sui) (protocol `sui`, 16 Nov 2026) |
| Sui revenue kept (storage fund / burn), 30d / 1y | **$722 / $617,748** | same |
| All apps on Sui, fees 30d / 1y | $3.10M / $57.3M (app revenue, not SUI's) | same (chain overview) |

**What it means:** The chain keeps about $0.6M a year against a $2.95B cap, roughly 0.02%. Gas is cheap by design (reference gas price 100 MIST). Score **1**, which **trips the Revenue gate**.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Builders | Mysten Labs builds the chain; the Sui Foundation runs grants, treasury and ecosystem | [Tier A] [sui.io](https://www.sui.io/blog/sui-mainnet-halts-resolved-after-major-upgrade) |
| Incident openness | A detailed postmortem of the May 2026 halts was published within days | [Tier A] [Sui blog](https://www.sui.io/blog/sui-mainnet-halts-resolved-after-major-upgrade) |
| Treasury openness | No official wallet list. `0x341f…` is the Foundation's by press tracing and Coincu; the foundation's own 2023 reply refers to "Sui Foundation's wallet address 0x341f" transactions | [Tier B] [Coincu](https://coincu.com/news/sui-foundation-token-transfers-draw-exchange) · [Tier B] [Cointelegraph](https://www.tradingview.com/news/cointelegraph:8ed5311c3094b:0-sui-foundation-denies-it-sold-locked-staking-rewards-on-binance/) |
| Undisclosed supply | 52.2% "allocated after 2030", recipients undisclosed | [Tier B] [Blockworks](https://app.blockworks.com/projects/sui/token-unlocks) · [Tier B] [CoinGlass](https://www.coinglass.com/currencies/SUI/vesting) |

**What it means:** A credible, well-funded team that writes good postmortems. But control of the supply is concentrated and the treasury is not published. Score **5**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Bucket | SUI | Notes |
|---|---:|---|
| Foundation wallet [`0x341f…`](https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1) | **1,652,301,633 staked (16.5% of supply)** | GraphQL `StakedSui` objects, 16 Nov 2026 |
| 13 single-stake wallets `0x341f…` funded on 30 Jan – 18 Feb 2026 (e.g. [`0x0345…`](https://suiscan.xyz/mainnet/account/0x0345cc00a2e6eeda03e54cf3c93f005d2b05f0790826c7507c6c3e366de8ccd4) 40M, [tx](https://suiscan.xyz/mainnet/tx/7p11PpgeAwi2DrGdyXoxenZongNvdX1Q8HkL31UjX9cL)) | **~414M staked** | Each holds one stake object; beneficiaries [Unverified] |
| `0x7f3b…` (2023 partner route) | 18,983,635 staked | still feeding `0xbe90…` |
| Not yet allocated / after 2030 | 5.22B (52.2%) | recipients undisclosed |

**What it means:** One foundation wallet holds more SUI than most of the float trades in a year. Add 52% of supply with no disclosed owner. Score **2**.

## 📉 Selling behavior — Do insiders sell into pumps? · 2/10 · ❌ FAIL

Route proven on-chain (Tier A); Binance identity of `0x9350…` from two Tier B labels ([Suiscan "Binance 1"](https://suiscan.xyz/mainnet/account/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd/portfolio) and [tide "Binance Hot Wallet 1"](https://tide.ad/address/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd)). `0x457f…` has sent SUI only to Binance 1 since May 2023, so it is a Binance deposit address.

| Day (UTC) | Route | SUI | 5-day change (CoinGecko) | Pump? |
|---|---|---:|---:|---|
| 16 Jun 2023 | Foundation `0x341f…` → `0x7f3b…` ([tx](https://suiscan.xyz/mainnet/tx/FdvGyjbAUUxwqHi1TzyoNWvSWocBSD6BhewNzi9Ssiq1)) | 310,595,908 | — | funding |
| 7 Jan 2026 | `0x7f3b…` → `0xbe90…` 17:44 ([tx](https://suiscan.xyz/mainnet/tx/Zhmd5wC9BC5ugKW5yJtLDCs1Fma81U8qK2C4pnMkUZp)) → `0x7f66…` 17:51 ([tx](https://suiscan.xyz/mainnet/tx/64W7VPF7gAP532cV2MAy8LumaJGWuNMziLiuqdxVv4jb)) | 5,000,000 | +12.9% | 🔴 Yes |
| 18 Mar 2026 | Foundation `0x341f…` → `0x7f66…` ([tx](https://suiscan.xyz/mainnet/tx/EvjjwGD6y4zJN9j57mvgiDTQ14Fk8Lujr9VMuNSyz9By)) | 16,295,641 | <10% | funding |
| 8–10 May 2026 | `0xbe90…` → Binance deposit `0x457f…` → Binance 1 | 17.6M in / 17.6M to Binance | up to +37.7% | 🔴 Yes |
| 21 Aug 2026 | `0xbe90…` → `0x457f…` (65 transfers, [e.g.](https://suiscan.xyz/mainnet/tx/7PVDC5bPZiA1kq29GHDfLsWaPJm9Te6ngBTmTXeDS99t)) → Binance 1 (38 sweeps, [e.g.](https://suiscan.xyz/mainnet/tx/HAVg1gBoF9Dt2EgSZ93kGCdWSMzvjZFGa7PEGiHhnqpG)) | 12,388,222 to Binance | +25.8% | 🔴 Yes |
| 21–22 Sep 2026 | `0xbe90…` → `0x7f66…` 19.6M ([21 Sep](https://suiscan.xyz/mainnet/tx/7c8YheAtCrLEefm1NuDfWupEB6jk3Tkh78WgZoUGzTSX) · [22 Sep](https://suiscan.xyz/mainnet/tx/2n5pWep6Ce3R1NrJpiMTjL6H6KGP8opecV4RM7ehMAnY)) → `0x457f…` ([e.g.](https://suiscan.xyz/mainnet/tx/CiuBqoQ3Xhn9PL42o6PFhsc3BDZArgqXNk5FMy8yRWJP)) → Binance ([e.g.](https://suiscan.xyz/mainnet/tx/7KdCv7LyG136NvvcHJN3pxCMFCrrRTmtBpBQ7YD6sQfg)) | 12.4M to Binance on 21–22 Sep (22.5M on 18–29 Sep) | +46.1% / +38.0% | 🔴 Yes |

- **12-month totals:** `0x457f…` → Binance 1 **165,960,975 SUI**, of which **67,588,059 on 37 pump days ≈ $72.2M** at those days' closes. `0xbe90…` sent 139.9M out (64.5M on pump days); `0x7f66…` sent 112.5M (48.0M on pump days).
- The foundation's 2023 position: these were "infrastructure partners on a lock-up period", and "Sui Foundation has not sold staking rewards or any other tokens from locked and non-circulating staked SUI" ([Cointelegraph](https://www.tradingview.com/news/cointelegraph:8ed5311c3094b:0-sui-foundation-denies-it-sold-locked-staking-rewards-on-binance/) · [Coincu](https://coincu.com/news/sui-foundation-token-transfers-draw-exchange)). Who controls `0x7f3b…`, `0xbe90…` and `0x7f66…` is [Unverified].

**What it means:** Whoever the end seller is, foundation-funded SUI reached Binance by the tens of millions in the last year, and much of it on pump days. The 18 Mar 2026 direct funding of `0x7f66…` shows the foundation is still funding the route. Score **2**, which **trips the Selling gate**.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- Supply is fixed at **10B** (GraphQL `coinMetadata`). Stake subsidies come from a pre-minted fund, not new issuance.
- Only **41.4%** is unlocked. Monthly unlocks of ~19–22M SUI (Early Contributors, Stake Subsidies, Community Reserve) and ~2.1M (Mysten Labs Treasury) run to 2030 ([Blockworks](https://app.blockworks.com/projects/sui/token-unlocks) · [CoinGlass](https://www.coinglass.com/currencies/SUI/vesting), Tier B ×2).
- **5.22B (52.2%) has no disclosed recipient or schedule** after 2030. FDV is 2.4 times the market cap.

## 💧 Liquidity & market · 7/10 · ✅ PASS

- $252.8M of 24h volume on a $2.95B cap (8.6%). SUI trades on Binance, Coinbase, Upbit and others, plus three US ETFs (GSUI, SUIS, TSUI).
- Down 86.7% from the Jan 2025 high and 58.5% over the year.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- `MystenLabs/sui`: last commit 14 Nov 2026, very active. Release 1.72 added address balances. Public JSON-RPC is being retired in favour of gRPC/GraphQL (the public fullnode now rejects `suix_*` calls).
- Epoch 1313 had processed 8.29M transactions by mid-day 16 Nov 2026 (GraphQL).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- TVL is **$368.5M**, down 86% from $2.64B in Oct 2025 ([DefiLlama](https://defillama.com/chain/Sui)).
- Apps on Sui still made $3.1M of fees in 30 days. The Canary SUIS ETF had $23.9M of net assets on 13 Nov 2026 ([Canary](https://canaryetfs.com/suis/)).

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- **28–29 May 2026: three mainnet halts** (~6.5h, ~3.5h, ~6h) from v1.72 gas-charging and randomness-state bugs. No funds were lost and no transactions were reverted ([Sui postmortem](https://www.sui.io/blog/sui-mainnet-halts-resolved-after-major-upgrade) · [CoinDesk](https://www.coindesk.com/tech/2026/06/01/three-sui-mainnet-halts-in-48-hours-traced-to-an-upgrade-bug-by-developers)). CoinDesk calls it the third major reliability failure since 2023.
- **May 2025 Cetus hack ($223M)** in an app's math library. Validators froze ~$160M, which shows the validator set can coordinate to freeze funds ([Cryptopolitan](https://www.cryptopolitan.com/us-sec-review-delays-21shares-sui-etf/)) [Tier B].

## ⚖️ Regulatory · 7/10 · ✅ PASS

- Three spot/staking SUI ETFs began trading on 18–24 Feb 2026: Grayscale GSUI (NYSE Arca), Canary SUIS and 21Shares TSUI (Nasdaq) ([Sui Monthly Feb 2026](https://www.sui.io/blog/sui-monthly-february-2026) · [Canary](https://canaryetfs.com/suis/)).
- No enforcement action against Mysten Labs or the Sui Foundation was found this pass.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| **28 Nov 2026** | Mysten Labs Treasury unlock ~2.1M SUI |
| **30 Nov – 3 Dec 2026** | Monthly unlock ~19–22M SUI (Early Contributors, Stake Subsidies, Community Reserve) |
| Monthly | Same pattern until 2030; then 5.22B with no disclosed schedule |
| Ongoing | ETF flows (SUIS $23.9M) and the `0x457f…` → Binance stream |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 No chain exploit; three halts on 28–29 May 2026. [postmortem](https://www.sui.io/blog/sui-mainnet-halts-resolved-after-major-upgrade) |
| Treasury → exchange during a pump | 🟢 No direct send from `0x341f…` to an exchange found |
| Treasury-funded wallet → exchange during a pump | 🔴 **Yes:** 67.6M SUI into Binance on 37 pump days in 12 months via `0x7f3b…`/`0xbe90…`/`0x7f66…` → `0x457f…`. [21 Aug](https://suiscan.xyz/mainnet/tx/HAVg1gBoF9Dt2EgSZ93kGCdWSMzvjZFGa7PEGiHhnqpG) · [22 Sep](https://suiscan.xyz/mainnet/tx/7KdCv7LyG136NvvcHJN3pxCMFCrrRTmtBpBQ7YD6sQfg) |
| Live mint path | 🟢 No: fixed 10B supply |
| Undisclosed allocation | 🔴 52.2% "after 2030" |

## 📚 Sources

- [Tier A] Sui GraphQL (`graphql.mainnet.sui.io`): balances, `StakedSui` objects, SENT transactions with balance changes for `0x341f…`, `0x7f3b…`, `0xbe90…`, `0x457f…`, `0x7f66…`, `0x51f8…`, `0xc6ff…` and 20 funded wallets; `coinMetadata`; epoch 1313; read 16 Nov 2026 MST
- [Tier B] Explorer labels: [Suiscan "Binance 1"](https://suiscan.xyz/mainnet/account/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd/portfolio) · [tide "Binance Hot Wallet 1"](https://tide.ad/address/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd)
- [Tier B] [Coincu: foundation transfers](https://coincu.com/news/sui-foundation-token-transfers-draw-exchange) · [Cointelegraph via TradingView: foundation denial, 27 Jun 2023](https://www.tradingview.com/news/cointelegraph:8ed5311c3094b:0-sui-foundation-denies-it-sold-locked-staking-rewards-on-binance/)
- [Tier A] [Sui postmortem, May 2026](https://www.sui.io/blog/sui-mainnet-halts-resolved-after-major-upgrade) · [Sui Monthly Feb 2026](https://www.sui.io/blog/sui-monthly-february-2026) · [Canary SUIS](https://canaryetfs.com/suis/)
- [Tier B] [Blockworks unlocks](https://app.blockworks.com/projects/sui/token-unlocks) · [CoinGlass vesting](https://www.coinglass.com/currencies/SUI/vesting) · [CoinDesk](https://www.coindesk.com/tech/2026/06/01/three-sui-mainnet-halts-in-48-hours-traced-to-an-upgrade-bug-by-developers)
- [Tier A] DefiLlama Sui fees/revenue/TVL; CoinGecko `sui` (16 Nov 2026 5:26 AM MST) and its 365-day closes for every pump test
- [Unverified] owners of `0x7f3b…`, `0xbe90…`, `0x7f66…`, the 13 single-stake wallets and the 5.22B post-2030 allocation

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Foundation `0x341f…` → `0x7f3b…` 310,595,908 SUI (16 Jun 2023) | [tx](https://suiscan.xyz/mainnet/tx/FdvGyjbAUUxwqHi1TzyoNWvSWocBSD6BhewNzi9Ssiq1) · [0x341f](https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1) | A chain · owner B ×2 | 16 Nov 2026 |
| `0x341f…` holds 1.652B SUI staked | [account](https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1) | A | 16 Nov 2026 |
| `0x341f…` → `0x7f66…` 16.3M (18 Mar 2026) | [tx](https://suiscan.xyz/mainnet/tx/EvjjwGD6y4zJN9j57mvgiDTQ14Fk8Lujr9VMuNSyz9By) | A | 16 Nov 2026 |
| 7 Jan 2026 pump day: `0x7f3b…` → `0xbe90…` → `0x7f66…` 5M | [in](https://suiscan.xyz/mainnet/tx/Zhmd5wC9BC5ugKW5yJtLDCs1Fma81U8qK2C4pnMkUZp) · [out](https://suiscan.xyz/mainnet/tx/64W7VPF7gAP532cV2MAy8LumaJGWuNMziLiuqdxVv4jb) | A | 16 Nov 2026 |
| 21 Aug 2026 pump day: 12.39M into Binance via `0x457f…` | [0xbe90→0x457f](https://suiscan.xyz/mainnet/tx/7PVDC5bPZiA1kq29GHDfLsWaPJm9Te6ngBTmTXeDS99t) · [0x457f→Binance](https://suiscan.xyz/mainnet/tx/HAVg1gBoF9Dt2EgSZ93kGCdWSMzvjZFGa7PEGiHhnqpG) | A + B labels | 16 Nov 2026 |
| 21–22 Sep 2026 pump days: 19.6M via `0x7f66…`, then Binance | [21 Sep](https://suiscan.xyz/mainnet/tx/7c8YheAtCrLEefm1NuDfWupEB6jk3Tkh78WgZoUGzTSX) · [22 Sep](https://suiscan.xyz/mainnet/tx/2n5pWep6Ce3R1NrJpiMTjL6H6KGP8opecV4RM7ehMAnY) · [→ 0x457f](https://suiscan.xyz/mainnet/tx/CiuBqoQ3Xhn9PL42o6PFhsc3BDZArgqXNk5FMy8yRWJP) · [→ Binance](https://suiscan.xyz/mainnet/tx/7KdCv7LyG136NvvcHJN3pxCMFCrrRTmtBpBQ7YD6sQfg) | A + B | 16 Nov 2026 |
| `0x9350…` is Binance | [Suiscan](https://suiscan.xyz/mainnet/account/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd/portfolio) · [tide](https://tide.ad/address/0x935029ca5219502a47ac9b69f556ccf6e2198b5e7815cf50f68846f723739cbd) | B ×2 | 16 Nov 2026 |
| Single-stake wallets funded Jan–Feb 2026 (e.g. 40M) | [tx](https://suiscan.xyz/mainnet/tx/7p11PpgeAwi2DrGdyXoxenZongNvdX1Q8HkL31UjX9cL) · [0x0345](https://suiscan.xyz/mainnet/account/0x0345cc00a2e6eeda03e54cf3c93f005d2b05f0790826c7507c6c3e366de8ccd4) | A | 16 Nov 2026 |
| Revenue $617,748 / 1y | [DefiLlama](https://defillama.com/chain/Sui) | A | 16 Nov 2026 |
| Three halts on 28–29 May 2026 | [postmortem](https://www.sui.io/blog/sui-mainnet-halts-resolved-after-major-upgrade) | A | 16 Nov 2026 |
| Three US ETFs, Feb 2026 | [Sui Monthly](https://www.sui.io/blog/sui-monthly-february-2026) · [Canary](https://canaryetfs.com/suis/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Labels for the unlabelled SUI wallets** (the maintainer's `arkham/sui_addresses.csv` list: `0x341f…`, `0x7f3b…`, `0xbe90…`, `0x7f66…`, `0x457f…`, `0x51f8…`, `0xc6ff…`, `0x3bd2…`) | **Not covered by Arkham:** Arkham does not support Sui (checked 16 Nov 2026 ~6:53 AM MST; the address page fails to load). Use Suiscan / SuiVision labels, or ask the Sui Foundation and Mysten Labs to publish their wallets | Free |
| 2 | **Is the 2023 "partner lock-up" still the explanation in 2026?** | Ask the Sui Foundation which entity controls `0x7f3b…`/`0x7f66…` and why it funded `0x7f66…` on 18 Mar 2026 | Free |
| 3 | **Who gets the 5.22B post-2030 SUI?** | Read the official token release schedule on sui.io and any foundation reports | Free |
| 4 | **Beneficiaries of the 13 single-stake wallets (~414M)** | Track `StakedSui` withdrawals from those wallets monthly | Free |
| 5 | **Pre-Nov-2025 pump-day flows** | Extend the GraphQL trace before Nov 2025 using Coinbase SUI-USD closes | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
