---
ticker: ADA
name: Cardano
chain: cardano (native layer 1)
contract: "native coin (no contract)"
overall_score: 5.1
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 7
  insider_holdings: 5
  selling_behavior: 5
  tokenomics_supply: 6
  liquidity_market: 8
  product_development: 8
  adoption_customers: 3
  security_audits: 6
  regulatory: 6
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "no funds stolen; a crafted transaction split mainnet for ~14.5 h on 21 Nov 2025 (Intersect incident report)"
  mint_path_live: "no discretionary mint; 6.0B ADA reserve still emits to stakers and the treasury under protocol rules (45B hard cap)"
  team_wallet_to_exchange_during_pump: "none found at hop 1–2; on-chain treasury payouts moved on pump days only between payout contracts and unlabelled vendor wallets; founding-entity wallets are not public"
  one_hop_sale_status: none_found
  treasury_spend: "804.4M ADA withdrawn from the on-chain treasury through 70 enacted governance actions, incl. 50M to a VC fund, 120M to AlphaGrowth and a 5M listings loan"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Staking rewards come mostly from the reserve (new ADA), not from fees; there is no burn, buyback or fee share."
pump_day_price_source: "Gate ADA_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (31 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.151959
price_source: "CoinGecko, 16 Nov 2026 ~5:08 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ADA · Overall grade **5.1 / 10 · ❌ FAIL**

**Summary:** Cardano is a large, long-running proof-of-stake chain with deep exchange liquidity and serious engineering. But it **earns almost nothing**: DefiLlama counts **$924,550 in chain fees over the last 12 months** on a **$5.71B market cap**, and only **$46.2M is locked in its apps**. On-chain governance has paid out **804.4M ADA (≈ $122M today) from the treasury** through 70 enacted proposals. These include **50M ADA to a VC fund** that left its receiving wallet within three days, a **120M ADA** ecosystem grant and **8.1M ADA for exchange listings and market making**. The price is down **69.4% in a year**. The Revenue gate fails.

