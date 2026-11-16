---
ticker: ACH
name: Alchemy Pay
chain: ethereum
contract: "0xed04915c23f00a313a544955524eb7dbd823143d"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 0
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 5
  adoption_customers: 4
  security_audits: 4
  regulatory: 6
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes, MinterRole with no cap; minter 0x483a0ad7be1381ca431216ca827ad38a96f0496f (3-of-6 Safe)"
  team_wallet_to_exchange_during_pump: "yes: vesting releases forwarded via a Cobo custody hot wallet to a Binance deposit on 3 pump days (23 Aug, 6 Sep, 21 Sep 2026); no disclosure found; undisclosed pump-day penalty applied (Selling 2 -> 0)"
  treasury_in_single_key_wallets: "yes: all 5 new vesting contracts are owned and revocable by EOA 0x907acf93336f034df8198c39c6707507b516bc92"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "ACH is gas and governance only; company payment revenue does not reach holders, and no fee burn, automatic buyback or fee share is live (the buyback is a proposal)."
pump_day_price_source: "Gate ACH/USDT UTC daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions:
  - address: "0xeae81df204b5beb70f6032ab173faff24c6d6990"
    label: "TokenVesting (Alchemy mint of 9 Apr 2026)"
    confidence: high
    independent_corroboration: true
    basis: "On-chain: minted by the ACH minter Safe; Arkham shows recurring releases"
  - address: "0x7d56078fa361b85ee7be627b3b3724e3e99203d2"
    label: "TokenVesting (Alchemy mint of 9 Apr 2026)"
    confidence: high
    independent_corroboration: true
    basis: "On-chain: minted by the ACH minter Safe; Arkham shows recurring releases"
  - address: "0xb8001c3ec9aa1985f6c747e25c28324e4a361ec1"
    label: "Cobo.com: Custody Hot Wallet"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan label \"Cobo: Custody\""
  - address: "0x526c7a714d27f523689022f237542664161bfbf3"
    label: "Binance Deposit"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan label"
  - address: "0x872c4832ea55687f7a3c8fe16baf0086a9bacc2c"
    label: "Binance Deposit"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan label"
  - address: "0x7196ca9fbc9760d156d301a7845d6e3f2597c3fe"
    label: "Coinbase: Cold Wallet"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x907acf93336f034df8198c39c6707507b516bc92"
    label: "Unlabelled EOA (vesting owner)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x483a0ad7be1381ca431216ca827ad38a96f0496f"
    label: "Safe with six signer tags (3-of-6 minter)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + RPC getOwners"
price_usd: 0.00372897
price_source: "CoinGecko, 16 Nov 2026 9:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ACH · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** Alchemy Pay is a real fiat on/off-ramp company (20 US money-transmitter licenses as of Nov 2026). It launched Alchemy Chain (May 2026), where ACH is the gas token. Payment revenue goes to the company, not the token, and DefiLlama tracks no fees. On **9 Apr 2026** a [3-of-6 Safe](https://etherscan.io/address/0x483a0ad7be1381ca431216ca827ad38a96f0496f) minted **5,346,246,088 ACH** in one transaction ([0x4b62b9d7…](https://etherscan.io/tx/0x4b62b9d7128e20b4663464c3e2e09149f1f77cfd3694a5354cea7f91afadf466)), the whole 2026–2037 "supply framework", into five 10-year vesting contracts. All five are **revocable by a single EOA** ([0x907a…bc92](https://etherscan.io/address/0x907acf93336f034df8198c39c6707507b516bc92)). Released ACH from them was relayed through three hops to a Cobo-custody wallet. That wallet sent it in round 5M lots to a **Binance deposit address on pump days**. Revenue and Selling both trip the hard gate.

