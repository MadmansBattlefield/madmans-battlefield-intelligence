---
ticker: CELO
name: Celo
not_to_be_confused_with: "stCELO, mCELO or Mento stablecoins (USDm, EURm)"
chain: celo (Ethereum L2, OP Stack)
contract: "0x471ece3750da237f93b8e339c536989b8978a438"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 5
  liquidity_market: 4
  product_development: 7
  adoption_customers: 6
  security_audits: 6
  regulatory: 4
  catalysts: 5
gates_failed: [revenue]
red_lines:
  funded_wallet_to_exchange_on_pump_day: tripped
  revenue_burn_not_active: open
  hack_exploit: none_found
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Some fees now buy CELO, but it lands in a governance-spent treasury, not burned or paid out."
pump_day_price_source: "Gate CELO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (27 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: buried_disclosure
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.060813
price_source: "CoinGecko celo, 15 Nov 2026 6:47 AM MST"
chain_read_block: 82850691
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### CELO · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** A busy stablecoin chain (MiniPay reports 20M+ wallets) that earns almost nothing for the token. The chain took about $594k in fees over 12 months, and Safes funded through a governance contractor's allowance paid about 9.3M CELO straight into a Binance deposit address since August, including on two pump days. The token is down 70% in a year.

**🚨 Top warning (red line):** Governance-funded Safes paid by the CICLOPS contractor sent **9.26M CELO straight into Binance deposit address** [`0x1b20…9202`](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) (21 Aug – 6 Nov 2026), including **575,000 CELO on the 21 and 24 Aug pump days**. Check: [21 Aug send](https://celo.blockscout.com/tx/0xf86a65ec5089fac79b08488259d6c725f4795e75c9f48a14c9c5f96c82651235) → [sweep to Binance](https://celo.blockscout.com/tx/0xbbe62518e940ceccfc2e373fb05a27d253e9721327d41ae932bf48d2a2b620e5) · [24 Aug send](https://celo.blockscout.com/tx/0x3d59c43be1791069f0ac9d1767cbc4d07ff0fbc753d18f7ae79edda0dbff8b06) → [sweep](https://celo.blockscout.com/tx/0xb5bf335048b5cb98841b2f0822de59d20ecc053b617e45256930fd3103aa65ae) · [Arkham “Binance Deposit”](https://intel.arkm.com/explorer/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) · [deposit address on Celo Blockscout](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202). Note: that deposit address takes coins from 36 senders, so the 97.8M swept since 2023 is **not** one team's selling.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 CELO · Celo · 4.7 / 10 · ❌ FAIL

> **One line:** A busy stablecoin chain (MiniPay reports 20M+ wallets) that earns almost nothing for the token. The chain took about $594k in fees over 12 months, and Safes funded through a governance contractor's allowance paid about 9.3M CELO straight into a Binance deposit address since August, including on two pump days. The token is down 70% in a year.

ℹ️ **Adapted for an L2 gas and governance token.** "Revenue" = sequencer fees and what reaches CELO. "Foundation" = Celo Core Co. (the merged Celo Foundation and cLabs) plus the on-chain Community Fund. "Holdings / Selling" = governance treasuries and the multisigs they fund.

| 📊 Market (CoinGecko, 15 Nov 2026 6:47 AM MST) | 🔗 On-chain (forno.celo.org, block 82,850,691) |
|---|---|
| **Price** $0.06081 | **Token** GoldToken [`0x471EcE37…a438`](https://celo.blockscout.com/address/0x471EcE3750Da237f93B8E339c536989b8978a438) (native CELO, ERC-20 view) |
| **24h / 7d / 30d / 1y** 🔴 −3.7% / −6.1% / −30.2% / −70.3% | **totalSupply()** 1,000,000,000 (cap) |
| **Market cap** $37.09M · **FDV** $60.81M · rank #506 | **Circulating (CoinGecko)** 609,975,347 (61%) |
| **24h volume** $4.36M on 71 tickers | **Community Fund** 77,858,505 · **Unreleased Treasury** 53,107,947 |
| **ATH** $9.82 (30 Aug 2021) · now **−99.4%** | **Locked (staked)** 81,640,196 · **Burned (0xdEaD)** 241,375 |
| **Chain TVL** $13.43M (DefiLlama) | **Old Celo Reserve** [`0x9380fA34…`](https://celo.blockscout.com/address/0x9380fA34Fd9e4Fd14c06305fd7B6199089eD4eb9) holds **0 CELO** |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric (DefiLlama `celo` chain fees) | Value | Source |
|---|---:|---|
| Fees, last 24h / 7d / 30d | $2,828 / $20,644 / $72,403 | [Tier A] DefiLlama |
| **Fees, 12 months** | **$594,471** | [Tier A] |
| Fees, all-time (since May 2020) | $1,601,454 | [Tier A] |
| Fees by month | Nov '25 $28.3k · Dec $20.2k · Jan $21.4k · Feb $17.6k · Mar $16.4k · Apr $26.2k · **May $99.9k** · Jun $58.3k · Jul $66.7k · Aug $62.8k · Sep $78.9k · Oct $76.4k · Nov 1–14 $37.5k | [Tier A] |
| DefiLlama "revenue" | $24,956, all of it in Nov 2026 (series starts 27 Apr 2026) | [Tier A] |
| Holders revenue | **$0** | [Tier A] |
| Fees vs market cap | ~1.6% a year | Calculated |

**Where the money goes** ([Tier A] [CGP-0233 CELOccelerate](https://forum.celo.org/t/celoccelerate-celo-tokenomics-proposal/13147), executed 15 Apr 2026; [Tier A] [Mondo buyback page](https://mondo.celo.org/buyback)):
- After costs (OP Stack share, EigenDA, Succinct, L1 posting), **net sequencer revenue buys CELO for the Community Fund**. Stablecoin fees are used to buy CELO at market once a day.
- First ongoing transfer: **2,566,770 CELO** for 9 Apr – 17 Jun 2026, from about **$90,199** of stablecoin fees ([Tier A] [forum post](https://forum.celo.org/t/initiating-ongoing-celo-chain-revenue-transactions/13494)).
- Celo Core Co. returned 1,748,950 CELO of earlier sequencer fees on 1 Apr 2026. The proposal to **burn** it (CGP-0234) **expired without passing** ([Tier A] celo-org/governance).
- A 25% burn of future net revenue (CGP-0257) is still a **DRAFT** ([Tier A] celo-org/governance, PR #848).
- 0xdEaD holds only 241,375 CELO.

**What it means:** The chain does about $70k a month in fees. Some of it now buys CELO, but it lands in a treasury that governance spends, not burns, so holders get little.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Some fees now buy CELO, but it lands in a governance-spent treasury, not burned or paid out.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Core organization | **Celo Core Co.**, formed when the Celo Foundation and cLabs merged (announced 20 Jan 2026, "CELOmorphosis") | [Tier A] [Celo Foundation Season 2 retrospective](https://forum.celo.org/t/season-2-celo-foundation-retrospective/13524) · [Tier A] [Season 3 funding proposal](https://forum.celo.org/t/celo-core-co-season-3-funding-proposal/13565) |
| CEO | Marek Olszewski (co-founder) | [Tier B] Consensus 2026 speaker page + Celo Core Co. LinkedIn post (two sources) |
| Funding model | Six-month "seasons" paid in CELO from the Community Fund by on-chain vote. Season 3 (CGP-0247, executed 6 Aug 2026): **$2,396,000 = 31,609,499 CELO** at a $0.0758 90-day average | [Tier A] CGP-0247 |
| Celo Core Co. multisig | [`0xB0D0780eDDC2FA35906C0b37B9b4Dc7583C3DbB0`](https://celo.blockscout.com/address/0xB0D0780eDDC2FA35906C0b37B9b4Dc7583C3DbB0) — Safe, **3 of 5** — published in the proposal | [Tier A] forum + RPC |
| Other funded teams | CICLOPS infra (CGP-0231: $2.7M = 21,738,286 CELO, Season 2; **3-of-6** multisig [`0xd71efa41…F09E`](https://celo.blockscout.com/address/0xd71efa410B6EaAB0bAc3b515B393C886BE70F09E), published in CGP-0237); Governance Guild (CGP-0250); Stabila (CGP-0246) | [Tier A] celo-org/governance |
| Governance | On-chain CELO votes; all proposals public on GitHub `celo-org/governance` | [Tier A] |
| Legal entity of Celo Core Co. | Not found this pass | Not found |

**What it means:** Spending is public and voted on chain, and the core team's wallet is named. The core team is also paid in the token it stewards, so it has to sell CELO to cover costs.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

Live reads, 15 Nov 2026 (block 82,850,691):

| Wallet | Role | CELO | % of supply | Control |
|---|---|---:|---:|---|
| [`0xD533Ca259b330c7A88f74E000a3FaEa2d63B7972`](https://celo.blockscout.com/address/0xD533Ca259b330c7A88f74E000a3FaEa2d63B7972) | **Community Fund** (Governance contract) | 77,858,505 | 7.79% | On-chain vote |
| [`0x7a8C7A833565fC428cdfba20Fe03FAFB178A434f`](https://celo.blockscout.com/address/0x7a8C7A833565fC428cdfba20Fe03FAFB178A434f) | CeloUnreleasedTreasury (future emissions) | 53,107,947 | 5.31% | Protocol / governance |
| [`0xB0D0780e…DbB0`](https://celo.blockscout.com/address/0xB0D0780eDDC2FA35906C0b37B9b4Dc7583C3DbB0) | **Celo Core Co. multisig** | 27,609,499 | 2.76% | 3-of-5 Safe, liquid |
| [`0x6cC083Aed9e3ebe302A6336dBC7c921C9f03349E`](https://celo.blockscout.com/address/0x6cC083Aed9e3ebe302A6336dBC7c921C9f03349E) | LockedGold (all stakers) | 81,640,196 | 8.16% | Holders |
| [`0x9380fA34Fd9e4Fd14c06305fd7B6199089eD4eb9`](https://celo.blockscout.com/address/0x9380fA34Fd9e4Fd14c06305fd7B6199089eD4eb9) | Old Celo/Mento Reserve | **0** | 0% | 43.0M CELO moved to the Community Fund by CGP-0231 |
| [`0x0f293B15…68C9`](https://celo.blockscout.com/address/0x0f293B1548a55a7ba9541d4c27442e1591B068C9) | Celo Foundation multisig (CGP-0200/0224) | 0 | 0% | 3-of-5 Safe |
| CICLOPS multisig [`0xd71efa41…F09E`](https://celo.blockscout.com/address/0xd71efa410B6EaAB0bAc3b515B393C886BE70F09E) | Infra contractor | 0 — but a **37,597,705 CELO allowance** on the Community Fund is still open | — | 3-of-6 Safe |

- **Governance-controlled CELO: ~131M (13.1%)** plus the 27.6M Core Co. holds and the 37.6M CICLOPS can still pull.
- **Supply gap:** totalSupply is 1.00B but CoinGecko counts 610M circulating. About 390M is not accounted for by the wallets above (the old Foundation-era treasuries are only partly mapped). **[Unverified]**.
- Mento reserve today: $16.05M collateral behind $14.1M of reserve-backed stablecoins (ratio 1.14); its CELO share not read ([Tier A] [reserve.mento.org](https://reserve.mento.org)).

**What it means:** Insiders and governance control a large, liquid stack that is spent every six months, and a big slice of supply can't yet be mapped to wallets.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **25 of 360 days** were pump days (clusters 21–26 Aug and 20–23 Sep 2026).

### A. CICLOPS funding → Safes → Binance deposit address

| Step | Finding | Source |
|---|---|---|
| 1 | Community Fund → [`0x702348eA…3658`](https://celo.blockscout.com/address/0x702348eA947e7E4849105AC55c928fC0490F3658) (Safe, 2 of 4): 10,869,143 + 1,897,469 CELO on 6 Apr 2026 and 7,910,673 on 29 May — **all executed by the CICLOPS multisig** `0xd71efa41…` pulling its approved allowance | [Tier A] Blockscout [tx `0xca1ca841…`](https://celo.blockscout.com/tx/0xca1ca84151e7fbff91149fd74c857c4318cbbfec19dedd024f43b5fc0af75b98), [tx `0xdcad5eac…`](https://celo.blockscout.com/tx/0xdcad5eacd98e90ed2bd6dbb1b6e826f7efa24e0540f7e77cf2ebc7bd3f2df2b3), [tx `0xef4a1741…`](https://celo.blockscout.com/tx/0xef4a1741ec6a9037448aab4e82c960adf2c0e664bec9f9b3dc4d1e8627de51da) |
| 2 | `0x702348…` sent: 14,944,640 CELO to EOA [`0x0E17c935…7D19`](https://celo.blockscout.com/address/0x0E17c9352CC02A1C9d6aE517153C91c2df587D19) (29 sends, Jul 2025 – Jul 2026) · 9,203,070 to Safe [`0x2fb70f05…ce1`](https://celo.blockscout.com/address/0x2fb70f0585E23E16add864fa07E8220135238ce1) (2 of 4; 3 sends, 2 Jul – 10 Sep 2026) · 5,517,212 to [`0xc731e70c…`](https://celo.blockscout.com/address/0xc731e70c03a2a5958A0470896f37E9a5cdAc5dce) (18 Jun 2026) · **1,505,010 to EOA [`0x1b20B200…9202`](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) (6 sends, 21 Aug – 4 Sep 2026: [21 Aug](https://celo.blockscout.com/tx/0xf86a65ec5089fac79b08488259d6c725f4795e75c9f48a14c9c5f96c82651235), [24 Aug](https://celo.blockscout.com/tx/0x3d59c43be1791069f0ac9d1767cbc4d07ff0fbc753d18f7ae79edda0dbff8b06), [27 Aug](https://celo.blockscout.com/tx/0xebceb3dbb27cb437bd5a7923209abe28a6d403ca5270c02437ba823c56ffc6f4), [2 Sep](https://celo.blockscout.com/tx/0x555027907a9269daf8a23932408db6e378c029243e855445837f4932ffa24ff8), [4 Sep](https://celo.blockscout.com/tx/0xd6a2cfd0252a52d66bb188b8d74851debedb810ec7f980e8d760453e9c31d5f7))** | [Tier A] |
| 3 | Safe `0x2fb70f…` **also feeds `0x1b20B200…`**: **7,753,762 CELO in 15 sends, 10 Sep – 6 Nov 2026** (first [10 Sep](https://celo.blockscout.com/tx/0xe6c4d6ca5845512b50965a299a324aa9d6da31c39ebc776bea0d7aa01236fd29); largest 1,500,000 on 4 Nov, [tx](https://celo.blockscout.com/tx/0x3bd5c198c289380e68c83cfab031c81897017777e26b2c66adea9440d0a6894e); last [6 Nov](https://celo.blockscout.com/tx/0x169adcd29a58d2d0497aa15603617c796b498b43f13810a66a1ff45c84636a66)). None on a pump day | [Tier A] Blockscout token transfers, read 15 Nov 2026 ~10:50 AM MST |
| 4 | [`0x1b20B200…`](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) is a **Binance deposit address**: Arkham labels it "Binance Deposit" ([Arkham](https://intel.arkm.com/explorer/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202)), and on-chain it passes on everything it receives (100,059,359 CELO in from 36 senders since 27 Jan 2023; 97,840,607 out to [`0xf6436829…C4ED`](https://celo.blockscout.com/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED) in 70 sweeps, 2,218,752 to [`0x6247ffEe…1F09`](https://celo.blockscout.com/address/0x6247ffEe0Ca3f0e63fe3e160f4503d565FB11F09) on 10 Nov 2026 ([tx `0x8568ed62…`](https://celo.blockscout.com/tx/0x8568ed62e806db567a8c9d322442db3870036d4ec5a01f033488d0113e1f8b4f)), nothing kept) | [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST (one label, read from the same address on other EVM chains; Arkham does not support Celo) · [Tier A] Blockscout flows |
| 5 | [`0xf6436829…C4ED`](https://celo.blockscout.com/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED) is **Binance**: Blockscout tags it "Tether: Binance" and Arkham separately labels it "Binance" (Proof of Reserves; [Arkham](https://intel.arkm.com/explorer/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED)). It has made ~1.92M transactions on Celo | ✅ Two independent Tier B labels · [Tier A] nonce |
| **Pump days** | 21 Aug 2026: 300,000 (Safe `0x702348…` → Binance deposit `0x1b20…` 7:09 AM MST, [send](https://celo.blockscout.com/tx/0xf86a65ec5089fac79b08488259d6c725f4795e75c9f48a14c9c5f96c82651235); swept to Binance 7:32 AM MST, [sweep](https://celo.blockscout.com/tx/0xbbe62518e940ceccfc2e373fb05a27d253e9721327d41ae932bf48d2a2b620e5)) · 24 Aug 2026: 275,000 (8:52 → 9:13 AM MST; [send](https://celo.blockscout.com/tx/0x3d59c43be1791069f0ac9d1767cbc4d07ff0fbc753d18f7ae79edda0dbff8b06) → [sweep](https://celo.blockscout.com/tx/0xb5bf335048b5cb98841b2f0822de59d20ecc053b617e45256930fd3103aa65ae)) — **575,000 CELO ≈ $42k at the time** (CoinGecko daily price ~$0.067–0.078). These are the only pump-day deposits into `0x1b20…` from any sender in the 12-month window | [Tier A] |
| Other pump-day sends from `0x702348…` | 310,000 (2 Jul) and 500,000 (11 May) to EOA `0x0E17c935…7D19`, which forwards to [`0x2d880CCC…`](https://celo.blockscout.com/address/0x2d880CCC788AAa6DbdEaAd3B585f8C533C6BE54C). Arkham has **no entity** for either ([0x0E17…](https://intel.arkm.com/explorer/address/0x0E17c9352CC02A1C9d6aE517153C91c2df587D19) · [0x2d88…](https://intel.arkm.com/explorer/address/0x2d880CCC788AAa6DbdEaAd3B585f8C533C6BE54C)). On other EVM chains both trade in size with exchanges and Circle (`0x0E17…`: ~$58.8M sent to Circle, ~$87.7M received from Circle; `0x2d88…`: $177.6M sent to Binance, Coinbase, Gate and others, $368M received). That is the profile of a trading, OTC or payments firm, not a retail wallet. Owner Not found | [Tier A] Celo flows · [Tier B] Arkham, read 15 Nov 2026 ~10:40 AM MST (other chains only) |

- CGP-0231 says CICLOPS funds "will be used exclusively to pay infrastructure vendors", so turning CELO into cash is disclosed in purpose. The wallets and the timing were not disclosed.
- **Total straight to Binance from CICLOPS-funded Safes:** 1,505,010 (`0x702348…`) + 7,753,762 (`0x2fb70f…`) = **9,258,772 CELO ≈ $748k** at daily closes, 21 Aug – 6 Nov 2026 ([Tier A] Blockscout; value calculated).
- **What the Binance labels change:** the sale point is the deposit into `0x1b20…`, not the later sweep. The **97.8M CELO swept since 2023 is not one team's selling**: it is everything 36 senders paid into one Binance deposit address. The CICLOPS-funded Safes supplied 9.26M of it (9.3%). The largest other senders (`0x6a849df3…` 17.0M, `0x6dec25d7…` 13.45M, `0x2c2d845f…` 12.8M, `0x87647780…` 11.0M) are not linked to Celo governance this pass.
- **Who receives the money:** an exchange deposit address normally belongs to one customer account, so these Safes and the other senders all pay the **same Binance customer**. That could be CICLOPS itself, a vendor or an OTC desk. Not found.
- **How far the cross-chain labels reach:** `0x1b20…`, `0xf643…`, `0x0E17…`, `0x2d88…` and `0x6247…` are all plain key-held accounts on Celo (no contract code; [Tier A] RPC). A key-held address is controlled by the same key on every EVM chain, and exchanges commonly reuse one deposit address across EVM chains, so Arkham's Ethereum and other-chain labels very likely carry over to Celo. It is still an inference, so single Arkham labels stay Tier B, one source.
- `0x6247ffEe…1F09`, which got the last 2.22M from `0x1b20…`, holds ~1.18M CELO and makes many small payouts (1,255 transactions). It behaves like an exchange hot wallet, possibly Binance's, but has no label [Unverified].

### B. Other team wallets

| Wallet | Finding |
|---|---|
| Celo Core Co. multisig | Received 31,609,498 on 23 Oct 2026; one send since: **4,000,000 to Safe [`0x16864253…`](https://celo.blockscout.com/address/0x16864253e0aB1D3E6844C24896899F99e5272E7C)** on 29 Oct (not a pump day), which pays out small grants (e.g. 20+ payments of about 1k–24k CELO on 13 Nov) |
| Celo Foundation multisig `0x0f293B15…` | 1.0M (Oct 2025) and 400k (Nov 2025) to EOA `0x0E17c935…`; 2.0M–5.3M to other Safes in 2026. **No pump-day send found** |

**What it means:** The pattern looks like a steady budget sell-down, not a team timing pumps, and the reason for selling is disclosed. The new labels make the exchange route firmer (a 2-of-4 Safe paying straight into a Binance deposit address), show more of the budget reaching Binance (9.26M CELO), and show that the 97.8M swept since 2023 is not all team money. They add no new pump-day sends: still 575k CELO on 21 and 24 Aug. Under this layout's rule that is a fail, though not a gate-level one. Score unchanged at 5/10.

- **Disclosure quality (16 Nov 2026 rules): buried disclosure.** The budget sell-down is approved in governance, but these sends are not itemised, so disclosure is partial and no penalty applies; Selling stays 5. 21 and 24 Aug 2026 are still pump days on Gate prices. Pump days from Gate CELO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (27 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Cap | 1,000,000,000 (`totalSupply()` returns the cap) | [Tier A] RPC |
| Circulating | 609,975,347 (61%) | [Tier B] CoinGecko |
| Future emissions | 53.1M in CeloUnreleasedTreasury (epoch rewards) | [Tier A] RPC |
| Treasury spending | ~$2.4M (Core Co.) + ~$2.7M (CICLOPS) per season, paid in CELO at a 90-day average price, so a falling price means more CELO paid out | [Tier A] CGPs 0231, 0247 |
| Reserve drain | 43,012,777 CELO moved from the Governance Reserve to the Community Fund (CGP-0231) because the Fund "has insufficient balance" | [Tier A] |
| Burns | Only ad hoc; the 1.75M burn expired; the 25% revenue burn is a draft | [Tier A] |
| Carbon fund payments | Paused: carbon share of fees (10%) set to zero (CGP-0236, executed 9 May 2026) | [Tier A] |

## 💧 Liquidity & market · 4/10 · ❌ FAIL

| Venue (15 Nov 2026) | Pair | 24h volume / liquidity | Source |
|---|---|---:|---|
| HTX | CELO/USDT | $917k vol | [Tier B] CoinGecko |
| Uniswap v3 (Celo) `0x6cde5f5a…` | USDT/CELO | **$169,586 liq** · $771,883 vol · 19,250 txns | [Tier A] DexScreener |
| WhiteBIT | CELO/USDT | $683k vol | [Tier B] |
| Binance | CELO/USDT | $493k vol | [Tier B] |
| Upbit | CELO/KRW | $306k vol | [Tier B] |
| Uniswap stCELO/CELO | | $575,691 liq · $112 vol | [Tier A] DexScreener |
| All 30 DEX pairs | | $1,042,917 liq | [Tier A] |

**Order-book depth within ±2% (public APIs, 15 Nov 2026 ~7:00 AM MST):** OKX bids **$8,797** / asks $6,808 · Kraken bids **$12,521** / asks $9,269. Binance and Bybit books were blocked from this network (HTTP 451/403).

**What it means:** About $4M of daily volume, but only around $10k of bids sit within 2% on the books checked. A $25k sale would move the price noticeably.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

| Item | Detail | Source |
|---|---|---|
| L2 migration | Celo runs as an OP Stack Ethereum L2 (since Mar 2025) | [Tier A] Celo docs / old draft |
| Upgrades | Jello hardfork with OP Succinct Lite ZK fault proofs (10 Dec 2025); Jovian hardfork (31 Mar 2026) | [Unverified] from old draft sources, not re-fetched |
| GitHub | `celo-org/optimism` **337 commits** in 90 days, pushed 13 Nov 2026 · `celo-org/op-geth` 118 commits (release `celo-v2.2.5`, 18 Aug) · `celo-org/celo-monorepo` 23 commits | [Tier A] GitHub API |
| Mento | `mento-protocol/mento-core` last push 24 Jul 2026 | [Tier A] GitHub API |
| Roadmap | Espresso fast confirmations: "major headway", work continues into H2 2026, no date given | [Tier A] H2 2026 roadmap post |

## 🤝 Adoption & customers · 6/10 · ✅ PASS

| Claim | Status | Source |
|---|---|---|
| MiniPay (Opera): **20M+ wallet activations, 600M+ transactions, $2.3B+ volume, 70+ countries, 77 Mini Apps** (since launch, as of Q3 2026) | Self-reported by the official forum | [Tier A] [MiniPay Q3 2026 update](https://forum.celo.org/t/minipay-update-q3-2026/13926) |
| 4.78M CELO staked via MiniPay; 386k CELO paid to Opera users in Q3 | Self-reported | [Tier A] same |
| Opera moving from distribution partner to network stakeholder | ✅ Executed vote (CGP-0232, 29 Mar 2026) | [Tier A] |
| USDT weekly active users all-time high of 5M | Self-reported | [Tier A] Season 2 retrospective |
| Bridge (a Stripe company) added Celo support | Self-reported | [Tier A] Season 2 retrospective · [Unverified] by Bridge |
| Payments are in USDT, not CELO | CELO is only gas and governance | [Tier A] |

**What it means:** Real users, mostly moving stablecoins. Fees are tiny because transactions cost fractions of a cent, so usage barely touches CELO.

## 🛡️ Security & audits · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Hacks / exploits | None found | [Tier A] (absence) |
| Multisigs | Core Co. 3/5 · Foundation 3/5 · CICLOPS 3/6 · onward Safes 2/4 | [Tier A] RPC |
| Fault proofs | OP Succinct Lite (ZK) since the Jello fork | [Unverified] not re-fetched |
| L2 risk rating | Not checked on L2BEAT this pass | Not found |

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- No regulatory filing for CELO found this pass. The EU MiCA register, US filings and Celo Core Co.'s legal entity were not checked, and under the method that counts as a fail.
- MiniPay KYC runs through partners (Sumsub Reusable KYC Gateway); MiniPay says it never stores documents ([Tier A] Q3 update).

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Open | CGP-0257: burn 25% of net sequencer revenue (DRAFT) | Small supply ↓ if passed |
| Open | CGP-0256: fix USA₮ and XAU₮0 fee distribution in the FeeHandler (PROPOSED) | Housekeeping |
| Dec 2026 | Season 3 ends; Season 4 funding requests | More CELO spent / sold |
| Any time | CICLOPS can pull up to 37.6M CELO from its open allowance | Sell pressure |
| H2 2026 (no date) | Espresso fast confirmations | Product news |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Governance-funded wallet sends to an exchange on a pump day | 🔴 **Tripped** | 21 and 24 Aug 2026, 575k CELO from Safe [`0x702348…`](https://celo.blockscout.com/address/0x702348eA947e7E4849105AC55c928fC0490F3658) into Binance deposit address [`0x1b20B200…`](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) ([21 Aug](https://celo.blockscout.com/tx/0xf86a65ec5089fac79b08488259d6c725f4795e75c9f48a14c9c5f96c82651235) · [24 Aug](https://celo.blockscout.com/tx/0x3d59c43be1791069f0ac9d1767cbc4d07ff0fbc753d18f7ae79edda0dbff8b06) · [Arkham label](https://intel.arkm.com/explorer/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202); Binance confirmed by Blockscout + Arkham) |
| Revenue burn active | 🟡 Open | CGP-0234 expired; CGP-0257 still a draft |
| Hack / exploit | 🟢 None found | |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| 2-of-4 Safe → Binance deposit | Celo budget Safe | Etherscan + Arkham labels | high | yes (on-chain) | Selling: 575k CELO on 21 and 24 Aug 2026 pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Celo RPC `forno.celo.org`: Registry `0x…ce10` lookups, `balanceOf`, `totalSupply`, Safe owners/thresholds, Community Fund allowance; 15 Nov 2026, block ~82.85M
- [Tier A] Celo Blockscout API v2: CELO token transfers and transactions for the Community Fund, Core Co., Foundation, CICLOPS and onward wallets
- [Tier A] GitHub `celo-org/governance` (CGPs 0200, 0224, 0231–0237, 0246, 0247, 0250, 0256, 0257; PR #848) and GitHub API for repo activity
- [Tier A] Celo forum: [CELOccelerate](https://forum.celo.org/t/celoccelerate-celo-tokenomics-proposal/13147) · [revenue transfers](https://forum.celo.org/t/initiating-ongoing-celo-chain-revenue-transactions/13494) · [25% burn FINAL](https://forum.celo.org/t/final-revenue-based-celo-burn-allocate-25-of-net-l2-sequencer-revenue-to-permanent-burn/13727) · [Core Co. Season 3](https://forum.celo.org/t/celo-core-co-season-3-funding-proposal/13565) · [Foundation Season 2 retro](https://forum.celo.org/t/season-2-celo-foundation-retrospective/13524) · [MiniPay Q3 2026](https://forum.celo.org/t/minipay-update-q3-2026/13926) · [H2 2026 roadmap](https://forum.celo.org/t/h1-2026-engineering-retro-h2-2026-roadmap/13528)
- [Tier A] [Mondo buyback page](https://mondo.celo.org/buyback) · [Mento reserve](https://reserve.mento.org)
- [Tier A] DefiLlama `celo` fees / revenue / chain TVL API, to 14 Nov 2026
- [Tier A] DexScreener token-pairs API; OKX and Kraken public order books, 15 Nov 2026
- [Tier B] CoinGecko `celo` market data and 365 daily closes, 15 Nov 2026 6:47 AM MST
- [Tier B] Consensus 2026 speaker page and Celo Core Co. LinkedIn post (CEO, merger date)
- [Tier A] Celo Blockscout token transfers for `0x1b20B200…` (all 192 CELO transfers, 2023–2026) and `0x6247ffEe…`; Celo RPC `eth_getCode` / nonce for `0x1b20…`, `0xf643…`, `0x0E17…`, `0x2d88…`, `0x6247…`; 15 Nov 2026 ~10:50 AM MST
- [Tier B] Arkham Intelligence, read 15 Nov 2026 ~10:40 AM MST (signed-in account): `0x1b20…` "Binance Deposit", `0xf643…` "Binance" (Proof of Reserves), no entity for `0x0E17…`, `0x2d88…`, `0x6247…`. Arkham does not support Celo; all its labels and flows come from the same addresses on other EVM chains
- [Tier A] Explorer pages used (Celo Blockscout): Community Fund [`0xD533…`](https://celo.blockscout.com/address/0xD533Ca259b330c7A88f74E000a3FaEa2d63B7972) · Core Co. [`0xB0D0…`](https://celo.blockscout.com/address/0xB0D0780eDDC2FA35906C0b37B9b4Dc7583C3DbB0) · CICLOPS [`0xd71e…`](https://celo.blockscout.com/address/0xd71efa410B6EaAB0bAc3b515B393C886BE70F09E) · [`0x7023…`](https://celo.blockscout.com/address/0x702348eA947e7E4849105AC55c928fC0490F3658) · [`0x2fb7…`](https://celo.blockscout.com/address/0x2fb70f0585E23E16add864fa07E8220135238ce1) · [`0x1b20…`](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) · [`0xf643…`](https://celo.blockscout.com/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED) · [`0x6247…`](https://celo.blockscout.com/address/0x6247ffEe0Ca3f0e63fe3e160f4503d565FB11F09) · [`0x0E17…`](https://celo.blockscout.com/address/0x0E17c9352CC02A1C9d6aE517153C91c2df587D19) · [`0x2d88…`](https://celo.blockscout.com/address/0x2d880CCC788AAa6DbdEaAd3B585f8C533C6BE54C) · Foundation [`0x0f29…`](https://celo.blockscout.com/address/0x0f293B1548a55a7ba9541d4c27442e1591B068C9)
- [Tier B] Arkham address pages used (EVM data from other chains): [0x1b20…](https://intel.arkm.com/explorer/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) · [0xf643…](https://intel.arkm.com/explorer/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED) · [0x0E17…](https://intel.arkm.com/explorer/address/0x0E17c9352CC02A1C9d6aE517153C91c2df587D19) · [0x2d88…](https://intel.arkm.com/explorer/address/0x2d880CCC788AAa6DbdEaAd3B585f8C533C6BE54C) · [0x6247…](https://intel.arkm.com/explorer/address/0x6247ffEe0Ca3f0e63fe3e160f4503d565FB11F09)
- [Unverified] Binance customer behind deposit address `0x1b20B200…` (and the deposit label itself, one source); owners of `0x0E17c935…`, `0x2d880CCC…`, `0x6247ffEe…`; 390M supply gap; Jello/Jovian dates; Celo Core Co. legal entity

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Community Fund → Safe `0x7023…` (CICLOPS pulled its allowance): 10.87M + 1.90M + 7.91M CELO | [tx 1](https://celo.blockscout.com/tx/0xca1ca84151e7fbff91149fd74c857c4318cbbfec19dedd024f43b5fc0af75b98) · [tx 2](https://celo.blockscout.com/tx/0xdcad5eacd98e90ed2bd6dbb1b6e826f7efa24e0540f7e77cf2ebc7bd3f2df2b3) · [tx 3](https://celo.blockscout.com/tx/0xef4a1741ec6a9037448aab4e82c960adf2c0e664bec9f9b3dc4d1e8627de51da) · [Community Fund](https://celo.blockscout.com/address/0xD533Ca259b330c7A88f74E000a3FaEa2d63B7972) · [CICLOPS multisig](https://celo.blockscout.com/address/0xd71efa410B6EaAB0bAc3b515B393C886BE70F09E) | A | 15 Nov 2026 |
| **Pump-day deposits:** 300,000 (21 Aug) + 275,000 (24 Aug 2026) CELO from `0x7023…` into Binance deposit `0x1b20…`, each swept to Binance within ~21–23 min | [21 Aug send](https://celo.blockscout.com/tx/0xf86a65ec5089fac79b08488259d6c725f4795e75c9f48a14c9c5f96c82651235) · [21 Aug sweep](https://celo.blockscout.com/tx/0xbbe62518e940ceccfc2e373fb05a27d253e9721327d41ae932bf48d2a2b620e5) · [24 Aug send](https://celo.blockscout.com/tx/0x3d59c43be1791069f0ac9d1767cbc4d07ff0fbc753d18f7ae79edda0dbff8b06) · [24 Aug sweep](https://celo.blockscout.com/tx/0xb5bf335048b5cb98841b2f0822de59d20ecc053b617e45256930fd3103aa65ae) | A | 15 Nov 2026 ~10:50 AM MST |
| **9,258,772 CELO from CICLOPS-funded Safes straight to the Binance deposit** (21 Aug – 6 Nov 2026) | [0x7023… transfers](https://celo.blockscout.com/address/0x702348eA947e7E4849105AC55c928fC0490F3658) · [0x2fb7… transfers](https://celo.blockscout.com/address/0x2fb70f0585E23E16add864fa07E8220135238ce1) · examples [4 Sep](https://celo.blockscout.com/tx/0xd6a2cfd0252a52d66bb188b8d74851debedb810ec7f980e8d760453e9c31d5f7) · [4 Nov 1.5M](https://celo.blockscout.com/tx/0x3bd5c198c289380e68c83cfab031c81897017777e26b2c66adea9440d0a6894e) · [6 Nov](https://celo.blockscout.com/tx/0x169adcd29a58d2d0497aa15603617c796b498b43f13810a66a1ff45c84636a66) | A | 15 Nov 2026 |
| `0x1b20…` is a Binance deposit address (36 senders, 100.06M in, swept to Binance) | [Celo Blockscout](https://celo.blockscout.com/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) · [Arkham “Binance Deposit”](https://intel.arkm.com/explorer/address/0x1b20B200a78C6068cE5ea96226D1B53E0A119202) | A pattern + one B | 15 Nov 2026 |
| `0xf643…` is Binance (Blockscout "Tether: Binance" + Arkham "Binance") | [Celo Blockscout](https://celo.blockscout.com/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED) · [Arkham](https://intel.arkm.com/explorer/address/0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED) | 2× B | 15 Nov 2026 |
| `0x0E17…` / `0x2d88…` trade heavily with exchanges and Circle on other chains; no Arkham entity | [0x0E17…](https://celo.blockscout.com/address/0x0E17c9352CC02A1C9d6aE517153C91c2df587D19) · [0x2d88…](https://celo.blockscout.com/address/0x2d880CCC788AAa6DbdEaAd3B585f8C533C6BE54C) · [Arkham 0x0E17…](https://intel.arkm.com/explorer/address/0x0E17c9352CC02A1C9d6aE517153C91c2df587D19) · [Arkham 0x2d88…](https://intel.arkm.com/explorer/address/0x2d880CCC788AAa6DbdEaAd3B585f8C533C6BE54C) | A + B | 15 Nov 2026 |
| Community Fund holds 77,858,505 CELO; Core Co. multisig 27,609,499 | [Community Fund](https://celo.blockscout.com/address/0xD533Ca259b330c7A88f74E000a3FaEa2d63B7972) · [Core Co. Safe](https://celo.blockscout.com/address/0xB0D0780eDDC2FA35906C0b37B9b4Dc7583C3DbB0) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | How to close it | Access needed |
|---|---|---|---|
| 1 | **Narrowed:** `0x1b20B200a78C6068cE5ea96226D1B53E0A119202` is a Binance deposit address (Arkham + sweep pattern), so Binance holds the key. The open question is now **whose Binance account it credits**, and who the other depositors are (`0x6a849df3…`, `0x6dec25d7…`, `0x2c2d845f…`, `0x87647780…`; 36 senders in all) | Ask the CICLOPS multisig signers (named on the CICLOPS forum thread) or Celo Core Co. on the governance forum which vendor or OTC desk they pay via Binance; Arkham or Nansen entity pages for the four largest senders | Free / request to team |
| 2 | ✅ **Closed:** `0xf6436829Cf96EA0f8BC49d300c536FCC4f84C4ED` is Binance (Blockscout "Tether: Binance" + Arkham "Binance", Proof of Reserves). It is Binance's collection wallet; the deposit address is `0x1b20…` | — | — |
| 3 | **Partly closed:** Safe `0x2fb70f05…` sends to Binance deposit `0x1b20…` (7.75M CELO, 10 Sep – 6 Nov 2026). `0x6247ffEe…` behaves like an exchange hot wallet. Still open: where `0x0E17c935…` and `0x2d880CCC…` (23.9M received; no Arkham entity, heavy exchange and Circle flows on other chains) and `0xc731e70c…` send CELO | Blockscout `addresses/{addr}/token-transfers?filter=from`, then label receivers | Free |
| 4 | Why ~390M CELO is outside circulating supply | Celo Registry addresses (`getAddressForString`) for every treasury contract, plus the Mondo supply page and CoinGecko's circulating-supply method; ask Celo Core Co. for the wallet list behind "circulating" | Free / request |
| 5 | Mento reserve CELO holdings | reserve.mento.org "Collateral" and "Addresses" tabs (JS-rendered; load in a browser) or Mento's reserve multisig balances on Blockscout | Free |
| 6 | Total CELO paid to Season 1–3 teams and how much was sold | Sum all Community Fund outflows (Blockscout, paginated) and map each to its CGP; ask teams for disclosure of conversions | Free |
| 7 | Celo Core Co. legal entity and directors | Ask Celo Core Co.; then the relevant register (cLabs was a US company; the Foundation was Swiss) — Swiss commercial register (Zefix) and Delaware search | Free (Delaware details may cost a fee) |
| 8 | Fault-proof and upgrade-key setup today | L2BEAT Celo page; Celo docs "operate/notices" for Jello and Jovian | Free |
| 9 | MiCA white paper / any filing for CELO | ESMA interim MiCA register (white papers CSV); SEC EDGAR full-text search "Celo" | Free |
| 10 | MiniPay figures independently confirmed | Opera's own investor releases / 20-F filing (Opera is SEC-listed) for MiniPay wallet numbers | Free (EDGAR) |
| 11 | Binance / Bybit order-book depth | `api.binance.com/api/v3/depth?symbol=CELOUSDT` and Bybit `v5/market/orderbook` (blocked from this network: 451/403); retry from another region | Free, IP-dependent |
| 12 | Status of the 25% burn (CGP-0257) and the 1.75M burn | Watch celo-org/governance PR #848 and Mondo's proposal page; re-propose status of CGP-0234 | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
