---
ticker: EDEN
name: OpenEden
chain: ethereum
contract: "0x24a3d725c37a8d1a66eb87f0e5d07fe67c120035"
overall_score: 4.1
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 3
  product_development: 6
  adoption_customers: 6
  security_audits: 5
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes: uncapped mint(); MINTER_ROLE held by the CCIP pool 0xc8adf2f51a35b0a9d8f74675b64c954ca2dcbc14, and a 3-of-5 Safe 0xf9900ce9f2072f906f30baf7f280930483ec5949 can grant it to anyone"
  pause_power: "ban + seize: the same Safe can ban any address (BANLIST_ROLE) and burn its balance (burnBanned)"
  team_wallet_to_exchange_during_pump: "yes [Unverified insider]: 3.30M EDEN from a MerkleVester allocation reached Binance deposit 0x71b83613743e42c800fc7b7648c53f16847c7cdd on pump day 19 May 2026"
  one_hop_sale_status: not_proven
  treasury_in_single_key_wallets: "none found; vesting and admin wallets are Safes"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "TBILL and USDO earn fees, but buybacks are discretionary and bought EDEN stays in treasury; xEDEN yield is emissions, so revenue does not reach holders."
pump_day_price_source: "Binance EDENUSDT UTC daily closes (Gate cross-check)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xc6056053f6e3bf71855d61d6a54bbcf6deed9087"
    label: "Generic Gnosis Safes"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x18ac6ceacffce66d998693626500066517ed6527"
    label: "Generic Gnosis Safes"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xd88b8221f789ab448bcaa8f76e616339a0a9424a"
    label: "Anchorage Digital; Anchorage Digital Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x9ceb1acb844c759bd47d7026e9a9f168260f0328"
    label: "Anchorage Digital; Anchorage Digital Custody"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xb5e4d21240e9356cafc3a1261d10383f62dfc24e"
    label: "a16z"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x80d96ab88aeedc75530e8ec952db284171497985"
    label: "MerkleVester (verified)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
  - address: "0x9adcbe30375753773a2940dc2b34ba5fda7b82a5"
    label: "MerkleVester (verified)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
  - address: "0x6fe70858fda5b642ca2e48903e5402501bb7bb78"
    label: "MerkleVester (verified)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
  - address: "0xc8adf2f51a35b0a9d8f74675b64c954ca2dcbc14"
    label: "EDENBurnMintTokenPool (verified)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Etherscan"
price_usd: 0.04466
price_source: "CoinGecko, 16 Nov 2026 9:56 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EDEN · Overall grade **4.1 / 10 · ❌ FAIL**

