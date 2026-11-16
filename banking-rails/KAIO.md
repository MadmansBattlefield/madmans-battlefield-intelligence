---
ticker: KAIO
name: KAIO (formerly Libre Capital)
chain: ethereum
contract: "0x00bac91fd8f5b4a0dc03c8021139b76f6549ee7e (ERC-20 KaioToken on Ethereum)"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 3
  tokenomics_supply: 2
  liquidity_market: 3
  product_development: 6
  adoption_customers: 5
  security_audits: 6
  regulatory: 6
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: none found
  treasury_to_exchange_during_pump: "yes, via the project's TGE liquidity wallet: 0xf9fe… funded fresh wallet 0x7875… with 13M KAIO on 1 Oct 2026, which sent 10M to Gate, Coinbase and Bitget deposits on the 1, 2 and 8 Oct 2026 pump days (+43%, +51%, +28%)"
  treasury_funded_wallet_to_exchange_during_pump: "yes (same flow)"
  unenforced_lockups: "yes: 9.32B of 10B KAIO (93%) sits in five plain EOAs (no vesting contract) that match the published investor, community, foundation, team and pre-sale buckets"
  mint_path_live: "no (fixed 10B minted once to the deployer, 16 Apr 2026)"
price_usd: 0.02039
price_source: "CoinGecko, 16 Nov 2026 6:51 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### KAIO · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** KAIO (the renamed Libre Capital) tokenizes real institutional funds: BlackRock ICS, Hamilton Lane, Brevan Howard, Laser Digital and Mubadala strategies, audited by Cyfrin. The business looks real. The token does not yet: it launched on 6 May 2026, is down 92% from its launch-day price, trades about $230k a day, has only 6.8% of supply circulating (FDV $204M against a $13.9M market cap) and earns its holders nothing. The chain shows the published allocation exactly, but **every locked bucket sits in a plain wallet, not a vesting contract**, so the lock-ups are promises. The project's own liquidity wallet fed a fresh wallet that sold into the October spike. Both gates fail.

