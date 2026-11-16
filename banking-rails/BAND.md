---
ticker: BAND
name: Band Protocol
chain: bandchain
contract: "0xba11d00c5f74255f56a5e366f4f77f5a186d7f55"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "yes, by design (BandChain mints 7-20%/yr to stakers; 13.0% today); the Ethereum ERC20 is fixed at 100M"
  team_wallet_to_exchange_during_pump: "none found on Ethereum (Band's Locked Swap sent 12M ERC20 BAND to a Binance deposit in 2023-2025 and the Main MultiSig funded 1.64M of exchange deposits in Aug 2025, all on non-pump days); BandChain-native wallets not tested"
  treasury_in_single_key_wallets: "no (the 60.75M BAND Main MultiSig is a 1-of-1 wallet whose only owner is a 2-of-4 Safe)"
price_usd: 0.144693
price_source: "CoinGecko, 16 Nov 2026 7:13 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BAND · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** Band is an oracle network that has run on its own Cosmos chain since 2020. It is live on 40+ chains, launched BandChain v3 in Jul 2025, and is pivoting toward an AI data product (Membit). But it **publishes no revenue**, DefiLlama does not track any, and stakers are paid mostly from **13% a year of new supply**. Supply has grown from 100M to 185.7M. The founding vesting ended in 2024. The Foundation's biggest visible stash, **60.75M BAND on Ethereum (≈33% of supply)**, sits in a legacy multisig controlled by a 2-of-4 Safe. The price is down 99.4% from its 2021 high. Revenue trips the hard gate.

