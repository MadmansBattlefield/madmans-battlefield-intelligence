---
ticker: QNT
name: Quant
chain: ethereum
contract: "0x4a220E6096B25EADb88358cb44068A3248254675"
overall_score: 4.3
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 1
  tokenomics_supply: 2
  liquidity_market: 7
  product_development: 6
  adoption_customers: 8
  security_audits: 3
  regulatory: 5
  catalysts: 6
gates_failed: [selling_behavior]
red_lines:
  hack_exploit: none
  mint_path_live: "yes (crowdsale owner EOA 0xf5e3… can still mint new QNT; simulated 16 Nov 2026, not executed)"
  team_wallet_to_exchange_during_pump: "yes (Etherscan 'Quant: Team Wallet 1' sent 350,000 QNT into exchange deposit addresses on 5 pump days, Jul–Sep 2021; plus 200,000 via wallets it funded on 4 more pump days, Mar–May 2021; no disclosure found)"
  unattributed_cluster_pump_day_flow: "30 Sep 2026 (0x7513 'QNT Whale' -> Galaxy Digital OTC -> Kraken hot wallet / B2C2 / Binance; cluster descended from Team Wallet 2 via Bitcoin Suisse; owner [Unverified])"
  founder_wallet_pump_day_move: "29 Sep 2026 (Arkham 'Quant Network: Founder' 0x48e9 moved 25,776 QNT to a Quant-labelled wallet; no exchange deposit seen. Quant-funded 0x8266 moved 22,807, of which 1,000 reached Coinbase on 30 Sep)"
  team_funds_to_broker_deposit: "yes (1.18M QNT into Arkham 'Quant Network — Bitcoin Suisse Deposit' 0x86c0, 2022; ~1.22M swept to Bitcoin Suisse in Jun 2023; sale not provable on-chain)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Customers may pay in dollars and nothing forces buying; the token gets no share of the company's revenue. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "the daily closes cited in the body (2021 pump days)"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 155.5
price_source: "CoinGecko, 16 Nov 2026 3:50 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### QNT · Overall grade **4.3 / 10 · ❌ FAIL**

**Summary:** Quant Network Ltd is a real, audited, profitable UK software company (£11.5M revenue, FY to Sep 2025), and The Clearing House and seven UK banks now run on its tech. But the token is optional to that business (customers can pay in USD). A **Quant team wallet** (labelled by both Etherscan and Arkham) sent 350,000 QNT into exchange deposit addresses on five 2021 pump days, and Arkham files the wallets it funded to sell another 1.07M under Quant Network too. And the 2018 crowdsale contract still lets one plain key mint new QNT, which contradicts the "fixed supply" story.

