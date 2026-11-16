---
ticker: ZEC
name: Zcash
chain: zcash
contract: "native (transparent t-addresses + Sapling/Orchard shielded pools)"
overall_score: 4.9
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 7
  selling_behavior: 5
  tokenomics_supply: 7
  liquidity_market: 7
  product_development: 6
  adoption_customers: 4
  security_audits: 7
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  treasury_to_exchange_during_pump: "not provable (every dev-fund payout is shielded first; consensus requires transparent coinbase outputs to go to a shielded pool)"
  treasury_funded_wallet_to_exchange_during_pump: "not provable (12 of 100 weekly ZCG/FPF shielding days were pump days, e.g. 17 Sep 2026, +30.7%; destinations hidden)"
  mint_path_live: "yes by design (PoW issuance ~1,800 ZEC/day; 20% of subsidy to dev funding streams; 21M cap)"
  regulatory_delisting_risk: "yes (EU AMLR Art. 79 applies 10 Jul 2027 to anonymity-enhancing coins)"
price_usd: 872.73
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZEC · Overall grade **4.9 / 10 · ❌ FAIL**

**Summary:** Zcash is a 10-year-old proof-of-work privacy coin with a hard 21M cap, no insider token allocation, and dev funding written into consensus code and paid to published multisig addresses. It has a spot ETF (Grayscale ZCSH, $528M AUM). But the chain earns almost nothing: about $625k a year of fees, and none of it reaches holders. Dev funding is 20% of every block, and every payout is shielded before it is spent, so whether insiders sell into pumps cannot be checked on-chain. EU rules from July 2027 threaten exchange access. The Revenue gate fails.

