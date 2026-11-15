---
ticker: SEI
name: Sei
chain: sei
contract: "native (denom usei)"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 4
  liquidity_market: 6
  product_development: 7
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  foundation_wallets_unpublished: tripped
  fees_under_100k_per_year: tripped
price_usd: 0.03923
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_height: 243333375
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SEI · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** An actively built, fast chain with almost no paid usage: about $1,600 of fees in 30 days. The Sei Foundation's 9% was unlocked at launch and its wallets aren't published, and team and investor unlocks are still running.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (1 ≤ 3).*

---


# 🪪 SEI · Sei · 4.0 / 10 · ❌ FAIL

> **One line:** An actively built, fast chain with almost no paid usage: about $1,600 of fees in 30 days. The Sei Foundation's 9% was unlocked at launch and its wallets aren't published, and team and investor unlocks are still running.

ℹ️ **Adapted for a layer-1.** "Revenue" = network fees. "Foundation" = Sei Foundation and Sei Labs. "Holdings / Selling" = official allocations, the on-chain mint schedule and any traceable foundation flows.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (Sei REST, block 243,333,375) |
|---|---|
| **Price** $0.03923 | **Supply on-chain** 9,246,702,265 SEI (10B planned) |
| **24h / 7d / 30d** 🔴 −9.7% / −14.1% / −36.7% | **Circulating (CoinGecko)** 6.73B (67.3% of 10B) |
| **Market cap** $264.4M · **FDV** $392.7M | **Bonded stake** 4,079,608,491 SEI (44.1% of on-chain supply) |
| **24h volume** $31.09M | **Validators** 40 bonded · Nakamoto coefficient **9** |
| **ATH** $1.14 (15 Mar 2024) · now **−96.6%** | **Mint** 453,297 SEI/day to stakers (165M in Aug 2026–Aug 2027) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $22 | [Tier A] DefiLlama `sei`, 14 Nov 2026 |
| 30-day fees | $1,640 | [Tier A] DefiLlama |
| 12-month fees | $61,511 | [Tier A] DefiLlama |
| All-time fees / revenue | $302,432 / $117,228 | [Tier A] DefiLlama |
| Community pool | 0.51 SEI | [Tier A] `distribution/community_pool` |

**What it means:** Effectively no fee income: ~$61k in a year on a $264M market cap. (DefiLlama may undercount some activity, but nothing primary shows a materially higher number.)

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Sei Foundation | Holds the 9% foundation allocation; funds ecosystem | [Tier A] Sei tokenomics blog |
| Sei Labs | Core developer; co-founder Jeff Feng publicly leads Giga push | [Tier B] TokenPost + Signalyze |
| Code | `sei-protocol/sei-chain` pushed 14 Nov 2026; v6.7.4 and v6.8.0-rc3 on 10 Nov 2026 | [Tier A] GitHub |
| Governance | On-chain SIPs (e.g. SIP-3 EVM-only, SIP-6 Autobahn approved Nov 2026) | [Tier A] blog.sei.io |
| Foundation directors / registry | Not checked this pass | [Unverified] |

**What it means:** Active builders and on-chain governance, but who sits on the foundation and what wallets it uses are not published.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Allocation (of 10B) | % | SEI | Vesting |
|---|---:|---:|---|
| Ecosystem Reserve | 48% | 4.8B | Linear over 120 months, ends 15 Aug 2033 |
| Team | 20% | 2.0B | 1-year cliff (from Aug 2023), then monthly |
| Private-sale investors | 20% | 2.0B | 1-year cliff, then monthly |
| Foundation Treasury | 9% | 900M | **Fully unlocked at launch** |
| Binance Launchpool | 3% | 300M | Unlocked at launch |

Source: [Tier A] Sei tokenomics blog · [Tier B] Blockworks disclosures + Tokenomics.com.

| Live check | Value | Source |
|---|---:|---|
| Supply minted so far | 9.247B | [Tier A] chain |
| Still to mint (staking-reward schedule, to Aug 2033) | ~753M (123.3M left this year + 630M later years) | [Tier A] `seichain/mint` params |
| Not circulating (10B − CoinGecko 6.73B) | ~3.27B (32.7%) | Calculated |
| Foundation / team wallet balances | **Not found** — addresses not published | Not found |

**What it means:** Team, investors and the foundation got 49% of supply, and another 48% sits in a foundation-steered ecosystem reserve. About a third of supply is still locked or unminted. The foundation's 900M has been free to move since launch.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **33 of 361 days** were pump days, including **11 in a row, 20–30 Sep 2026** (up to +39.8%).

| Check | Finding |
|---|---|
| Foundation → exchange on a pump day | **Not found — wallets not published, so not provable either way** |
| Team / investor monthly unlocks | Continue on a monthly schedule; recipients not traced |
| Disclosure of foundation sales | None found |

**What it means:** No direct evidence of insider selling into pumps, but there's no way to check it, and unlocks keep landing. Not proven → fail.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

- 10B planned supply; staking-reward mint continues to 2033 (165M this year, then 135M, 120M, 112.5M ×2, 75M ×2) [Tier A].
- Ongoing team/investor/ecosystem unlocks into a market cap of $264M.

## 💧 Liquidity & market · 6/10 · ✅ PASS

- $31.09M 24h volume across major CEXs (CoinGecko). Adequate, but the price is down 96.6% from its high.

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- Frequent releases (v6.7.4, v6.8.0-rc3 on 10 Nov 2026). Giga upgrade: parts live; SIP-6 Autobahn consensus approved Nov 2026 but still needs audits and a public testnet [Tier A blog.sei.io · Tier B TokenPost].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- ~$22/day of fees. No confirmed paying enterprise customer found in a primary source.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No SEI-specific hack in this series. 40 validators; 9 control over one-third of stake — a small set.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found; US ETF filings for SEI reported but not checked this pass. Not proven either way.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Monthly | Team / investor / ecosystem unlocks | Supply ↑ |
| TBD | Autobahn (SIP-6) audits → testnet → mainnet | Product |
| 15 Aug 2027 | Next staking-reward year (135M SEI) | Supply ↑ |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Foundation wallets unpublished | 🟡 Tripped |
| Fees under $100k per year | 🔴 Tripped ($61.5k) |

## 📚 Sources

- [Tier A] Sei REST (`rest.sei-apis.com`): bank supply, staking pool, community pool, validators, `seichain/mint` minter and params; 14 Nov 2026 ~12:27 PM MST
- [Tier A] DefiLlama fees `sei`, 14 Nov 2026
- [Tier A] CoinGecko `sei-network` price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] GitHub `sei-protocol/sei-chain` · [Sei tokenomics blog](https://blog.sei.io/seis-future-proofed-tokenomics-setting-the-scene-sei-is-an-open-source-permissionless-layer-1-blockchain-specifically-designed-in-response-to-the-fundamental-use-case-of-blockchains-the/) · [SIP-6 post](https://blog.sei.io/introducing-sip-6-upgrade-sei-to-autobahn-consensus/)
- [Tier B] Blockworks disclosures · Tokenomics.com · TokenPost
- [Unverified] Foundation directors; ETF filings; team/investor vesting end date

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
