---
ticker: SOLV
name: Solv Protocol
chain: bsc
contract: "0xabE8E5CabE24Cb36df9540088fD7cE1175b9bc52"
overall_score: 4.2
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 1
  tokenomics_supply: 4
  liquidity_market: 4
  product_development: 7
  adoption_customers: 6
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [selling_behavior]
red_lines:
  hack_exploit: "yes, Mar 2026: the BRO vault (a one-off Solv deployment tied to the token listing) lost 38.05 SolvBTC (~$2.7M) to a double-mint bug; Solv says both affected participants were repaid by 9 Mar 2026"
  mint_path_live: "no in code (both SOLV contracts are fixed-supply OZ ERC20s with no mint function and no owner); but the docs call max supply 'dynamic' and say it may grow by governance for future BRO tranches, which would need a new deployment"
  team_wallet_to_exchange_during_pump: "yes, small (Solv Safe 0xccbc sent 18,666,567 SOLV to a Binance deposit on the 11 Mar 2026 pump day, +18.8%; EOA 0x8353, funded by a Solv vesting Safe, sent the same amount to the same deposit on the 21 Nov 2025 pump day, +14.0%); ~304M more went from Solv-funded wallets to Binance/Bybit deposits on non-pump days, purpose undisclosed. The 2 Apr 2026 31.5M pump-day deposit was by a wallet Arkham labels OKX Blockdream Ventures (investor), not counted"
  treasury_in_single_key_wallets: "partly (~3.85B SOLV, 39.9% of max supply, sits in five 4-of-5 Safes with no vesting contract, plus 91.0M in a sixth Safe 0x5e75 with the same signers; ~739M more sits in EOAs that Solv's Safes funded: 0x1478 428.7M, 0x5030 310M across two chains)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The token has no claim on revenue and no live buyback. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate SOLV/USDT daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.004495
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SOLV · Overall grade **4.2 / 10 · ❌ FAIL**

**Summary:** Solv runs SolvBTC, a real Bitcoin-yield product with $439M TVL, and DefiLlama counts **$12.2M of protocol revenue in the last year**, about 2x revenue against a $26.5M market cap. But **none of that revenue reaches SOLV holders** (holders revenue $0), and the only "buyback" (vSOLV) paid out of token supply and ended on 17 Mar 2026. About 40% of max supply sits in five Solv-run 4-of-5 Safes that hand out a monthly release by policy, not by a vesting contract. A sixth Safe with the same signers holds 91M more, and another ~739M sits in single-key EOAs those Safes funded. The token is down 97.8% from its listing high, the 17 Nov 2026 unlock (186.6M, 3.2% of circulating supply) lands tomorrow, and a Mar 2026 exploit hit a Solv vault. No hard gate trips, but the average fails.