**🚨 Top warning (red line):** Etherscan's **"Quant: Team Wallet 1"** [`0xc5ae…b420`](https://etherscan.io/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420) sent **350,000 QNT (≈ $94M at those days' closes) into exchange deposit addresses on five pump days** in 2021: 26 Jul (+23.7%), 18 Aug (+18.9%), 6 Sep (+73.9%), 7 Sep (+90.2%) and 14 Sep (+19.3%). Arkham also files this wallet as "Quant Network: Team Wallet", and puts the three wallets it funded, which sold another 1.07M QNT through a Bittrex deposit address (200k of it on four more pump days), under its Quant Network entity ([Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account)). No disclosure was found. Check it yourself: [6 Sep, 50k in](https://etherscan.io/tx/0xd999be6d3d59d22fe2f78f381f92f9737f15990570eba77b9cd9dd0fbd829fc5) → [swept to Coinbase 12 two minutes later](https://etherscan.io/tx/0x532df3ab75b0de5faef2a8df80f74a4db54a914a3997eaef1acfcf8be8239992) · [7 Sep, 50k → "Binance Deposit"](https://etherscan.io/tx/0xfa29d38bd76f0cc995bae0ce4f4dd5e09b0361912bdd7e7dd7c6c93da8219fa7) · [14 Sep, 50k → Binance Deposit](https://etherscan.io/tx/0x8af3c88fc9ba13d36ab79932eb6f5361d0ed62404e44af02f0386d4f2e2d7c8c) · [Team Wallet 1 on Etherscan](https://etherscan.io/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420) · [on Arkham](https://intel.arkm.com/explorer/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420) · [seller `0x416b…` on Arkham](https://intel.arkm.com/explorer/address/0x416b992c5ced9cb4d9996882af8c847aa2c53488). **Second warning:** the crowdsale [`0x398e…46f7`](https://etherscan.io/address/0x398e41ac3d5972b4bac2320cd130c7a25ca446f7) is still owned by the single key [`0xf5e3…c4bc`](https://etherscan.io/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc) ("Quant: Deprecated Deployer" on Etherscan, ["Quant Network: Deployer" on Arkham](https://intel.arkm.com/explorer/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc)). A simulation on 16 Nov 2026 shows that key can still mint new QNT. Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 7/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 8/10 | ✅ PASS |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 QNT · Quant · 4.3 / 10 · ❌ FAIL

> **One line:** Quant Network Ltd is a real, audited, profitable UK software company (£11.5M revenue, FY to Sep 2025), and The Clearing House and seven UK banks now run on its tech. But the token is optional to that business (customers can pay in USD). A **Quant team wallet** (labelled by both Etherscan and Arkham) sent 350,000 QNT into exchange deposit addresses on five 2021 pump days, and Arkham files the wallets it funded to sell another 1.07M under Quant Network too. And the 2018 crowdsale contract still lets one plain key mint new QNT, which contradicts the "fixed supply" story.

| 📊 Market (CoinGecko, 16 Nov 2026 3:50 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $155.5 | **Token** [`0x4a22…4675`](https://etherscan.io/address/0x4a220E6096B25EADb88358cb44068A3248254675) "StandardToken", Solidity 0.4.21, not a proxy |
| **24h / 7d / 30d** 🟢 +2.2% / 🔴 −22.3% / −23.8% · 1y +84.4% | **`totalSupply()`** reports a hardcoded 45,467,000 (wrong; see Tokenomics) |
| **Market cap** $2.263B · **FDV** $2.272B | **Supply outside the contract** 14,880,362.19 · CoinGecko / Quant 14,612,493 |
| **24h volume** $64.1M | **Burn** 9,550,896.84 QNT held by the token contract itself (no way out) |
| **ATH** $427.42 (11 Sep 2021) · now −63.6% | **Mint path** crowdsale [`0x398e…46f7`](https://etherscan.io/address/0x398e41ac3d5972b4bac2320cd130c7a25ca446f7), owner EOA [`0xf5e3…c4bc`](https://etherscan.io/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc) |
| **Holders** 196,807 (Blockscout) | **Labelled team wallets** TW1 25,938.84 · TW2 0 · deployer 1.00001 · Arkham ["Quant Network: Founder"](https://intel.arkm.com/explorer/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) 599,999 |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Quant Network Ltd turnover, FY to 30 Sep 2025 | **£11,515,582** (FY24 £10,704,062, +7.6%) | [Tier A] [Companies House 09798383, full audited accounts, filed 6 Jul 2026](https://find-and-update.company-information.service.gov.uk/company/09798383/filing-history/MzUyOTUwOTAxNGFkaXF6a2N4/document?format=pdf&download=0), p13 |
| Gross / operating / after-tax profit | £9,761,148 / £1,794,454 / £1,545,899 | [Tier A] same filing, p13 |
| Revenue type | 100% "Licence fees and service agreements", all arising in the UK (note 4) | [Tier A] same filing |
| Customer concentration | "A significant proportion of revenue" from a small number of clients (strategic report) | [Tier A] same filing, p4–5 |
| Cash at year end | £7,867,037 | [Tier A] same filing, p14 |
| Revenue paid to QNT holders | **None by contract.** The FAQ says "You can pay your platform fee in USD, or you can subscribe with QNT" | [Tier A] [Quant FAQ](https://quant.network/frequently-asked-questions/) |
| Fusion Rollup gas paid in QNT | Live since 2 Jun 2026; fee volume **not measured** this pass | [Tier A] [Quant news](https://quant.network/news/a-new-category-of-infrastructure-the-fusion-rollup-is-live-on-mainnet/) · volume [Unverified] |

**What it means:** The company makes real, audited money and is profitable. The token gets no share of it. Paying in QNT is optional and nothing forces buying, so ~$2.3B of market cap sits on top of a ~£11.5M-a-year software business that can be paid in dollars. Better than a token with no business behind it (4, not 3). Fusion gas is the one direct token sink, and it is unmeasured.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Customers may pay in dollars and nothing forces buying; the token gets no share of the company's revenue. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Operating company | **Quant Network Ltd** (England & Wales, 09798383). Sole director Gilbert Verdian (founder). Auditor MAH, Chartered Accountants. 44 staff, R&D £445,714 | [Tier A] [Companies House](https://find-and-update.company-information.service.gov.uk/company/09798383) |
| Parent | **Quant Group Corporation Ltd** (12299977, formerly Quant Network Holdings). FY25 unaudited small accounts: investments ~£871k, no revenue. Director David Gregg Yates appointed 9 Oct 2024 | [Tier A] [Companies House 12299977](https://find-and-update.company-information.service.gov.uk/company/12299977) · [FY25 accounts](https://find-and-update.company-information.service.gov.uk/company/12299977/filing-history/MzUyOTUwOTAxN2FkaXF6a2N4/document?format=pdf&download=0) |
| Who controls the parent | PSC: **Ogier Global Trustee (Jersey) Ltd as trustee of the Goulding Trust** (since 1 Apr 2022). The people who benefit are not public | [Tier A] Companies House PSC register |
| Founder wallet | Arkham labels [`0x48e9…a170`](https://intel.arkm.com/explorer/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) **"Quant Network: Founder"** with a Team Wallet tag. It holds 599,999 QNT ([Etherscan](https://etherscan.io/address/0x48e9af81fb93d144ad4683fcf219974c8304a170)). Whose wallet it is personally is not shown | [Tier A] balance · [Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account) |
| Token issuer | **QNT Services AG**, Switzerland (per the MiCA white paper). Swiss register not read this pass | [Tier A] [MiCA white paper](https://assets.bitstamp.net/docs/whitepaper/Quant_2026_05_13.xhtml) · Swiss registry [Unverified] |

**What it means:** A named founder, a UK company filing audited accounts, and a named token issuer. That is far better than most. But the parent is held through a Jersey trust, and the token entity (Swiss) is separate from the revenue company (UK). Neither publishes which wallets hold the company's QNT.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket | QNT | Notes |
|---|---:|---|
| Retained at sale (to the deployer, 25 Jun 2018) | 14,467,000 | [mint tx](https://etherscan.io/tx/0x29d451f4cbe9e3dae283d6e79186346fb211ac727ee1ffc625f22ba1eab9f770). Equals the MiCA paper's 31.81% "retained" (13.67% team/advisors + 18.13% reserve), pre-burn |
| Burned by the deployer, 14 Sep 2018 | 9,545,765.95 | [burn tx](https://etherscan.io/tx/0x763f32a09916193139e03bd0c97967c7c9eb9e085d677e3940d8b726ea4c8605) (sent into the token contract) |
| Left for team/reserve after the burn | **~4.92M (≈ 33.7% of today's supply)** | Deployer → [Team Wallet 2](https://etherscan.io/address/0x1f1e4f2219ee0b805f67a23f5f4daaf95165a126) 3,584,225.5 on 8 Jun 2019 ([tx](https://etherscan.io/tx/0xac64cd4b092980c68d617544f8a78984f5227c28ad5832bfcc6ad7915686f64c)). The rest went in 20k–161k sends to individuals in 2018–2019 |
| Team Wallet 2 → Team Wallet 1 | 2,559,754.71 | 8 Jun 2019 ([tx](https://etherscan.io/tx/0x93fa03997795ae4787767aaea2bc271a5d08192b8b0211cf93c6fdcfa4f232ca)) |
| Team Wallet 2 → [`0x86c0…50f6`](https://etherscan.io/address/0x86c046866bad93f9890850f52880044d22ce50f6) | 1,024,460.83 | 4 Apr 2022 ([tx](https://etherscan.io/tx/0x67c91cae9bcddf42b6ee46e7fe86ed94106770e6b82e273f88961cb189a73dcd)); then to Bitcoin Suisse in Jun 2023 |
| **Labelled Quant wallets today** | **25,939.84** | TW1 25,938.84 · TW2 0 · deployer 1.00001 |
| `0x86c0…50f6` identified ([Arkham](https://intel.arkm.com/explorer/address/0x86c046866bad93f9890850f52880044d22ce50f6)) | 1,178,473.72 in | Arkham labels `0x86c0…` **"Quant Network — Bitcoin Suisse Deposit"**: a deposit address at a broker/custodian. It also got 154,012.89 from [`0xd1ba…ed00`](https://intel.arkm.com/explorer/address/0xd1baf518c3ffda991ae1ed16ce1f94ec9875ed00) (Arkham: Quant Network) the same day ([tx](https://etherscan.io/tx/0x39ce5afd8238e5b9d6281226479f109d1dbeb99782b7842aa75e890e79c3b40e)), and swept ~1.22M to Bitcoin Suisse's hot wallet in Jun 2023 [Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account) · [Tier A] chain. **Whether Bitcoin Suisse sold it for Quant is not visible on-chain** |
| Arkham "Quant Network: Founder" [`0x48e9…a170`](https://etherscan.io/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) | **599,999** (4.1%) | Funded 16 Oct 2018 with 625,775 from [`0x3070…ad9f`](https://intel.arkm.com/explorer/address/0x30701834bec7f362ff52b22199e6a7469ba8ad9f) (Arkham: Quant Network) ([tx](https://etherscan.io/tx/0xeb273c757034652c82506b22d3aca2df9c21731a4016187d8abbbdaad94daefe)). [Arkham](https://intel.arkm.com/explorer/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) |
| [`0x8266…d78b`](https://etherscan.io/address/0x826678aD6b1aaa5e1f20E079333D9b66ab22d78b) (#2 holder; Arkham "QNT Whale", no entity) | **600,000** (4.1%) | Funded the same day by the same Quant Network address, 622,806 ([tx](https://etherscan.io/tx/0x5e9688c42ff86fbb7f26a46038ab010d61ca8b0bfb10bb572be54cdd17704cba)). Owner [Unverified]. [Arkham](https://intel.arkm.com/explorer/address/0x826678ad6b1aaa5e1f20e079333d9b66ab22d78b) |
| Other Arkham "Quant Network" wallets | 47,152 | [`0xd13d…1a1d`](https://intel.arkm.com/explorer/address/0xd13d3c5f29579b17a0a9d1c88c6a4ebf6ac61a1d) 30,376 (funded by TW1) · [`0x2071…b65a`](https://intel.arkm.com/explorer/address/0x2071fd0bcbc6e076aef49bb598946bb37c48b65a) 16,776 (funded by the founder wallet on 29 Sep 2026) |
| On Quant Network Ltd's balance sheet | **nil** | Intangible assets nil, so no crypto is held there [Tier A] FY25 accounts p14 |

**What it means:** About 4.9M QNT was kept for the team and reserve after the 2018 burn. Arkham now ties about **1.27M QNT (≈ 8.7% of supply)** to Quant: the founder wallet, the Quant-funded 600k wallet, two smaller Quant Network wallets and TW1. Almost all of it sits in two plain wallets of ~600k each, with no lock, and both moved coins on the 29 Sep 2026 pump day (see Selling). About 1.18M of team funds went into Quant's own Bitcoin Suisse deposit in 2022. That points to a broker sale or custody, but neither can be proven on-chain. Quant itself still publishes none of these wallets. The score stays **3**: we now know more about where the coins are, but the concentration is high, nothing is locked, and none of it is disclosed by the issuer. Where the rest sits is **not disclosed**. The #3 holder ([`0x7513…4c57`](https://etherscan.io/address/0x7513ae7e87290094b17b35e26cdb537170634c57), 454,798) descends from Team Wallet 2 through a Bitcoin Suisse account. Attribution: [Unverified].

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

**A. Team Wallet 1 straight into exchange deposit addresses (Etherscan label "Quant: Team Wallet 1")**

| Day (UTC) | Route | QNT | Close / 5-day change | Pump? |
|---|---|---:|---:|---|
| 26 Jul 2021 | TW1 → Bittrex deposit [`0x09f7…effd`](https://etherscan.io/address/0x09f7cb22c7d521e76c72cb166ff6efc7ec03effd) ([in](https://etherscan.io/tx/0x775a06c256eb72ed297704239e69490b8ce7b948586f6ab183c1bd6a9b8df522) · [swept to Bittrex](https://etherscan.io/tx/0x89c03c9489e88a8d4ac0c7ee904a8198aee972ec6722aeb0b1975451128fc2ee)) | 50,000 | $90.84 / +23.7% (KuCoin) | 🔴 Yes |
| 18 Aug 2021 | TW1 → Bittrex deposit ([in](https://etherscan.io/tx/0xa87f3ee9188f02f99e9a616cd447e0904841e2f0ce928015d3d36fef2af79fa7) · [sweep](https://etherscan.io/tx/0x0a0477d4e51a47cbf3e21bcf7c461823277df7f2275b5f623610109ddf0b8ce5)) + TW1 → [`0x0e1e…d14b`](https://etherscan.io/address/0x0e1e31db1f1a2cba2e865d25d3b378ecb2c7d14b) ([in](https://etherscan.io/tx/0x6d700346be6bb920dcce28694cb8f8803f449d15e08bb4cc63ec7e2bceddd9d1) · [→ KuCoin 3](https://etherscan.io/tx/0x5d14476f40b6dbeede936bc4dce03e65bbaf11eac293c8486c507483ea55d479)) | 100,000 | $182.8 / +18.9% | 🔴 Yes |
| 6 Sep 2021 | TW1 → [`0x49e1…0d40`](https://etherscan.io/address/0x49e1a437b7b6ffef9301ad04f0072bc181db0d40) ([in](https://etherscan.io/tx/0xd999be6d3d59d22fe2f78f381f92f9737f15990570eba77b9cd9dd0fbd829fc5) · [→ Coinbase 12 in 2 min](https://etherscan.io/tx/0x532df3ab75b0de5faef2a8df80f74a4db54a914a3997eaef1acfcf8be8239992)) | 50,000 | $326.1 / +73.9% | 🔴 Yes |
| 7 Sep 2021 | TW1 → "Binance Deposit" [`0x3df4…18d1`](https://etherscan.io/address/0x3df4cbb5f22e736034da170c453c2beec6b618d1) ([in](https://etherscan.io/tx/0xfa29d38bd76f0cc995bae0ce4f4dd5e09b0361912bdd7e7dd7c6c93da8219fa7)) | 50,000 | $355.0 / +90.2% | 🔴 Yes |
| 14 Sep 2021 | TW1 → [`0xb313…c4f8`](https://etherscan.io/address/0xb313b7549fc1d671a732003e01bf796d8ba1c4f8) ([in](https://etherscan.io/tx/0x5b606fbb31946661559347f7a5dc1fb66ea9faa45f63c59aca6e3b57f41090cd) · [→ Coinbase 12](https://etherscan.io/tx/0x1fc8096848955742c630db453879008f1e5d545aee9b57cb669e4e774efb3721)) + TW1 → Binance Deposit ([in](https://etherscan.io/tx/0x8af3c88fc9ba13d36ab79932eb6f5361d0ed62404e44af02f0386d4f2e2d7c8c); swept 100,100 to [Binance 14](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60) on 25 Sep, [tx](https://etherscan.io/tx/0xac9f7974d265a60c691919af8dad581a51ad4a3846873db13c653d7259626751)) | 100,000 | $374.2 / +19.3% | 🔴 Yes |
| 6 Nov 2021 | TW1 → "Wintermute: Multisig" [`0x4f3a…cb81`](https://etherscan.io/address/0x4f3a120e72c76c22ae802d129f599bfdbc31cb81) ([tx](https://etherscan.io/tx/0x2eef6fda841f78c672b362e3b3348089233011345d60bd45499cc4c2564d6ce1)) | 24,995 | −6.4% | No (market maker) |
| 18 Jan 2022 | TW1 → [`0xb3f9…ef5b`](https://etherscan.io/address/0xb3f923eabaf178fc1bd8e13902fc5c61d3ddef5b) ([in](https://etherscan.io/tx/0xd6e4f5705b9edaf16c0cb6d582a2bfa204faaad3e5c25745490a97c30ca189fb) · [→ Binance 14 on 20 Jan](https://etherscan.io/tx/0xcc5321cbc94ccce6943fec24bd0450fb2cd2c50fef4f925fb83cb4d9e8db993d)) | 99,990 | −11.6% | No |

- **Pump-day total from TW1: 350,000 QNT ≈ $94.3M** at those days' closes. Each big send was preceded by a 100 QNT test send to the same deposit address, e.g. [6 Sep test](https://etherscan.io/tx/0xb7ca282e16fca044272ebd52f1d98295908a45e3e9cc4f8a728d401c5dc73bbc).
- **What the deposit addresses are:** `0x49e1…`, `0xb313…` and `0x3df4…` received only from TW1 and swept everything to Coinbase 12 / Binance 14. `0x3df4…` carries Etherscan's "Binance Deposit" tag. `0x09f7…` is a "UserWallet" contract that sweeps every inflow (many unrelated senders) to Etherscan's "Bittrex" [`0xfbb1…bb98`](https://etherscan.io/address/0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98) within minutes. `0xb3f9…` has 1,077 transfers, all swept to Binance 14. `0x0e1e…` forwards everything to "KuCoin 3" [`0xa1d8…3fbf`](https://etherscan.io/address/0xa1d8d972560c2f8144af871db508f0b0b10a3fbf). [Tier A] pattern plus Etherscan tags on the hot wallets. Arkham's counterparty labels agree: "Bittrex Deposit" for `0x09f7…` and "KuCoin Deposit" for `0x0e1e…`, and it names TW1 "Quant Network: Team Wallet" ([Arkham](https://intel.arkm.com/explorer/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420); [Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account)). So TW1 is now confirmed by two Tier B label sources.

**B. Wallets funded by TW1 that sold on pump days.** TW1 sent 100,000-QNT chunks to [`0x416b…3488`](https://etherscan.io/address/0x416b992c5ced9cb4d9996882af8c847aa2c53488), [`0xaee5…d03b`](https://etherscan.io/address/0xaee54821da31e1ce50d50aa748720f15cbc9d03b) and [`0x524e…c93b`](https://etherscan.io/address/0x524e034609972c7354bc2d3714e9a3bd72f9c93b) in Jun 2020 – Mar 2021. Those three paid **1,070,000 QNT into the Bittrex deposit `0x09f7…`** in 50k lots. `0x524e…` also received **1,151 ETH straight from the deployer** on 8 Jun 2019 ([tx](https://etherscan.io/tx/0x6fe94d15fbdb0d877881bc7cc840f7ca8e9e5774fb9c7ac6db65dccc9a656e77)), which ties it to Quant's own wallets. **Arkham files all three under its Quant Network entity** ([`0x416b…`](https://intel.arkm.com/explorer/address/0x416b992c5ced9cb4d9996882af8c847aa2c53488) · [`0xaee5…`](https://intel.arkm.com/explorer/address/0xaee54821da31e1ce50d50aa748720f15cbc9d03b) · [`0x524e…`](https://intel.arkm.com/explorer/address/0x524e034609972c7354bc2d3714e9a3bd72f9c93b); [Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account)). It shows `0x524e…`'s first funder as Team Wallet 2, and its 1,151 ETH going on to a Bitcoin Suisse deposit. The on-chain funding (Tier A) plus the Etherscan and Arkham labels make these **Quant-controlled wallets**. Which person or entity held the keys is still not shown. [`0xd1ba…ed00`](https://intel.arkm.com/explorer/address/0xd1baf518c3ffda991ae1ed16ce1f94ec9875ed00), also filed under Quant Network, sent 31k to another Bittrex deposit (Arkham counterparty totals; dates not read). Four of those lots fell on pump days (KuCoin closes):

| Day | Wallet → Bittrex deposit | QNT | 5-day change |
|---|---|---:|---:|
| 9 Mar 2021 | `0x416b…`, 3 minutes after receiving 100k from TW1 ([TW1 → 0x416b](https://etherscan.io/tx/0xb1efa1005af54f821c93086210c78cfb9d83401dea26b88df80d4216f0a99107) · [→ Bittrex deposit](https://etherscan.io/tx/0x8f0f28b6f9a0dbee943eeb8206c7f684d42436ec4c304245b08ad7b747bf705a)) | 50,000 | +32.4% |
| 17 Mar 2021 | `0xaee5…` ([tx](https://etherscan.io/tx/0x40c43bd0e480ebb4b7b9d9ebff1f8317fcf0ccf7283c3ba0ca07eef074db702f)) | 50,000 | +21.6% |
| 30 Apr 2021 | `0x524e…` ([tx](https://etherscan.io/tx/0x620b8bf7c87616e5679a7cb8f89094327b3c374213ce5dda8cac2962c431e98a)) | 50,000 | +17.4% |
| 13 May 2021 | `0xaee5…` ([tx](https://etherscan.io/tx/0xf1366c91f0cc595da4eeddba7f079541bafdb1535ccd890dc83b232465067b7f)) | 50,000 | +43.2% |

- **All in, the TW1 cluster put at least ~1.75M QNT (≈ 12% of today's supply) into exchange deposit addresses between Apr 2020 and Jan 2022.** That counts 1,295,000 to Bittrex, 158,000 to KuCoin, 200,000 in Sep 2021 to Coinbase/Binance and 99,990 to Binance in Jan 2022. Days before 29 Jul 2021 could only be pump-tested on KuCoin closes (from 7 Feb 2021). Sends from Apr 2020 to early Feb 2021 could not be tested.

**C. Last 12 months.** TW1's only move was 42,377 QNT to unlabelled [`0xd13d…1a1d`](https://etherscan.io/address/0xd13d3c5f29579b17a0a9d1c88c6a4ebf6ac61a1d) on 10 Oct 2025 ([tx](https://etherscan.io/tx/0xa8ec56b0a1281cdc37a4079f64d807b1d2ce314152dc4ac40e587f1d0bc588a0)). That wallet still holds 30,376 and sent 12,002 to unlabelled [`0x278f…0cb8`](https://etherscan.io/address/0x278fa35721e7d22eaf0b5485fdf86d3a69360cb8) on 6 and 10 Oct 2026 (not pump days). Separately, **on the 30 Sep 2026 pump day (+196.4%)**, the Team-Wallet-2-descended cluster moved QNT toward exchanges:
- [`0xdf3b…8eb6`](https://etherscan.io/address/0xdf3b5a5b7af53ac8dda95b55fb7822152da98eb6) → `0x7513…` 492,721 ([tx](https://etherscan.io/tx/0x246a91620d5cd1715501ef937af375bf0c9bb454bd6b9d864077fc182cfa2f89)).
- `0x7513…` → [`0x434a…45ac`](https://etherscan.io/address/0x434aaa7c02874e614149ad572a05cffd007145ac), which Arkham labels **Galaxy Digital** (an OTC desk; it also shows an "Ethereum First Funder: B2C2 Group?" tag) ([Arkham](https://intel.arkm.com/explorer/address/0x434aaa7c02874e614149ad572a05cffd007145ac)), 20,000 + 30,000 ([tx](https://etherscan.io/tx/0x652e9b6ba9d0932301ab4654d072ab7b1f522961e53b41b13468d69c19f2c82b) · [tx](https://etherscan.io/tx/0x98ad1c0705fd0336a8ad929897101e54fb305206057559c6107ab9abde88f3b7)).
- `0x434a…` then split three ways:
  - 15,000 → [`0xa29e…4ff5`](https://etherscan.io/address/0xa29e963992597b21bcdcaa969d571984869c4ff5) ([tx](https://etherscan.io/tx/0x294f97e2012d50da913be8bb5e3d5094f3eeba768209f49f3f6cfbe58c912fee)), which sent 10,990 to "B2C2 Group 1" ([tx](https://etherscan.io/tx/0x7671f10f838812114cfe3b3430ee5af78bfb56b77767df5774adcaee1147b7ac)).
  - 10,000 → [`0x755f…afd3`](https://etherscan.io/address/0x755f3318f9ee4b5c0928158088078a14134fafd3) ([tx](https://etherscan.io/tx/0x53fe47be8f5bc7fd405e7543b2a2b928e70105cc7efe5893b71208647099e963)), which passed it on to [`0x88d5…1e72`](https://etherscan.io/address/0x88d5c89f6356c8c9c39ed325165793cb41dd1e72) ([tx](https://etherscan.io/tx/0x94306ebf86798d1dc13201c10060e62bed9e49b2fa5f25fe43e50da684f05c12)). Arkham labels `0x88d5…` **"Kraken: Hot Wallet"** ([Arkham](https://intel.arkm.com/explorer/address/0x88d5c89f6356c8c9c39ed325165793cb41dd1e72)), and on-chain it pays Etherscan's Kraken 245/246.
  - 12,411.48 → a BitGo forwarder ([tx](https://etherscan.io/tx/0x2f3d5d53636089434ec4faf06c08b9d9f00f9134440983501818ac172f731620)). After four more hops (mixed with other coins) it reached a "Binance Deposit" and then [Binance 14](https://etherscan.io/tx/0x11450a7b2c54a95d16457a2dcfc7ee41c1ab381225f3abb8734bd984bc67f5d0).
- So the pump-day route was **`0x7513…` → Galaxy Digital OTC → Kraken hot wallet / B2C2 / Binance**.
- **Whose wallets `0x7513…` and `0xdf3b…` are is still [Unverified].** Arkham shows both only as unlabelled "QNT Whale" wallets ([`0x7513…`](https://intel.arkm.com/explorer/address/0x7513ae7e87290094b17b35e26cdb537170634c57) · [`0xdf3b…`](https://intel.arkm.com/explorer/address/0xdf3b5a5b7af53ac8dda95b55fb7822152da98eb6)). Their named counterparties are Bitcoin Suisse (hot wallet and the [`0x8c45…`](https://intel.arkm.com/explorer/address/0x8c4558543804b97221ff37bb903e13b8aeb1a46f) address) and the prime broker Elwood ([`0x7e8b…`](https://intel.arkm.com/explorer/address/0x7e8bada55b156a03378ad1bab48039e4f88e594c)). They look like a client account at Bitcoin Suisse, but that client is not identified.

**D. Quant-linked wallets on the 29–30 Sep 2026 pump days** (both pump days, with five-day rises near +190%):
- Arkham's **"Quant Network: Founder"** wallet [`0x48e9…`](https://etherscan.io/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) sent **25,776 QNT** on 29 Sep to [`0x2071…b65a`](https://etherscan.io/address/0x2071fd0bcbc6e076aef49bb598946bb37c48b65a) (Arkham: Quant Network) in four transfers ([first 9,999](https://etherscan.io/tx/0x03742c70b689bd3c142a04abf62b0b5c7869154183c41330a5764ee93293fa71)). `0x2071…` then sent 9,000 in 1,000 lots to fresh [`0x0ac8…183a`](https://etherscan.io/address/0x0ac84b6a4b964b8a59ea40d8ce1be9da75a8183a), which still holds it. **No exchange deposit seen.**
- The Quant-funded 600k wallet `0x8266…` sent **22,807 QNT** on 29 Sep to fresh [`0x5802…247e`](https://etherscan.io/address/0x580205378c034877b30f495ad550275a0f66247e) ([9,999 tx](https://etherscan.io/tx/0xf283e920c0b194f3d7279bcf389a7292b386488289e9e4e43fc917b3cdc83aa2)). That wallet moved 12,807 to fresh [`0x9fc0…c703`](https://etherscan.io/address/0x9fc0c58c46316194862435aa34abbf66b1fbc703) (still held). It also sent **1,000 QNT on 30 Sep** to [`0x823a…344c`](https://etherscan.io/address/0x823a2a29326846c95642eebd2b013abe82f4344c) ([tx](https://etherscan.io/tx/0xff7147a2f17f7ffa859e315827523148a3db6b9827b6117f209df061c597832b)), which swept it to Coinbase 10 / "Coinbase: Hot Wallet" [`0xa9d1…3e43`](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) four minutes later ([tx](https://etherscan.io/tx/0x949a6c51b5b8e0f7106399bdca2f2be332c64a6678a69a00b8ec4c0c82073e96)).
- The many zero-value transfers from these wallets to look-alike addresses are address-poisoning spam, not moves by the owner.
- **Other unlabelled whale:** [`0x9e86…efdd`](https://intel.arkm.com/explorer/address/0x9e86b2299a73208ab7196be3148f77a88825efdd) (235,000; Arkham "QNT Whale", no entity) got its coins in Aug 2022 from `0xded9…`, downstream of the deployer branch. Arkham shows it paying Gate and Binance deposits. On-chain it sent 19,990 to the Gate deposit [`0x5c71…cd5b`](https://etherscan.io/address/0x5c7197e9f132d77647fe3cca2c97a52a4055cd5b) on the **26 Nov 2025 pump day** (+18.6%) ([tx](https://etherscan.io/tx/0x089f46655635a99740285e438f0e78dff30e007bc02a11a8065ecf03172e743a)). Owner [Unverified].

**What it means:** The rule is plain: a team wallet selling on a pump day, or funding a wallet that does, without disclosure, fails Selling. The labelled Quant team wallet did it on five days, and the wallets it funded did it on four more. It is old (2021), and the labelled wallets are now nearly empty, so the risk going forward is lower than the score suggests. But the scale (≈ 12% of supply into exchanges) and the repeated pump timing put it at **3**, which **trips the Selling gate**. **Arkham update:** the 2020–21 sellers are now filed under Quant Network, so the finding is stronger: these were Quant's own wallets, not outside buyers. The score stays at 3 rather than 2. The verified-Quant wallets' 2026 pump-day moves went into fresh wallets, and only 1,000 QNT, from the Quant-funded but unattributed `0x8266…` branch, reached an exchange. The large 2026 pump-day flow came from wallets Arkham does not tie to Quant.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **3 → 1**. Pump days from the daily closes cited in the body (2021 pump days).

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: the labelled team wallet route runs through an OTC desk to exchanges, and Quant has published no OTC, market-making or payout program covering it. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- **Four different supply numbers:**
  - `totalSupply()` returns a **hardcoded 45,467,000** that never changes ([source](https://etherscan.io/address/0x4a220E6096B25EADb88358cb44068A3248254675#code)).
  - Minted on-chain: 24,431,259.03 (608 mints, all on 25 Jun 2018). Less the 9,550,896.84 sitting in the token contract, **14,880,362.19** is outside it.
  - CoinGecko / Quant: **14,612,493**.
  - MiCA white paper: "**capped at 14,881,364** … no additional tokens can be created".
  - Blockscout circulating: 14,556,178.
  - The ~268k gap between the on-chain figure and Quant's figure is not explained [Unverified].
- **"No additional tokens can be created" is not true in code.** The token's `mint()` is restricted to the crowdsale contract, and that contract is still controlled by one EOA. See Security for the simulation.
- **Allocation (MiCA paper):** 68.19% sold at the TGE, 31.81% retained (pre-burn). The burn came entirely out of the retained share.
- **No vesting contract.** Team tokens sat in plain wallets and were moved at will (see Holdings and Selling).

## 💧 Liquidity & market · 7/10 · ✅ PASS

- $64.1M of volume in 24h on a $2.26B cap (≈ 2.8% turnover). Listed on Binance, Coinbase, Kraken, Upbit, Crypto.com, Bitpanda and others (exchange wallets are among the top holders).
- Thin before the September run: Binance QNT/USDT traded about $0.7M a day before the pump, and $240M on 28 Sep 2026. 34 of the last 360 days were pump days, clustered in late Nov 2025, Jan–Apr 2026, 22–24 Aug and 23 Sep – 4 Oct 2026 (peak +289% on 28 Sep). 29 Oct was also one.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- **Overledger** (API gateway to many ledgers, **closed source**) and the **Fusion Rollup**, live on mainnet 2 Jun 2026 ([Quant news](https://quant.network/news/a-new-category-of-infrastructure-the-fusion-rollup-is-live-on-mainnet/)). QNT is used for Fusion gas and Trusted Node staking; staking parameters are not published [Unverified].
- GitHub `quantnetwork`: 15 public repos, **only 1 pushed in the last 90 days** (op-geth, 7 Oct 2026). Most of the work is closed, so it can't be checked from outside.
- The company spends real money on it (44 staff, R&D £445,714 in FY25).

## 🤝 Adoption & customers · 8/10 · ✅ PASS

| Customer | What happened | Confirmed by both sides? |
|---|---|---|
| The Clearing House (US) | Quant selected as tech provider for the **On-Chain Money Initiative** (tokenised deposits, linked to RTP and CHIPS). Network expected **H1 2027** | ✅ [TCH](https://www.theclearinghouse.org/payment-systems/Articles/2026/09/The-Clearing-House-Partners-with-Quant-to-Advance-the--On-Chain-Money-Initiative) · [Quant](https://quant.network/press-releases/the-clearing-house-partners-with-quant-to-advance-the-on-chain-money-initiative/), 24 Sep 2026 |
| UK Finance GBTD | First **live retail transactions** in tokenised sterling deposits on the Quant-built platform: Barclays, HSBC UK, Lloyds, Monzo, Nationwide, NatWest, Santander | ✅ [UK Finance](https://www.ukfinance.org.uk/tokenised-sterling-deposits-gbtd-initiative) · Quant, Sep 2026 |

**What it means:** Real, named, top-tier bank customers, confirmed by the customers themselves. **Neither announcement mentions QNT.** The banks are buying Quant's software, not the token.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- **Live mint path, tested.** The crowdsale [`0x398e…46f7`](https://etherscan.io/address/0x398e41ac3d5972b4bac2320cd130c7a25ca446f7) state as of 16 Nov 2026:
  - `owner()` is the EOA [`0xf5e3…c4bc`](https://etherscan.io/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc) (Etherscan "Quant: Deprecated Deployer"; Arkham ["Quant Network: Deployer"](https://intel.arkm.com/explorer/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc), type Contract Deployer, [Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account); nonce 817). Its last outgoing transaction was on 8 Jun 2019 ([tx](https://etherscan.io/tx/0x6fe94d15fbdb0d877881bc7cc840f7ca8e9e5774fb9c7ac6db65dccc9a656e77)); since then it has only received two zero-value transactions from others (16 Feb 2024, [11 Dec 2024](https://etherscan.io/tx/0xc7f69504449963ca0eac4fd60a0f36d4d1ed170fbd010e95b5de5f82414a109c)). Neither label source shows who holds this key now [Unverified].
  - `inSale` and `inPresale` are both false.
  - `totalPresaleTokensSold` is 8,533,112.51 against a 15M cap.
  - The owner can call `recordPresalePurchase` (no sale-state check), `enableSale` + `buyTokens`, or `endPresale()` repeatedly, which raises the regular cap each time.
- **Simulation** (`eth_simulateV1`, public RPC, ~block 26,427,101, 16 Nov 2026 3:50 AM MST, **not executed on-chain**):
  - The owner calls `recordPresalePurchase(owner, 1000e18)`, then `transferTokensWithOffsetAndLimit(0, 1)`.
  - The owner's QNT balance goes from 1.00001 to **1,001.00001**, with a `Transfer` from 0x0. `totalSupply()` still reads 45,467,000.
  - The same `mint` called from a random address reverts.
- The **MiCA white paper (H.5)** says "no evidence is publicly available confirming whether this minting path remains operationally active". This simulation is that evidence.
- **Audit:** [EtherAuthority, 14 May 2024](https://etherauthority.io/wp-content/uploads/2024/05/Quant-Token.pdf). It passed the contract, but its informational findings include "an unbounded minting capability with no maximum supply cap" via the crowdsale-only mint path. Blockworks' filing treats supply as fixed, with no new tokens since the 2018 TGE. That is true so far, but the code still allows new minting.
- No exploit of the token contract or of Quant-held funds was found. Blockworks lists two third-party exchange incidents ([filing](https://blockworks.com/token-transparency/filing/quant)).

**What it means:** One old, single-signature key could mint new QNT at any time. It has not been used to mint since 2018, but nothing in code stops it. Moving ownership to a dead address or a multisig would close this.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- **MiCA white paper** notified on 13 May 2026 by the trading platform **Bitstamp Europe S.A.** (Luxembourg), on its own initiative ([document](https://assets.bitstamp.net/docs/whitepaper/Quant_2026_05_13.xhtml)). That is a notification, not an authority's approval, and it was filed by an exchange, not the issuer.
- UK operating company files full audited accounts. No FCA, FINMA or other licence for Quant or QNT Services AG was checked this pass. Not proven either way.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| H1 2027 | The Clearing House On-Chain Money network opens to institutions (no QNT role announced) |
| ~Jul 2027 | Quant Network Ltd FY26 accounts due at Companies House (FY25 filed 6 Jul 2026) |
| Ongoing | Fusion Rollup usage (QNT gas) and Trusted Node staking terms (unpublished) |
| Any time | Crowdsale owner key can mint; ownership could be renounced (no announcement) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found on the token or Quant-held funds |
| Team wallet → exchange during a pump | 🔴 **Yes, 2021:** 350,000 QNT from "Quant: Team Wallet 1" on 5 pump days, plus 200,000 via wallets it funded on 4 more. [6 Sep](https://etherscan.io/tx/0xd999be6d3d59d22fe2f78f381f92f9737f15990570eba77b9cd9dd0fbd829fc5) · [7 Sep](https://etherscan.io/tx/0xfa29d38bd76f0cc995bae0ce4f4dd5e09b0361912bdd7e7dd7c6c93da8219fa7) · [14 Sep](https://etherscan.io/tx/0x8af3c88fc9ba13d36ab79932eb6f5361d0ed62404e44af02f0386d4f2e2d7c8c) |
| Live mint path | 🔴 **Yes:** single EOA owner of the crowdsale; simulated 16 Nov 2026. [crowdsale](https://etherscan.io/address/0x398e41ac3d5972b4bac2320cd130c7a25ca446f7) · [owner](https://etherscan.io/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc) |
| Pump-day flow from an unattributed cluster | 🟡 30 Sep 2026, `0x7513…` ("QNT Whale") → Galaxy Digital OTC → [Kraken hot wallet](https://intel.arkm.com/explorer/address/0x88d5c89f6356c8c9c39ed325165793cb41dd1e72) / B2C2 / Binance (owner [Unverified]). [tx](https://etherscan.io/tx/0x652e9b6ba9d0932301ab4654d072ab7b1f522961e53b41b13468d69c19f2c82b) |
| Founder / Quant wallets moving on a pump day | 🟡 29–30 Sep 2026: [founder wallet](https://intel.arkm.com/explorer/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) 25,776 → Quant wallet (no exchange seen); `0x8266…` branch 1,000 → [Coinbase](https://etherscan.io/tx/0x949a6c51b5b8e0f7106399bdca2f2be332c64a6678a69a00b8ec4c0c82073e96) |
| Team funds into a broker deposit | 🟡 1.18M QNT into ["Quant Network — Bitcoin Suisse Deposit"](https://intel.arkm.com/explorer/address/0x86c046866bad93f9890850f52880044d22ce50f6) (2022); sale not provable on-chain |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Quant: Team Wallet 1 | Quant team | Etherscan name tag + funding | high | yes | Selling: 350,000 QNT into exchange deposits on 2021 pump days, plus funded wallets on four more |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API: `tokentx` full history for Team Wallet 1, Team Wallet 2, the deployer, every relay and deposit address named above; `getsourcecode` for the token and the crowdsale; read 16 Nov 2026 MST
- [Tier A] Ethereum RPC (publicnode): crowdsale state reads and `eth_simulateV1`, 16 Nov 2026 3:50 AM MST; `eth_getLogs` for all 608 mint events and the 22 Sep – 4 Oct 2026 window (378,915 logs)
- [Tier B] Etherscan name tags read from each address page, 16 Nov 2026: "Quant: Deprecated Deployer", "Quant: Team Wallet 1", "Quant: Team Wallet 2", "Binance Deposit", "Binance 14", "Binance: Cold Wallet 28", "Coinbase 12", "Coinbase 10", "Bittrex", "KuCoin 3", "Wintermute: Multisig", "B2C2 Group 1", "Bitcoin Suisse 1", "Copper 4/5/45", "Kraken 245/246"
- [Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account): entity, labels and first-page counterparties for 15 addresses: [`0xc5ae…` (counterparty label)](https://intel.arkm.com/explorer/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420) · [`0x7513…`](https://intel.arkm.com/explorer/address/0x7513ae7e87290094b17b35e26cdb537170634c57) · [`0xdf3b…`](https://intel.arkm.com/explorer/address/0xdf3b5a5b7af53ac8dda95b55fb7822152da98eb6) · [`0x86c0…`](https://intel.arkm.com/explorer/address/0x86c046866bad93f9890850f52880044d22ce50f6) · [`0x7e8b…`](https://intel.arkm.com/explorer/address/0x7e8bada55b156a03378ad1bab48039e4f88e594c) · [`0x434a…`](https://intel.arkm.com/explorer/address/0x434aaa7c02874e614149ad572a05cffd007145ac) · [`0x88d5…`](https://intel.arkm.com/explorer/address/0x88d5c89f6356c8c9c39ed325165793cb41dd1e72) · [`0x8266…`](https://intel.arkm.com/explorer/address/0x826678ad6b1aaa5e1f20e079333d9b66ab22d78b) · [`0x48e9…`](https://intel.arkm.com/explorer/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) · [`0xd13d…`](https://intel.arkm.com/explorer/address/0xd13d3c5f29579b17a0a9d1c88c6a4ebf6ac61a1d) · [`0x416b…`](https://intel.arkm.com/explorer/address/0x416b992c5ced9cb4d9996882af8c847aa2c53488) · [`0xaee5…`](https://intel.arkm.com/explorer/address/0xaee54821da31e1ce50d50aa748720f15cbc9d03b) · [`0x524e…`](https://intel.arkm.com/explorer/address/0x524e034609972c7354bc2d3714e9a3bd72f9c93b) · [`0x9e86…`](https://intel.arkm.com/explorer/address/0x9e86b2299a73208ab7196be3148f77a88825efdd) · [`0xd1ba…`](https://intel.arkm.com/explorer/address/0xd1baf518c3ffda991ae1ed16ce1f94ec9875ed00) · [`0xf5e3…`](https://intel.arkm.com/explorer/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc). Counterparty totals come from Arkham's first transfer page only; dates and amounts in this report come from on-chain reads
- [Tier A] Blockscout v2: top-50 holders, holder count, circulating figure, 16 Nov 2026
- [Tier A] Companies House: [Quant Network Ltd 09798383](https://find-and-update.company-information.service.gov.uk/company/09798383) FY25 full audited accounts; [Quant Group Corporation Ltd 12299977](https://find-and-update.company-information.service.gov.uk/company/12299977) FY25 accounts and PSC register
- [Tier A] [MiCA white paper (Bitstamp Europe notification, 13 May 2026)](https://assets.bitstamp.net/docs/whitepaper/Quant_2026_05_13.xhtml)
- [Tier A] [Quant FAQ](https://quant.network/frequently-asked-questions/) · [Fusion mainnet news](https://quant.network/news/a-new-category-of-infrastructure-the-fusion-rollup-is-live-on-mainnet/) · [TCH press release](https://www.theclearinghouse.org/payment-systems/Articles/2026/09/The-Clearing-House-Partners-with-Quant-to-Advance-the--On-Chain-Money-Initiative) · [UK Finance GBTD](https://www.ukfinance.org.uk/tokenised-sterling-deposits-gbtd-initiative)
- [Tier B] [EtherAuthority audit, 14 May 2024](https://etherauthority.io/wp-content/uploads/2024/05/Quant-Token.pdf) · [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/quant)
- [Tier A] CoinGecko `quant-network` price and 365-day closes (16 Nov 2026); Binance QNT/USDT daily klines (from 29 Jul 2021); KuCoin QNT-USDT daily candles (from 7 Feb 2021)
- [Tier A] GitHub `quantnetwork` org
- [Unverified] owner of the `0x7513…`/`0xdf3b…` cluster (Arkham: unlabelled "QNT Whale"); owner of `0x8266…` and `0x9e86…`; who holds the deployer key; whether Bitcoin Suisse sold the 1.18M deposited by Quant; where the rest of the ~4.9M team/reserve QNT is; the ~268k supply gap; Fusion staking terms; whether the 2021 sales were disclosed; any licences

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Team Wallet 1 is Quant's (Etherscan tag) and was funded from the deployer via Team Wallet 2 | [TW1](https://etherscan.io/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420) · [TW2](https://etherscan.io/address/0x1f1e4f2219ee0b805f67a23f5f4daaf95165a126) · [deployer → TW2](https://etherscan.io/tx/0xac64cd4b092980c68d617544f8a78984f5227c28ad5832bfcc6ad7915686f64c) · [TW2 → TW1](https://etherscan.io/tx/0x93fa03997795ae4787767aaea2bc271a5d08192b8b0211cf93c6fdcfa4f232ca) | A chain + B tag | 16 Nov 2026 |
| Arkham files TW1, the three Bittrex sellers and `0xd1ba…` under Quant Network | [TW1](https://intel.arkm.com/explorer/address/0xc5aef1adf58e895cd7cdc0fa50786f45ac14b420) · [0x416b](https://intel.arkm.com/explorer/address/0x416b992c5ced9cb4d9996882af8c847aa2c53488) · [0xaee5](https://intel.arkm.com/explorer/address/0xaee54821da31e1ce50d50aa748720f15cbc9d03b) · [0x524e](https://intel.arkm.com/explorer/address/0x524e034609972c7354bc2d3714e9a3bd72f9c93b) · [0xd1ba](https://intel.arkm.com/explorer/address/0xd1baf518c3ffda991ae1ed16ce1f94ec9875ed00) | B (Arkham) + A funding | 16 Nov 2026 ~4:28 AM MST |
| 26 Jul 2021 pump day: 50k TW1 → Bittrex deposit | [in](https://etherscan.io/tx/0x775a06c256eb72ed297704239e69490b8ce7b948586f6ab183c1bd6a9b8df522) · [sweep](https://etherscan.io/tx/0x89c03c9489e88a8d4ac0c7ee904a8198aee972ec6722aeb0b1975451128fc2ee) · [deposit](https://etherscan.io/address/0x09f7cb22c7d521e76c72cb166ff6efc7ec03effd) · [Bittrex](https://etherscan.io/address/0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98) | A | 16 Nov 2026 |
| 18 Aug 2021 pump day: 100k TW1 → Bittrex + KuCoin | [Bittrex in](https://etherscan.io/tx/0xa87f3ee9188f02f99e9a616cd447e0904841e2f0ce928015d3d36fef2af79fa7) · [Bittrex sweep](https://etherscan.io/tx/0x0a0477d4e51a47cbf3e21bcf7c461823277df7f2275b5f623610109ddf0b8ce5) · [KuCoin leg in](https://etherscan.io/tx/0x6d700346be6bb920dcce28694cb8f8803f449d15e08bb4cc63ec7e2bceddd9d1) · [→ KuCoin 3](https://etherscan.io/tx/0x5d14476f40b6dbeede936bc4dce03e65bbaf11eac293c8486c507483ea55d479) | A | 16 Nov 2026 |
| 6 Sep 2021 pump day: 50k TW1 → Coinbase 12 | [test 100](https://etherscan.io/tx/0xb7ca282e16fca044272ebd52f1d98295908a45e3e9cc4f8a728d401c5dc73bbc) · [in](https://etherscan.io/tx/0xd999be6d3d59d22fe2f78f381f92f9737f15990570eba77b9cd9dd0fbd829fc5) · [→ Coinbase 12](https://etherscan.io/tx/0x532df3ab75b0de5faef2a8df80f74a4db54a914a3997eaef1acfcf8be8239992) · [Coinbase 12](https://etherscan.io/address/0x503828976d22510aad0201ac7ec88293211d23da) | A | 16 Nov 2026 |
| 7 and 14 Sep 2021 pump days: 100k TW1 → "Binance Deposit", swept to Binance 14 | [7 Sep in](https://etherscan.io/tx/0xfa29d38bd76f0cc995bae0ce4f4dd5e09b0361912bdd7e7dd7c6c93da8219fa7) · [14 Sep in](https://etherscan.io/tx/0x8af3c88fc9ba13d36ab79932eb6f5361d0ed62404e44af02f0386d4f2e2d7c8c) · [sweep](https://etherscan.io/tx/0xac9f7974d265a60c691919af8dad581a51ad4a3846873db13c653d7259626751) · [deposit](https://etherscan.io/address/0x3df4cbb5f22e736034da170c453c2beec6b618d1) | A + B tag | 16 Nov 2026 |
| 14 Sep 2021 pump day: 50k TW1 → Coinbase 12 | [in](https://etherscan.io/tx/0x5b606fbb31946661559347f7a5dc1fb66ea9faa45f63c59aca6e3b57f41090cd) · [→ Coinbase 12](https://etherscan.io/tx/0x1fc8096848955742c630db453879008f1e5d545aee9b57cb669e4e774efb3721) | A | 16 Nov 2026 |
| 18 Jan 2022 (not a pump day): 99,990 TW1 → Binance 14 | [in](https://etherscan.io/tx/0xd6e4f5705b9edaf16c0cb6d582a2bfa204faaad3e5c25745490a97c30ca189fb) · [→ Binance 14](https://etherscan.io/tx/0xcc5321cbc94ccce6943fec24bd0450fb2cd2c50fef4f925fb83cb4d9e8db993d) | A | 16 Nov 2026 |
| TW1-funded wallets sold 1.07M via Bittrex, 4 lots on pump days | [9 Mar fund](https://etherscan.io/tx/0xb1efa1005af54f821c93086210c78cfb9d83401dea26b88df80d4216f0a99107) · [9 Mar sell](https://etherscan.io/tx/0x8f0f28b6f9a0dbee943eeb8206c7f684d42436ec4c304245b08ad7b747bf705a) · [17 Mar](https://etherscan.io/tx/0x40c43bd0e480ebb4b7b9d9ebff1f8317fcf0ccf7283c3ba0ca07eef074db702f) · [30 Apr](https://etherscan.io/tx/0x620b8bf7c87616e5679a7cb8f89094327b3c374213ce5dda8cac2962c431e98a) · [13 May](https://etherscan.io/tx/0xf1366c91f0cc595da4eeddba7f079541bafdb1535ccd890dc83b232465067b7f) | A | 16 Nov 2026 |
| Live mint path; simulated mint of 1,000 QNT | [crowdsale code](https://etherscan.io/address/0x398e41ac3d5972b4bac2320cd130c7a25ca446f7#code) · [owner EOA](https://etherscan.io/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc) · [crowdsale creation](https://etherscan.io/tx/0x25be97ce12c6c5fb47f6f009596914d83dd938c2a8117b7bdd539fcf0b481cc6) · [token code](https://etherscan.io/address/0x4a220E6096B25EADb88358cb44068A3248254675#code) | A (code + simulation) | 16 Nov 2026 3:50 AM MST |
| Retained 14,467,000 and burned 9,545,765.95 in 2018 | [mint to deployer](https://etherscan.io/tx/0x29d451f4cbe9e3dae283d6e79186346fb211ac727ee1ffc625f22ba1eab9f770) · [burn](https://etherscan.io/tx/0x763f32a09916193139e03bd0c97967c7c9eb9e085d677e3940d8b726ea4c8605) · [token creation](https://etherscan.io/tx/0xae16f475aa5968cd36a491f1c22afa095bd3fe527074df382eb373b2853c337c) | A | 16 Nov 2026 |
| TW2 → `0x86c0…` → Bitcoin Suisse → `0xdf3b…` → `0x7513…` (#3 holder) | [TW2 → 0x86c0](https://etherscan.io/tx/0x67c91cae9bcddf42b6ee46e7fe86ed94106770e6b82e273f88961cb189a73dcd) · [0x86c0 → BS1](https://etherscan.io/tx/0x2a323373bcdb2b3049bb9aa456ff4884ded1dedc375e49ca2c919f36e9866d40) · [BS1 → 0xdf3b](https://etherscan.io/tx/0x6684307f31fa2341003317762fd2bcee64d27e7afcbd55d8d5669fb85e0f866e) · [0x7513](https://etherscan.io/address/0x7513ae7e87290094b17b35e26cdb537170634c57) | A chain · owner [Unverified] | 16 Nov 2026 |
| 30 Sep 2026 pump-day flow from that cluster toward exchanges | [0xdf3b → 0x7513](https://etherscan.io/tx/0x246a91620d5cd1715501ef937af375bf0c9bb454bd6b9d864077fc182cfa2f89) · [→ 0x434a](https://etherscan.io/tx/0x98ad1c0705fd0336a8ad929897101e54fb305206057559c6107ab9abde88f3b7) · [→ B2C2](https://etherscan.io/tx/0x7671f10f838812114cfe3b3430ee5af78bfb56b77767df5774adcaee1147b7ac) · [→ Binance 14](https://etherscan.io/tx/0x11450a7b2c54a95d16457a2dcfc7ee41c1ab381225f3abb8734bd984bc67f5d0) | A chain · owner [Unverified] | 16 Nov 2026 |
| "Quant Network: Founder" wallet holds 599,999; it and the 600k `0x8266…` were both funded by Quant Network `0x3070…` on 16 Oct 2018 | [founder on Arkham](https://intel.arkm.com/explorer/address/0x48e9af81fb93d144ad4683fcf219974c8304a170) · [funding tx](https://etherscan.io/tx/0xeb273c757034652c82506b22d3aca2df9c21731a4016187d8abbbdaad94daefe) · [0x8266 funding tx](https://etherscan.io/tx/0x5e9688c42ff86fbb7f26a46038ab010d61ca8b0bfb10bb572be54cdd17704cba) · [0x3070 on Arkham](https://intel.arkm.com/explorer/address/0x30701834bec7f362ff52b22199e6a7469ba8ad9f) | A chain + B label | 16 Nov 2026 |
| 29–30 Sep 2026 pump days: founder wallet 25,776 → Quant wallet; `0x8266…` branch 1,000 → Coinbase | [founder → 0x2071](https://etherscan.io/tx/0x03742c70b689bd3c142a04abf62b0b5c7869154183c41330a5764ee93293fa71) · [0x8266 → 0x5802](https://etherscan.io/tx/0xf283e920c0b194f3d7279bcf389a7292b386488289e9e4e43fc917b3cdc83aa2) · [→ 0x823a](https://etherscan.io/tx/0xff7147a2f17f7ffa859e315827523148a3db6b9827b6117f209df061c597832b) · [→ Coinbase](https://etherscan.io/tx/0x949a6c51b5b8e0f7106399bdca2f2be332c64a6678a69a00b8ec4c0c82073e96) | A | 16 Nov 2026 |
| `0x86c0…` is "Quant Network — Bitcoin Suisse Deposit" (1.18M in, ~1.22M to Bitcoin Suisse hot wallet) | [Arkham](https://intel.arkm.com/explorer/address/0x86c046866bad93f9890850f52880044d22ce50f6) · [TW2 → 0x86c0](https://etherscan.io/tx/0x67c91cae9bcddf42b6ee46e7fe86ed94106770e6b82e273f88961cb189a73dcd) · [0xd1ba → 0x86c0](https://etherscan.io/tx/0x39ce5afd8238e5b9d6281226479f109d1dbeb99782b7842aa75e890e79c3b40e) | B label + A chain | 16 Nov 2026 ~4:27 AM MST |
| 30 Sep 2026 route: `0x434a…` = Galaxy Digital, `0x88d5…` = Kraken hot wallet, `0x7e8b…` = Elwood | [0x434a](https://intel.arkm.com/explorer/address/0x434aaa7c02874e614149ad572a05cffd007145ac) · [0x88d5](https://intel.arkm.com/explorer/address/0x88d5c89f6356c8c9c39ed325165793cb41dd1e72) · [0x7e8b](https://intel.arkm.com/explorer/address/0x7e8bada55b156a03378ad1bab48039e4f88e594c) | B (Arkham) | 16 Nov 2026 ~4:27–4:29 AM MST |
| `0x9e86…` (unlabelled whale) 19,990 → Gate deposit on the 26 Nov 2025 pump day | [tx](https://etherscan.io/tx/0x089f46655635a99740285e438f0e78dff30e007bc02a11a8065ecf03172e743a) · [Arkham](https://intel.arkm.com/explorer/address/0x9e86b2299a73208ab7196be3148f77a88825efdd) | A chain · owner [Unverified] | 16 Nov 2026 |
| Revenue £11,515,582, profit £1,545,899, no crypto on the balance sheet | [FY25 accounts](https://find-and-update.company-information.service.gov.uk/company/09798383/filing-history/MzUyOTUwOTAxNGFkaXF6a2N4/document?format=pdf&download=0) | A | 16 Nov 2026 |
| Mint path "no evidence … operationally active"; cap 14,881,364 | [MiCA white paper](https://assets.bitstamp.net/docs/whitepaper/Quant_2026_05_13.xhtml) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ✅ **Closed 16 Nov:** Arkham attribution of the 15 unlabelled wallets | Done ([Tier B] Arkham, read 16 Nov 2026 ~4:2x AM MST (signed-in account)). Results are folded in above. Still open from it: who owns `0x7513…`/`0xdf3b…`, `0x8266…` and `0x9e86…` (see #8) | — |
| 2 | **Were the 2021 team-wallet sales disclosed?** | Search Quant's blog, X posts and treasury statements for Jul–Sep 2021; ask Quant what Team Wallet 1 was for | Free |
| 3 | **Where is the rest of the ~4.9M team/reserve QNT?** (partly answered) | Arkham ties ~1.27M to Quant (founder 599,999, `0x8266…` 600,000, smaller Quant wallets, TW1), and 1.18M went to Quant's Bitcoin Suisse deposit. Still open: the deployer's 2018–2019 sends to individuals and the rest. Ask QNT Services AG for its wallet list | Free |
| 4 | **Will the crowdsale owner key be retired?** | Watch [`0xf5e3…`](https://etherscan.io/address/0xf5e38bbedc78efea055e0c56035adb320e64c4bc) for a `transferOwnership` to a dead address or a multisig; ask Quant. Arkham labels it "Quant Network: Deployer" but does not show who holds it | Free |
| 5 | **The ~268k supply gap** (14,880,362 on-chain vs 14,612,493 published) | Ask Quant which addresses it excludes; check balances of known dead addresses | Free |
| 6 | **Fusion gas and staking in QNT** | Read Fusion explorer fee totals and Trusted Node staking contracts once published | Free |
| 7 | **Licences** | Check the FCA register, FINMA and the Swiss commercial register for QNT Services AG | Free |
| 8 | **Who owns `0x7513…`/`0xdf3b…` (the 30 Sep seller), `0x8266…` (600k) and `0x9e86…`?** | Ask Quant and Bitcoin Suisse; watch whether Arkham adds an entity; trace `0x3070…`'s other recipients | Free |
| 9 | **Did Bitcoin Suisse sell the 1.18M Quant deposited in 2022?** | Ask Quant for the purpose of the Bitcoin Suisse account; check whether its accounts show token sale proceeds | Free |
| 10 | **What are the fresh wallets `0x0ac8…`, `0x9fc0…` and `0x5802…`** that the founder and `0x8266…` wallets funded on 29 Sep 2026? | Watch them for exchange deposits; Arkham lookup | Free (Arkham login) |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