**🚨 Top warning:** chain fees run at about **$2.5K a day** ([DefiLlama](https://defillama.com/chain/cardano)), while the treasury keeps spending. The "Cardano x Draper Dragon: Orion Fund" withdrawal paid [50,000,000 ADA](https://cardanoscan.io/transaction/c8695a581b41d349bd75def538cac434b85cef16699ec4e981c6ddcdd7c6a9d8) to [`stake1u99m…57z0g`](https://cardanoscan.io/stakekey/stake1u99m2kxsvdwlulg4l6qwjrpvayzrzwk0fugnvu3uklfqtws257z0g) on 9 Apr 2026. **40M** went [to an intermediate wallet](https://cardanoscan.io/transaction/5a5067637f0a6e8b5d6a98e75a96962b91ad074c4f0fc661fe30cf34b64769ff) the same day and [on to `stake1u9m8…ldm8p`](https://cardanoscan.io/transaction/4387bbc63b68c1c17f64089a0f83793e1c755bf64489e93874211d629c4b6de8), a wallet active since 2021 that is **now empty**. The other **10M** [left on 12 Apr](https://cardanoscan.io/transaction/fe85af38142c616e1aba74cb1de6a9055e90d1224967472f6cdd41ba9cb92486). The receiving key now holds 3 ADA. Where the funds went next is not labelled [Unverified] and is queued for Arkham. All links are in the 🔗 Evidence trail.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 8/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---

# 🪪 ADA · Cardano · 5.1 / 10 · ❌ FAIL

> **One line:** A big, liquid, well-engineered chain whose usage hardly pays for itself (≈ $0.92M fees a year on a $5.7B cap), funded by an on-chain treasury that has paid out 804M ADA, some of it to listings, market making and a VC fund.

| 📊 Market (CoinGecko, 16 Nov 2026 ~5:08 AM MST) | 🔗 On-chain (Koios, epoch 668, 16 Nov 2026) |
|---|---|
| **Price** $0.151959 | **Native coin**, 45,000,000,000 ADA hard cap |
| **24h / 7d / 30d** 🔴 −1.9% / −13.6% / −31.8% · 1y −69.4% | **Supply issued** 38,999,661,388 · **reserve** 6,000,338,612 |
| **Market cap** $5.712B · **FDV** $6.84B | **On-chain treasury** 1,426,715,411 ADA (≈ $217M) |
| **24h volume** $207.6M | **Fees, epoch 668** 47,547 ADA (5 days) |
| **Circulating** 37.57B of 45B | **Treasury withdrawals enacted** 804,427,136 ADA (70 actions, 17 receivers) |
| **ATH** $3.09 (1 Sep 2021) · now −95.1% | **DeFi TVL** $46.2M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 24h / 30d / 12 months | $1,476 / $55,192 / **$924,550** | [Tier A] [DefiLlama fees API](https://api.llama.fi/summary/fees/cardano?dataType=dailyFees), 16 Nov 2026 |
| Fees in epoch 668 (5 days) | 47,547 ADA (≈ $7.2K) | [Tier A] Koios `/totals` |
| Fees ÷ market cap | ≈ 0.016% a year | Derived |
| Who gets fees | A share goes to the treasury, the rest to stake pools and delegators along with reserve emissions | [Tier A] protocol rules |

**What it means:** Staking "yield" is mostly new ADA from the reserve, not users paying fees. Under $1M a year in fees against a $5.7B valuation is **2**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Staking rewards come mostly from the reserve (new ADA), not from fees; there is no burn, buyback or fee share.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

- Three founding entities: **Input Output (IOG)** does engineering, **EMURGO** does commercial adoption and the **Cardano Foundation** (Switzerland) handles standards and adoption [Tier A [cardano.org/genesis](https://cardano.org/genesis/)].
- **Intersect** (a member organisation) administers most treasury budgets. Spending is approved by on-chain DRep and Constitutional Committee votes [Tier A Koios `/proposal_list`].
- They are public, long-running organisations with named leaders. The Cardano Foundation publishes annual reports. IOG's and EMURGO's ADA balances are not published on-chain [Unverified].

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

| Bucket | ADA | Share | Source |
|---|---:|---:|---|
| IOHK (IOG) at genesis | 2,463,071,701 | 7.9% of genesis | [Tier A] [cardano.org/genesis](https://cardano.org/genesis/) |
| EMURGO at genesis | 2,074,165,644 | 6.7% | same |
| Cardano Foundation at genesis | 648,176,761 | 2.1% | same |
| **Founding entities total** | **5,185,414,108** | **16.7% of 31.11B genesis** | same |
| On-chain treasury (governance-controlled) | 1,426,715,411 | 3.8% of issued | [Tier A] Koios `/totals` |
| Undistributed reserve | 6,000,338,612 | 13.3% of cap | same |

**What it means:** The founding entities' share was moderate at launch, and the public sale was 25.93B (83%). How much they still hold today is not public for IOG or EMURGO, so it cannot be tested. The treasury is large and spent by vote rather than by the founders, but IOG is its biggest single recipient (see Selling). That is **5**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**A. Largest treasury withdrawals (Tier A, Koios `/proposal_list` + `/account_info`)**

| Receiver (stake credential) | Withdrawn | Balance now | Notes |
|---|---:|---:|---|
| [`stake17xzc…5qjr`](https://cardanoscan.io/stakekey/stake17xzc8pt7fgf0lc0x7eq6z7z6puhsxmzktna7dluahrj6g6ghh5qjr) (script) | 569,625,624 | 71,838,177 | IO / Intersect-administered budgets (IO engineering, Hydra, Consensus, Critical Integrations …) |
| [`stake1784…u3j9v`](https://cardanoscan.io/stakekey/stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v) (script) | 158,509,512 | 1,773,896 | incl. [120M AlphaGrowth "Cardano PRIME"](https://cardanoscan.io/transaction/529dccaadaa000746c22f1682574cb3f436eeba4d19710b90791a54226dc96d7) |
| [`stake1u99m…57z0g`](https://cardanoscan.io/stakekey/stake1u99m2kxsvdwlulg4l6qwjrpvayzrzwk0fugnvu3uklfqtws257z0g) (key) | 50,000,000 | 3 | ["Cardano x Draper Dragon: Orion Fund"](https://cardanoscan.io/transaction/8807e3cee3be5647742c329c1dea242f0c1c29b8ad050e15169e3b0302fcbfd6) |
| Listings | 5,000,000 + 3,126,000 | – | ["Loan ₳5,000,000 to Expand Cardano's Global Listings"](https://cardanoscan.io/transaction/03f671791fd97011f30e4d6b76c9a91f4f6bcfb60ee37e5399b9545bb3f2757a) and "Ecosystem Exchange Listing and Market Making" (in [this batch](https://cardanoscan.io/transaction/8ad3d454f3496a35cb0d07b0fd32f687f66338b7d60e787fc0a22939e5d8833e)) |

**B. Orion Fund flow (not pump days)**

| Day (UTC) | Move | ADA | Close / pump? |
|---|---|---:|---|
| 9 Apr 2026 | Treasury → `stake1u99m…` ([tx](https://cardanoscan.io/transaction/c8695a581b41d349bd75def538cac434b85cef16699ec4e981c6ddcdd7c6a9d8)) | 50,000,000 | $0.2543 · No |
| 9 Apr 2026 | → `stake1uxhe…` ([tx](https://cardanoscan.io/transaction/5a5067637f0a6e8b5d6a98e75a96962b91ad074c4f0fc661fe30cf34b64769ff)) → [`stake1u9m8…ldm8p`](https://cardanoscan.io/stakekey/stake1u9m8u3ffrgf95u3g2ts3p7z6cmu53j96qeygea2d7uvz6yg7ldm8p) ([tx](https://cardanoscan.io/transaction/4387bbc63b68c1c17f64089a0f83793e1c755bf64489e93874211d629c4b6de8)) | 40,000,000 | No |
| 12 Apr 2026 | → `stake1uxhe…` ([tx](https://cardanoscan.io/transaction/35345c46f18fd892f9270d648da53a80833b8b1c92153979f0c93fbf3bbcf1db)) → [`stake1u9el…glnp`](https://cardanoscan.io/stakekey/stake1u9el35uha3seyt0u9taxv7vdj095pe8u8gfk8zhvja5twfcpzglnp) ([tx](https://cardanoscan.io/transaction/fe85af38142c616e1aba74cb1de6a9055e90d1224967472f6cdd41ba9cb92486)) | 10,000,000 | $0.2364 · No |

`stake1u9m8…` is active since Jul 2021 (507 txs) and is now empty. Its largest outflows went to `stake1u9el…` (72.6M) and `stake1uykm…` (35.4M). Neither has an exchange label from a primary source [Unverified].

**C. Pump days (30 of the last 365, CoinGecko closes)**

- **AlphaGrowth / PRIME contract `stake1784…`** paid out on pump days 2–3 Aug ([3.49M](https://cardanoscan.io/transaction/6b5499833d6b0252df950b60574b9458efe992e0d16b850e0f29084547f3e1e5) · [12.71M](https://cardanoscan.io/transaction/a2e707c514b73a513354c44c80adcf83ba734ba5bb239d6549ab5cfe1f9017ec) · [11.52M](https://cardanoscan.io/transaction/3c5d1885f34268fa8ef07a40795d8d4ae50e3921cd5e74bd5ed6eebd065035d3)), 24 Aug ([9.70M](https://cardanoscan.io/transaction/256b530faf1d2d4e4d511027a4eafa912623c16e2d297ef9885c660bfc47e649)) and 5 Sep ([4.95M](https://cardanoscan.io/transaction/684772a59e7a32962993bfc3c403be5ef4475b59a1f251d1d088580afc4b07c4)). Every one of these went to another **script** credential, [`stake179d6…ktu9`](https://cardanoscan.io/stakekey/stake179d6k9z6t6fvsetj2djmerargk475lef9gfvshy4rwh4h7srcktu9), which holds 143.06M ADA. A script cannot be an exchange deposit, so these are internal moves.
- `stake179d6…` paid **6.29M** to unlabelled key wallet `stake1u9n8…dq8n9` on pump day 6 Aug 2026 (+15.3%) ([tx 1](https://cardanoscan.io/transaction/f8f7c4425c0f462e0582e069879e37da350832025edcca80293f3eaeb8b2d620) · [tx 2](https://cardanoscan.io/transaction/e922925be389a683d84c1d644946c5c680d72aaa1a5d82195532a0aae000f76c) · [tx 3](https://cardanoscan.io/transaction/5ce027a47ae813869be7eecb8f674049a8c6170606059f82957eb5b62f2f1a4b)). It is likely a vendor payout; the destination is [Unverified].
- Payout wallet `stake1uxkq…jyw03` got ~137M from `stake1784…` on [21 Jul](https://cardanoscan.io/transaction/5ec4a23402135b68b779001cff579bf63872cbb9cecd7e843054b1b9ea7592ce) and [14 Aug](https://cardanoscan.io/transaction/c869161a601ce2efa36a743113d37b9cca810b62f9c6c1ad93c56d13774ac86b) (not pump days). It has made 1,000+ small payouts and now holds 3.85M.
- **Founding-entity wallets (IOG, EMURGO, CF) are not public.** They were not tested.

**What it means:** No labelled exchange deposit from a treasury receiver was found at hops 1–2, and the pump-day flows found are contract-to-contract. But the money is disclosed only at proposal level, the trail goes cold in unlabelled wallets, and treasury money paid for listings and market making. The founders' own wallets cannot be tested. That is **5**: not a gate fail, but not proven clean.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate ADA_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (31 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- **Hard cap of 45B**, with 38.999B issued. The 6.0B reserve keeps emitting about 0.3% of the remaining reserve each epoch to rewards and the treasury, so inflation slows over time [Tier A protocol rules, Koios].
- No vesting cliffs or unlock calendar. The supply pressure that matters is treasury spending (804M so far) plus reserve emission.

## 💧 Liquidity & market · 8/10 · ✅ PASS

- **$207.6M** in 24h volume across top-tier exchanges, about 3.6% of market cap a day [Tier A CoinGecko].
- Liquidity is deep, but the trend is weak: −69.4% in a year and 30 pump days out of 365.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Mainnet has run since 2017, with Plutus smart contracts and on-chain governance (CIP-1694) live [Tier A].
- Treasury-funded engineering is large and public: IO core engineering, Hydra, Consensus, Mithril, Amaru, Dingo (a Go node), Pebble and Tweag core infrastructure (see the proposal list).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- **DeFi TVL is $46.2M** (DefiLlama), under 1% of market cap. Fees are about $1.5K a day.
- Usage is small for a top-tier valuation. Treasury money is now paying for adoption through Critical Integrations (93M), PRIME (120M) and listings.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No funds have been stolen at the protocol level. The protocol has a formal-methods culture.
- ⚠️ On **21 Nov 2025** a deliberately malformed delegation transaction exploited a deserialization bug in node 10.3.1–10.5.1. It **split mainnet for ~14.5 hours**, and exchanges paused deposits [Tier A [Intersect incident report](https://www.intersectmbo.org/news/incident-report-network-partition-analysis-and-resolution-strategy)].
- Treasury payout contracts hold large balances (71.8M and 143.1M). Their audits were not read this pass.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- The SEC named ADA as a security in its 2023 exchange cases. Those cases were later dropped [Tier B].
- The founding entities are regulated companies and foundations in several countries. No MiCA white paper check was done this pass.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| Every epoch (5 days) | Reserve emission to rewards and the treasury |
| Ongoing | Treasury budget votes by DReps and the Constitutional Committee (each one is new spend) |
| Ongoing | Hydra, Leios and other IO roadmap items funded by the 2025–2026 budgets |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 No funds stolen · chain split for 14.5 h on 21 Nov 2025 |
| Live mint path | 🟢 No discretionary mint · rule-based reserve emission under a 45B cap |
| Team wallet → exchange during a pump | 🟢 None found at hops 1–2 · 🟡 founder wallets not public |
| Treasury paying for listings / market making | 🟡 Yes, disclosed: 5M listings loan + 3.126M listing and market making |
| Revenue vs valuation | 🔴 ≈ $0.92M fees a year on a $5.71B cap |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Treasury withdrawal receivers (hops 1–2) | Cardano treasury recipients | Governance actions + chain trace | medium | yes (governance records) | None: no labelled exchange deposit on a pump day |
| Founder wallets | Unpublished | — | low | no | Selling stays 5 (not proven clean) |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Koios API (`/tip`, `/totals`, `/proposal_list`, `/account_info`, `/account_txs`, `/tx_info`, `/account_addresses`), 16 Nov 2026 MST
- [Tier A] [cardano.org/genesis](https://cardano.org/genesis/) for the genesis allocation
- [Tier A] DefiLlama fees API and chain TVL (Cardano), 16 Nov 2026
- [Tier A] CoinGecko `cardano` market data and 365-day closes, 16 Nov 2026 ~5:08 AM MST
- [Tier A] [Intersect incident report](https://www.intersectmbo.org/news/incident-report-network-partition-analysis-and-resolution-strategy) · [IOG post](https://www.iog.io/news/ouroboros-self-healing-in-the-wild)
- [Unverified] current IOG and EMURGO holdings; owners of `stake1u9m8…`, `stake1u9el…`, `stake1uykm…`, `stake1u9n8…`, `stake1uxkq…`; the Orion Fund's investments

## 🔗 Evidence trail

*Every link below opens the primary record for the claim.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Genesis split (5.19B to IOHK, EMURGO, CF) | [cardano.org/genesis](https://cardano.org/genesis/) | A | 16 Nov 2026 |
| 12-month fees $924,550 | [DefiLlama API](https://api.llama.fi/summary/fees/cardano?dataType=dailyFees) · [chain page](https://defillama.com/chain/cardano) | A | 16 Nov 2026 |
| Treasury 1.427B, reserve 6.0B | [Koios totals](https://api.koios.rest/api/v1/totals) | A | 16 Nov 2026 |
| 50M Orion Fund withdrawal and onward moves | [proposal](https://cardanoscan.io/transaction/8807e3cee3be5647742c329c1dea242f0c1c29b8ad050e15169e3b0302fcbfd6) · [withdrawal](https://cardanoscan.io/transaction/c8695a581b41d349bd75def538cac434b85cef16699ec4e981c6ddcdd7c6a9d8) · [40M](https://cardanoscan.io/transaction/4387bbc63b68c1c17f64089a0f83793e1c755bf64489e93874211d629c4b6de8) · [10M](https://cardanoscan.io/transaction/fe85af38142c616e1aba74cb1de6a9055e90d1224967472f6cdd41ba9cb92486) | A | 16 Nov 2026 |
| 120M AlphaGrowth PRIME | [proposal](https://cardanoscan.io/transaction/529dccaadaa000746c22f1682574cb3f436eeba4d19710b90791a54226dc96d7) · [119M to contract](https://cardanoscan.io/transaction/ca3f7b243232049388f548a27bd3a89c47d84b9014aaa0f8dd7759fea515cd6c) | A | 16 Nov 2026 |
| Listings loan and market-making budget | [5M loan](https://cardanoscan.io/transaction/03f671791fd97011f30e4d6b76c9a91f4f6bcfb60ee37e5399b9545bb3f2757a) · [3.126M batch](https://cardanoscan.io/transaction/8ad3d454f3496a35cb0d07b0fd32f687f66338b7d60e787fc0a22939e5d8833e) | A | 16 Nov 2026 |
| Pump-day payouts are contract-to-contract | [2 Aug](https://cardanoscan.io/transaction/6b5499833d6b0252df950b60574b9458efe992e0d16b850e0f29084547f3e1e5) · [3 Aug](https://cardanoscan.io/transaction/a2e707c514b73a513354c44c80adcf83ba734ba5bb239d6549ab5cfe1f9017ec) · [24 Aug](https://cardanoscan.io/transaction/256b530faf1d2d4e4d511027a4eafa912623c16e2d297ef9885c660bfc47e649) · [5 Sep](https://cardanoscan.io/transaction/684772a59e7a32962993bfc3c403be5ef4475b59a1f251d1d088580afc4b07c4) | A | 16 Nov 2026 |
| Chain split, 21 Nov 2025 | [Intersect report](https://www.intersectmbo.org/news/incident-report-network-partition-analysis-and-resolution-strategy) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Wallet labels for 10 Cardano wallets** (the wallet list: the Orion Fund route, PRIME payout wallets and the pump-day receiver `stake1u9n8…`) | **Not covered by Arkham:** Arkham does not support Cardano (checked 16 Nov 2026). Use Cardanoscan / AdaStat pool and exchange tags, or ask Intersect and the fund manager to identify the wallets | Free |
| 2 | **IOG and EMURGO current holdings** | Ask both for wallet disclosures. Trace the genesis redemption addresses forward (adagenesistransparency.com traced IOG's) | Free |
| 3 | **What did the Orion Fund buy?** | Read the Orion Fund's reporting under the treasury proposal and match it to on-chain moves | Free |
| 4 | **Were the listings loan and market-making ADA sold?** | Trace both withdrawals to their receivers and check for exchange deposits and repayment of the 5M loan | Free (Koios) |
| 5 | **Treasury payout-contract audits** | Read the audits for the Intersect / Sundae treasury contracts behind `stake17xzc…` and `stake179d6…` | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