**🚨 Top warning:** the token pays for itself with inflation, and the Foundation's 60.75M ERC20 stash has started to move. BandChain [`/mint/inflation`](https://laozi1.bandchain.org/api/cosmos/mint/v1beta1/inflation) reads **13.0%**, about 24M new BAND a year (~$3.5M at today's price), against no disclosed protocol revenue. The **Band: Main MultiSig** [`0x7a62…5062`](https://etherscan.io/address/0x7a62a7dcf64e1eb94e374ec187ad14ba6e595062) has held 60.75M ERC20 BAND since 2019. It moved [1.64M on 19 Aug 2025](https://etherscan.io/tx/0xa74d26fd11cc8728ce0c65ce228a3e5789d58614a2ce01ffa2d28c9670bda36d) to [`0x1cb1…06f1`](https://etherscan.io/address/0x1cb16110453c42c95aa89b1878a6cfb92f8a06f1), which spread it to Binance, Gate and KuCoin deposits. Band's **Locked Swap** wallet sent **12M ERC20 BAND to a Binance deposit** between 2023 and 2025 (e.g. [5M on 26 Aug 2025](https://etherscan.io/tx/0x639091c546a2ca7233c5ab5040ec9bbab366183633ada87b4741f45792617e0f)). Band has not explained whether these are reverse swaps or sales. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BAND · Band Protocol · 4.0 / 10 · ❌ FAIL

> **One line:** A long-running oracle network with real integrations but no disclosed revenue. Holders are paid in 13% yearly inflation, and a third of supply sits in one legacy Foundation multisig.

| 📊 Market (CoinGecko, 16 Nov 2026 7:13 AM MST) | 🔗 On-chain (BandChain + Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.144693 | **Native supply** 185,727,658 BAND ([LCD](https://laozi1.bandchain.org/api/cosmos/bank/v1beta1/supply/by_denom?denom=uband)) |
| **24h / 7d / 30d** 🔴 −1.0% / −17.8% / −37.4% · 1y −65.2% | **Inflation** 13.0% (min 7%, max 20%, goal 67% bonded) |
| **Market cap** $26.87M · **FDV** $26.87M | **Bonded** 91.18M (49%) |
| **24h volume** $915k | **ERC20** [`0xBA11…7f55`](https://etherscan.io/address/0xba11d00c5f74255f56a5e366f4f77f5a186d7f55#code) fixed 100M; 36,815 holders (Blockscout) |
| **ATH** $22.83 (15 Apr 2021) · now −99.4% | **Main MultiSig** [`0x7a62…5062`](https://etherscan.io/address/0x7a62a7dcf64e1eb94e374ec187ad14ba6e595062) 60,747,284 ERC20 BAND |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Protocol fees / revenue | **Not found.** Band is not listed on DefiLlama fees; Band does not publish revenue | [Tier A] DefiLlama (no listing) · [Tier B] [WillItSurvive](https://willitsurvive.net/c/band-protocol/) |
| Staker income | Mostly new tokens: "the reward comes from newly minted tokens"; data-request fees go to validators | [Tier A] [Band token economics docs](https://docs.bandchain.org/core-concepts/token-economics) |
| Inflation paid | 13.0% × 185.7M ≈ **24M BAND a year (~$3.5M)** | [Tier A] BandChain LCD |
| Buyback / burn | None | — |

**What it means:** No revenue figure can be checked, and the yield is paid by diluting non-stakers. **2, which trips the Revenue gate.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Company | Founded 2017; $3M seed (Feb 2019) and a $5.85M Binance Launchpad sale (Sep 2019); no raise since | [Tier B] [WillItSurvive](https://willitsurvive.net/c/band-protocol/) · [Tokenomics.com](https://app.tokenomics.com/tokenomics/band-protocol) |
| Governance | On-chain BandChain proposals; the latest passed 30 Sep 2026 (IBC client recovery); BCIP-21 (Aug 2026) gated new oracle scripts behind governance | [Tier A] [gov LCD](https://laozi1.bandchain.org/api/cosmos/gov/v1/proposals?pagination.reverse=true) |
| Strategy | Rebranded to "Band" in Aug 2025; launched Membit, an AI data product | [Tier A] [Band blog](https://blog.bandprotocol.com/) |
| Disclosure | No treasury report, no wallet list, no market-maker disclosure | — |

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | BAND | Notes |
|---|---:|---|
| **Band: Main MultiSig** [`0x7a62…5062`](https://etherscan.io/address/0x7a62a7dcf64e1eb94e374ec187ad14ba6e595062) | **60,747,284 ERC20** | Got the whole 100M mint in 2019. It is a 1-of-1 `MultiSigWalletWithDailyLimit` whose only owner is Safe [`0x7a6b…fa20`](https://etherscan.io/address/0x7a6baf1c7d0940e4952186b3025b8e68aa87fa20) (**2-of-4**) [Tier A RPC] |
| Band: Locked Swap [`0x8CD2…35B8`](https://etherscan.io/address/0x8cd2283bf278e55ec40ba00438a7c71455d135b8) | 1,631,839 ERC20 | Same Safe owner; took 13.2M ERC20 in from Binance in 2020–21 swaps and sent 12M back out 2023–25 |
| Original allocation | Foundation 22% · Team 20% · Ecosystem 25.63% · Advisors 5% · Seed 10% · Private 5% · Launchpad 12.37% | [Tier B] [Tokenomics.com](https://app.tokenomics.com/tokenomics/band-protocol) + [DropsTab](https://dropstab.com/coins/band-protocol/vesting); fully vested Aug 2024 |
| BandChain-native Foundation wallets | **Not found** | No public list; not traced in this pass |

**Arkham check ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the controlling Safe [`0x7a6b…`](https://intel.arkm.com/explorer/address/0x7a6baf1c7d0940e4952186b3025b8e68aa87fa20) is unlabelled (it holds 160.006K USDC and no BAND). Arkham shows its signer EOAs as unlabelled deployer and signer addresses with no named person or firm. One signer's first-funder field carries a machine prediction of a trading firm, which Arkham does not confirm [Unverified]. Two other large ERC20 holders are exchange custody: [Coinbase cold wallet `0x4e91…`](https://intel.arkm.com/explorer/address/0x4e9105a459f37990c62c113972b94049567bae0e) 3.806M BAND (labelled) and [`0x7a59…`](https://intel.arkm.com/explorer/address/0x7a59600782cbb3be57340b820366a65505c78e65) 3.634M BAND (Coinbase is Arkham's *predicted* entity only).

**What it means:** AlphaGrowth counts the 60.75M as the "Band Protocol DAO" treasury ([Tier B](https://alphagrowth.io/dao-treasuries/band-protocol)). That is ≈33% of today's supply under a 2-of-4 Safe, and whether these ERC20 tokens back native BAND or are free to sell is not disclosed. **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Pump test uses Gate BAND/USDT daily closes (UTC). 26 of the last 365 days were pump days. Only Ethereum flows were tested.*

| Day (UTC) | Route | BAND | 5-day change | Pump? |
|---|---|---:|---:|---|
| 23 Oct 2024 · 21 Jan · 28 Jun 2025 | Locked Swap → Binance deposit [`0x6864…5Ea7`](https://etherscan.io/address/0x6864b5fc7c8d19bda1a1d1ea0ee131cb7f245ea7) ([e.g.](https://etherscan.io/tx/0x87233ed9013e75c534dc7581c7750b24ab6613aa770a5c4a5a5476aa876e3a1b)) | 2M each | 0.0% / −11.3% / −2.2% | No |
| 26 Aug 2025 | Locked Swap → same Binance deposit ([tx](https://etherscan.io/tx/0x639091c546a2ca7233c5ab5040ec9bbab366183633ada87b4741f45792617e0f)) | 5,000,000 | +4.0% | No |
| 21 Aug 2025 | Main MultiSig → `0x1cb1…` → Binance, KuCoin, Gate deposits and three EOAs ([Binance tx](https://etherscan.io/tx/0xc84d8c3a3ddb096d614468ffa046a122ffff6adf5efe728fc761fefe77c762cd)) | ~845k | +8.3% | No (just under) |
| 26 Aug 2026 | `0x1cb1…` → Binance deposit [`0x1CD8…230F`](https://etherscan.io/address/0x1cd835843a59cfa2e3ebcdf21f7a7be645e3230f) | 1,639,995 | −5.2% | No |

- `0x1cb1…` also *withdrew* from Binance 14, OKX 192, KuCoin 20, Gate and a Coinbase hot wallet during the Aug 2026 rally, which looks like market-making inventory [Unverified].
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [`0x1cb1…`](https://intel.arkm.com/explorer/address/0x1cb16110453c42c95aa89b1878a6cfb92f8a06f1) is an unlabelled **Gnosis Safe** (a multisig, not an EOA). Its top BAND counterparties are a Binance deposit (1.64M), a Binance hot wallet (372.417K) and a KuCoin hot wallet (15.913K). Arkham names no market maker or controller. [`0xA9D1…`](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43), which sent `0x1cb1…` 224.5k BAND on 21 Aug 2026, is a **Coinbase hot wallet**.

**What it means:** No pump-day sale was found on Ethereum. But ~13.6M of Foundation-controlled ERC20 went to exchanges with no stated purpose, and BandChain-native wallets (where most supply lives) were not tested. Not proven clean, so **5**.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- **Uncapped inflation:** 7–20% a year, today 13.0%; 2% of block rewards go to the community pool ([docs](https://docs.bandchain.org/core-concepts/token-economics)). Supply is **185.7M against the original 100M**.
- Non-stakers are diluted at 13%/yr; only 49% is bonded.
- The founding vesting is finished (Aug 2024), so there are no unlock cliffs left.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $915k of 24h volume on a $26.87M cap (3.4% turnover). Wide listing: Binance, Kraken, OKX, BtcTurk, Bitvavo, Bitpanda and Gate wallets are among the ERC20 top holders.
- −99.4% from ATH; −65% over a year.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- BandChain v3 mainnet (Jul 2025), governance-gated oracle scripts (BCIP-21, Aug 2026), v3.1.3 upgrade (Apr 2026) ([gov LCD](https://laozi1.bandchain.org/api/cosmos/gov/v1/proposals?pagination.reverse=true)).
- New feeds on Monad (Nov 2025), XRPL EVM (Jun 2025) and Elysium (Nov 2026) ([Band blog](https://blog.bandprotocol.com/)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Claimed total value secured ~$185–232M against Chainlink's ~$32–33B [Tier B, single source → Unverified]. Membit has no independently verified paying customer [Tier B].

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of BandChain or the BAND token found in this pass. The Foundation's ERC20 stash is under a 2-of-4 Safe, not a single key.
- Cosmos SDK chain with 49% bonded; IBC light-client recoveries passed by governance (Jan and Sep 2026).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. Not named in the SEC exchange cases [Unverified].

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Ongoing | 13% inflation; new chain integrations |
| TBA | Membit reward redemptions (possible sell pressure) [Tier B] |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None found on Ethereum; 🟡 BandChain not tested |
| Live mint path | 🔴 13% yearly inflation on BandChain |
| Treasury in single-key wallets | 🟢 No (2-of-4 Safe controls the 60.75M) |
| Unexplained Foundation flows to exchanges | 🟡 12M Locked Swap → [Binance](https://etherscan.io/address/0x6864b5fc7c8d19bda1a1d1ea0ee131cb7f245ea7); 1.64M Main MultiSig → [`0x1cb1…`](https://etherscan.io/tx/0xa74d26fd11cc8728ce0c65ce228a3e5789d58614a2ce01ffa2d28c9670bda36d) |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): [`0x1cb1…`](https://intel.arkm.com/explorer/address/0x1cb16110453c42c95aa89b1878a6cfb92f8a06f1) (unlabelled Safe) · [Safe `0x7a6b…`](https://intel.arkm.com/explorer/address/0x7a6baf1c7d0940e4952186b3025b8e68aa87fa20) and its signers (unlabelled) · [Coinbase hot wallet](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) · [Coinbase cold wallet](https://intel.arkm.com/explorer/address/0x4e9105a459f37990c62c113972b94049567bae0e) · [`0x7a59…`](https://intel.arkm.com/explorer/address/0x7a59600782cbb3be57340b820366a65505c78e65) (predicted Coinbase)
- [Tier A] Etherscan v2 API `tokentx` for the Main MultiSig, Locked Swap, `0x1cb1…` and their hops; Ethereum RPC `getOwners()`, `required()`, `getThreshold()`, `eth_getCode`; read 16 Nov 2026 ~8:05–8:20 AM MST
- [Tier A] BandChain LCD: supply, inflation, mint params, staking pool, governance proposals, 16 Nov 2026
- [Tier B] Etherscan name tags ("Band: Main MultiSig", "Band: Locked Swap", "Binance Deposit", "Gate Deposit", "KuCoin Deposit", "Binance 14", "OKX 192"); Blockscout holder list
- [Tier A] [Band token economics docs](https://docs.bandchain.org/core-concepts/token-economics) · [Band blog](https://blog.bandprotocol.com/)
- [Tier B] [Tokenomics.com](https://app.tokenomics.com/tokenomics/band-protocol) · [DropsTab](https://dropstab.com/coins/band-protocol/vesting) · [AlphaGrowth treasury](https://alphagrowth.io/dao-treasuries/band-protocol) · [WillItSurvive](https://willitsurvive.net/c/band-protocol/)
- [Tier A] CoinGecko `band-protocol` (16 Nov 2026 7:13 AM MST); Gate BAND/USDT daily candles
- [Unverified] BandChain-native Foundation wallets and their exchange flows; what the Locked Swap → Binance flows are; protocol fee totals

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Native supply 185.73M; inflation 13.0% | [supply](https://laozi1.bandchain.org/api/cosmos/bank/v1beta1/supply/by_denom?denom=uband) · [inflation](https://laozi1.bandchain.org/api/cosmos/mint/v1beta1/inflation) · [params](https://laozi1.bandchain.org/api/cosmos/mint/v1beta1/params) | A | 16 Nov 2026 |
| Main MultiSig holds 60.75M; 1-of-1 owned by a 2-of-4 Safe | [MultiSig](https://etherscan.io/address/0x7a62a7dcf64e1eb94e374ec187ad14ba6e595062#readContract) · [Safe](https://etherscan.io/address/0x7a6baf1c7d0940e4952186b3025b8e68aa87fa20#readProxyContract) | A | 16 Nov 2026 |
| Main MultiSig → `0x1cb1…` 1.64M, 19 Aug 2025 | [tx](https://etherscan.io/tx/0xa74d26fd11cc8728ce0c65ce228a3e5789d58614a2ce01ffa2d28c9670bda36d) | A | 16 Nov 2026 |
| Locked Swap → Binance deposit, 2023–2025 | [1M, Jul 2023](https://etherscan.io/tx/0x7b77d293a941f7f0fd30b0faa86cfb2f7b24bb0d618ebe135b127389988415e8) · [2M, Oct 2024](https://etherscan.io/tx/0xb62d9e008eb72c16b67dbf2fe85569e2742f63f83e68f9ffdbe4eb1c5e6ea527) · [2M, Jun 2025](https://etherscan.io/tx/0x560afb14058afb2f46385c187bdd6860f3c074e85670cc841c0ac678e41925d8) · [5M, Aug 2025](https://etherscan.io/tx/0x639091c546a2ca7233c5ab5040ec9bbab366183633ada87b4741f45792617e0f) | A + B tag | 16 Nov 2026 |
| Rewards come from new tokens | [docs](https://docs.bandchain.org/core-concepts/token-economics) | A | 16 Nov 2026 |
| Recent governance and upgrades | [proposals](https://laozi1.bandchain.org/api/cosmos/gov/v1/proposals?pagination.reverse=true) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who runs the `0x1cb1…` Safe, and is it a market maker?** | Arkham (16 Nov 2026) shows it as an unlabelled Safe that trades with Binance, KuCoin and Coinbase; `0xA9D1…` is Coinbase. Ask Band to name its market makers and the Safe's purpose | Free |
| 2 | **Do the 60.75M ERC20 back native BAND, or are they spendable treasury?** | Ask Band; compare ERC20 outside the multisig with native swap records | Free |
| 3 | **What were the 12M Locked Swap → Binance transfers?** | Ask Band whether they were native→ERC20 reverse swaps for Binance | Free |
| 4 | **BandChain-native Foundation wallets and their exchange flows** | Pull genesis accounts and large native transfers with a BandChain indexer (e.g. Mintscan API) and pump-test them | Free / API key |
| 5 | **Protocol fees** | Sum data-request fees from BandChain blocks, or ask Band to publish them | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
