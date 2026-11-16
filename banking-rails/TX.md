---
ticker: TX
name: TX (Coreum + Sologenic)
chain: coreum
contract: "native ucore denom on coreum-mainnet-1"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 2
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 5
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes; inflation targets ~24% staking APY while PSE is paused, and PSE resumes Dec 2027"
  team_wallet_to_exchange_during_pump: "not proven: foundation recipient accounts hold less than they likely received, but public nodes return no outgoing transfers to trace"
  one_hop_sale_status: none_found
  entity_concentration: "PSE clearing accounts still hold 90.5B of 102.2B supply (89%); 54.3B of it is earmarked for the foundation, founding partners, partnerships, investors and team"
price_usd: 0.00126666
price_source: "CoinGecko, 16 Nov 2026 ~12:30 PM MST"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "standard Cosmos fee distribution pays gas fees to stakers automatically; tiny next to inflation and PSE emissions, so it rounds to zero"
pump_day_price_source: "Gate TX_USDT daily closes (UTC), series from 12 Mar 2026; Binance unavailable (451), Gate is next in the hierarchy"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "core1u692m7ddssgffpfwx33g3s95ahqnsw29nstncn"
    label: "pse_foundation module (clearing) account"
    confidence: high
    independent_corroboration: true
    basis: "named module account on-chain; PSE allocation in the official docs"
  - address: "core142498n8sya3k3s5jftp7dujuqfw3ag4tpzc2ve45ykpwx6zmng8skcw5nw"
    label: "PSE Foundation recipient (x/group policy account)"
    confidence: high
    independent_corroboration: true
    basis: "listed under pse_foundation in the on-chain PSE params"
  - address: "core12xyww2vucfufyzknvyameh5v25cn6gxzzagwgpzhwdq8v35zdmgqd6t6c7"
    label: "PSE Team recipient"
    confidence: high
    independent_corroboration: true
    basis: "listed under pse_team in the on-chain PSE params"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TX · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** TX is the merged Coreum and Sologenic chain, relaunched on 6 Mar 2026. Gas fees reach stakers automatically, but they are tiny next to the inflation and Proof-of-Support emissions (PSE) that make up the yield. 89% of supply still sits in PSE module accounts, and 53% is earmarked for the foundation, founding partners, investors and team. PSE is paused until Dec 2027 while inflation targets ~24% APY. Foundation recipient accounts appear to have moved out ~1.5B TX, but no outgoing transfers can be traced, so Selling is not proven. The revenue gate fails.

