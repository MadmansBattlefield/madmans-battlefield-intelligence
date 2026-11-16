---
ticker: ZKP
name: zkPass
chain: ethereum
contract: "0xe1be424f442d0687129128c6c38aace44f8c8dbc (BSC 0xd89b7dd376e671c124352267516bef1c2cc231a3)"
overall_score: 3.1
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 2
  selling_behavior: 1
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 6
  catalysts: 4
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: fixed 1B supply minted at genesis"
  team_wallet_to_exchange_during_pump: "yes: the Safe that receives monthly community and DAO unlocks sent 1,125,414 ZKP to a Binance deposit address on 3 Jul 2026, a +30.6% pump day; no disclosure found"
  entity_concentration: "four project Safes hold 692.5M ZKP (69% of supply); investor and team cliffs sit in plain Safes, not vesting contracts"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee or revenue record."
pump_day_price_source: "Gate ZKP_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 319 days); the body's earlier count used the daily closes cited in the body"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions:
  - address: "0x491a6acfeab80b4bd80dc25d949d7c45c310f5be"
    label: "Receives monthly community and DAO unlocks"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan (unlock contract payouts)"
price_usd: 0.02973
price_source: "CoinGecko, 16 Nov 2026 ~8:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZKP · Overall grade **3.1 / 10 · ❌ FAIL**

**Summary:** zkPass is a zkTLS protocol for proving web data privately. Its token launched on 19 Dec 2025 and is down 87% from its launch-week high. **69% of supply sits in four project Safes** created at genesis. The investor (225M) and core-contributor (140M) allocations are held in plain multisig Safes, not time-locked vesting contracts, so the published cliffs are a promise, not code. No fees exist, the Safe that pays out monthly unlocks sent ZKP to Binance on a pump day, and 87% of volume is on one exchange. Both hard gates fail.