**Summary:** OpenEden issues the TBILL tokenized T-bill vault and the USDO yield stablecoin. Those products earn real fees (DefiLlama: **$647K of revenue in the past year**, TBILL $276K and USDO $371K) [Tier A]. None of it reaches EDEN holders automatically. xEDEN staking pays EDEN emissions, and buybacks are discretionary: the docs say bought tokens stay in treasury and are not distributed or burned [Tier A]. Supply is 1B (921.8M on Ethereum and 78.2M on BNB Chain, reconciled by RPC). The token is an upgradeable proxy with an **uncapped `mint`**. A 3-of-5 Safe [0xf990…5949](https://etherscan.io/address/0xf9900ce9f2072f906f30baf7f280930483ec5949) holds admin, upgrade and ban roles. About **57% of supply** sits in MerkleVester contracts topped up and drained by a 3-of-4 Safe [0x2d7e…dc04](https://etherscan.io/address/0x2d7e4bfee1483766c2720c44c98b2662f7d7dc04). One vesting allocation was routed through four hops into **Binance on pump day 19 May 2026 (3.30M EDEN)**.

**🚨 Top warning:** Mint is uncapped and role-gated: the 3-of-5 admin Safe can grant MINTER_ROLE, upgrade the contract, and ban and burn any holder's balance. A MerkleVester allocation went to Binance on a pump day ([0x57eda1ae…](https://etherscan.io/tx/0x57eda1ae5f417e8d800a125e7bde20b18ace86123d012e26121c917b95df7861)). Revenue does not reach holders. Price is −51.8% in a year and −96.6% from ATH.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EDEN · OpenEden · 4.1 / 10 · ❌ FAIL

> **One line:** Real RWA fees, but none reach EDEN holders. Mint is uncapped and admin-controlled, and one vesting allocation was sold into a pump.

| 📊 Market (CoinGecko, 16 Nov 2026 9:56 AM MST) | 🔗 On-chain (Blockscout / RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.0447 · 7d / 30d −5.3% / −20.1% · 1y −51.8% | **Supply** 1,000,000,000 (921.8M Ethereum + 78.2M BNB Chain) · 6,314 Ethereum holders |
| **Market cap** $17.9M · rank #816 · circ 401.4M · FDV $44.7M | **MerkleVesters** [0x9adc…82a5](https://etherscan.io/address/0x9adcbe30375753773a2940dc2b34ba5fda7b82a5) 24.1%, [0x6fe7…bb78](https://etherscan.io/address/0x6fe70858fda5b642ca2e48903e5402501bb7bb78) 21.0%, [0x80d9…7985](https://etherscan.io/address/0x80d96ab88aeedc75530e8ec952db284171497985) 11.6% |
| **24h volume** $0.92M: Bithumb $0.22M, Binance $0.19M (USDT), Biconomy, Toobit | **Admin** 3-of-5 Safe [0xf990…5949](https://etherscan.io/address/0xf9900ce9f2072f906f30baf7f280930483ec5949) (admin, upgrade, ban roles) |
| **Pump days** 48 in 365 (Binance EDEN/USDT daily closes) | **Minter/burner** CCIP pool [0xc8ad…bc14](https://etherscan.io/address/0xc8adf2f51a35b0a9d8f74675b64c954ca2dcbc14) (owner: 3-of-4 Safe) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| TBILL revenue, 1y | $275,570 | [Tier A] DefiLlama `openeden-tbill` |
| USDO revenue, 1y | $371,041 (fees $1.90M) | [Tier A] DefiLlama `openeden-usdo` |
| Paid to EDEN holders | $0 automatic. xEDEN yield is EDEN emissions; buybacks are discretionary and bought EDEN "is not redistributed or injected into the xEDEN staking contract" | [Tier A] [docs: Usecases](https://docs.openeden.com/openeden-foundation/eden/usecases), [EDEN Staking](https://docs.openeden.com/openeden-foundation/eden/eden-staking) |
| First governance buyback | 30,000 USDC proposal | [Tier A] [openeden.com governance launch](https://openeden.com/news/openeden-governance-launch/) |

**What it means:** the company earns revenue, but the token does not receive it. **2 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** TBILL and USDO earn fees, but buybacks are discretionary and bought EDEN stays in treasury; xEDEN yield is emissions, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- OpenEden has run TBILL since 2023 and USDO since 2025 ([openeden.com](https://openeden.com/), Tier A). The OpenEden Foundation issues EDEN and runs governance through Tally ([docs](https://docs.openeden.com/openeden-foundation/eden/overview), Tier A).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | % supply | Note |
|---|---:|---|
| [0x9adc…82a5](https://etherscan.io/address/0x9adcbe30375753773a2940dc2b34ba5fda7b82a5) MerkleVester | 24.07% | funded by Safe [0xf64b…63cc](https://etherscan.io/address/0xf64b05ede203faf6e04a88eb510d046d767263cc) (240.7M) |
| [0x6fe7…bb78](https://etherscan.io/address/0x6fe70858fda5b642ca2e48903e5402501bb7bb78) MerkleVester | 21.00% | funded 7 Oct 2026 by Safe [0x2d7e…dc04](https://etherscan.io/address/0x2d7e4bfee1483766c2720c44c98b2662f7d7dc04) ([0xb32c1690…](https://etherscan.io/tx/0xb32c1690fa8ea2444495f40d034a0d2a0e8af7cfdd50e705a06e9e0d3bcc18b4)) |
| [0x80d9…7985](https://etherscan.io/address/0x80d96ab88aeedc75530e8ec952db284171497985) MerkleVester | 11.64% | 3-of-4 Safe [0x2d7e…dc04](https://etherscan.io/address/0x2d7e4bfee1483766c2720c44c98b2662f7d7dc04) pulled 63.4M back out on 14 Oct 2026 ([0x894487ac…](https://etherscan.io/tx/0x894487ac39589d57594fdb3e18c5d07cda832360a9a580c257865875002514e9)) and put 119.5M in on 22 Oct ([0x331d338c…](https://etherscan.io/tx/0x331d338c2dd351972a46b1fd8fa589c4b31451a9ef49586eed721f2ec7b49b6b)) |
| [0x7e6c…af23](https://etherscan.io/address/0x7e6c274e9f57b0f052647c37084d372ed665af23) xEDEN staking | 4.85% | staking pool |
| Binance cold wallets | 9.14% | exchange [Tier A label] |
| Safes [0x107a…6ebb](https://etherscan.io/address/0x107a0cdba237d6d8ea317f4f72e795bf912c6ebb), [0xac76…a3bd](https://etherscan.io/address/0xac76d02b1d1ea4d37a7576504b800e113ff9a3bd), [0xf990…5949](https://etherscan.io/address/0xf9900ce9f2072f906f30baf7f280930483ec5949) | 6.37% | project-linked Safes [Unverified role] |

- Vesting contracts can be drained back to the funding Safe, so vesting schedules are not locked on-chain [Tier A, transfers above].

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Binance EDEN/USDT daily closes (UTC): 48 pump days in the last 365 (Gate gives 48, with 4 dates different).*

| Wallet | Pump-day transfers | What it is |
|---|---|---|
| [0x80d9…7985](https://etherscan.io/address/0x80d96ab88aeedc75530e8ec952db284171497985) → Safe [0xc605…9087](https://etherscan.io/address/0xc6056053f6e3bf71855d61d6a54bbcf6deed9087) → EOA [0xd88b…424a](https://etherscan.io/address/0xd88b8221f789ab448bcaa8f76e616339a0a9424a) → [0x9ceb…0328](https://etherscan.io/address/0x9ceb1acb844c759bd47d7026e9a9f168260f0328) → [0xb5e4…c24e](https://etherscan.io/address/0xb5e4d21240e9356cafc3a1261d10383f62dfc24e) → Binance deposit [0x71b8…7cdd](https://etherscan.io/address/0x71b83613743e42c800fc7b7648c53f16847c7cdd) | vested claims (595K a month) plus airdrop and xEDEN redemptions via [0x18ac…6527](https://etherscan.io/address/0x18ac6ceacffce66d998693626500066517ed6527), consolidated into 3,297,579 EDEN and sent to Binance on **19 May 2026** ([0x30c11611…](https://etherscan.io/tx/0x30c116111d73207af1ccac307f10d5d717bbec9f548303632777fa432fcdd83a), [0xa1570e09…](https://etherscan.io/tx/0xa1570e098b4ec33bcb1492a9fdea76ea465d831422fbf5543a090307ddb88cbb), [0x57eda1ae…](https://etherscan.io/tx/0x57eda1ae5f417e8d800a125e7bde20b18ace86123d012e26121c917b95df7861)), then swept to Binance 14 ([0x341dc9cb…](https://etherscan.io/tx/0x341dc9cbaa18138bf332ad214791b366ba31bf3b2b3c0d20ad3d4b9b06b4abca)) | a vesting-allocation holder (investor, advisor or team) [Unverified identity] |
| Safe [0x05f1…703c](https://etherscan.io/address/0x05f1d0b2b5adfd2a9fa9c6234dcb8e2e4a4f703c) | claims 1.25M a month from [0x80d9…7985](https://etherscan.io/address/0x80d96ab88aeedc75530e8ec952db284171497985) and bridges it to BNB Chain via the CCIP pool, incl. 1.25M on 20 May ([0x8b3d8394…](https://etherscan.io/tx/0x8b3d83946e21cc32d4239a8e46cddd977b5d8c4ab72e1c9c9c21d36051963bb2)) and 15 Jun ([0x881078e9…](https://etherscan.io/tx/0x881078e9dded34d8bddaeaf4b28d85a1533c6ef2cb03a5bb329a4b6b510542e5)) | allocation holder; BNB Chain destination not traced |
| Admin Safe [0xf990…5949](https://etherscan.io/address/0xf9900ce9f2072f906f30baf7f280930483ec5949) → Safe [0xedb9…5693](https://etherscan.io/address/0xedb98a8466cfc4c9c662c6b0136751d61b965693) → Angle Merkl distributor [0x3ef3…d9ae](https://etherscan.io/address/0x3ef3d8ba38ebe18db133cec108f4d14ce00dd9ae) | 500K on 27 Aug ([0x9d9d4425…](https://etherscan.io/tx/0x9d9d442532dba0b47e78488a35ed9ddefba8513b2cf7c9ef2a34015ae6a07e01)) | incentive campaign, not a sale |
| Funding Safe [0xf64b…63cc](https://etherscan.io/address/0xf64b05ede203faf6e04a88eb510d046d767263cc) | 1M to Safe [0x9d70…bb8b](https://etherscan.io/address/0x9d7000e738c7dd34015c58c080d2fa79b512bb8b) on 22 May ([0xc95c0199…](https://etherscan.io/tx/0xc95c019965ca3bc2455cf4475a6889eb11919fe183bee20430cde7a5bd725f58)) | internal Safe-to-Safe |

- No transfer from the admin, vesting-funding or treasury Safes went directly to an exchange.

- **Arkham (16 Nov 2026):** the Safes [0xc605…9087](https://intel.arkm.com/explorer/address/0xc6056053f6e3bf71855d61d6a54bbcf6deed9087) and [0x18ac…6527](https://intel.arkm.com/explorer/address/0x18ac6ceacffce66d998693626500066517ed6527) carry only generic Safe labels (no team, investor or advisor tag). [0xc605…9087](https://intel.arkm.com/explorer/address/0xc6056053f6e3bf71855d61d6a54bbcf6deed9087) receives about 595K EDEN a month from the MerkleVester [0x80d9…7985](https://intel.arkm.com/explorer/address/0x80d96ab88aeedc75530e8ec952db284171497985) and forwards the same amount to [0xd88b…424a](https://intel.arkm.com/explorer/address/0xd88b8221f789ab448bcaa8f76e616339a0a9424a), which Arkham labels **Anchorage Digital**; the next hop [0x9ceb…0328](https://intel.arkm.com/explorer/address/0x9ceb1acb844c759bd47d7026e9a9f168260f0328) is **Anchorage Digital Custody**. That pattern fits a vesting beneficiary holding through a custodian. The wallet that made the 19 May Binance deposit, [0xb5e4…c24e](https://intel.arkm.com/explorer/address/0xb5e4d21240e9356cafc3a1261d10383f62dfc24e), carries an **a16z** label (single source, medium confidence), which points to an investor, not the team [Unverified]. The Binance deposit [0x71b8…7cdd](https://intel.arkm.com/explorer/address/0x71b83613743e42c800fc7b7648c53f16847c7cdd) is labelled. Arkham also lists the monthly 1.25M from [0x05f1…703c](https://intel.arkm.com/explorer/address/0x05f1d0b2b5adfd2a9fa9c6234dcb8e2e4a4f703c) next to a Binance deposit counterparty; on Etherscan every Ethereum outflow from that Safe goes to the CCIP pool (e.g. [tx](https://etherscan.io/tx/0x8b3d83946e21cc32d4239a8e46cddd977b5d8c4ab72e1c9c9c21d36051963bb2)), so the Binance leg would be on BNB Chain [Unverified]. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

**What it means:** one vesting allocation (0.33% of supply) reached Binance on a pump day through custody wallets. Its owner is not labelled as the team, and the labels point to an investor. **4 (not proven).**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Binance EDENUSDT UTC daily closes (Gate cross-check).

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- Fixed issuance of 1B so far, but `mint(address,uint256)` has **no cap** (verified source `Eden.sol`). MINTER_ROLE and BURNER_ROLE sit with the CCIP BurnMint pool [0xc8ad…bc14](https://etherscan.io/address/0xc8adf2f51a35b0a9d8f74675b64c954ca2dcbc14) (EDEN BurnMintTokenPool 1.5.1). The pool's `burn(from, amount)` needs no allowance. DEFAULT_ADMIN_ROLE (3-of-5 Safe [0xf990…5949](https://etherscan.io/address/0xf9900ce9f2072f906f30baf7f280930483ec5949)) can grant MINTER_ROLE to any address [Tier A, RPC `hasRole`].
- Circulating 401M of 1B; the rest is mainly in MerkleVesters. **4**.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.92M of 24h volume on a $17.9M cap. Bithumb (KRW) leads, ahead of Binance.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- TBILL and USDO are live on several chains; governance launched on Tally with a first buyback proposal.

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- DefiLlama fees: USDO $1.90M and TBILL $447K in the past year; fees have fallen sharply in the last 30 days (USDO $45.6K, TBILL $72.5K).

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- UUPS upgradeable (implementation `EdenV2` [0x39b7…39d3](https://etherscan.io/address/0x39b77c1c6f1a6d786c54135612e65831500e39d3), read from the EIP-1967 slot). UPGRADE_ROLE belongs to the 3-of-5 Safe. The deployer EOA [0xb09f…19bc](https://etherscan.io/address/0xb09f37281ca7eaeeade2fa344690db2760ed19bc) renounced admin, upgrade and upgrade-admin roles on 1 Oct 2025 [Tier A, RoleRevoked events].
- Ban list: BANLIST_ROLE can freeze any address and DEFAULT_ADMIN can `burnBanned` its balance. **5**.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement action found. Licensing of TBILL and USDO was not re-sourced this run [Unverified].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly | MerkleVester claims (e.g. 1.25M and 595K tranches on Ethereum) |
| Ongoing | Discretionary EDEN buybacks via governance |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: vesting allocation → Anchorage custody → Binance on 19 May 2026 (owner unlabelled; a16z-labelled last hop) |
| Live mint path | 🔴 Uncapped mint; admin Safe can grant MINTER_ROLE |
| Single-key controls | 🟢 None; admin and vesting control via Safes (3-of-5, 3-of-4) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xc605…9087](https://intel.arkm.com/explorer/address/0xc6056053f6e3bf71855d61d6a54bbcf6deed9087), [0x18ac…6527](https://intel.arkm.com/explorer/address/0x18ac6ceacffce66d998693626500066517ed6527) | Generic Gnosis Safes | Arkham | low | no | Selling stays 4 (cannot carry a sale) |
| [0xd88b…424a](https://intel.arkm.com/explorer/address/0xd88b8221f789ab448bcaa8f76e616339a0a9424a), [0x9ceb…0328](https://intel.arkm.com/explorer/address/0x9ceb1acb844c759bd47d7026e9a9f168260f0328) | Anchorage Digital; Anchorage Digital Custody | Arkham | medium | no | Custody, not team |
| [0xb5e4…c24e](https://intel.arkm.com/explorer/address/0xb5e4d21240e9356cafc3a1261d10383f62dfc24e) | a16z | Arkham | medium | no | Points to an investor, not team |
| [0x80d9…7985](https://intel.arkm.com/explorer/address/0x80d96ab88aeedc75530e8ec952db284171497985), [0x9adc…82a5](https://intel.arkm.com/explorer/address/0x9adcbe30375753773a2940dc2b34ba5fda7b82a5), [0x6fe7…bb78](https://intel.arkm.com/explorer/address/0x6fe70858fda5b642ca2e48903e5402501bb7bb78) | MerkleVester (verified) | Arkham + Etherscan | high | yes | Holdings |
| [0xc8ad…bc14](https://intel.arkm.com/explorer/address/0xc8adf2f51a35b0a9d8f74675b64c954ca2dcbc14) | EDENBurnMintTokenPool (verified) | Arkham + Etherscan | high | yes | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the vesting Safes, Anchorage wallets, the a16z-labelled wallet, the vesters and the CCIP pool; dates from Etherscan
- [Tier A] Etherscan v2 token transfers and logs (RoleGranted, RoleRevoked); Blockscout holders, verified source and address metadata; Ethereum and BNB Chain RPC (`hasRole`, `totalSupply`, `getThreshold`, `getOwners`, EIP-1967 slot, pool `owner()`, `typeAndVersion()`)
- [Tier A] Etherscan labels (Binance Deposit; Binance cold wallets; Angle Protocol: Distributor)
- [Tier A] DefiLlama fees and revenue for `openeden-tbill` and `openeden-usdo`
- [Tier A] [OpenEden docs: EDEN overview](https://docs.openeden.com/openeden-foundation/eden/overview) · [Usecases](https://docs.openeden.com/openeden-foundation/eden/usecases) · [Staking](https://docs.openeden.com/openeden-foundation/eden/eden-staking) · [Governance launch](https://openeden.com/news/openeden-governance-launch/)
- [Tier A] CoinGecko `openeden` (16 Nov 2026 9:56 AM MST); Binance EDENUSDT daily klines (cross-checked with Gate EDEN_USDT)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Vesting allocation into a Binance deposit on a pump day | [0x57eda1ae…](https://etherscan.io/tx/0x57eda1ae5f417e8d800a125e7bde20b18ace86123d012e26121c917b95df7861) | A | 16 Nov 2026 |
| Safe pulls tokens back out of a MerkleVester | [0x894487ac…](https://etherscan.io/tx/0x894487ac39589d57594fdb3e18c5d07cda832360a9a580c257865875002514e9) | A | 16 Nov 2026 |
| Deployer renounces admin role | [0xb09f…19bc](https://etherscan.io/address/0xb09f37281ca7eaeeade2fa344690db2760ed19bc) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who is the vesting beneficiary behind `0xc605…9087`** | Arkham (16 Nov 2026): generic Safe, Anchorage custody downstream; ask OpenEden for the allocation list | Free |
| 2 | **Who owns the 19 May seller cluster** | Arkham entity for [0xd88b…424a](https://etherscan.io/address/0xd88b8221f789ab448bcaa8f76e616339a0a9424a) / [0xc605…9087](https://etherscan.io/address/0xc6056053f6e3bf71855d61d6a54bbcf6deed9087) | Free |
| 3 | **Did the 30K USDC buyback execute?** | Tally proposal result and reserve-contract transfers | Free |
| 4 | **BNB Chain destination of bridged vesting claims** | BNB Chain transfers of EDEN after CCIP releases to [0x05f1…703c](https://etherscan.io/address/0x05f1d0b2b5adfd2a9fa9c6234dcb8e2e4a4f703c)'s counterparty | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
