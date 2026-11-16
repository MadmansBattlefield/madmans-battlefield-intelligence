---
ticker: PHA
name: Phala Network
chain: ethereum
contract: "0x6c5ba91642f10282b576d91922ae6448c9d52f4e"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 0
  tokenomics_supply: 6
  liquidity_market: 6
  product_development: 6
  adoption_customers: 4
  security_audits: 5
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: fixed 1B ERC20 supply"
  team_wallet_to_exchange_during_pump: "yes: ~15.9M PHA (~$0.85M) reached Gate deposit addresses on six pump days, 18-25 Sep 2026, from Safes funded by the protocol escrow; no disclosure found"
  entity_concentration: "protocol escrow Safe holds 128.8M (12.9%)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee or revenue record; the old treasury share of mining rewards ended."
pump_day_price_source: "Gate PHA/USDT daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.03045
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PHA · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Phala shut down its Polkadot parachain in 2025 and moved PHA to an Ethereum ERC20, with vPHA as the staking and governance wrapper. The holdings left on the old chain (332.1M PHA) were bridged into one 3-of-6 Safe. That Safe funded the official PHA Assets Claimer and the vPHA rewards. It also funded a chain of other Safes that sent PHA to Gate during the September 2026 rally. No protocol fees or revenue are published, so both hard gates fail.

