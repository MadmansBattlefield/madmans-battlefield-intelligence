---
ticker: WAN
name: Wanchain
chain: wanchain
contract: "native coin (Wanchain mainnet)"
overall_score: 4.7
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 6
  insider_holdings: 5
  selling_behavior: 4
  tokenomics_supply: 7
  liquidity_market: 3
  product_development: 6
  adoption_customers: 3
  security_audits: 3
  regulatory: 5
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: "yes: Wanchain's Cardano bridge contract was drained of ~515.2M NIGHT (~$500K) on 20 Jul 2026 through a message-encoding flaw"
  mint_path_live: "PoS issuance of ~1.04M WAN a year, offset by bridge-fee burns (~1.1M WAN a year projected)"
  team_wallet_to_exchange_during_pump: "not proven: native Wanchain explorer has no public API and the foundation wallets are not published"
  entity_concentration: "Community Treasury ~5.7M WAN (2.9% of supply); foundation balance not published"
price_usd: 0.04677
price_source: "CoinGecko, 16 Nov 2026 ~9:40 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### WAN · Overall grade **4.7 / 10 · ❌ FAIL**

**Summary:** Wanchain is a 2017-era interoperability chain whose bridges collect real fees. Each fee is converted to WAN and split: 20% is burned, 20% goes to a community treasury, and the rest goes to operations, nodes and stakers. Since October 2026 the project projects that burns will slightly exceed new issuance. But the fees are small next to even a $9M market cap, trading is thin, and in July 2026 the project's Cardano bridge was drained. The revenue gate passes. The coin fails overall.

**🚨 Top warning:** a **bridge exploit in July 2026**. An attacker reused a valid bridge signature with shifted number boundaries to withdraw about **515.2M NIGHT (~$500K)** from the Wanchain bridge contract on Cardano. The flaw had passed two external audits ([post-mortem](https://medium.com/@wanchain_org/cardano-bnb-chain-bridge-incident-post-mortem-353e465276e7), [BlockSec](https://blocksec.com/blog/web3-security-allbridge-wanchain-exploits)). Bridging is Wanchain's whole product. Every link is in the 🔗 Evidence trail below.

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 3/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 WAN · Wanchain · 4.7 / 10 · ❌ FAIL

> **One line:** Real bridge fees with burn and treasury, but tiny scale, thin liquidity and a 2026 bridge exploit.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:40 AM MST) | 🔗 Chain (project posts) |
|---|---|
| **Price** $0.04677 | **Supply** 199.35M circulating of 210M max |
| **24h / 7d / 30d** ⚪ −0.2% / 🔴 −4.9% / 🔴 −17.4% | **Fee split** 20% burn · 20% treasury · 30% operations · 30% nodes and stakers |
| **Market cap** $9.32M · **FDV** $9.82M | **Community Treasury** ~5.7M WAN (~$0.27M) |
| **24h volume** $0.50M (KuCoin USDT $0.28M, KuCoin BTC $0.21M, HTX) | **Net issuance** ≈ −64k WAN a year projected (burns minus PoS) |
| **ATH** $9.84 (3 May 2018) · now −99.5% | |
| **Pump days** 3 in the last year (KuCoin WAN-USDT; largest +12.3% on 26–27 Nov 2025) | |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

- Bridge fees are converted to WAN. At current volume, the 20% burn share is projected at ~1.1M WAN a year ([proposal](https://medium.com/wanchain-foundation/governance-proposal-1-increase-the-wan-burn-rate-4669ffc73488), [update](https://wanchain.substack.com/p/wanchain-governance-goes-live-and)). That implies total fees of roughly 5.5M WAN (~$0.26M) a year [derived]. The income is real and goes to holders through burns and staking, but it is small. **5.**

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- A long-running team that ships continuously. On-chain governance went live on 15 Sep 2026, and its first proposal passed ([update](https://wanchain.substack.com/p/wanchain-governance-goes-live-and)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

- Community Treasury of ~5.7M WAN (~$0.27M) [Tier B, project-adjacent sources]. The foundation's own WAN balance isn't published.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Wanchain's native explorer has no public API, and the foundation wallets aren't published, so the insider pump-day test can't be run. There were only 3 pump days in the year → **not proven, 4.**

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- 95% of the 210M max is circulating, and burns are projected to slightly exceed staking issuance since 2 Oct 2026 ([Wanchain Academy](https://wanchainacademy.com/quema-anual-de-wan-supero-el-millon-propuesta-wcp-002-activa-y-token2049/)).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.50M a day, almost all on KuCoin. A governance proposal to deepen WAN/ETH liquidity on Uniswap was still being sponsored on 30 Oct.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Bridges and XFlows cross-chain swaps across many chains, plus xWAN staking that pays yield in BTC, ETH and stables.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Bridge volumes are modest. A weekly report cited a 109k USDT transfer as a highlight.

## 🛡️ Security & audits · 3/10 · ❌ FAIL

- The Cardano bridge contract was drained of ~$500K on 20 Jul 2026 ([post-mortem](https://medium.com/@wanchain_org/cardano-bnb-chain-bridge-incident-post-mortem-353e465276e7), [BlockSec](https://blocksec.com/blog/web3-security-allbridge-wanchain-exploits)). The team says EVM bridges use different code. **3.**

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- 2017 ICO. No enforcement found.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- Treasury-spending governance, a WAN/ETH liquidity proposal, and chain abstraction in development.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Cardano bridge drained (~$500K), 20 Jul 2026 |
| Team wallet → exchange during a pump | ⚪ Not proven (no public explorer API) |
| Live mint path | 🟢 PoS issuance roughly offset by burns |
| Entity concentration | 🟡 Foundation balance unpublished |

## 📚 Sources

- [Tier A] [Governance proposal #1](https://medium.com/wanchain-foundation/governance-proposal-1-increase-the-wan-burn-rate-4669ffc73488), [Sep 2026 update](https://wanchain.substack.com/p/wanchain-governance-goes-live-and), [Bridge post-mortem](https://medium.com/@wanchain_org/cardano-bnb-chain-bridge-incident-post-mortem-353e465276e7)
- [Tier B] [BlockSec weekly, 30 Jul 2026](https://blocksec.com/blog/web3-security-allbridge-wanchain-exploits), [Wanchain Academy, Oct 2026](https://wanchainacademy.com/quema-anual-de-wan-supero-el-millon-propuesta-wcp-002-activa-y-token2049/)
- [Tier A] CoinGecko `wanchain` (market, venues); pump days from KuCoin WAN-USDT daily closes
- Wanchain explorer (wanscan.org): browser-only, no public API

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Bridge exploit, 515.2M NIGHT | [post-mortem](https://medium.com/@wanchain_org/cardano-bnb-chain-bridge-incident-post-mortem-353e465276e7), [BlockSec](https://blocksec.com/blog/web3-security-allbridge-wanchain-exploits) | A+B | 16 Nov 2026 |
| 20% burn, ~1.1M WAN a year | [proposal](https://medium.com/wanchain-foundation/governance-proposal-1-increase-the-wan-burn-rate-4669ffc73488) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Foundation and treasury wallet addresses** | Ask the team, or read the bridge dashboard in a browser | Free |
| 2 | **Actual burn totals vs projection** | Bridge dashboard | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
