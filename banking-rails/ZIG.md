---
ticker: ZIG
name: ZIGChain (Zignaly)
chain: zigchain (native) · ethereum / bsc / polygon / solana (bridged)
contract: "0xb2617246d0c6c0087f18703d576831899ca94f01"
overall_score: 3.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 3
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 4
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: none found
  mint_path_live: "no on the Ethereum token (fixed 2B, no mint function); native ZIGChain has 1–2% staking inflation and a 2.5B mainnet cap"
  team_wallet_to_exchange_during_pump: "not on a pump day: a Safe run by the same 3 signers as the founders' Safe (signers funded by or labelled Zignaly: Deployer per Arkham) sent 335.67M ZIG via relay 0x38ae… into a Bybit deposit (Nansen + Arkham), 16–22 Jan 2024 (price fell); earlier Safe-sourced ZIG reached an HTX deposit (400M, 9 Jun 2022) and a Gate deposit (200M, 6 Oct 2022) via 0x6f04 → 0x3367, not pump days; no disclosure found"
  reported_volume_concentration: "~94% of CoinGecko-reported 24h volume ($51.4M of $54.4M) is one PancakeSwap V3 BSC venue, on a $48M market cap"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Buybacks are optional by the project's own wording and revenue is not published."
pump_day_price_source: "Gate ZIG_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (43 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.03404
price_source: "CoinGecko, 16 Nov 2026 ~6:02 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZIG · Overall grade **3.3 / 10 · ❌ FAIL**

**Summary:** ZIG started as Zignaly's exchange token and now runs its own Cosmos-plus-EVM chain, ZIGChain. The chain is small, about **$4.0M locked across all its apps** (DefiLlama). The token has no measured revenue; buybacks by "ZIG Markets" are optional by the project's own words. A Gnosis Safe controlled by **the same three signers as the founders' Safe** moved **335.67M ZIG (about 17% of the then-2B supply) into a Bybit deposit address** over six days in Jan 2024 (Arkham confirms the Bybit deposit and that the Safe signers are Zignaly deployer-linked). Arkham also shows an earlier Safe-sourced branch ending in **HTX and Gate deposits** in 2022. The supply cap was raised from 2.0B to 2.5B at mainnet, and **~94% of the reported trading volume sits on one BSC pool**.