**🚨 Top warning (red line):** The **Zcash Community Grants / Financial Privacy Foundation funding-stream multisig** [`t3cFfPt1…GCow`](https://blockchair.com/zcash/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow) (8% of every block, named in [Zebra's consensus code](https://github.com/ZcashFoundation/zebra/blob/main/zebra-chain/src/parameters/network/subsidy/constants/mainnet.rs)) has received **103,624 ZEC** since Nov 2024 and sent **100,997 ZEC** into the shielded pool in ~1,000-ZEC weekly batches. **12 of those 100 weekly spend days were pump days (365-day window)**, e.g. **17 Sep 2026 (+30.7%)**: 1,001 inputs → 125.1 ZEC shielded ([tx](https://blockchair.com/zcash/transaction/2402f06fdc401c3cd5abe03b6e9ddf37c76f13f5fa319784fc2d6cf90eab794c)). Once shielded, nobody outside can see whether the ZEC was paid to grantees or sold on an exchange. **Second warning:** the ZIP 271 **2-of-3 key-holder multisig** (Zcash Foundation, Electric Coin Company, Shielded Labs) [`t3ev37Q2…wYo`](https://blockchair.com/zcash/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) still holds **70,863 ZEC (≈ $61.8M)** after shielding ~37.8k ZEC between Feb and Oct 2026 ([3 Feb](https://blockchair.com/zcash/transaction/eaedfdddd569ef24eaeeae9642746aaa26959a0e7f35ccb32aef660277ade2a9) · [16 Oct](https://blockchair.com/zcash/transaction/3ad0da85bea918406537ace183590377412675a413e7d127916076eb13094173)); none of those days was a pump day. Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 7/10 | ✅ PASS |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZEC · Zcash · 4.9 / 10 · ❌ FAIL

> **One line:** Bitcoin-style supply with optional privacy and a US ETF, but a fee-less economy, dev funding that disappears into the shielded pool the moment it is spent, and a hard EU deadline in July 2027.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (Blockchair API, height ~3,579,378, 16 Nov 2026) |
|---|---|
| **Price** $872.73 | **Circulating** 17.044M of 21M max (CoinGecko) |
| **24h / 7d / 30d** 🔴 −5.2% / −27.7% / −25.5% · 1y +24.9% | **ZCG/FPF stream** [`t3cF…GCow`](https://blockchair.com/zcash/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow) balance 2,626.6 ZEC |
| **Market cap** $14.875B · **FDV** $14.875B | **Key-holder multisig** [`t3ev…wYo`](https://blockchair.com/zcash/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) balance 70,862.9 ZEC |
| **24h volume** $561.0M | **Transactions, 24h** 8,833 |
| **ATH** $3,191.93 (28 Oct 2016) · now −72.7% | **TVL** $2.3M (DefiLlama) |
| **Pump days, last 365** 93 (CoinGecko closes) | **ETF** Grayscale ZCSH, AUM $527.8M |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, 30d / 1y | $65,553 / $624,608 | [Tier A] [DefiLlama Zcash](https://defillama.com/chain/Zcash) (16 Nov 2026) |
| Revenue to the protocol / holders | **$0** (fees go to miners; nothing is burned) | same |

**What it means:** $0.6M a year of fees on a $14.9B coin, with nothing accruing to holders. Like Bitcoin, the bet is on money demand, not cash flow. Under this framework that scores **1** and **trips the Revenue gate**.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Organisations | Electric Coin Company (ECC), Zcash Foundation (ZF), Shielded Labs, Zcash Community Grants (ZCG, administered by the Financial Privacy Foundation) | [Tier A] [ZIP 271](https://zips.z.cash/zip-0271) · [Zebra consensus constants](https://github.com/ZcashFoundation/zebra/blob/main/zebra-chain/src/parameters/network/subsidy/constants/mainnet.rs) |
| How funding is set | By network upgrades (ZIP 1015 in NU6, Nov 2024; ZIP 271 / ZIP 214 rev. 2 in NU6.1, Nov 2025) | [Tier A] ZIPs |
| Key control | The dev-fund multisig is **2-of-3** with keys held by ZF, ECC and Shielded Labs | [Tier A] [ZIP 271](https://zips.z.cash/zip-0271) |
| Spending disclosure | Grants are decided off-chain; payouts are shielded, so they cannot be matched to grants on-chain | chain |

**What it means:** Rules are public and written into consensus code, and the key-holders are named organisations. The blind spot is the shielded spending side. Score **6**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 7/10 · ✅ PASS

| Bucket | ZEC | Notes |
|---|---:|---|
| Key-holder 2-of-3 multisig [`t3ev…wYo`](https://blockchair.com/zcash/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) | **70,862.9** (0.42% of supply) | Got the 78,750 ZEC one-time lockbox disbursement at NU6.1 (24 Nov 2025); 108,668 ZEC received in total |
| ZCG/FPF stream [`t3cF…GCow`](https://blockchair.com/zcash/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow) | 2,626.6 | 8% of subsidy; shielded weekly |
| Deferred lockbox (12% of subsidy, held by consensus, no address) | ~81,000 [Unverified estimate] | ≈ 433k blocks since NU6.1 × 0.1875 ZEC; read `getblockchaininfo` valuePools to confirm |
| Insider premine | None | The 2016–2020 Founders' Reward (10% of early issuance) has long been paid out |

**What it means:** Visible dev-org holdings are about 1% of supply, under multisig, with no investor allocation. Score **7**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

| Day (UTC) | Route | ZEC | 5-day change (CoinGecko) | Pump? |
|---|---|---:|---:|---|
| Weekly, 5 Dec 2024 – 2 Nov 2026 | ZCG/FPF `t3cF…` → shielded pool (100 spend days, ~1,000 ZEC each) | 100,997 total | — | 12 of 100 on pump days (last 365 days) |
| 17 Sep 2026 | `t3cF…` → shielded, 1,001 inputs, 125.1 ZEC ([tx](https://blockchair.com/zcash/transaction/2402f06fdc401c3cd5abe03b6e9ddf37c76f13f5fa319784fc2d6cf90eab794c)); 1,000 ZEC that day | 1,000 | +30.7% | 🟡 Yes, destination hidden |
| 8 May 2026 · 9 Apr 2026 | same weekly pattern | 1,000 each | +48.4% · +46.8% | 🟡 Yes, destination hidden |
| 3 Feb 2026 · 14 Apr 2026 · 16 Oct 2026 | Key-holder multisig `t3ev…` → shielded ([3 Feb](https://blockchair.com/zcash/transaction/eaedfdddd569ef24eaeeae9642746aaa26959a0e7f35ccb32aef660277ade2a9) · [16 Oct](https://blockchair.com/zcash/transaction/3ad0da85bea918406537ace183590377412675a413e7d127916076eb13094173)) | ~37,805 | <10% | No |

- The ZCG/FPF spends run on a **fixed weekly cadence** (mostly Thursdays, ~8,000 coinbase outputs of 0.125 ZEC each), so pump-day overlap looks scheduled rather than timed.
- Zcash consensus forces transparent coinbase outputs to go to a shielded pool before they can be spent, so the shielding is required, not a choice ([protocol spec](https://zips.z.cash/protocol/protocol.pdf)).
- **Arkham pass ([Tier B] Arkham, read 16 Nov 2026 ~7:33 AM MST (signed-in account)).** Arkham does index Zcash transparent addresses (an earlier note here said it did not). It labels [`t3cF…Cow`](https://blockchair.com/zcash/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow) "Community Grants (Gemini Custody)" ([Arkham](https://intel.arkm.com/explorer/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow)), [`t3Xy…Xym`](https://blockchair.com/zcash/address/t3XyYW8yBFRuMnfvm5KLGFbEVz25kckZXym) "Major Grant Review Committee Funds (Gemini Custody)" ([Arkham](https://intel.arkm.com/explorer/address/t3XyYW8yBFRuMnfvm5KLGFbEVz25kckZXym)) and [`t3dv…BA1`](https://blockchair.com/zcash/address/t3dvVE3SQEi7kqNzwrfNePxZ1d4hUyztBA1) "Foundation (Gemini Custody)" ([Arkham](https://intel.arkm.com/explorer/address/t3dvVE3SQEi7kqNzwrfNePxZ1d4hUyztBA1)), all under entity Zcash Foundation. It labels [`t3ev…wYo`](https://blockchair.com/zcash/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) "ZIP-271 Disbursement Multisig" with no entity ([Arkham](https://intel.arkm.com/explorer/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo)), and the old ECC Development Fund address [`t3Lm…iif`](https://blockchair.com/zcash/address/t3LmX1cxWPPPqL4TZHx42HU3U5ghbFjRiif) as Electric Coin Co., one of 48 ECC-attributed addresses ([Arkham](https://intel.arkm.com/explorer/address/t3LmX1cxWPPPqL4TZHx42HU3U5ghbFjRiif)). Arkham files `t3cF…` under Zcash Foundation, but ZIP 271 and Zebra assign that stream to ZCG/FPF, so the Tier A designation stands; the "Gemini Custody" wording is a single Tier B hint about custody [Unverified].
- **The "COINBASE" counterparty is the block reward, not the Coinbase exchange.** Arkham shows repeated inbound "COINBASE" transfers on four of these addresses. Blockchair marks the same outputs `is_from_coinbase = true`, and the sizes are funding-stream shares of the block subsidy: 0.25 ZEC per block to `t3Xy…` and 0.15625 to `t3dv…` (8% and 5% of the 3.125 ZEC pre-halving subsidy, last on 23 Nov 2024), and 0.0417 per block to `t3cF…` today. The 78.75K ZEC "COINBASE" inflow to `t3ev…` is the ZIP 271 one-time disbursement, which the ZIP requires to be paid in the coinbase transaction of the NU6.1 activation block ([ZIP 271](https://zips.z.cash/zip-0271)). On the first transfer pages, every outflow goes to Arkham's opaque SHIELDED endpoint. No exchange-bound outflow appears, and the old ECC Development Fund address's last indexed transfer is 1 Sep 2021.
- No direct transfer from any dev-fund address to an exchange is possible to see. Verdict: **not proven either way** → **5**. Not gated. **Unchanged after the Arkham pass:** Arkham adds labels and confirms the in-flows are block rewards and the out-flows are shielded. It shows no exchange-bound transfer, so the premise of the 5 (destination hidden by design) still holds.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- **21M hard cap**, 17.04M issued (81%). Block subsidy 1.5625 ZEC per 75-second block (~1,800 ZEC/day ≈ 3.9% a year). The next halving is in ~2028.
- 20% of each subsidy goes to dev funding: 12% to the lockbox/Coinholder-Controlled Fund (stream `FS_CCF_H3` to height 4,406,399) and 8% to ZCG/FPF ([ZIP 271](https://zips.z.cash/zip-0271) · [Zebra](https://github.com/ZcashFoundation/zebra/blob/main/zebra-chain/src/parameters/network/subsidy/constants/mainnet.rs)). No unlock cliffs.

## 💧 Liquidity & market · 7/10 · ✅ PASS

- $561M of 24h volume on a $14.9B cap (3.8%). Spot ETF ZCSH on NYSE Arca since 25 Aug 2026 ([Grayscale](https://etfs.grayscale.com/zcsh)).
- Some exchanges restrict ZEC to transparent withdrawals in the EU. Very volatile (93 pump days in a year; −27.7% this week).

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The Zebra node is active (last commit 12 Nov 2026, `ZcashFoundation/zebra`). The legacy `zcash/zcash` (zcashd) was last committed 19 Jul 2026 as the ecosystem moves to Zebra plus new wallets.
- Shielded Orchard pool, viewing keys, NU7 in development.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- 8,833 transactions in 24h (Blockchair); TVL $2.3M. Use is mostly holding and exchange trading; ETF demand is the main new buyer.

## 🛡️ Security & audits · 7/10 · ✅ PASS

- No exploit or chain halt found in the last year. Proof-of-work chain since 2016. The 2018 Sapling counterfeiting bug was fixed before it was known to be used [Tier B, background].

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- **EU AMLR Article 79 applies on 10 Jul 2027.** It bars crypto service providers from accounts allowing anonymisation "including through anonymity-enhancing coins". It does not name Zcash, and transparent-only handling may be allowed ([analysis](https://zecwallet.at/eu-privacy-coin-ban-2027/) · [analysis](https://www.cryptocodes.eu/news/eu-privacy-coins-ban-monero-zcash-10-july-2027-20-october-2026), Tier B ×2).
- The US has an approved spot ETF (ZCSH). Mixed picture → **5**.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Weekly | ZCG/FPF shields ~1,000 ZEC |
| Ongoing | ZCSH flows (AUM $527.8M, 20.78M shares) |
| TBD | NU7 network upgrade (rotates the ZCG stream address per Zebra code) |
| **10 Jul 2027** | EU AMLR Article 79 applies: exchange delisting/restriction risk |
| ~2028 | Next halving |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Treasury → exchange during a pump | ⚪ Not provable: payouts are shielded. [example](https://blockchair.com/zcash/transaction/2402f06fdc401c3cd5abe03b6e9ddf37c76f13f5fa319784fc2d6cf90eab794c) |
| Treasury-funded wallet → exchange during a pump | ⚪ Not provable |
| Live mint path | 🟡 By design: PoW issuance, 21M cap |
| Regulatory delisting | 🟠 EU AMLR from 10 Jul 2027 |

## 📚 Sources

- [Tier A] Blockchair Zcash API: address dashboards, outputs aggregated by spending date, transaction dashboards for `t3cF…`, `t3ev…`, `t3Xy…`; chain stats; read 16 Nov 2026 MST
- [Tier A] [Zebra consensus constants (mainnet funding streams)](https://github.com/ZcashFoundation/zebra/blob/main/zebra-chain/src/parameters/network/subsidy/constants/mainnet.rs) · [ZIP 271](https://zips.z.cash/zip-0271) · [ZIP 1015](https://zips.z.cash/zip-1015) · [protocol spec](https://zips.z.cash/protocol/protocol.pdf)
- [Tier A] [Grayscale ZCSH](https://etfs.grayscale.com/zcsh) · [launch release](https://www.nasdaq.com/press-release/zcash-etf-ticker-zcsh-built-grayscale-begins-trading-nyse-arca-expanding-investor)
- [Tier B] EU AMLR analyses: [zecwallet.at](https://zecwallet.at/eu-privacy-coin-ban-2027/) · [cryptocodes.eu](https://www.cryptocodes.eu/news/eu-privacy-coins-ban-monero-zcash-10-july-2027-20-october-2026)
- [Tier A] DefiLlama Zcash fees/TVL; CoinGecko `zcash` (16 Nov 2026 5:26 AM MST) and its 365-day closes for every pump test; GitHub commits API
- [Tier B] Arkham, read 16 Nov 2026 ~7:33 AM MST (signed-in account): Zcash Foundation labels [t3cF…](https://intel.arkm.com/explorer/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow), [t3Xy…](https://intel.arkm.com/explorer/address/t3XyYW8yBFRuMnfvm5KLGFbEVz25kckZXym), [t3dv…](https://intel.arkm.com/explorer/address/t3dvVE3SQEi7kqNzwrfNePxZ1d4hUyztBA1) · ZIP-271 Disbursement Multisig [t3ev…](https://intel.arkm.com/explorer/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) · Electric Coin Co. Development Fund [t3Lm…](https://intel.arkm.com/explorer/address/t3LmX1cxWPPPqL4TZHx42HU3U5ghbFjRiif). Arkham's "COINBASE" counterparty = block-reward coinbase outputs (Blockchair `is_from_coinbase`, read 16 Nov 2026 ~7:45 AM MST). First transfer page only
- [Unverified] lockbox balance; where the shielded dev-fund payouts went; whether the "Gemini Custody" labels mean Gemini holds the keys

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| ZCG/FPF stream address is `t3cFfPt1…` (8%) and lockbox is 12% | [Zebra constants](https://github.com/ZcashFoundation/zebra/blob/main/zebra-chain/src/parameters/network/subsidy/constants/mainnet.rs) | A | 16 Nov 2026 |
| `t3cF…` received 103,624 ZEC and shielded 100,997 over 100 spend days | [address](https://blockchair.com/zcash/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow) | A | 16 Nov 2026 |
| 17 Sep 2026 pump day: 125.1 ZEC shielded (1,001 inputs, 0 transparent outputs) | [tx](https://blockchair.com/zcash/transaction/2402f06fdc401c3cd5abe03b6e9ddf37c76f13f5fa319784fc2d6cf90eab794c) | A | 16 Nov 2026 |
| Key-holder multisig is 2-of-3 ZF / ECC / Shielded Labs; 78,750 ZEC disbursement | [ZIP 271](https://zips.z.cash/zip-0271) · [address](https://blockchair.com/zcash/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) | A | 16 Nov 2026 |
| Key-holder multisig shielded ZEC on 3 Feb, 14 Apr, 16 Oct 2026; 70,863 ZEC left | [3 Feb](https://blockchair.com/zcash/transaction/eaedfdddd569ef24eaeeae9642746aaa26959a0e7f35ccb32aef660277ade2a9) · [14 Apr](https://blockchair.com/zcash/transaction/8a93724082fcc84bcd2c423c539214f1b3ec0802f11d25ec6021370a9e764c8a) · [16 Oct](https://blockchair.com/zcash/transaction/3ad0da85bea918406537ace183590377412675a413e7d127916076eb13094173) | A | 16 Nov 2026 |
| Arkham labels for the dev-fund addresses; "COINBASE" inflows are block-reward outputs; ZIP 271 disbursement paid in the activation coinbase | [t3cF](https://intel.arkm.com/explorer/address/t3cFfPt1Bcvgez9ZbMBFWeZsskxTkPzGCow) · [t3ev](https://intel.arkm.com/explorer/address/t3ev37Q2uL1sfTsiJQJiWJoFzQpDhmnUwYo) · [t3Xy](https://intel.arkm.com/explorer/address/t3XyYW8yBFRuMnfvm5KLGFbEVz25kckZXym) · [t3dv](https://intel.arkm.com/explorer/address/t3dvVE3SQEi7kqNzwrfNePxZ1d4hUyztBA1) · [t3Lm](https://intel.arkm.com/explorer/address/t3LmX1cxWPPPqL4TZHx42HU3U5ghbFjRiif) · [ZIP 271](https://zips.z.cash/zip-0271) · [`t3dv on Blockchair`](https://blockchair.com/zcash/address/t3dvVE3SQEi7kqNzwrfNePxZ1d4hUyztBA1) | A + B | 16 Nov 2026 ~7:33 AM MST |
| Old Major Grants address received and spent 420,001 ZEC (2020–2024) | [address](https://blockchair.com/zcash/address/t3XyYW8yBFRuMnfvm5KLGFbEVz25kckZXym) | A | 16 Nov 2026 |
| Fees $624,608 / 1y; revenue $0 | [DefiLlama](https://defillama.com/chain/Zcash) | A | 16 Nov 2026 |
| ZCSH listed 25 Aug 2026; AUM $527.8M | [Grayscale](https://etfs.grayscale.com/zcsh) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026** (first transfer page per address). Arkham labels `t3cF…`, `t3Xy…` and `t3dv…` Zcash Foundation ("Gemini Custody"), `t3ev…` the ZIP-271 Disbursement Multisig and `t3Lm…` the ECC Development Fund. Inflows are block-reward coinbase outputs; outflows go to the shielded pool. Still open: where the shielded payouts go, and whether `t3cF…` is held at Gemini | Ask ZCG/FPF and the key-holder organisations to publish shielded-payout reports or viewing keys | Free |
| 2 | **Where do shielded payouts go?** | Ask ZCG/FPF and the key-holders for viewing keys or published payout reports, and match them to grant decisions | Free |
| 3 | **Lockbox balance** | Run `getblockchaininfo` on a Zebra/zcashd node and read the `lockbox` value pool | Free (node) |
| 4 | **EU exchange status before Jul 2027** | Track Binance/Kraken/Coinbase EEA notices for ZEC | Free |
| 5 | **ECC and ZF funding after Nov 2024** | Read the 2025–26 ECC and ZF financial reports | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
