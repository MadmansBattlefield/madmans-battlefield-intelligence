---
ticker: INV
name: Inverse Finance
chain: ethereum
contract: "0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68"
overall_score: 4.8
overall_verdict: FAIL
section_scores:
  revenue: 6
  foundation_team: 6
  insider_holdings: 6
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 2
  product_development: 5
  adoption_customers: 5
  security_audits: 4
  regulatory: 6
  catalysts: 4
gates_failed: []
red_lines:
  hack_exploit: "yes, 2022: Anchor/Frontier oracle manipulations (2 Apr 2022, $15.6M; 16 Jun 2022, $5.83M DOLA net loss); bad debt carried until 2025"
  mint_path_live: "yes: owner() = Anchor Treasury timelock (governance) and mint() is uncapped; 104,000 INV minted 25 Jul 2025, 8,000 on 8 Dec 2025"
  team_wallet_to_exchange_during_pump: "no CEX deposit found; Policy Committee multisig (Arkham: Inverse Finance Gnosis Safe) DCA-sold 13,606 INV through CoW Protocol in Feb-Aug 2024 (10 clips on pump days) and 10,607 INV through Bond Protocol in 2022-2023; disclosure of the 2024 CoW sales not found"
  treasury_selling: "TWG paid ~321k INV (~$12.7M at the day's price) as vote incentives 2022-2025 (bribe platforms); DAO buybacks since Feb 2026 (mill 345)"
price_usd: 8.64
price_source: "CoinGecko, 16 Nov 2026 5:10 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### INV · Overall grade **4.8 / 10 · ❌ FAIL**

**Summary:** Inverse Finance runs FiRM (fixed-rate lending), the DOLA stablecoin ($122.6M) and the DBR token, and it really earns money: DefiLlama counts **$3.75M of revenue in 12 months against a $6.2M market cap**, and the DAO has been buying back INV since February 2026. But very little of that reaches INV holders directly ($113.6k a year via sINV), governance can **mint INV without a cap** (it minted 104,000 INV in July 2025 to repay bad debt), the token trades only ~$27k a day, and the protocol lost $21M+ to two oracle exploits in 2022. On-chain, the treasury and its working-group multisigs did not pay an exchange deposit address, but the **Policy Committee multisig (labelled Inverse Finance by Arkham) DCA-sold 24,213 INV** (through Bond Protocol and CoW Protocol), some of it on pump days, and the **Treasury Working Group spent ~321k INV on vote incentives** that recipients typically sell.

**🚨 Top warning:** INV's `owner()` is the [Anchor Treasury timelock `0x926d…5d9b`](https://etherscan.io/address/0x926df14a23be491164dcf93f4c468a50ef659d5b) and the [INV contract](https://etherscan.io/address/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68#code) lets the owner `mint()` with **no cap**. Governance used it for [104,000 INV on 25 Jul 2025](https://etherscan.io/tx/0x58a29f3dc169888575b32cdd2b0ec46ca65e9516bab9b039bc2996eb01c05466) (≈17% of supply then, issued at 25 DOLA per INV to strategic investors to repay $2.6M of bad debt) and [8,000 more on 8 Dec 2025](https://etherscan.io/tx/0x433e88d712e1d9d79ee1c5a10d719c20beac7c5c10f3d3757462dec1101aef05). Today's price is $8.64, about a third of that issue price. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 6/10 | ✅ PASS |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 INV · Inverse Finance · 4.8 / 10 · ❌ FAIL

> **One line:** A real, revenue-earning DeFi lender with a tiny, illiquid governance token that governance can mint at will. It was hit by two 2022 exploits, and its multisigs have sold or given away INV for years, mostly through DEXs and vote-incentive markets rather than exchanges.

