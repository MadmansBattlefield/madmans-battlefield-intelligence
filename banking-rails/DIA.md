---
ticker: DIA
name: DIA
chain: ethereum
contract: "0x84ca8bc7997272c7cfb4d0cd3d55cd942b3c9419"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 7
  tokenomics_supply: 7
  liquidity_market: 3
  product_development: 6
  adoption_customers: 5
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no (fixed 200M; no mint function in verified source)"
  pause_power: "no; owner 0x5737bf56559dd32d8880cfa236fe613e2162e157 (DIA Data: Deployer EOA) can only addAuditHash and transfer ownership"
  team_wallet_to_exchange_during_pump: "none found"
  treasury_in_single_key_wallets: "no: 0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0 (35.55M, 17.8%) is labelled Coinbase Prime Custody by Arkham; beneficial owner [Unverified]"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No oracle or Lasernet fee is measured and staking yield is an emission rate, so revenue does not reach holders."
pump_day_price_source: "Binance DIAUSDT UTC daily closes (Gate agrees)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0"
    label: "Coinbase Prime Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + gas-supplier funding"
  - address: "0x7170a0b768d5b2dd69188e2c7976102ac69cbc85"
    label: "Coinbase Prime Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + gas-supplier funding"
  - address: "0x05c5fe0f2ca2a46747ef7004aab502e7a031fa54"
    label: "Coinbase Prime Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + gas-supplier funding"
  - address: "0x519e6e5ea9bb4a0c779f3d9b06d86a2e561aabb2"
    label: "Coinbase Prime Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham + gas-supplier funding"
  - address: "0x5737bf56559dd32d8880cfa236fe613e2162e157"
    label: "DIA: Deployer (token owner)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + RPC owner()"
  - address: "0x0ba3171032059e9e2348b1316c36760bb87cd6ba"
    label: "Unlabelled (DIA Whale tag)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x15da7556d5ed888306839bed06f868aeaedcb0d7"
    label: "Revolut: Cold Wallet"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.1214
price_source: "CoinGecko, 16 Nov 2026 9:56 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### DIA · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** DIA is an oracle network that runs on its own Ethereum L2 rollup, Lasernet. DIA is Lasernet's gas token, and holders stake it as wDIA [Tier A]. Supply is fixed at **200M with no mint function**, and **31.27M (15.6%) is burned** at the dead address. Most of the burn came from unsold bonding-curve tokens in 2020 [Tier A, RPC and transfers]. Oracle fees are not measured. DefiLlama tracks no DIA fees, and staking yield is an emission rate DIA sets (about 5–6% APY from 1 Jul 2026) [Tier A, DIA blog]. The largest holder is EOA [0x1b2f…6ed0](https://etherscan.io/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0) with **17.8%**. It received 35.55M on 20 Jul 2026 from EOA [0x7170…bc85](https://etherscan.io/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85), which also funds DIA-linked Safes [Unverified ownership]. No DIA-linked wallet sent tokens to an exchange on a pump day.

