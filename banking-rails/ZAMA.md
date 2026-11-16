---
ticker: ZAMA
name: Zama
chain: ethereum
contract: "0xa12cc123ba206d4031d1c7f6223d1c2ec249f4f3"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 2
  selling_behavior: 2
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 7
  adoption_customers: 5
  security_audits: 6
  regulatory: 6
  catalysts: 5
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes by design: 5% yearly emission to operators and stakers (supply 11.39B vs 11B initial)"
  team_wallet_to_exchange_during_pump: "yes: the Etherscan-labelled 'Zama 1' wallet sent 15,000,000 ZAMA to a Binance deposit address on 14 Apr 2026 (+39.1% pump day); no disclosure found"
  entity_concentration: "one plain EOA (single key) holds 7.665B ZAMA, 67.3% of supply"
price_usd: 0.05429
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZAMA · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Zama builds fully homomorphic encryption (FHE) for confidential smart contracts. The protocol is live, with staking, 18 operators and about $85M of TVL. The token launched on 2 Feb 2026. Fees are burned, but Zama deliberately keeps them near zero, so the revenue gate fails. The selling gate also fails: a Zama-labelled wallet deposited to Binance on a pump day. The custody setup is the biggest problem: **a single plain address (an EOA, not a vesting contract) holds 67.3% of all ZAMA**.

