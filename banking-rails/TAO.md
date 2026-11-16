---
ticker: TAO
name: Bittensor
chain: bittensor
contract: "native (Subtensor / Finney)"
overall_score: 5.5
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 5
  insider_holdings: 6
  selling_behavior: 5
  tokenomics_supply: 8
  liquidity_market: 8
  product_development: 8
  adoption_customers: 6
  security_audits: 5
  regulatory: 5
  catalysts: 6
gates_failed: [revenue]
red_lines:
  one_hop_sale_status: none_found
  hack_exploit: none_in_series
  central_halt_authority: present
  foundation_wallets_unpublished: tripped
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Holders are paid with new TAO, not fees; subnet income does not flow to TAO by protocol."
pump_day_price_source: "Gate TAO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (52 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 193.44
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
chain_read_block: 9506723
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TAO · Overall grade **5.5 / 10 · ❌ FAIL**

**Summary:** A fair-launch, bitcoin-style supply with no team or VC allocation and an active AI-subnet economy, but the network has no meaningful fee revenue (rewards are paid from new issuance), and core-developer foundations can still halt the chain.

**⚠️ Top warning:** TAO has **no fee revenue to holders** (rewards are new issuance, ~3,600 TAO/day), the foundations can **halt the chain** (done in July 2024), and foundation/early-miner wallets are **unpublished**, so selling into the 53 pump days can't be tested. Check it: [emissions docs](https://www.bittensor.com/docs/concepts/emissions) · [July 2024 halt](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d) · [Arkham: no foundation entity](https://intel.arkm.com/explorer/entity/bittensor).

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 8/10 | ✅ PASS |
| 💧 Liquidity & market | 8/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (3 ≤ 3).*

---


# 🪪 TAO · Bittensor · 5.5 / 10 · ❌ FAIL

> **One line:** A fair-launch, bitcoin-style supply with no team or VC allocation and an active AI-subnet economy, but the network has no meaningful fee revenue (rewards are paid from new issuance), and core-developer foundations can still halt the chain.