**🚨 Top warning:** the vesting schedule is a promise, not code. Genesis Safe [`0x8749…bf75`](https://bscscan.com/address/0x8749b13fe36c72b745f948f91fb2ffec3b63bf75) split the 8.4B BSC supply on 13 Feb 2025, putting **3.85B SOLV (39.9% of max supply)** into five 4-of-5 Safes with the same five signers. The largest is [`0xbf1f…4ca0`](https://bscscan.com/address/0xbf1f4347dd6e7a7ccfa3f78acae28b2f01b44ca0) (1.515B, [funding tx](https://bscscan.com/tx/0xfeb1cfd9e5cf4e2a1f759dd7236f2a40423b5fe864b50e074d0ad628c3ddbab5)). Releases go to the 3-of-5 operating Safe [`0xccbc…1fd0`](https://bscscan.com/address/0xccbc5f15d91f474a37c171d6de51815946d21fd0), and from there to Binance deposits and single-key EOAs. Examples:
- **18.67M SOLV into a Binance deposit on the 11 Mar 2026 pump day** (+18.8%, [tx](https://bscscan.com/tx/0x5d6279473fb13bf3dd3191db4ae6e79cf84d6a4a7d613922df490a99310630da)).
- **18.67M into the same Binance deposit on the 21 Nov 2025 pump day** (+14.0%) from EOA `0x8353…`, which a sixth Solv Safe funded ([tx](https://bscscan.com/tx/0x760d09c52377b99205bbe4c2a094e36204ea94512e8ae843f69fd6315c4bd998)).
- **428.7M into EOA [`0x1478…565c`](https://bscscan.com/address/0x1478f63a183553b77dbc41458443450271c1565c)** on 18 Sep 2026 ([tx](https://bscscan.com/tx/0x9effa554016dbb1a88ea87f1f8620cb14ea6598fd2737d01eac19cda387f626b)), the same day Safe `0x82b3…` released 210M.

Nothing on-chain stops the signers from releasing faster. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SOLV · Solv Protocol · 4.2 / 10 · ❌ FAIL

> **One line:** A real Bitcoin-yield business with $12M a year of revenue that the token does not share. Forty percent of max supply sits in team-run Safes that release it by policy, and the price is 97.8% below its listing high.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (BSC + Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.004495 | **BSC token** [`0xabE8…bc52`](https://bscscan.com/address/0xabe8e5cabe24cb36df9540088fd7ce1175b9bc52#code) (OZ ERC20, fixed 8.4B, no owner) |
| **24h / 7d / 30d** 🟢 +0.6% / +3.7% / +1.1% · 1y −68.9% | **Ethereum token** [`0x169e…940d`](https://etherscan.io/address/0x169e36f327caa83d004f5c2668ac25a1424c940d#code) (fixed 1.26B BRO tranche, [minted 15 May 2026](https://etherscan.io/tx/0x5567bfdb79460625f861bc5502822d4d139f696ea06259e7d833fa93ab459538)) |
| **Market cap** $26.54M · **FDV** $43.42M | **`totalSupply()`** 8,400,000,000 (BSC) + 1,260,000,000 (ETH) = 9.66B |
| **24h volume** $3.20M | **Circulating (CoinGecko)** 5,904,733,333 (61%) |
| **ATH** $0.2001 (17 Jan 2025, listing) · now −97.8% | **Vesting Safes (4-of-5)** 3,853,920,000 SOLV in A–E (39.9% of max) + 90,999,998 in Safe F = 40.8% |
| **Holders** 115,039 on BSC (GoPlus) | **Binance cold wallet** [`0xf977…acec`](https://bscscan.com/address/0xf977814e90da44bfa03b6295a0616a897441acec) 1.24B (#1 holder) |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, last 1 year | **$24.25M** | [Tier A] [DefiLlama Solv Protocol](https://defillama.com/protocol/solv-protocol), read 16 Nov 2026 |
| Protocol revenue, last 30 days / 1 year | **$1.22M / $12.23M** ("protocol share of staking rewards plus all mint/redemption fees") | [Tier A] DefiLlama |
| Holders revenue | **$0** | [Tier A] DefiLlama `dailyHoldersRevenue` |
| Price / sales | ≈ **2.2x** on market cap, 3.6x on FDV | Calculated |
| Buyback | vSOLV "buyback" ran 17 Sep 2025 – 17 Mar 2026 and was paid from a **2.5% supply allocation**, not from revenue. It has ended, and no revenue buyback is live | [Tier A] [vSOLV docs](https://docs.solv.finance/solv-token/vsolv-campaign) |

**What it means:** The business is real and cheap on a sales multiple, but the token has no claim on revenue and no live buyback. SOLV's uses are governance, staking and fee discounts. **4**: better than a zero-revenue token, but it does not pass.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The token has no claim on revenue and no live buyback. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Entity | Solv Foundation issues the token; Solv Protocol runs SolvBTC | [Tier A] [Solv docs](https://docs.solv.finance/solv-token/solv-tokenomics) |
| Team | Public founding team; the protocol has run since 2020 (vouchers, then SolvBTC) | [Tier B] [Alea Q4 2025](https://alearesearch.io/reports/benchmark/solv-q4-2025) · Solv site |
| Wallet control | All six vesting Safes (A–F) share the **same five signers** (4-of-5). Operating Safe `0xccbc…` (3-of-5) shares three of them | [Tier A] Safe `getOwners()` / `getThreshold()` on BSC RPC |
| Incident handling | Published a [post-incident review](https://insights.solv.finance/post-incident-review-bro-vault-incident-and-strengthened-security-commitments/) and says it repaid the two affected participants within four days | [Tier A] Solv |

**What it means:** A known, long-running team that reacted openly to its exploit. But one group of five people controls every vesting bucket, and Solv does not publish its wallet list.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket | SOLV | Notes |
|---|---:|---|
| Published allocation | Private sale 28.86% · Community & DAO Treasury 18% · Team & Advisors 13% · Ecosystem 8.14% · Airdrop 8.5% · External partners 8.5% · Megadrop 7% · BD 4% · Liquidity 3% · Vesting voucher 1% · BRO 13.04% | [Tier A] [Solv tokenomics](https://docs.solv.finance/solv-token/solv-tokenomics) |
| Safe A [`0xbf1f…4ca0`](https://bscscan.com/address/0xbf1f4347dd6e7a7ccfa3f78acae28b2f01b44ca0) (4-of-5) | **1,515,150,000** | Got 2.424B from genesis on 13 Feb 2025 ([tx](https://bscscan.com/tx/0xfeb1cfd9e5cf4e2a1f759dd7236f2a40423b5fe864b50e074d0ad628c3ddbab5)) |
| Safe B [`0x82b3…1c5f`](https://bscscan.com/address/0x82b3cbafb7d0ad59f44a8295e4a57ae759a61c5f) (4-of-5) | **882,000,000** | Releases 210M at a time to `0xccbc…` ([16 Mar](https://bscscan.com/tx/0x9e28322ea4f723b2a52871457274047dd9e7a0458aeb28ada3fb987dcd00f297), [4 Jun](https://bscscan.com/tx/0xf43efe2f68dd59d07c0b1236affa8b1fcb97892ef55cd75204d9ee749161632c), [18 Aug](https://bscscan.com/tx/0x7fe8af7eae3222f9e1dd5c467d603c6857956d9b0868d5958848222b0feac61e), [18 Sep 2026](https://bscscan.com/tx/0xe6c1b046f43f446c8eebcc558defe4d6ac2823481ca30a5ae40a35721b4bf15e)) and got 210M back from EOA `0x0bd8…` on [24 Sep 2026](https://bscscan.com/tx/0xfd3dddf74f14af75746ede587f09de2d825ef7afd49bf207ecf4008479044452) |
| Safe C [`0x07ea…8205`](https://bscscan.com/address/0x07ea1e798ddd64dea59ef828f32937d7660b8205) (4-of-5) | **819,000,002** | Same signers |
| Safe D [`0xa354…54ef`](https://bscscan.com/address/0xa3544f3055cae99b8ef9aac07570a68404e254ef) (4-of-5) | **490,769,998** | Same signers |
| Safe E [`0xbfbe…9601`](https://bscscan.com/address/0xbfbe670c205dd848cd49a14590aadbe29e8c9601) (4-of-5) | **147,000,000** | Same signers |
| EOA [`0x1478…565c`](https://bscscan.com/address/0x1478f63a183553b77dbc41458443450271c1565c) | **428,687,661** | One transfer from Safe `0xccbc…` on 18 Sep 2026; not moved since. **Single key**, owner not disclosed. Arkham: unlabelled, 428.688M, only that one inbound transfer ([Arkham](https://intel.arkm.com/explorer/address/0x1478f63a183553b77dbc41458443450271c1565c)) |
| EOA [`0x5030…32c1`](https://bscscan.com/address/0x50301ce376e7e66ffc07ee442dbcff5b34d332c1) | **238.1M (BSC) + 71.9M ([Ethereum](https://etherscan.io/address/0x50301ce376e7e66ffc07ee442dbcff5b34d332c1))** | Paid directly by Safes A, C, D, E and F and by `0x0bd8…`. **Single key**. Arkham: unlabelled, 310.0M across networks ([Arkham](https://intel.arkm.com/explorer/address/0x50301ce376e7e66ffc07ee442dbcff5b34d332c1)) |
| Safe F [`0x5e75…55a6`](https://bscscan.com/address/0x5e75298a82b758308706cff215c2b99d1af155a6) (4-of-5) | **90,999,998** | **Corrected: a Safe, not an EOA.** BSC RPC `getOwners()`/`getThreshold()` show the same five signers as Safes A–E, threshold 4. Got 546M from genesis ([tx](https://bscscan.com/tx/0xf766bed6c728565c4cf962983d0cc0b748117a1de2672c29acccdf9a50508f0b)); sent 182M to `0xccbc…` (30.333M monthly releases) and 191.3M to unlabelled EOA `0x8353…`. Arkham: Gnosis Safe Proxy, no entity named ([Arkham](https://intel.arkm.com/explorer/address/0x5e75298a82b758308706cff215c2b99d1af155a6)) |

**What it means:** About 3.85B SOLV (39.9% of max supply, 65% of the circulating count) sits in Safes that work as vesting by policy only: four of five signers can move any amount at any time. A sixth Safe with the same signers (Safe F) holds 91.0M more, so the Safe total is ~3.94B (40.8% of max). About 739M more sits in plain EOAs funded by those Safes. Multisigs beat single keys, and the Safes have released on a steady monthly rhythm so far, so this scores **4**, not lower. Moving Safe F from the EOA list to the Safe list (a 4-of-5 multisig, Tier A) does not change the score.

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

*Pump test uses Gate SOLV/USDT daily closes (UTC). 51 of the last 365 days were pump days. "Solv-funded" means the sender got its SOLV from the Solv Safes above. Exchange deposit labels are Etherscan name tags for the same address (Tier B): Binance 51 = [`0x8894…d4e3`](https://bscscan.com/address/0x8894e0a0c962cb723c1976a4421c95949be2d4e3).*

| Day (UTC) | Route | SOLV | 5-day change | Pump? | Note |
|---|---|---:|---:|---|---|
| 3 Jan 2025 | Genesis Safe → [`0x3bb9…e77e`](https://bscscan.com/address/0x3bb9c00b4f5f9337dedfa59eeb5b68c205cee77e) → Binance 51 ([tx](https://bscscan.com/tx/0x4bcadcd751cf44ebf42c33da57e88f19f34c7ce6670d1527f0df6b2078233d83)) | 587,999,990 | pre-listing | n/a | Exactly 7% of 8.4B = the disclosed **Binance Megadrop** bucket |
| 30 Oct 2025 | Safe F → EOA [`0x8353…5f40`](https://bscscan.com/address/0x83536027de14d96e9d34382c825263be9b305f40) → Binance deposit `0x7d32…` ([tx](https://bscscan.com/tx/0x09132bc0c484959540a235c271c9058252f14589e200dc07537795c0cbdfaf1b)) | 18,666,567 | +4.2% | No | Start of the fixed 18.67M series |
| **21 Nov 2025** | Safe F → EOA `0x8353…` → Binance deposit `0x7d32…` ([tx](https://bscscan.com/tx/0x760d09c52377b99205bbe4c2a094e36204ea94512e8ae843f69fd6315c4bd998)) | **18,666,567** | **+14.0%** | 🔴 **Yes** | Same amount, same deposit as 11 Mar 2026 |
| 30 Dec 2025 | `0x8353…` → `0x7d32…` ([tx](https://bscscan.com/tx/0xbbdee2189f28e72b0403e681f9fe5beb89f39d144d6ad1b2bd7e89c326ae5fc2)) | 18,666,567 | −5.1% | No | |
| 26 Jan 2026 | `0x8353…` → `0x7d32…` ([tx](https://bscscan.com/tx/0x33ed32819fbac1e5779b02847286d00eb3bdd456185e44fc8ff3890f14e92013)) | 18,666,567 | +2.8% | No | Last of four from `0x8353…`; it then returned 90M to `0xccbc…` on [4 Mar 2026](https://bscscan.com/tx/0x5c0743b97633765d38bab642677e23716756c17af98ea64b7a2c41f3cff73760) |
| 26 Dec 2025 | Safe E → [`0xef12…2fd7`](https://bscscan.com/address/0xef12417df03f2722a2baed3111c7b6a4347d2fd7) → Binance deposit [`0xcca9…4de8`](https://bscscan.com/address/0xcca996f6a29313e264930731f5838adc85d44de8) ([tx](https://bscscan.com/tx/0xa3406a9865ca72c63d810d5ca858f6abc866f1f723ab21337aceb6a2b138a6dc)) | 28,999,999 | 0.0% | No | Undisclosed |
| 13 Feb 2026 | `0xef12…` → `0x7d9c…` → **Bybit Wallet 16** ([tx](https://bscscan.com/tx/0xf5ae242f0cc8d3a6c5e920d95118972ed5a912cee0d7840bd6684cb3ebbff1ff)) | 10,839,990 | −7.4% | No | Undisclosed |
| 9 Mar 2026 | **Safe `0xccbc…`** → Binance deposit [`0xb86b…69a2`](https://bscscan.com/address/0xb86bcc45d275459953a5a02d8312bd9eb3b269a2) ([tx](https://bscscan.com/tx/0xf2d80278ff827237520b4dd03a17efbf43ae7dc7cfeddc60f5d9a91225e44108)) | 6,999,999 | −2.0% | No | Deposit forwards only to Binance 51 |
| **11 Mar 2026** | **Safe `0xccbc…`** → Binance deposit [`0x7d32…dd45`](https://bscscan.com/address/0x7d3217feb6f310f7e7b7c8ee130db59dcad1dd45) ([tx](https://bscscan.com/tx/0x5d6279473fb13bf3dd3191db4ae6e79cf84d6a4a7d613922df490a99310630da)) | **18,666,567** | **+18.8%** | 🔴 **Yes** | No disclosure found |
| 18 Mar 2026 | Safe `0xccbc…` → same deposit `0x7d32…` ([tx](https://bscscan.com/tx/0xb385ae77eea9e655a69930b484415d0b971dc5403a7385f15d7ab72669dc0e21)) | 18,666,567 | −4.2% | No | Same amount repeats, like a vesting payout to a beneficiary's exchange account [Unverified] |
| *2 Apr 2026* | *Investor flow, not counted:* operator `0x50b4…` → disperse → fund wallet [`0x78db…e239`](https://bscscan.com/address/0x78db576873f032a7c4749b214a8af6966b3be239) on 28 Mar ([tx](https://bscscan.com/tx/0x960b582ff86acf424e26ede8fcb356c406906ef6eca2cc168f29c6497e7e1f66)) and 31 Mar ([tx](https://bscscan.com/tx/0x87f7591dd8c889099f525614d07ddedda40e73adb1ebdced7ab0814ef0ef33c0)), 31.5M in total; the fund sent it to deposit `0x2620…e457` ([tx](https://bscscan.com/tx/0xf8c9cbc1269ed6fbbe0de738c4305146474d683ce28ecccf424994cefbc7ed27)), which swept it to Binance 51 two minutes later ([tx](https://bscscan.com/tx/0x6734f7a5b41620c575f150958907ababcf3458b79606b0d15c0e4e6be3d3923a)) | *31,500,000* | *+83.6%* | *Yes* | Arkham labels `0x78db…` **OKX Blockdream Ventures** (fund, 63M SOLV now, [Arkham](https://intel.arkm.com/explorer/address/0x78db576873f032a7c4749b214a8af6966b3be239)). An investor sold or deposited its own allocation |
| 6 Jul 2026 | ETH Safe `0xccbc…` → `0x50b4…` → disperse → Binance deposit [`0x3311…2636`](https://etherscan.io/address/0x33119a9812dab4b805c1113bcfa41524f0cd2636) ([tx](https://etherscan.io/tx/0x1d5e67376f2de0ad4caac056e64190f914bcf43e802aca45bdc15f6efdee2094)) | 50,000,000 | −2.7% | No | Forwarded to Binance 14 on 8 Jul |
| 29 Sep 2026 | `0xe4a8…` → `0x7d32…` ([tx](https://bscscan.com/tx/0x3f44e8b9972eba04c434fa311661c471f61e556e708404df37786048d4ed3d34)) | 18,666,000 | +0.6% | No | `0xe4a8…` is fed by `0x0bd8…` and `0x5030…` |
| 30 Sep 2026 | `0x0bd8…` → Binance deposits `0x3f84…` ([tx](https://bscscan.com/tx/0x76aca588b89fe5dd6ccbee0b0d5b62c842b58bea978bbcf4b2f92ca5273f2957)) + `0xb86b…` ([tx](https://bscscan.com/tx/0x4e43b30aa6ff53abf08c083e257b529f6d851a8a44149d81d091857c9e13d678)) | 36,170,900 | +1.5% | No | `0x0bd8…` got 364.7M from `0xccbc…` |
| 13 Oct 2026 | `0xe4a8…` → Binance deposit [`0x1b20…9202`](https://bscscan.com/address/0x1b20b200a78c6068ce5ea96226d1b53e0a119202) ([tx](https://bscscan.com/tx/0x4f96075c8b916192e762957b97e4faf955db9c4c572f962e5cfe0bc5d0061c75)) | 52,208,000 | +5.8% | No | |
| 23 Oct 2026 | `0xe4a8…` → `0x7d32…` ([tx](https://bscscan.com/tx/0x573b569fa688838b06b8ad4ff0eda352782cbc8d20abfa7084e2e5607672598b)) + `0xb86b…` ([tx](https://bscscan.com/tx/0x949d0ffebb009e1f577060a7dfe6374563d34eb65692aa455346019ad6cf4023)) | 25,665,000 | −6.2% | No | |

- **BRO tranche on Ethereum:** Safe `0xccbc…` sent 840M on [31 May 2026](https://etherscan.io/tx/0xaed921884d5620d89db1d133e242fa7d7b48021e5bad6539f524cd721d6407f6) and 420M on [1 Sep 2026](https://etherscan.io/tx/0x89fd0e88183f8156b9760fa7243677930e6241e16e059c2745e063f97fbf4529) to operator `0x50b4…`. It batched them through disperse contract [`0x3cf6…`](https://etherscan.io/address/0x3cf63891928b8ceebb81c95426600a18cd59c03f) to about 25 wallets, including 420M on the **5 Sep 2026 pump day (+13.1%)** ([tx](https://etherscan.io/tx/0x09f6dddad0669c156e53fc05c20a6cc79b9926189b0fc579218e85925ccf11fe)). Recipients moved tokens on 8–10 Sep (+52.5% / +26.6%). This was the disclosed BRO distribution, so it is not counted as Solv selling. But the BRO buyers' identities and unlock terms are not public.
- **Total from Solv-funded wallets into exchange deposits, Oct 2025 – Oct 2026:** ~341.6M SOLV (Megadrop and the investor row excluded), of which **37.3M (10.9%) landed on pump days**, both in the fixed 18.67M series to deposit `0x7d32…`. Pump days were 14% of all days (51 of 365), so the timing looks no worse than chance. The 30 Oct 2025 – 26 Jan 2026 rows were added after the Arkham pass pointed to `0x8353…`.
- **Arkham pass ([Tier B] Arkham, read 16 Nov 2026 ~7:19–7:20 AM MST (signed-in account)):** `0x8353…` is an unlabelled EOA that got SOLV from Safe F and sent 18.667M ×4 to Binance deposit `0x7D3…` ([Arkham](https://intel.arkm.com/explorer/address/0x83536027de14d96e9d34382c825263be9b305f40)), which supports the beneficiary-payout reading. `0xef12…` is unlabelled; Arkham confirms its 29M Binance deposit and 10.84M Bybit deposit, funded by Safe E ([Arkham](https://intel.arkm.com/explorer/address/0xef12417df03f2722a2baed3111c7b6a4347d2fd7)). `0x0bd8…` ([Arkham](https://intel.arkm.com/explorer/address/0x0bd8ab88ec2b8d672d6dcafba571bc79430bf4eb)) and `0xe4a8…` ([Arkham](https://intel.arkm.com/explorer/address/0xe4a84981da2122e265ed2adf20467c8f63c3ad6e)) are unlabelled pass-through EOAs; Arkham shows a Safe it labels Solv Protocol among `0x0bd8…`'s funders. `0xe4a8…` sent **31,499,000 SOLV to the same OKX Blockdream Ventures wallet on 14 Nov 2026** ([tx](https://bscscan.com/tx/0x42e2db072248b43053f1ad6055cbfd1199bd72f5d93c1f5475f3804e95b6c095); −1.4%, not a pump day), the same size as the March payout. That looks like a scheduled Solv-to-investor vesting payout [Unverified]. Arkham does not name Solv on Safe `0xccbc…` or Safe F; the Solv attribution in this report rests on the on-chain flow logic (genesis split, shared signers), not on an Arkham label.

**What it means:** Two undisclosed pump-day deposits of Solv-released SOLV (11 Mar 2026 straight from the operating Safe, and 21 Nov 2025 via `0x8353…`, funded by Safe F) fail this section under the rules. Both are the same fixed 18.67M payment into the same Binance deposit, part of a roughly monthly series that lands on pump days about as often as chance would. That looks like a scheduled payout to one beneficiary's exchange account, not Solv timing sales. The 2 Apr 2026 31.5M pump-day deposit, an open question before, turns out to be investor flow: the fund wallet received its allocation from Solv's operator on 28 and 31 Mar and deposited it itself. It was never counted here. **5, unchanged after the Arkham pass.** The second pump-day deposit argues for a 4. The stronger payout evidence and the resolved investor flow argue against it. A 4 would make the overall 4.6, still FAIL, so the verdict does not depend on this call.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. The fixed monthly amount looks like a scheduled payout, but under the one-hop rule a direct project-Safe → exchange-deposit transfer on a pump day is a proven sale. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **5 → 1** (capped at 3, then −2). This adds the Selling hard gate. Pump days from Gate SOLV/USDT daily closes.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- **Fixed in code:** both contracts mint their whole supply in the constructor, with no `mint` and no owner ([BSC code](https://bscscan.com/address/0xabe8e5cabe24cb36df9540088fd7ce1175b9bc52#code) · [ETH code](https://etherscan.io/address/0x169e36f327caa83d004f5c2668ac25a1424c940d#code)).
- **But the policy says otherwise:** the docs call max supply "dynamic" and say it may increase by governance for future BRO tranches ([docs](https://docs.solv.finance/solv-token/solv-tokenomics)). The 1.26B Ethereum tranche (13.04% of max) was a **new token deployment in May 2026**, which shows this route is real. The docs also say each BRO mints "42 million", but on-chain the payouts went out in 420M blocks (840M + 420M), so the docs look wrong by 10x [Unverified which is meant].
- **Unlocks:** 61% is circulating. Next: **186.58M on 17 Nov 2026**, 154.46M on 18 Dec 2026, 370.46M on 17 Jan 2027 [Tier B: AlphaGrowth + Tokenomist]. That is 3–6% of circulating supply each month.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $3.20M of volume in 24h on a $26.54M cap (12% turnover); listed on Binance (Megadrop), Gate, Bybit and others.
- **−97.8% from the listing high** and −68.9% over a year. Binance cold wallets hold ~2.24B SOLV ([`0xf977…`](https://bscscan.com/address/0xf977814e90da44bfa03b6295a0616a897441acec) 1.24B plus `0x5a52…` ~997M).
- High-volume address [`0x0995…a4c5`](https://bscscan.com/address/0x09958d2ace12f464b8ed02b26fc756a55e51a4c5) (199.3M, about 4,800 transfers, heavily address-poisoned) is a **Bithumb Hot Wallet**, not a market maker ([Tier B] Arkham, read 16 Nov 2026 ~7:19–7:20 AM MST (signed-in account), [Arkham](https://intel.arkm.com/explorer/address/0x09958d2ace12f464b8ed02b26fc756a55e51a4c5)). **Corrected:** this was listed as a possible market maker before. With Binance, Bybit, Gate and Bithumb wallets, exchange custody holds a large share of the float.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- SolvBTC and its yield variants (xSolvBTC, SolvBTC.BNB) run across BSC, Ethereum and other chains; there are staking and Pendle PT/YT markets ([DefiLlama](https://defillama.com/protocol/solv-protocol)).
- The token contracts are verified, minimal OZ ERC20s.

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- **TVL $439.4M** (Bitcoin $371.4M, Ethereum $57.8M, BSC $6.6M) and $24.25M of fees a year ([Tier A] DefiLlama).
- 115,039 BSC holders (GoPlus). The 167k-transfer airdrop distributor [`0x21f1…f01c`](https://bscscan.com/address/0x21f109a0a431c75cfeb4939b7ed8069acfc4f01c) gave out 705M.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- **Exploit, 5 Mar 2026:** the BRO wrapper [`0x15f7…cfcf`](https://etherscan.io/address/0x15f7c1ac69f0c102e4f390e45306bd917f21cfcf) (beacon [`0x014e…6869`](https://etherscan.io/address/0x014e6f6ba7a9f4c9a51a0aa3189b5c0a21006869)) minted twice per deposit. The attacker looped it 22 times, inflating 135 BRO into 567.8M BRO, and drained **38.05 SolvBTC (~$2.7M)** from treasury [`0xfb2d…afef9`](https://etherscan.io/address/0xfb2dc2428b6c2fb149a3e6d658fdf979cc0afef9) ([Solv review](https://insights.solv.finance/post-incident-review-bro-vault-incident-and-strengthened-security-commitments/) · [DarkNavy](https://www.darknavy.org/web3/exploits/solv-bro-double-mint/) · [Halborn](https://www.halborn.com/blog/post/explained-the-solv-hack-march-2026)).
- Solv says only two participants were hit and both were fully repaid by 9 Mar 2026. Core SolvBTC was not affected.
- **Weak spot:** ~739M SOLV in single-key EOAs (see Holdings).

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. BRO was sold to institutions as a BTC-for-SOLV offering; its terms and buyers are not public. SolvBTC custody and reserve attestations sit outside this report's scope [Unverified].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| **17 Nov 2026** | Unlock of 186.58M SOLV (3.2% of circulating) [Tier B] |
| 18 Dec 2026 | Unlock of 154.46M [Tier B] |
| 17 Jan 2027 | Unlock of 370.46M [Tier B] (two-year anniversary of listing) |
| Any time | A new BRO tranche (new supply by governance, per docs) |
| Ongoing | Monthly releases from the 4-of-5 Safes to `0xccbc…` |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 BRO vault, 5 Mar 2026, ~$2.7M; [repaid](https://insights.solv.finance/post-incident-review-bro-vault-incident-and-strengthened-security-commitments/) |
| Team wallet → exchange during a pump | 🟡 Safe `0xccbc…` 18.67M → [Binance deposit](https://bscscan.com/tx/0x5d6279473fb13bf3dd3191db4ae6e79cf84d6a4a7d613922df490a99310630da) on 11 Mar 2026 (+18.8%); Safe F-funded `0x8353…` 18.67M → [same deposit](https://bscscan.com/tx/0x760d09c52377b99205bbe4c2a094e36204ea94512e8ae843f69fd6315c4bd998) on 21 Nov 2025 (+14.0%). The 2 Apr 2026 31.5M pump-day deposit was by an investor fund wallet (Arkham: OKX Blockdream Ventures), not the team |
| Live mint path | 🟡 None in code; the docs allow new BRO supply by governance, which happened once (May 2026 deployment) |
| Treasury in single-key wallets | 🟡 ~739M in EOAs [`0x1478…`](https://bscscan.com/address/0x1478f63a183553b77dbc41458443450271c1565c) and [`0x5030…`](https://bscscan.com/address/0x50301ce376e7e66ffc07ee442dbcff5b34d332c1); the ~3.94B main stash is in six 4-of-5 Safes ([`0x5e75…`](https://bscscan.com/address/0x5e75298a82b758308706cff215c2b99d1af155a6) corrected from EOA to Safe) |
| Vesting enforced on-chain | 🔴 No; Safes release by policy |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Solv operating Safe and `0x8353…` (funded by Safe F) | Solv Protocol | Etherscan funding + Solv Safes | high | yes (on-chain) | Selling: 18.67M SOLV into one Binance deposit on 11 Mar 2026 and 21 Nov 2025 pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] BSC logs: every SOLV `Transfer` to and from the genesis Safe, the five vesting Safes, `0xccbc…`, `0x0bd8…`, `0xe4a8…`, `0x5030…`, `0xef12…`, `0x5e75…` and their second hops (NodeReal public `eth_getLogs`); block timestamps, `balanceOf`, `totalSupply` and Safe `getOwners()`/`getThreshold()` via BSC RPC; read 16 Nov 2026 ~5:30–7:45 AM MST
- [Tier A] Etherscan v2 API `tokentx` for Ethereum SOLV (all 398 transfers) and `getsourcecode` for both token contracts, 16 Nov 2026
- [Tier B] Etherscan name tags for the same addresses ("Binance 51", "Binance Deposit", "Binance 14", "Bybit: Wallet 16", "Binance: Cold Wallet"), 16 Nov 2026; GoPlus BSC token security (holder count, top holders)
- [Tier A] [DefiLlama Solv Protocol](https://defillama.com/protocol/solv-protocol) fees, revenue, holders revenue and TVL, 16 Nov 2026
- [Tier A] [Solv tokenomics docs](https://docs.solv.finance/solv-token/solv-tokenomics) · [vSOLV docs](https://docs.solv.finance/solv-token/vsolv-campaign) · [BRO post-incident review](https://insights.solv.finance/post-incident-review-bro-vault-incident-and-strengthened-security-commitments/)
- [Tier B] [DarkNavy](https://www.darknavy.org/web3/exploits/solv-bro-double-mint/) · [Halborn](https://www.halborn.com/blog/post/explained-the-solv-hack-march-2026) · [Alea Q4 2025](https://alearesearch.io/reports/benchmark/solv-q4-2025) · AlphaGrowth and Tokenomist unlock calendars
- [Tier B] Arkham, read 16 Nov 2026 ~7:19–7:20 AM MST (signed-in account): Bithumb Hot Wallet [0x0995…](https://intel.arkm.com/explorer/address/0x09958d2ace12f464b8ed02b26fc756a55e51a4c5) · OKX Blockdream Ventures (fund) [0x78db…](https://intel.arkm.com/explorer/address/0x78db576873f032a7c4749b214a8af6966b3be239) · unnamed Gnosis Safes [0x5e75…](https://intel.arkm.com/explorer/address/0x5e75298a82b758308706cff215c2b99d1af155a6), [0xccbc…](https://intel.arkm.com/explorer/address/0xccbc5f15d91f474a37c171d6de51815946d21fd0) · unlabelled EOAs [0x1478…](https://intel.arkm.com/explorer/address/0x1478f63a183553b77dbc41458443450271c1565c), [0x0bd8…](https://intel.arkm.com/explorer/address/0x0bd8ab88ec2b8d672d6dcafba571bc79430bf4eb), [0xe4a8…](https://intel.arkm.com/explorer/address/0xe4a84981da2122e265ed2adf20467c8f63c3ad6e), [0x5030…](https://intel.arkm.com/explorer/address/0x50301ce376e7e66ffc07ee442dbcff5b34d332c1), [0xef12…](https://intel.arkm.com/explorer/address/0xef12417df03f2722a2baed3111c7b6a4347d2fd7), [0x8353…](https://intel.arkm.com/explorer/address/0x83536027de14d96e9d34382c825263be9b305f40), [0x50b4…](https://intel.arkm.com/explorer/address/0x50b47fffc9fdbcaf0c218988bc1424cc9cb8e892). Token filter is Enterprise-only; first transfer page only
- [Tier A] Follow-up BSC logs after the Arkham pass (NodeReal `eth_getLogs`, read 16 Nov 2026 ~8:00–8:30 AM MST): every SOLV transfer out of `0x8353…` (Oct 2025 – Mar 2026), into and out of `0x78db…` (Dec 2025 – Apr 2026, Nov 2026) and out of `0xe4a8…` (10–16 Nov 2026); Safe F `getOwners()`/`getThreshold()`/`balanceOf`
- [Tier A] CoinGecko `solv-protocol` market data (16 Nov 2026 5:26 AM MST); Gate SOLV/USDT daily candles
- [Unverified] who controls `0x1478…`, `0x5030…`, `0x0bd8…`, `0xe4a8…`, `0x8353…` (Arkham: unlabelled); whether the repeated 18.67M deposits and the 31.5M fund payments are vesting payouts; which allocation each Safe holds; BRO buyers and their lockups

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Fixed supply, no mint, no owner (BSC and ETH) | [BSC code](https://bscscan.com/address/0xabe8e5cabe24cb36df9540088fd7ce1175b9bc52#code) · [ETH code](https://etherscan.io/address/0x169e36f327caa83d004f5c2668ac25a1424c940d#code) · [ETH 1.26B mint](https://etherscan.io/tx/0x5567bfdb79460625f861bc5502822d4d139f696ea06259e7d833fa93ab459538) | A | 16 Nov 2026 |
| Genesis Safe funded vesting Safe A with 2.424B on 13 Feb 2025 | [tx](https://bscscan.com/tx/0xfeb1cfd9e5cf4e2a1f759dd7236f2a40423b5fe864b50e074d0ad628c3ddbab5) · [genesis Safe](https://bscscan.com/address/0x8749b13fe36c72b745f948f91fb2ffec3b63bf75) | A | 16 Nov 2026 |
| Safe B releases 210M at a time to `0xccbc…` | [16 Mar](https://bscscan.com/tx/0x9e28322ea4f723b2a52871457274047dd9e7a0458aeb28ada3fb987dcd00f297) · [4 Jun](https://bscscan.com/tx/0xf43efe2f68dd59d07c0b1236affa8b1fcb97892ef55cd75204d9ee749161632c) · [18 Aug](https://bscscan.com/tx/0x7fe8af7eae3222f9e1dd5c467d603c6857956d9b0868d5958848222b0feac61e) · [18 Sep 2026](https://bscscan.com/tx/0xe6c1b046f43f446c8eebcc558defe4d6ac2823481ca30a5ae40a35721b4bf15e) | A | 16 Nov 2026 |
| 428.7M from `0xccbc…` to single-key EOA `0x1478…` | [tx](https://bscscan.com/tx/0x9effa554016dbb1a88ea87f1f8620cb14ea6598fd2737d01eac19cda387f626b) | A | 16 Nov 2026 |
| 11 Mar 2026 pump day: Safe `0xccbc…` 18.67M → Binance deposit | [tx](https://bscscan.com/tx/0x5d6279473fb13bf3dd3191db4ae6e79cf84d6a4a7d613922df490a99310630da) · [deposit](https://bscscan.com/address/0x7d3217feb6f310f7e7b7c8ee130db59dcad1dd45) | A + B tag | 16 Nov 2026 |
| 21 Nov 2025 pump day: Safe F-funded `0x8353…` 18.67M → same Binance deposit (plus 30 Oct, 30 Dec, 26 Jan) | [21 Nov](https://bscscan.com/tx/0x760d09c52377b99205bbe4c2a094e36204ea94512e8ae843f69fd6315c4bd998) · [30 Oct](https://bscscan.com/tx/0x09132bc0c484959540a235c271c9058252f14589e200dc07537795c0cbdfaf1b) · [30 Dec](https://bscscan.com/tx/0xbbdee2189f28e72b0403e681f9fe5beb89f39d144d6ad1b2bd7e89c326ae5fc2) · [26 Jan](https://bscscan.com/tx/0x33ed32819fbac1e5779b02847286d00eb3bdd456185e44fc8ff3890f14e92013) · [Arkham](https://intel.arkm.com/explorer/address/0x83536027de14d96e9d34382c825263be9b305f40) | A + B | 16 Nov 2026 |
| 0x5e75 is a 4-of-5 Safe with the vesting Safes' signers | [`0x5e75…55a6`](https://bscscan.com/address/0x5e75298a82b758308706cff215c2b99d1af155a6) (`getOwners()`, `getThreshold()` on BSC RPC) · [Arkham](https://intel.arkm.com/explorer/address/0x5e75298a82b758308706cff215c2b99d1af155a6) | A + B | 16 Nov 2026 |
| 2 Apr 2026 31.5M pump-day deposit = investor fund wallet; funded by Solv operator 28/31 Mar; paid 31.499M again 14 Nov 2026 | [28 Mar](https://bscscan.com/tx/0x960b582ff86acf424e26ede8fcb356c406906ef6eca2cc168f29c6497e7e1f66) · [31 Mar](https://bscscan.com/tx/0x87f7591dd8c889099f525614d07ddedda40e73adb1ebdced7ab0814ef0ef33c0) · [2 Apr deposit](https://bscscan.com/tx/0xf8c9cbc1269ed6fbbe0de738c4305146474d683ce28ecccf424994cefbc7ed27) · [sweep to Binance 51](https://bscscan.com/tx/0x6734f7a5b41620c575f150958907ababcf3458b79606b0d15c0e4e6be3d3923a) · [14 Nov](https://bscscan.com/tx/0x42e2db072248b43053f1ad6055cbfd1199bd72f5d93c1f5475f3804e95b6c095) · Arkham [OKX Blockdream Ventures](https://intel.arkm.com/explorer/address/0x78db576873f032a7c4749b214a8af6966b3be239) | A + B | 16 Nov 2026 |
| 0x0995 is a Bithumb Hot Wallet | [Arkham](https://intel.arkm.com/explorer/address/0x09958d2ace12f464b8ed02b26fc756a55e51a4c5) | B | 16 Nov 2026 ~7:20 AM MST |
| Megadrop 588M (7%) to Binance at launch | [tx](https://bscscan.com/tx/0x4bcadcd751cf44ebf42c33da57e88f19f34c7ce6670d1527f0df6b2078233d83) | A | 16 Nov 2026 |
| Solv-funded EOAs → Binance deposits, Sep–Oct 2026 | [0x0bd8 → 0x3f84](https://bscscan.com/tx/0x76aca588b89fe5dd6ccbee0b0d5b62c842b58bea978bbcf4b2f92ca5273f2957) · [0xe4a8 → 0x1b20](https://bscscan.com/tx/0x4f96075c8b916192e762957b97e4faf955db9c4c572f962e5cfe0bc5d0061c75) · [0xe4a8 → 0x7d32](https://bscscan.com/tx/0x573b569fa688838b06b8ad4ff0eda352782cbc8d20abfa7084e2e5607672598b) | A + B tag | 16 Nov 2026 |
| 0x0bd8 funded by `0xccbc…`; returned 210M to Safe B | [return tx](https://bscscan.com/tx/0xfd3dddf74f14af75746ede587f09de2d825ef7afd49bf207ecf4008479044452) · [0x0bd8](https://bscscan.com/address/0x0bd8ab88ec2b8d672d6dcafba571bc79430bf4eb) | A | 16 Nov 2026 |
| BRO tranche distribution on Ethereum (840M, 420M) incl. 5 Sep 2026 pump-day disperse | [840M](https://etherscan.io/tx/0xaed921884d5620d89db1d133e242fa7d7b48021e5bad6539f524cd721d6407f6) · [420M](https://etherscan.io/tx/0x89fd0e88183f8156b9760fa7243677930e6241e16e059c2745e063f97fbf4529) · [disperse](https://etherscan.io/tx/0x09f6dddad0669c156e53fc05c20a6cc79b9926189b0fc579218e85925ccf11fe) | A | 16 Nov 2026 |
| ETH 50M → Binance deposit on 6 Jul 2026 | [tx](https://etherscan.io/tx/0x1d5e67376f2de0ad4caac056e64190f914bcf43e802aca45bdc15f6efdee2094) | A + B tag | 16 Nov 2026 |
| ETH 71.9M `0xccbc…` → `0x0bd8…` → `0x5030…` | [21 Sep](https://etherscan.io/tx/0xd67240305b0bcaca881296734ee1a28903576c3d231ac3a814e7af967cb4d0b7) · [19 Oct 2026](https://etherscan.io/tx/0x8e7c212a5fe720ed415c442e8f61ca4ecffd9b251f25a3da67da4a43f8d25e46) | A | 16 Nov 2026 |
| BRO exploit ~$2.7M, repaid | [Solv review](https://insights.solv.finance/post-incident-review-bro-vault-incident-and-strengthened-security-commitments/) · [DarkNavy](https://www.darknavy.org/web3/exploits/solv-bro-double-mint/) | A + B | 16 Nov 2026 |
| Revenue $12.23M (1y), holders $0, TVL $439.4M | [DefiLlama](https://defillama.com/protocol/solv-protocol) | A | 16 Nov 2026 |
| vSOLV buyback from 2.5% supply, ended 17 Mar 2026 | [docs](https://docs.solv.finance/solv-token/vsolv-campaign) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026** (first transfer page per wallet). Named: `0x0995…` = Bithumb Hot Wallet; `0x78db…` = OKX Blockdream Ventures (fund). Corrected: `0x5e75…` is a Safe. Still unlabelled: `0x1478…`, `0x0bd8…`, `0xe4a8…`, `0x5030…`, `0xef12…`, `0x8353…`, `0x50b4…`; Arkham names no Solv entity on `0xccbc…` or Safe F | Ask Solv to publish its wallet list; Arkham Enterprise token filter for full histories | Free / paid |
| 2 | **Which allocation does each 4-of-5 Safe hold?** | Match each Safe's balance and release rhythm to the docs' allocation table; ask Solv to publish its wallet list | Free |
| 3 | **Are the repeated 18.67M deposits vesting payouts?** | Ask Solv whether `0x7d32…` belongs to a vesting beneficiary; check whether the amount equals a fixed monthly share of one bucket | Free |
| 4 | ~~Who funded `0x78db…` before its 2 Apr 2026 pump-day deposit?~~ **Closed:** Solv's operator `0x50b4…` paid it 31.5M via disperse on 28 and 31 Mar 2026; Arkham labels it OKX Blockdream Ventures. Investor flow, not counted as team selling (see Selling) | Still open: the fund's vesting terms; whether its 14 Nov 2026 31.499M reaches an exchange | Free |
| 5 | **BRO buyers and lockups; size of future BRO tranches (42M vs 420M in the docs)** | Ask Solv; watch for new SOLV deployments | Free |
| 6 | **Confirm the unlock calendar with a second source on-chain** | Watch the Safes around 17 Nov and 18 Dec 2026 | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