**🚨 Top warning:** **7,664,999,001 ZAMA (67.3% of supply, ≈$416M)** sits in one externally owned address, [0x6aed…2b28](https://etherscan.io/address/0x6aed4db2305b22cff494a15433975b7cc2732b28). It received the 9.68B genesis mint. The published team, VC and angel cliffs (Feb 2027) and the Treasury and Growth vesting are not enforced by any contract that could be found; whoever holds that key controls them. Separately, the Etherscan-labelled **"Zama 1"** wallet, which that address funded with 1.57B, sent [15M ZAMA to Binance on 14 Apr 2026](https://etherscan.io/tx/0x9240a25d1e7de5181e35c5ce70ec6a1aba2fdcdf8d67d9def5adc3378eba1caa), when the close was 39.1% above five days earlier. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 2/10 | ❌ FAIL (hard gate) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZAMA · Zama · 3.8 / 10 · ❌ FAIL

> **One line:** Real FHE technology, but two-thirds of the token sits behind a single key and fees are switched off.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0xa12cc123ba206d4031d1c7f6223d1c2ec249f4f3), 16 Nov 2026 ~9:05 AM MST) |
|---|---|
| **Price** $0.05429 | **Total supply** 11,391,483,308 ZAMA |
| **24h / 7d / 30d** 🟢 +0.3% / 🔴 −20.6% / −25.5% | **Circulating** 2.55B (CoinGecko) |
| **Market cap** $138.4M · **FDV** $618.4M | **Genesis EOA** 7.665B (67.3%) |
| **24h volume** $3.53M (Binance $1.24M, PancakeSwap $0.32M, OKX $0.27M, Bybit $0.26M, Uniswap $0.24M) | **"Zama 1" wallet** 7.0M left of 1.57B received |
| **ATH** $0.1074 (23 Sep 2026) · now −49.4% | **ZamaOFTAdapter 0xa798…a268** 266.8M (LayerZero bridge escrow) |
| **Pump days** 51 since listing (largest +102.5% on 22 Sep 2026) | **TVL** $84.5M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Fees for proof verification, decryption and bridging are paid in ZAMA and 100% burned ([staking post](https://www.zama.org/post/staking-is-now-live-on-mainnet)). DefiLlama has no fee record, and a research report says Zama keeps fees near zero on purpose (Tier B). **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- An established FHE company with a long research record. Governance runs through an Aragon DAO of the 18 elected operators, each with an equal vote. Leaders are described by role only.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Address | ZAMA | Type | Note |
|---|---:|---|---|
| [0x6aed…2b28](https://etherscan.io/address/0x6aed4db2305b22cff494a15433975b7cc2732b28) | 7,664,999,001 | EOA | Received the 9.68B genesis mint; 9 transfers in total. [Arkham](https://intel.arkm.com/explorer/address/0x6aed4db2305b22cff494a15433975b7cc2732b28): unlabelled (Whale), one 0.04 ETH funding transfer, no custodian or MPC identified |
| ["Zama 1" 0x5c17…67d4](https://etherscan.io/address/0x5c178c08363928c6296ed420eaeef73e21b667d4) | 7.0M | Labelled | Received 1.57B from the genesis EOA (Jan 2026). Unlabelled on [Arkham](https://intel.arkm.com/explorer/address/0x5c178c08363928c6296ed420eaeef73e21b667d4) (33.5M across all networks) |
| [ZamaOFTAdapter 0xa798…a268](https://intel.arkm.com/explorer/address/0xa798b04149e7a61cc95b7d114ad420e8969ea268) | 266,841,712 | Contract | LayerZero OFT bridge escrow: it locks ZAMA bridged off Ethereum. "Zama 1" deposited 380M into it on 27–28 Jan 2026. **Not a team wallet** |
| ["Zama: Public Auction"](https://etherscan.io/address/0x04a5b8c32f9c38092b008a4939f1f91d550c4345) | 0 | Contract | Received 440M; paid out auction claims at TGE |

- Published allocation: Team 20%, VCs 20%, Treasury 20%, Angels 10%, Growth 10%. The still-locked pools (about 7.8B by that table) match the EOA's balance, but nothing on-chain enforces the locks.

## 📉 Selling behavior — Do insiders sell into pumps? · 2/10 · ❌ FAIL (hard gate)

| Date | From | To | ZAMA | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---|---|
| 1 Apr 2026 | "Zama 1" | Binance Deposit 0xf2eb… | 10,000,000 | $228k | No | [0xf6f4…](https://etherscan.io/tx/0xf6f46911a4ccecf53d5b2a6f7390b9e4bf0e666635a1e6d3dbd1cca423b3c49b) |
| 14 Apr 2026 | "Zama 1" | Binance Deposit 0xf2eb… | 15,000,000 | $483k | **Yes, +39.1%** | [0x9240…](https://etherscan.io/tx/0x9240a25d1e7de5181e35c5ce70ec6a1aba2fdcdf8d67d9def5adc3378eba1caa) |

- **Correction:** 6.35M ZAMA that `0xa798…` sent to an Upbit deposit on 14 Apr 2026 is not a team sale. Arkham labels `0xa798` **ZamaOFTAdapter**, and the transaction ([tx](https://etherscan.io/tx/0xd4ac48eaba8eb67fefee47a7f12297a3070765c297a86f6979c2dcfd2fc42111)) is a LayerZero `lzReceive` delivery: someone bridged ZAMA from another chain to an Upbit deposit. The sender is unknown, so it is no longer counted.
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) on "Zama 1":** it sent 27.5M ZAMA to a **Wintermute deposit** on 31 Jul 2026 ([tx](https://etherscan.io/tx/0xc82e1fa5cf998270c2b9ee25c44815efb3894ff87e914d0735a790a9edfb58b5); −10.3% on Gate, not a pump day), market-maker flow rather than a sale. It also sent 25M ZAMA on 9 Nov 2026 ([tx](https://etherscan.io/tx/0x57bcbecb954cd156b1221a0fabfeaf0f18cc43951a826733262fa4bf68b4b8d2)) to a Safe that Arkham labels as belonging to a named Zama co-founder: an internal team transfer.
- These could be liquidity or market-making transfers (2% of supply was allocated to liquidity), but no disclosure was found. Exchange deposits from a team-labelled wallet on a pump day score 2 (unchanged after the Upbit correction: the 15M Binance deposit on 14 Apr still stands). Transfers at the 2 Feb 2026 launch (auction claims and exchange campaign funding) are treated as documented distribution. All linked transactions returned status 1 (success).

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 5% yearly emission to operators and stakers, and supply is already 11.39B against the 11B launch figure. The Feb 2027 cliff releases about 550M to the team, VCs and angels, followed by linear unlocks.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $3.5M of 24h volume (2.6% of market cap). FDV is 4.5 times market cap.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Mainnet is live with staking and 18 operators (13 KMS nodes and 5 FHE coprocessors). Confidential tokens such as cZAMA are deployed.

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- TVL is $84.5M (DefiLlama). Confidential DeFi value is about $120M (Tier B).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found. FHE plus threshold KMS. Key custody of the treasury is the weak point (see 🪙 above).

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Confidential, not anonymous, with selective disclosure. No enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Feb 2027 | Team, VC and angel cliff (about 550M), then linear unlocks |
| Ongoing | Treasury and Growth releases (about 117M a month, per unlock calendars) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: "Zama 1" → Binance, 14 Apr 2026 |
| Live mint path | 🟠 Yes, by design (5% emission) |
| Entity concentration | 🔴 67.3% in one EOA |

## 📚 Sources

- [Tier A] Etherscan token, address and transaction pages, with labels. Receipts were checked through the Etherscan API on 16 Nov 2026
- [Tier A] [Zama token launch post](https://www.zama.org/post/zama-token-launch) and [staking post](https://www.zama.org/post/staking-is-now-live-on-mainnet)
- [Tier B] Allocation and vesting tables (tokenomics.com, tokenradar), and a research report on fee policy
- [Tier A] CoinGecko `zama`; DefiLlama TVL; pump days from Binance ZAMAUSDT daily closes
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): 0x6aed unlabelled; ZamaOFTAdapter on 0xa798; Wintermute Deposit and a co-founder-labelled Safe among "Zama 1"'s counterparties
- [Tier A] Etherscan v2 API `tokentx` for "Zama 1" and the 14 Apr 2026 receipt of tx 0xd4ac (LayerZero delivery)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 67.3% of supply in one EOA | [0x6aed…2b28](https://etherscan.io/address/0x6aed4db2305b22cff494a15433975b7cc2732b28) | A | 16 Nov 2026 |
| "Zama 1" → Binance on a pump day | [tx 0x9240…](https://etherscan.io/tx/0x9240a25d1e7de5181e35c5ce70ec6a1aba2fdcdf8d67d9def5adc3378eba1caa) | A | 16 Nov 2026 |
| 6.35M to Upbit on 14 Apr was a bridge delivery, not a team sale | [tx 0xd4ac…](https://etherscan.io/tx/0xd4ac48eaba8eb67fefee47a7f12297a3070765c297a86f6979c2dcfd2fc42111) · [Arkham: ZamaOFTAdapter](https://intel.arkm.com/explorer/address/0xa798b04149e7a61cc95b7d114ad420e8969ea268) | A + B | 16 Nov 2026 |
| Fees burned; 5% emission | [Zama staking post](https://www.zama.org/post/staking-is-now-live-on-mainnet) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **How the locked allocations are custodied** | Arkham (16 Nov 2026) leaves 0x6aed…2b28 unlabelled. Ask Zama whether it is an MPC or custodian address [Unverified] | Free |
| 2 | **Was the 14 Apr deposit market making?** | Look for a liquidity-provider disclosure | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
