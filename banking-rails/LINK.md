---
ticker: LINK
name: Chainlink
chain: ethereum
contract: "0x514910771AF9Ca656af840dff83E8264EcF986CA"
overall_score: 6.9
overall_verdict: PASS
section_scores:
  revenue: 8
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 10
  product_development: 9
  adoption_customers: 8
  security_audits: 8
  regulatory: 5
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none
  treasury_to_exchange_during_pump: not_found
  undisclosed_treasury_to_exchange_flow: recurring_quarterly
price_usd: 9.19
price_source: "CoinGecko, 14 Nov 2026 9:08 AM MST"
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### LINK · Overall grade **6.9 / 10 · ✅ PASS**

**Summary:** A real, fee-earning oracle network with clean token code, but its non-circulating treasury sends ~16–19M LINK to Binance every quarter without a formal announcement.

**Sections passed: 8 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 8/10 | ✅ PASS |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 10/10 | ✅ PASS |
| 🧑‍💻 Product & development | 9/10 | ✅ PASS |
| 🤝 Adoption & customers | 8/10 | ✅ PASS |
| 🛡️ Security & audits | 8/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 LINK · Chainlink · 6.9 / 10 · ✅ PASS

> **One line:** A real, fee-earning oracle network with clean token code, but its non-circulating treasury sends ~16–19M LINK to Binance every quarter without a formal announcement.

| 📊 Market (CoinGecko, 14 Nov 2026 9:08 AM MST) | 🔗 On-chain (Ethereum, 10 Oct / 3 Nov 2026) |
|---|---|
| **Price** $9.19 | **Token** `0x5149…86CA` "LinkToken" ERC-677, Solidity 0.4.16 |
| **24h / 7d / 30d** 🔴 −7.4% / −15.1% / −24.9% | **Supply** 1,000,000,000 fixed · no owner, mint, pause, blacklist, upgrade |
| **Market cap** $7.05B · **FDV** $9.19B | **Circulating (CoinGecko)** 766.85M → ~233.15M non-circulating |
| **24h volume** $246.3M | **Holders** ~1,007,408 (Blockscout, 10 Oct) |
| **ATH** $52.70 (9 May 2021) · now −83% | **Community staking pool** `0xBc10…B5e` 40,875,544 (4.09%) |

---

## 💰 Revenue — Does it make money? · 8/10 · ✅ PASS

| Metric | Value | Source |
|---|---:|---|
| 30-day fees | $5,516,481 | [Tier A] DefiLlama `chainlink-requests`, `chainlink-staking` (pulled 13 Nov 2026) |
| 30-day revenue | $5,340,836 | [Tier A] DefiLlama |
| All-time fees | $82,853,166 | [Tier A] DefiLlama |
| All-time revenue | $75,513,614 | [Tier A] DefiLlama |
| Chainlink Reserve buys | 431,900 LINK in 30 days, funded by service revenue | [Tier A] treasury pass |
| Reserve size | >6M LINK (28 Sep 2026) | [Unverified] news only; contract balance not read |