| 📊 Market (CoinGecko, 16 Nov 2026 5:10 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $8.64 | **Contract** [`0x41d5…fb68`](https://etherscan.io/token/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68) (Etherscan tag "Inverse Finance: INV Token") |
| **24h / 7d / 30d** 🔴 −3.6% / −13.1% / −22.8% · 1y −75.9% | **`totalSupply()`** 727,000 INV · `owner()` = Anchor Treasury · `tradable` = true · `seizable` = false |
| **Market cap** $6.18M · **FDV** $6.28M | **INV staked in FiRM's INV market (xINV)** [`0x1637…d61b`](https://etherscan.io/address/0x1637e4e9941d55703a7a5e7807d6ada3f7dcd61b) 491,852 INV (67.7%) |
| **24h volume** $26.6k (Coinbase $20.9k, rest Curve) | **Treasury** [`0x926d…5d9b`](https://etherscan.io/address/0x926df14a23be491164dcf93f4c468a50ef659d5b) 2,414 INV held directly |
| **ATH** $2,075 (6 Mar 2021) · now −99.6% | **Minted to the treasury since 2021** 647,740 INV (13 mint events) |
| **Pump days, last ~360 days** 8 (Coinbase INV-USD closes) | **DOLA supply** $122.6M · **TVL** $28.1M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 6/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| Fees, last 12 months | **$3.83M** (30 days: $261,860) | [Tier A] [DefiLlama fees API, `inverse-finance`](https://api.llama.fi/summary/fees/inverse-finance?dataType=dailyFees), read 16 Nov 2026 |
| Revenue, last 12 months | **$3.75M** (30 days: $280,000; all-time $12.75M) | [Tier A] [DefiLlama, dailyRevenue](https://api.llama.fi/summary/fees/inverse-finance?dataType=dailyRevenue) |
| Holders revenue, last 12 months | **$113,585** (30 days: $9,337) | [Tier A] [DefiLlama, dailyHoldersRevenue](https://api.llama.fi/summary/fees/inverse-finance?dataType=dailyHoldersRevenue) |
| How holders are paid | sINV: DBR streaming rewards are auctioned for INV and added to the vault weekly | [Tier A] [Inverse docs: sINV](https://docs.inverse.finance/inverse-finance/inverse-finance/products/tokens/inv/sinv) |
| Buybacks | Since Feb 2026 the TWG runs a DBR→INV auction (up to 50M DBR a year) and keeps the INV in the treasury | [Tier A] [Mill 345](https://www.inverse.finance/governance/proposals/mills/345) · [INV tokenomics docs](https://docs.inverse.finance/inverse-finance/inverse-finance/products/tokens/inv/inv-tokenomics) |

**What it means:** $3.75M of yearly revenue on a $6.2M market cap is unusually high, and the DAO now uses DBR issuance to buy INV. But only ~3% of revenue reaches holders directly, the buyback is funded by printing DBR (not from cash profit), and expenses are not netted here. **6.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Structure | DAO: INV votes on-chain ("mills"); proposals need 7,270 INV, quorum 24,000 INV | [Tier A] [Governance overview](https://docs.inverse.finance/inverse-finance/inverse-finance/governance/governance-overview) |
| Working groups | Fed Chair 2/7 · TWG (Treasury) 3/5 · Policy Committee 5/9 (can cancel proposals) · GWG 2/3 · PWG 3/5 · AWG 2/3 · RWG 1/3 · Bug Bounty 3/5 | [Tier A] same page |
| TWG multisig | [`0x9d5d…b61b`](https://etherscan.io/address/0x9d5df30f475cea915b1ed4c0cca59255c897b61b); Arkham shows a Safe whose signer is "Inverse Finance: Deployer" ([Arkham](https://intel.arkm.com/explorer/address/0x9d5df30f475cea915b1ed4c0cca59255c897b61b)) | [Tier A] [Inverse forum: TWG allowance refresh](https://forum.inverse.finance/t/treasury-working-group-allowance-refresh/171) · [Tier B] Arkham, read 16 Nov 2026 ~6:52 AM MST (signed-in account) |
| Policy Committee multisig | [`0x4b6c…1F1B7`](https://etherscan.io/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7); Arkham entity **Inverse Finance** (Gnosis Safe Proxy, [Arkham](https://intel.arkm.com/explorer/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7)) | [Tier A] [Mill 259](https://www.inverse.finance/governance/proposals/mills/259) · [Tier B] Arkham, read 16 Nov 2026 ~6:52 AM MST (signed-in account) |
| Treasury | Anchor Treasury = a `Timelock` contract (verified source), also INV `owner()` | [Tier A] [Etherscan](https://etherscan.io/address/0x926df14a23be491164dcf93f4c468a50ef659d5b#code) |

**What it means:** Roles, multisigs and quorums are public and on-chain. The weak spot is that a small group of multisigs runs day-to-day money, and governance has repeatedly voted to mint. **6.**

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Bucket | INV | Notes |
|---|---:|---|
| Anchor Treasury (held directly) | **2,414 (0.3%)** | [`balanceOf`](https://etherscan.io/token/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68?a=0x926df14a23be491164dcf93f4c468a50ef659d5b) |
| TWG multisig | **0** | [`0x9d5d…b61b`](https://etherscan.io/token/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68?a=0x9d5df30f475cea915b1ed4c0cca59255c897b61b) |
| Policy Committee multisig | **0** | [`0x4b6c…1F1B7`](https://etherscan.io/token/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68?a=0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7) |
| Contributor vesting (`XinvVester` contracts) | Grants of 1,061–2,457 INV each (Dec 2025, Aug 2026) | e.g. [`0x069a…4b58`](https://etherscan.io/address/0x069a2f1256792f9f2390fd3a01017ca550c04b58#code) |
| July 2025 investors (via `RepayRewardEscrow`) | 104,000 INV, released Jan–Apr 2026 | [escrow](https://etherscan.io/address/0x21f9049121f81ad1959938dc2e1c202412ac6766) |

**What it means:** The DAO's visible wallets hold very little INV; most supply (67.7%) is staked in FiRM. Individual contributors' private holdings are unknown. **6.**

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**A. No exchange deposits found.** None of the treasury's, TWG's or Policy Committee's INV went straight to an Etherscan-tagged exchange address. The 23 EOAs that got 300+ INV from these wallets were checked one hop further: none of their main INV destinations is a tagged exchange address. Most staked the INV in FiRM or swapped small amounts on CoW, Velora or Curve. Arkham agrees for the largest recipients ([Tier B] Arkham, read 16 Nov 2026 ~6:52 AM MST (signed-in account)): the 47.6k-INV TWG recipient [`0x759a…f430`](https://etherscan.io/address/0x759a159d78342340ebacffb027c05910c093f430) is an individual-labelled ENS wallet that put its INV into sINV and an INVEscrow ([Arkham](https://intel.arkm.com/explorer/address/0x759a159d78342340ebacffb027c05910c093f430)); a contributor wallet [`0x16ec…51cb`](https://etherscan.io/address/0x16ec2aea80863c1fb4e13440778d0c9967fc51cb) (also an individual-labelled ENS wallet, [Arkham](https://intel.arkm.com/explorer/address/0x16ec2aea80863c1fb4e13440778d0c9967fc51cb)) shows no exchange flow on its first page.

**B. Policy Committee DCA sales (treasury-funded).** Arkham files the multisig under entity **Inverse Finance** ([Arkham](https://intel.arkm.com/explorer/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7)), a second label source on top of [mill 259](https://www.inverse.finance/governance/proposals/mills/259). Its first page shows 187.5-INV lots going to CoW Protocol Settlement with DOLA coming back, and DOLA (83.7k) and the 6.7k INV return moving between the Safe and the Anchor Treasury. Only 14 of 393 transfers were read there. The treasury sent the Policy Committee multisig 30,918 INV in 11 transfers (Dec 2022 – Aug 2024; [example](https://etherscan.io/tx/0x19a6a6bf63631c2a760eecd01d4521d4f7567aebb940c2f1b6d5b52205ef033a)). It sold:
- **10,607 INV into Bond Protocol's `BondFixedTermTeller`** (Dec 2022 – Aug 2023), the disclosed bonding program ([docs](https://docs.inverse.finance/inverse-finance/inverse-finance/products/tokens/inv/inv-tokenomics));
- **13,606 INV through CoW Protocol** (Feb – Aug 2024, ≈ $601k at the day's price), in fixed 214.3-INV clips every ~2 days. 10 clips fell on pump days, e.g. [1 Mar 2024 (+45.0%)](https://etherscan.io/tx/0xe2ecc1420c90af487b1fe174476c1440f143164ea51d75c633bc811d4ebd3b86), [16 Mar 2024 (+51.1%)](https://etherscan.io/tx/0xc370b90092ce4e20b551e84238e8e28633293910659bba7cbd98086e99eb15bb), [18 Mar 2024 (+30.0%)](https://etherscan.io/tx/0x3e8fe0eeb6154fefccf91629724b8007f1696ecd9b4a9c17aa9d1c14f7246425). The fixed size and timing look like a mechanical DCA rather than pump-timing, but **no governance post authorising these 2024 sales was found**. It returned the last 6,705 INV to the treasury on [23 Jan 2025](https://etherscan.io/tx/0x8d4d7e8dd0423cbc3279716f3d99e880adbcf7a04b7e4dbd0c33e59996769c7c).

**C. TWG paid INV as vote incentives.** The TWG sent **~321k INV (≈ $12.7M at the day's price) to vote-incentive markets** (Votium, Votemarket/Stake DAO "Platform" and "CampaignRemoteManager", Hidden Hand "BribeVault", Quest) in 2022–2025, e.g. [Votium `0x6394…2d1e`](https://etherscan.io/address/0x63942e31e98f1833a234077f47880a66136a2d1e) 129,389 INV. Those recipients usually sell. It also bought ~180k INV back through CoW in 2022–2025. These are working-group operations, not hidden sales, but they are steady sell pressure. None in 2026.

**D. 2025 investor tranche.** The 104,000 INV minted in July 2025 went into an escrow and was released as sINV to six wallets in Jan–Apr 2026. At least two redeemed some sINV and moved the INV on; two still hold all of theirs. They are investors, not team, so this does not count against the team. Arkham ([Tier B] Arkham, read 16 Nov 2026 ~6:52 AM MST (signed-in account)): the two INV destinations that looked like possible exchange or custody addresses, [`0xc1c9…d6c4`](https://etherscan.io/address/0xc1c99e764e80db823838ea63e93f862bffa7d6c4) ([Arkham](https://intel.arkm.com/explorer/address/0xc1c99e764e80db823838ea63e93f862bffa7d6c4)) and [`0x36c8…0232`](https://etherscan.io/address/0x36c80c84e286426c148cd80aaf7bafaeee020232) ([Arkham](https://intel.arkm.com/explorer/address/0x36c80c84e286426c148cd80aaf7bafaeee020232)), are **Inverse Finance INVEscrow staking proxies**, not exchanges; both forward INV into xINV. The 107k-INV source [`0x0591…dfa5`](https://etherscan.io/address/0x0591926d5d3b9cc48ae6efb8db68025ddc3adfa5) is a whale Safe Arkham does not name ([Arkham](https://intel.arkm.com/explorer/address/0x0591926d5d3b9cc48ae6efb8db68025ddc3adfa5)). Another investor wallet [`0xfa4f…6199`](https://etherscan.io/address/0xfa4fc4ec2f81a4897743c5b4f45907c02ce06199) is one Arkham tags as an individual KOL ([Arkham](https://intel.arkm.com/explorer/address/0xfa4fc4ec2f81a4897743c5b4f45907c02ce06199)), with no INV on its first page.

**What it means:** No exchange dumping by the DAO's wallets was found, but a treasury-funded multisig did sell INV on the open market (including on pump days) without a sale post we could find, and INV has been the DAO's currency for incentives. **4, unchanged after the Arkham pass.** Arkham's "Inverse Finance" label adds a second source, but the multisig was already tied to Inverse at Tier A by mill 259, and the 4 already assumed it was the DAO selling. Arkham adds nothing that makes the sales worse. The clips were fixed-size and every ~2 days, which looks mechanical rather than timed to pumps. They went through CoW rather than an exchange, and the DOLA that came back moved between the Safe and the Anchor Treasury, not to a private wallet (first page only). Arkham also shows the suspected exchange destinations were INVEscrow staking proxies. That keeps the score one point above the gate. It would drop to 3 if a governance record showed the 2024 sales were not authorised.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **Uncapped mint by governance:** `mint(address,uint)` is callable only by `owner()`, which is the treasury timelock ([verified source](https://etherscan.io/address/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68#code); `owner()`, `tradable()`, `seizable()` read via `eth_call` on 16 Nov 2026). `seizable` is false (seizing is permanently off).
- **Supply:** 727,000 INV. 647,740 INV was minted to the treasury in 13 events since 2021, most recently [104,000 (25 Jul 2025)](https://etherscan.io/tx/0x58a29f3dc169888575b32cdd2b0ec46ca65e9516bab9b039bc2996eb01c05466) and [8,000 (8 Dec 2025)](https://etherscan.io/tx/0x433e88d712e1d9d79ee1c5a10d719c20beac7c5c10f3d3757462dec1101aef05). Over the last 12 months supply grew +1.1%. The docs say there is "no maximum supply".
- xINV dilution rewards are set to 0 ("net 0 INV inflation") per the [sINV docs](https://docs.inverse.finance/inverse-finance/inverse-finance/products/tokens/inv/sinv).

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- $26.6k 24h volume on a $6.2M cap. Coinbase INV-USD $20.9k is the only real CEX market; the rest is Curve (CoinGecko tickers, 16 Nov 2026 5:10 AM MST).
- −99.6% from the 2021 high and −76% in a year. A $50k order would move the price a lot.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- FiRM fixed-rate lending, DOLA, sDOLA, DBR, sINV and jrDOLA are live ([smart-contracts page](https://docs.inverse.finance/inverse-finance/inverse-finance/technical/smart-contracts)).
- Pulling back in 2026: mill 389 paused new borrows on the INV FiRM market, [mill 393](https://www.inverse.finance/governance/proposals/mills/393) shut the sINV CCIP lanes (21 Jul 2026), and mill 396 shut the sDOLA lanes (11 Aug 2026).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- DOLA circulating supply **$122.6M**; TVL **$28.1M** (DefiLlama, 16 Nov 2026).
- Revenue run-rate is ~$280k a month. That is real usage, but small and falling with the market.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- **2 Apr 2022:** oracle manipulation of INV on SushiSwap; $15.6M borrowed from Anchor ([Inverse post-mortem](https://medium.com/inverse-finance/inv-price-manipulation-incident-55ea0433f4fc) · [CertiK](https://www.certik.com/blog/inverse-finance-02-april-2022)).
- **16 Jun 2022:** yvcrv3crypto oracle manipulation; $5.83M DOLA net loss ([Inverse docs](https://docs.inverse.finance/inverse-finance/inverse-finance/legacy-products/frontier-anchor)).
- The bad debt was carried until the July 2025 investor deal ([mill 305](https://www.inverse.finance/governance/proposals/mills/305)). A Risk Working Group with pause powers now exists.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- A DAO with no company issuer found; no enforcement action against INV or Inverse was found this pass.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Ongoing | DBR→INV treasury buybacks (mill 345), rate set by the TWG |
| Ongoing | Wind-down of cross-chain lanes; INV FiRM market borrows paused |
| None scheduled | No dated launch found |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Two oracle exploits in 2022 ($15.6M + $5.83M DOLA) |
| Team wallet → exchange during a pump | 🟡 No CEX deposit found; the Policy Committee multisig (Arkham: Inverse Finance, [Arkham](https://intel.arkm.com/explorer/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7)) DCA-sold INV on CoW incl. 10 pump-day clips ([1 Mar 2024](https://etherscan.io/tx/0xe2ecc1420c90af487b1fe174476c1440f143164ea51d75c633bc811d4ebd3b86)) |
| Live mint path | 🔴 Uncapped `mint()` by the treasury timelock; 112k INV minted in 2025 |
| Treasury selling | 🟡 ~321k INV paid to vote-incentive markets (2022–2025); buybacks since Feb 2026 |

## 📚 Sources

- [Tier A] Ethereum via Etherscan API v2: INV `totalSupply()`, `owner()`, `tradable()`, `seizable()`, `balanceOf` for treasury/TWG/Policy Committee/xINV/sINV; full INV `tokentx` for the treasury (18,331 rows), TWG (2,703), Policy Committee (193), `RepayRewardEscrow`; `getsourcecode` contract names; receipts for every linked tx (status 1), 16 Nov 2026 ~6:30–7:15 AM MST
- [Tier A] DefiLlama: fees, revenue, holders revenue, TVL (`inverse-finance`) and stablecoins (DOLA), 16 Nov 2026
- [Tier A] Inverse docs: [governance](https://docs.inverse.finance/inverse-finance/inverse-finance/governance/governance-overview) · [INV tokenomics](https://docs.inverse.finance/inverse-finance/inverse-finance/products/tokens/inv/inv-tokenomics) · [sINV](https://docs.inverse.finance/inverse-finance/inverse-finance/products/tokens/inv/sinv) · [smart contracts](https://docs.inverse.finance/inverse-finance/inverse-finance/technical/smart-contracts) · [Frontier/Anchor](https://docs.inverse.finance/inverse-finance/inverse-finance/legacy-products/frontier-anchor); mills [259](https://www.inverse.finance/governance/proposals/mills/259), [305](https://www.inverse.finance/governance/proposals/mills/305), [345](https://www.inverse.finance/governance/proposals/mills/345), [393](https://www.inverse.finance/governance/proposals/mills/393); [forum: TWG](https://forum.inverse.finance/t/treasury-working-group-allowance-refresh/171); [post-mortem](https://medium.com/inverse-finance/inv-price-manipulation-incident-55ea0433f4fc)
- [Tier B] [CertiK incident write-up](https://www.certik.com/blog/inverse-finance-02-april-2022)
- [Tier B] Arkham, read 16 Nov 2026 ~6:52 AM MST (signed-in account): Policy Committee Safe = Inverse Finance [0x4b6c…](https://intel.arkm.com/explorer/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7) · TWG Safe signer = Inverse Finance: Deployer [0x9d5d…](https://intel.arkm.com/explorer/address/0x9d5df30f475cea915b1ed4c0cca59255c897b61b) · INVEscrow proxies [0xc1c9…](https://intel.arkm.com/explorer/address/0xc1c99e764e80db823838ea63e93f862bffa7d6c4), [0x36c8…](https://intel.arkm.com/explorer/address/0x36c80c84e286426c148cd80aaf7bafaeee020232) · unnamed whale Safe [0x0591…](https://intel.arkm.com/explorer/address/0x0591926d5d3b9cc48ae6efb8db68025ddc3adfa5) · individual-labelled wallets [0x759a…](https://intel.arkm.com/explorer/address/0x759a159d78342340ebacffb027c05910c093f430), [0x16ec…](https://intel.arkm.com/explorer/address/0x16ec2aea80863c1fb4e13440778d0c9967fc51cb), [0xfa4f…](https://intel.arkm.com/explorer/address/0xfa4fc4ec2f81a4897743c5b4f45907c02ce06199) (names not reproduced here). Token filter is Enterprise-only; first transfer page only
- [Tier A] CoinGecko `inverse-finance` market data and tickers (16 Nov 2026 5:10 AM MST); Coinbase INV-USD daily closes (from 13 Jan 2022)
- [Unverified] governance authorisation for the 2024 Policy Committee CoW sales; private holdings of contributors; whether the INV markets paid by vote incentives were sold; which investor runs Safe `0x0591…dfa5`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Owner can mint without cap; owner = treasury timelock | [INV source](https://etherscan.io/address/0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68#code) · [treasury](https://etherscan.io/address/0x926df14a23be491164dcf93f4c468a50ef659d5b#code) | A | 16 Nov 2026 |
| 104,000 INV minted 25 Jul 2025; 8,000 on 8 Dec 2025 | [mint 1](https://etherscan.io/tx/0x58a29f3dc169888575b32cdd2b0ec46ca65e9516bab9b039bc2996eb01c05466) · [mint 2](https://etherscan.io/tx/0x433e88d712e1d9d79ee1c5a10d719c20beac7c5c10f3d3757462dec1101aef05) · [mill 305](https://www.inverse.finance/governance/proposals/mills/305) | A | 16 Nov 2026 |
| 104k INV went to `RepayRewardEscrow` | [escrow tx](https://etherscan.io/tx/0x368543bc6bc4bf3840251916448b3c3a5bc016e386ed7c2aafdc352f4e914f73) · [escrow](https://etherscan.io/address/0x21f9049121f81ad1959938dc2e1c202412ac6766) | A | 16 Nov 2026 |
| Policy Committee sold 13,606 INV via CoW in 2024, incl. pump days | [27 Feb 2024](https://etherscan.io/tx/0x4b85cde2ab9b78ac0973394ff205a6f0f4b7a83e6ad3769ba87c3f03bc2101dd) · [1 Mar 2024](https://etherscan.io/tx/0xe2ecc1420c90af487b1fe174476c1440f143164ea51d75c633bc811d4ebd3b86) · [16 Mar 2024](https://etherscan.io/tx/0xc370b90092ce4e20b551e84238e8e28633293910659bba7cbd98086e99eb15bb) · [multisig](https://etherscan.io/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7) | A chain · authorisation [Unverified] | 16 Nov 2026 |
| Policy Committee multisig identity | [mill 259](https://www.inverse.finance/governance/proposals/mills/259) · Arkham entity Inverse Finance [Arkham](https://intel.arkm.com/explorer/address/0x4b6c63e6a94ef26e2df60b89372db2d8e211f1b7) | A + B | 16 Nov 2026 |
| Suspected exchange destinations `0xc1c9…`, `0x36c8…` are INVEscrow staking proxies | [0xc1c9](https://intel.arkm.com/explorer/address/0xc1c99e764e80db823838ea63e93f862bffa7d6c4) · [0x36c8](https://intel.arkm.com/explorer/address/0x36c80c84e286426c148cd80aaf7bafaeee020232) | B | 16 Nov 2026 ~6:52 AM MST |
| TWG multisig identity; ~321k INV to vote-incentive markets | [forum](https://forum.inverse.finance/t/treasury-working-group-allowance-refresh/171) · [TWG](https://etherscan.io/address/0x9d5df30f475cea915b1ed4c0cca59255c897b61b) · [Votium](https://etherscan.io/address/0x63942e31e98f1833a234077f47880a66136a2d1e) | A | 16 Nov 2026 |
| Revenue $3.75M, holders revenue $113.6k (12 months) | [revenue](https://api.llama.fi/summary/fees/inverse-finance?dataType=dailyRevenue) · [holders](https://api.llama.fi/summary/fees/inverse-finance?dataType=dailyHoldersRevenue) | A | 16 Nov 2026 |
| Buybacks since Feb 2026 | [mill 345](https://www.inverse.finance/governance/proposals/mills/345) | A | 16 Nov 2026 |
| 2022 exploits | [post-mortem](https://medium.com/inverse-finance/inv-price-manipulation-incident-55ea0433f4fc) · [docs](https://docs.inverse.finance/inverse-finance/inverse-finance/legacy-products/frontier-anchor) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Was the 2024 Policy Committee CoW selling authorised and disclosed?** | Search mills/forum Feb–Aug 2024 for the Policy Committee INV allowance and its purpose | Free |
| 2 | **Arkham pass: done 16 Nov 2026** (first transfer page per wallet). No exchange found; still unnamed: the whale Safe `0x0591…dfa5`. Not answered: whether the TWG reached an exchange through intermediaries | Page through the full TWG and Policy Committee histories (393+ transfers); ask Inverse which investor runs `0x0591…` | Free |
| 3 | **DAO profit after expenses** | Inverse transparency pages / quarterly reports | Free |
| 4 | **How much INV the DAO holds inside FiRM/xINV** | Read the treasury's xINV/sINV positions | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