ℹ️ **Adapted for a layer-1.** "Revenue" = fees and recycling that return value to TAO (subnet businesses' own income is not network revenue). "Foundation" = Opentensor Foundation (OTF) and Rao Foundation. "Holdings / Selling" = foundation / insider stacks, which do not exist as allocations, plus large known holders.

| 📊 Market (CoinGecko, 14 Nov 2026 12:12 PM MST) | 🔗 On-chain (Subtensor RPC, block 9,506,723) |
|---|---|
| **Price** $193.44 | **Total issuance** 11,727,180.43 TAO of 21M cap (55.8%; cross-check on [Taostats](https://taostats.io)) |
| **24h / 7d / 30d** 🔴 −11.3% / −13.2% / −29.8% | **Total staked** 7,464,253 TAO (63.6% of issuance) |
| **Market cap** $2.27B · **FDV (issued)** same | **Subnets** 129 networks registered (incl. root) |
| **24h volume** $142.3M | **Emission** 0.5 TAO/block ≈ 3,600 TAO/day (after Dec 2025 halving) |
| **ATH** $757.60 (7 Mar 2024) · now −74% | **Next halving** at 15.75M TAO issued |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama fees / revenue | **Not tracked** for Bittensor | [Tier A] DefiLlama (absence) |
| Native TAO fees and EVM fees | Subtracted from issuance (recycled), pushing halvings out | [Tier A] [Bittensor docs — emissions](https://www.bittensor.com/docs/concepts/emissions) |
| Subnet registration costs | Recycled / burned | [Tier A] docs |
| Rewards to miners / validators / stakers | Paid from **new issuance** (3,600 TAO/day ≈ $696k/day at spot) | [Tier A] docs · calculated |
| Subnet buybacks | Mature subnets route excess emission TAO into alpha buybacks — funded by issuance, not customers | [Tier A] docs |

**What it means:** TAO holders are paid with newly minted TAO, not with fees. Some subnets sell real AI services, but that money does not flow to TAO by protocol. Score 3 = gate fail.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Holders are paid with new TAO, not fees; subnet income does not flow to TAO by protocol.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Opentensor Foundation (OTF) | Ecosystem, events, developer programs; supplies the **Triumvirate** that holds chain-upgrade authority | [Tier B] Blockworks token-transparency filing |
| Rao Foundation | Now maintains core code: `opentensor/subtensor` redirects to **[`RaoFoundation/subtensor`](https://github.com/RaoFoundation/subtensor)** (pushed 13 Nov 2026, release v490 on 10 Nov 2026); reportedly runs Proof-of-Authority nodes | [Tier A] GitHub · role [Tier B] Blockworks |
| Founders | Jacob Steeves and Ala Shaabana (commonly cited) | [Unverified] |
| Central control | OTF put the chain into "safe mode" (halted transactions) during the July 2024 incident | [Tier A] [OTF community update, 3 Jul 2024](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d) |

**What it means:** Development is active, but a small group can still upgrade and halt the chain. That is more central control than BTC or ETH.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Bucket | TAO | Source |
|---|---:|---|
| Team / VC / ICO allocation | **0** — fair launch, no premine | [Tier A] [Bittensor blog "TAO token economy explained"](https://blog.bittensor.com/tao-token-economy-explained-17a3a90cd44e) |
| OTF / Rao Foundation balances | **Not found** — addresses not published | Not found |
| Grayscale Bittensor Trust | Holds TAO (fair value below book cost in mid-2026 filings) | [Tier A] SEC EDGAR (10 Oct 2026 pass) |

**What it means:** No insider allocation exists, which is the best possible start. But early miners and the foundations will have earned TAO since 2021, and those balances aren't disclosed.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Pump test:** CoinGecko daily closes, 15 Nov 2025 – 14 Nov 2026: **53 of 361 days** were pump days — the most of any coin in this set. Last 26 Sep 2026 (+21.5%).

| Check | Finding |
|---|---|
| Foundation → exchange on a pump day | **Not found — foundation wallets not published** |
| Team unlocks | None exist |
| Subnet-owner selling | Subnet owners receive 18% of their subnet's alpha by default and can sell it; not traced |

**What it means:** There's no team unlock to dump, but foundation and early-miner wallets can't be checked. Not proven → fail.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate TAO_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (52 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 8/10 · ✅ PASS

| Item | Value | Source |
|---|---|---|
| Cap | 21,000,000 TAO | [Tier A] docs |
| Issued | 11,727,180.43 (on-chain; matches CoinGecko) | [Tier A] Subtensor `TotalIssuance` |
| Emission | 0.5 TAO/block, 7,200 blocks/day → 3,600/day (~11.2% a year of current supply) | [Tier A] docs |
| Halving trigger | By issuance (15.75M next), not block count; recycling delays it | [Tier A] docs |
| Alpha tokens | Each subnet has its own 21M-cap alpha since dTAO (Feb 2025, block 4,920,351) | [Tier A] docs |

**What it means:** Bitcoin-like and fully on-chain, but still ~11% annual inflation today.

## 💧 Liquidity & market · 8/10 · ✅ PASS

- $142.3M 24h volume; major CEX listings; Grayscale trust in the US.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Weekly-cadence runtime releases (v490, 10 Nov 2026); 129 subnets; recent emission-design changes (demand-gated emission shares, owner-set emission splits) documented [Tier A docs / GitHub].

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- 129 subnets and 63.6% of TAO staked show heavy participation. Paying external customers exist at some subnets (e.g. Chutes inference) but are not measured here [Unverified].

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| July 2024 incident | Malicious PyPI package (bittensor 6.12.2) stole decrypted keys; ~32,000 TAO (~$8M) taken; chain not compromised; OTF halted the chain | [Tier A] OTF update · [Tier B] The Block |
| Since then | No TAO-specific hack in this series | [Tier A] |
| Admin power | Triumvirate / PoA authority can upgrade and pause | [Tier B] |

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found. Grayscale trust files with the SEC. Foundation jurisdictions not checked this pass.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| Ongoing | 3,600 TAO/day issuance | Supply ↑ |
| When issuance hits 15.75M | Second halving → 0.25 TAO/block | Supply ↓ |
| Weekly | Runtime releases | Product |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None in this series (2024 incident is history) |
| Central halt authority | 🟡 Present ([July 2024 safe-mode halt](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d)) |
| Foundation wallets unpublished | 🟡 Tripped ([Arkham: no OTF/Rao entity](https://intel.arkm.com/explorer/entity/bittensor)) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Foundation and early-miner wallets | Not published | — | low | no | Selling stays 5 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Subtensor RPC (`entrypoint-finney.opentensor.ai`): `SubtensorModule.TotalIssuance`, `TotalStake`, `TotalNetworks`, chain head; 14 Nov 2026 ~12:35 PM MST
- [Tier A] [Bittensor docs — emissions](https://www.bittensor.com/docs/concepts/emissions) · [TAO token economy](https://blog.bittensor.com/tao-token-economy-explained-17a3a90cd44e) · [OTF update 3 Jul 2024](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d)
- [Tier A] GitHub [`RaoFoundation/subtensor`](https://github.com/RaoFoundation/subtensor) · [Taostats](https://taostats.io) explorer for issuance/stake cross-checks
- [Tier A] [CoinGecko `bittensor`](https://www.coingecko.com/en/coins/bittensor) price and 365-day daily closes, 14 Nov 2026 12:12 PM MST
- [Tier A] SEC EDGAR, Grayscale Bittensor Trust (from 10 Oct 2026 pass)
- [Tier B] Blockworks token-transparency filing · The Block
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): **no Opentensor Foundation or Rao Foundation entity**. Search returns only a "Bittensor" entity ([Arkham entity “Bittensor”](https://intel.arkm.com/explorer/entity/bittensor); 2 EVM contract-deployer addresses, $23,447), and Arkham does not cover Subtensor accounts. Foundation balances and exchange deposits stay unverified. No score change
- [Unverified] Founder names; subnet customer revenue; foundation balances

## 🔗 Evidence trail

*Strongest findings first. Subtensor is not covered by Arkham; links open official docs, GitHub and the Taostats explorer. Subtensor RPC reads have no shareable URL.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Rewards paid from new issuance; fees are recycled, no fee flow to holders | [Bittensor docs — emissions](https://www.bittensor.com/docs/concepts/emissions) | A | 14 Nov 2026 |
| OTF halted transactions ("safe mode") in July 2024 | [OTF community update](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d) | A | 14 Nov 2026 |
| Fair launch, 0 team/VC allocation | [TAO token economy](https://blog.bittensor.com/tao-token-economy-explained-17a3a90cd44e) | A | 14 Nov 2026 |
| Foundation wallets unpublished; Arkham has no OTF/Rao entity and no Subtensor coverage | [Arkham “Bittensor” entity](https://intel.arkm.com/explorer/entity/bittensor) | B | 15 Nov 2026 ~11:05 AM MST |
| Total issuance 11.73M of 21M; 63.6% staked | Subtensor RPC (no public link) · [Taostats](https://taostats.io) | A | 14 Nov 2026 |
| Core code maintained by Rao Foundation (release v490, 10 Nov 2026) | [GitHub](https://github.com/RaoFoundation/subtensor) | A | 14 Nov 2026 |

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Foundation (Opentensor) and early-miner wallets.** Not published, so pump-day selling cannot be tested | Ask the Opentensor Foundation to publish its wallets, then match their exchange sends to the Gate pump-day list | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
