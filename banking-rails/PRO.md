---
ticker: PRO
name: Propy
chain: ethereum
contract: "0x226bb599a12c826476e3a771454697ea52e9e220 (Ethereum); 0x18dd5b087bca9920562aff7a0199b96b9230438b (Base)"
overall_score: 4.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 4
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no: 100M fully issued in 2017"
  team_wallet_to_exchange_during_pump: "not proven: wallets funded from the 2017 sale contract moved ~17.0M PRO (~$5.1M) to Coinbase Prime on 1 Jan 2026, three days before a +52.9% run; not a pump day, and Coinbase Prime can be custody"
  entity_concentration: "yes: issuer held ~29M PRO (29%) per its Aug 2025 MiCA white paper"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "PRO does not represent an entitlement to revenue distribution, and revenue-funded buybacks are undocumented, so revenue does not reach holders."
pump_day_price_source: "MEXC PROUSDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x48a3104ad62c4af304734438da83d427e6ed40b1"
    label: "Coinbase Prime Deposit (forwards to Prime hot wallet)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain forwarding"
  - address: "0x3c0f464db20d60b8d94f3c2810529015507daadb"
    label: "Unlabelled or generic tags; no Propy label"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x89f266dba1ef608b4e431c30037f925273da3cb3"
    label: "Unlabelled or generic tags; no Propy label"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x97085a1db3e9a7d94280522d43a547336fde40ef"
    label: "Unlabelled or generic tags; no Propy label"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x97dd39e8a8e4546f94410121b88f77d22aaaebc8"
    label: "Unlabelled or generic tags; no Propy label"
    confidence: low
    independent_corroboration: false
    basis: "Arkham"
  - address: "0x10987d8361338eae4472f107cf069558c54516ae"
    label: "Unlabelled (2017 sale contract per its bytecode and history)"
    confidence: low
    independent_corroboration: false
    basis: "Arkham + Etherscan"
price_usd: 0.257149
price_source: "CoinGecko, 16 Nov 2026 ~9:45 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PRO · Overall grade **4.3 / 10 · ❌ FAIL**

**Summary:** Propy is a US real-estate closing and title company that records deeds on-chain. PRO is used for its services and a staking-style loyalty programme. All 100M tokens were issued in its 2017 sale. Propy's own MiCA white paper says the token carries no right to revenue, and in Aug 2025 Propy still held about 29M. On 1 Jan 2026, wallets funded from the original sale contract moved about 17M PRO to Coinbase Prime, three days before the price ran up 52.9%. The revenue gate fails.

