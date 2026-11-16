---
ticker: AXL
name: Axelar
chain: axelar
contract: "0x467719ad09025fcc6cf6f8311755809d45a5e5f3"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 6
  adoption_customers: 4
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "yes, by design (no supply cap; net supply growth ~3.0% a year after fee burns; base Cosmos inflation set to 0)"
  team_wallet_to_exchange_during_pump: "not proven (Foundation and company wallets on the Axelar chain are not labelled; the largest unlabelled native movers trade two-way with high-volume hot wallets, which looks like exchange custody)"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "not found (no published treasury addresses)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Fees are burned on-chain automatically, but the burn covers only ~4% of issuance; Revenue stays 2."
pump_day_price_source: "KuCoin AXL/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.03252332
price_source: "CoinGecko, 16 Nov 2026 7:13 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### AXL · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Axelar is a cross-chain messaging network (its own Cosmos PoS chain plus gateway contracts on 70+ chains) with ~$126M bridged TVL. Since the Feb 2025 "Cobalt" upgrade, 98% of AXL gas fees are burned. But fees are tiny: **$53.6k in the last year** on DefiLlama, and DefiLlama counts **$0 revenue**. Meanwhile staking rewards still add ~38M AXL a year, so supply grows ~3% net. In Dec 2025 **Circle agreed to buy the Interop Labs team and IP**, the company that built Axelar, to work on Circle's own Arc and CCTP. A smaller contributor, Common Prefix, now leads development. The price is $0.0325, 4.9% above its all-time low, and down 98.8% from its Mar 2024 high. Revenue trips the hard gate.