**🚨 Top warning:** **a huge insider-earmarked emission overhang plus high inflation.** On-chain PSE params show **54.3B TX (53% of supply)** still to be released to the foundation, founding partners, partnerships, investors and team ([PSE balances](https://coreum-rest.publicnode.com/tx/pse/v1/clearing_account_balances), [mappings](https://coreum-rest.publicnode.com/tx/pse/v1/params)). Market cap is $14.8M against an FDV of $129M. PSE is paused until 6 Dec 2027, but inflation meanwhile targets ~24% staking APY ([proposal 46](https://explorer.tx.org/tx/proposals/46)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TX · TX (Coreum + Sologenic) · 3.5 / 10 · ❌ FAIL

> **One line:** A merged Cosmos L1 with tiny fee revenue, inflation-funded yield and a 53% insider emission overhang.

| 📊 Market (CoinGecko, 16 Nov 2026 ~12:30 PM MST) | 🔗 Chain (TX LCD) |
|---|---|
| **Price** $0.00127 | **Supply** 102.18B on-chain; 11.71B circulating per CoinGecko |
| **24h / 7d / 30d** 🟢 +0.5% / 🔴 −9.6% / 🔴 −32.5% | **PSE clearing accounts** 90.5B (89%) |
| **Market cap** $14.83M · **FDV** $129.1M | **Bonded** 5.23B TX |
| **24h volume** ~$66.7k (WEEX $17.8k, Ourbit $16.6k, Biconomy $13.5k, Kraken USD $8.1k, Gate $7.0k) | **Foundation recipients** 1.32B across 10 accounts |
| **ATH** $0.0378 (6 Mar 2026) · now −96.7% | |
| **Pump days** 46 since Mar 2026 (Gate TX_USDT; largest +42.5% on 9 Jun 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Gas fees go to the fee collector and are paid to stakers automatically by the standard Cosmos distribution module. But fees are tiny: staking yield comes from inflation and PSE emissions, not usage.

**What it means:** fee revenue reaches holders: about zero, because it rounds to zero next to issuance. **Holder test: yes, but tiny.** **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- Run by the TX foundation after the Coreum–Sologenic merger, with on-chain governance ([proposal 29](https://explorer.tx.org/tx/proposals/29), [proposal 46](https://explorer.tx.org/tx/proposals/46)). Leaders are described by role only.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- PSE minted 100B TX at the 6 Mar 2026 TGE into module clearing accounts, released monthly over 84 months: stakers 40%, foundation 30%, founding partners 20%, investors 5%, partnerships 3%, team 2% [Tier A, TX docs].
- **Still unreleased** ([LCD](https://coreum-rest.publicnode.com/tx/pse/v1/clearing_account_balances)): foundation 27.1B, founding partners 18.1B, investors 4.5B, partnerships 2.7B, team 1.8B, for **54.3B (53%)** earmarked for insiders.
- **Attribution confidence:** high. Module names and recipient accounts are set in the on-chain [PSE params](https://coreum-rest.publicnode.com/tx/pse/v1/params), and the official docs describe the same split. Score 3.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Eight monthly PSE distributions (Apr–Nov 2026) have paid ~2.86B TX to 10 foundation recipient accounts (x/group policy accounts). They now hold **1.32B**, e.g. [`core142498n8…`](https://coreum-rest.publicnode.com/cosmos/bank/v1beta1/balances/core142498n8sya3k3s5jftp7dujuqfw3ag4tpzc2ve45ykpwx6zmng8skcw5nw) holds 220.7M.
- If the payouts were split equally (they look round), ~1.5B TX left foundation accounts and ~0.43B left two founding-partner accounts [Unverified]. Investor, team and partnership recipients appear untouched.
- Public LCD nodes return only governance votes from these accounts, with no outgoing transfers, so destinations and dates can't be traced, nor whether any landed on pump days.
- **Attribution confidence:** high for the senders, but there are no traced destinations: **not proven → 4.** **Disclosure quality:** not applicable.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- 102.2B on-chain against 11.7B circulating. PSE is paused after the 6 Nov 2026 payout and resumes 6 Dec 2027; meanwhile inflation targets ~24% staking APY ([proposal 46](https://explorer.tx.org/tx/proposals/46)). 6.04% was reserved for Tier 1 exchange listings [Tier B].

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $67k a day, spread over small venues; Kraken USD $8k.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- A live L1 with smart tokens, a DEX and a Sologenic tokenisation stack.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Low on-chain usage relative to the issuance.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- PSE pause and the Dec 2027 restart; exchange listing reserve.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven: outflows exist but can't be traced |
| Live mint path | 🔴 Inflation (~24% staking APY target) and PSE |
| Entity concentration | 🔴 PSE modules 89%; 53% insider-earmarked |

## 📚 Sources

- [Tier A] TX LCD: [PSE params](https://coreum-rest.publicnode.com/tx/pse/v1/params), [clearing balances](https://coreum-rest.publicnode.com/tx/pse/v1/clearing_account_balances), [supply](https://coreum-rest.publicnode.com/cosmos/bank/v1beta1/supply/by_denom?denom=ucore)
- [Tier A] [Proposal 29](https://explorer.tx.org/tx/proposals/29), [Proposal 46](https://explorer.tx.org/tx/proposals/46); TX docs PSE guide; TX ecosystem Medium posts
- [Tier A] CoinGecko `coreum` (market, venues); pump days from Gate TX_USDT daily closes (UTC), per the price-source hierarchy

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 54.3B insider-earmarked PSE still unreleased | [clearing balances](https://coreum-rest.publicnode.com/tx/pse/v1/clearing_account_balances) | A | 16 Nov 2026 |
| Recipient accounts per PSE bucket | [PSE params](https://coreum-rest.publicnode.com/tx/pse/v1/params) | A | 16 Nov 2026 |
| PSE paused to Dec 2027; ~24% APY inflation target | [proposal 46](https://explorer.tx.org/tx/proposals/46) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Where ~1.5B TX left the foundation recipient accounts** | An archive node or indexer with full tx history for the 10 group accounts | Free if an archive explorer is reachable; Arkham coverage of TX unknown |
| 2 | **Were payouts split equally?** | Read the PSE distribution events at each monthly payout height | Archive node |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
