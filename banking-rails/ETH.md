---
ticker: ETH
name: Ethereum
chain: ethereum
contract: "native (WETH 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2 is the wrapper)"
overall_score: 7.2
overall_verdict: PASS
section_scores:
  revenue: 5
  foundation_team: 7
  insider_holdings: 8
  selling_behavior: 7
  tokenomics_supply: 6
  liquidity_market: 10
  product_development: 9
  adoption_customers: 9
  security_audits: 8
  regulatory: 7
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none
  foundation_sale_on_pump_day: not_found
  undisclosed_foundation_to_exchange_flow: not_found
price_usd: 1831.06
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ETH · Overall grade **7.2 / 10 · ✅ PASS**

**Summary:** The busiest smart-contract chain, with a foundation that sells ETH under a published policy and has not sold on a pump day, but fees have shrunk to ~$175M a year and the burn no longer offsets new issuance.

**Sections passed: 10 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 8/10 | ✅ PASS |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 10/10 | ✅ PASS |
| 🧑‍💻 Product & development | 9/10 | ✅ PASS |
| 🤝 Adoption & customers | 9/10 | ✅ PASS |
| 🛡️ Security & audits | 8/10 | ✅ PASS |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ETH · Ethereum · 7.2 / 10 · ✅ PASS

> **One line:** The busiest smart-contract chain, with a foundation that sells ETH under a published policy and has not sold on a pump day, but fees have shrunk to ~$175M a year and the burn no longer offsets new issuance.

ℹ️ **Adapted for a layer-1.** "Revenue" = fees users pay and the part burned for all holders (EIP-1559). "Foundation" = the Ethereum Foundation (EF). "Holdings / Selling" = EF treasury wallets and EF sales checked against pump days.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (Ethereum / Blockscout, 14 Nov 2026) |
|---|---|
| **Price** $1,831.06 | **Asset** native ETH (no cap) |
| **24h / 7d / 30d** 🔴 −6.0% / −18.1% / −25.1% | **Supply** 122,218,624 ETH |
| **Market cap** $223.90B | **Blocks** 26,415,203 · **txs** 3.86B lifetime, ~2.10M today |
| **24h volume** $13.79B | **Gas** slow 0.31 / avg 1.05 / fast 2.12 gwei |
| **ATH** $4,946.05 (24 Aug 2025) · now −63% | **EF Safe** `0x9fC3…213e` 20,176.05 ETH · **EF wallet** `0xde0B…7BAe` 4,774.55 ETH |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $395,140 | [Tier A] DefiLlama `ethereum`, 14 Nov 2026 |
| 30-day fees | $19,845,088 | [Tier A] DefiLlama |
| 12-month fees | $174,667,664 | [Tier A] DefiLlama |
| All-time fees | $20,607,823,745 | [Tier A] DefiLlama |
| 30-day revenue (= ETH burned, value to all holders) | $6,206,492 | [Tier A] DefiLlama (holders revenue = revenue) |
| 12-month burn | $47,624,394 | [Tier A] DefiLlama |
| Who captures the rest | Priority fees + MEV → validators / stakers | [Tier A] protocol |