**🚨 Top warning:** during the **+21% to +130% pump of 18–25 Sep 2026**, Safes funded by the protocol escrow moved about **15.9M PHA (~$0.85M)** to Gate deposit addresses on six pump days. Most of it went to one Etherscan-labelled **Gate Deposit (0x053f…dfd8)**, either directly or through one or two pass-through wallets. Example: [18 Sep tx](https://etherscan.io/tx/0xea6828ecbc55a3045829aa6557d594ea43aa1cbdacbe9f2c1b65818ab24f0374) (close +21.6% vs five days earlier), [21 Sep](https://etherscan.io/tx/0x55353cae31e35ac96ad7e71f16844d0c608ca058413ab8ca4efbf6ccdfd07b46) (+81.7%). No treasury disclosure for these transfers was found. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PHA · Phala Network · 3.8 / 10 · ❌ FAIL

> **One line:** A TEE cloud with no published token revenue, whose escrow-funded Safes fed exchange deposits through a 130% pump.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x6c5ba91642f10282b576d91922ae6448c9d52f4e), 16 Nov 2026 ~8:45 AM MST) |
|---|---|
| **Price** $0.03045 | **Total supply** 1,000,000,000 PHA |
| **24h / 7d / 30d** 🟢 +3.1% / 🔴 −12.6% / −40.8% | **Circulating** 868.9M (CoinGecko) |
| **Market cap** $26.3M · **FDV** $30.3M | **Binance cold wallet** 285.1M (28.5%), an exchange, not team |
| **24h volume** $15.2M (BloFin $6.2M, WhiteBIT $1.8M, Binance $2.2M, Bithumb $1.1M) | **Protocol escrow Safe (3-of-6)** 128.8M (12.9%) |
| **ATH** $1.39 (14 May 2021) · now −97.8% | **vPHA contract** 128.9M (staked by holders) |
| **Pump days** 65 in the last year (largest +130% on 25 Sep 2026) | **Escrow inflow** 332.1M from the Sygma bridge handler, 20 Nov 2025 |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- DefiLlama has no fee or revenue record for Phala. The old model (20% of mining rewards to the treasury) ended when the parachain was shut down. No revenue figures for the TEE cloud business were found, and no mechanism sends cloud revenue to PHA holders. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee or revenue record; the old treasury share of mining rewards ended.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- A long-running core team (since 2018). Governance runs through Snapshot votes with vPHA. Signers on the escrow Safes and their thresholds are visible on-chain, but who the signers are is not disclosed. Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) gives the Safes only generic Gnosis Safe labels, with no Phala, market-maker or exchange label, so **project control stays [Unverified]**. On-chain `getOwners()` shows the three Safes share the same five signers, and the escrow Safe adds a sixth: [`0x1771…c111`](https://intel.arkm.com/explorer/address/0x1771564a5455523ded62dcd787bc4c1443c8c111), the pass-through wallet in the 📉 table.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Wallet | PHA | Note |
|---|---:|---|
| [Escrow Safe 0x4a39…ebef](https://etherscan.io/address/0x4a396b5c9a6fbc1bc0525f24ac0a246766f3ebef) (3-of-6; [Arkham: generic Safe](https://intel.arkm.com/explorer/address/0x4a396b5c9a6fbc1bc0525f24ac0a246766f3ebef)) | 128.8M (12.9%) | Received 332.1M from the bridge ([tx](https://etherscan.io/tx/0x074db62818c53f82f41f3d53aea0759a95d62ec4d2087665b70f69982a4f6a89)) and funded the labelled [PHA Assets Claimer](https://etherscan.io/tx/0x63c45d51b14fa296518291c43b3c1b64598d05f7800e5868878bf3993849f4a0) (87.7M) |
| [Safe 0x35e0…b103](https://etherscan.io/address/0x35e0316b78a1cafa165521aac961ddd60165b103) (2-of-5; [Arkham: generic Safe](https://intel.arkm.com/explorer/address/0x35e0316b78a1cafa165521aac961ddd60165b103)) | 0 now | Received 58.4M from the escrow; sent 60.7M on to 0xf32f…ecb6 on 28 Jun 2026 |
| [Safe 0xf32f…ecb6](https://etherscan.io/address/0xf32f0c04ab7496ae6de6b893889327f8c60fecb6) (3-of-5; [Arkham: generic Safe](https://intel.arkm.com/explorer/address/0xf32f0c04ab7496ae6de6b893889327f8c60fecb6)) | 0 now | The distribution Safe in the 📉 table below |

- Control is [Unverified]: none of these Safes is labelled. The link to the project is inferred from the escrow funding Phala's labelled claimer and the vPHA contract.

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

| Date | Pump (vs 5d) | Path | PHA | ≈ USD | Tx |
|---|---|---|---:|---:|---|
| 18 Sep 2026 | +21.6% | Safe 0xf32f → Gate Deposit 0x053f | 1,988,179 | $65k | [0xea68…](https://etherscan.io/tx/0xea6828ecbc55a3045829aa6557d594ea43aa1cbdacbe9f2c1b65818ab24f0374) |
| 21 Sep 2026 | +81.7% | 0xf32f → 0x1771 → Gate Deposit 0x053f | 2,867,555 | $142k | [0xf5de…](https://etherscan.io/tx/0xf5dee434b108d8112fe09c49cbd20cfff94a5d87eb3017e2f08785f85bd75c6c), [0x5535…](https://etherscan.io/tx/0x55353cae31e35ac96ad7e71f16844d0c608ca058413ab8ca4efbf6ccdfd07b46) |
| 22 Sep 2026 | +58.2% | 0xf32f → 0x1771 → Gate Deposit 0x053f | 3,117,445 | $153k | [0x5fe6…](https://etherscan.io/tx/0x5fe62a0e48b7bfea380676f027e83ca28ffcb6d056a74810138ca066a9548561), [0xe3d3…](https://etherscan.io/tx/0xe3d315ab130f16362e73b797eb89bfbf7aa18318c8b25d0b5178cfad586b3e68) |
| 23 Sep 2026 | +45.3% | 0xf32f → 0x1771 → Gate Deposit 0x053f | 2,458,576 | $117k | [0xb6c1…](https://etherscan.io/tx/0xb6c1bbc88ff12d1e0e31e9969b0c85214530495f14d39f4f1cb4e299a6469164), [0x5673…](https://etherscan.io/tx/0x567301b11e0da47cd7c934f74fd858de9794cd7459c344503401f6c33cce1ce8) |
| 24 Sep 2026 | +41.7% | 0xf32f → 0x1771 → 0xdce1 → Gate Deposit 0x053f | 3,051,547 | $156k | [0x6b0c…](https://etherscan.io/tx/0x6b0cedef325a73fd284e651671951bbd6f0e5a21e0234361af34ca7e3d9812ff), [0x3231…](https://etherscan.io/tx/0x3231e0db5dd2996835c05cea5907db73c61d3e9a60047ea9c9e3b7e8c5e61274), [0xba07…](https://etherscan.io/tx/0xba07610b9f7d2d36ad8c50a0fa0acb892295aaa4e619bba3d4ad8beb3894458c) |
| 25 Sep 2026 | +130.0% | Escrow → 0xf32f ([0xdbf6…](https://etherscan.io/tx/0xdbf6f83dec8a361b13913734e52ff5d262e6fee6d5a5a0b205fe3cd661801826)), same day 0xf32f → 0x0d15 → **Gate Deposit 0x809b** | 2,449,415 | $212k | [0xbb1d…](https://etherscan.io/tx/0xbb1d4228064fa5142b8779c88a1575b6ed462e0a4c28aa8d40ec033ec7c61fb3), [0x066e…](https://etherscan.io/tx/0x066edf5c39ce0504b022dd385ab7f6b5b3a912a8423fc6d5e5ec7f1cdc89c503) |

- Gate Deposit 0x053f…dfd8 is labelled by Etherscan. **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** `0x053f` and `0x809b` are **Gate Deposit** addresses. The 25 Sep destination is now traced: [`0x0d15…2608`](https://intel.arkm.com/explorer/address/0x0d15d5999a67084c78fa8c2fd60a799d3bfe2608) (unlabelled) forwarded 2,449,300 PHA to Gate Deposit `0x809b` 31 minutes later (Etherscan, 15:46 UTC), on the +130% day. The feeders are unlabelled: [`0x1771…c111`](https://intel.arkm.com/explorer/address/0x1771564a5455523ded62dcd787bc4c1443c8c111) is tagged **signer of the escrow Safe 0x4A3**, which `getOwners()` on [the Safe](https://etherscan.io/address/0x4a396b5c9a6fbc1bc0525f24ac0a246766f3ebef#readProxyContract) confirms, and [`0xdce1…835d`](https://intel.arkm.com/explorer/address/0xdce1fc1b7c0c27bab27f571b661aa5350adf835d) is tagged **contract deployer** and signer of another Safe (`0x277e…`); it had first received 33M PHA from Safe 0xf32f on 29 Jun 2026.
- After the window, the same route kept reaching exchanges on non-pump days (Gate closes): 0xf32f → 0x1771 → **MEXC Deposit** 2.875M on 30 Sep 2026 ([tx](https://etherscan.io/tx/0xce8b2c6784fe09aa6bf7bcbeed559c7f0f760acd610cdffe610bf380013bef2c), −8.9%) and → **KuCoin Deposit** 2.125M on 29 Oct 2026 ([tx](https://etherscan.io/tx/0x20efeda812fafa087e6ebe056662d3020cb2b50a92f293e336a03ba22798b506), −10.4%). Exchange labels are Arkham's. Every linked transaction returned status 1 (success). Prices are Binance PHAUSDT daily closes.
- This could be a disclosed market-making arrangement, but no disclosure was found. Under the rules, protocol-funded wallets depositing to an exchange on six pump days, without disclosure, score **1**.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **1 → 0**. Pump days from Gate PHA/USDT daily closes.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: no market-making or other disclosure covering these transfers was found. Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed 1B supply, about 87% circulating. The overhang is the 128.8M escrow.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $15.2M of 24h volume (58% of market cap), but 41% of it is on BloFin.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- The product moved from a parachain to TEE (confidential compute) cloud services. The token migration claim system went live in Nov 2025 (snapshot block #9064613).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- No verified usage or customer revenue figures were found.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. Token custody now depends on the Sygma bridge path and on Safe signers who are not disclosed.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- No dated catalysts. The escrow keeps sending periodic transfers (most recently 2.04M on 4 Nov 2026).

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: ~15.9M PHA over six pump days, 18–25 Sep 2026 |
| Live mint path | 🟢 None |
| Entity concentration | 🟠 12.9% in the escrow Safe |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Safe `0xf32f…` (funded by the protocol escrow) | Phala protocol escrow | Etherscan funding | high | yes (on-chain) | Selling: ~15.9M PHA to Gate deposits on six pump days, 18–25 Sep 2026 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan token, address and transaction pages (links above). Receipts, balances and Safe owner/threshold reads were made through the Etherscan API on 16 Nov 2026
- [Tier A] CoinGecko `pha`. Pump days are from Binance PHAUSDT daily closes
- [Tier A] DefiLlama fees endpoint (no Phala record)
- [Tier A] Phala forum post on the claim system (snapshot block #9064613)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): generic Safe labels on 0x4a39, 0x35e0 and 0xf32f; Gate Deposit on 0x053f and 0x809b; MEXC and KuCoin Deposit labels; signer tag on 0x1771 and deployer tag on 0xdce1. No Phala or market-maker label anywhere
- [Tier A] Etherscan API `getOwners()` on the three Safes; Gate PHA/USDT closes for the post-window transfers

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 332.1M bridged into the escrow Safe | [tx 0x074d…](https://etherscan.io/tx/0x074db62818c53f82f41f3d53aea0759a95d62ec4d2087665b70f69982a4f6a89) | A | 16 Nov 2026 |
| Escrow funded the labelled PHA Assets Claimer | [tx 0x63c4…](https://etherscan.io/tx/0x63c45d51b14fa296518291c43b3c1b64598d05f7800e5868878bf3993849f4a0) | A | 16 Nov 2026 |
| Escrow → Safe 0x35e0 (54.9M) | [tx 0x2744…](https://etherscan.io/tx/0x2744b6a3ab8ed27ebbc6bbc7f9d0cd590842a3cb3229d02c0287c76d0a1684ff) | A | 16 Nov 2026 |
| Safe 0x35e0 → Safe 0xf32f (60.7M) | [tx 0x0f1f…](https://etherscan.io/tx/0x0f1f82cd1061c8395933c1e6f95aed658afd23df48e17ec973feacced0ef0617) | A | 16 Nov 2026 |
| Pump-day Gate deposits | see the 📉 table | A | 16 Nov 2026 |
| 0x1771 signs the escrow Safe | [Safe owners](https://etherscan.io/address/0x4a396b5c9a6fbc1bc0525f24ac0a246766f3ebef#readProxyContract) · [Arkham signer tag](https://intel.arkm.com/explorer/address/0x1771564a5455523ded62dcd787bc4c1443c8c111) | A + B | 16 Nov 2026 |
| 0xdce1 is a contract deployer | [Arkham deployer tag](https://intel.arkm.com/explorer/address/0xdce1fc1b7c0c27bab27f571b661aa5350adf835d) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who the Safe signers are; is there a market maker?** | Arkham (16 Nov 2026) shows only generic Safe labels and an unlabelled signer. Ask the project for its treasury reports and signer list [Unverified] | Free account |
| 2 | **TEE cloud revenue** | Look for a published revenue figure or an on-chain payment address | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
