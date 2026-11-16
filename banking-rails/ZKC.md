---
ticker: ZKC
name: Boundless
chain: ethereum
contract: "0x000006c2a22ff4a44ff1f5d0f2ed65f781f55555"
overall_score: 3.4
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 3
  adoption_customers: 2
  security_audits: 6
  regulatory: 6
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes: emissions minted supply from 1.0B to 1.081B; end planned Q4 2026"
  team_wallet_to_exchange_during_pump: "not proven: an unlabelled distributor-like wallet funded by an Anchorage Digital custody address deposited 840,000 ZKC to Binance on 30 Aug 2026 (+53.3%); the custody client is not named"
  one_hop_sale_status: none_found
  entity_concentration: "four genesis-line wallets hold 424M (39%), two of them Anchorage Digital custody addresses for an unnamed client; no vesting contracts"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee data and no published revenue to holders."
pump_day_price_source: "Gate ZKC_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (25 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.02354
price_source: "CoinGecko, 16 Nov 2026 ~8:52 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZKC · Overall grade **3.4 / 10 · ❌ FAIL**

**Summary:** Boundless is a marketplace for zero-knowledge proofs. ZKC is staked as proving collateral and earned through emissions. On 5 Nov 2026 the proving protocol was paused and the project pivoted to "AI credits", so the token's main use is on hold. Price is down 98.7% from its listing-day high, and 39% of supply sits in four plain wallets on the genesis line. The revenue gate fails. The genesis wallet turns out to be an Anchorage Digital custody address, so the pump-day Binance deposit that tripped the selling gate is a custodian's client flow through an unlabelled distributor, not proven team selling.