**What it means:** Yes, it makes money, and some of it is used to buy LINK. Annualised revenue is ~$65M on a $7B cap.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Sergey Nazarov | Co-founder; CEO of Chainlink Labs. Verified commits | [Tier A] GitHub `smartcontractkit` |
| Steve Ellis | Co-founder; CTO (commonly stated). Commits verified by name | [Tier A] commits · title [Unverified] |
| Chainlink Foundation | Entity, directors and jurisdiction **not checked** this pass | [Unverified] |
| Non-circulating Safes | Known on-chain ("Noncirculating Supply" Safe multisigs, e.g. #17 `0xa42d0a18…9a3`), **no official address list** | [Tier A] chain · labels Etherscan |

**What it means:** The builders are known and active. Who legally controls the treasury Safes is still an open question.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Bucket | LINK | % of supply | Notes |
|---|---:|---:|---|
| Non-circulating (1B − CoinGecko circulating) | ~233,150,030 | ~23.3% | Held in Safe multisigs; not vested on-chain |
| Community staking pool | 40,875,544 | 4.09% | User stake, not treasury |
| Quarterly release | ~19M per quarter | ~1.9% | Discretionary |

**What it means:** About a quarter of supply is in treasury Safes that can move at any time; there is no on-chain lock.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

| Window (UTC) | Route | Amount to Binance 14 | LINK 5-day change before send | Pump? |
|---|---|---:|---:|---|
| 9–10 Oct 2026 | Noncirculating Safes → `0x9b1c1752…cde9` (forwards in minutes) → Binance 14 `0x28c6c062…1d60` | 15,875,000 (+1,874,999 to Safe `0xd50f074e`) | −10.0% | ❌ No |
| 19 Jun 2026 (partial window) | same route | ≥10,000,000 | +0.3% | ❌ No |
| 3 Apr 2026 (partial window) | same route | ≥4,600,000 | +2.4% | ❌ No |

- Example tx: `0x2f03bf93b7c50c740a6a9ebdcb2182ae112ea3c14474559e189afa8aaed40836`.
- Pump test: 25 of 360 days in the last year had a ≥10% 5-day rise; **none** of the three sends fell in one.
- Reports said 16.875M in Oct; on-chain trace shows 15.875M to Binance + 1.875M to a Safe (17.75M total). Whether Binance sold it cannot be seen on-chain.

**What it means:** Not pump-timed, and the cadence is regular. But it is still undisclosed treasury-to-exchange flow, so it does not pass.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed 1B, ERC-677, not upgradeable, no tax. Matches white paper v2.0 (15 Apr 2021).
- No burn claimed. Unlock pressure ~19M/quarter (~2.5% of circulating per quarter).

## 💧 Liquidity & market · 10/10 · ✅ PASS

- $246.3M 24h volume; deep on every major CEX and DEX.

## 🧑‍💻 Product & development · 9/10 · ✅ PASS

- Live: Data Feeds, Data Streams, CCIP (GA 24 Apr 2024), Automation, VRF, Functions; Staking v0.2 (Nov 2023).
- GitHub `smartcontractkit`: 100 repos listed, **93 pushed in last 90 days**, last push 3 Nov 2026.

## 🤝 Adoption & customers · 8/10 · ✅ PASS

- Confirmed: Swift + UBS Asset Management pilot bridging tokenized assets to payment systems (Nov 2024).
- Partly: "Chainlink is Swift's contingency plan." Unverified: Chainlink + RedStone with Plume.

## 🛡️ Security & audits · 8/10 · ✅ PASS

- No LINK-token or Chainlink protocol hack on file (2025–2026). Remaining risk lives in oracle configs, CCIP lanes, staking and Reserve contracts.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No licence or enforcement record checked this pass. Not proven either way.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| ~Jan 2027 | Next quarterly treasury release window (based on Apr/Jun/Oct pattern) |
| Ongoing | Reserve buys from service revenue |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None |
| Treasury → exchange during a pump | 🟢 Not found (sends were off-pump) |
| Undisclosed treasury → exchange flow | 🟡 Recurring every quarter |

## 📚 Sources

- [Tier A] Ethereum RPC and Blockscout; `eth_getLogs` Transfer trace, Oct 2026
- [Tier A] [docs.chain.link](https://docs.chain.link) · [white paper v2](https://research.chain.link/whitepaper-v2.pdf)
- [Tier A] DefiLlama fees/revenue, pulled 13 Nov 2026 4:22 AM MST
- [Tier A] CoinGecko `chainlink` price and 365-day daily closes, 14 Nov 2026
- [Tier A] GitHub `smartcontractkit`
- [Tier B] [PR Newswire, CCIP GA](https://www.prnewswire.com/news-releases/chainlink-announces-general-availability-for-ccip-302126061.html)
- [Unverified] Reserve balance >6M LINK; Foundation entity and signers; Steve Ellis title

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
