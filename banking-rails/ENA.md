---
ticker: ENA
name: Ethena
chain: ethereum
contract: "0x57e114B691Db790C35207b2e685D4A43181e6061"
overall_score: 5.6
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 7
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 5
  liquidity_market: 9
  product_development: 8
  adoption_customers: 6
  security_audits: 7
  regulatory: 5
  catalysts: 6
gates_failed: [revenue]
red_lines:
  hack_exploit: "none on Ethena contracts; 217.5M ENA was stolen from Binance in its 29 Oct 2026 hot-wallet hack (exchange-side)"
  mint_path_live: "yes, owner-only mint of up to 10% of supply a year; owner is the EthenaTimelockController; never used (lastMintTimestamp = deployment)"
  team_wallet_to_exchange_during_pump: "downgraded after Arkham: the two largest pump-day moves were into custody (35.7M to a Gemini Custody multisig, 19 Jul 2024; 70M to Ethena's own Coinbase Prime deposit, 5 Sep 2025). Remaining pump-day exchange deposits from foundation-funded wallets: 21.8M (unlabelled 0xB2af, 19 Jul 2025), 8M (YZi Labs, Sep 2025), 6.3M (Ethena team vesting proxy, 2026)"
  treasury_coins_to_exchange_via_market_maker: "yes, ~1.6B ENA from foundation-funded wallets reached Coinbase Prime, Binance, Bybit, Gemini, FalconX and Galaxy OTC deposit addresses (2024–2026), mostly on non-pump days; Arkham labels ~715M of it as Ethena's own custody (Coinbase Prime) or Gemini Custody"
  fee_switch: "approved 8 Sep 2026 but inactive until 14-day average USDe supply reaches $7.5B (now ~$4.85B)"
price_usd: 0.115481
price_source: "CoinGecko, 16 Nov 2026 5:39 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ENA · Overall grade **5.6 / 10 · ❌ FAIL**

**Summary:** Ethena runs USDe, a synthetic dollar backed by hedged crypto and treasuries, and its protocol earns real fees ($233M over the last year per DefiLlama). But almost all of it goes to sUSDe holders and reserves: **ENA holders receive nothing today.** The ENA fee switch passed a vote on 8 Sep 2026 but only turns on when USDe supply averages $7.5B, and supply is about $4.85B. Wallets funded by the token's foundation-allocation Safe have sent about 1.6B ENA to exchange, custody and OTC deposit addresses since 2024. An Arkham pass shows the two biggest pump-day moves were into custody (Ethena's own Coinbase Prime account and Gemini Custody), not exchange trading, and that 2.15B ENA sits with the treasury company StablecoinX. Liquidity, product and audits are strong. **Revenue scores 3, a hard-gate FAIL.**

**🚨 Top warning (red, hard gate: Revenue):** ENA holders receive **$0** of Ethena's $233.1M in yearly fees ([DefiLlama](https://defillama.com/protocol/ethena)); the approved fee switch stays off until USDe averages **$7.5B**, and supply is **$4.85B** ([governance forum](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830)). **Selling (yellow, downgraded from red after Arkham):** the 35.7M ENA the `_foundation` Safe sent on the 19 Jul 2024 pump day went to a **Gemini Custody** multisig ([`0x90c7…`](https://etherscan.io/address/0x90c74dfe1ff09789cbdaa4514d80b8d8043ccf51), [Arkham](https://intel.arkm.com/explorer/address/0x90c74dfe1ff09789cbdaa4514d80b8d8043ccf51)), and the 680M from [`0xcfc4…`](https://etherscan.io/address/0xcfc40d4eca21f60d329f1e6b9b3d6069eaa20bbc) (incl. [70M on the 5 Sep 2025 pump day](https://etherscan.io/tx/0xc5b38697ec936814ef055a07079f48bc2eaaa779b383c55af7f338aef13ab7f0)) went to a deposit Arkham labels **"Ethena: Coinbase Prime Deposit"** ([Arkham](https://intel.arkm.com/explorer/address/0xf2e2f6827ab893d636eb98f3aac81e850880da83)) from a wallet it labels **"Ethena: Coinbase Prime Custody"** ([Arkham](https://intel.arkm.com/explorer/address/0xcfc40d4eca21f60d329f1e6b9b3d6069eaa20bbc)). Both look like custody moves, not sales. What remains: Ethena's custody wallet [`0xB805…`](https://etherscan.io/address/0xB805Ef84dd9c7DE96D8Fe79C1B6F2cA52E890936) sold [128.6M ENA](https://etherscan.io/tx/0xfc4ce913264207fec931fb3833c441d6c827c06093a931b5433ba60e29937ac7) to Binance via an Arkham-labelled **"Ethena: Binance Deposit"** ([Arkham](https://intel.arkm.com/explorer/address/0xD45e232819045d9D34fd107d19b594170515580E)) on 30 Oct 2026 (not a pump day), and investor **YZi Labs** ([Arkham](https://intel.arkm.com/explorer/address/0x877b3d5c681c8890d19dbf450306caa3c3d4bba6)), funded with 375M by the foundation Safe, keeps depositing to Binance, 8M of it on Sep 2025 pump days. Labels: [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account).

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

> **Re-scored 16 Nov 2026 after the Arkham pass:** Holdings **4 → 5** and Selling behavior **4 → 5**; overall **5.4 → 5.6**, still ❌ FAIL on the Revenue hard gate. Reasons: Arkham names the biggest "team" holders (StablecoinX treasury company 2.15B; Ethena team wallets and custody), and shows the two largest pump-day transfers went into custody, not to exchange trading.

---


# 🪪 ENA · Ethena · 5.6 / 10 · ❌ FAIL

> **One line:** Ethena runs USDe, a synthetic dollar backed by hedged crypto and treasuries, and its protocol earns real fees ($233M over the last year per DefiLlama). But almost all of it goes to sUSDe holders and reserves: **ENA holders receive nothing today.** The ENA fee switch passed a vote on 8 Sep 2026 but only turns on when USDe supply averages $7.5B, and supply is about $4.85B. Wallets funded by the token's foundation-allocation Safe have sent about 1.6B ENA to exchange, custody and OTC deposit addresses since 2024. An Arkham pass shows the two biggest pump-day moves were into custody (Ethena's own Coinbase Prime account and Gemini Custody), not exchange trading, and that 2.15B ENA sits with the treasury company StablecoinX. Liquidity, product and audits are strong. **Revenue scores 3, a hard-gate FAIL.**