**What it means:** Ethereum makes real money and burns part of it for every holder. But $175M of fees a year on a $224B asset is thin (~0.08%), and the burn (~$48M/yr) is far below what is issued to stakers, so supply is growing again.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Ethereum Foundation | Swiss non-profit (Stiftung). Funds research, client teams and grants; does **not** control the protocol | [Tier A] ethereum.foundation |
| Treasury policy | Published 4 Jun 2025: opex target **15%** of treasury per year, **2.5-year** fiat buffer; ETH sales recalculated quarterly; quarterly reports to the Board | [Tier A] [EF Treasury Policy](https://blog.ethereum.org/2025/06/04/ef-treasury-policy) |
| Clients | Multiple independent teams (e.g. go-ethereum last release v1.17.10, 23 Oct 2026; consensus-specs v1.7.0-beta.4, 8 Oct 2026) | [Tier A] GitHub |
| Change process | EIPs + All Core Devs calls; no on-chain vote, no admin key | [Tier A] |
| Current EF leadership names | Not re-checked this pass | [Unverified] |

**What it means:** A known, regulated foundation with a written treasury rule, but it cannot change the chain on its own.

## 🪙 Foundation / team holdings — How many coins do they hold? · 8/10 · ✅ PASS

| Wallet / bucket | ETH | % of supply | Source |
|---|---:|---:|---|
| EF Safe `0x9fC3dc011b461664c835F2527fffb1169b3C213e` | 20,176.05 (+ DeFi positions) | 0.017% | [Tier A] Blockscout, 14 Nov 2026 |
| EF wallet `0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe` | 4,774.55 | 0.004% | [Tier A] Blockscout |
| Safe `0xbC9a9Ac7Dc36b1706732374bF632eF39FB6EfbC3` (receives 1,000 ETH lots + DAI from EF) | 2,222.21 | — | [Tier A] chain · EF control [Unverified] |
| EF total (Arkham estimate) | ~92,500 liquid + ~53,000 staked | ~0.12% | [Unverified] one Tier B outlet (Cointelegraph citing Arkham) |
| EF unstaked 17,035 ETH (late Apr 2026) | — | — | [Unverified] one Tier B outlet |

- The `0x9fC3…` Safe sold exactly 5,000 WETH via CoW Protocol on 8–10 Apr 2026, matching EF's announced "5,000 ETH in early April" sale — that ties the Safe to EF.
- No team vesting or ICO unlocks remain (genesis sale was 2014).

**What it means:** The foundation holds roughly a tenth of a percent of supply. Even a full sell-off would be small next to daily volume.

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **20 of 361 days** were pump days. Last one 23 Sep 2026 (+12.5%).

| Date (UTC) | EF sale | Route | 5-day move | Pump? | Source |
|---|---|---|---:|---|---|
| Mar 2026 (exact day not traced) | 5,000 ETH OTC to BitMine at ~$2,043 | OTC | — (price level matches non-pump days) | ❌ likely no | [Tier B] Cointelegraph |
| 8 Apr 2026 13:49–21:49 | 9 × 416.667 WETH = 3,750 | EF Safe → CoW `0x9008…ab41` (e.g. tx `0x7d6d0141…45ea`) | +8.9% | ❌ No | [Tier A] Blockscout |
| 10 Apr 2026 18:12–22:42 | 4 × 312.5 WETH = 1,250 | EF Safe → CoW (e.g. tx `0x81896da1…18f1`) | +6.1% | ❌ No | [Tier A] |
| 24 Apr 2026 | 10,000 ETH OTC to BitMine at $2,387 | OTC, announced by EF | −0.9% | ❌ No | [Tier B] Decrypt + Cointelegraph |
| 1 May 2026 | 10,000 ETH OTC to BitMine at $2,292 | OTC, announced by EF on X | −2.7% | ❌ No | [Tier B] Cointelegraph quoting EF's X post |
| 26 Oct 2026 | 2,785 ETH | CoW → USDS | −4.9% | ❌ No | [Tier B] Crypto Briefing + Crypto-Economy |
| 10–13 Nov 2026 | ~4,000 ETH in 1,000-ETH lots | CoW → USDS | −12.0% / −8.3% | ❌ No | [Tier B] Crypto Briefing + Crypto-Economy |

- 18 Mar 2026 (a pump day, +12.0%): the EF Safe moved 3,400 WETH to a Morpho adapter — a lending deposit, **not a sale** ([Tier A] txs `0xbe73b6cf…`, `0x0fa49432…`, `0x3295400a…`).
- 2026 sales total about 20,000+ ETH (~$45M) per reports [Tier B].

**What it means:** EF sells steadily under a published rule and announces OTC deals. None of the sales found fell on a pump day. It loses points because some Oct–Nov sales came from a wallet EF has not formally listed.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Supply | 122,218,624 ETH, no hard cap | [Tier A] CoinGecko / chain |
| Issuance | To validators, scales with total stake | [Tier A] protocol |
| Burn | EIP-1559 base fee burned ($47.6M in 12 months) | [Tier A] DefiLlama |
| Net | Issuance > burn → mildly inflationary | Calculated (exact annual rate not read this pass) |
| Admin / mint key | None | [Tier A] |

## 💧 Liquidity & market · 10/10 · ✅ PASS

- $13.79B 24h volume; on every exchange; US spot ETFs. ETF net outflows of ~$696M in Nov 2026 reported (SoSoValue via Crypto-Economy) [Unverified].

## 🧑‍💻 Product & development · 9/10 · ✅ PASS

- Multiple clients shipping (go-ethereum v1.17.10 on 23 Oct 2026; consensus-specs pushed 13 Nov 2026) [Tier A GitHub].
- Regular hard forks (Pectra May 2025, Fusaka Dec 2025) — EF blog not re-opened this pass [Unverified dates].

## 🤝 Adoption & customers · 9/10 · ✅ PASS

- ~2.1M transactions today on L1 alone (Blockscout). Hosts most tokenized funds and stablecoins; ETH-treasury companies (e.g. BitMine, ~5M ETH reported) [Tier B].

## 🛡️ Security & audits · 8/10 · ✅ PASS

- No protocol-level hack; client diversity reduces single-bug risk. App, bridge and liquid-staking hacks hit tokens built on Ethereum, not ETH itself.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- US spot ETH ETFs trading (SEC-approved 2024) [Tier A]. EF is a Swiss foundation. No enforcement against ETH as an asset found.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| Quarterly | EF recalculates ETH sales under its policy | Possible sell flow (disclosed) |
| 8–9 Dec 2026 | FOMC | Macro |
| 2026–27 | Next hard fork (Glamsterdam) — date not confirmed | Product news [Unverified] |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| EF sale on a pump day | 🟢 Not found |
| Undisclosed EF → exchange flow | 🟢 Not found (sales go via CoW / OTC and are reported) |

## 📚 Sources

- [Tier A] Blockscout API (EF wallets, internal and token transfers, 15 Nov 2025 – 14 Nov 2026)
- [Tier A] DefiLlama fees `ethereum`, 14 Nov 2026
- [Tier A] CoinGecko `ethereum` price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] [EF Treasury Policy](https://blog.ethereum.org/2025/06/04/ef-treasury-policy) · GitHub `ethereum/*`
- [Tier B] [Cointelegraph, 2 May 2026](https://cointelegraph.com/news/ethereum-foundation-sells-another-10000-eth-to-bitmine-in-third-otc-deal) · Decrypt · Crypto Briefing · Crypto-Economy
- [Unverified] Arkham EF totals; 17,035 ETH unstake; EF leadership names; ETF outflow figure

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
