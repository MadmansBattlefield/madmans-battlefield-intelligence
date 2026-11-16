---
ticker: RVN
name: Ravencoin
chain: ravencoin
contract: "native coin (no contract)"
overall_score: 4.4
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 9
  selling_behavior: 7
  tokenomics_supply: 8
  liquidity_market: 4
  product_development: 3
  adoption_customers: 2
  security_audits: 4
  regulatory: 7
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "May-Jul 2020 asset-reissue bug let attackers mint 301.8M RVN (~1.5% of cap), sold to exchanges; fixed at block 1,304,352 on 4 Jul 2020; coins never burned"
  mint_path_live: "no beyond the fixed PoW schedule: 1,250 RVN a block since 15 Jan 2026, 21B cap"
  team_wallet_to_exchange_during_pump: "not applicable: fair launch 3 Jan 2018, no premine, ICO or team allocation"
  entity_concentration: "none (no team or treasury wallets)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Asset-creation fees are burned automatically on-chain, but the amount is negligible and transaction fees go to miners; Revenue stays 1."
pump_day_price_source: "not applicable (no insider wallets)"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.001076
price_source: "CoinGecko, 16 Nov 2026 ~9:15 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### RVN · Overall grade **4.4 / 10 · ❌ FAIL**

**Summary:** Ravencoin is a 2018 fair-launch proof-of-work fork of Bitcoin for issuing assets on-chain. With no premine, ICO or team allocation, there are no insider wallets that could sell, and supply follows a fixed halving schedule. That's why holdings, selling and tokenomics pass. But the chain earns nothing: there is no protocol revenue, and asset fees are burned rather than paid to anyone. Development and usage are thin, and the market cap is only $17.8M. The revenue gate fails.

**🚨 Top warning:** security depends on a small, cheap mining budget. Since the 15 Jan 2026 halving, miners earn about 1.8M RVN a day, roughly **$1.9k a day** at today's price. Little money secures the chain, which makes a majority-hashrate attack cheaper. In May–Jul 2020 a bug in a community code contribution let attackers mint **301.8M RVN** (~1.5% of the cap), which they sold on exchanges. The developers left those coins in circulation. Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 9/10 | ✅ PASS |
| 📉 Selling behavior | 7/10 | ✅ PASS |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 RVN · Ravencoin · 4.4 / 10 · ❌ FAIL

> **One line:** Clean fair launch with no insiders, but no revenue, little use and a thin security budget.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:15 AM MST) | 🔗 Chain (protocol rules) |
|---|---|
| **Price** $0.001076 | **Supply** 16,569,014,325 RVN (78.9% of 21B cap) |
| **24h / 7d / 30d** ⚪ −1.1% / 🔴 −15.5% / 🔴 −26.3% | **Block reward** 1,250 RVN (since 15 Jan 2026) |
| **Market cap** $17.8M · **FDV** $17.8M | **New supply** ~1.8M RVN/day (~$1.9k) |
| **24h volume** $1.09M (Binance $0.26M, CoinW $0.12M, Bybit $0.10M, WhiteBIT $0.09M, OKX $0.07M) | **Team / treasury** none (fair launch 3 Jan 2018) |
| **ATH** $0.2852 (20 Feb 2021) · now −99.6% | |
| **Pump days** 13 in the last year (largest +22.9% on 23 Aug 2026) | |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

- Proof-of-work with no protocol treasury. Asset-creation fees are burned, and transaction fees go to miners. Nothing accrues to holders. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Asset-creation fees are burned automatically on-chain, but the amount is negligible and transaction fees go to miners; Revenue stays 1.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- Volunteer open-source developers with no company. Development funding is ad hoc.

## 🪙 Foundation / team holdings — How many coins do they hold? · 9/10 · ✅ PASS

- No premine, ICO or team allocation. Every coin was mined.

## 📉 Selling behavior — Do insiders sell into pumps? · 7/10 · ✅ PASS

