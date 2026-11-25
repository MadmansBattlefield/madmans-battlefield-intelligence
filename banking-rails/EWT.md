---
ticker: EWT
name: Energy Web Token
chain: energy-web-x
contract: "0xb66a5d30d04f076e78ffb0d045c55846fdcde928"
overall_score: 4.0
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 5
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: none found
  mint_path_live: "yes: 192,307.69 EWT minted on Ethereum about every 4 weeks since Oct 2025 (~2.5M a year); 14.04M of headroom remains under the 100M cap"
  team_wallet_to_exchange_during_pump: "none found (an unattributed 3-of-5 Safe sent 165k EWT to a KuCoin deposit in Oct 2026 on non-pump days); Foundation wallets not identified"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "unknown (Foundation and EWX treasury wallets not published)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No checkable revenue reaches the token."
pump_day_price_source: "KuCoin EWT/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.250898
price_source: "CoinGecko, 16 Nov 2026 8:20 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### EWT · Overall grade **4.0 / 10 · ❌ FAIL**

**Summary:** Energy Web is a non-profit-led blockchain for the energy sector. In 2025–2026 it retired its permissioned Energy Web Chain and moved to **Energy Web X** (a Polkadot parachain), with EWT now an **ERC20 on Ethereum** ([`0xB66a…e928`](https://etherscan.io/token/0xb66a5d30d04f076e78ffb0d045c55846fdcde928)). Exchanges finished migrating in Jul 2026. The token is capped at 100M, but **a new 192,308 EWT has been minted every ~4 weeks since Oct 2025** (~2.5M a year, ~3%). On-chain usage is nil (**$17 of fees in a year**, $51k TVL on the old chain), and no enterprise revenue is published. The price is down **98.9% from ATH and 67% in a year**. Revenue trips the hard gate.

**🚨 Top warning:** the docs say "no automatic inflation", yet the chain shows a steady mint. The Energy Web FAQ says new EWT "can only be minted via on-chain governance" ([FAQ](https://docs.energyweb.org/energy-web-x-upgrade-faq)). In practice, the ERC20 has minted [192,307.69 EWT](https://etherscan.io/tx/0x8bdc0033460e37d219c37efae1fdb09eef1dc5aa90f2fa59a10e910aaafd0104) to the Energy Bridge 14 times since [the 83.26M genesis mint](https://etherscan.io/tx/0xee122c867c7bda420eebbc84ccb656fb3935eb08b585efe0db1ae09c4b2b3fbe), taking supply to **85.95M**. Meanwhile, the token trades only ~$246k a day.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 EWT · Energy Web Token · 4.0 / 10 · ❌ FAIL

> **One line:** A respected energy-sector consortium that has just rebuilt its chain, but the token has no measurable revenue, thin trading, and a steady ~3% yearly mint.

| 📊 Market (CoinGecko, 16 Nov 2026 8:20 AM MST) | 🔗 On-chain (Ethereum + Energy Web Chain, 16 Nov 2026) |
|---|---|
| **Price** $0.250898 | **ERC20 EWT** [`0xB66a…e928`](https://etherscan.io/token/0xb66a5d30d04f076e78ffb0d045c55846fdcde928) supply 85,953,337; 1,208 holders (Blockscout) |
| **24h / 7d / 30d** 🟢 +4.9% / 🔴 −7.4% / −25.3% · 1y −67.2% | **Energy Bridge** [`0x5dDe…259D`](https://etherscan.io/address/0x5dded30f8cd557257ccdc4a530cb77ac45f0259d) 67,558,550 EWT locked for EWX |
| **Market cap** $20.34M · **FDV** $20.34M | **Old-chain lift bridge** [`0x0BDb…d2B1`](https://explorer.energyweb.org/address/0x0BDb4Ff8396Fbd0b8Baa9cF2ea188cC620D5d2B1) 62.64M native EWT |
| **24h volume** $246k (KuCoin, MEXC, Kraken) | **Fees, 12 months** $17 · revenue $0 ([DefiLlama](https://api.llama.fi/summary/fees/energyweb?dataType=dailyFees)) |
| **ATH** $22.67 (16 Apr 2021) · now −98.9% | **Cap** 100M; 83.26M frozen at the Aug 2025 Zurich fork |

*Note: CoinGecko still lists the old bridged token `0x178c…6054` (917k supply). The live ERC20 named in Energy Web's own FAQ is `0xB66a…e928`.*

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$17** | [Tier A] [DefiLlama fees](https://api.llama.fi/summary/fees/energyweb?dataType=dailyFees) |
| Protocol revenue | **$0** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/energyweb?dataType=dailyRevenue) |
| Enterprise / VCC revenue | **Not found.** VCC clients "pay for the service", but no totals are published | [Tier A] [Energy Web FAQ](https://docs.energyweb.org/energy-web-x-upgrade-faq) |
| Staker income | Fees plus "governance-approved issuance" | [Tier A] same |

**What it means:** No checkable revenue reaches the token. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No checkable revenue reaches the token.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Organisation | Energy Web Foundation (non-profit), with energy-company affiliates since 2017 | [Tier B] [EW chain paper](https://academy.bit2me.com/wp-content/uploads/2022/03/TheEnergyWebChain-v2-FINAL.pdf) + [Crypto Adventure review](https://cryptoadventure.com/energy-web-review-2026-ewt-ewx-and-blockchain-infrastructure-for-the-energy-transition/) |
| Governance | The Aug 2025 Zurich hard fork was approved by the old validator set. Governance is moving to on-chain EWX referenda | [Tier A] [FAQ](https://docs.energyweb.org/energy-web-x-upgrade-faq) |
| Disclosure | Good technical docs; no treasury report or wallet list | — |

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | EWT | Notes |
|---|---:|---|
| Energy Bridge [`0x5dDe…259D`](https://etherscan.io/address/0x5dded30f8cd557257ccdc4a530cb77ac45f0259d) | 67.56M | Locked backing for EWT on EWX, not a team wallet [Tier A FAQ] |
| Community Fund → EWX treasury | **Not found** | Originally 37.9M EWT, released over 10 years; now "transitions into the EWX on-chain treasury" [Tier A FAQ + Tier B chain paper] |
| 3-of-5 Safe [`0x2ea5…D7f5`](https://etherscan.io/address/0x2ea55460f499fab0cc851e49716f3f02c599d7f5) | 1.10M | Received 1.27M from the Energy Bridge on 2 Oct 2026. [Arkham](https://intel.arkm.com/explorer/address/0x2ea55460f499fab0cc851e49716f3f02c599d7f5): generic Gnosis Safe, no entity; owner not known |
| Bitcoin Suisse custody [`0x6b7a…e66b`](https://intel.arkm.com/explorer/address/0x6b7afaacb2fa911594de32762e6c7c35b833e66b) | 500,000 | Arkham: **Bitcoin Suisse Deposit**. Filled by the [Bitcoin Suisse Hot Wallet](https://intel.arkm.com/explorer/address/0x2dcbc69ca4d13c232f39fc65d1aa568567c1c1c3) on 11 May 2026 ([tx](https://etherscan.io/tx/0xad2794ae6954057857300ec3251e19c3f4364e0f66ff0fd8f75c2eb3bea4d2c1)). A custodian's client address, **not** a Foundation wallet |
| [`0xC317…2a4d`](https://intel.arkm.com/explorer/address/0xc3174f2190e5d9c55a295656f694990793f72a4d) | 404,014 | Unlabelled; received from the Bitcoin Suisse Hot Wallet on 5 Oct 2026 ([tx](https://etherscan.io/tx/0x98a54615951665e5c046c481e00613c37bef766a785dae2cbd18ac007c541bfd)). Looks like a custodian client, not the Foundation [Unverified] |
| Kraken 245 / 246, MEXC 16 | 7.2M | Exchange wallets (Etherscan tags) |

**What it means:** Where the Foundation's and treasury's EWT sit is not disclosed. **4**.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Pump test uses KuCoin EWT/USDT daily closes (UTC). 45 of the last 365 days were pump days.*

| Day (UTC) | Route | EWT | 5-day change | Pump? |
|---|---|---:|---:|---|
| 2 Oct 2026 | Energy Bridge → Safe `0x2ea5…` ([tx](https://etherscan.io/tx/0xee5bb7483c2ea8ecf08c7b10fefc30042f4649511248bf711c37cbf0104cb849)) | 1,267,417 | +13.9% | Pump day (lowered from EWX, not a sale) |
| 6 Oct 2026 | Safe → KuCoin deposit [`0xf08a…5Be9`](https://etherscan.io/address/0xf08ab18b22dbda8c66e8b46c0056c46bb72d5be9) ([tx](https://etherscan.io/tx/0xacfe6cfb1e95c24ec6f68d0e335eeb2d8497e1aec8eaa9bac78acec808bf9887)) | 65,000 | −0.8% | No |
| 14 Oct 2026 | Safe → same KuCoin deposit ([tx](https://etherscan.io/tx/0x07a459e8defde9ba9be2cc09d8664baff3be274c8115a93f0cc3aedad16c94b6)) | 100,000 | −0.1% | No |

- The Safe is not attributed to the Foundation, and Arkham's first transfers page does not show its KuCoin sends. The 500k and 404k EOAs are Bitcoin Suisse custody flows (Arkham), not Foundation selling. [`0xf7ff…8c27`](https://intel.arkm.com/explorer/address/0xf7ff52b4acc7db559b6e7427e19ce47a08e98c27) (1.73M EWT on Etherscan) has no market-maker or Foundation label on Arkham. The [Energy Bridge](https://intel.arkm.com/explorer/address/0x5dded30f8cd557257ccdc4a530cb77ac45f0259d) shows **"No transfers match these filters"** on Arkham, so no Arkham view of its flows. EWX-side treasury and Foundation accounts were not tested.

**What it means:** Nothing incriminating found, but the main wallets are unknown. **5**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from KuCoin EWT/USDT daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- Cap 100M; 83.26M frozen at the Zurich fork (6 Aug 2025); "headroom ~16.74M EWT that can only be minted via on-chain governance" ([FAQ](https://docs.energyweb.org/energy-web-x-upgrade-faq)).
- **On-chain reality:** 14 mints of 192,307.69 EWT to the Energy Bridge between 11 Oct 2025 and 20 Oct 2026 (e.g. [Oct 2025](https://etherscan.io/tx/0x03c681c97bde123247110326d6f6a4dcef96255b139b14f156b0fa31da327539), [Oct 2026](https://etherscan.io/tx/0x8bdc0033460e37d219c37efae1fdb09eef1dc5aa90f2fa59a10e910aaafd0104)). That is ~2.5M a year (~3%), and 14.04M of headroom is left. Which referendum approved it was not found [Unverified].

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $246k of 24h volume on a $20.3M cap (1.2% turnover), mostly on KuCoin; no Binance listing.
- −98.9% from ATH, −67% in a year.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Delivered: Zurich fork (Aug 2025), ERC20 and Energy Bridge (Sep 2025), NPoS on EWX (Oct 2025), exchange migration (Jul 2026; [Kraken notice](https://support.kraken.com/articles/ewt-migration)). VCC enterprise rollout "will be provided soon" [Tier A FAQ].

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- $51k TVL on the old chain ([DefiLlama chains](https://api.llama.fi/v2/chains)); only 1,208 holders of the new ERC20. Enterprise users are not quantified.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found in this pass. The Ethereum ↔ EWX bridge holds 67.6M EWT, which is a concentration risk.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. The FAQ says VCC staking "does not confer ownership, revenue rights, nor does it guarantee yield".

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Every ~4 weeks | 192,308 EWT mint (next due about mid-Nov 2026) |
| TBA | VCC enterprise rollout; permissionless collators |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟢 None found (Foundation wallets unknown) |
| Live mint path | 🔴 ~2.5M EWT a year, minted monthly |
| Treasury in single-key wallets | 🟡 Unknown |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Unattributed 3-of-N Safe | Unknown | Etherscan | low | no | Selling stays 5 |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API: EWT ERC20 mint logs (Transfer from 0x0) and `tokentx` for the Safe and top EOAs, read 16 Nov 2026 ~9:10 AM MST; Ethereum RPC `getThreshold()`, `getOwners()`
- [Tier A] Blockscout (Ethereum and Energy Web Chain explorers): holders, supply, bridge contracts
- [Tier A] [Energy Web upgrade FAQ](https://docs.energyweb.org/energy-web-x-upgrade-faq) · [Kraken migration notice](https://support.kraken.com/articles/ewt-migration)
- [Tier B] [EW chain paper (2019 allocation)](https://academy.bit2me.com/wp-content/uploads/2022/03/TheEnergyWebChain-v2-FINAL.pdf) · [Crypto Adventure review](https://cryptoadventure.com/energy-web-review-2026-ewt-ewx-and-blockchain-infrastructure-for-the-energy-transition/)
- [Tier A] DefiLlama `energyweb` fees/revenue; CoinGecko `energy-web-token` (16 Nov 2026 8:20 AM MST); KuCoin EWT-USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): EnergyBridge proxy (no transfers shown), generic Safe, Bitcoin Suisse Deposit and Hot Wallet labels. Arkham does not cover Energy Web X
- [Unverified] The referendum behind the monthly mints; Foundation and EWX treasury balances; enterprise revenue

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Genesis mint of 83.26M ERC20 EWT, 11 Sep 2025 | [tx](https://etherscan.io/tx/0xee122c867c7bda420eebbc84ccb656fb3935eb08b585efe0db1ae09c4b2b3fbe) | A | 16 Nov 2026 |
| Monthly 192,307.69 EWT mints | [Oct 2025](https://etherscan.io/tx/0x03c681c97bde123247110326d6f6a4dcef96255b139b14f156b0fa31da327539) · [Oct 2026](https://etherscan.io/tx/0x8bdc0033460e37d219c37efae1fdb09eef1dc5aa90f2fa59a10e910aaafd0104) | A | 16 Nov 2026 |
| Cap 100M, 16.74M headroom, "no automatic inflation" | [FAQ](https://docs.energyweb.org/energy-web-x-upgrade-faq) | A | 16 Nov 2026 |
| Safe → KuCoin deposit, Oct 2026 | [65k](https://etherscan.io/tx/0xacfe6cfb1e95c24ec6f68d0e335eeb2d8497e1aec8eaa9bac78acec808bf9887) · [100k](https://etherscan.io/tx/0x07a459e8defde9ba9be2cc09d8664baff3be274c8115a93f0cc3aedad16c94b6) | A + B tag | 16 Nov 2026 |
| $17 fees, $0 revenue | [DefiLlama](https://api.llama.fi/summary/fees/energyweb?dataType=dailyFees) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who signs the 3-of-5 Safe** | Arkham (16 Nov 2026) shows a generic Safe with no entity. Ask Energy Web whether it is a Foundation or market-maker wallet [Unverified] | Free |
| 2 | **What authorises the monthly 192k mint?** | Find the EWX referendum, or ask Energy Web | Free |
| 3 | **Foundation and EWX treasury wallets** | Pull EWX treasury and Foundation accounts from energywebx.subscan.io (API key) and pump-test them | Free API key |
| 4 | **Enterprise / VCC revenue** | Ask Energy Web for VCC client fee totals | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.

## Nansen-month findings, 24 Nov 2026 (MST) — reported only, unscored

This appendix publishes findings from the desk's 24 Nov 2026 holder and treasury research. It does not change the v3 score, badge, gates, formula or `revenue_reaches_holders`. Labels marked **Nansen-labeled** come from one third-party labeler and are treated as leads. Under process rule P12, every Nansen balance or holder figure used here was checked against a direct on-chain read before use, and mismatches were discarded. Hypotheses are labelled **Unverified**. Times are MST.

### Holder mix (top 100 holders)
- Exchange share of the top 100 holders: **12.56%** of supply in Nansen-labeled exchange and DEX-pool wallets (Nansen holders pass, 24 Nov 2026).
- Issuer and other named holders: No issuer wallet identified in the top 10. Uniswap pools hold 5.35% and 4.40%. 24.1% of the top 100 is unlabeled.
- Checked on-chain: `balanceOf` / `totalSupply` read on each wallet named above (public Ethereum RPC), 24 Nov 2026, about 4:35 AM MST; every figure matched. The exchange share itself is Nansen's top-100 sum and was checked on-chain only through its largest wallets.
- Unscored: this line has no effect on the score, badge or ranking. Labels are Nansen's (a third-party labeler) and are leads, not confirmed ownership.