**🚨 Top warning:** 17.8% of supply sits in one EOA ([0x1b2f…6ed0](https://etherscan.io/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0)) held in Coinbase Prime custody (Arkham label), with the beneficial owner unconfirmed but tied by funding to DIA-linked Safes. No revenue reaches holders; staking yield is emissions. Price is −70.3% in a year and −97.9% from ATH.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 DIA · DIA · 4.7 / 10 · ❌ FAIL

> **One line:** Fixed supply and no pump-timed insider selling, but no measurable fee revenue and a 17.8% single-key holder.

| 📊 Market (CoinGecko, 16 Nov 2026 9:56 AM MST) | 🔗 On-chain (Blockscout / RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.1214 · 7d / 30d −9.8% / −23.1% · 1y −70.3% | **Supply** 200,000,000 minted · 31.27M burned · 24,135 holders |
| **Market cap** $14.5M · rank #923 · circ 119.7M · FDV $20.5M | **Largest holder** EOA [0x1b2f…6ed0](https://etherscan.io/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0): 17.76% |
| **24h volume** $0.88M: Binance $0.15M, WEEX, Pionex, WhiteBIT | **Lasernet bridge** [0x1eee…49a7](https://etherscan.io/address/0x1eee9b9f024188e54930d2927d7a28e66e7649a7): 2.54% |
| **Pump days** 31 in 365 (Binance DIA/USDT daily closes) | **Token owner** DIA Data: Deployer EOA [0x5737…e157](https://etherscan.io/address/0x5737bf56559dd32d8880cfa236fe613e2162e157) (no mint, no pause) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Oracle / Lasernet fees | Not tracked | [Tier A] DefiLlama has no DIA fees or revenue entry |
| Staking yield | Emission rate targeting ~5–6% APY from 1 Jul 2026, on 4.4M DIA staked | [Tier A] [DIA blog, 5 Jun 2026](https://www.diadata.org/blog/post/update-on-dia-staking/) |
| Fee share | "fees … are reinvested back into the system, rewarding feeders and, eventually, delegators" (not yet live for delegators) | [Tier A] [DIA staking layer post](https://www.diadata.org/blog/post/dia-oracle-staking-layer/) |
| Token utility | Lasernet gas, staking, governance | [Tier A] [diadata.org/token](https://www.diadata.org/token/) |

**What it means:** no measured revenue reaches holders; yield is emissions. **2 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No oracle or Lasernet fee is measured and staking yield is an emission rate, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- DIA (Decentralised Information Asset) has run oracles since 2020. Lasernet mainnet staking launched in late June 2025, and more than 11 independent feeders were live by June 2026 ([DIA blog](https://www.diadata.org/blog/post/update-on-dia-staking/), Tier A).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | % supply | Note |
|---|---:|---|
| [0x1b2f…6ed0](https://etherscan.io/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0) | 17.76% | EOA. Received 35.55M from [0x7170…bc85](https://etherscan.io/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85) on 20 Jul 2026 ([0x9fd070ec…](https://etherscan.io/tx/0x9fd070ece3e573664307cdeec18e5db79a58cf092c8283f239150b6f627bedc0)); only small monthly outflows since |
| [0x7170…bc85](https://etherscan.io/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85) | ~0% now | EOA. Received 63.31M via [0x05c5…fa54](https://etherscan.io/address/0x05c5fe0f2ca2a46747ef7004aab502e7a031fa54) from [0x519e…abb2](https://etherscan.io/address/0x519e6e5ea9bb4a0c779f3d9b06d86a2e561aabb2) on 9 Jul 2024 ([0x52a8f1f6…](https://etherscan.io/tx/0x52a8f1f6001bc9e999bf5b359185667224a9dd125872b59d66cb51445cf9003d)); also funded 2-of-3 Safe [0x68c0…179e](https://etherscan.io/address/0x68c0a3d0ddce1df6ebd7f41ee0ea85882393179e) with 9.15M ([0xddfbd8ec…](https://etherscan.io/tx/0xddfbd8ec0eb66cc398aa957fd784e266e860dd5ef046e7713a8c951ff05eb492)) |
| Dead address | 15.63% | burned |
| Binance cold wallets | 12.75% | exchange [Tier A label] |
| EOAs [0x3970…ace2](https://etherscan.io/address/0x39703ae8cafc87540268bd9aab7fca2c5ae4ace2), [0x21a2…616c](https://etherscan.io/address/0x21a2233208f6c767567a9cf031c97b47e28e616c), [0x785a…12c1](https://etherscan.io/address/0x785aa9e026bb45a8f2e2a6eeeefff77f4ddf12c1), [0x7d40…f932](https://etherscan.io/address/0x7d409e57515a745d297411e5aea0f31938c7f932) | 12.69% | funded by withdrawals from omnibus contract [0xa9d1…3e43](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) (Oct–Dec 2025); only [0x785a…12c1](https://etherscan.io/address/0x785aa9e026bb45a8f2e2a6eeeefff77f4ddf12c1) moved any (176K) |
| 2-of-3 Safes [0xfaca…8c2f](https://etherscan.io/address/0xfaca2b5ea36de3c693924531cf8812b9778d8c2f), [0xd949…7932](https://etherscan.io/address/0xd949969936b0fd66321da06ac3edb2a36bad7932) | 2.30% | each got 3.05M from Safe [0x68c0…179e](https://etherscan.io/address/0x68c0a3d0ddce1df6ebd7f41ee0ea85882393179e) on 6 Feb 2026; [0xd949…7932](https://etherscan.io/address/0xd949969936b0fd66321da06ac3edb2a36bad7932) was funded in 2020 by 2-of-3 Safe [0x72ac…950e](https://etherscan.io/address/0x72ac1760daf52986421b1552bdca04707e78950e), which burned 4.575M the same day ([0x14296e84…](https://etherscan.io/tx/0x14296e844fdf88bf0f2a9fab1837d4f8aee69bfcaedd4007465bf6fbbe97dbc2)) |

- **Arkham (16 Nov 2026)** labels [0x1b2f…6ed0](https://intel.arkm.com/explorer/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0), its funder [0x7170…bc85](https://intel.arkm.com/explorer/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85) and the earlier hops [0x05c5…fa54](https://intel.arkm.com/explorer/address/0x05c5fe0f2ca2a46747ef7004aab502e7a031fa54) and [0x519e…abb2](https://intel.arkm.com/explorer/address/0x519e6e5ea9bb4a0c779f3d9b06d86a2e561aabb2) all **Coinbase Prime Custody**. The 63.3M move in 2024 and the 35.55M move in Jul 2026 are internal to Prime custody, not sales. Because 0x7170 also funded DIA's Safe 0x68c0, the 17.8% is most likely held for DIA or a DIA-linked client in Coinbase Prime custody [Unverified]; it is a custodial account, not a single self-held key. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

*Binance DIA/USDT daily closes (UTC): 31 pump days in the last 365 (Gate gives the same 31).*

| Wallet | Pump-day transfers | What it is |
|---|---|---|
| [0x1b2f…6ed0](https://etherscan.io/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0), [0x7170…bc85](https://etherscan.io/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85), Safes [0x68c0…179e](https://etherscan.io/address/0x68c0a3d0ddce1df6ebd7f41ee0ea85882393179e), [0xfaca…8c2f](https://etherscan.io/address/0xfaca2b5ea36de3c693924531cf8812b9778d8c2f), [0xd949…7932](https://etherscan.io/address/0xd949969936b0fd66321da06ac3edb2a36bad7932) | none | DIA-linked reserve cluster [Unverified] |
| [0x78c4…5a4d](https://etherscan.io/address/0x78c4400ab087ff939c6312ded96608ac0e855a4d) → [0x55a8…38a4](https://etherscan.io/address/0x55a82e12251d82f76bd31164b81f5a0d82cf38a4) → [0x0ba3…d6ba](https://etherscan.io/address/0x0ba3171032059e9e2348b1316c36760bb87cd6ba) | 1,308,354 DIA on 3 Nov 2026 ([0x4ec1f162…](https://etherscan.io/tx/0x4ec1f1626373ac543eec6a3e6eb1f56799bf296bd44b36ff74e9fc68491e1107), [0x8667c9c8…](https://etherscan.io/tx/0x8667c9c8b0ce873e496841cf03c56460cf38295750a87881129118bc67f02ea4)); funded by Safe [0x68c0…179e](https://etherscan.io/address/0x68c0a3d0ddce1df6ebd7f41ee0ea85882393179e) 4 days earlier ([0x5420b3a8…](https://etherscan.io/tx/0x5420b3a80741bd5452528c2581116ee30e885552cd1ce07dbf88fc63d27316e8)) | wallet-to-wallet; [0x0ba3…d6ba](https://etherscan.io/address/0x0ba3171032059e9e2348b1316c36760bb87cd6ba) still holds it; no exchange arrival |
| [0x15da…b0d7](https://etherscan.io/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) → Revolut 3 [0x9b0c…8d46](https://etherscan.io/address/0x9b0c45d46d386cedd98873168c36efd0dcba8d46) | 11 transfers, 30K–61K each, on Sep and Oct pump days (e.g. [0x1232becf…](https://etherscan.io/tx/0x1232becfa5035827baa3b90c03ef8c02ea04d3f96ed1f07c4db710bc14193285)) | Arkham labels [0x15da…b0d7](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) **Revolut: Cold Wallet**, so these are exchange-internal moves |
| [0xed17…51f1](https://etherscan.io/address/0xed17a03296bb6d68a2bdf1f909659ac79a9751f1) → [0xa9d1…3e43](https://etherscan.io/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) | 735,924 on 27 Jul ([0xb3557486…](https://etherscan.io/tx/0xb3557486885da28ca31431382fa9e9949288f2af0d448e19e16d805240092060)) | trading wallet sending to [Coinbase: Hot Wallet](https://intel.arkm.com/explorer/address/0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43) (Arkham) |

- **Arkham (16 Nov 2026):** the 1.308M hop ends at [0x0ba3…d6ba](https://intel.arkm.com/explorer/address/0x0ba3171032059e9e2348b1316c36760bb87cd6ba), an unlabelled wallet with a generic "DIA Whale" tag that still holds 1.374M DIA; the intermediate wallets [0x78c4…5a4d](https://intel.arkm.com/explorer/address/0x78c4400ab087ff939c6312ded96608ac0e855a4d) and [0x55a8…38a4](https://intel.arkm.com/explorer/address/0x55a82e12251d82f76bd31164b81f5a0d82cf38a4) are unlabelled. No exchange arrival. The DIA Safes [0x443b…a44](https://intel.arkm.com/explorer/address/0x443b44a55822cc1b8a1f2af99a09ca19cf71ca44) (signer: DIA Deployer) and [0x72ac…950e](https://intel.arkm.com/explorer/address/0x72ac1760daf52986421b1552bdca04707e78950e) show the 19.84M and 4.575M dead-address burns. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

**What it means:** pump-day flows into exchanges come from unrelated holders or exchange-internal wallets. **7**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Binance DIAUSDT UTC daily closes (Gate agrees).

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- Fixed 200M; verified `DIAToken` (solc 0.5.11) has no `mint` and no `pause`. 31.27M burned: 19.84M unsold bonding-curve tokens on 18 Aug 2020 ([0x8efc5ce8…](https://etherscan.io/tx/0x8efc5ce8b2e80da32f34289006c614d6929ce99b91510481933c72ea03f05368)), plus later burns from Safes. 2.47M bridged to BNB Chain [Tier A, RPC]. **7**.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.88M of 24h volume on a $14.5M cap. Binance is the top venue at only $0.15M.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Lasernet (OP-stack L2) and Lumina oracles are live. The staking reward rate was reset on 1 Jul 2026 ([DIA blog](https://www.diadata.org/blog/post/update-on-dia-staking/)).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- Only 4.4M DIA (2.2% of supply) is staked. DIA claims 60+ chains and 200+ dApps [Tier A, self-reported]. Oracle TVS was not cross-checked [Unverified].

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Token owner [0x5737…e157](https://etherscan.io/address/0x5737bf56559dd32d8880cfa236fe613e2162e157) (Etherscan: DIA Data: Deployer) can only call `addAuditHash` and transfer ownership. The staking contract was audited by MixBytes ([diadata.org/token](https://www.diadata.org/token/), Tier A). **6**.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found. DIA staking is closed to US, UK and Canada residents (Tier A, token page).

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Ongoing | Lasernet feeder delegation and slashing (planned, no date) |
| 15th of each month | Small recurring outflows from the large-holder wallets |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None found |
| Live mint path | 🟢 None (fixed supply) |
| Single-key controls | 🟡 17.8% in a Coinbase Prime Custody wallet linked by funding to DIA Safes (owner [Unverified]) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x1b2f…6ed0](https://intel.arkm.com/explorer/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0), [0x7170…bc85](https://intel.arkm.com/explorer/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85), [0x05c5…fa54](https://intel.arkm.com/explorer/address/0x05c5fe0f2ca2a46747ef7004aab502e7a031fa54), [0x519e…abb2](https://intel.arkm.com/explorer/address/0x519e6e5ea9bb4a0c779f3d9b06d86a2e561aabb2) | Coinbase Prime Custody | Arkham + gas-supplier funding | medium | no | Holdings: custody; moves are not sales |
| [0x5737…e157](https://intel.arkm.com/explorer/address/0x5737bf56559dd32d8880cfa236fe613e2162e157) | DIA: Deployer (token owner) | Arkham + RPC owner() | high | yes | None |
| [0x0ba3…d6ba](https://intel.arkm.com/explorer/address/0x0ba3171032059e9e2348b1316c36760bb87cd6ba) | Unlabelled (DIA Whale tag) | Arkham | low | no | None |
| [0x15da…b0d7](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) | Revolut: Cold Wallet | Arkham | medium | no | Removes a candidate |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the Prime custody chain, the deployer, the DIA Safes and the 1.308M hop; dates from Etherscan
- [Tier A] Etherscan v2 token transfers; Blockscout holders, verified source and address metadata; Ethereum and BNB Chain RPC (`owner`, `totalSupply`, `balanceOf(dead)`, Safe `getThreshold`/`getOwners`)
- [Tier A] Etherscan labels (DIA Data: Deployer; Binance cold wallets; Revolut 3; Crypto.com)
- [Tier A] [diadata.org/token](https://www.diadata.org/token/) · [Staking update, Jun 2026](https://www.diadata.org/blog/post/update-on-dia-staking/) · [Staking layer post](https://www.diadata.org/blog/post/dia-oracle-staking-layer/) · DefiLlama protocol and fees lists (no DIA entry)
- [Tier A] CoinGecko `dia-data` (16 Nov 2026 9:56 AM MST); Binance DIAUSDT daily klines (cross-checked with Gate DIA_USDT: 31 pump days on both)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 35.55M to the largest-holder EOA | [0x9fd070ec…](https://etherscan.io/tx/0x9fd070ece3e573664307cdeec18e5db79a58cf092c8283f239150b6f627bedc0) | A | 16 Nov 2026 |
| Unsold bonding-curve tokens burned | [0x8efc5ce8…](https://etherscan.io/tx/0x8efc5ce8b2e80da32f34289006c614d6929ce99b91510481933c72ea03f05368) | A | 16 Nov 2026 |
| Pump-day cluster transfer with no exchange arrival | [0x4ec1f162…](https://etherscan.io/tx/0x4ec1f1626373ac543eec6a3e6eb1f56799bf296bd44b36ff74e9fc68491e1107) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Beneficial owner of the Prime custody wallet `0x1b2f…6ed0`** | Arkham (16 Nov 2026): Coinbase Prime Custody; ask DIA whether it is its reserve | Free |
| 2 | **Who controls the 17.8% EOA** | Arkham entity for [0x1b2f…6ed0](https://etherscan.io/address/0x1b2fdbdb1b56a3e09649301a7ac5a9d770aa6ed0) and [0x7170…bc85](https://etherscan.io/address/0x7170a0b768d5b2dd69188e2c7976102ac69cbc85); DIA treasury disclosure | Free |
| 3 | **Lasernet fee income** | Lasernet explorer gas totals in DIA | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