**🚨 Top warning (red line):** KAIO's TGE liquidity wallet [`0xf9fe…12cc`](https://etherscan.io/address/0xf9fe4f7279207b6795f8c94b96de86f127fe12cc) (468.75M from the deployer = exactly the 12.5% of the community bucket unlocked "for liquidity", [tx](https://etherscan.io/tx/0xc644428b99b161d69390c30123dd4eab3927d4a72d643da990734bdcadc0a75e)) sent **13,000,000 KAIO to a brand-new wallet [`0x7875…b2e2`](https://etherscan.io/address/0x787563c7f4a1f9fdeb84b828a509314bd6acb2e2) on 1 Oct 2026** ([tx](https://etherscan.io/tx/0xb48978b227246d86600fd025452dc757d437b07e04a8abd44d893f91fc87e565)), in the middle of a +144% / +102% / +79% run. That wallet sent **3M to a Gate deposit the same day (+43% vs 5 days earlier)** ([tx](https://etherscan.io/tx/0x2941ae6c76a81f601c0518c60c05797a7a49932584973665aa2c1fc94e6070ab)) , **3M to a Coinbase deposit on 2 Oct (+51%)** ([tx](https://etherscan.io/tx/0x03bf7e211a05862fe916811fccc45a4634684e0c476d5c9ddd6b363c14c93b1a)) and **4M to a Bitget deposit on 8 Oct (+28%)** ([tx](https://etherscan.io/tx/0x3e54f39001ca111210a25ad8ab6f9f061985b621a5a4206707fdcbe36729be5a)): 10M KAIO, ≈ $230k at those closes. Small in dollars, but it is the project's own wallet putting coins on exchanges into a spike, through an intermediary, with no announcement. **Second warning:** 9.32B of the 10B supply sits in five ordinary wallets, untouched since 1 May 2026 (investors 3.1B [`0xc2ed…`](https://etherscan.io/address/0xc2ed4aa16d749c50fb3be34cdc99b80ef42899e6), community 3.28B [`0x5eaa…`](https://etherscan.io/address/0x5eaa87a6867d29a6288424a238a3d0dba9ec951d), foundation 1.49B [`0x1c5e…`](https://etherscan.io/address/0x1c5e97a7b4fe01bba50827e3dd78bd9f272bee4b), team 1.1B [`0x588f…`](https://etherscan.io/address/0x588f42183046d626470e5019e02a2b3ba97e994b), pre-sale 350M [`0xd31b…`](https://etherscan.io/address/0xd31bc138a2438cfb676f50053b10697d990fa8d7)). Nothing on-chain stops any of them from selling tomorrow. Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 KAIO · KAIO · 3.6 / 10 · ❌ FAIL

> **One line:** A credible fund-tokenization business wrapped in a 6.8%-float token whose locks live only in wallets, not code.

**Identity:** KAIO = KAIO (formerly Libre Capital), kaio.xyz. CoinGecko `kaio`, symbol KAIO, Ethereum contract [`0x00ba…ee7e`](https://etherscan.io/token/0x00bac91fd8f5b4a0dc03c8021139b76f6549ee7e) (verified as `KaioToken`; deployer [`0xfddf…1419`](https://etherscan.io/address/0xfddf70861a4ffd7cb52a1ee992b42020f3cd1419)). Not Kaia (KAIA), which is a separate pipeline row. Matches the pipeline row (KAIO, kaio.xyz).

| 📊 Market (CoinGecko, 16 Nov 2026 6:51 AM MST) | 🔗 On-chain (Etherscan v2 API, 16 Nov 2026) |
|---|---|
| **Price** $0.02039 | **Supply** 10,000,000,000 minted once on 16 Apr 2026 ([tx](https://etherscan.io/tx/0xf61eb43f84aa08b2e82f605ef87a77c23555c4cef9ac6cd232e876a8d43eba6b)) |
| **24h / 7d / 30d** 🔴 −0.8% / −6.6% / −43.1% | **Locked buckets in plain EOAs** 9.53B in six EOAs (incl. the 212.5M foundation TGE unlock, also unmoved) |
| **Market cap** $13.89M · **FDV** $203.9M | **Liquidity wallet** `0xf9fe…` 216.7M left of 468.75M |
| **24h volume** $231k | **Holders' revenue** $0 (DefiLlama) |
| **ATH** $0.2566 (6 May 2026, launch day) · now −92.1% | **Circulating** 681.25M (6.8%) |
| **Pump days, since launch** 29 (CoinGecko closes) | **TVL** $34.7M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees = revenue, 30d / since tracking | $36,410 / $235,069 | [Tier A] [DefiLlama KAIO](https://defillama.com/protocol/kaio) (16 Nov 2026) |
| Revenue to KAIO holders | **$0** | same (`dailyHoldersRevenue` = 0) |
| Token utility | Governance; staking for "priority participation" and fee discounts (proposed) | [Tier B] [IQ.wiki](https://iq.wiki/wiki/kaio) · [KuCoin news](https://www.kucoin.com/news/flash/kaio-reveals-tokenomics-37-5-allocated-for-community-and-liquidity-incentives) |

**What it means:** Fund fees go to the company, not to KAIO holders: ~$440k a year at the current run rate against a $204M FDV. Score **2**, which **trips the Revenue gate**.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Entities | KAIO Foundation (announced Apr 2026 to manage governance, treasury, ecosystem); operating company formerly Libre Capital | [Tier B ×2] [KuCoin/Foresight](https://www.kucoin.com/news/flash/kaio-reveals-tokenomics-37-5-allocated-for-community-and-liquidity-incentives) · [Bitget/Foresight](https://www.bitget.com/news/detail/12560605390886) |
| Backers | $19M raised, incl. an $8M Apr 2026 round with Tether and Systemic Ventures; Laser Digital, Brevan Howard Digital, Further Ventures | [Tier B] [IQ.wiki](https://iq.wiki/wiki/kaio) |
| Published wallets | None. The deployer's six 1 May 2026 transfers match the published table exactly (3.1B / 3.28125B / 1.4875B / 1.1B / 350M / 212.5M, plus 468.75M liquidity) | Not found (official) · [Tier A] chain |
| Docs | Whitepaper "Soon"; token docs missing from docs.kaio.xyz | [Tier A] [kaio.xyz](https://www.kaio.xyz/) · [docs](https://docs.kaio.xyz/) |

**What it means:** Credible backers and partners, but no whitepaper, no published treasury addresses and no vesting contracts six months after TGE. Score **5**.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Bucket (published %) | Wallet | KAIO now | Type |
|---|---|---:|---|
| Early investors (31%) | [`0xc2ed…99e6`](https://etherscan.io/address/0xc2ed4aa16d749c50fb3be34cdc99b80ef42899e6) ([tx](https://etherscan.io/tx/0x11595c5de7701eab3b28405525a568d0263c62fe40b5ff0d40ead4e3a7dbad1d)) | 3,100,000,000 | EOA, never moved |
| Community, locked part (37.5% × 87.5%) | [`0x5eaa…951d`](https://etherscan.io/address/0x5eaa87a6867d29a6288424a238a3d0dba9ec951d) ([tx](https://etherscan.io/tx/0xda249531da9a56964b330c6145b38b6cfe357bade0e36173017bbc981053eca9)) | 3,281,250,000 | EOA, never moved |
| Foundation, locked part (17% × 87.5%) | [`0x1c5e…ee4b`](https://etherscan.io/address/0x1c5e97a7b4fe01bba50827e3dd78bd9f272bee4b) ([tx](https://etherscan.io/tx/0x26e747d6839f497152ed05309e6989422c117c63327e5ce43820dc36aef67551)) | 1,487,500,000 | EOA, never moved |
| Team (11%) | [`0x588f…994b`](https://etherscan.io/address/0x588f42183046d626470e5019e02a2b3ba97e994b) ([tx](https://etherscan.io/tx/0xd19ad79ba89d675bdaaabff911517bf6d8245c3e0c752e37e55a9a5acfa04962)) | 1,100,000,000 | EOA, never moved |
| Pre-TGE sale (3.5%) | [`0xd31b…a8d7`](https://etherscan.io/address/0xd31bc138a2438cfb676f50053b10697d990fa8d7) ([tx](https://etherscan.io/tx/0xd146bddc0181b2867b258a376eac2ced9116bd2061911aa7cbf09245b77d6858)) | 350,000,000 | EOA, never moved |
| Foundation TGE unlock (17% × 12.5%) | [`0x97ce…3f27`](https://etherscan.io/address/0x97ce88a5dba86c4c0de250394612ba9f1a5c3f27) ([tx](https://etherscan.io/tx/0xa214084b238ca37a7dc1a39fd85150494e86339f9c9d2f306d377b31169af38d)) | 212,500,000 | EOA, never moved |
| Community liquidity (37.5% × 12.5%) | [`0xf9fe…12cc`](https://etherscan.io/address/0xf9fe4f7279207b6795f8c94b96de86f127fe12cc) | 216,682,159 | EOA with an EIP-7702 delegation (not a Safe; Arkham shows no signers) |

**Arkham check ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** the six allocation wallets ([0xc2ed](https://intel.arkm.com/explorer/address/0xc2ed4aa16d749c50fb3be34cdc99b80ef42899e6) 3.1B · [0x5eaa](https://intel.arkm.com/explorer/address/0x5eaa87a6867d29a6288424a238a3d0dba9ec951d) 3.281B · [0x1c5e](https://intel.arkm.com/explorer/address/0x1c5e97a7b4fe01bba50827e3dd78bd9f272bee4b) 1.488B · [0x588f](https://intel.arkm.com/explorer/address/0x588f42183046d626470e5019e02a2b3ba97e994b) 1.1B · [0xd31b](https://intel.arkm.com/explorer/address/0xd31bc138a2438cfb676f50053b10697d990fa8d7) 350M · [0x97ce](https://intel.arkm.com/explorer/address/0x97ce88a5dba86c4c0de250394612ba9f1a5c3f27) 212.5M) are unlabelled "KAIO Whale" addresses with no custodian label. Their Arkham transfer tables read **"No transfers match these filters"**, so no selling is inferred from them. The deployer [`0xfddf…`](https://intel.arkm.com/explorer/address/0xfddf70861a4ffd7cb52a1ee992b42020f3cd1419) carries only a generic token-deployer tag.

**What it means:** Insiders and the foundation control ~95% of supply. Nothing has moved from the locked wallets, which is good, but the locks are not enforced on-chain. Score **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL

Pump test uses KuCoin KAIO-USDT daily closes (from 6 May 2026); CoinGecko closes agree. Exchange and market-maker labels are Etherscan name tags [Tier B]; transfers are Tier A.

| Day (UTC) | Route | KAIO | 5-day change | Pump? |
|---|---|---:|---:|---|
| 5–6 May 2026 (TGE) | Liquidity wallet → Wintermute via [`0xaa9f…`](https://etherscan.io/address/0xaa9f8b6c6d1ca0d5abd96357a7871864173edb3c) ([tx](https://etherscan.io/tx/0x838a25f1b972bead7b828a979e29cbb58bb236ab61f96dca18b6e68a431e7882)); → Jump Trading via [`0x437f…`](https://etherscan.io/address/0x437f000b58cf0bbfe89ab29b9a6d6511c6f3bd44) ([tx](https://etherscan.io/tx/0xcc3ceead803da59d22d9daafa342f5ee8413e8c4faf153c4662a58a6be073532)); → Gate ([tx](https://etherscan.io/tx/0x741ab9f562b6701f2d3dc3b118bf8256ded06b9ca981348233af48641c8c3c09)), KuCoin ([tx](https://etherscan.io/tx/0xbcf0b5abb2aeffb4896e325b05f7f6acb07db189361d48e9568214163f16d9da)), Bitget (20M via `0x59f2`→`0x3103`) | 37.5M + 25M + 10M + 7M + 20M | launch | Disclosed purpose: liquidity |
| 30 Jun – 21 Jul 2026 | Liquidity wallet → [`0x1fee…`](https://etherscan.io/address/0x1feeb6c6b92864b82aed16391eba223becd568d0) 12.5M ([tx](https://etherscan.io/tx/0x188ff50f4c0ae1a0333f27746f73947fd561f328b3b95912faa2058c6efda04a)) → Gate deposit 7.61M in four lots | 7,613,586 | <10% | No |
| **1 Oct 2026** | Liquidity wallet → new wallet `0x7875` 13M ([tx](https://etherscan.io/tx/0xb48978b227246d86600fd025452dc757d437b07e04a8abd44d893f91fc87e565)) → Gate deposit [`0x485c…`](https://etherscan.io/address/0x485ca09ba5bde91ebcad9ff2393ee96401ee0285) ([tx](https://etherscan.io/tx/0x2941ae6c76a81f601c0518c60c05797a7a49932584973665aa2c1fc94e6070ab)) | 3,000,000 | **+43.0%** | 🔴 Yes |
| **2 Oct 2026** | `0x7875` → Coinbase deposit [`0x5fac…`](https://etherscan.io/address/0x5fac7bbf222a1236f91f2985f8434cf505385369) ([tx](https://etherscan.io/tx/0x03bf7e211a05862fe916811fccc45a4634684e0c476d5c9ddd6b363c14c93b1a)), swept to a Coinbase hot wallet 4 min later ([tx](https://etherscan.io/tx/0xe67b58f2ecaef47bc89bdbb872178ec9b92631abdbedcd5605f71aa7300c29e9)) | 2,999,990 | **+51.0%** | 🔴 Yes (corrected: Arkham labels `0x5fac` a Coinbase deposit) |
| **8 Oct 2026** | `0x7875` → Bitget deposit [`0x5420…`](https://etherscan.io/address/0x54206b5386d927db00f7eb5bb57aae43f91e4507) ([tx](https://etherscan.io/tx/0x3e54f39001ca111210a25ad8ab6f9f061985b621a5a4206707fdcbe36729be5a)) | 3,999,900 | **+28.3%** | 🔴 Yes |

- The liquidity wallet also sent 100M in tranches (25M on 5 May, 50M on 21 Jul and 25M on 2 Sep 2026, per Etherscan) to [`0x437f`](https://intel.arkm.com/explorer/address/0x437f000b58cf0bbfe89ab29b9a6d6511c6f3bd44). Arkham labels `0x437f` itself **Jump Crypto**. It still holds 75M and passed 25M on to another Jump wallet (`0xf584…`, Etherscan "Jump Trading") on 6 May 2026. This is market-maker / fund flow, not a team sale. Market-maker agreements were not published.
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** [`0xaa9f…`](https://intel.arkm.com/explorer/address/0xaa9f8b6c6d1ca0d5abd96357a7871864173edb3c) is a **Wintermute deposit** address, so the 37.5M at TGE went to a market maker. [`0x7875…`](https://intel.arkm.com/explorer/address/0x787563c7f4a1f9fdeb84b828a509314bd6acb2e2) is unlabelled. Besides the KAIO deposits it moved USDC both ways with Coinbase and Gate, which looks like a trading wallet, but no owner is named [Unverified]. [`0x5fac…`](https://intel.arkm.com/explorer/address/0x5fac7bbf222a1236f91f2985f8434cf505385369) is a **Coinbase deposit**.
- None of the six allocation wallets has sent a single token.

**What it means:** The insider buckets have not sold. But the project's liquidity wallet fed a fresh wallet that put 10M KAIO onto Gate, Coinbase and Bitget on three pump days (corrected from 7M on two days once Arkham identified the Coinbase deposit). The size is small, and the "liquidity" purpose is disclosed, but the timing and the intermediary wallet were not. Score **3** (unchanged), which **trips the Selling gate**.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- 10B fixed supply, 6.8% circulating; FDV is **14.7×** the market cap.
- Community and foundation buckets: 6-month cliff (ended ~6 Nov 2026), then 60 and 36 months linear. Team, early investors and pre-sale (45.5%): 12-month cliff to **6 May 2027**, then 24 months linear ([KuCoin](https://www.kucoin.com/news/insight/KAIO/69fb095b9514cf00076fe3eb) · [Tokenomics.com](https://app.tokenomics.com/tokenomics/kaio), Tier B ×2).
- Early investors paid **$0.00355** a token (Tokenomics.com) [Tier B]. At $0.0204 they are still up ~5.7× before their cliff opens.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $231k of 24h volume. Biggest books are Toobit, MEXC (USDC and USDT) and KCEX, each $25–56k; Coinbase and KuCoin under $8k each (CoinGecko tickers).
- −92% from launch day, −43% in 30 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Live tokenized funds: CASH (BlackRock ICS USD liquidity), SCOPE (Hamilton Lane), VOLT (Laser Digital), MACRO (Brevan Howard), MCAS (Mubadala), on Ethereum, Base, Solana and Sui ([kaio.xyz](https://www.kaio.xyz/)). Retail product "KASH" is waitlist-only.
- Public code is thin: `librecapital/kaio-token` was last pushed 2 Feb 2026; platform contracts are closed apart from audits.

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- The site shows fund TVLs of $64.7M (MCAS), $37.3M (CASH), $19.5M (VOLT), $18.0M (MACRO) and $16M (SCOPE) [Tier A, self-reported]. DefiLlama tracks $34.7M.
- Investors are private-bank clients onboarded by dealers ([docs](https://docs.kaio.xyz/guide-to-using-kaio/smart-contracts)): real customers, but permissioned and small.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Cyfrin audits from Mar 2025 to Feb 2026 (platform contracts, Solana gateway, enterprise bridge, receipt-token vault, holding-fee updates) plus API/AWS penetration tests ([audits repo](https://github.com/KAIO-xyz/audits/tree/main/reports)).
- No exploit found. The KAIO token itself is simple and verified.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Fund tokens carry eligibility, jurisdiction and transfer rules in the contract, and dealers do the KYC ([docs](https://docs.kaio.xyz/guide-to-using-kaio/smart-contracts)). No enforcement found. The KAIO token itself is a free-trading governance token with no stated legal opinion. The issuer's jurisdiction was not confirmed this pass.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Now (from ~6 Nov 2026) | Community and foundation linear unlocks begin (~4.77B over 3–5 years) |
| **6 May 2027** | Cliff opens for early investors, team and pre-sale (4.55B = 6.7× today's float) |
| TBD | KASH retail launch; whitepaper ("Soon") |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Treasury → exchange during a pump | 🔴 **Yes, via a fresh wallet:** liquidity wallet → `0x7875` → Gate and Bitget, 1 and 8 Oct 2026. [Gate tx](https://etherscan.io/tx/0x2941ae6c76a81f601c0518c60c05797a7a49932584973665aa2c1fc94e6070ab) |
| Unenforced lock-ups | 🔴 **Yes:** 93% of supply in five plain EOAs |
| Live mint path | 🟢 No: fixed supply |

## 📚 Sources

- [Tier A] Etherscan v2 API: `tokentx` (KAIO contract and ~15 traced wallets from the deployer), `tokenbalance`, `tokensupply`, `getsourcecode`, `getcontractcreation`; `eth_getCode` (EOA/contract test); read 16 Nov 2026 MST
- [Tier B] Etherscan name tags: "Jump Trading", "Wintermute 4", "Bitget 6", "Gate Deposit" (0xfb77, 0x74a5, 0x485c), "KuCoin Deposit", "Bitget Deposit"
- [Tier A] [kaio.xyz](https://www.kaio.xyz/) · [docs.kaio.xyz](https://docs.kaio.xyz/) · [audit reports](https://github.com/KAIO-xyz/audits/tree/main/reports) · [librecapital GitHub](https://github.com/librecapital)
- [Tier B] [KuCoin: TGE notice](https://www.kucoin.com/news/insight/KAIO/69fb095b9514cf00076fe3eb) · [KuCoin/Foresight tokenomics](https://www.kucoin.com/news/flash/kaio-reveals-tokenomics-37-5-allocated-for-community-and-liquidity-incentives) · [Bitget/Foresight](https://www.bitget.com/news/detail/12560605390886) · [Tokenomics.com](https://app.tokenomics.com/tokenomics/kaio) · [IQ.wiki](https://iq.wiki/wiki/kaio)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Jump Crypto (`0x437f`), Wintermute Deposit (`0xaa9f`), Coinbase Deposit (`0x5fac`); `0x7875`, `0xf9fe` and the allocation wallets unlabelled (links in Holdings and Selling). Etherscan `eth_getCode(0xf9fe…)` = EIP-7702 delegation (EOA)
- [Tier A] DefiLlama fees/revenue/TVL; CoinGecko `kaio` (16 Nov 2026 6:51 AM MST); KuCoin KAIO-USDT daily candles for every pump test
- [Unverified] owner of `0x7875`; market-maker terms with Jump and Wintermute; any vesting enforcement off-chain (custodian)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 10B minted to the deployer; six allocation transfers on 1 May 2026 match the published table | [mint](https://etherscan.io/tx/0xf61eb43f84aa08b2e82f605ef87a77c23555c4cef9ac6cd232e876a8d43eba6b) · [investors](https://etherscan.io/tx/0x11595c5de7701eab3b28405525a568d0263c62fe40b5ff0d40ead4e3a7dbad1d) · [community](https://etherscan.io/tx/0xda249531da9a56964b330c6145b38b6cfe357bade0e36173017bbc981053eca9) · [team](https://etherscan.io/tx/0xd19ad79ba89d675bdaaabff911517bf6d8245c3e0c752e37e55a9a5acfa04962) | A | 16 Nov 2026 |
| Allocation wallets are EOAs and have never moved | [0xc2ed](https://etherscan.io/address/0xc2ed4aa16d749c50fb3be34cdc99b80ef42899e6) · [0x5eaa](https://etherscan.io/address/0x5eaa87a6867d29a6288424a238a3d0dba9ec951d) · [0x1c5e](https://etherscan.io/address/0x1c5e97a7b4fe01bba50827e3dd78bd9f272bee4b) · [0x588f](https://etherscan.io/address/0x588f42183046d626470e5019e02a2b3ba97e994b) | A | 16 Nov 2026 |
| Liquidity wallet → 0x7875 13M on 1 Oct 2026 | [tx](https://etherscan.io/tx/0xb48978b227246d86600fd025452dc757d437b07e04a8abd44d893f91fc87e565) | A | 16 Nov 2026 |
| 0x7875 → Gate 3M (1 Oct), Coinbase 3M (2 Oct) and Bitget 4M (8 Oct) on pump days | [Gate](https://etherscan.io/tx/0x2941ae6c76a81f601c0518c60c05797a7a49932584973665aa2c1fc94e6070ab) · [Coinbase](https://etherscan.io/tx/0x03bf7e211a05862fe916811fccc45a4634684e0c476d5c9ddd6b363c14c93b1a) · [Arkham: Coinbase Deposit](https://intel.arkm.com/explorer/address/0x5fac7bbf222a1236f91f2985f8434cf505385369) · [Bitget](https://etherscan.io/tx/0x3e54f39001ca111210a25ad8ab6f9f061985b621a5a4206707fdcbe36729be5a) | A + B tag | 16 Nov 2026 |
| TGE market-maker transfers (Wintermute 37.5M, Jump 25M) | [Wintermute](https://etherscan.io/tx/0x838a25f1b972bead7b828a979e29cbb58bb236ab61f96dca18b6e68a431e7882) · [Jump](https://etherscan.io/tx/0xcc3ceead803da59d22d9daafa342f5ee8413e8c4faf153c4662a58a6be073532) | A + B tag | 16 Nov 2026 |
| Published allocation and vesting | [KuCoin](https://www.kucoin.com/news/insight/KAIO/69fb095b9514cf00076fe3eb) · [Bitget/Foresight](https://www.bitget.com/news/detail/12560605390886) | B ×2 | 16 Nov 2026 |
| Fees $235k since tracking; holder revenue $0 | [DefiLlama](https://defillama.com/protocol/kaio) | A | 16 Nov 2026 |
| Cyfrin audits | [reports](https://github.com/KAIO-xyz/audits/tree/main/reports) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who runs `0x7875`, and do the allocation EOAs sit with a custodian?** | Arkham (16 Nov 2026) names neither; `0x437f` is Jump Crypto and `0x5fac` a Coinbase deposit. Ask KAIO | Free |
| 2 | **Vesting enforcement** | Ask KAIO for vesting contracts or custodian attestations for the five allocation wallets; watch for any outflow after 6 Nov 2026 | Free |
| 3 | **Market-maker terms** | Ask KAIO for the Jump and Wintermute loan terms and whether 0x7875 is a market maker | Free |
| 4 | **Whitepaper / primary tokenomics** | Read the whitepaper when published and replace the Tier B allocation sources | Free |
| 5 | **6 May 2027 cliff** | Watch `0xc2ed`, `0x588f` and `0xd31b` for exchange deposits | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
