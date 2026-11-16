---
ticker: ZKJ
name: Polyhedra Network
chain: bsc
contract: "0xc71b5f631354be6853efe9c3ab6b9590f8302e81 (Ethereum and BNB Chain)"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 5
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 5
  adoption_customers: 3
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "no protocol exploit found; Jun 2025 price crash (outside window) blamed by the team on a liquidity attack"
  mint_path_live: "no new minting; 670M of 1B unlocked, ~30.1M a month still unlocking"
  team_wallet_to_exchange_during_pump: "no: a wallet line receiving 2,083,333 ZKJ a month (matches the 100M/48-month core-contributor schedule) sent each tranche to OKX; other large holders sent to OKX, Bitvavo and Gate; none on an OKX pump day"
  entity_concentration: "unlocking allocations still 330M (33%)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "No fee, buyback or burn data is published and the 2025 buybacks are not documented as ongoing, so revenue does not reach holders."
pump_day_price_source: "OKX ZKJ-USDT UTC daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xe43470280fdceb239972d1c52fea0e483ef1b6d8"
    label: "Polyhedra Network: Core Contributors (Team Wallet)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham + on-chain 100M allocation"
  - address: "0x36e2d9f03a3a241603ea5da62d0490a01ea43816"
    label: "OKX Blockdream Ventures"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xdb1a99d729c6fc9039b0a7a2ad424305684cee12"
    label: "Polyhedra reserves (Ecosystem; Foundation; Community)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham"
  - address: "0x8caebe5a5895b5101824b1cd0277d905e82dd988"
    label: "Polyhedra reserves (Ecosystem; Foundation; Community)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham"
  - address: "0xb8332a9b674b78f014c7b0d821f8085d79194d58"
    label: "Polyhedra reserves (Ecosystem; Foundation; Community)"
    confidence: high
    independent_corroboration: true
    basis: "Arkham"
  - address: "0x15da7556d5ed888306839bed06f868aeaedcb0d7"
    label: "Revolut: Cold Wallet"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
  - address: "0xcea70aeeac112d2c63d789f9330653906c50bcc4"
    label: "Coinbase Prime Custody (Bitvavo deposit tag)"
    confidence: medium
    independent_corroboration: false
    basis: "Arkham"
price_usd: 0.00376029
price_source: "CoinGecko, 16 Nov 2026 ~10:05 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZKJ · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** Polyhedra builds zkBridge and the EXPchain network, and ZKJ is its fee and staking token. The token crashed more than 80% in June 2025 in what the team called a liquidity attack. It has since fallen another ~99%, to about $0.004. Binance delisted its futures in April 2026. About 30M ZKJ still unlocks every month to buyers, the ecosystem and the team. One wallet line receiving exactly the core-contributor monthly amount sends each tranche to OKX. No fee revenue reaches holders. The revenue gate fails.