**🚨 Top warning:** the vesting is not enforced on-chain. The genesis Safe split supply on 26 Nov 2025 into Safes holding **225,000,000** and **140,000,000** ZKP. Those amounts exactly match the 22.5% investor and 14% core-contributor allocations ([zkPass docs](https://docs.zkpass.org/zkpass-dao/zkp)). Both are ordinary Safes that their signers could move at any time. The **first investor unlock is 19 Dec 2026** (12.5M a month). Separately, the unlock-payout Safe sent [1.13M ZKP to Binance on 3 Jul 2026](https://etherscan.io/tx/0x10347a1bc316a8edb4171b0372d1af2c8d36e936a1f3f5e9166550b8b0b1ef5b) (+30.6% pump). Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZKP · zkPass · 3.1 / 10 · ❌ FAIL

> **One line:** A $6M float with 69% of supply in project multisigs and vesting that is not locked in code.

| 📊 Market (CoinGecko, 16 Nov 2026 ~8:40 AM MST) | 🔗 On-chain ([Etherscan](https://etherscan.io/token/0xe1be424f442d0687129128c6c38aace44f8c8dbc), 16 Nov 2026 ~9:00 AM MST) |
|---|---|
| **Price** $0.02973 | **Supply** 1B (921.7M on Ethereum, the rest bridged to BSC) |
| **24h / 7d / 30d** 🟢 +0.2% / 🔴 −17.4% / −32.2% | **Circulating** 201.7M (CoinGecko) |
| **Market cap** $6.0M · **FDV** $29.7M | **Project Safes** 692.5M (69%) |
| **24h volume** $4.51M (LBank $3.94M, Upbit $0.31M, Binance $0.14M) | **Investor Safe** 225.0M, never moved |
| **ATH** $0.2329 (19 Dec 2025) · now −87.2% | **Core-contributor Safe** 140.0M, never moved |
| **Pump days** 27 since the Binance listing (largest +41.1% on 28 Apr 2026) | **Next unlocks** 19 Nov (6.67M), 19 Dec 2026 (19.17M incl. investors) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No DefiLlama fee or revenue record, and no published protocol revenue. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee or revenue record.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- A DAO structure with a foundation share. Allocations are published in the [docs](https://docs.zkpass.org/zkpass-dao/zkp). Leaders are described by role only; Safe signers are not disclosed.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Safe (all 4-signature threshold) | ZKP | Likely allocation (by amount) |
|---|---:|---|
| [0xfc12…a66e](https://etherscan.io/address/0xfc128c6b4049b1a45dfc0a2d02a9e6edf51ba66e) | 245.8M | Community (received 485M) |
| [0x303a…ccef](https://etherscan.io/address/0x303a3ff74fb2c6f05cdb18161611a4146743ccef) | 225.0M | Early investors, 22.5% |
| [0xb845…90b7](https://etherscan.io/address/0xb845c1d9e15b38ea5a00bac2efc57278d90490b7) | 140.0M | Core contributors, 14% |
| [0x7f84…7baf](https://etherscan.io/address/0x7f8410796549a621cd4dc8ff631dbdc477007baf) | 81.7M | Genesis Safe / DAO treasury |

- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)):** all four are generic Gnosis Safes with no entity label. [0x7f84](https://intel.arkm.com/explorer/address/0x7f8410796549a621cd4dc8ff631dbdc477007baf) pays 1.667M ZKP a month and [0xfc12](https://intel.arkm.com/explorer/address/0xfc128c6b4049b1a45dfc0a2d02a9e6edf51ba66e) 5M a month to the payout Safe [0x491a](https://intel.arkm.com/explorer/address/0x491a6acfeab80b4bd80dc25d949d7c45c310f5be), which spreads 0.5–1M lots to about 14 unlabelled wallets. [0x303a](https://intel.arkm.com/explorer/address/0x303a3ff74fb2c6f05cdb18161611a4146743ccef) and [0xb845](https://intel.arkm.com/explorer/address/0xb845c1d9e15b38ea5a00bac2efc57278d90490b7) show no transfers. The investor and contributor mapping stays inferred from amounts [Unverified].
- The 123.3M ZKP at [`0x3C0c…8b04`](https://intel.arkm.com/explorer/address/0x3c0c57713342aa593e5dac69efa8fa06a05e8b04) is an **Upbit deposit address** (exchange custody), not an insider.
- The genesis Safe received all 1B ZKP and split it on 26 Nov 2025. The investor and contributor Safes match the documented allocations exactly, which is why the mapping is inferred. None of these Safes has an Etherscan label.

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

| Date | From | To | ZKP | ≈ USD | Pump? | Tx |
|---|---|---|---:|---:|---|---|
| 3 Jul 2026 | Unlock-payout Safe [0x491a…f5be](https://etherscan.io/address/0x491a6acfeab80b4bd80dc25d949d7c45c310f5be) | Binance Deposit | 1,125,414 | $69k | **Yes, +30.6%** | [0x1034…](https://etherscan.io/tx/0x10347a1bc316a8edb4171b0372d1af2c8d36e936a1f3f5e9166550b8b0b1ef5b) |
| 16 Dec 2025 | Community Safe | ByBit Deposit | 2,169,258 | — | Pre-listing | [0x35c5…](https://etherscan.io/tx/0x35c5555797e2e8a660c50b6915cff15670d5b7518585578618cc2a686ddfd1fa) |

- 0x491a…f5be is a Safe. It receives the monthly community unlocks (49.6M) and DAO unlocks (15.0M). The community pool covers "exchange-related marketing", so the Binance deposit may be a campaign, but no disclosure was found. Around launch, the 50M liquidity allocation was spread across exchanges as documented. Arkham shows a 30M ZKP transfer from the community Safe to a Binance-labelled address about 10 months ago; on Etherscan the only 30M outflow went to the contract `0xdaa9…97ce` on 18 Dec 2025 ([tx](https://etherscan.io/tx/0x5b1a02e827fac9c695be521726907801c4b8f00870c1637dc020cc5b16226841)), the day before trading opened, and that contract then paid out many small lots. That is a pre-listing launch distribution, not a pump-day sale [Unverified as to the campaign]. Both linked transactions returned status 1 (success).

- **Disclosure quality (16 Nov 2026 rules): silence.** The community pool may fund "exchange-related marketing", but no disclosure was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **3 → 1**. 3 Jul 2026 is a pump day on Gate prices. Pump days from Gate ZKP_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 319 days); the body's earlier count used the daily closes cited in the body.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- Fixed 1B supply, but 70% is still to unlock through Dec 2030. Monthly unlocks triple to 19.17M from 19 Dec 2026, roughly 9.5% of today's float each month.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $4.5M of 24h volume, but 87% of it is on LBank. Binance spot volume is $135k.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- A zkTLS protocol with a published [whitepaper](https://paper.zkpass.org/zkPass_WP2025.pdf). No usage metrics.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No verified usage or customer data.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found. Custody of 69% of supply depends on 4-signature Safes whose signers are not disclosed.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| 19 Nov 2026 | 6.67M unlock (community and foundation) |
| 19 Dec 2026 | First investor unlock; 19.17M a month from here |
| 19 Dec 2027 | Core-contributor cliff |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Yes: unlock Safe → Binance, 3 Jul 2026 |
| Live mint path | 🟢 None |
| Entity concentration | 🔴 69% in project Safes; vesting not enforced in code |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [Unlock-payout Safe `0x491a…f5be`](https://etherscan.io/address/0x491a6acfeab80b4bd80dc25d949d7c45c310f5be) | Receives monthly community and DAO unlocks | Etherscan (unlock contract payouts) | high | yes (on-chain) | Selling: 1,125,414 ZKP into a Binance deposit on the 3 Jul 2026 pump day (+30.6%) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan token, Safe and transaction pages. Receipts and Safe thresholds were checked through the Etherscan API on 16 Nov 2026
- [Tier A] [zkPass token docs](https://docs.zkpass.org/zkpass-dao/zkp) and [whitepaper](https://paper.zkpass.org/zkPass_WP2025.pdf) (allocation and vesting)
- [Tier B] Unlock calendars (tokenomics.com, coinlaunch) for monthly unlock sizes
- [Tier A] CoinGecko `zkpass`; pump days from Binance ZKPUSDT daily closes
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): generic Safe labels on all four Safes and the payout Safe; Upbit Deposit on 0x3c0c; Binance-labelled recipient of the Dec 2025 30M transfer
- [Tier A] Etherscan v2 API `tokentx` for the community Safe

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Investor allocation in a plain Safe (225M) | [0x303a…ccef](https://etherscan.io/address/0x303a3ff74fb2c6f05cdb18161611a4146743ccef) | A | 16 Nov 2026 |
| Contributor allocation in a plain Safe (140M) | [0xb845…90b7](https://etherscan.io/address/0xb845c1d9e15b38ea5a00bac2efc57278d90490b7) | A | 16 Nov 2026 |
| Unlock Safe → Binance on a pump day | [tx 0x1034…](https://etherscan.io/tx/0x10347a1bc316a8edb4171b0372d1af2c8d36e936a1f3f5e9166550b8b0b1ef5b) | A | 16 Nov 2026 |
| Allocation percentages and cliffs | [zkPass docs](https://docs.zkpass.org/zkpass-dao/zkp) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Confirm which Safe is which allocation; signers** | Arkham (16 Nov 2026) gives no entity for any of the Safes. Ask zkPass for the allocation-to-Safe map and signer list [Unverified] | Free account |
| 2 | **Whether the 3 Jul deposit was a disclosed campaign** | Check zkPass announcements around 3 Jul 2026 | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
