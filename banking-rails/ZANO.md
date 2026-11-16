---
ticker: ZANO
name: Zano
chain: zano
contract: "native coin (no contract)"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 3
  product_development: 6
  adoption_customers: 3
  security_audits: 2
  regulatory: 4
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: Gateway Addresses inflation exploit (late Aug to 25 Sep 2026) minted illicit ZANO and fUSD; chain rolled back ~1 month to block 3,833,000 on 27 Sep 2026"
  mint_path_live: "PoW/PoS issuance of 1 ZANO per block; the minting exploit is closed and Gateway Addresses are disabled pending audit"
  team_wallet_to_exchange_during_pump: "not proven: privacy chain, so the 3.69M team premine cannot be traced"
  entity_concentration: "unknown (shielded balances)"
price_usd: 3.87
price_source: "CoinGecko, 16 Nov 2026 ~9:30 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZANO · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Zano is a hybrid proof-of-work/proof-of-stake privacy chain launched in 2019 that can issue confidential assets, including the fUSD stablecoin. In September 2026 an attacker used a bug in the new Gateway Addresses feature to mint ZANO and fUSD that shouldn't exist. The team rolled the chain back about a month to remove it. The chain earns almost nothing (fees are burned). Because the chain hides balances, the 3.69M team premine can't be traced. The revenue gate fails.

**🚨 Top warning:** a **one-month chain rollback in Sep 2026**. Starting around 29 August, an attacker abused a missing check in Gateway Addresses to mint ZANO and fUSD that shouldn't exist. On 27 September the core team shipped an emergency release that restarted the chain from block 3,833,000 (26 Aug 2026), erasing every transaction after that point. Users who received funds in that window lost them and are being reimbursed ([emergency release](https://github.com/hyle-team/zano/releases/tag/2.2.3.600), [Zano docs](https://docs.zano.org/docs/learn/pre-rollback-build/), [Bitcoin.com News](https://news.bitcoin.com/security/zano-wipes-1-month-of-history-to-fix-massive-crypto-inflation-bug/)). Gateway Addresses stay disabled until an independent audit is done. Every link is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 2/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZANO · Zano · 3.8 / 10 · ❌ FAIL

> **One line:** A working privacy chain whose team rolled back a month of history after an inflation exploit.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:30 AM MST) | 🔗 Chain (project docs) |
|---|---|
| **Price** $3.87 | **Supply** ~15.50M ZANO, +1 ZANO per block (~0.53M a year) |
| **24h / 7d / 30d** 🔴 −2.4% / 🟢 +2.5% / 🔴 −26.6% | **Consensus** hybrid PoW (ProgPowZ) / PoS (Zarcanum), 50/50 |
| **Market cap** $60.0M · **FDV** $60.0M (no cap) | **Team premine** 3.69M at launch (2019), "most of it" spent |
| **24h volume** $0.78M (MEXC $0.59M, Ourbit, Biconomy, Nonkyc, XT) | **Fees** 0.01 ZANO, burned |
| **ATH** $17.81 (7 Jan 2025) · now −78.3% | |
| **Pump days** 39 in the last year (MEXC ZANOUSDT; largest +66.2% on 21 Mar 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- No treasury income. Fees of 0.01 ZANO are burned, which at roughly 1,200 transactions a day comes to under $50 a day [Unverified: transaction count from one aggregator]. **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- A full-time core team (hyle-team) ships regular releases ([GitHub](https://github.com/hyle-team/zano/releases)). It responded to the exploit within two days and publishes monthly updates ([blog](https://blog.zano.org/zano-monthly-project-update-24-september-october-2026/)). Its funding comes from a premine the project says is mostly spent ([guide](https://intro.zano.org/zano-introduction-guidebook.pdf)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- At the 2019 launch, 3.69M ZANO were reserved for the team, about 21% of the starting supply ([blog](https://blog.zano.org/a-week-into-mainnet/)). The project says most of it is now spent ([guide](https://intro.zano.org/zano-introduction-guidebook.pdf)). It's unclear where it went or what's left.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Zano hides amounts and owners, so the premine can't be followed to exchanges. With 39 pump days in the year, this can't be checked → **not proven, 4.**

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed reward of 1 ZANO per block, so inflation is about 3.4% a year and falling. Burned fees offset a small part. No cap.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.78M a day, three-quarters of it on MEXC. No tier-1 exchange lists ZANO. A THORChain route is planned.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Real privacy tech: Zarcanum hidden-stake proof of stake, confidential assets, the fUSD stablecoin, aliases, and mobile and lite wallets.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- About 1,200 transactions a day [Unverified]. fUSD paused activity after counterfeit issuance in the exploit ([Bitcoin.com News](https://news.bitcoin.com/security/zano-wipes-1-month-of-history-to-fix-massive-crypto-inflation-bug/)).

## 🛡️ Security & audits · 2/10 · ❌ FAIL

- An inflation exploit in Sep 2026 was fixed by a one-month rollback ([release](https://github.com/hyle-team/zano/releases/tag/2.2.3.600), [docs](https://docs.zano.org/docs/learn/pre-rollback-build/)). That shows the core team can, and did, rewrite the chain. There's one client, and Gateway Addresses are disabled until an audit. **2.**

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- A privacy coin, so delisting risk is high. Nothing was sold to the public, but 553,500 premine ZANO repaid a 2018 development loan [Unverified: one source].

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- Gateway Addresses audit and re-enable, an HF8 fork, and a THORChain route ([update](https://blog.zano.org/zano-monthly-project-update-24-september-october-2026/)).

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Inflation exploit, then a 1-month rollback (Sep 2026) |
| Team wallet → exchange during a pump | ⚪ Not proven (shielded chain) |
| Live mint path | 🟡 Block rewards only; the exploit path is disabled pending audit |
| Entity concentration | ⚪ Unknown |

## 📚 Sources

- [Tier A] [Emergency release v2.2.3.600](https://github.com/hyle-team/zano/releases/tag/2.2.3.600), [Pre-rollback docs](https://docs.zano.org/docs/learn/pre-rollback-build/), [Monthly update #24](https://blog.zano.org/zano-monthly-project-update-24-september-october-2026/)
- [Tier A] [Mainnet week one (premine 3.69M)](https://blog.zano.org/a-week-into-mainnet/), [Introduction guide](https://intro.zano.org/zano-introduction-guidebook.pdf)
- [Tier B] [Bitcoin.com News, rollback](https://news.bitcoin.com/security/zano-wipes-1-month-of-history-to-fix-massive-crypto-inflation-bug/), [Bitcoin.com News, network stable](https://news.bitcoin.com/crypto-news/zano-network-stabilizes-after-30-day-blockchain-rewind/)
- [Tier A] CoinGecko `zano` (market, venues); pump days from MEXC ZANOUSDT daily closes
- Arkham doesn't cover Zano (shielded chain)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Rollback to block 3,833,000 | [release](https://github.com/hyle-team/zano/releases/tag/2.2.3.600), [docs](https://docs.zano.org/docs/learn/pre-rollback-build/) | A+A | 16 Nov 2026 |
| 3.69M team premine | [blog](https://blog.zano.org/a-week-into-mainnet/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Premine balance today** | Ask the team for a signed view-key disclosure or audit | Free |
| 2 | **Independent Gateway Addresses audit** | Watch for its publication | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
