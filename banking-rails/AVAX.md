---
ticker: AVAX
name: Avalanche
chain: avalanche
contract: "native (P-, X- and C-Chain); C-Chain is EVM chain id 43114"
overall_score: 5.5
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 9
  product_development: 8
  adoption_customers: 7
  security_audits: 7
  regulatory: 8
  catalysts: 6
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  foundation_pump_day_exchange_send: open_unresolved
  foundation_wallet_roster_published: no
  nyse_settlement_launch: pending_regulatory_approval
price_usd: 7.31
price_source: "CoinGecko avalanche-2, 15 Nov 2026 6:45 AM MST"
chain_read_height: 100394651
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### AVAX · Overall grade **5.5 / 10 · ❌ FAIL**

**Summary:** A busy, deep, well-built network that the SEC now calls a digital commodity, and every fee is burned. But fees come to only ~$2.65M a year (about 0.08% of market cap), the Foundation does not publish its wallets or holdings, and a Foundation-labelled wallet sent 320,000 AVAX to Coinbase Prime on a +56% pump day with no disclosure. Fails the revenue gate.

**🚨 Top warning:** On the **21 Sep 2026 pump day (+55.8%)**, explorer-labelled "Avalanche Foundation: Wallet 1" [`0x76bD…0fC5`](https://snowtrace.io/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5) sent **320,000 AVAX into a Coinbase Prime deposit address** [`0x712b…800f`](https://snowtrace.io/address/0x712bba035b9775764aba04d1c86b48edef90800f), swept to Coinbase Prime's hot wallet 95 seconds later. Undisclosed. Check: [deposit tx](https://snowtrace.io/tx/0x30b40fa6280c72991f9fc8a7bc8b75750398fbe8d723a664c8cbc46e8daf8ec5) · [sweep tx](https://snowtrace.io/tx/0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b) · [Arkham “Coinbase Prime Deposit”](https://intel.arkm.com/explorer/address/0x712bba035b9775764aba04d1c86b48edef90800f) · [Arkham “Coinbase Prime: Hot Wallet”](https://intel.arkm.com/explorer/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1). (1 of 21 forwards, in line with chance; Wallet 1's Foundation label rests on one source.)

**Sections passed: 7 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 AVAX · Avalanche · 5.5 / 10 · ❌ FAIL

> **One line:** A busy, deep, well-built network that the SEC now calls a digital commodity, and every fee is burned. But fees come to only ~$2.65M a year (about 0.08% of market cap), the Foundation does not publish its wallets or holdings, and a Foundation-labelled wallet sent 320,000 AVAX to Coinbase Prime on a +56% pump day with no disclosure. Fails the revenue gate.

ℹ️ **Adapted for a layer-1.** "Revenue" = fees users pay and the part burned for all holders. "Foundation" = Avalanche (BVI), Inc. ("the Foundation") plus Ava Labs, the main developer. "Holdings / Selling" = Foundation allocation and the Foundation-labelled wallets we can see, checked against pump days.

🔎 **The old draft's "Under Investigation" flag, resolved as far as public data allows:** the flag came from one transfer: 320,000 AVAX from the explorer-labelled "Avalanche Foundation: Wallet 1" to a Coinbase Prime hot wallet on 21 Sep 2026, a +55.8% pump day. This pass re-read it on-chain. It is real. It is also **1 of 21** identical forwards through the same hop since Sep 2024. With 5.3% of days being pump days, chance alone predicts about 1.1 of 21 to land on one. No sale can be seen, and the Foundation has disclosed nothing. **Arkham check (15 Nov 2026):** the hop [`0x712b…`](https://snowtrace.io/address/0x712bba035b9775764aba04d1c86b48edef90800f) ([Arkham](https://intel.arkm.com/explorer/address/0x712bba035b9775764aba04d1c86b48edef90800f)) is a Coinbase Prime **deposit address**, and the destination is Coinbase Prime's hot wallet (now two independent labels), so the 320k was credited to a Coinbase Prime account. Arkham does **not** tie Wallet 1 to the Foundation, so that attribution still rests on one explorer label. **Status: unresolved, downgraded to Watch.** Scored as a fail on Selling (4/10), but not a hard-gate fail. Details in 📉 and in the open items at the end.

| 📊 Market (CoinGecko, 15 Nov 2026 6:45 AM MST) | 🔗 On-chain (api.avax.network, C-Chain block 100,394,651 · P-Chain height 25,873,296) |
|---|---|
| **Price** $7.31 | **Asset** native AVAX (no token contract) |
| **24h / 7d / 30d** 🔴 −8.1% / −10.5% / −28.7% | **Minted so far (P-Chain `getCurrentSupply`)** 476,590,179 of 720,000,000 cap (66.2%) |
| **Market cap** $3.266B · **FDV** $3.448B | **Burned on C-Chain** (burn address [`0x0100…0000`](https://snowtrace.io/address/0x0100000000000000000000000000000000000000)) 5,150,034 AVAX |
| **24h volume** $401.5M | **Staked (P-Chain `getTotalStake`)** 217,019,580 AVAX · **605** current validators |
| **ATH** $144.96 (21 Nov 2021) · now **−95%** | **Circulating (CoinGecko)** 446.44M · **total** 471.44M (= minted − C-Chain burn) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees paid by users | $24,483 | [Tier A] DefiLlama `avalanche` fees, 15 Nov 2026 |
| 7-day fees | $128,997 | [Tier A] DefiLlama |
| 30-day fees | $355,457 | [Tier A] DefiLlama |
| 12-month fees | **$2,650,211** | [Tier A] DefiLlama |
| All-time fees | $92,545,296 | [Tier A] DefiLlama |
| Where fees go | **100% burned.** "Fees are burned, this includes all fees from the X, C, P-chain, and L1s that utilize AVAX as its gas token" | [Tier A] [Avalanche Tokenomics FAQ](https://support.avax.network/en/articles/6912428-tokenomics-faq) |
| All-time C-Chain burn | 5,150,034 AVAX at `0x0100000000000000000000000000000000000000` (≈ $37.6M at today's price) | [Tier A] C-Chain `eth_getBalance` |
| Validator rewards | Newly **minted** on the P-Chain, not paid from fees | [Tier A] Tokenomics FAQ |
| 12-month fees ÷ market cap | ≈ **0.08%** | Calculated |

**What it means:** The burn is real and reaches every holder, but $2.65M a year is small for a $3.3B asset, and validators are paid with new coins, not fees. The NYSE settlement chain (see 🤝) runs on its own dedicated chain, so it is not C-Chain fee revenue today.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Foundation entity | **Avalanche (BVI), Inc.**, "a British Virgin Islands company (the 'Foundation')" | [Tier A] AVAT 8-K, SEC accession 0001104659-26-111940 |
| Foundation directors / officers | **Not found.** No published board or officer list | Not found |
| Foundation wallet roster | **Not published.** Wallet attributions come only from explorer labels (Routescan "Avalanche Foundation: Wallet 1 / Wallet 3"). Arkham has **no entity** for either wallet (only "first funder" tags), so there is still no second label | [Tier A] absence on avalanche.com; labels [Unverified] · [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST (signed-in account) |
| Standing permission to trade | Avalanche and associated parties "may give, receive, lend, borrow, purchase, and sell AVAX tokens" privately, in open markets and via DeFi | [Tier A] [avalanche.com/legal/important-notice](https://www.avalanche.com/legal/important-notice) |
| Main developer | Ava Labs (GitHub org `ava-labs`) | [Tier A] GitHub |
| Ava Labs leadership | John Nahas, chief business officer, quoted on the NYSE deal | [Tier B] CoinDesk 9 Nov 2026 (one outlet) |
| Ava Labs founder / CEO | Emin Gün Sirer | [Unverified] not checked against a primary record this pass |
| Related public company | Avalanche Treasury Corp. (Nasdaq: AVAT, CIK 0002092446, Delaware; CEO Gerald Bartholomew Smith signed the 8-K) | [Tier A] SEC EDGAR |
| Foundation ↔ AVAT ties | Oct 2025 token sale to AVAT at a 60% discount for $50M + 3,000,000 AVAT shares; Foundation board-designation right and right of first refusal on AVAT's AVAX sales | [Unverified] one Tier B outlet citing AVAT's 10-Q |

**What it means:** We know the Foundation's legal shell from an SEC filing, and the developer is active and public. We do not know who runs the Foundation, which wallets it owns, or how much AVAX it holds.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Holder | AVAX | Notes | Source |
|---|---:|---|---|
| Foundation allocation (genesis) | 9.26% of 720M ≈ 66.7M | Still vesting: **1.67M AVAX per quarter** | [Tier B] DefiLlama unlocks + other unlock trackers |
| Team / strategic partners / community endowment | 10% / 5% / 7% of 720M | Reported fully unlocked | [Tier B] unlock trackers |
| Foundation's **current** total holdings | **Not found** | No disclosure, no roster | Not found |
| "Avalanche Foundation: Wallet 1" [`0x76bDB80A6D0bC70912491BE97b38625f76de0fC5`](https://snowtrace.io/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5) ([Arkham](https://intel.arkm.com/explorer/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5)) | **90,223** (live) | Also holds **5,649,915 USDC** on Avalanche (Arkham shows 6.01M USDC across chains). Explorer label only; Arkham has no entity for it | [Tier A] balances (C-Chain block ~100.41M, 15 Nov ~10:45 AM MST) · label [Unverified] |
| "Avalanche Foundation: Wallet 3" [`0x5E12fc70B97902AC19B9cB87F2aC5a8593769779`](https://snowtrace.io/address/0x5E12fc70B97902AC19B9cB87F2aC5a8593769779) ([Arkham](https://intel.arkm.com/explorer/address/0x5E12fc70B97902AC19B9cB87F2aC5a8593769779)) | 1.0 (live) | Explorer label only; Arkham has no entity. On **18 Jun 2025** it sent 66,661.88 AVAX and 1,181,184.28 USDC (USDC [tx `0xe337f88e…`](https://snowtrace.io/tx/0xe337f88e374eceeb90bd8d6539f3c1bebf25b6b2d431516fe957d058c39cb601); AVAX tx hash not re-pulled) to [`0x663d966f…`](https://snowtrace.io/address/0x663d966f03d66cf3fa3e007f34c8662ec4fda7c3), which Arkham labels a **Binance deposit** ([Arkham](https://intel.arkm.com/explorer/address/0x663d966f03d66cf3fa3e007f34c8662ec4fda7c3)) (before this report's 12-month pump window) | [Tier A] balance + Routescan txs · Binance label [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST (one label) · Foundation label [Unverified] |
| Unlabelled feeder [`0x87dda0daba3f7b309a4fe99f406a074811d5a3bf`](https://snowtrace.io/address/0x87dda0daba3f7b309a4fe99f406a074811d5a3bf) ([Arkham](https://intel.arkm.com/explorer/address/0x87dda0daba3f7b309a4fe99f406a074811d5a3bf)) | 16,876 (live) | Sent 1.6M AVAX into the **same Coinbase Prime deposit address** as Wallet 1 in May–Aug 2026, and 2,249,992 AVAX to [`0xc1145611…`](https://snowtrace.io/address/0xc1145611702a30ccdaa47ba4286cf317a2757f46) (largest: 999,998 on 11 Aug 2026, [tx `0xf35f5d4f…`](https://snowtrace.io/tx/0xf35f5d4fb67b13dc7a2814c1aa46c6045ea9493bcb7088b900cc79c6c44f8753)). Last sent 33,000 to `0xc9ad9d2a…` on 2 Nov 2026. Arkham: no entity | [Tier A] Routescan · Foundation link [Unverified] |
| Locked AVAX bought from AVAT, 23 Sep 2026 | 2,082,371.61 | Foundation **bought** for $15,000,000 (≈ $7.20 each) | [Tier A] AVAT 8-K |
| AVAT shares held by Foundation | 3,000,000 | From the Oct 2025 token-sale agreement | [Unverified] |

**What it means:** The Foundation clearly still holds and receives AVAX (a quarterly unlock plus a $15M purchase in September), but there is no number to check. Arkham does not add one: it has no Avalanche Foundation entity. "Not proven" scores as a fail.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **19 of 360 days** were pump days (5.3%): 27–29 Nov 2025; 4–6 Jan 2026; 21–25 Aug; 8 Sep; 19–24 Sep (peak **+55.8% on 21 Sep**); 30 Sep. Last pump day 30 Sep 2026 (+12.1%).

### A. The flagged path, re-read on-chain today

| Step | Time (UTC) | From → To | AVAX | Tx |
|---|---|---|---:|---|
| Principal | 21 Sep 2026 14:27:28 | Wallet 1 [`0x76bD…0fC5`](https://snowtrace.io/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5) → Coinbase Prime deposit address [`0x712bba035b9775764aba04d1c86b48edef90800f`](https://snowtrace.io/address/0x712bba035b9775764aba04d1c86b48edef90800f) | **320,000** | [tx `0x30b40fa6280c72991f9fc8a7bc8b75750398fbe8d723a664c8cbc46e8daf8ec5`](https://snowtrace.io/tx/0x30b40fa6280c72991f9fc8a7bc8b75750398fbe8d723a664c8cbc46e8daf8ec5) (block 95,838,455) |
| Sweep (95 s later) | 21 Sep 2026 14:29:03 | deposit address → "Coinbase Prime: Hot Wallet" [`0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1`](https://snowtrace.io/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1) | **320,001.9999** | [tx `0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b`](https://snowtrace.io/tx/0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b) (block 95,838,544) |
| Same path, a month later | 21 Oct 2026 | Wallet 1 → deposit address → Prime hot wallet | 1,903 / 1,904 | [tx `0x67fca5e5…`](https://snowtrace.io/tx/0x67fca5e5404bc7cad45d3ac6b0627b2f2ea80c13fb4ca902865386c75f8c4837) · [tx `0x566cc9f4…`](https://snowtrace.io/tx/0x566cc9f4ab08dbf6183a099af2af57c65e6b087e56c1007ef9ce3d741a6bfeef) |

Notional on 21 Sep ≈ $3.6M. The deposit address holds 0.00004 AVAX today.

**Labels on this path (Arkham, 15 Nov 2026):**

| Address | Arkham label | Second label? | Status |
|---|---|---|---|
| [`0x1D67bd45…6ED1`](https://snowtrace.io/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1) ([Arkham](https://intel.arkm.com/explorer/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1)) | "Coinbase Prime: Hot Wallet" (exchange, OTC, hot wallet) | Yes: Routescan uses the same name | ✅ Two independent Tier B labels → **confirmed Coinbase Prime** |
| [`0x712bba03…800f`](https://snowtrace.io/address/0x712bba035b9775764aba04d1c86b48edef90800f) ([Arkham](https://intel.arkm.com/explorer/address/0x712bba035b9775764aba04d1c86b48edef90800f)) | "Coinbase Prime Deposit" (deposit address) | No; but on-chain it forwards everything to the Prime hot wallet within minutes and keeps only dust, which is how exchange deposit addresses behave | Tier B + [Tier A] behaviour |
| Wallet 1 `0x76bD…0fC5` | **No entity**; tags only ("Avalanche First Funder" and similar) | No | Foundation ownership still [Unverified] (Routescan only) |

- Exchange deposit addresses are normally assigned to **one customer account**. The 320k therefore landed in a Coinbase Prime account at 14:27 UTC on 21 Sep. Whether it was then sold, held in custody or posted as collateral happens inside Coinbase and cannot be seen on-chain.
- Wallet 1 and the feeder `0x87dda0da…` both pay into this same deposit address, which suggests they credit the same Prime account. That is an inference from how deposit addresses work, not a label [Unverified].

### B. Is it a one-off? No: 21 forwards since Sep 2024

All sweeps from the Coinbase Prime deposit address to the Prime hot wallet ([Tier A] Routescan txlist, read 15 Nov 2026): **21 forwards, 3,064,943 AVAX** between 30 Sep 2024 and 21 Oct 2026. The 2026 ones, with the 5-day price move:

| Date | AVAX to Prime wallet | Fed by | 5-day move | Sweep tx |
|---|---:|---|---:|---|
| 4 Mar 2026 | 2,128 | Wallet 1 | −1.3% | [sweep](https://snowtrace.io/tx/0x10030f0056f4514891904bf7ed3f6d951d3af66a43b4d66d542efdd6c018cceb) |
| 10 Mar 2026 | 2,500 | Wallet 1 | −2.4% | [sweep](https://snowtrace.io/tx/0x482163d964f9482e0ceadbb185c75f80da6877969a6c044930f37200c60527c8) |
| 25 Mar 2026 | 250,002 | (internal) | +1.7% | [sweep](https://snowtrace.io/tx/0x70212f0b9c0e62291e09b4fae0aea08b7e447aeebfbcb03d4c442e703bef83db) |
| 20 May 2026 | 400,010 | `0x87dda0da…` | −8.1% | [sweep](https://snowtrace.io/tx/0x751860f249b0c3fee058fd3731338dbe926bb82e40c3039e729aafb05fe2a451) |
| 26 May 2026 | 200,000 | `0x87dda0da…` | +0.1% | [sweep](https://snowtrace.io/tx/0xfbbf139acfae4c7fb27c58e6ce90add89ba17fa152d16061bc124f61dd81190f) |
| 23 Jun 2026 | 350,007 | `0x87dda0da…` | −7.8% | [sweep](https://snowtrace.io/tx/0x8d57260cd02a2eaf90916752edaf1a77080aaf7d097d08c1b22a3b302cf2b63d) |
| 3 Aug 2026 | **650,000** | `0x87dda0da…` | −0.4% | [sweep](https://snowtrace.io/tx/0xcc46420ff2aa94c34e1815426927914938469699b46a6af83623cb14aa196177) |
| **21 Sep 2026** | **320,002** | **Wallet 1** | **+55.8% 🚩** | [sweep](https://snowtrace.io/tx/0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b) |
| 21 Oct 2026 | 1,904 | Wallet 1 | −2.9% | [sweep](https://snowtrace.io/tx/0x566cc9f4ab08dbf6183a099af2af57c65e6b087e56c1007ef9ce3d741a6bfeef) |

- **Chance check:** 5.3% of days are pump days. 21 forwards × 5.3% ≈ **1.1 expected by luck**. Observed: **1**. The timing looks like routine operations, not a pattern of selling into rises.
- **Two-way relationship:** the Prime-labelled wallet has also sent AVAX back to Wallet 1 (e.g. 79,176.62 on 22 Jul 2026, [tx `0xdac48748…`](https://snowtrace.io/tx/0xdac48748019eb2623a642d517bc1d68036e552d931dbc27d387ea0d733dbd2fe); 35,360.28 on 17 Feb 2026, [tx `0x8f67ae40…`](https://snowtrace.io/tx/0x8f67ae403d381bfcb00fbf0abd0edecd67a343d4b67589cc53ca47ecb64ed68e)) [Tier A, carried from the 10 Nov deep dive tx list].
- **A round trip with Galaxy Digital's OTC desk:** Wallet 1 sent 400,000 to [`0xff504ac5…`](https://snowtrace.io/address/0xff504ac5be886fca7184ab26b0bc6c49145240b0) on 4 Aug 2026 (20:25 UTC, [tx `0xf7a515b9…`](https://snowtrace.io/tx/0xf7a515b9660898cb8db8ddcb25bb0275708b41386853509bd6d693d81edb3340)), which forwarded it to [`0x46f34c24a7ba7a2ac6dd76c3f09b32d41c144d08`](https://snowtrace.io/address/0x46f34c24a7ba7a2ac6dd76c3f09b32d41c144d08) on 5 Aug ([tx `0x77b991f3…`](https://snowtrace.io/tx/0x77b991f30a006f348d157a0010a6e2f003a92e7cea6d758bbdf9487ce1f5e94d)). On 8 Sep 2026 that wallet sent **400,987** back to Wallet 1 ([tx `0xa22f8664…`](https://snowtrace.io/tx/0xa22f8664f775cabd98211576df7ebc517d3145dcd5f8dc69e6510b72162da84a)), after receiving 300,987 from [`0x15abb66b…`](https://snowtrace.io/address/0x15abb66ba754f05cbc0165a64a11cded1543de48) on 4 Sep ([tx `0xd888be58…`](https://snowtrace.io/tx/0xd888be5878ba87dcdebcf4296a2c82719ada4402ca4a0b387eabcb22699599dd)). Arkham labels `0xff504ac5…` a **Galaxy Digital deposit** address ([Arkham](https://intel.arkm.com/explorer/address/0xff504ac5be886fca7184ab26b0bc6c49145240b0)) and both `0x46f34c24…` ([Arkham](https://intel.arkm.com/explorer/address/0x46f34c24a7ba7a2ac6dd76c3f09b32d41c144d08)) and `0x15abb66b…` ([Arkham](https://intel.arkm.com/explorer/address/0x15abb66ba754f05cbc0165a64a11cded1543de48)) **Galaxy Digital: OTC** wallets ([Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST, one label each). So the 400k went to Galaxy Digital and came back 35 days later with 987 AVAX (~0.25%) extra. That fits a loan or OTC arrangement with Galaxy, not a sale. Purpose [Unverified]; Galaxy labels [Unverified] (one source). 8 Sep was a pump day (+12.3%), but this was an inflow to Wallet 1, not a send.
- **Dollars out of Coinbase, then to Circle (new this pass):** after the 21 Sep deposit, Wallet 1 received **1,999,985 USDC on 7 Oct 2026** ([tx `0x43333b10…`](https://snowtrace.io/tx/0x43333b10f35536b09f43ea62ec41f4488e62981752be5f127922ac37f4c40062)) and **4,000,000 USDC on 2 Nov 2026** ([tx `0x34f3e283…`](https://snowtrace.io/tx/0x34f3e2839cab952e89ee9968d0807e6f2b85458705ba4d3c0b111196a8f37213)) from [`0x7ed53f6e…`](https://snowtrace.io/address/0x7ed53f6e3de6b2b4156fa8e618506e60d8e65843) (Arkham shows $4M withdrawn to Wallet 1 from Coinbase hot wallets, matching the 2 Nov transfer). On **22 Oct 2026** it sent **4,600,000 USDC** to [`0xe9ae1b65…`](https://snowtrace.io/address/0xe9ae1b65a48b3a6473eb126b5f5060f172455645) ([tx `0x9b2a574a…`](https://snowtrace.io/tx/0x9b2a574a6e57841493073e2466be30fbdcef6dde669abdcb373e08109d993b62)), which Arkham labels a Circle deposit ([Arkham](https://intel.arkm.com/explorer/address/0xe9ae1b65a48b3a6473eb126b5f5060f172455645)) ([Tier A] Routescan USDC transfers; labels [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST). Arkham's Circle total is ~$5M; the other ~$0.4M was not found on Avalanche and may be on another chain. Dollars coming out of Coinbase after AVAX went in **fits** a sale, but USDC can come out of Coinbase for many reasons, so it does **not prove** the 320k was sold.
- **Other exchange deposits near these wallets:** [`0xc9ad9d2a…`](https://snowtrace.io/address/0xc9ad9d2ab2d25b4c58eeea36a7e44a7c35d7a825) (funded by the feeder, the Prime hot wallet and `0xc1145611…`) sent **204,613.20 AVAX** to [`0xff1a817f…`](https://snowtrace.io/address/0xff1a817fc120370762497aed61aef67732708a2c), an Arkham-labelled **Coinbase deposit** ([Arkham](https://intel.arkm.com/explorer/address/0xff1a817fc120370762497aed61aef67732708a2c)), on **2 Nov 2026** ([tx `0xe77b8284…`](https://snowtrace.io/tx/0xe77b828488f48aff36f1d911faa17198d4de545fc93880fe33a6063e262cdb88)) (−2.9% five-day move, not a pump day). No Foundation link for `0xc9ad9d2a…` is known.
- **Lookalike dust:** addresses starting `0x76bde312…` / `0x76bde434…` keep sending 0-value transfers to these wallets. That is address-poisoning spam, not Foundation activity.

### C. The same week, the Foundation was a buyer

| Date | Event | Source |
|---|---|---|
| 23 Sep 2026 | Foundation **bought** 2,082,371.607744 locked AVAX from AVAT for **$15,000,000** in three tranches | [Tier A] AVAT 8-K, filed 29 Sep 2026 |
| Match to the 320k? | **No.** Opposite direction, ~6.5× the size, locked vs liquid | Calculated |

### D. What a fail or a pass would need

| Would confirm a selling FAIL (≤3, hard gate) | Would clear to PASS |
|---|---|
| Proof the 320k was sold (a Foundation or AVAT disclosure, or a court or SEC record), or a second Foundation-wallet exchange deposit on a pump day with no operations explanation | A Foundation or AVAT statement mapping the 320k (custody, collateral, OTC settlement), or the coins returning to Foundation wallets |

**What it means:** One undisclosed send to an exchange on a big pump day by a Foundation-labelled wallet. Arkham confirms the coins went into a Coinbase Prime account and shows dollars later coming out of Coinbase to the same wallet. That fits a sale but does not prove one, and Arkham does not confirm the wallet is the Foundation's. The timing is consistent with chance, the Foundation was a net buyer that week, and the August 400k was a Galaxy Digital round trip, not a sale. It is still undisclosed, and the Foundation publishes no wallets, so this stays a fail at 4/10 (score unchanged). It is not a proven dump.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Hard cap | 720,000,000 AVAX | [Tier A] Tokenomics FAQ |
| Genesis | 360,000,000 minted at launch; the rest is minted as staking rewards | [Tier A] Tokenomics FAQ |
| Minted to date | 476,590,179 (P-Chain upper bound, height 25,873,296) | [Tier A] `platform.getCurrentSupply` |
| C-Chain burn | 5,150,034 AVAX | [Tier A] |
| Net total | ≈ 471.44M (matches CoinGecko total supply) | Calculated / [Tier B] CoinGecko |
| Staked | 217.02M (45.5% of minted) | [Tier A] `platform.getTotalStake` |
| Reward rate | Falls as supply nears the cap | [Tier A] Tokenomics FAQ |
| Yearly new-coin issuance | **Not computed this pass** (needs a P-Chain supply read from a year ago) | Not found |
| Next unlock | **Foundation 1.67M AVAX** (0.37% of circulating). **24 Jan 2027** per DefiLlama; other trackers say **6 Feb 2027**, then quarterly through Nov 2027 | [Tier B] DefiLlama · date [Unverified] |
| Mint / freeze / admin key | None at protocol level. Supply changes need a network upgrade | [Tier A] |

**What it means:** The rules are clear and enforced by the protocol, and the burn offsets a little of the issuance. New-coin staking rewards still far exceed the burn.

## 💧 Liquidity & market · 9/10 · ✅ PASS

| Venue (CoinGecko tickers, 15 Nov 2026) | Pair | 24h volume | Bid depth to −2% |
|---|---|---:|---:|
| Binance | AVAX/USDT | $37.85M | $349k |
| KuCoin | AVAX/USDT | $22.15M | $187k |
| Coinbase Exchange | AVAX/USD | $12.52M | $507k |
| Bybit | AVAX/USDT | $11.05M | $84k |
| Gate | AVAX/USDT | $9.47M | $375k |
| OKX | AVAX/USDT | $9.30M | $201k |
| Upbit | AVAX/KRW | $9.19M | $70k |
| Kraken | AVAX/USD | $5.60M | $858k |
| **Major-venue USD/stable pairs, total −2% depth** | | | **≈ $3.40M** |

- Total 24h volume $401.5M (CoinGecko). No single venue has more than ~10% of the first 100 tickers.
- DeFi TVL on Avalanche: **$551.1M** ([Tier A] DefiLlama chains).

**What it means:** Deep, spread across many top-tier venues. A Foundation-sized sale of a few hundred thousand AVAX can be absorbed over a day.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

| Item | Detail | Source |
|---|---|---|
| Node client | `ava-labs/avalanchego`: last push 15 Nov 2026; **270 commits in 13 weeks**; releases v1.15.3 (5 Nov 2026), v1.15.2 (22 Oct), v1.15.1 (1 Oct) | [Tier A] GitHub API |
| Old repos | `coreth` is **archived** (EVM code now inside avalanchego); `subnet-evm` last pushed Dec 2025 | [Tier A] GitHub API |
| Avalanche L1s | Firms run their own chains (custom gas token allowed). Validators pay a small fee in AVAX, which is burned | [Tier A] build.avax.network docs (via old draft) · [Unverified] not reread this pass |
| C-Chain speed | ~1.0 s blocks, ~3.1 tx per block in a 400-block sample | [Tier A] RPC sample, calculated |

## 🤝 Adoption & customers · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| C-Chain activity | ≈ **265,000 tx/day** (sample of 400 blocks across the last ~10,000) | [Tier A] RPC, calculated |
| Stablecoins on Avalanche | **$772.3M** | [Tier A] DefiLlama stablecoins |
| DeFi TVL | $551.1M | [Tier A] DefiLlama |
| **NYSE** | NYSE / ICE picked Avalanche technology as the core ledger for clearing and settlement on a planned 24/7 tokenized-securities ATS. It runs on a **dedicated** Avalanche-based chain, not the public C-Chain, and **needs regulatory approval** | [Tier B ×2] CoinDesk 9 Nov 2026, Decrypt 11 Nov 2026 |
| NYSE terms | "Cost nothing" per Ava Labs; target launch Q4 2026 | [Unverified] one outlet |
| Zengo wallet | Added AVAX for 2M+ users (4 Nov 2026) | [Unverified] one outlet |
| NEC | Signed an exploratory MOU on biometric stablecoin payments (3 Nov 2026), no committed deployment | [Unverified] one outlet |
| AVAT | Public company holding ~15.3M AVAX (30 Jun 2026), staking it | [Unverified] secondary summary of AVAT 10-Q |

**What it means:** Real usage and a marquee institutional win. Most of the institutional work runs on private L1s, which pay AVAX only in small validator fees.

## 🛡️ Security & audits · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Protocol hack | None found in 2025–26 | [Tier A] absence of a post-mortem |
| C-Chain halts | None in 2026. An AvaCloud RPC / ICM relayer outage on 8–9 Sep 2026 did **not** stop the chain. Last reported chain halt 23 Feb 2024 | [Unverified] status trackers (one source each) |
| Validator set | 605 current primary-network validators; 217.02M AVAX staked | [Tier A] P-Chain |
| Admin keys | No protocol admin key; upgrades are node releases that validators adopt | [Tier A] |
| Foundation operational security | Foundation-labelled wallets are targeted by address-poisoning dust | [Tier A] tx history |

## ⚖️ Regulatory · 8/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| United States | SEC interpretive release **33-11412** (effective 23 Mar 2026) lists **Avalanche (AVAX)** as an example of a **digital commodity**, not a security | [Tier A] [sec.gov 33-11412](https://www.sec.gov/files/rules/interp/2026/33-11412.pdf) |
| EU MiCA white papers | Filed by third parties, not the Foundation: Crypto Risk Metrics GmbH via BaFin (21 Apr 2026, FFG S6JCBF70N); LCX AG via FMA Liechtenstein, for admission to trading (14 Apr 2025) | [Tier A] ESMA interim MiCA register (OTHER.csv) |
| Related public filer | AVAT files 8-K / 10-Q with the SEC | [Tier A] EDGAR |
| Enforcement / court | None found against the Foundation or Ava Labs this pass | [Unverified] no docket search this pass |

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| Q4 2026 (target) | NYSE tokenized-securities ATS on Avalanche technology, if approved | Adoption / credibility; little direct C-Chain fee |
| 24 Jan 2027 (DefiLlama) or 6 Feb 2027 | Foundation unlock, 1.67M AVAX | Supply ↑ 0.37% of float |
| May / Aug / Nov 2027 | Further quarterly Foundation unlocks | Supply ↑ |
| Open | Foundation or AVAT explanation of the 21 Sep 320k transfer | Would close or confirm the selling flag |
| 8–9 Dec 2026 | FOMC meeting | Macro |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack / exploit | 🟢 None | No protocol incident found |
| Foundation wallet sends to an exchange on a pump day, undisclosed | 🟡 **Open, unresolved** | 320k on 21 Sep 2026 (+55.8%) into a Coinbase Prime deposit address ([deposit tx](https://snowtrace.io/tx/0x30b40fa6280c72991f9fc8a7bc8b75750398fbe8d723a664c8cbc46e8daf8ec5) · [sweep tx](https://snowtrace.io/tx/0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b) · [Arkham label](https://intel.arkm.com/explorer/address/0x712bba035b9775764aba04d1c86b48edef90800f); Prime hot wallet confirmed by Routescan + Arkham); 1 of 21 forwards, in line with chance; Wallet 1's Foundation label still has one source |
| Foundation publishes wallets / holdings | 🔴 No | No roster, no holdings report |
| NYSE settlement goes live | 🟡 Pending regulatory approval | CoinDesk, Decrypt |

## 📚 Sources

- [Tier A] Avalanche public API `api.avax.network`: C-Chain `eth_getTransactionByHash`, `eth_getBalance`, `eth_getBlockByNumber` (block ~100,394,651); P-Chain `getCurrentSupply`, `getTotalStake`, `getCurrentValidators` (height 25,873,296); 15 Nov 2026 ~6:50 AM MST
- [Tier A] Routescan Etherscan-compatible API (chain 43114) txlists for Wallet 1, the Coinbase Prime deposit address `0x712bba03…`, `0x87dda0da…`, `0x46f34c24…`; re-read 15 Nov 2026 ~10:45 AM MST for Wallet 1 (AVAX + USDC transfers), Wallet 3 (AVAX + tokens), `0x87dda0da…`, `0xc9ad9d2a…`, `0xff504ac5…`; USDC `balanceOf` for Wallet 1 via C-Chain RPC
- [Tier B] Arkham Intelligence, read 15 Nov 2026 ~10:40 AM MST (signed-in account): entity pages and flows for Wallet 1, Wallet 3, `0x712bba03…` (Coinbase Prime Deposit), `0x1D67bd45…` (Coinbase Prime: Hot Wallet), `0x87dda0da…`, `0xff504ac5…` (Galaxy Digital Deposit), `0x46f34c24…` and `0x15abb66b…` (Galaxy Digital: OTC), `0xc9ad9d2a…`. Arkham shows relative ages only; dates above come from on-chain reads where amounts match
- [Tier A] Explorer pages used (Snowtrace): Wallet 1 [`0x76bD…`](https://snowtrace.io/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5) · Wallet 3 [`0x5E12…`](https://snowtrace.io/address/0x5E12fc70B97902AC19B9cB87F2aC5a8593769779) · feeder [`0x87dd…`](https://snowtrace.io/address/0x87dda0daba3f7b309a4fe99f406a074811d5a3bf) · Prime deposit [`0x712b…`](https://snowtrace.io/address/0x712bba035b9775764aba04d1c86b48edef90800f) · Prime hot wallet [`0x1D67…`](https://snowtrace.io/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1) · Galaxy [`0xff50…`](https://snowtrace.io/address/0xff504ac5be886fca7184ab26b0bc6c49145240b0) / [`0x46f3…`](https://snowtrace.io/address/0x46f34c24a7ba7a2ac6dd76c3f09b32d41c144d08) / [`0x15ab…`](https://snowtrace.io/address/0x15abb66ba754f05cbc0165a64a11cded1543de48) · [`0xc9ad…`](https://snowtrace.io/address/0xc9ad9d2ab2d25b4c58eeea36a7e44a7c35d7a825) · [`0xc114…`](https://snowtrace.io/address/0xc1145611702a30ccdaa47ba4286cf317a2757f46) · Coinbase deposit [`0xff1a…`](https://snowtrace.io/address/0xff1a817fc120370762497aed61aef67732708a2c) · Circle deposit [`0xe9ae…`](https://snowtrace.io/address/0xe9ae1b65a48b3a6473eb126b5f5060f172455645) · Binance deposit [`0x663d…`](https://snowtrace.io/address/0x663d966f03d66cf3fa3e007f34c8662ec4fda7c3)
- [Tier B] Arkham address pages used: [Wallet 1](https://intel.arkm.com/explorer/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5) · [Wallet 3](https://intel.arkm.com/explorer/address/0x5E12fc70B97902AC19B9cB87F2aC5a8593769779) · [0x712b…](https://intel.arkm.com/explorer/address/0x712bba035b9775764aba04d1c86b48edef90800f) · [0x1D67…](https://intel.arkm.com/explorer/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1) · [0x87dd…](https://intel.arkm.com/explorer/address/0x87dda0daba3f7b309a4fe99f406a074811d5a3bf) · [0xff50…](https://intel.arkm.com/explorer/address/0xff504ac5be886fca7184ab26b0bc6c49145240b0) · [0x46f3…](https://intel.arkm.com/explorer/address/0x46f34c24a7ba7a2ac6dd76c3f09b32d41c144d08) · [0x15ab…](https://intel.arkm.com/explorer/address/0x15abb66ba754f05cbc0165a64a11cded1543de48) · [0xc9ad…](https://intel.arkm.com/explorer/address/0xc9ad9d2ab2d25b4c58eeea36a7e44a7c35d7a825) · [0xff1a…](https://intel.arkm.com/explorer/address/0xff1a817fc120370762497aed61aef67732708a2c) · [0xe9ae…](https://intel.arkm.com/explorer/address/0xe9ae1b65a48b3a6473eb126b5f5060f172455645) · [0x663d…](https://intel.arkm.com/explorer/address/0x663d966f03d66cf3fa3e007f34c8662ec4fda7c3)
- [Tier A] DefiLlama fees (`avalanche`), chain TVL, stablecoins by chain, 15 Nov 2026
- [Tier A] CoinGecko `avalanche-2` market data, tickers with depth, and 365 daily closes, 15 Nov 2026 6:45 AM MST
- [Tier A] GitHub API: `ava-labs/avalanchego`, `coreth`, `subnet-evm`
- [Tier A] SEC: AVAT 8-K (accession 0001104659-26-111940); interpretive release 33-11412
- [Tier A] ESMA interim MiCA register, OTHER.csv
- [Tier A] [Avalanche Tokenomics FAQ](https://support.avax.network/en/articles/6912428-tokenomics-faq) · [Avalanche legal notice](https://www.avalanche.com/legal/important-notice)
- [Tier B] CoinDesk (9 Nov 2026), Decrypt (11 Nov 2026) on NYSE; DefiLlama unlocks page
- [Tier A] Prior deep dive, 10 Nov 2026 (`avax_deep_dive_2026-11-10`), principal transactions re-verified this pass
- [Unverified] Foundation labels for Wallet 1 / Wallet 3 (Routescan only; Arkham has no entity); Galaxy Digital, Binance, Coinbase and Circle deposit labels (Arkham only); Foundation ↔ AVAT agreement terms; Ava Labs CEO; Zengo, NEC, NYSE terms; unlock date; chain-halt history

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **Pump-day send:** Wallet 1 → Coinbase Prime deposit `0x712b…`, 320,000 AVAX, 21 Sep 2026 14:27 UTC (+55.8%) | [deposit tx](https://snowtrace.io/tx/0x30b40fa6280c72991f9fc8a7bc8b75750398fbe8d723a664c8cbc46e8daf8ec5) · [Wallet 1](https://snowtrace.io/address/0x76bDB80A6D0bC70912491BE97b38625f76de0fC5) · [Arkham “Coinbase Prime Deposit”](https://intel.arkm.com/explorer/address/0x712bba035b9775764aba04d1c86b48edef90800f) | A + B | 15 Nov 2026 ~10:45 AM MST |
| Swept to Coinbase Prime hot wallet 95 s later | [sweep tx](https://snowtrace.io/tx/0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b) · [Arkham “Coinbase Prime: Hot Wallet”](https://intel.arkm.com/explorer/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1) · [Snowtrace tag](https://snowtrace.io/address/0x1D67bd4503AD0639bEeb843890a6A90BD74E6ED1) | A + 2× B | 15 Nov 2026 |
| 21 forwards through the same deposit address since Sep 2024 (1 on a pump day) | [deposit address txs](https://snowtrace.io/address/0x712bba035b9775764aba04d1c86b48edef90800f) · 2026 sweeps: [4 Mar](https://snowtrace.io/tx/0x10030f0056f4514891904bf7ed3f6d951d3af66a43b4d66d542efdd6c018cceb) · [10 Mar](https://snowtrace.io/tx/0x482163d964f9482e0ceadbb185c75f80da6877969a6c044930f37200c60527c8) · [25 Mar](https://snowtrace.io/tx/0x70212f0b9c0e62291e09b4fae0aea08b7e447aeebfbcb03d4c442e703bef83db) · [20 May](https://snowtrace.io/tx/0x751860f249b0c3fee058fd3731338dbe926bb82e40c3039e729aafb05fe2a451) · [26 May](https://snowtrace.io/tx/0xfbbf139acfae4c7fb27c58e6ce90add89ba17fa152d16061bc124f61dd81190f) · [23 Jun](https://snowtrace.io/tx/0x8d57260cd02a2eaf90916752edaf1a77080aaf7d097d08c1b22a3b302cf2b63d) · [3 Aug](https://snowtrace.io/tx/0xcc46420ff2aa94c34e1815426927914938469699b46a6af83623cb14aa196177) · [21 Sep](https://snowtrace.io/tx/0x05addc56e6314bb3c99a0a507556d5ee39b6724f09289f870bd583052da9554b) · [21 Oct](https://snowtrace.io/tx/0x566cc9f4ab08dbf6183a099af2af57c65e6b087e56c1007ef9ce3d741a6bfeef) | A | 15 Nov 2026 |
| Feeder `0x87dd…` put 1.6M AVAX into the same Prime deposit address (May–Aug 2026) | [feeder](https://snowtrace.io/address/0x87dda0daba3f7b309a4fe99f406a074811d5a3bf) · [3 Aug 649,998](https://snowtrace.io/tx/0x5e0099ed64caa99246b1481f3586132917959d5f7a08c3ad5983fc85239757bc) · [Arkham](https://intel.arkm.com/explorer/address/0x87dda0daba3f7b309a4fe99f406a074811d5a3bf) | A | 15 Nov 2026 |
| 400k AVAX round trip with Galaxy Digital OTC (4 Aug out, 8 Sep back +987) | [out](https://snowtrace.io/tx/0xf7a515b9660898cb8db8ddcb25bb0275708b41386853509bd6d693d81edb3340) · [forward](https://snowtrace.io/tx/0x77b991f30a006f348d157a0010a6e2f003a92e7cea6d758bbdf9487ce1f5e94d) · [back](https://snowtrace.io/tx/0xa22f8664f775cabd98211576df7ebc517d3145dcd5f8dc69e6510b72162da84a) · [Arkham Galaxy deposit](https://intel.arkm.com/explorer/address/0xff504ac5be886fca7184ab26b0bc6c49145240b0) · [Arkham Galaxy OTC](https://intel.arkm.com/explorer/address/0x46f34c24a7ba7a2ac6dd76c3f09b32d41c144d08) | A + one B | 15 Nov 2026 |
| USDC out of Coinbase to Wallet 1 (2.0M + 4.0M), then 4.6M USDC to a Circle deposit | [7 Oct](https://snowtrace.io/tx/0x43333b10f35536b09f43ea62ec41f4488e62981752be5f127922ac37f4c40062) · [2 Nov](https://snowtrace.io/tx/0x34f3e2839cab952e89ee9968d0807e6f2b85458705ba4d3c0b111196a8f37213) · [22 Oct → Circle](https://snowtrace.io/tx/0x9b2a574a6e57841493073e2466be30fbdcef6dde669abdcb373e08109d993b62) · [Arkham Circle label](https://intel.arkm.com/explorer/address/0xe9ae1b65a48b3a6473eb126b5f5060f172455645) | A + one B | 15 Nov 2026 |
| Wallet 3 → Binance deposit (18 Jun 2025) | [USDC tx](https://snowtrace.io/tx/0xe337f88e374eceeb90bd8d6539f3c1bebf25b6b2d431516fe957d058c39cb601) · [Arkham Binance label](https://intel.arkm.com/explorer/address/0x663d966f03d66cf3fa3e007f34c8662ec4fda7c3) | A + one B | 15 Nov 2026 |
| `0xc9ad…` → Coinbase deposit 204,613 AVAX (2 Nov 2026) | [tx](https://snowtrace.io/tx/0xe77b828488f48aff36f1d911faa17198d4de545fc93880fe33a6063e262cdb88) · [Arkham Coinbase label](https://intel.arkm.com/explorer/address/0xff1a817fc120370762497aed61aef67732708a2c) | A + one B | 15 Nov 2026 |
| C-Chain burn 5,150,034 AVAX | [burn address](https://snowtrace.io/address/0x0100000000000000000000000000000000000000) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **What happened to the 320,000 AVAX sent to Coinbase Prime on 21 Sep 2026** (sold, custody, collateral, OTC?). *Narrowed 15 Nov:* it was credited to a Coinbase Prime account via deposit address `0x712b…` (Arkham), and 1,999,985 + 4,000,000 USDC later came to Wallet 1 from `0x7ed53f6e…` on 7 Oct and 2 Nov (Arkham counts the 2 Nov $4M as a Coinbase withdrawal), with 4.6M USDC sent to an Arkham-labelled Circle deposit on 22 Oct | (a) Ask the Foundation in writing; Avalanche's support and legal contacts are on avalanche.com. (b) Read AVAT's Q3 2026 10-Q on EDGAR (CIK 0002092446), filed or due ~mid-Nov 2026, for any Foundation transaction in Sep 2026. (c) Keep watching Wallet 1 `0x76bDB80A…0fC5` for a return from `0x1D67bd45…6ED1` | Free (EDGAR, Routescan). A sale inside Coinbase Prime is **never** visible on-chain, so only a disclosure can settle it |
| 2 | **Are the explorer labels right?** ✅ **Closed for Coinbase Prime:** Arkham independently labels `0x1D67…` "Coinbase Prime: Hot Wallet" (2 labels) and `0x712b…` "Coinbase Prime Deposit". **Still open for the Foundation:** Arkham has no entity for Wallet 1 or Wallet 3, so "Avalanche Foundation: Wallet 1/3" still has one label | A Foundation-published address list (best), Nansen entity labels, or Snowtrace/Etherscan-family name tags | Nansen paid · others free |
| 3 | **Foundation's total AVAX holdings** | No public source. Request a holdings / transparency statement from the Foundation. Partial route: find Foundation P-Chain addresses (lock-up UTXOs from genesis) and query `platform.getBalance` / `platform.getUTXOs` on `api.avax.network`. Avalanche's Glacier Data API (`glacier-api.avax.network`) lists P-Chain balances by address | Free API (key optional) · needs the addresses, which only the Foundation can confirm |
| 4 | **Exact date of the next 1.67M Foundation unlock** (24 Jan vs 6 Feb 2027) | Find the P-Chain UTXO with that locktime: the `lockedNotStakeable` output in `platform.getBalance` for the Foundation's genesis address shows the exact Unix locktime. Or check the Avalanche Native Token Dynamics paper (the CDN copy returned 403 earlier, so try the Wayback Machine) | Free |
| 5 | **Yearly new-coin issuance (staking inflation)** | Read `platform.getCurrentSupply` at a P-Chain height from Nov 2025 (archive node, or Glacier API historical supply) and compare with 476.59M today | Free with Glacier; an archive node is self-hosted |
| 6 | **Foundation ↔ AVAT agreement terms** (60% discount, 3M shares, board seat, right of first refusal) | Read AVAT's 10-Q / S-4 / 8-K exhibits on EDGAR, CIK 0002092446, searching "Token Sale Agreement" and "Avalanche (BVI)" | Free |
| 7 | **Who runs the Foundation** | BVI Registry of Corporate Affairs (VIRRGIN online search) for "Avalanche (BVI), Inc.". Director names are not public in the BVI by default. Also check AVAT's filings for the Foundation's board designee | Paid BVI search (small fee); directors may stay private |
| 8 | **Ava Labs CEO and officers** | Ava Labs, Inc. Delaware entity search (Delaware Division of Corporations), Ava Labs' own "team" page, or any SEC Form D filed by Ava Labs on EDGAR | Delaware search free (officers not listed); EDGAR free |
| 9 | **NYSE terms and launch date** | ICE / NYSE press release and the ATS's Form ATS-N filing on sec.gov (search ATS-N filings for the new NYSE-affiliated ATS) | Free |
| 10 | **Owner of `0x87dda0da…`** (1.6M AVAX into the same Prime deposit address in 2026, plus 2.25M to `0xc1145611…`) and of `0xc9ad9d2a…` (204,613 AVAX to a Coinbase deposit, 2 Nov 2026). ✅ **Round trip closed:** Arkham labels `0xff504ac5…` a Galaxy Digital deposit and `0x46f34c24…` / `0x15abb66b…` Galaxy Digital OTC wallets, so the Aug–Sep 400k round trip was with Galaxy Digital (one label each) | Arkham has no entity for `0x87dda0da…`, `0xc1145611…` or `0xc9ad9d2a…`. Trace their funding back to genesis or P-Chain exports with the Routescan API and Glacier; ask the Foundation whether it uses Coinbase Prime and Galaxy Digital | Free; attribution may stay unknown |
| 11 | **Chain-halt history** | Avalanche's official status page and GitHub post-mortems in `ava-labs/avalanchego` releases; or scan C-Chain block timestamps for gaps of 60 s or more | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