- With no team, foundation or treasury wallets, the insider pump-day test doesn't apply. This follows the BCH, XMR and ETC reports. Ongoing sell pressure is normal miner selling (~1.8M RVN/day).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from not applicable (no insider wallets).

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

- Fixed 21B cap with halvings every 2.1M blocks (~4 years). The second halving was 15 Jan 2026 at block 4,200,000 (Tier B, two sources).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.09M of 24h volume. CoinGecko also lists a larger CoinUp.io figure that exceeds the coin's own total, so I treated it as unreliable. Down 99.6% from ATH.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- The asset layer, messaging and restricted assets have been live for years, with little new development.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No meaningful asset issuance volume or paying users found.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- A $1.9k/day mining budget makes the chain cheap to attack. In 2020 a validation bug allowed 301.8M RVN to be minted outside the coinbase ([developer post](https://blog.ravencoin.email/post/ravencoin-emergency-update), [CoinDesk](https://www.coindesk.com/markets/2020/07/03/bad-ravencoin-code-allows-attackers-to-generate-coins-without-mining), [fix PR](https://github.com/RavenProject/Ravencoin/pull/794)). Ravencoin shares the KAWPOW mining algorithm with other small PoW coins, so hashrate for an attack can be rented.

## ⚖️ Regulatory · 7/10 · ✅ PASS

- With no issuer and no sale, the fair launch makes it hard to frame as a security. No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- The next halving is about 2030. No funded roadmap.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟠 2020 inflation exploit, 301.8M RVN (fixed), outside the 1-year window |
| Team wallet → exchange during a pump | 🟢 Not applicable (no team wallets) |
| Live mint path | 🟢 Fixed PoW schedule only |
| Entity concentration | 🟢 None |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| No team, foundation or treasury wallets | — | — | high | n/a | None |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] CoinGecko `ravencoin` (market, venues); pump days from Binance RVNUSDT daily closes
- [Tier B] [CoinDesk week-ahead, 8 Jan 2026](https://www.coindesk.com/markets/2026/01/08/u-s-inflation-report-bnb-smart-chain-s-hard-fork-crypto-week-ahead) and [NiceHash countdown](https://www.nicehash.com/countdown/rvn-halving-2026-01-11-12-00) (halving at block 4,200,000, 2,500 → 1,250)
- [Tier A] [Ravencoin emergency update, 30 Jun 2020](https://blog.ravencoin.email/post/ravencoin-emergency-update), [fix PR #794](https://github.com/RavenProject/Ravencoin/pull/794); [Tier B] [CoinDesk, 3 Jul 2020](https://www.coindesk.com/markets/2020/07/03/bad-ravencoin-code-allows-attackers-to-generate-coins-without-mining), [explorer team write-up](https://medium.com/@cryproscope/the-anatomy-of-ravencoin-exploit-finding-8fa4fe7547a9) (301,804,400 RVN)
- [Tier A] [ravencoin.org](https://ravencoin.org/)
- Arkham was not run for this report (no team wallets to check)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Halving to 1,250 RVN at block 4,200,000 | [CoinDesk](https://www.coindesk.com/markets/2026/01/08/u-s-inflation-report-bnb-smart-chain-s-hard-fork-crypto-week-ahead), [NiceHash](https://www.nicehash.com/countdown/rvn-halving-2026-01-11-12-00) | B+B | 16 Nov 2026 |
| 2020 exploit, 301.8M RVN | [developer post](https://blog.ravencoin.email/post/ravencoin-emergency-update), [write-up](https://medium.com/@cryproscope/the-anatomy-of-ravencoin-exploit-finding-8fa4fe7547a9) | A+B | 16 Nov 2026 |
| Supply, price, venues | [CoinGecko](https://www.coingecko.com/en/coins/ravencoin) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Current network hashrate and cost to rent 51%** | Read a public hashrate-rental cost page for KAWPOW | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
