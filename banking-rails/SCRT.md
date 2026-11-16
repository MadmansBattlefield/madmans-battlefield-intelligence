---
ticker: SCRT
name: Secret Network
chain: secret
contract: "native uscrt on Secret Network (secret-4)"
overall_score: 2.6
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 2
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 1
  liquidity_market: 3
  product_development: 4
  adoption_customers: 2
  security_audits: 2
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: the CW20-ICS20 contract on the Axelar route was drained of ~$4.67M through an infinite-mint flaw (10 Jun 2026), unnoticed for seven days"
  mint_path_live: "yes: governance minted 1,079M SCRT on 21 Aug 2026 (v1.26 upgrade); inflation is now pinned at 5%"
  team_wallet_to_exchange_during_pump: "not proven: Foundation and core-development lines sent ~10.2M SCRT (~$92k) to one busy unlabelled hot wallet between 28 Aug and 6 Nov 2026, none on a Gate pump day"
  one_hop_sale_status: none_found
  entity_concentration: "the ten mint buckets hold ~81% of bonded stake (690.9M of 856.3M SCRT)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Gas fees go to validators and stakers, and staking yield is inflation; there is no fee capture, burn or buyback, so revenue does not reach holders."
pump_day_price_source: "Gate SCRT-USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.00335963
price_source: "CoinGecko, 16 Nov 2026 ~11:20 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SCRT · Overall grade **2.6 / 10 · ❌ FAIL**

**Summary:** Secret Network is a Cosmos privacy chain. Its founding developer company ended support on 1 September 2026. To keep the chain alive, governance passed Proposal 365 and minted 1,079M new SCRT on 21 August 2026. That cut existing holders to about a quarter of the supply. Most of the new SCRT went to a Foundation, a core-development team, advisors and an ecosystem fund. Those buckets now stake about 81% of all bonded SCRT, so they effectively control governance. In June 2026 the chain's Axelar bridge route was drained of about $4.67M. No fees reach holders, and the price is down 99.97% from its peak. The revenue gate fails.

