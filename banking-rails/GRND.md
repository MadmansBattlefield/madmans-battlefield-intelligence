---
ticker: GRND
name: SuperWalk
chain: kaia
contract: "0x84f8c3c8d6ee30a559d73ec570d574f671e82647"
overall_score: 4.2
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 2
  product_development: 5
  adoption_customers: 5
  security_audits: 4
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no further mint seen: 1B minted once at deploy (block 95,356,998)"
  team_wallet_to_exchange_during_pump: "none found: 0 transfers from 9 traced allocation/reserve wallets on the 30 pump days"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "yes: unreleased move-to-earn (115M) and ecosystem (14.6M) GRND sit in EOAs 0x2890e9710fbf673ee930f7515c3d659ca9fb5751 and 0xd692bee951304510a51bd8a67a2eef49b047bd45"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "The token only recycles in-app spending; the one-off buyback was a company decision, not an automatic on-chain mechanism, so revenue does not reach holders."
pump_day_price_source: "Gate GRND_USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x3b58a4c865b568a2f6a957c264f6b50cba35d8ce"
    label: "SuperWalk: SuperWalk (GRND) token"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + Arbiscan token"
price_usd: 0.00652
price_source: "CoinGecko, 16 Nov 2026 9:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### GRND · Overall grade **4.2 / 10 · ❌ FAIL**