**🚨 Top warning:** Inflation sold into strength: about 280M ACH released from the new vesting contracts since April went beneficiary → two relay hops → [0xb800…1ec1](https://etherscan.io/address/0xb8001c3ec9aa1985f6c747e25c28324e4a361ec1) (Etherscan label "Cobo: Custody") → Binance deposit [0x526c…fbf3](https://etherscan.io/address/0x526c7a714d27f523689022f237542664161bfbf3). That included 24.35M on 23 Aug, 17.8M on 6 Sep and 20M on 21 Sep 2026, all pump days. The minter has no cap, and the 5.35B vesting pool can be revoked by one key.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ACH · Alchemy Pay · 3.1 / 10 · ❌ FAIL

> **One line:** A licensed payments company, but its token is a dilution pipe that feeds Binance on pump days.

| 📊 Market (CoinGecko, 16 Nov 2026 9:11 AM MST) | 🔗 On-chain (Blockscout / RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.00373 · 1y −64.5% · ATH $0.1987 (2021) −98.1% | **Total supply** 15,346,246,088 (all minted) · 38,734 holders |
| **Market cap** not reported by CoinGecko (0) · FDV $57.2M | **New vesting pool** 33.8% of supply in 5 contracts |
| **24h volume** $2.43M: BloFin $0.79M, Binance $0.15M, Pionex, Binance TRY, Biconomy | **Minter** [3-of-6 Safe](https://etherscan.io/address/0x483a0ad7be1381ca431216ca827ad38a96f0496f) · no cap |
| **Pump days** 35 in 365 (Gate ACH/USDT) | **Vesting owner** single EOA [0x907a…bc92](https://etherscan.io/address/0x907acf93336f034df8198c39c6707507b516bc92) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama fees (alchemy-pay) / Alchemy Chain TVL | Not listed | [Tier A] api.llama.fi |
| Company payment revenue to token | None; ACH is gas and governance only | [Tier B] AInvest, Nov 2026; [Tier A] supply framework post |
| Revenue-funded buyback | Proposed only; no buyback wallet found | [Tier A] vote.alchemypay.org |

**What it means:** the business earns, the token does not. **2 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** ACH is gas and governance only; company payment revenue does not reach holders, and no fee burn, automatic buyback or fee share is live (the buyback is a proposal).

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Alchemy Pay is an operating payments company: 20 US state money-transmitter licenses, Mississippi added Nov 2026 ([TokenPost](https://www.tokenpost.com/news/regulation/48800), Tier B; company release, Tier A).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Holder | % supply | Note |
|---|---:|---|
| [0xeae8…6990](https://etherscan.io/address/0xeae81df204b5beb70f6032ab173faff24c6d6990) TokenVesting | 11.48% | minted 9 Apr 2026; 10-year linear; revocable |
| [0x7d56…03d2](https://etherscan.io/address/0x7d56078fa361b85ee7be627b3b3724e3e99203d2) TokenVesting | 9.82% | same |
| Binance cold wallets ([0x5a52…Efcb](https://etherscan.io/address/0x5a52E96BAcdaBb82fd05763E25335261B270Efcb), [0xF977…aceC](https://etherscan.io/address/0xF977814e90dA44bFA03b6295A0616a897441aceC)) | 14.83% | exchange |
| [0x7196…C3FE](https://etherscan.io/address/0x7196cA9fbC9760D156D301a7845D6e3F2597C3FE) | 7.35% | exchange: **Coinbase: Cold Wallet** per [Arkham](https://intel.arkm.com/explorer/address/0x7196cA9fbC9760D156D301a7845D6e3F2597C3FE) (outflows go to Coinbase Prime Custody); not an insider wallet |
| [0xf72e…292c](https://etherscan.io/address/0xf72ef4967506572bc5038d8399507ede1c32292c), [0x1918…4faf](https://etherscan.io/address/0x1918ecb56f69b9e4cb28c024065fec1ae4394faf), [0x174e…24f3](https://etherscan.io/address/0x174ed5f5befb9b7853ad32e5209d2b9ad22424f3) TokenVesting | 11.74% | same owner; starts Apr, Jul, Oct 2026 |

- Every vesting contract's `owner()` is the same EOA, [0x907a…bc92](https://etherscan.io/address/0x907acf93336f034df8198c39c6707507b516bc92), and `revocable()` is true. One key can claw back the unvested part of 5.35B ACH [Tier A, RPC].
- Separately, the original 10B schedule has ~30% still to unlock through Apr 2029 [Tier B, tokenomics.com].

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

*Gate ACH/USDT daily closes (UTC): 35 pump days in the last 365.*

| Step | Address | Pump-day transfers (23 Aug / 5–6 Sep / 21 Sep 2026) |
|---|---|---|
| Vesting → beneficiary | [0xeae8…6990](https://etherscan.io/address/0xeae81df204b5beb70f6032ab173faff24c6d6990) → [0x7469…e738](https://etherscan.io/address/0x7469d9a6a86692d9e576cad04233165da338e738) | [0x2f09b5a4…](https://etherscan.io/tx/0x2f09b5a4232b7be69b340710aa27d126590c2b5ea73e0d3daeba9dba97de16bb) 9.23M · [0x80fde05f…](https://etherscan.io/tx/0x80fde05f795df29704efb90712bcf3838aef1af69c4608748bcfe182140d6f3a) 6.77M · [0x3e06d8f1…](https://etherscan.io/tx/0x3e06d8f1a1f85a4a83cad009af43e6993da18cd4145965e7bbe6990e755ee40d) 7.89M |
| Vesting → beneficiary | [0x7d56…03d2](https://etherscan.io/address/0x7d56078fa361b85ee7be627b3b3724e3e99203d2) → [0xb158…c834](https://etherscan.io/address/0xb158c911c81f27f06a9cfc2ce689a75a9d32c834) | [0x56ffe3cd…](https://etherscan.io/tx/0x56ffe3cdf9b9c4d03c68b02bce152768aaaeb3059f430b773e861d9d9d5236d5) 7.90M · [0x3fded14f…](https://etherscan.io/tx/0x3fded14f00a5cca81be18801105954b46d289f440ca62bf1f3532d869939eea7) 5.79M · [0x60f5b7b7…](https://etherscan.io/tx/0x60f5b7b76b0ad81400d654bee4f749c8f78d20b3a0621967eb9deb49132bba74) 6.75M |
| Relay hop 1 | [0x7469…e738](https://etherscan.io/address/0x7469d9a6a86692d9e576cad04233165da338e738) → [0xedbe…dd73](https://etherscan.io/address/0xedbe2d46396b9617bee2bcdc083bf40f41c2dd73); [0xb158…c834](https://etherscan.io/address/0xb158c911c81f27f06a9cfc2ce689a75a9d32c834) → [0x4138…379e](https://etherscan.io/address/0x41389ba318b1c74c8b43f9a2828318c21cfc379e) | [0xeb60d471…](https://etherscan.io/tx/0xeb60d471237095bd38334159519f4db0fc5e1e7217fe6d636dfda252174e63e4) 9.24M · [0xfad86bc8…](https://etherscan.io/tx/0xfad86bc8d7dd24aab414bf15cb74eceadb95f384be5bfdfc16d403ff943df345) 7.91M |
| Relay hop 2 | [0xedbe…dd73](https://etherscan.io/address/0xedbe2d46396b9617bee2bcdc083bf40f41c2dd73) → [0x7e37…a745](https://etherscan.io/address/0x7e37eb228e1fe0af33ae80970dba5a2c5d00a745); [0x4138…379e](https://etherscan.io/address/0x41389ba318b1c74c8b43f9a2828318c21cfc379e) → [0xa71f…06ed](https://etherscan.io/address/0xa71f9751c0619818de4fa7ed110f58d89b0306ed) | [0x46aebcc4…](https://etherscan.io/tx/0x46aebcc495436e279d6174fc54e386b0fbdfda8b0c94b7778a4d57b82232ef5d) 9.24M · [0x76095f07…](https://etherscan.io/tx/0x76095f07e9a01da91d48d07c2f0f64320329b0cf792deeb48a395b12b2100a06) 12.39M |
| → Cobo-custody wallet | [0x7e37…a745](https://etherscan.io/address/0x7e37eb228e1fe0af33ae80970dba5a2c5d00a745), [0xa71f…06ed](https://etherscan.io/address/0xa71f9751c0619818de4fa7ed110f58d89b0306ed) → [0xb800…1ec1](https://etherscan.io/address/0xb8001c3ec9aa1985f6c747e25c28324e4a361ec1) | [0xfe3491dd…](https://etherscan.io/tx/0xfe3491dd136f8c6fc2fc84c82117791e971880bfd1449606bd6688d6cdb5541d) 9.24M · [0x7a575460…](https://etherscan.io/tx/0x7a575460ca369075af9d4ebd1f5a3adca875b55ba071530908e17d5c8aadd328) 12.39M · [0x7fef2396…](https://etherscan.io/tx/0x7fef23968bcc9d7f7591336e05e6839ebd00e97330f44c776067046d2a8a5d45) 10.57M |
| → **Binance deposit** | [0xb800…1ec1](https://etherscan.io/address/0xb8001c3ec9aa1985f6c747e25c28324e4a361ec1) → [0x526c…fbf3](https://etherscan.io/address/0x526c7a714d27f523689022f237542664161bfbf3) | 23 Aug: [0xb32be7d5…](https://etherscan.io/tx/0xb32be7d542d48a59a183955832c62e96cb04d09ba243b325f186e648e03a4030) 6M + 4×5M/3.35M · 6 Sep: [0x4fb28f3a…](https://etherscan.io/tx/0x4fb28f3a80cd28ae6c737843834dd10d20e226ca468b0e5541d57a105eded326) … 17.8M · 21 Sep: [0x6ff30f21…](https://etherscan.io/tx/0x6ff30f21ac80fb1e795d03bb5abd875b83c6988ab093539e77745d56386906a4) … 4×5M |
| Deposit → Binance hot wallet | [0x526c…fbf3](https://etherscan.io/address/0x526c7a714d27f523689022f237542664161bfbf3) → [0x28c6…1d60](https://etherscan.io/address/0x28c6c06298d514db089934071355e5743bf21d60) | [0xc31f25bf…](https://etherscan.io/tx/0xc31f25bff5b0452a2e3c6426eed6564b2d7704778593c6f20a4e34a713f1f542) 21M · [0x5f0e13d7…](https://etherscan.io/tx/0x5f0e13d7eea8f4900bc50c4c27aac88881438099fa7a812ff97af80989c4cb34) 17.8M · [0x3bf1500e…](https://etherscan.io/tx/0x3bf1500eee5b977ff9f0d3baca4ce8a6f5ebe555a4a7168f16c56ef8726ad95c) 20M |

- Over 365 days the Cobo wallet sent 386.6M ACH to [0x526c…fbf3](https://etherscan.io/address/0x526c7a714d27f523689022f237542664161bfbf3) and 162.9M to another Binance deposit, [0x872c…cc2c](https://etherscan.io/address/0x872c4832ea55687f7a3c8fe16baf0086a9bacc2c) (Etherscan labels).
- The relay hops are surrounded by zero-value lookalike ("address-poisoning") transfers, which this trace ignores.
- Who controls the Cobo wallet is [Unverified]; the funds trace directly from Alchemy's own vesting contracts. Arkham labels [0xb800…1ec1](https://intel.arkm.com/explorer/address/0xb8001c3ec9aa1985f6c747e25c28324e4a361ec1) **Cobo.com: Custody Hot Wallet**, a custodian wallet that also serves other clients, and names no beneficial client. It confirms both receiving addresses as **Binance Deposit** ([0x526c…fbf3](https://intel.arkm.com/explorer/address/0x526c7a714d27f523689022f237542664161bfbf3), Cobo inflows in 5M lots swept to Binance hot wallets; [0x872c…cc2c](https://intel.arkm.com/explorer/address/0x872c4832ea55687f7a3c8fe16baf0086a9bacc2c), Cobo inflows of 6.667M, 7.778M and 3 × 4.444M). The vesting pages show recurring releases ([0xeae8…6990](https://intel.arkm.com/explorer/address/0xeae81df204b5beb70f6032ab173faff24c6d6990) holds 1.762B ACH, paying [0x7469…e738](https://intel.arkm.com/explorer/address/0x7469d9a6a86692d9e576cad04233165da338e738); [0x7d56…03d2](https://intel.arkm.com/explorer/address/0x7d56078fa361b85ee7be627b3b3724e3e99203d2) holds 1.507B, paying [0xb158…c834](https://intel.arkm.com/explorer/address/0xb158c911c81f27f06a9cfc2ce689a75a9d32c834)) with no exchange counterparty of their own. Arkham does not contradict the trace [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

**What it means:** newly minted supply is delivered to Binance on pump days. Ordinary score **2**; with the undisclosed pump-day penalty below, **0 (hard gate)**.

- **Disclosure quality (16 Nov 2026 rules): silence.** Alchemy Pay published the supply framework, but no notice of these exchange deposits was found (no disclosure found). **Undisclosed pump-day penalty: applied** (Selling 2 → 0); the overall moves 3.4 → 3.1. Pump days from Gate ACH/USDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- The Feb 2026 framework promised a 10B → 10.8B rise in 2026, then ~8% a year decaying to 15.35B by 2037 ([Alchemy Pay](https://alchemypay.org/news-and-press/alchemy-chain-introduces-the-ach-supply-framework-to-power-a-stablecoin-payment-native-blockchain), Tier A). Instead, the full 5.35B was minted at once on 9 Apr 2026 ([0x4b62b9d7…](https://etherscan.io/tx/0x4b62b9d7128e20b4663464c3e2e09149f1f77cfd3694a5354cea7f91afadf466)) and parked in vesting.
- The token uses OpenZeppelin MinterRole with **no cap**: the minter Safe can mint more. **3**.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $2.43M of 24h volume; the largest venue is BloFin, with Binance second. FDV $57.2M; ~$38M market cap on about 10.3B circulating [Tier B, CoinMarketCap via AInvest].

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Alchemy Chain (stablecoin-payments L1, ACH gas) launched in 2026; no TVL tracked.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- The ramp business is live in 50+ fiat currencies. Chain-level adoption is unmeasured.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found. Control risk: uncapped minter (3-of-6 Safe) and single-EOA vesting owner [0x907a…bc92](https://etherscan.io/address/0x907acf93336f034df8198c39c6707507b516bc92). **4**.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Licensed money transmitter in 20 US states; more applications pending. No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 25 Nov 2026 | 85.3M ACH legacy unlock [Tier B] |
| Continuous | ~1.5M ACH a day linear release from the new vesting pool |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Vesting releases → Cobo custody → Binance deposit on 3 pump days; no disclosure found (penalty applied) |
| Live mint path | 🔴 MinterRole, no cap (3-of-6 Safe) |
| Treasury in single-key wallets | 🔴 5 vesting contracts owned and revocable by one EOA |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xeae8…6990](https://etherscan.io/address/0xeae81df204b5beb70f6032ab173faff24c6d6990), [0x7d56…03d2](https://etherscan.io/address/0x7d56078fa361b85ee7be627b3b3724e3e99203d2) | TokenVesting (Alchemy mint of 9 Apr 2026) | On-chain: minted by the ACH minter Safe; Arkham shows recurring releases | high | yes (on-chain mint and RPC reads) | Sets the team origin of the flow |
| [0xb800…1ec1](https://intel.arkm.com/explorer/address/0xb8001c3ec9aa1985f6c747e25c28324e4a361ec1) | Cobo.com: Custody Hot Wallet | Arkham + Etherscan label "Cobo: Custody" | high (custodian); client unknown | yes (label); client [Unverified] | Custodian hop; client not named |
| [0x526c…fbf3](https://intel.arkm.com/explorer/address/0x526c7a714d27f523689022f237542664161bfbf3), [0x872c…cc2c](https://intel.arkm.com/explorer/address/0x872c4832ea55687f7a3c8fe16baf0086a9bacc2c) | Binance Deposit | Arkham + Etherscan label | high | yes | Selling (pump-day deposits) |
| [0x7196…C3FE](https://intel.arkm.com/explorer/address/0x7196cA9fbC9760D156D301a7845D6e3F2597C3FE) | Coinbase: Cold Wallet | Arkham | medium | no | Holdings note corrected to exchange; score unchanged |
| [0x907a…bc92](https://intel.arkm.com/explorer/address/0x907acf93336f034df8198c39c6707507b516bc92) | Unlabelled EOA (vesting owner) | Arkham | low | no | None |
| [0x483a…496f](https://intel.arkm.com/explorer/address/0x483a0ad7be1381ca431216ca827ad38a96f0496f) | Safe with six signer tags (3-of-6 minter) | Arkham + RPC `getOwners` | high | yes | None (mint path) |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Cobo custody hot wallet, both Binance deposits, the Coinbase cold wallet, the two vesting contracts, the minter Safe and the vesting-owner EOA
- [Tier A] Etherscan v2 token transfers; Ethereum RPC reads (`isMinter`, `getThreshold`, `getOwners`, vesting `owner`/`beneficiary`/`revocable`/`released`); Blockscout holders and verified ABI
- [Tier A] Etherscan labels (Cobo: Custody; Binance Deposit; Binance cold wallets)
- [Tier A] [ACH supply framework](https://alchemypay.org/news-and-press/alchemy-chain-introduces-the-ach-supply-framework-to-power-a-stablecoin-payment-native-blockchain) · [governance vote page](https://vote.alchemypay.org/)
- [Tier B] [TokenPost](https://www.tokenpost.com/news/regulation/48800) · [AInvest](https://www.ainvest.com/news/alchemy-pay-adding-licenses-ach-token-falling-captures-2611/) · [tokenomics.com unlocks](https://app.tokenomics.com/tokenomics/alchemy-pay/unlocks)
- [Tier A] CoinGecko `alchemy-pay` (16 Nov 2026 9:11 AM MST); Gate ACH/USDT daily candles

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 5.35B minted in one Safe tx | [0x4b62b9d7…](https://etherscan.io/tx/0x4b62b9d7128e20b4663464c3e2e09149f1f77cfd3694a5354cea7f91afadf466) | A | 16 Nov 2026 |
| Vesting revocable by one EOA | [0x907a…bc92](https://etherscan.io/address/0x907acf93336f034df8198c39c6707507b516bc92) | A | 16 Nov 2026 |
| Cobo wallet → Binance deposit on pump days | [0xb32be7d5…](https://etherscan.io/tx/0xb32be7d542d48a59a183955832c62e96cb04d09ba243b325f186e648e03a4030) | A | 16 Nov 2026 |
| Deposit → Binance hot wallet | [0xc31f25bf…](https://etherscan.io/tx/0xc31f25bff5b0452a2e3c6426eed6564b2d7704778593c6f20a4e34a713f1f542) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham attribution of the ACH wallets** | Done 16 Nov 2026: Cobo custody hot wallet, both Binance deposits and the Coinbase cold wallet are labelled; the Cobo client is not. Ask Alchemy Pay to publish its custody and exchange wallets | Free |
| 2 | **Who is Cobo's client for these flows** | Arkham names no client [Unverified]; ask Alchemy Pay or Cobo | Free |
| 3 | **Holder of the single vesting key** | Arkham shows [0x907a…bc92](https://intel.arkm.com/explorer/address/0x907acf93336f034df8198c39c6707507b516bc92) as an unlabelled EOA first funded by [0x38F6…463F](https://intel.arkm.com/explorer/address/0x38F6CC44Fd8DddE752d84503302881a35cf6463F) (also unlabelled) [Unverified]; ask Alchemy Pay | Free |
| 4 | **Chain revenue** | Alchemy Chain explorer fee totals | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