**🚨 Top warning:** **monthly insider supply going to exchanges.** A wallet line from `0xe434…b6d8` (40M ZKJ) receives **2,083,333 ZKJ a month**. That matches the core-contributor schedule of 100M over 48 months. Each tranche goes on to OKX: 21 Mar, 27 Apr, 25 May and 30 Jun 2026 ([tx](https://etherscan.io/tx/0x6f116a2e129da944f7e48a76818f163e37ecdd3be5ea5cfbbfd045c7cca433af), status 1). About 30.1M ZKJ a month keeps unlocking until 2030 ([Blockworks unlocks](https://app.blockworks.com/projects/polyhedra-network/token-unlocks)). That's ~54% of the current float a year. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZKJ · Polyhedra Network · 3.8 / 10 · ❌ FAIL

> **One line:** A crashed ZK-infrastructure token with no fee capture and steady unlock selling.

| 📊 Market (CoinGecko, 16 Nov 2026 ~10:05 AM MST) | 🔗 Chain (Etherscan) |
|---|---|
| **Price** $0.00376 | **Supply** 669.9M unlocked of 1B |
| **24h / 7d / 30d** 🔴 −5.6% / 🔴 −21.2% / 🔴 −32.6% | **Unlocks** ~30.1M a month (buyers, ecosystem, community, foundation, team) |
| **Market cap** $2.52M · **FDV** $3.76M | **Top Ethereum holders** 141M, 93M, 73M, 65M, 58M (unlabelled) |
| **24h volume** ~$0.15M on ZKJ pairs (OKX $42k, Bitunix $69k, Ourbit, PancakeSwap). The Phemex and WEEX "ZK" pairs CoinGecko lists are likely another token | |
| **ATH** $4.01 (19 Mar 2024) · now −99.9% | |
| **Pump days** 22 in the last year (OKX ZKJ-USDT; largest +54.6% on 28 Apr 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- ZKJ pays for zkBridge, proof services and EXPchain gas ([tokenomics](https://polyhedra.foundation/tokenomics)), but no fee, buyback or burn data is published. The buybacks promised in 2025 aren't documented as ongoing. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** No fee, buyback or burn data is published and the 2025 buybacks are not documented as ongoing, so revenue does not reach holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- A well-funded company (Polychain-led round). The team blamed the Jun 2025 crash on others and injected $30M of liquidity ([CoinDesk](https://www.coindesk.com/tech/2025/06/17/polyhedra-blames-liquidity-attacks-for-sudden-80-price-drop-in-zkj-promises-buyback), [The Block](https://www.theblock.co/news/markets/2025-06-16-polyhedra-buybacks-coming-after-token-crash-attack-358442)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

- Allocation: ecosystem 32%, buyers 28%, community 15%, foundation 15%, core contributors 10%. About 330M is still locked.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

- I traced the bridge minter and the top eight holders two hops out, for transfers of 2M ZKJ or more. 12 deposits in the window: the core-contributor-sized monthly tranches to OKX, 6.0M and 5.5M to OKX from the `0x15da…` line (14 Jan, 2 Jul), 33.7M to Bitvavo from `0xcea7…` (Jun–Sep), and 2M to Gate (21 Sep). All have status 1, and none fell on an OKX pump day. The vesting is disclosed → **5.**
- **Arkham (16 Nov 2026)** labels [0xe434…b6d8](https://intel.arkm.com/explorer/address/0xe43470280fdceb239972d1c52fea0e483ef1b6d8) **Polyhedra Network: Core Contributors** (Team Wallet tag). Etherscan shows it sending 20M ZKJ on 19 Aug, 19 Sep and 20 Oct 2026 to [OKX Blockdream Ventures 0x36e2…3816](https://intel.arkm.com/explorer/address/0x36e2d9f03a3a241603ea5da62d0490a01ea43816), an investment arm rather than an exchange deposit, which splits each batch into many small vesting-sized payments (e.g. 208,334, 166,667, 20,834) and sends some to OKX and Gate deposits (1.875M to a Gate deposit on 20 Oct). None of those dates is a pump day on OKX ZKJ-USDT closes (19 Aug −2.0%, 19 Sep −1.5%, 20 Oct +2.0%, 4 Nov −0.4%). Arkham also labels the reserves [Ecosystem and Network Incentives](https://intel.arkm.com/explorer/address/0xdb1a99d729c6fc9039b0a7a2ad424305684cee12) (93.2M), [Foundation Reserves](https://intel.arkm.com/explorer/address/0x8caebe5a5895b5101824b1cd0277d905e82dd988) (73.4M) and [Community, Airdrop, and Other Activities](https://intel.arkm.com/explorer/address/0xb8332a9b674b78f014c7b0d821f8085d79194d58) (65.3M), none with exchange activity in 30 days. Two lines in the trace above are exchanges, not insiders: [0x15da…e0d7](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) is **Revolut: Cold Wallet** and [0xcea7…bcc4](https://intel.arkm.com/explorer/address/0xcea70aeeac112d2c63d789f9330653906c50bcc4) is **Coinbase Prime Custody** (Bitvavo deposit tag). The score stays **5**. [Tier B] Arkham, read 16 Nov 2026 (signed-in account).

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from OKX ZKJ-USDT UTC daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- About 30.1M a month unlocks until 2030, ~54% of the float a year at today's float.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- About $0.15M a day on ZKJ pairs. Binance delisted the perpetual in Apr 2026 [Tier B]. The 99.9% drawdown leaves little depth.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- zkBridge, Expander proof system, and EXPchain ([Polyhedra blog](https://blog.polyhedra.network/polyhedra-moving-into-2026/)).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- zkBridge is used, but no 2026 fee figures.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No protocol exploit found in the window.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- EXPchain mainnet, and continued unlocks.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 No protocol exploit in window (Jun 2025 market crash outside) |
| Team wallet → exchange during a pump | 🟢 No: vesting-sized deposits, none on pump days |
| Live mint path | 🟡 No minting, but ~30M a month unlocking |
| Entity concentration | 🟡 ~33% still locked |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [0xe434…b6d8](https://intel.arkm.com/explorer/address/0xe43470280fdceb239972d1c52fea0e483ef1b6d8) | Polyhedra Network: Core Contributors (Team Wallet) | Arkham + on-chain 100M allocation | high | yes (on-chain allocation matches the published schedule) | Selling: team line confirmed; no pump-day deposit |
| [0x36e2…3816](https://intel.arkm.com/explorer/address/0x36e2d9f03a3a241603ea5da62d0490a01ea43816) | OKX Blockdream Ventures | Arkham | medium | no | None (distributor, not an exchange deposit) |
| [0xdb1a…ee12](https://intel.arkm.com/explorer/address/0xdb1a99d729c6fc9039b0a7a2ad424305684cee12), [0x8cae…d988](https://intel.arkm.com/explorer/address/0x8caebe5a5895b5101824b1cd0277d905e82dd988), [0xb833…4d58](https://intel.arkm.com/explorer/address/0xb8332a9b674b78f014c7b0d821f8085d79194d58) | Polyhedra reserves (Ecosystem; Foundation; Community) | Arkham | high | yes (allocation sizes match the published tokenomics) | Holdings: confirms reserve buckets |
| [0x15da…e0d7](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) | Revolut: Cold Wallet | Arkham | medium | no | Removes an insider candidate |
| [0xcea7…bcc4](https://intel.arkm.com/explorer/address/0xcea70aeeac112d2c63d789f9330653906c50bcc4) | Coinbase Prime Custody (Bitvavo deposit tag) | Arkham | medium | no | Removes an insider candidate |

## 📚 Sources

- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): the Core Contributors, Ecosystem, Foundation Reserves and Community wallets, OKX Blockdream Ventures, and two exchange wallets; dates from Etherscan
- [Tier A] [Polyhedra tokenomics](https://polyhedra.foundation/tokenomics), [Polyhedra: moving into 2026](https://blog.polyhedra.network/polyhedra-moving-into-2026/)
- [Tier B] [CoinDesk, 17 Jun 2025](https://www.coindesk.com/tech/2025/06/17/polyhedra-blames-liquidity-attacks-for-sudden-80-price-drop-in-zkj-promises-buyback), [The Block, 16 Jun 2025](https://www.theblock.co/news/markets/2025-06-16-polyhedra-buybacks-coming-after-token-crash-attack-358442), [Blockworks unlocks](https://app.blockworks.com/projects/polyhedra-network/token-unlocks), [Binance futures delisting record](https://cryptolisting.ws/listings/binance-futures-delisting-zkj-2026-04-23/)
- [Tier A] Etherscan transfers and holders for `0xc71b…2e81`
- [Tier A] CoinGecko `polyhedra-network` (market, venues); pump days from OKX ZKJ-USDT daily closes

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Monthly 2,083,333 ZKJ → OKX | [21 Mar](https://etherscan.io/tx/0xc9d15d51dcabaff038716a403bd052a5f76ac4500a9972e9a82e59f449fad952), [27 Apr](https://etherscan.io/tx/0x2b50d316288f948db9a3a6a5595628f9cdc76add518a91d9a7ac682b414413cc), [25 May](https://etherscan.io/tx/0x9a0544d86143d0ab842ce511ced6e95704a5e154307308c5f28798956ff9eeea), [30 Jun](https://etherscan.io/tx/0x6f116a2e129da944f7e48a76818f163e37ecdd3be5ea5cfbbfd045c7cca433af) | A | 16 Nov 2026 |
| 6.0M ZKJ → OKX, 14 Jan 2026 | [tx](https://etherscan.io/tx/0x60fbff838d9c8818bf4e29b8f3b40c44e81eadf093089538e6f72e2baf9c7b40) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who receives the Core Contributors batches after OKX Blockdream Ventures** | Arkham (16 Nov 2026) confirms the Core Contributors label; trace the small onward payments | Free |
| 2 | **BNB Chain side** (the main venue) | BscScan API needs a paid tier | Arkham |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