**Summary:** SuperWalk is a Korean move-to-earn pedometer app run by Proground. GRND is its fixed 1B governance and in-app token on Kaia (all minted at deploy to [0x846c…b4db](https://kaiascan.io/address/0x846c4fd91f04a52a22768f508eac16d7a3feb4db)). The company reports ~100k MAU and ~30k DAU. In-app spending recycled 9.26M GRND in July 2026, and a one-off ₩30M buyback (1 Aug 2026) was funded from B2B campaign revenue ([AMA summary](https://superwalknavi.com/ama-media/20260804/), Tier B). That is a token sink, not protocol revenue, so Revenue sits at the hard-gate line. Wallet behaviour is clean: across the 30 pump days, none of the nine traced allocation and reserve wallets moved GRND. Monthly releases from the [move-to-earn reserve](https://kaiascan.io/address/0x2890e9710fbf673ee930f7515c3d659ca9fb5751) follow the published schedule. The weak spots are liquidity (~95% of volume on Bithumb KRW) and reserves held in single-key EOAs.

**🚨 Top warning:** About 95% of the $1.97M daily volume is on one venue (Bithumb KRW), against a $5.35M market cap. The remaining 129.6M unreleased GRND (15.8% of circulating) sits in two plain EOAs ([0x2890…5751](https://kaiascan.io/address/0x2890e9710fbf673ee930f7515c3d659ca9fb5751), [0xd692…bd45](https://kaiascan.io/address/0xd692bee951304510a51bd8a67a2eef49b047bd45)) with no multisig or timelock. Price is −74% in a year and −98.3% from ATH.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 5/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 GRND · SuperWalk · 4.2 / 10 · ❌ FAIL

> **One line:** A real consumer app with clean wallets, but a thin, single-venue token with only a token sink for revenue.

| 📊 Market (CoinGecko, 16 Nov 2026 9:11 AM MST) | 🔗 On-chain (Kaia RPC, 16 Nov 2026) |
|---|---|
| **Price** $0.00652 · 1y −74.4% · ATH $0.3848 (2023) −98.3% | **Total supply** 1,000,000,000 (Kaia); 2,619,507 bridged on Arbitrum |
| **Market cap** $5.35M · FDV $6.2M · circ 821.5M | **M2E reserve** [0x2890…5751](https://kaiascan.io/address/0x2890e9710fbf673ee930f7515c3d659ca9fb5751): 115.0M · **Ecosystem reserve** [0xd692…bd45](https://kaiascan.io/address/0xd692bee951304510a51bd8a67a2eef49b047bd45): 14.6M |
| **24h volume** $1.97M, of which Bithumb KRW $1.86M (~95%) | **Pump-day outflows** from 9 traced wallets: 0 |
| **Pump days** 30 in 365 (Gate GRND/USDT) | Releases ~9.1M a month (7.67M M2E + 1.46M ecosystem) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| In-app GRND used (sink) | 6.29M / 6.71M / 9.26M (May / Jun / Jul 2026) | [Tier B] [AMA summary](https://superwalknavi.com/ama-media/20260804/) |
| Buyback | ₩30M (~$21k), 1 Aug 2026, from B2B revenue; no further commitment | same |
| DefiLlama fees | Not listed | [Tier A] api.llama.fi |

**What it means:** the company has ad and B2B revenue, but the token only recycles spending. **3 (hard gate).**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** The token only recycles in-app spending; the one-off buyback was a company decision, not an automatic on-chain mechanism, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Proground (Korea) has operated the app since 2022. Partners have included Kyobo Life Insurance and LG Uplus Medialog ([Asia Business Daily](https://www.asiae.co.kr/en/article/2026032310393420983), Tier B).

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Allocation path | Now | Source |
|---|---|---|
| Deploy mint 1B → [0x846c…b4db](https://kaiascan.io/address/0x846c4fd91f04a52a22768f508eac16d7a3feb4db) | 0 | [Tier A] Kaia logs, block 95,356,998 |
| 5 allocation contracts (M2E 460M, team 2×150M, 160.6M, 55.1M) → swept to new EOAs ~30 Sep 2024 | 0 | [Tier A] e.g. [0xce9ba282…](https://kaiascan.io/tx/0xce9ba2821d7455973ac4d723b70a4177c2d8a7f835eae00bf0cf93898fb6d414) (460M) |
| Team EOAs paid out monthly; last release Aug 2025 | 0 | [Tier A] [0xaa3b557d…](https://kaiascan.io/tx/0xaa3b557db34ccb48efeda7deb5ab6da524410f7e969dc2626e0d2f9c96924756) |
| M2E remainder 168.67M → [0x2890…5751](https://kaiascan.io/address/0x2890e9710fbf673ee930f7515c3d659ca9fb5751) (7 May 2026) | 115.0M | [Tier A] [0xf0b5676a…](https://kaiascan.io/tx/0xf0b5676a2bb97ee993312cbcac083bc5de3047c9728c84004054009c04039fd1) |
| Ecosystem remainder 24.84M → [0xd692…bd45](https://kaiascan.io/address/0xd692bee951304510a51bd8a67a2eef49b047bd45) (7 May 2026) | 14.6M | [Tier A] [0x8d1b2c01…](https://kaiascan.io/tx/0x8d1b2c018e6886aacd55627bca85c0258a4c9ce5b11daee92d0f3ba81655f019) |

- Team, partners, private sale and advisors are 100% released [Tier B, NAUT; matches the on-chain sweep]. A free holder list for Kaia was not reachable.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Gate GRND/USDT daily closes (UTC): 30 pump days in the last 365.*

- **0 transfers** on any pump day from the five allocation contracts, the five sweep EOAs, the two team payout EOAs, or the two 2026 reserves (Kaia `eth_getLogs` per pump day).
- Reserve releases ran on 28 May, 8 Jun, 7 Jul, 12 Aug and 7 Oct 2026, none of them pump days. Examples: [0xfd04ec85…](https://kaiascan.io/tx/0xfd04ec858ecb1a101972f624432ed004ec6ab7eaef1a80bb50719325a074f380) (15.33M → [0x2126…aabe](https://kaiascan.io/address/0x2126e44589baebcbd489988431c4c91d21d3aabe)), [0x91688e3e…](https://kaiascan.io/tx/0x91688e3e742667839cb96fdb42e4a4a6cc67917d5d5d01dd8ab639117fbb20f1) (15.33M → [0xc460…a33b](https://kaiascan.io/address/0xc4605a499fabf9aebb7b78df6ee0f0d4e17da33b)), [0x55c15940…](https://kaiascan.io/tx/0x55c159405f0ce3dc2392e704a6914d3d65517e173d259a7225d16a6565807c57) (2.92M → [0x1126…e8fc](https://kaiascan.io/address/0x11261f50e2fa22194082342880f2472f4260e8fc)).
- The recipients ([0xc460…a33b](https://kaiascan.io/address/0xc4605a499fabf9aebb7b78df6ee0f0d4e17da33b), [0x1126…e8fc](https://kaiascan.io/address/0x11261f50e2fa22194082342880f2472f4260e8fc), [0xffc9…eb13](https://kaiascan.io/address/0xffc9101fdc7ac4ef7cf0a74509ed15a43ec4eb13)) were not traced further.

**What it means:** no pump-timed insider selling found; downstream of releases is unknown. **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate GRND_USDT UTC daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed 1B ([docs](https://docs.superwalk.io/english/tokenomics/usdgrnd-governance-token), Tier A); 87.7% released. The remaining ~9M a month runs to Feb 2028 [Tier B, NAUT].

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- ~95% of volume on Bithumb KRW; Gate and MEXC are thin. Volume of $1.97M against a $5.35M cap suggests KRW retail churn. **2**.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Four years live (Basic and Pro modes). Basic mode ad revenue per user now exceeds rewards (company claim, Tier B).

## 🤝 Adoption & customers · 5/10 · ❌ FAIL

- ~100k MAU and ~30k DAU (Aug 2026), 520k cumulative users (Mar 2026), ₩41B of cumulative NFT trades [Tier B ×2].

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found. Reserves sit in single-key EOAs. No token audit located.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Listed on Bithumb under the Korean listing regime. No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| 1 Dec 2026 | 9.3M GRND release (M2E + ecosystem) [Tier B] |
| Feb 2028 | Final release |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None found (0 pump-day transfers) |
| Live mint path | 🟢 None seen after the deploy mint |
| Treasury in single-key wallets | 🔴 129.6M unreleased GRND in two EOAs |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x3b58…d8ce](https://intel.arkm.com/explorer/address/0x3b58a4c865b568a2f6a957c264f6b50cba35d8ce) (Arbitrum) | SuperWalk: SuperWalk (GRND) token | Arkham + Arbiscan token | high | yes | None |
| Kaia allocation and reserve wallets | Not covered (Arkham has no Kaia coverage) | — | — | — | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the Arbitrum GRND contract (labelled SuperWalk); Kaia wallets are outside Arkham coverage
- [Tier A] Kaia public RPC (`eth_getLogs`, historical `balanceOf`, `eth_getCode`, nonces); Etherscan v2 Arbitrum `tokensupply`
- [Tier A] [SuperWalk GRND docs](https://docs.superwalk.io/english/tokenomics/usdgrnd-governance-token)
- [Tier B] [AMA summary, Aug 2026](https://superwalknavi.com/ama-media/20260804/) · [NAUT unlocks](https://naut.so/unlocks/superwalk-grnd) · [Asia Business Daily](https://www.asiae.co.kr/en/article/2026032310393420983) · [IT Times](https://www.ittimes.com/news/articleView.html?idxno=1067)
- [Tier A] CoinGecko `superwalk` (16 Nov 2026 9:11 AM MST); Gate GRND/USDT daily candles

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| M2E remainder moved to a single EOA | [0xf0b5676a…](https://kaiascan.io/tx/0xf0b5676a2bb97ee993312cbcac083bc5de3047c9728c84004054009c04039fd1) | A | 16 Nov 2026 |
| Monthly release, not on a pump day | [0xfd04ec85…](https://kaiascan.io/tx/0xfd04ec858ecb1a101972f624432ed004ec6ab7eaef1a80bb50719325a074f380) | A | 16 Nov 2026 |
| 2024 allocation sweep | [0xce9ba282…](https://kaiascan.io/tx/0xce9ba2821d7455973ac4d723b70a4177c2d8a7f835eae00bf0cf93898fb6d414) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham attribution of the GRND wallets** | Done 16 Nov 2026: Arkham labels only the Arbitrum token contract; it does not cover Kaia, where the allocation wallets live. Ask SuperWalk to publish its reserve wallets | Free |
| 2 | **Release recipients** | Trace [0xc460…a33b](https://kaiascan.io/address/0xc4605a499fabf9aebb7b78df6ee0f0d4e17da33b) and [0x1126…e8fc](https://kaiascan.io/address/0x11261f50e2fa22194082342880f2472f4260e8fc) to exchanges | Free (slow RPC) |
| 3 | **Holder concentration** | Kaiascan holders page (API key) | Free key |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