**🚨 Top warning:** team Safe [`0x378b…9c4`](https://etherscan.io/address/0x378bb8ec3bf4db2a9cc83ab0893857c0ba9899c4) (2-of-3; same signers as founders' Safe [`0x4cc0…d20`](https://etherscan.io/address/0x4cc0fae6b4e889396f35ed9d0f6934284fa00d20)), which got [729M from the token deployer in Mar 2022](https://etherscan.io/tx/0x534745042b6e591c73a78c9573d922143d74686d0fc1364bc1f49ad871f90f32), sent [335,657,086 ZIG to relay `0x38ae…6bd` on 16 Jan 2024](https://etherscan.io/tx/0x95336999b6e3804f4d1ec624cf5b29a80ebc9eae9a59b35448f5eb93a0e102b8). Over the next six days the relay paid all of it in ten lots into [`0xb73f…41a`](https://etherscan.io/address/0xb73f44289d3a071e1ad91473be2f54b0b9af441a), a Bybit deposit address (Nansen; Arkham: **Bybit Deposit** [Arkham](https://intel.arkm.com/explorer/address/0xb73f44289d3a071e1ad91473be2f54b0b9af441a)) that forwards to "Bybit: Hot Wallet" `0xf89d…aa40` ([first lot](https://etherscan.io/tx/0x4c027a2aae6d6d16dfe64026f99e1ff75e4a2a602a48a082f7e678a61999575f) · [last lot](https://etherscan.io/tx/0x8b084869dff095158c3fa5a2a8ec383175781856d0c68677f8b120c2dbc1b9cc)). That is ≈ **$11.4M** at those days' Gate closes. These were not pump days; Gate's close fell 16.1% over 5 days on 18 Jan. No disclosure was found. All links are in the 🔗 Evidence trail.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

> **Arkham pass, 16 Nov 2026:** no score change. Arkham confirms `0xb73f…` is a **Bybit Deposit** (now two Tier B sources), that the Safe signers `0x103e…` and `0x87d7…` were funded by **Zignaly: Deployer** and `0x8386…` is itself a Zignaly deployer, and that the earlier branch `0x6f04…` → `0x3367…` paid 400M into an **HTX Deposit** and 200M into a **Gate Deposit** in 2022 (not pump days on Gate closes). `0xb0a3…` (58.8M) is a **Bitvavo cold wallet**, i.e. exchange custody. The Selling gate already trips at 3; the new routes add weight but no pump-day sale, so the score stays.

---


# 🪪 ZIG · ZIGChain · 3.3 / 10 · ❌ FAIL

> **One line:** A small Cosmos/EVM chain (~$4.0M TVL) with no measured token revenue. A team-signer Safe paid 335.67M ZIG into a Bybit deposit in Jan 2024, the cap rose from 2.0B to 2.5B at mainnet, and most reported volume comes from one BSC pool.

| 📊 Market (CoinGecko, 16 Nov 2026 ~6:02 AM MST) | 🔗 On-chain (16 Nov 2026) |
|---|---|
| **Price** $0.03404 | **Ethereum token** [`0xb261…4f01`](https://etherscan.io/token/0xb2617246d0c6c0087f18703d576831899ca94f01) "ZigCoin", Solidity 0.7.6, not a proxy, **no mint function** |
| **24h / 7d / 30d** 🟢 +1.2% / 🔴 −12.8% / −33.9% · 1y −50.4% | **ERC-20 supply** 2,000,000,000 (all minted 13 Dec 2021, [creation tx](https://etherscan.io/tx/0xef15c6a6a92e303d6424a64f825bf22447bb88c4bfc2790516923c00e9cb62ea)) |
| **Market cap** $47.96M · **FDV** $66.51M | **Native cap** 2,500,000,000 ZIG (`uzig`, `zigchain-1`) |
| **24h volume** $54.44M, of which **$51.41M PancakeSwap V3 (BSC)** | **Founders' Safe** [`0x4cc0…d20`](https://etherscan.io/address/0x4cc0fae6b4e889396f35ed9d0f6934284fa00d20) 545,000,000 ERC-20 ZIG, 2-of-3, untouched since 17 Mar 2022 |
| **ATH** $0.2242 (15 Apr 2021) · now −84.8% | **Axelar gateway** [`0x4f44…6a5`](https://etherscan.io/address/0x4f4495243837681061c4743b74b3eedf548d56a5) 538.5M locked (bridge to ZIGChain) |
| **Holders** 16,691 on Ethereum (Ethplorer) | **ZIGChain TVL** $3.97M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fee / revenue data | **Not tracked** by DefiLlama for ZIGChain or Zignaly | [Tier A] DefiLlama fees API returns "not found", 16 Nov 2026 |
| Buybacks | "ZIG Markets **may from time to time** allocate a portion of realized revenues toward market acquisitions … No acquisition should be considered automatic, guaranteed, or recurring" | [Tier A] [Tokenomics 2.0 white paper](https://whitepaper.zigchain.com/zig-tokenomics.pdf) |
| Retired to date | 41,059,556 ZIG (1.64% of 2.5B) | [Tier A] [ZIGChain docs](https://docs.zigchain.com/about-zigchain/zig) |
| ERC-20 ZIG at the dead address | 46,059,208 | [Tier A] [Ethplorer holders](https://ethplorer.io/address/0xb2617246d0c6c0087f18703d576831899ca94f01#tab=tab-holders) |

**What it means:** No measured revenue reaches the token. Buybacks are optional by the project's own wording, and Zignaly's business revenue is not published. That is **2**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Buybacks are optional by the project's own wording and revenue is not published.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- **Zignaly** (copy-trading platform) created the token, and the **ZIGChain Foundation** now runs the chain. "ZIG Markets" handles buybacks [Tier A, white paper].
- The founders' 545M sits in a **2-of-3 Gnosis Safe**; signers `0x103e…`, `0x87d7…`, `0x8386…` (`getOwners()`, `getThreshold()` read 16 Nov 2026) [Tier A]. Arkham: `0x103e…` [Arkham](https://intel.arkm.com/explorer/address/0x103e1b82af90c86a2fd37ade7aaed2f09da31adf) and `0x87d7…` [Arkham](https://intel.arkm.com/explorer/address/0x87d7cf0e563025405686bd2719d5505b4d419817) were first funded by **Zignaly: Deployer** (`0x3bc…`), and `0x8386…` is labelled **Zignaly: Deployer** itself [Arkham](https://intel.arkm.com/explorer/address/0x838663068445ee4dd7cded46a50761d1cc4cabcb) ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account)). So the signers are Zignaly team wallets (Tier B); no founder is named. The **same three signers** run the second Safe `0x378b…` that made the Jan 2024 Bybit deposits.
- Which people hold the signer keys, the legal entities and audited accounts were **not found** this pass.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket (native, 2.5B cap) | ZIG | Share | Source |
|---|---:|---:|---|
| Founders' tokens | 445,000,000 | 17.80% | 30-month linear vesting from Jan 2026 [Tier A white paper] |
| ZIGChain Foundation Reserve | 100,000,000 | 4.00% | "donation from the founding team's original allocation of 545 million"; 30-month vest from Jan 2026 |
| Stake subsidies + ecosystem + long-term rewards | 500,000,000 | 20.00% | Project-controlled pools |
| **Total project-controlled** | **~1.045B** | **~41.8%** | |
| ERC-20 founders' Safe [`0x4cc0…`](https://etherscan.io/address/0x4cc0fae6b4e889396f35ed9d0f6934284fa00d20) | 545,000,000 | 27.25% of ERC-20 | [Funded 17 Mar 2022](https://etherscan.io/tx/0x91799889f21e46bc09dc8a8cd568d25057f7184ff50d88fbf0924171eeda9f17), never moved [Tier A] |

*Not team:* the 58.8M holder `0xb0a3…` is a **Bitvavo cold wallet** [Arkham](https://intel.arkm.com/explorer/address/0xb0a3a2b60e969afd26561429aa4c1444c57e4411); the 49.9M holder `0xccb8…` is unlabelled and dormant [Arkham](https://intel.arkm.com/explorer/address/0xccb87581e17ab41e62549dfc0b661ae47beb6291) ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account)).

**What it means:** About 42% of the native supply is held or steered by the founders and the foundation. The white paper calls the current founder schedule "the fourth consecutive annual extension of the unlock schedule". Delays like that are good for sellers today but show the schedule keeps moving. How the 545M ERC-20 and the 445M native founder tokens relate is not explained [Unverified].

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL

**A. Team Safe → Bybit deposit, Jan 2024 (not pump days)**

| Day (UTC) | Route | ZIG | Gate close / 5-day change | Pump? |
|---|---|---:|---:|---|
| 16 Jan 2024 | Safe `0x378b…` → relay [`0x38ae…`](https://etherscan.io/address/0x38ae7f569ece01dd34732506a8a78b2d5877f6bd) ([10k test](https://etherscan.io/tx/0xc52b69b2435baa3fa5237e797219ee83d356d1baf5496934d60dd9245d0b5783) · [335,657,086](https://etherscan.io/tx/0x95336999b6e3804f4d1ec624cf5b29a80ebc9eae9a59b35448f5eb93a0e102b8)) | 335,667,086 | $0.03882 / −9.0% | No |
| 17 Jan 2024 | Relay → Bybit deposit `0xb73f…` ([20M](https://etherscan.io/tx/0x4c027a2aae6d6d16dfe64026f99e1ff75e4a2a602a48a082f7e678a61999575f) · [25M](https://etherscan.io/tx/0xe9359682da91ecbab76514f306e9edb0c40fba89c913c7d0f8a542d965512220)) | 45,000,000 | $0.03668 / −7.0% | No |
| 18 Jan 2024 | Same ([23M](https://etherscan.io/tx/0xc9b277265c2bce7bbc0da1880a65901f921467d13cfbc4c53d941c6ecbc39049) · [31M](https://etherscan.io/tx/0xe8b6545beb68f361da6d3579fda039189c8ed8d237ec673eec3aa90e3da2eb74) · [38M](https://etherscan.io/tx/0xceaa059a2dad7175187db8c3e9be3ddec3cbb53424675831c9914713cb761865) · [37M](https://etherscan.io/tx/0xf4e7ec5ba125d353942e03c532538ce652882635e0f32d6f04f8d5c4b70ef4b6)) | 129,000,000 | $0.03417 / −16.1% | No |
| 22 Jan 2024 | Same ([37M](https://etherscan.io/tx/0xd30ef3069d2ed6ac20f2c57a6554cc5df50a1548e4e0087143a00128c35c4afb) · [35M](https://etherscan.io/tx/0x294f4a1d298958a4dec28b86c0f256820f7cfc2254580a8b26439e84200d47e8) · [43M](https://etherscan.io/tx/0x84101498404cb1bec714126a92054df95a090c14d7acc18c7afc97980c0c45d9) · [46.67M](https://etherscan.io/tx/0x8b084869dff095158c3fa5a2a8ec383175781856d0c68677f8b120c2dbc1b9cc)) | 161,667,086 | $0.03292 / −10.3% | No |

- **Why `0xb73f…` is a Bybit deposit:** Nansen tags it "Bybit / CEX", and Arkham labels it **Bybit Deposit**, forwarding to Bybit hot wallets [Arkham](https://intel.arkm.com/explorer/address/0xb73f44289d3a071e1ad91473be2f54b0b9af441a) ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account)). The relay `0x38ae…` is unlabelled on Arkham [Arkham](https://intel.arkm.com/explorer/address/0x38ae7f569ece01dd34732506a8a78b2d5877f6bd). It is a plain EOA that receives from many senders, Gate withdrawals included, and forwards each lot within ~20 minutes to `0xf89d7b9c864f589bbf53a82105107622b35eaa40`, which Nansen tags **"Bybit: Hot Wallet"** ([example sweep](https://etherscan.io/tx/0x1debf5bbf2d9e04138d2f88eb28119c8b32d07c346e9b32348fa750f67d2e8ee)). [Tier A] pattern + [Tier B] Nansen, read 16 Nov 2026.
- **Why the Safe is the team's:** it got 729,052,334 ZIG straight from the token deployer `0x3bcd…` ([tx](https://etherscan.io/tx/0x534745042b6e591c73a78c9573d922143d74686d0fc1364bc1f49ad871f90f32)), and it has the same 3 owners and 2-of-3 threshold as the founders' Safe [Tier A].
- Closes come from Gate ZIG_USDT daily candles. CoinGecko's free history covers only the last 365 days.

**B. Earlier Safe flows (Arkham labels added):** 350M went to [`0x6f04…`](https://etherscan.io/address/0x6f04d76d7542551a24849d90212218e91c72af7f) on [19 May 2022](https://etherscan.io/tx/0x2c4cc8498f41c1ba7611187034033dda7c996a59a77db2cf6d8a7bdf0a2daa82). It then passed ~950M in total (incl. 200M it received from a Gate hot wallet) to unlabelled EOA [`0x3367…039`](https://etherscan.io/address/0x33677285f6ab88f6af97315a9f85539f6335e039). Both are unlabelled on Arkham ([0x6f04](https://intel.arkm.com/explorer/address/0x6f04d76d7542551a24849d90212218e91c72af7f) · [0x3367](https://intel.arkm.com/explorer/address/0x33677285f6ab88f6af97315a9f85539f6335e039)), but the big recipients are not:

| Day (UTC) | Route | ZIG | Gate close / 5-day | Pump? |
|---|---|---:|---:|---|
| 9 Jun 2022 | `0x6f04…` → `0x3367…` [350M](https://etherscan.io/tx/0x469a79afabc3357c0ec9008adeeb362f00c2284ea211f48cf106e2323cad0d31), then `0x3367…` → **HTX Deposit** [`0xe2b4…`](https://etherscan.io/address/0xe2b46e95804dd8a2aaa41f6b667a89f1fec7445a) [400M](https://etherscan.io/tx/0x8730111566fc617f3b3aec5baddc0ce279d72f586e257da232b9851780b3ca73) seven hours later ([Arkham](https://intel.arkm.com/explorer/address/0xe2b46e95804dd8a2aaa41f6b667a89f1fec7445a)) | 400,000,000 | $0.03606 / +2.2% | No |
| 6 Oct 2022 | `0x6f04…` → `0x3367…` [400M](https://etherscan.io/tx/0xc9a078b14bec0061ddd299945a379c0be9bfe883bd9f53994a7957d94cc7ff2b), then → **Gate Deposit** [`0xe4a7…`](https://etherscan.io/address/0xe4a7fcf7c9ea28b1e897e1ac85e9e6abb027466e) [200M](https://etherscan.io/tx/0x44ecbc7191c701555eb54cb95f5c76e391b222f2cd6b28924c3c0b8cef17a0e0) three minutes later ([Arkham](https://intel.arkm.com/explorer/address/0xe4a7fcf7c9ea28b1e897e1ac85e9e6abb027466e)) | 200,000,000 | $0.00918 / −1.7% | No |
| 12 Jul 2023 | `0x6f04…` → `0x3367…` [200M](https://etherscan.io/tx/0x2c7f34fc6aa15f781cdeba595d5e7637b41be6fbfc96c03bf21860cfc1f191fe), then → [`0x98a8…`](https://etherscan.io/address/0x98a808a1f425bc2d11cccd291d5757b623c5a71b) [221.8M](https://etherscan.io/tx/0x8ba1f7f0bb7df3dce780e72eb86cd895e4425b98bfced4cac39137bf4a2e1b52), which Arkham attributes to **Zignaly** (trades ZIG/USDT on PancakeSwap; [Arkham](https://intel.arkm.com/explorer/address/0x98a808a1f425bc2d11cccd291d5757b623c5a71b)) | 221,800,000 | $0.00452 / −8.5% | No |

Because `0x6f04…` also took 200M from a Gate hot wallet, not every coin in these lots is Safe-sourced; the 9 Jun 2022 HTX lot followed the Safe's 350M most directly [Tier A chain + Tier B Arkham labels].

**C. Last 12 months (CoinGecko pump days, 60 of 365):** neither team Safe sent any ZIG (last Safe transfer: 16 Jan 2024). Native-chain founder vesting wallets were **not traced** (see Open items).

**What it means:** A team-controlled Safe put about 17% of the then-total supply into a Bybit deposit within a week, with no disclosure found, while the price fell, and earlier Safe-sourced ZIG reached HTX and Gate deposits. None of it was on pump days, so the strict pump rule is not met. But the size and the lack of disclosure put it at **3** (unchanged after Arkham), which **trips the Selling gate**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate ZIG_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (43 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- The **ERC-20** has a fixed 2B with no mint (bytecode has only standard ERC-20 functions) [Tier A].
- **ZIGChain mainnet cap is 2.5B**, so 500M more than the ERC-20 supply. Circulating at mainnet was 1,726,440,444 (69.06%). Staking inflation is 1–2% [Tier A docs]. CoinGecko still shows a 2B max.
- Founder unlock extended four years running; now ~14.8M a month (445M ÷ 30) plus ~3.3M a month to the Foundation.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- CoinGecko reports $54.44M in 24h, but **$51.41M (94%) of it is PancakeSwap V3 on BSC**. Next are Bybit $1.28M, BloFin $0.46M, Zoomex $0.38M, Oroswap $0.31M and Gate $0.27M [Tier A CoinGecko tickers]. Volume near 1× market cap on one DEX pool looks like bot or wash activity [Unverified].
- 60 pump days in the last 365.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- ZIGChain mainnet (`zigchain-1`) with native EVM since v6.0.0 (chain ID 944) [Tier A docs]. Apps include OroSwap, Valdora, Nawa and Permapod.
- Public repos and audits were not read this pass.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- **Chain TVL $3.97M** (DefiLlama). The largest app counted on ZIGChain lists ~$7.2M across three chains. Small for a $66M FDV.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- ✅ The ERC-20 is immutable with no mint, and the founder funds sit in a multisig.
- ⚠️ 538.5M ERC-20 ZIG is locked in the Axelar gateway, so bridge risk applies. No audit of ZIGChain modules was read. No hack found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- No licence or MiCA white paper for ZIG was checked this pass. Not proven.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly to ~Jun 2028 | Founder (~14.8M) and Foundation (~3.3M) linear unlocks |
| Monthly | Possible ZIG Markets buybacks and retirement votes (discretionary) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Live mint path | 🟢 Not on the ERC-20 · 🟡 native chain has inflation and a cap raised to 2.5B |
| Team wallet → exchange during a pump | 🟢 Not found on pump days |
| Team wallet → exchange (any day) | 🔴 **Yes:** 335.67M via `0x38ae…` into a Bybit deposit, 16–22 Jan 2024; earlier 400M (HTX deposit, 9 Jun 2022) and 200M (Gate deposit, 6 Oct 2022) via `0x6f04…` → `0x3367…`. [Safe → relay](https://etherscan.io/tx/0x95336999b6e3804f4d1ec624cf5b29a80ebc9eae9a59b35448f5eb93a0e102b8) · [last lot](https://etherscan.io/tx/0x8b084869dff095158c3fa5a2a8ec383175781856d0c68677f8b120c2dbc1b9cc) |
| Reported-volume concentration | 🟡 94% on one BSC pool |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Team-controlled Safe → Bybit deposit | Zignaly team Safe (3 signers) | Etherscan | high | yes | Selling: ~17% of supply to Bybit, not on pump days; the score of 3 rests on size and silence, not on a pump-day sale |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API: `tokentx` for the deployer, both Safes, `0xfc3e…`, `0x6f04…`, `0x38ae…`, `0xb73f…`, `0x3367…`; `getsourcecode`, `getcontractcreation`; `eth_call` `getOwners()` / `getThreshold()` on both Safes, 16 Nov 2026 MST
- [Tier A] Ethplorer top holders and token info, 16 Nov 2026
- [Tier A] [Tokenomics 2.0 white paper](https://whitepaper.zigchain.com/zig-tokenomics.pdf) · [ZIG token docs](https://docs.zigchain.com/about-zigchain/zig) · [transparency dashboard docs](https://docs.zigchain.com/users/hub/transparency-dashboard)
- [Tier A] CoinGecko `zignaly` market data, tickers and 365-day closes (16 Nov 2026); Gate ZIG_USDT daily candles Dec 2023 – Jan 2024
- [Tier A] DefiLlama chains / protocols (ZIGChain TVL $3.97M) and fees API (no ZIG entry)
- [Tier B] Nansen labels, read 16 Nov 2026 ~6:05–6:15 AM MST: `0xb73f…` Bybit, `0xf89d…` Bybit: Hot Wallet, `0x6bb1…` / `0x0d07…` Gate, `0x4b1a…` AscendEx, `0x0211…` MEXC
- [Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account): **Bybit Deposit** [0xb73f…](https://intel.arkm.com/explorer/address/0xb73f44289d3a071e1ad91473be2f54b0b9af441a); **HTX Deposit** [0xe2b4…](https://intel.arkm.com/explorer/address/0xe2b46e95804dd8a2aaa41f6b667a89f1fec7445a); **Gate Deposit** [0xe4a7…](https://intel.arkm.com/explorer/address/0xe4a7fcf7c9ea28b1e897e1ac85e9e6abb027466e); **Zignaly** [0x98a8…](https://intel.arkm.com/explorer/address/0x98a808a1f425bc2d11cccd291d5757b623c5a71b); **Zignaly: Deployer** [0x8386…](https://intel.arkm.com/explorer/address/0x838663068445ee4dd7cded46a50761d1cc4cabcb); Zignaly-deployer-funded signers [0x103e…](https://intel.arkm.com/explorer/address/0x103e1b82af90c86a2fd37ade7aaed2f09da31adf), [0x87d7…](https://intel.arkm.com/explorer/address/0x87d7cf0e563025405686bd2719d5505b4d419817); **Bitvavo: Cold Wallet** [0xb0a3…](https://intel.arkm.com/explorer/address/0xb0a3a2b60e969afd26561429aa4c1444c57e4411); no label on [0x38ae…](https://intel.arkm.com/explorer/address/0x38ae7f569ece01dd34732506a8a78b2d5877f6bd), [0x3367…](https://intel.arkm.com/explorer/address/0x33677285f6ab88f6af97315a9f85539f6335e039), [0x6f04…](https://intel.arkm.com/explorer/address/0x6f04d76d7542551a24849d90212218e91c72af7f), [0xccb8…](https://intel.arkm.com/explorer/address/0xccb87581e17ab41e62549dfc0b661ae47beb6291). Arkham's token filter is Enterprise-only, so counterparties come from the default first page.
- [Tier A] Gate ZIG_USDT daily candles for 9 Jun 2022, 6 Oct 2022 and 12 Jul 2023
- [Unverified] individual signer identities; owner of `0x38ae…`, `0x3367…`, `0x6f04…`; whether the Jan 2024 deposit was disclosed or sold; native-chain founder wallets; Zignaly revenue

## 🔗 Evidence trail

*Every link below opens the primary record for the claim.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Fixed 2B ERC-20, no mint | [token code](https://etherscan.io/address/0xb2617246d0c6c0087f18703d576831899ca94f01#code) · [creation](https://etherscan.io/tx/0xef15c6a6a92e303d6424a64f825bf22447bb88c4bfc2790516923c00e9cb62ea) | A | 16 Nov 2026 |
| Founders' 545M in a 2-of-3 Safe, unmoved since 2022 | [Safe](https://etherscan.io/address/0x4cc0fae6b4e889396f35ed9d0f6934284fa00d20) · [funding](https://etherscan.io/tx/0x91799889f21e46bc09dc8a8cd568d25057f7184ff50d88fbf0924171eeda9f17) | A | 16 Nov 2026 |
| Second Safe got 729M from the deployer; same signers | [Safe](https://etherscan.io/address/0x378bb8ec3bf4db2a9cc83ab0893857c0ba9899c4) · [funding](https://etherscan.io/tx/0x534745042b6e591c73a78c9573d922143d74686d0fc1364bc1f49ad871f90f32) | A | 16 Nov 2026 |
| 335.67M Safe → relay → Bybit deposit, 16–22 Jan 2024 | [Safe → relay](https://etherscan.io/tx/0x95336999b6e3804f4d1ec624cf5b29a80ebc9eae9a59b35448f5eb93a0e102b8) · [17 Jan](https://etherscan.io/tx/0x4c027a2aae6d6d16dfe64026f99e1ff75e4a2a602a48a082f7e678a61999575f) · [18 Jan](https://etherscan.io/tx/0xceaa059a2dad7175187db8c3e9be3ddec3cbb53424675831c9914713cb761865) · [22 Jan](https://etherscan.io/tx/0x8b084869dff095158c3fa5a2a8ec383175781856d0c68677f8b120c2dbc1b9cc) · [deposit](https://etherscan.io/address/0xb73f44289d3a071e1ad91473be2f54b0b9af441a) | A chain + B label | 16 Nov 2026 |
| Deposit sweeps to Bybit hot wallet | [sweep example](https://etherscan.io/tx/0x1debf5bbf2d9e04138d2f88eb28119c8b32d07c346e9b32348fa750f67d2e8ee) · [hot wallet](https://etherscan.io/address/0xf89d7b9c864f589bbf53a82105107622b35eaa40) | A + B (Nansen) | 16 Nov 2026 |
| 350M Safe → 0x6f04 → 0x3367 | [tx](https://etherscan.io/tx/0x2c4cc8498f41c1ba7611187034033dda7c996a59a77db2cf6d8a7bdf0a2daa82) · [0x3367](https://etherscan.io/address/0x33677285f6ab88f6af97315a9f85539f6335e039) | A · owner [Unverified] | 16 Nov 2026 |
| 0x3367 → HTX deposit 400M (2022), Gate deposit 200M (2022), Zignaly wallet 221.8M (2023) | [HTX lot](https://etherscan.io/tx/0x8730111566fc617f3b3aec5baddc0ce279d72f586e257da232b9851780b3ca73) · [Gate lot](https://etherscan.io/tx/0x44ecbc7191c701555eb54cb95f5c76e391b222f2cd6b28924c3c0b8cef17a0e0) · [Zignaly lot](https://etherscan.io/tx/0x8ba1f7f0bb7df3dce780e72eb86cd895e4425b98bfced4cac39137bf4a2e1b52) · [Arkham HTX](https://intel.arkm.com/explorer/address/0xe2b46e95804dd8a2aaa41f6b667a89f1fec7445a) · [Arkham Gate](https://intel.arkm.com/explorer/address/0xe4a7fcf7c9ea28b1e897e1ac85e9e6abb027466e) · [Arkham Zignaly](https://intel.arkm.com/explorer/address/0x98a808a1f425bc2d11cccd291d5757b623c5a71b) | A chain + B (Arkham) | 16 Nov 2026 ~6:38 AM MST |
| Bybit deposit label; Safe signers tied to Zignaly: Deployer | [Arkham 0xb73f…](https://intel.arkm.com/explorer/address/0xb73f44289d3a071e1ad91473be2f54b0b9af441a) · [0x103e…](https://intel.arkm.com/explorer/address/0x103e1b82af90c86a2fd37ade7aaed2f09da31adf) · [0x87d7…](https://intel.arkm.com/explorer/address/0x87d7cf0e563025405686bd2719d5505b4d419817) · [0x8386…](https://intel.arkm.com/explorer/address/0x838663068445ee4dd7cded46a50761d1cc4cabcb) | B (Arkham) + B (Nansen for Bybit) | 16 Nov 2026 ~6:38 AM MST |
| Allocations, 2.5B cap, buybacks discretionary, fourth unlock extension | [white paper](https://whitepaper.zigchain.com/zig-tokenomics.pdf) · [docs](https://docs.zigchain.com/about-zigchain/zig) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ~~Arkham pass on 12 wallets~~ **Done 16 Nov 2026** (the maintainer's `arkham/zig_addresses.csv` list): Bybit / HTX / Gate deposits, Zignaly wallets and deployer-linked signers, Bitvavo cold wallet. Still unnamed: relay `0x38ae…`, hubs `0x6f04…` / `0x3367…`, `0xccb8…` | Re-check with Arkham Enterprise's token filter for full ZIG history | Arkham Enterprise |
| 2 | **Was the Jan 2024 Bybit deposit disclosed?** | Search Zignaly / ZIGChain posts from Jan 2024; ask the team what the 335.67M was for | Free |
| 3 | **Native-chain founder and foundation wallets** | Read ZIGChain vesting accounts via LCD (`/cosmos/auth/v1beta1/accounts`) and test transfers to exchange deposits on pump days | Free |
| 4 | **Is the BSC PancakeSwap volume real?** | Read the pool's swaps, count unique traders and look for self-trading | Free |
| 5 | **ERC-20 545M vs native 445M founders** | Ask how the ERC-20 Safe maps to the native allocation (burn, bridge or separate) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