**🚨 Top warning:** **a ~$5.1M issuer-line transfer to Coinbase Prime.** On 1 Jan 2026, four wallets funded (one or two hops) from the 2017 sale contract `0x1098…16ae` sent about **17.0M PRO (~$5.1M)** to a Coinbase Prime address ([tx](https://etherscan.io/tx/0x0ebb0b46e9fb20ca1319c33a3fabd889d3ec1db8ee7bb933df1d19b2ddc3aee2), all status 1). The price then ran up 52.9% by 5 Jan. Coinbase Prime is used for both custody and selling, so this may be a custody move. That's about 59% of what Propy reported holding in Aug 2025 ([MiCA white paper](https://propy.com/home/static/PropyWhitepaper2025.pdf)). Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PRO · Propy · 4.3 / 10 · ❌ FAIL

> **One line:** A working proptech company whose token has no revenue rights and a large issuer stash on the move.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:45 AM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.2571 | **Supply** 100M, fully issued (2017) |
| **24h / 7d / 30d** 🔴 −2.9% / 🔴 −13.2% / 🔴 −29.6% | **Issuer holdings (Aug 2025)** ~19M growth pool, ~4.5M company reserve, ~5M sale pool |
| **Market cap** $25.7M · **FDV** $25.7M | **Top Ethereum holders** many 5–7M wallets funded from Coinbase (custody pattern) |
| **24h volume** $0.22M (CoinUp $189k, Bitunix, Coinbase $62k, MEXC, Gate, HTX, Uniswap) | |
| **ATH** $5.15 (4 Jan 2018) · now −95.0% | |
| **Pump days** 35 in the last year (MEXC PROUSDT; largest +52.9% on 5 Jan 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Propy earns closing and title fees, but PRO "does not represent... entitlement to revenue distribution" ([MiCA white paper](https://propy.com/home/static/PropyWhitepaper2025.pdf)). Revenue-funded buybacks have been talked about but aren't documented [Unverified]. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** PRO does not represent an entitlement to revenue distribution, and revenue-funded buybacks are undocumented, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

- An operating US company with a public executive team and a MiCA filing. A reported $100M credit facility to acquire title companies is [Unverified: one secondary source].

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- In Aug 2025, Propy still held 55% of the 35M growth pool, 30% of the 15M company pool and 15% of the 35M sale pool, about 29M PRO ([MiCA white paper](https://propy.com/home/static/PropyWhitepaper2025.pdf)).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- I traced the sale contract and the top 14 holders two hops out, for transfers of 50k PRO or more. Five deposits in the window, all from wallets funded by the sale contract: 80k to KuCoin on 18 Nov 2025, and ~17.0M to Coinbase Prime on 1 Jan 2026. Neither date is a pump day. The Coinbase Prime move came three days before a +52.9% run, and Coinbase Prime can be custody → **not proven, 4.**
- **Arkham (16 Nov 2026):** the receiving address [0x48a3…40b1](https://intel.arkm.com/explorer/address/0x48a3104ad62c4af304734438da83d427e6ed40b1) is a **Coinbase Prime Deposit**. Every 1 Jan 2026 inflow was forwarded within minutes to Coinbase Prime Hot Wallet [0xcd53…ca7b](https://etherscan.io/address/0xcd531ae9efcce479654c4926dec5f6209531ca7b) (for example 14.86M, [tx](https://etherscan.io/tx/0x7c82eaaabe6137b0eac483c457be8ebc3ca72d332a3cb169637a541bf87f36e9)), which fits custody. The senders carry no Propy label: [0x3c0f…aadb](https://intel.arkm.com/explorer/address/0x3c0f464db20d60b8d94f3c2810529015507daadb) and [0x89f2…3cb3](https://intel.arkm.com/explorer/address/0x89f266dba1ef608b4e431c30037f925273da3cb3) are unlabelled, [0x9708…40ef](https://intel.arkm.com/explorer/address/0x97085a1db3e9a7d94280522d43a547336fde40ef) has only generic tags (OpenSea User, Contract Deployer, MultiSig Deployer) and [0x97dd…ebc8](https://intel.arkm.com/explorer/address/0x97dd39e8a8e4546f94410121b88f77d22aaaebc8) is a "MetaMask User". The 2017 sale contract [0x1098…16ae](https://intel.arkm.com/explorer/address/0x10987d8361338eae4472f107cf069558c54516ae) and the two `MultiSigWalletWithDailyLimit` contracts that funded them are unlabelled. The issuer link rests on 2017–2023 funding hops, not labels, so Selling stays **not proven, 4**. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from MEXC PROUSDT UTC daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- Fixed 100M supply, all issued. About 29% is issuer-held and feeds staking rewards and incentives.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $0.22M a day. Coinbase and MEXC are real venues. The top venue, CoinUp, is not.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Deed recording, address NFTs, title and escrow tools, and an AI escrow agent ([MiCA white paper](https://propy.com/home/static/PropyWhitepaper2025.pdf)).

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Propy claims over $4B in transactions processed [Unverified]. How much on-chain PRO use that drives is unclear.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- A 2017 public token sale. The MiCA white paper is filed.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

- Title-company acquisitions and staking seasons.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (~17M PRO to Coinbase Prime, not a pump day) |
| Live mint path | 🟢 None |
| Entity concentration | 🔴 ~29% issuer-held (Aug 2025) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0x48a3…40b1](https://intel.arkm.com/explorer/address/0x48a3104ad62c4af304734438da83d427e6ed40b1) | Coinbase Prime Deposit (forwards to Prime hot wallet) | Arkham + on-chain forwarding | high | yes (on-chain sweep to the Prime hot wallet) | Supports custody; Selling stays 4 |
| [0x3c0f…aadb](https://intel.arkm.com/explorer/address/0x3c0f464db20d60b8d94f3c2810529015507daadb), [0x89f2…3cb3](https://intel.arkm.com/explorer/address/0x89f266dba1ef608b4e431c30037f925273da3cb3), [0x9708…40ef](https://intel.arkm.com/explorer/address/0x97085a1db3e9a7d94280522d43a547336fde40ef), [0x97dd…ebc8](https://intel.arkm.com/explorer/address/0x97dd39e8a8e4546f94410121b88f77d22aaaebc8) | Unlabelled or generic tags; no Propy label | Arkham | low | no | None |
| [0x1098…16ae](https://intel.arkm.com/explorer/address/0x10987d8361338eae4472f107cf069558c54516ae) | Unlabelled (2017 sale contract per its bytecode and history) | Arkham + Etherscan | low | no | None |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the Coinbase Prime deposit, its senders, the 2017 sale contract and two MultiSigWalletWithDailyLimit contracts; dates from Etherscan
- [Tier A] [Propy MiCA white paper v4.0, Aug 2025](https://propy.com/home/static/PropyWhitepaper2025.pdf), [Staking terms](https://propy.com/browse/staking-terms/)
- [Tier A] Etherscan transfers and holders for `0x226b…e220`
- [Tier B] [CoinMarketCap AI summary (credit facility claim)](https://coinmarketcap.com/cmc-ai/propy/price-prediction/)
- [Tier A] CoinGecko `propy` (market, venues); pump days from MEXC PROUSDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 11.43M PRO → Coinbase Prime, 1 Jan 2026 | [tx](https://etherscan.io/tx/0x0ebb0b46e9fb20ca1319c33a3fabd889d3ec1db8ee7bb933df1d19b2ddc3aee2) | A | 16 Nov 2026 |
| 2.88M PRO → Coinbase Prime, 1 Jan 2026 | [tx](https://etherscan.io/tx/0x8507139a924942f5efc0f123329f5d3a7007a222622e9241ed6608575b9ab972) | A | 16 Nov 2026 |
| 2.15M PRO → Coinbase Prime, 1 Jan 2026 | [tx](https://etherscan.io/tx/0x79db6b08d5725bf825ae3e824f18bffd579b6c2683e9489304d7c0be3aaadff3) | A | 16 Nov 2026 |
| Issuer holdings | [MiCA white paper](https://propy.com/home/static/PropyWhitepaper2025.pdf) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Was the 1 Jan 2026 Coinbase Prime move custody or a sale?** | Arkham (16 Nov 2026): Prime deposit → Prime hot wallet, senders unlabelled. Ask Propy | Free |
| 2 | **Base-chain treasury and staking contract balances** | Basescan (paid tier for API) | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