| 📊 Market (CoinGecko, 16 Nov 2026 5:39 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.1155 | **Token** [`0x57e1…6061`](https://etherscan.io/address/0x57e114B691Db790C35207b2e685D4A43181e6061) ENA; owner [EthenaTimelockController `0xe8dc…7c94`](https://etherscan.io/address/0xe8dc0fab349ea169283c48ccfd09d797e6db7c94) |
| **24h / 7d / 30d** 🔴 −4.8% / −23.4% / −41.2% · 1y −57.2% | **`totalSupply()`** 15,000,000,000 ENA (no mint since deployment) |
| **Market cap** $1.560B · **FDV** $1.734B | **Deployment split** 11.25B to `_foundation` Safe [`0xd4b3…`](https://etherscan.io/address/0xd4b34207a671b813b5e66d31ea0b0a9849de9bc1) · 3.75B to `_treasury` Safe [`0x688a…`](https://etherscan.io/address/0x688ae58ebd684b3c475c81584f976593930ca67f); both now hold 0 |
| **24h volume** $216.8M | **Staked (sENA)** [944.5M (6.3%)](https://etherscan.io/token/0x8bE3460A480c80728a8C4D7a5D5303c85ba7B3b9) |
| **ATH** $1.52 (11 Apr 2024) · now −92.4% | **Holders** 106,724 (Blockscout) |
| **Circulating** 13.5B (90%) | **Wallets funded from the two deployment Safes, still holding** ≈ 6.1B ENA (≈ 41%), see Holdings |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol fees, last 365 days | **$233.1M** (≈ $15–20M a month in 2026) | [Tier A] [DefiLlama Ethena](https://defillama.com/protocol/ethena), API read 16 Nov 2026 |
| Protocol revenue kept, last 365 days | **$2.0M** | same |
| Paid to ENA holders | **$0** (sENA has no cash yield today) | [Tier A] DefiLlama holders revenue; [fee switch post](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830) |
| Fee switch | Passed Snapshot 8 Sep 2026; activates only when the **14-day average USDe supply ≥ $7.5B** | [Tier A] [governance forum](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830) · [Jul–Sep 2026 governance update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857/1) |
| USDe supply now | **$4.85B** (prev. month $4.71B) | [Tier A] [DefiLlama stablecoins](https://defillama.com/stablecoin/ethena-usde), 16 Nov 2026 |

**What it means:** A real, fee-producing business, but the fees pay sUSDe stakers and the reserve fund, not ENA. The approved fee switch is conditional on USDe growing by about 55% from here. Until it turns on, ENA is a governance token with a promise attached. Score **3**: real revenue exists, nothing reaches the token. Hard-gate FAIL.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Builder | Ethena Labs; founder and CEO Guy Young (public) | [Tier A] [Ethena docs](https://docs.ethena.fi/) |
| Token governance | Ethena Foundation forum + Snapshot votes by ENA/sENA holders | [Tier A] [gov.ethenafoundation.com](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857/1) |
| Token owner | [EthenaTimelockController](https://etherscan.io/address/0xe8dc0fab349ea169283c48ccfd09d797e6db7c94) (Blockscout contract name) | [Tier A] chain |
| Deployment Safes | `_foundation` [`0xd4b3…`](https://etherscan.io/address/0xd4b34207a671b813b5e66d31ea0b0a9849de9bc1) and `_treasury` [`0x688a…`](https://etherscan.io/address/0x688ae58ebd684b3c475c81584f976593930ca67f), both Gnosis Safes | [Tier A] [creation tx](https://etherscan.io/tx/0x143955622501605a763c6f373edef7c4a9139efffbbecb82d1833324dd558be1) |
| Signers / custody wallets | Signers of the two Safes and owners of most second-hop wallets are not published | [Unverified] |

**What it means:** Known founder, a working governance forum and a timelock on the token. The gap is wallet disclosure: Ethena does not publish which addresses hold contributor, investor and foundation tokens.

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Wallet (how it was funded) | ENA now | Notes |
|---|---:|---|
| [`0xfa84…a078`](https://etherscan.io/address/0xfa847C23ae9BD5407A64aCb2678F584bA350a078) (← [`0x1dc5…`](https://etherscan.io/tx/0xdd43ddde0c92fb68fe0149ec9a2f57b014600a72a9478f58d11b44f374ca98ca) ← [`0xcfc4…`](https://etherscan.io/tx/0x3339455dd775da5e18778577bdbb9dd20f96858295cb05c9d3ed0f630f6fb868) ← foundation Safe) | **1,231.9M (8.2%)** | Arkham: **StablecoinX** (treasury company / fund), funded via StablecoinX's Anchorage custody [Arkham](https://intel.arkm.com/explorer/address/0xfa847C23ae9BD5407A64aCb2678F584bA350a078) |
| [`0x2146…F1d0`](https://etherscan.io/address/0x2146AA5807D96E6B2922a149CeE870F17347F1d0) contract (← treasury Safe 1.55B) | **1,168.1M** | Arkham: **Ethena team wallet** (EIP-1167 proxy) [Arkham](https://intel.arkm.com/explorer/address/0x2146AA5807D96E6B2922a149CeE870F17347F1d0); pays out in small lots, like a vesting/claims contract |
| [`0xB805…0936`](https://etherscan.io/address/0xB805Ef84dd9c7DE96D8Fe79C1B6F2cA52E890936) "Ethena : Coinbase Prime Custody" (← `0xc4e5…` ← treasury Safe) | **1,100.3M** | Blockscout tag (Tier B); the funding wallet `0xc4e5…` is also "Ethena: Coinbase Prime Custody" on Arkham [Arkham](https://intel.arkm.com/explorer/address/0xc4e512313dd1ce0795f88ec5229778edf1fdf79b) |
| [`0xd332…aeC9`](https://etherscan.io/address/0xd332AB00f78884a467f11ba9c7551EC32671aeC9) (funded 8 Jul 2026; [tx](https://etherscan.io/tx/0x6eef68a18314a0a8f7e40da576825b5b45bf5ce61785f8e82dbd8a7ba6046370)) | **914.3M** | Arkham: **StablecoinX** [Arkham](https://intel.arkm.com/explorer/address/0xd332AB00f78884a467f11ba9c7551EC32671aeC9); same amount as [`0xc4e5…` → `0x8dd9…`](https://etherscan.io/tx/0xd00b7c2cc84f9935891a3b848be039ad802e48326b4661d479fb8540354e9dbf) in Sep 2025 |
| [`0x6a4B…4EB8`](https://etherscan.io/address/0x6a4B4a0FCe628750CA200B73c10Bb211b3614EB8) (← [`0x7462…`](https://etherscan.io/tx/0x846421cc881b1486fe884034f7a7f708fb11ff1367db75cf09947cea2b3ed3a8), which trades with Ethena's Safe `0xdedc…`) | **882.8M** | Unlabelled on Arkham [Arkham](https://intel.arkm.com/explorer/address/0x6a4B4a0FCe628750CA200B73c10Bb211b3614EB8); its funder `0x7462…` was first funded by StablecoinX's Anchorage custody (Arkham), so possibly StablecoinX-linked [Unverified] |
| [`0xB2af…8298`](https://etherscan.io/address/0xb2af973905f05bc82bf97486b6ab883598d98298) (← foundation Safe 1.33B) | **839.3M** | Unlabelled on Arkham [Arkham](https://intel.arkm.com/explorer/address/0xb2af973905f05bc82bf97486b6ab883598d98298); trades with FalconX |
| **Total in wallets funded from the deployment Safes** | **≈ 6.14B (≈ 41%)** | Includes unvested contributor/investor tokens, by the published schedule |

**Published allocation** ([Tier A] [docs.ethena.fi tokenomics](https://docs.ethena.fi/ena/tokenomics)): core contributors 30%, investors 25% (both 1-year cliff for 25%, then monthly over 3 years from 5 Mar 2024), Ethena Foundation 15%, ecosystem 30%.

**What it means:** Over 40% of supply sits in wallets funded straight from Ethena's own Safes. Arkham now names most of the big ones ([Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account)): ≈ 2.15B with **StablecoinX**, an outside treasury company, and ≈ 2.4B in Ethena team or custody wallets (`0x2146…`, `0xB805…`, `0x54b8…` [Arkham](https://intel.arkm.com/explorer/address/0x54b8c65f0635fd91c8729dd3269c630d9aed54e5)). Ethena itself still does not publish which wallet is which bucket, and ≈ 1.7B (`0x6a4B…`, `0xB2af…`) remains unnamed. Score **5** (was 4: identity of the largest holders is now known at Tier B).

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Method:** full ENA `tokentx` history (Etherscan v2) for the two deployment Safes and the 17 largest wallets they funded. Every transfer of 1M+ ENA was matched against exchange hot wallets, plus "deposit addresses" (wallets that forward 80%+ of what they get to an exchange). Pump days use KuCoin ENA-USDT daily closes from 3 Apr 2024.

| From (funded by) | To | ENA | Dates | Pump days? |
|---|---|---:|---|---|
| Foundation Safe `0xd4b3…` | [Binance (Launchpool)](https://etherscan.io/tx/0xc9020d0328b09b4e45fb6ac266db9d91f43e55f4573ed44d5843ce3a7b492ff3) | 300M | 29 Mar 2024 | No (pre-listing, disclosed Launchpool) |
| Foundation Safe `0xd4b3…` | [Gemini via `0x90c7…`](https://etherscan.io/tx/0x70eb2dba161d422a1c49971627309f5ab7ac02956394dfab1556f2aeebec794b), which Arkham labels **MultiSig (Gemini Custody)** [Arkham](https://intel.arkm.com/explorer/address/0x90c74dfe1ff09789cbdaa4514d80b8d8043ccf51) | **35.7M** | 19 Jul 2024 | Pump day (+21.9%), but **custody**, likely not a sale |
| Foundation Safe `0xd4b3…` | [Anchorage custody](https://etherscan.io/tx/0x6b5ee818b69b461481268d34b1b8a5915fd2a4dad7bfca2724992c7e3a6174ed) | 24.1M | 11 Apr 2024 | Pump day (+25.9%) but custodian, likely not a sale |
| Foundation Safe `0xd4b3…` | Bybit deposits ([e.g.](https://etherscan.io/tx/0x4eafeb3f9a750caad242b2a73f9759bdfbfa4f5f44fd215a2528f04d8f429e58)) | 41.4M | May 2025 | No |
| `0xcfc4…` **Ethena: Coinbase Prime Custody** (Arkham) (← 3.2B from foundation Safe) | **Ethena: Coinbase Prime Deposit** [`0xf2e2…`](https://etherscan.io/address/0xf2e2f6827ab893d636eb98f3aac81e850880da83) [Arkham](https://intel.arkm.com/explorer/address/0xf2e2f6827ab893d636eb98f3aac81e850880da83) | **680M** | 5 Sep – 14 Oct 2025 | 70M on 5 Sep 2025 (+14.3%), but **into Ethena's own custody account**, likely not a sale |
| `0xB2af…` (← 1.33B from foundation Safe) | [Coinbase Prime deposit](https://etherscan.io/tx/0x8f631c1d288b2f1c0ceb0d454eb0dd7118908864d1c292c286184fb76d7624cc) | **21.8M** | 19 Jul 2025 | **Yes, +28.7%** |
| `0xB2af…` | [FalconX deposit](https://etherscan.io/tx/0xb2baa43c6715043305be6ec483515fd52060f5eb2554dced726ecb1d97ebf04a) | 170M | 18 Aug 2026 | No (−3.7%) |
| `0x877b…` **YZi Labs (Binance Labs Fund)** per Arkham [Arkham](https://intel.arkm.com/explorer/address/0x877b3d5c681c8890d19dbf450306caa3c3d4bba6) (← 375M from foundation Safe) | Binance deposit [`0xe690…`](https://etherscan.io/address/0xe69060279c23279b3ff34d7bfb1bf50dbd626e41) | 149.4M | Aug–Sep 2025, 13–15 Oct 2026 | **8M on 3 and 5 Sep 2025** ([tx](https://etherscan.io/tx/0x374fd6daa97da45d97cd5ea19aca09f5dc12f83482896779ddd0418993c191cc)); Oct 2026 no |
| `0x54b8…` **Ethena team-wallet proxy** per Arkham (← 1.32B from foundation Safe) | Galaxy OTC and Binance deposits, monthly | 100.1M | Mar 2025 – Nov 2026 | 2 of 21 monthly payouts fell on pump days (6 May, 6 Aug 2026; 3.13M each). Looks like a vesting stream |
| `0x3C71…` (← 142.9M from foundation Safe, 2024) | Coinbase deposit [`0x649a…`](https://etherscan.io/address/0x649a16acc1fddcaf2771bd85ed9b45e887a7f273) | 102M | 9–11 Nov 2026 ([50M](https://etherscan.io/tx/0x83ac270f6a85c4153cb6bca338a84901eb9a00f54b422e95ceddace3cb25a89a)) | No (−15%) |
| "Ethena : Coinbase Prime Custody" `0xB805…` | [`0xD45e…`](https://etherscan.io/address/0xD45e232819045d9D34fd107d19b594170515580E) (Arkham: **Ethena: Binance Deposit** [Arkham](https://intel.arkm.com/explorer/address/0xD45e232819045d9D34fd107d19b594170515580E)) → [`0x690c…`](https://etherscan.io/tx/0x0246eeb34038d74877626a9f46950963fab3b2012f67a47fd843da9252b8a09e) → [Binance hot wallet 28](https://etherscan.io/tx/0xb8db97765656259a244fba8b7d0ea3e7a3420a5449734a566a76ee96d10d3c76) | 128.6M | 30 Oct – 4 Nov 2026 | No (−8.3%); reported as a sale to Binance after its hack ([Lookonchain](https://www.lookonchain.com/feeds/79712), [Bitcoin.com](https://news.bitcoin.com/market-updates/binance-buys-back-stolen-tokens-ethena-ena/)) |

- **Pump-day total ≈ 135M ENA** (35.7M + 70M + 21.8M + 8M), out of ≈ 1.6B ENA that reached exchange, OTC or prime-broker deposit addresses from Ethena-funded wallets. **After Arkham:** 105.7M of that went into custody (Gemini Custody; Ethena's own Coinbase Prime), so the pump-day amount that reached exchange trading wallets is **≈ 36M** (21.8M from unlabelled `0xB2af…`, 8M from YZi Labs, 6.3M from the Ethena vesting proxy).
- The **treasury Safe `0x688a…`** itself sent nothing to an exchange.
- Only the foundation Safe is provably Ethena's at Tier A. Arkham ([Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account)) labels `0xcfc4…`, `0xc4e5…`, `0x2146…` and `0x54b8…` as Ethena team/custody wallets, `0x877b…` as investor YZi Labs, and `0xfa84…`/`0xd332…` as StablecoinX. `0xB2af…` and `0x3C71…` have no owner label.

**What it means:** The two big pump-day moves were custody transfers, so the pump-day selling picture is smaller than first shown (≈ 36M, mostly an investor and an unnamed wallet). Ethena's own custody did sell 128.6M to Binance after its hack (not a pump day), and none of these flows is tied to a published unlock or OTC schedule. Score **5** (was 4): still a fail because team-funded wallets keep feeding exchanges without disclosure.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- **Supply:** 15B fixed at deployment; 13.5B (90%) circulating per CoinGecko.
- **Mint path:** `mint()` is owner-only, capped at 10% of supply per year, only after a 365-day wait. `lastMintTimestamp` = 1709674199 (deployment), so **it has never been used but has been callable since Mar 2025**. The owner is a timelock ([token code](https://etherscan.io/address/0x57e114B691Db790C35207b2e685D4A43181e6061#code)).
- **Unlocks:** contributor and investor tokens vest monthly until Mar 2028 ([docs](https://docs.ethena.fi/ena/tokenomics)). The monthly payouts above (e.g. `0x54b8…`) are consistent with that.
- **Staking:** only 6.3% of supply is in sENA.

## 💧 Liquidity & market · 9/10 · ✅ PASS

- $216.8M of volume in 24h on a $1.56B cap (≈ 14% turnover). Binance (hot wallets 20 and 28 hold 788M and 666M ENA), Coinbase, Bybit, Bithumb and others (Blockscout tags).
- 60 pump days in the last 365, notably 20–26 Aug 2026 (up to +95%) and 19–30 Sep 2026. Price is −92% from its ATH and −57% over the year.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- USDe (synthetic dollar), sUSDe, USDtb (treasury-backed, issued with Anchorage) and sENA.
- GitHub [`ethena-labs`](https://github.com/ethena-labs): minting clients pushed 13 Nov and 22 Oct 2026; most protocol code is in audited contracts, not public repos.

## 🤝 Adoption & customers · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| USDe supply | $4.85B (+3% month on month) | [Tier A] [DefiLlama](https://defillama.com/stablecoin/ethena-usde) |
| Fees over the last year | $233.1M | [Tier A] DefiLlama |
| Holders | 106,724 ENA holders | [Tier B] Blockscout |

Supply is well below the $7.5B fee-switch trigger, which is the adoption number that matters for ENA.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- Audits by Zellic, Quantstamp, Spearbit, Pashov (incl. ENA and sENA), Code4rena, Cyfrin; Chaos Labs risk reports. Ethena reports no critical or high findings ([Tier A] [audits page](https://docs.ethena.fi/resources/audits)).
- No exploit of Ethena contracts found. The 217.5M ENA lost in the [29 Oct 2026 Binance hack](https://news.bitcoin.com/market-updates/binance-buys-back-stolen-tokens-ethena-ena/) was an exchange failure, not an Ethena bug.
- Risk that remains: USDe depends on centralised custodians and exchanges for its hedge.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- **Germany:** BaFin stopped Ethena GmbH's USDe activity on 21 Mar 2025 and ordered a redemption process on 25 Jun 2025 ([Tier A] [BaFin](https://www.bafin.de/)).
- USDtb is issued with Anchorage Digital; Ethena markets it as GENIUS Act-ready [Tier A self-reported].
- USDe itself has no licence; the ENA token has no registration.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| Ongoing | USDe supply needs a 14-day average of $7.5B to turn on the fee switch |
| 5th of each month | Contributor/investor monthly unlocks (until Mar 2028) |
| Any time (timelocked) | Owner may mint up to 1.5B ENA a year (never used) |
| Next quarter | Ethena Foundation Oct–Dec 2026 governance update (pattern) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None on Ethena contracts (Binance's own hack lost ENA) |
| Team / treasury wallet → exchange during a pump | 🟡 (was 🔴; Arkham shows both are custody: Gemini Custody and Ethena: Coinbase Prime Deposit) Foundation Safe → Gemini Custody, [35.7M on 19 Jul 2024](https://etherscan.io/tx/0x70eb2dba161d422a1c49971627309f5ab7ac02956394dfab1556f2aeebec794b) (+21.9%); foundation-funded `0xcfc4…` [70M on 5 Sep 2025](https://etherscan.io/tx/0xc5b38697ec936814ef055a07079f48bc2eaaa779b383c55af7f338aef13ab7f0) (+14.3%) |
| Team-funded wallets → exchanges (any day) | 🟡 ≈ 1.6B ENA, 2024–2026, undisclosed per wallet |
| Live mint path | 🟡 Owner (timelock) can mint 10% a year; unused |
| Token earns nothing | 🔴 Fee switch inactive until USDe ≥ $7.5B |

## 📚 Sources

- [Tier A] Etherscan v2 API `tokentx`, `tokenbalance` and token supply for ENA and sENA; the two deployment Safes, 17 funded wallets and the second hops named above; read 16 Nov 2026 ~4:30–5:40 AM MST
- [Tier A] ENA contract source and constructor (creation tx); Blockscout contract names (GnosisSafe, EthenaTimelockController)
- [Tier A] [Ethena docs: tokenomics](https://docs.ethena.fi/ena/tokenomics) · [audits](https://docs.ethena.fi/resources/audits)
- [Tier A] [Fee switch thread](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830) · [Jul–Sep 2026 governance update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857/1)
- [Tier A] DefiLlama fees API (`ethena`) and stablecoins API (USDe), 16 Nov 2026
- [Tier A] CoinGecko `ethena` price and 365-day closes; KuCoin ENA-USDT daily candles from 3 Apr 2024
- [Tier A] [BaFin](https://www.bafin.de/) orders on Ethena GmbH (21 Mar 2025, 25 Jun 2025)
- [Tier B] Blockscout name tags and top holders ("Ethena : Coinbase Prime Custody", exchange hot wallets); the private exchange-address list used for earlier reports
- [Tier B] Arkham, read 16 Nov 2026 ~6:10 AM MST (signed-in account): labels for [0xcfc4…](https://intel.arkm.com/explorer/address/0xcfc40d4eca21f60d329f1e6b9b3d6069eaa20bbc), [0xf2e2…](https://intel.arkm.com/explorer/address/0xf2e2f6827ab893d636eb98f3aac81e850880da83), [0x90c7…](https://intel.arkm.com/explorer/address/0x90c74dfe1ff09789cbdaa4514d80b8d8043ccf51), [0x877b…](https://intel.arkm.com/explorer/address/0x877b3d5c681c8890d19dbf450306caa3c3d4bba6), [0xfa84…](https://intel.arkm.com/explorer/address/0xfa847C23ae9BD5407A64aCb2678F584bA350a078), [0xd332…](https://intel.arkm.com/explorer/address/0xd332AB00f78884a467f11ba9c7551EC32671aeC9), [0x2146…](https://intel.arkm.com/explorer/address/0x2146AA5807D96E6B2922a149CeE870F17347F1d0), [0x54b8…](https://intel.arkm.com/explorer/address/0x54b8c65f0635fd91c8729dd3269c630d9aed54e5), [0xc4e5…](https://intel.arkm.com/explorer/address/0xc4e512313dd1ce0795f88ec5229778edf1fdf79b), [0xD45e…](https://intel.arkm.com/explorer/address/0xD45e232819045d9D34fd107d19b594170515580E), [0x690c… (Binance Hot Wallet)](https://intel.arkm.com/explorer/address/0x690c3eebf6ee237f00fc96f9766282f096c191cc); no owner label on [0xB2af…](https://intel.arkm.com/explorer/address/0xb2af973905f05bc82bf97486b6ab883598d98298), [0x3C71…](https://intel.arkm.com/explorer/address/0x3c716d252b53891753de883894ff29a9ebee0f54), [0x6a4B…](https://intel.arkm.com/explorer/address/0x6a4B4a0FCe628750CA200B73c10Bb211b3614EB8), [0x7462…](https://intel.arkm.com/explorer/address/0x7462f0d93260909870487f17a27c336349579557). Arkham's token filter is Enterprise-only, so counterparties come from the default first page.
- [Tier B] [Lookonchain 79675](https://www.lookonchain.com/feeds/79675) · [Lookonchain 79712](https://lookonchain.com/feeds/79712) · [Bitcoin.com](https://news.bitcoin.com/market-updates/binance-buys-back-stolen-tokens-ethena-ena/) · [CryptoTimes](https://www.cryptotimes.io/2026/10/31/binance-buys-back-stolen-assets-via-otc-deals-after-6-3b-hack-as-ethena-sends-24m/)
- [Unverified] owners of `0xB2af…`, `0x3C71…`, `0x6a4B…`; whether Coinbase Prime/Anchorage deposits were sales; signers of both Safes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 11.25B ENA to `_foundation` Safe and 3.75B to `_treasury` Safe at deployment | [creation tx](https://etherscan.io/tx/0x143955622501605a763c6f373edef7c4a9139efffbbecb82d1833324dd558be1) · [foundation Safe](https://etherscan.io/address/0xd4b34207a671b813b5e66d31ea0b0a9849de9bc1) · [treasury Safe](https://etherscan.io/address/0x688ae58ebd684b3c475c81584f976593930ca67f) | A | 16 Nov 2026 |
| Mint is owner-only, 10%/yr, never used; owner is a timelock | [token code](https://etherscan.io/address/0x57e114B691Db790C35207b2e685D4A43181e6061#code) · [timelock](https://etherscan.io/address/0xe8dc0fab349ea169283c48ccfd09d797e6db7c94) | A | 16 Nov 2026 |
| Foundation Safe → Gemini route on a pump day | [35.7M, 19 Jul 2024](https://etherscan.io/tx/0x70eb2dba161d422a1c49971627309f5ab7ac02956394dfab1556f2aeebec794b) · [`0x90c7…`](https://etherscan.io/address/0x90c74dfe1ff09789cbdaa4514d80b8d8043ccf51) | A chain + B label | 16 Nov 2026 |
| 300M ENA to Binance for Launchpool | [Safe → `0x61ab`](https://etherscan.io/tx/0xc9020d0328b09b4e45fb6ac266db9d91f43e55f4573ed44d5843ce3a7b492ff3) · [→ Binance 14](https://etherscan.io/tx/0x5be01097d15ac337c6c7d20b19ae1482b5714033ca0f4b741534b7be449cd95b) | A + B | 16 Nov 2026 |
| `0xcfc4…` → Coinbase Prime deposit, 680M | [5 Sep 2025, 70M (pump)](https://etherscan.io/tx/0xc5b38697ec936814ef055a07079f48bc2eaaa779b383c55af7f338aef13ab7f0) · [10 Sep](https://etherscan.io/tx/0xbe76788347b17f1393840411645ae19630f13c51e7fad36bd33b54710bc865f2) · [14 Oct 2025, 363M](https://etherscan.io/tx/0x5152627b344638435633a019236e89d5aa8b4dfeb2d3888d624c2094339aa520) · [funding from Safe](https://etherscan.io/address/0xcfc40d4eca21f60d329f1e6b9b3d6069eaa20bbc) | A chain + B label | 16 Nov 2026 |
| `0xB2af…` → Coinbase Prime on pump day, FalconX later | [19 Jul 2025](https://etherscan.io/tx/0x8f631c1d288b2f1c0ceb0d454eb0dd7118908864d1c292c286184fb76d7624cc) · [18 Aug 2026, 170M](https://etherscan.io/tx/0xb2baa43c6715043305be6ec483515fd52060f5eb2554dced726ecb1d97ebf04a) | A + B | 16 Nov 2026 |
| `0x877b…` → Binance deposit | [3 Sep 2025](https://etherscan.io/tx/0x374fd6daa97da45d97cd5ea19aca09f5dc12f83482896779ddd0418993c191cc) · [5 Sep 2025](https://etherscan.io/tx/0x77bc5401402c498084219b82e267dc5f68e4eca4aa5e7bec0d6e8b4cec5c2cac) · [deposit addr](https://etherscan.io/address/0xe69060279c23279b3ff34d7bfb1bf50dbd626e41) | A + B | 16 Nov 2026 |
| `0x3C71…` sold its last 102M via Coinbase | [50M, 9 Nov 2026](https://etherscan.io/tx/0x83ac270f6a85c4153cb6bca338a84901eb9a00f54b422e95ceddace3cb25a89a) · [39M, 11 Nov](https://etherscan.io/tx/0x5e654a2fba51c3b775373c4515e870087be42e4260609d313c773d2e84e62f80) | A + B | 16 Nov 2026 |
| 128.6M ENA from Ethena's Coinbase Prime custody to Binance after the hack | [first lot](https://etherscan.io/tx/0x44cd9498460ba16ac065700da72e18cc4400a121389a27e85149efe68601e2a0) · [last lot](https://etherscan.io/tx/0x84fb50b976d5aa613015ddef4d8fa10df60445de7d3bae36bd095aae41216b0b) · [onward](https://etherscan.io/tx/0x0246eeb34038d74877626a9f46950963fab3b2012f67a47fd843da9252b8a09e) · [→ Binance 28](https://etherscan.io/tx/0xb8db97765656259a244fba8b7d0ea3e7a3420a5449734a566a76ee96d10d3c76) · [Lookonchain](https://www.lookonchain.com/feeds/79675) | A chain + B ×2 | 16 Nov 2026 |
| Fee switch passed, inactive below $7.5B USDe | [forum](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830) · [Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857/1) · [USDe supply](https://defillama.com/stablecoin/ethena-usde) | A | 16 Nov 2026 |
| Fees $233.1M, revenue $2.0M, holders $0 (1y) | [DefiLlama](https://defillama.com/protocol/ethena) | A | 16 Nov 2026 |
| `0xcfc4…` and `0xf2e2…` are Ethena's own Coinbase Prime custody and deposit | [Arkham 0xcfc4…](https://intel.arkm.com/explorer/address/0xcfc40d4eca21f60d329f1e6b9b3d6069eaa20bbc) · [Arkham 0xf2e2…](https://intel.arkm.com/explorer/address/0xf2e2f6827ab893d636eb98f3aac81e850880da83) | B | 16 Nov 2026 ~6:10 AM MST |
| `0x90c7…` is a Gemini Custody multisig | [Arkham 0x90c7…](https://intel.arkm.com/explorer/address/0x90c74dfe1ff09789cbdaa4514d80b8d8043ccf51) | B | 16 Nov 2026 ~6:10 AM MST |
| `0x877b…` is YZi Labs (Binance Labs Fund) | [Arkham 0x877b…](https://intel.arkm.com/explorer/address/0x877b3d5c681c8890d19dbf450306caa3c3d4bba6) | B | 16 Nov 2026 ~6:10 AM MST |
| `0xfa84…` and `0xd332…` (2.15B ENA) are StablecoinX | [Arkham 0xfa84…](https://intel.arkm.com/explorer/address/0xfa847C23ae9BD5407A64aCb2678F584bA350a078) · [Arkham 0xd332…](https://intel.arkm.com/explorer/address/0xd332AB00f78884a467f11ba9c7551EC32671aeC9) | B | 16 Nov 2026 ~6:10 AM MST |
| `0x2146…`, `0x54b8…`, `0xc4e5…` are Ethena team / custody wallets; `0xD45e…` is Ethena's Binance deposit | [0x2146…](https://intel.arkm.com/explorer/address/0x2146AA5807D96E6B2922a149CeE870F17347F1d0) · [0x54b8…](https://intel.arkm.com/explorer/address/0x54b8c65f0635fd91c8729dd3269c630d9aed54e5) · [0xc4e5…](https://intel.arkm.com/explorer/address/0xc4e512313dd1ce0795f88ec5229778edf1fdf79b) · [0xD45e…](https://intel.arkm.com/explorer/address/0xD45e232819045d9D34fd107d19b594170515580E) | B | 16 Nov 2026 ~6:10 AM MST |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ~~Arkham pass on the unlabelled Ethena-funded wallets~~ **Done 16 Nov 2026** (the maintainer's `arkham/ena_addresses.csv` list). Still unnamed: `0xB2af…` (839.3M), `0x3C71…`, `0x6a4B…` (882.8M), `0x7462…` | Re-check with Arkham Enterprise's token filter for full ENA counterparty history | Arkham Enterprise |
| 2 | **Which bucket (contributor, investor, foundation, market maker) is each funded wallet?** | Ask Ethena Foundation on the governance forum to publish its vesting and custody addresses | Free |
| 3 | **Partly answered:** Arkham labels the 680M destination "Ethena: Coinbase Prime Deposit" (Ethena's own account), so it looks like custody. Still open: whether Coinbase Prime later sold any of it | Ask Ethena Foundation to confirm, or track Coinbase Prime hot-wallet flows (`0xceB…`) after each deposit | Free |
| 4 | **Partly answered:** Arkham labels `0x2146…` an Ethena team-wallet proxy. Still open: which vesting bucket and who the recipients are | Read its payout pattern on Etherscan against the published vesting schedule | Free |
| 5 | **Fee switch timing** | Watch the 14-day average USDe supply on DefiLlama against $7.5B | Free |
| 6 | **BaFin order text** | Pull the two BaFin notices (21 Mar 2025, 25 Jun 2025) and link them directly | Free |
| 7 | **Is `0x6a4B…` (882.8M) StablecoinX?** | Its funder `0x7462…` was first funded by StablecoinX's Anchorage custody; ask StablecoinX for its wallet list or check its filings | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