**🚨 Top warning:** **a 75% dilution mint handed governance to insiders.** The v1.26 upgrade minted **1,079,000,000 SCRT** on 21 Aug 2026. The new SCRT went to Foundation (299M), core development (299M), ecosystem (178M), advisors (72M), research (72M), validators (72M), builders and relayers (43M) and remediation (44M). See the [upgrade config](https://github.com/Secret3dev/SecretNetwork/blob/secretcommunity-release-1/app/upgrades/v1.26/config/ECONOMICS.md) and [CryptoSlate](https://cryptoslate.com/layer-1-network-dilutes-supply-by-75-overnight-to-fund-survival-after-main-developer-quits/). The bucket accounts now stake **690.9M of the 856.3M bonded SCRT (~81%)** (LCD staking pool, 16 Nov 2026). Separately, the Foundation's spending line and a core-development line sent about 10.2M SCRT to one busy, unlabelled hot wallet. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 2/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 1/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 2/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SCRT · Secret Network · 2.6 / 10 · ❌ FAIL

> **One line:** A privacy L1 diluted 4× to survive its developer's exit, now governed by the mint's recipients.

| 📊 Market (CoinGecko, 16 Nov 2026 ~11:20 AM MST) | 🔗 Chain (Secret LCD) |
|---|---|
| **Price** $0.00336 (Gate closed $0.00208) | **Supply** 1,461.0M SCRT (bank module) |
| **24h / 7d / 30d** 🟢 +20.0% / 🟢 +1.5% / 🔴 −53.8% | **Bonded** 856.3M; mint buckets stake 690.9M (~81%) |
| **Market cap** $2.33M · **FDV** $4.91M | **Inflation** 5%, foundation tax 0 (v1.26) |
| **24h volume** ~$0.08M (Kraken USD $53k, Gate $20k, Kraken EUR $19k, Osmosis) | **Liquid at the mint** 308.4M |
| **ATH** $10.38 (28 Oct 2021) · now −99.97% | |
| **Pump days** 31 in the last year (Gate SCRT-USDT; largest +27.9%) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Gas fees go to validators and stakers. Staking yield is 5% inflation, not revenue. No fee capture, burn or buyback. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Gas fees go to validators and stakers, and staking yield is inflation; there is no fee capture, burn or buyback, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 2/10 · ❌ FAIL

- The founding developer company exited on 1 Sep 2026 after its Arbitrum-migration proposal (360) was rejected. Continuation now rests on a Foundation and a newly funded core team ([Blockworks disclosures](https://app.blockworks.com/projects/secret-network/disclosures)). The two sides publicly dispute each other's record. People are described here by role only.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

- Mint buckets: Foundation 299M (10% liquid, 60-month linear after a 6-month cliff), core development 299M (same), ecosystem 178M (fully liquid), advisors 72M, research 72M, validators 72M, builders and relayers 43M, remediation 44M ([ECONOMICS.md](https://github.com/Secret3dev/SecretNetwork/blob/secretcommunity-release-1/app/upgrades/v1.26/config/ECONOMICS.md)). They stake ~81% of bonded SCRT.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I read all ten bucket accounts on the LCD. The Foundation account sent 7.8M SCRT through `secret1p4y0…6jsx`, and a core-development account sent 2.4M through two relays. Both ended at `secret1ctpu…99wc`, an unlabelled wallet making ~33 sends a day (28 Aug–6 Nov 2026, ~$92k in total). None fell on a Gate pump day. The ecosystem fund paid 29.0M to five wallets on 29 Sep. Destinations are unlabelled. **Not proven → 4.**

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate SCRT-USDT UTC daily closes.

## 📊 Tokenomics & supply · 1/10 · ❌ FAIL

- 1,079M minted in one step (~75% of the new supply) plus 5% inflation. Vested buckets keep unlocking monthly from Feb 2027.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $0.08M a day, mostly Kraken. The mint's own documents warn exchanges might drop support.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- The chain runs v1.26, maintained by community validators. No founding developer.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- Little activity. The remediation pool hasn't been paid out yet.

## 🛡️ Security & audits · 2/10 · ❌ FAIL

- The CW20-ICS20 contract on the Axelar route was drained of ~$4.67M through an infinite-mint flaw on 10 Jun 2026 and went unnoticed for seven days ([The Block](https://www.theblock.co/news/ecosystems/2026-06-20-secret-networks-axelar-bridge-drained-for-4-67-million-in-infinite-mint-exploit-that-went-unnoticed-for-seven-days-405459), [Common Prefix](https://www.commonprefix.com/blog/secret-network-exploit)). **2.**

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

- Remediation payouts and whether exchanges keep supporting SCRT. No dated upside catalyst.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 Yes: ~$4.67M bridge-route drain, 10 Jun 2026 |
| Team wallet → exchange during a pump | ⚪ Not proven: ~10.2M SCRT to an unlabelled hot wallet, no pump days |
| Live mint path | 🔴 1,079M minted Aug 2026; 5% inflation |
| Entity concentration | 🔴 Mint buckets stake ~81% of bonded SCRT |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| `secret1ctpu…99wc` hot wallet | Unlabelled | Secret explorer flows | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): not used: no Secret Network addresses were looked up on Arkham for this report
- [Tier A] [Proposal 365 on-chain record](https://rest.lavenderfive.com/secretnetwork/cosmos/gov/v1/proposals/365), [v1.26 ECONOMICS.md](https://github.com/Secret3dev/SecretNetwork/blob/secretcommunity-release-1/app/upgrades/v1.26/config/ECONOMICS.md), [v1.26 config.go](https://github.com/Secret3dev/SecretNetwork/blob/secretcommunity-release-1/app/upgrades/v1.26/config/config.go)
- [Tier A] Secret LCD: staking pool, bank supply, bucket balances, delegations and sends (16 Nov 2026)
- [Tier B] [CryptoSlate on the mint](https://cryptoslate.com/layer-1-network-dilutes-supply-by-75-overnight-to-fund-survival-after-main-developer-quits/), [Blockworks disclosures](https://app.blockworks.com/projects/secret-network/disclosures), [The Block on the exploit](https://www.theblock.co/news/ecosystems/2026-06-20-secret-networks-axelar-bridge-drained-for-4-67-million-in-infinite-mint-exploit-that-went-unnoticed-for-seven-days-405459), [Common Prefix](https://www.commonprefix.com/blog/secret-network-exploit)
- [Tier A] CoinGecko `secret` (market, venues); pump days from Gate SCRT-USDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Foundation → `secret1p4y0…` 1.0M, 26 Sep 2026 | tx 269B02CC65958F6BE8F7A6B5606C6E2957FD69B705219B828750E88BC751F0F4 (code 0) | A | 16 Nov 2026 |
| `secret1p4y0…` → `secret1ctpu…` 5.0M, 28 Aug 2026 | tx 54627B1BC23404A8BF76CD4F61F1FD41D1C0059511C78B3D75A62ED33FC91C5E (code 0) | A | 16 Nov 2026 |
| Core-dev line → `secret1ctpu…` 1.11M, 5 Nov 2026 | tx 6AC74B86A8E0B5FA746996E35063FAF38C7AE87047314241654635BDAA2CDB01 (code 0) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls `secret1ctpu…99wc`** (exchange, OTC desk or market maker?) | No public Secret label source | Arkham, if it covers Secret |
| 2 | **Where the 29.0M ecosystem grants went** | Unlabelled | LCD follow-up |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