**🚨 Top warning:** the builders left for a competitor and the token does not pay for itself. Circle's [Dec 2025 post](https://www.circle.com/blog/circle-signs-agreement-to-acquire-interop-labs-team-intellectual-property) says the Interop Labs team and its proprietary IP move to Circle to speed up **Arc and CCTP**, both of which compete with Axelar. The ~$53.6k of fees burned last year ([DefiLlama](https://defillama.com/protocol/axelar)) offsets about **4%** of the ~38M AXL (~$1.2M) minted as rewards ([MoonRunners](https://moon-runners.net/axelar/mainnet/supply)). Only **262.2M AXL (20.8%, ~$8.5M)** is staked to secure ~$126M of bridged value, and another 57.4M is unbonding ([staking pool LCD](https://axelar-rest.publicnode.com/cosmos/staking/v1beta1/pool)). Bid depth is thin: CoinGecko shows $2.99M of daily volume, but Binance's AXL/USDT book holds about $13k within 2% below the price ([TokenRadar](https://tokenradar.ai/tokens/axelar-network/tokenomics)).

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 AXL · Axelar · 3.8 / 10 · ❌ FAIL

> **One line:** Working cross-chain plumbing whose fees are too small to offset its staking issuance, whose original builders have moved to Circle, and whose token trades near its all-time low.

| 📊 Market (CoinGecko, 16 Nov 2026 7:13 AM MST) | 🔗 On-chain (Axelar chain + Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.03252 (ATL $0.03098) | **Native supply** 1,260,472,718 AXL ([LCD](https://axelar-rest.publicnode.com/cosmos/bank/v1beta1/supply/by_denom?denom=uaxl)) |
| **24h / 7d / 30d** 🔴 −0.7% / −8.9% / −41.2% · 1y −76.8% | **Bonded** 262.2M (20.8%) · **Unbonding** 57.4M ([pool](https://axelar-rest.publicnode.com/cosmos/staking/v1beta1/pool)) |
| **Market cap** $40.84M · **FDV** $40.99M · no max supply | **Cosmos mint inflation** 0% ([LCD](https://axelar-rest.publicnode.com/cosmos/mint/v1beta1/inflation)); chain-voting reward 0.2% per chain ([params](https://axelar-rest.publicnode.com/axelar/reward/v1beta1/params)) |
| **24h volume** $2.99M | **Bridge escrow** [`axelar1jesak…95sm`](https://axelarscan.io/account/axelar1jesak80ju7yw09pncdz7r2myg3jwz8a66yhm7dwrvqz7xhmvdndqx095sm) 345.06M AXL backing wrapped AXL |
| **ATH** $2.64 (1 Mar 2024) · now −98.8% | **Ethereum wAXL** [`0x4677…e5f3`](https://etherscan.io/token/0x467719ad09025fcc6cf6f8311755809d45a5e5f3) 326.1M; largest holders per Arkham: Upbit deposit 119.25M, an unlabelled EOA 9.10M, Kraken 8.38M |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees | **$1,780 (30d) · $53,639 (1y)** | [Tier A] [DefiLlama Axelar](https://defillama.com/protocol/axelar) |
| Revenue | **$0** ("Axelar doesn't collect any fee") | [Tier A] DefiLlama |
| Value to holders | 98% of AXL gas fees burned, 2% to the community pool (Cobalt, Feb 2025) | [Tier A] [Axelar blog](https://www.axelar.network/blog/cobalt-tokenomics-upgrade) |
| New supply | ~38M AXL a year (~$1.2M), net of burns | [Tier B] [MoonRunners](https://moon-runners.net/axelar/mainnet/supply) + [TokenRadar](https://tokenradar.ai/tokens/axelar-network/tokenomics) (~109.7k/day) |

**What it means:** The burn is real but covers about 4% of issuance. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Fees are burned on-chain automatically, but the burn covers only ~4% of issuance; Revenue stays 2.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Core developer | Circle agreed (15 Dec 2025) to acquire the Interop Labs team and proprietary IP, to work on Arc and CCTP. Axelar Network, Foundation and AXL "continue to operate independently under community governance" | [Tier A] [Circle](https://www.circle.com/blog/circle-signs-agreement-to-acquire-interop-labs-team-intellectual-property) · [Axelar blog](https://www.axelar.network/blog/circle-interop-labs-acquisition-agreement) |
| New steward | Common Prefix took over Interop Labs' activities. 2026 roadmap: institutional products, co-staking, gasless bridging | [Tier A] [Common Prefix roadmap](https://www.commonprefix.com/blog/axelar-roadmap) |
| Cost cuts | May 2026: proposal to drop Flow, Berachain and Plume, which had "effectively no sustained economic activity". The Foundation had been subsidising "hundreds of thousands of dollars per year" of verifier costs | [Tier A] [Axelar blog](https://www.axelar.network/blog/discontinuing-flow-berachain-plume) |
| Disclosure | No published Foundation or company treasury addresses or balances | — |

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | AXL | Notes |
|---|---:|---|
| Genesis allocation | Company 29.5% (core team 17%, operations 12.5%) · Backers 29.54% · Community programs (Foundation) 35.96% · Sale 5% | [Tier A] [Axelar Foundation token economics](https://medium.com/@axelar-foundation/an-overview-of-axl-token-economics-4dc701c9054d) |
| Vesting status | Core-team release models end around late Nov 2026; everything else is released | [Tier B] [TokenRadar](https://tokenradar.ai/tokens/axelar-network/tokenomics) [Unverified, single source] |
| Bridge escrow `axelar1jesak…` | 345,057,636 | Backs wrapped AXL elsewhere (Ethereum wAXL alone is 326.1M, [Tier A RPC](https://etherscan.io/token/0x467719ad09025fcc6cf6f8311755809d45a5e5f3)); not a treasury |
| Largest unlabelled native account [`axelar1p3uc…463`](https://axelarscan.io/account/axelar1p3ucd3ptpw902fluyjzhq3ffgq4ntddautx463) | 89,470,644 | Got 601.7M from, and sent back out to, [`axelar1rhfw…tdsz`](https://axelarscan.io/account/axelar1rhfwuk0f5ft2watjaxx07d99jhf3c8u4mjtdsz) (125,805 txs). Looks like exchange custody [Unverified] |
| Unlabelled Ethereum holder [`0x1a9d…85e3`](https://intel.arkm.com/explorer/address/0x1a9d699aee3a56ca49d0cc3b542ae3a37885a3e1) | 9,096,000 (9.096M) | wAXL. Arkham shows no owner, only "High Transacting" and "Early Holder" tags, and no AXL transfers on its first page. Not shown to be an exchange or an insider ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) |
| Foundation / company wallets | **Not found** | No public list. Arkham does not cover the Axelar chain, and no Ethereum wallet it shows is labelled Axelar Foundation or Interop Labs |

**What it means:** On paper the insiders are almost fully vested, but nobody can see what the Foundation and the old company still hold. Arkham's Ethereum labels show exchange custody for most large wAXL balances and no Foundation wallet. **4** (unchanged).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Pump test uses KuCoin AXL/USDT daily closes (UTC) because AXL is delisted on Gate. 33 of the last 365 days were pump days.*

| Day (UTC) | Route | AXL | 5-day change | Pump? |
|---|---|---:|---:|---|
| 16–17 Apr 2026 | `axelar1p3uc…` → `axelar1rhfw…` ([35M](https://axelarscan.io/tx/6C926AF3CC2F43D538E4CF762837294929245C22831557770021833031CB612E) · [30M](https://axelarscan.io/tx/903A07D0AAC045554C45846EBEEECC7CBBD2FEEB05B418B20833DA9F62BE694F)) | 65,000,000 | +46.0% / +26.6% | Yes, but unattributed |
| 16 Apr 2026 | [`axelar1tgjx…2un`](https://axelarscan.io/account/axelar1tgjxuylt4qpvup7wwfe698zww8j3kd0tepk2un) → [`axelar1pdw4…tnn`](https://axelarscan.io/account/axelar1pdw4mgz49pmgwnjz64fgfeys32a5sjxgyx2tnn) ([tx](https://axelarscan.io/tx/1AC459255CF75613C0E6B762E10E97082273B30626D559D53527B5FA630391D9)) | 29,814,364 | +46.0% | Yes, but unattributed |
| 10 and 12 Jun 2025 | `axelar1p3uc…` → `axelar1rhfw…` ([35.8M](https://axelarscan.io/tx/410BF64922677D231350A485201C68FBF5285A39E6FC93CC8558EEB7C3F66FCD)) | 55,799,938 | +69.0% / +35.0% | Yes, but unattributed |

- Both pairs move hundreds of millions **in both directions**: `axelar1tgjx…` got 372.4M from `axelar1pdw4…`. That is how exchange hot and cold wallets behave, not how a Foundation sells. Nothing ties either pair to the Foundation or the company [Unverified].
- On Ethereum, Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) puts the largest wAXL balances with exchanges: [Upbit deposit `0xD2FF…`](https://intel.arkm.com/explorer/address/0xd2ff2d432a0078672cf4f9e2e97858a33cbdeebc) **119.253M** (its first transfers are Upbit hot-wallet sweeps) and [Kraken hot wallet `0xfcac…`](https://intel.arkm.com/explorer/address/0xfcac185644e5c6cd73c309a60d2758ae56cf78b3) **8.375M**. [Paribu hot wallet `0xc80a…`](https://intel.arkm.com/explorer/address/0xc80afd311c9626528de66d86814770361fe92416) showed **no AXL** in its portfolio or first transfer page. The token contract itself holds 24.251K AXL ([Arkham](https://intel.arkm.com/explorer/address/0x467719ad09025fcc6cf6f8311755809d45a5e5f3)).
- The one large non-exchange holder, `0x1a9d…` (**9.096M**, ~0.7% of supply), is unlabelled and has no AXL transfers on its first Arkham page. That neither shows nor rules out insider selling. The ERC20 side shows no proven insider flows, but it is not shown clean either.

**What it means:** No insider sale was found, but Foundation and company wallets could not be identified (Arkham does not cover the Axelar chain, and the largest unlabelled Ethereum holder has no owner), so the selling record is not proven. **4** (unchanged after the Arkham check).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from KuCoin AXL/USDT daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **No cap.** Base Cosmos inflation is 0 today ([LCD](https://axelar-rest.publicnode.com/cosmos/mint/v1beta1/params)); it was cut by [proposal 294](https://axelar.valopers.com/proposals/294) (Mar 2025), but chain-voting rewards of 0.2% per connected EVM chain remain ([params](https://axelar-rest.publicnode.com/axelar/reward/v1beta1/params)). Net growth is ~3.0% a year (+2.9M AXL in 30 days) [Tier B ×2].
- **Amplifier chains** fund verifier reward pools out of existing supply, not new mint ([Cobalt blog](https://www.axelar.network/blog/cobalt-tokenomics-upgrade)).
- Supply 1.26B against a 1.0B genesis supply; genesis vesting is nearly finished.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- CoinGecko shows $2.99M of 24h volume (7.3% of the cap), but TokenRadar's market table shows HTX volume of $1.3M with **$3 / $18** of 2% depth, and Binance with **$13k / $217k**. That suggests much of the reported volume is not real depth [Tier B, Unverified].
- Price is 4.9% above the all-time low; −41% in 30 days; −98.8% from ATH.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Active on-chain governance: consensus gateways upgraded to v6.5.0 (10 Nov 2026) and the Robinhood chain registered on the ITS Hub (Nov 2026) ([gov LCD](https://axelar-rest.publicnode.com/cosmos/gov/v1/proposals?pagination.reverse=true)).
- Interchain Amplifier, Interchain Token Service and Solana, Stellar and Hedera integrations in 2026 ([Common Prefix](https://www.commonprefix.com/blog/axelar-roadmap)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- ~$126M bridged TVL, mostly on Ethereum ($110.8M) and BSC ($10.7M) ([DefiLlama](https://defillama.com/protocol/axelar)).
- $1,780 of fees in 30 days. Three Amplifier chains were cut for having no usage.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit of the Axelar network found in this pass.
- **Thin economic security:** 262.2M AXL bonded (~$8.5M) for ~$126M bridged; 57.4M (4.6% of supply) is unbonding.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. Canary filed an S-1 for an AXL trust in Mar 2025 ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2059208/000183988225013999/canary-s1_030525.htm)). No approval was found [Unverified].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Late Nov 2026 | Core-team vesting modelled to end [Tier B] |
| Ongoing | Common Prefix roadmap: co-staking, gasless bridging, institutional products |
| Risk | Circle's Arc and CCTP, now staffed by Axelar's original builders, compete directly |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not proven; unlabelled native movers look like exchange custody |
| Live mint path | 🔴 No cap; ~3% net yearly growth |
| Treasury in single-key wallets | 🟡 Unknown; no treasury addresses published |
| Core team departure | 🔴 Interop Labs team and IP to Circle ([post](https://www.circle.com/blog/circle-signs-agreement-to-acquire-interop-labs-team-intellectual-property)) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Largest unlabelled Ethereum holder | Unknown owner | Etherscan | low | no | None: Selling stays 4 (not proven) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Axelar LCD: supply, mint inflation and params, reward params, staking pool, community pool, distribution params, governance proposals, all 207,874 `denom_owners`, account types; read 16 Nov 2026 ~9:30–9:50 AM MST
- [Tier A] Axelarscan API `searchTransactions` and `getAccountAmounts` for the largest unlabelled native accounts; Ethereum and BSC RPC `totalSupply()` of wAXL; Blockscout wAXL holder list; Etherscan name tags [Tier B]
- [Tier A] [DefiLlama Axelar](https://defillama.com/protocol/axelar) fees and TVL; CoinGecko `axelar` (16 Nov 2026 7:13 AM MST); KuCoin AXL-USDT daily candles
- [Tier A] [Circle](https://www.circle.com/blog/circle-signs-agreement-to-acquire-interop-labs-team-intellectual-property) · [Axelar blog: Circle](https://www.axelar.network/blog/circle-interop-labs-acquisition-agreement) · [Cobalt](https://www.axelar.network/blog/cobalt-tokenomics-upgrade) · [Discontinuing chains](https://www.axelar.network/blog/discontinuing-flow-berachain-plume) · [Common Prefix roadmap](https://www.commonprefix.com/blog/axelar-roadmap) · [Token economics](https://medium.com/@axelar-foundation/an-overview-of-axl-token-economics-4dc701c9054d)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): [token contract](https://intel.arkm.com/explorer/address/0x467719ad09025fcc6cf6f8311755809d45a5e5f3) (24.251K AXL) · [Upbit deposit](https://intel.arkm.com/explorer/address/0xd2ff2d432a0078672cf4f9e2e97858a33cbdeebc) (119.253M) · [`0x1a9d…`](https://intel.arkm.com/explorer/address/0x1a9d699aee3a56ca49d0cc3b542ae3a37885a3e1) (9.096M, unlabelled) · [Kraken hot wallet](https://intel.arkm.com/explorer/address/0xfcac185644e5c6cd73c309a60d2758ae56cf78b3) (8.375M) · [Paribu hot wallet](https://intel.arkm.com/explorer/address/0xc80afd311c9626528de66d86814770361fe92416) (no AXL shown). Arkham does not support the Axelar chain itself, so the native `axelar1…` accounts have no Arkham labels
- [Tier B] [MoonRunners supply](https://moon-runners.net/axelar/mainnet/supply) · [TokenRadar](https://tokenradar.ai/tokens/axelar-network/tokenomics)
- [Unverified] Foundation and company wallet balances and flows; who controls `axelar1p3uc…`, `axelar1rhfw…`, `axelar1tgjx…` and `axelar1pdw4…`; whether the Circle deal has closed; real order-book depth

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply 1.26B; bonded 262.2M; unbonding 57.4M | [supply](https://axelar-rest.publicnode.com/cosmos/bank/v1beta1/supply/by_denom?denom=uaxl) · [pool](https://axelar-rest.publicnode.com/cosmos/staking/v1beta1/pool) | A | 16 Nov 2026 |
| Mint inflation 0; 0.2% per-chain voting reward | [mint params](https://axelar-rest.publicnode.com/cosmos/mint/v1beta1/params) · [reward params](https://axelar-rest.publicnode.com/axelar/reward/v1beta1/params) | A | 16 Nov 2026 |
| Interop Labs team and IP to Circle | [Circle](https://www.circle.com/blog/circle-signs-agreement-to-acquire-interop-labs-team-intellectual-property) · [Axelar](https://www.axelar.network/blog/circle-interop-labs-acquisition-agreement) | A | 16 Nov 2026 |
| Fee burn (98%) | [Cobalt blog](https://www.axelar.network/blog/cobalt-tokenomics-upgrade) | A | 16 Nov 2026 |
| Pump-day native transfers (unattributed) | [35M 16 Apr 2026](https://axelarscan.io/tx/6C926AF3CC2F43D538E4CF762837294929245C22831557770021833031CB612E) · [29.8M 16 Apr 2026](https://axelarscan.io/tx/1AC459255CF75613C0E6B762E10E97082273B30626D559D53527B5FA630391D9) · [35.8M 10 Jun 2025](https://axelarscan.io/tx/410BF64922677D231350A485201C68FBF5285A39E6FC93CC8558EEB7C3F66FCD) | A | 16 Nov 2026 |
| Largest wAXL holders: Upbit 119.253M, `0x1a9d…` 9.096M, Kraken 8.375M; Paribu none shown | [Upbit](https://intel.arkm.com/explorer/address/0xd2ff2d432a0078672cf4f9e2e97858a33cbdeebc) · [0x1a9d](https://intel.arkm.com/explorer/address/0x1a9d699aee3a56ca49d0cc3b542ae3a37885a3e1) · [Kraken](https://intel.arkm.com/explorer/address/0xfcac185644e5c6cd73c309a60d2758ae56cf78b3) · [Paribu](https://intel.arkm.com/explorer/address/0xc80afd311c9626528de66d86814770361fe92416) | B (Arkham) | 16 Nov 2026 |
| Bridge escrow 345.06M | [account](https://axelarscan.io/account/axelar1jesak80ju7yw09pncdz7r2myg3jwz8a66yhm7dwrvqz7xhmvdndqx095sm) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the large native accounts** | Arkham does not cover the Axelar chain. Check Mintscan / Axelarscan labels for `axelar1p3uc…`, `axelar1rhfw…`, `axelar1tgjx…` and `axelar1pdw4…`, or ask the Foundation | Free |
| 2 | **Who owns `0x1a9d…` (9.096M wAXL)?** | Arkham shows no owner (16 Nov 2026). Watch it for exchange deposits on pump days | Free |
| 3 | **Foundation and company treasury** | Ask the Axelar Foundation to publish its treasury addresses and the remaining company allocation | Free |
| 4 | **Did the Circle deal close, and who holds the old company's AXL?** | Check Circle's filings (10-Q / 10-K) for the Interop Labs closing | Free |
| 5 | **Real liquidity** | Pull live order books from Binance, Upbit and HTX and measure ±2% depth | Free (needs a non-blocked network) |
| 6 | **Pump-test Foundation wallets** | Once labelled, run native sends through the KuCoin pump map | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