**🚨 Top warning:** the genesis supply sits with a custodian for an unnamed client, and its funding chain reaches exchanges. Wallet [0x453a…d905](https://etherscan.io/address/0x453a7657477d84069df19e5236f07c244112d905) received the 550M genesis mint. It sent 149M to [0x16cd…982c](https://etherscan.io/address/0x16cdf88b991deb3c37e35fe25010906af4f1982c), which funded [0x7ee7…d4ad](https://etherscan.io/address/0x7ee7ffd5a2ec4e8acd87fc6eb51cc99e3aefd4ad). Arkham labels both 0x453a and 0x16cd **Anchorage Digital Custody**; 0x7ee7 is unlabelled and behaves like a market maker or distributor. It deposited **840,000 ZKC** to Binance on **30 Aug 2026**, when ZKC closed 53.3% above five days earlier ([tx](https://etherscan.io/tx/0x45c9f3ff693168b55973f912dfc4400f78fdaf78bca12f700e4dd3a8615c8c63)). It has made 8 Binance or Bybit deposits since Nov 2025. The genesis wallet itself sent **15M ZKC (~$3.6M)** straight to Binance on 24 Oct 2025 ([tx](https://etherscan.io/tx/0x4fe96d14398f1ffefdb7148e6f10487fe847817399d5c2a289bed9e8b5260e7e)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZKC · Boundless · 3.4 / 10 · ❌ FAIL

> **One line:** Protocol paused, no revenue, and 39% of supply in genesis-line wallets (partly at Anchorage custody) that keep feeding exchanges.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:52 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0x000006c2a22ff4a44ff1f5d0f2ed65f781f55555), 16 Nov 2026 ~9:05 AM MST) |
|---|---|
| **Price** $0.02354 | **Supply** 1,080,884,707 ZKC (1.0B genesis + emissions) |
| **24h / 7d / 30d** ⚪ −0.2% / 🔴 −14.4% / 🔴 −31.6% | **Genesis 550M wallet 0x453a** 131.2M |
| **Market cap** $6.84M · **FDV** $25.5M | **0xf52f (funded by 0x453a)** 126.0M |
| **24h volume** $1.65M (LBank $0.37M, Binance $0.26M) | **0x3b3a (funded by 0x7b81)** 121.1M |
| **Circulating** 290.6M (26.9%) | **0x7b81 (genesis 450M line)** 45.5M |
| **ATH** $1.78 (15 Sep 2025) · now −98.7% | |
| **Pump days** 25 in the last year (largest +54.9% on 25 Jan 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No fee data found, and the proving protocol has been paused since 5 Nov 2026. No published revenue to token holders. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee data and no published revenue to holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Incubated by the zkVM company that built it, with a foundation as token issuer. Leaders are described by role only. Wallet ownership is not published.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | ZKC | Origin |
|---|---:|---|
| [0x453a…d905](https://etherscan.io/address/0x453a7657477d84069df19e5236f07c244112d905) ([Arkham: Anchorage Digital Custody](https://intel.arkm.com/explorer/address/0x453a7657477d84069df19e5236f07c244112d905)) | 131.2M | 550M genesis mint, 4 Jun 2025 ([tx](https://etherscan.io/tx/0xe850a98f406e326dfd9f0a4d8305fd1b8067dc2bf7ae8b56871b6a36de7a40a3)) |
| [0xf52f…a063](https://etherscan.io/address/0xf52f9bdaea64d07b996f0aaf4cc91f1554eea063) ([Arkham: unlabelled](https://intel.arkm.com/explorer/address/0xf52f9bdaea64d07b996f0aaf4cc91f1554eea063)) | 126.0M | 180M from 0x453a, Aug 2025; sent 48.9M to another Anchorage Digital address |
| [0x3b3a…6f7f](https://etherscan.io/address/0x3b3ae156cfd7958847f109b610a90a2bfcb36f7f) ([Arkham: Anchorage Digital](https://intel.arkm.com/explorer/address/0x3b3ae156cfd7958847f109b610a90a2bfcb36f7f)) | 121.1M | 260.6M from 0x7b81, Dec 2025 |
| [0x7b81…f738](https://etherscan.io/address/0x7b81cd3a612b41d85225e3e16fa52d2dc01bf738) ([Arkham: unlabelled](https://intel.arkm.com/explorer/address/0x7b81cd3a612b41d85225e3e16fa52d2dc01bf738)) | 45.5M | 450M from the second genesis wallet 0x48a0, 3 Sep 2025 ([tx](https://etherscan.io/tx/0x50b1664ab4f710a990ab03ceb241a3520c2c38f620629aa45bbe7c06d3d44f1f)) |

- All four are plain wallets (no contract code), not vesting contracts. **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** 0x453a and 0x3b3a are **Anchorage Digital** custody addresses, as is 0x16cd, which received 149M from 0x453a. A qualified custodian holds them, but Arkham does not name the client (foundation or investors) [Unverified], and custody does not lock anything in code. Holdings stays **3**. Team and investor tokens (45%) are meant to sit behind a 1-year cliff and then 24 months of vesting. A "MerkleVester" contract [0x0ca7…00b9](https://etherscan.io/address/0x0ca704f0ddcae3f7eb81cc3fe9642c968b3100b9), funded through 0x3b3a, started paying out on 15 Sep 2026. That day its claims sent ~5.9M straight to five Binance deposit addresses.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

| Date | From | To | ZKC | Close | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---:|---|---|
| 24 Oct 2025 | Anchorage custody 0x453a (genesis wallet), for an unnamed client | Binance deposit | 15,000,000 | $0.2415 | $3.62M | No | [0x4fe9…](https://etherscan.io/tx/0x4fe96d14398f1ffefdb7148e6f10487fe847817399d5c2a289bed9e8b5260e7e) |
| 30 Aug 2026 | unlabelled 0x7ee7 (Anchorage 0x453a → Anchorage 0x16cd → 0x7ee7) | Binance deposit 0xeda5 | 840,000 | $0.0604 | $51k | **Yes, +53.3%** | [0x45c9…](https://etherscan.io/tx/0x45c9f3ff693168b55973f912dfc4400f78fdaf78bca12f700e4dd3a8615c8c63) |
| 15 Sep 2026 | MerkleVester claims | 5 Binance deposits | ~5.91M | $0.0388 | $229k | No | e.g. [0x4844…](https://etherscan.io/tx/0x48440c6ec0afd002731b017973275a623056977910e63f1f06cdd3ba7ee0ddc6) |
| 17 Sep 2026 | 0x7b81 | Coinbase Prime Deposit (Arkham) | 15,800,000 | $0.0381 | $602k | No | [0x6303…](https://etherscan.io/tx/0x630386bfa9bf4bc6a8bca4eb1f34a35c3605fbf04bebfa27ed9c2a7245435e54) |

- Before listing (12–16 Sep 2025), 0x16cd and 0xf52f funded ~52M ZKC of deposits to Binance, Bybit, Gate and others. That looks like listing and airdrop supply, not a sale.
- **Re-score after Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** 0x453a and 0x16cd are Anchorage Digital custody addresses, so the genesis → 0x16cd → 0x7ee7 chain is a custodian moving tokens on behalf of an unnamed client, not proven team flow. [0x7ee7](https://intel.arkm.com/explorer/address/0x7ee7ffd5a2ec4e8acd87fc6eb51cc99e3aefd4ad) is unlabelled and acts like a market maker or distributor: it currently sends small lots to Bybit, Bitget and Gate deposits. The only pump-day deposit (840k, ~$51k) therefore cannot be pinned on the team. The 15M Binance deposit from 0x453a (24 Oct 2025) came from the custodian for its client and was not on a pump day.
- Large genesis-line supply still reaches exchanges on ordinary days (15M to Binance, 15.8M to Coinbase Prime, MerkleVester claims to Binance), with no disclosure. Not proven clean, and heavy exchange flow → **4** (was 3). **The Selling gate no longer fails.** All linked transactions returned status 1.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate ZKC_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (25 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 26.9% circulating. 23.75M unlock each month on the 15th, and emissions added 81M (to end Q4 2026).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $1.65M of 24h volume against a $6.8M market cap. Down 98.7% from the listing-day high.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- Proving marketplace paused 5 Nov 2026, with a pivot to AI credits announced (Tier B).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- With the protocol paused, there is no current paying demand.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Monthly 23.75M unlocks continue while the product is paused.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟡 Not proven: 840k on 30 Aug 2026 came via Anchorage custody and an unlabelled distributor |
| Live mint path | 🟠 Emissions until Q4 2026 |
| Entity concentration | 🔴 39% in four genesis-line wallets (two at Anchorage custody), no vesting contracts |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Anchorage custody `0x453a…` (genesis wallet) | Anchorage Digital, for an unnamed client | Etherscan + Arkham | medium | no | None: custody flow, not a proven team sale |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan token, wallet and transaction pages, with exchange deposit labels; receipts checked 16 Nov 2026
- [Tier A] CoinGecko `boundless`; pump days from Binance ZKCUSDT daily closes
- [Tier B] Project announcements on the 5 Nov 2026 pause and pivot, and the tokenomics/unlock schedule
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Anchorage Digital Custody on 0x453a and 0x16cd; Anchorage Digital on 0x3b3a; 0x7ee7, 0x7b81, 0xf52f and 0x48a0 unlabelled; MerkleVester contract; Bybit, Bitget, Gate and Coinbase Prime Deposit labels

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 550M genesis to 0x453a | [tx 0xe850…](https://etherscan.io/tx/0xe850a98f406e326dfd9f0a4d8305fd1b8067dc2bf7ae8b56871b6a36de7a40a3) | A | 16 Nov 2026 |
| Pump-day Binance deposit | [tx 0x45c9…](https://etherscan.io/tx/0x45c9f3ff693168b55973f912dfc4400f78fdaf78bca12f700e4dd3a8615c8c63) | A | 16 Nov 2026 |
| 15M genesis → Binance | [tx 0x4fe9…](https://etherscan.io/tx/0x4fe96d14398f1ffefdb7148e6f10487fe847817399d5c2a289bed9e8b5260e7e) | A | 16 Nov 2026 |
| 15.8M → Coinbase Prime | [tx 0x6303…](https://etherscan.io/tx/0x630386bfa9bf4bc6a8bca4eb1f34a35c3605fbf04bebfa27ed9c2a7245435e54) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls 0x7ee7, and whose Anchorage vaults these are** | Arkham (16 Nov 2026) leaves 0x7ee7 unlabelled and does not name Anchorage's client. Ask Boundless for its market-maker and custody disclosures [Unverified] | Free |
| 2 | **Which genesis wallets hold team or investor tokens** | Ask the foundation for an address map | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
