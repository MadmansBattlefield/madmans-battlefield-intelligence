---
ticker: XDB
name: XDB CHAIN (formerly DigitalBits)
chain: xdb-chain
contract: "native (XDB CHAIN, a Stellar-core fork)"
overall_score: 2.9
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 5
  selling_behavior: 3
  tokenomics_supply: 6
  liquidity_market: 1
  product_development: 3
  adoption_customers: 2
  security_audits: 4
  regulatory: 4
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none found in the review window"
  mint_path_live: "no: native supply fixed; 80B hard-burned at the outset, quarterly burns since"
  team_wallet_to_exchange_during_pump: "yes (pattern): the disclosed treasury funded a wallet that sent all 95.5M XDB to memo-tagged exchange-pattern deposit addresses, 5 deposits (6.5M) on pump days; exchange label [Unverified]"
  treasury_in_single_key_wallet: "yes: the disclosed treasury (1.57B XDB) is controlled by one master key"
price_usd: 0.00005306
price_source: "CoinGecko, 16 Nov 2026 7:33 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XDB · Overall grade **2.9 / 10 · ❌ FAIL**

**Summary:** XDB CHAIN is the 2023 rebrand of the DigitalBits blockchain, a Stellar-core fork marketed for "branded tokens" and real-world assets. The chain earns essentially nothing: the **entire network fee pool is 14.25 XDB** (under one tenth of a cent). Trading is down to **~$14k a day** on two exchanges, and the price is **−99.99% from its 2021 high**. The foundation's own disclosed treasury sent **95.6M XDB** to a fresh wallet on 30 Jan 2026, and that wallet then passed **all of it** to memo-tagged deposit addresses in small, regular tranches, five of them on pump days. Revenue and Selling both trip the hard gates.

**🚨 Top warning:** treasury coins went straight to exchange-pattern deposits. The disclosed treasury [`GBMOHKO3…R222`](https://horizon.livenet.xdbchain.com/accounts/GBMOHKO3CVEJSMUXCJ3WZR5DIZAL33LVLH7CRRXLMV5X655WHPS5R222) sent [95.6M XDB](https://explorer.xdbchain.com/transaction/d07aca29741401e6f1d680dbb13d2e46328abb512b1702a977704bcc93f9f54a) to [`GDMLQS4L…YT4N`](https://horizon.livenet.xdbchain.com/accounts/GDMLQS4LURVQ73JU27OAMLVG6EGLLJSOC5USBRAUUQ6VK5445JW3YT4N) on 30 Jan 2026. That wallet sent 56.1M in 12 transfers on 11 Feb to [`GDXOD6WU…DKMA`](https://horizon.livenet.xdbchain.com/accounts/GDXOD6WUOZWUYVTNO5RGIHPQVLXEFDH56GWQILQ5S2I75QLR6TFEDKMA), then 39.4M in 25 weekly-style transfers (Mar–Aug 2026), all with the same memo, to [`GAO6XKBJ…R5UA`](https://horizon.livenet.xdbchain.com/accounts/GAO6XKBJKJIK6BAH3UOV6UA5LDOJ4PLZXZDOQ45XDAOUIMKIMLTNR5UA). That address holds 1.08B XDB and takes memo-tagged deposits from many senders, the pattern of an exchange hot wallet [Unverified label]. Five of those transfers (6.5M) landed on pump days, e.g. [1.76M on 27 Apr 2026](https://explorer.xdbchain.com/transaction/cd12545e768e5ffe5887cde1452adb598af91df5798596c8079d4cafc0fe333f). No sale was announced. The dollar amounts are small (~$14k in total) because the coin is nearly worthless. Every link is in the 🔗 Evidence trail below.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 5/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL (hard gate) |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XDB · XDB CHAIN · 2.9 / 10 · ❌ FAIL

> **One line:** A near-idle Stellar fork with no fee income, ~$14k of daily volume, and a treasury that fed exchange deposits.

| 📊 Market (CoinGecko, 16 Nov 2026 7:33 AM MST) | 🔗 On-chain ([Horizon](https://horizon.livenet.xdbchain.com/), 16 Nov 2026 ~7:44 AM MST) |
|---|---|
| **Price** $0.00005306 | **Latest ledger** 18,763,313 (stellar-core 19.7.0) |
| **24h / 7d / 30d** 🔴 −3.6% / −4.8% / −22.3% · 1y −86.4% | **Network fee pool** 14.25 XDB (all fees ever collected, not burned) |
| **Market cap** $905k · **FDV** $996k | **Supply** 20B max · 18.74B total · 17.13B circulating (network paper) |
| **24h volume** $13.96k (KuCoin $13.1k, Gate $0.9k) | **Treasury** 1,573,086,063 XDB on one key |
| **ATH** $0.8507 (21 Nov 2021) · now −99.99% | **Activity** ~29 successful transactions in 200 ledgers (~17 min) ≈ 2,500 a day |
| **Pump days, last 365 days** 69 (CoinGecko daily closes; largest +380% on 26 Mar 2026) | **Burn address** 1,264,163,370 XDB, keys disabled |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Network fees collected, all time | **14.25 XDB** (≈ $0.0008) | [Tier A] [Horizon latest ledger `fee_pool`](https://horizon.livenet.xdbchain.com/ledgers?order=desc&limit=1) |
| Protocol revenue to holders | **$0** | No DefiLlama listing; no fee switch |

**What it means:** Fees are near zero and no business revenue flows to the token. Burns are funded by "Branded Coin" projects pledging part of their own tokens, which in Jan 2026 had to be sold OTC "in light of lack of liquidity" ([XDB news, Burn Event #7](https://xdbchain.com/news/)). **1 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

- The DigitalBits Foundation became the **XDB Foundation** when the chain was rebranded on 4 Oct 2023 ([rebrand release](https://chainwire.org/2023/10/04/digitalbits-blockchain-evolves-into-xdb-chain-a-game-changing-rebranding-initiative/), Tier B). The network relaunched with the passphrase "LiveNet Global XDBChain Network ; November 2023" ([Horizon root](https://horizon.livenet.xdbchain.com/)).
- News releases are datelined Dublin, Ireland and quote the founder by role. No audited accounts or team-wallet disclosure beyond the treasury and burn addresses were found.
- The DigitalBits brand carried a 2022 sponsorship-payment dispute with a European football club [Unverified: not checked against court records this session].

## 🪙 Foundation / team holdings — How many coins do they hold? · 5/10 · ❌ FAIL

- **Treasury:** 1,573,086,063 XDB (8.4% of total supply) at [`GBMOHKO3…R222`](https://horizon.livenet.xdbchain.com/accounts/GBMOHKO3CVEJSMUXCJ3WZR5DIZAL33LVLH7CRRXLMV5X655WHPS5R222). The [network paper](https://xdbchain.com/network-paper/) listed 1,609,599,838 in Aug 2026, so ~36.5M has left since.
- The account has **one signer (its master key, weight 1) and all thresholds at 0**, so one key moves the whole treasury.
- No other foundation or team wallets are disclosed. Horizon has no rich list, so other insider holdings are **Not found**.

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL (hard gate)

| Date (MST) | Flow | Amount (XDB) | Evidence |
|---|---|---:|---|
| 30 Jan 2026 3:11 AM | Treasury → `GDMLQS4L` (fresh-funded wallet) | 95,600,000 | [tx](https://explorer.xdbchain.com/transaction/d07aca29741401e6f1d680dbb13d2e46328abb512b1702a977704bcc93f9f54a) |
| 11 Feb 2026 8:12–11:19 AM | `GDMLQS4L` → `GDXOD6WU` (12 transfers of 3.8–5.5M) | 56,076,000 | e.g. [3.75M](https://explorer.xdbchain.com/transaction/d5e75c3edc17dfc83fd273c811de49fe1849f10259b2d6a636ffe04e7ca3a4ee) · [5.46M](https://explorer.xdbchain.com/transaction/ddd6b3cec6e5aeb2f7da43b1cff06d59d215fbcce756ff04042a70a96ed9c9da) |
| 4 Mar – 30 Aug 2026 | `GDMLQS4L` → `GAO6XKBJ`, 25 transfers, same memo every time | 39,442,000 | e.g. [2.0M on 30 Aug](https://explorer.xdbchain.com/transaction/74d75289c5a8a1d2a17cf96a240a1978f9dc654299e4ca37e0cba845450d80b6) |
| 4 Mar, 19 Mar, 22 Apr, 24 Apr, 27 Apr 2026 (pump days: +17%, +10%, +31%, +14%, +14% vs 5 days earlier) | of which on pump days | 6,525,000 | [4 Mar](https://explorer.xdbchain.com/transaction/87c73ec798ec4b3830f196d3fd49784b57abc6c2e3d5bdca75f527cb0def1002) · [19 Mar](https://explorer.xdbchain.com/transaction/6ff8699ba3a3d7eab321e1ee5840c1ffd84927d09cd32a1f67a983cd177694fd) · [22 Apr](https://explorer.xdbchain.com/transaction/d90fb8090c01589f83380e4445c40f45881d2e335858395e464b10fb21dd277b) · [24 Apr](https://explorer.xdbchain.com/transaction/4f670b45cd25d0ac36bc5bff39bfcc05b80ccdba85c4da005c293006b2dfa18c) · [27 Apr](https://explorer.xdbchain.com/transaction/cd12545e768e5ffe5887cde1452adb598af91df5798596c8079d4cafc0fe333f) |

- `GDMLQS4L` sent out **95.52M of the 95.6M** it received; it now holds 82k XDB. At daily closes the flow was worth only ~$14k.
- `GAO6XKBJ` holds **1.08B XDB** and its recent transactions carry many different deposit memos ("0", "12345", "test" and others) from many senders, which is what a centralized-exchange deposit wallet looks like. `GDXOD6WU` also takes numeric text memos from several senders. **Neither is labelled** on a public explorer, so the exchange attribution is [Unverified].
- The treasury also sent 61.0M on [14 Mar 2024](https://explorer.xdbchain.com/transaction/265a1351dae1597a60eb840143c188a4162c3711331194b825b54e101168b0a2) to a wallet that split it into hundreds of small payments (distribution-style), and 21.6M on [28 Oct 2026](https://explorer.xdbchain.com/transaction/6d4e4445048e40afda842c392581feabadec53d5ce75853c38888a03ae45c118) to `GACZS4QX…` (still holds 22.8M; it had already sent 5.9M to `GAO6XKBJ` in Oct).
- **Score 3:** a disclosed treasury key funded a wallet that fed one exchange-pattern deposit stream for seven months, including pump days, with no announcement. The amounts are small, and the exchange label is not confirmed.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- 100B created at genesis; 80B hard-burned to a key-disabled address ([network paper](https://xdbchain.com/network-paper/)). Max supply 20B; total 18.74B after 1.264B more sits at the [burn address](https://horizon.livenet.xdbchain.com/accounts/GC7GH763TKNVOWOOLOZR4ZYHHDSJIYJPP746ZFNEQZLJHB244WBBBBRN) (master weight 0, so it can never send). The ledger header still prints `total_coins` 100,000,000,000.
- No inflation. Branded Coins pledge up to 2.5% of their supply to quarterly XDB burns (Burn Event #7 on 4 Jan 2026 burned 12.2M).

## 💧 Liquidity & market · 1/10 · ❌ FAIL

- $13.96k of 24h volume on two venues (KuCoin, Gate) against a $905k cap. A single $5k order would move the price. 69 pump days in a year shows a thin, swingy book.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- The network runs **stellar-core 19.7.0**, several major versions behind upstream Stellar. Product news is partnership-led (an Alchemy Pay on-ramp on the DEX, Jan 2026) rather than shipped protocol work.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- About 2,500 successful transactions a day (29 in a 17-minute sample) and no DefiLlama TVL listing. Branded Coin burns show the sponsors' own tokens could not find buyers.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- No exploit found. The treasury on a single key and the outdated core version are the main risks. No recent public audit found.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- The foundation's releases are datelined Dublin, Ireland (registration not checked). No enforcement found against XDB itself. The DigitalBits-era disputes are [Unverified] here.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Quarterly | Branded Coin burn events (next after Burn Event #7, date not published) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🔴 Treasury-funded wallet → exchange-pattern deposits on 5 pump days (label [Unverified]) |
| Live mint path | 🟢 None (fixed native supply) |
| Treasury in a single-key wallet | 🔴 Yes, 1.57B XDB |

## 📚 Sources

- [Tier A] XDB CHAIN Horizon API: root, latest ledger, `/accounts/{id}` for the treasury, burn address and recipients, `/accounts/{id}/payments` and `/transactions/{hash}`; read 16 Nov 2026 ~7:40–7:50 AM MST. Every linked transaction returned `successful: true`
- [Tier A] [XDB CHAIN network paper](https://xdbchain.com/network-paper/) (supply definitions, treasury and burn addresses); [XDB CHAIN news](https://xdbchain.com/news/) (Burn Event #7, Alchemy Pay)
- [Tier B] [Rebrand release, 4 Oct 2023](https://chainwire.org/2023/10/04/digitalbits-blockchain-evolves-into-xdb-chain-a-game-changing-rebranding-initiative/)
- [Tier A] CoinGecko `digitalbits` (16 Nov 2026 7:33 AM MST) for price, volume, venues and 365-day closes used for pump days
- [Tier B] Arkham, network list read 16 Nov 2026 ~7:35 AM MST (signed-in account): **XDB CHAIN is not supported.** Arkham's network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. No Arkham labels were available for this report

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Fee pool 14.25 XDB | [latest ledger](https://horizon.livenet.xdbchain.com/ledgers?order=desc&limit=1) | A | 16 Nov 2026 |
| Treasury 1.57B XDB, one key | [account](https://horizon.livenet.xdbchain.com/accounts/GBMOHKO3CVEJSMUXCJ3WZR5DIZAL33LVLH7CRRXLMV5X655WHPS5R222) · [paper](https://xdbchain.com/network-paper/) | A | 16 Nov 2026 |
| Burn address 1.264B, keys disabled | [account](https://horizon.livenet.xdbchain.com/accounts/GC7GH763TKNVOWOOLOZR4ZYHHDSJIYJPP746ZFNEQZLJHB244WBBBBRN) | A | 16 Nov 2026 |
| Treasury → `GDMLQS4L` 95.6M | [tx](https://explorer.xdbchain.com/transaction/d07aca29741401e6f1d680dbb13d2e46328abb512b1702a977704bcc93f9f54a) | A | 16 Nov 2026 |
| `GDMLQS4L` payments (all 95.5M out) | [payments](https://horizon.livenet.xdbchain.com/accounts/GDMLQS4LURVQ73JU27OAMLVG6EGLLJSOC5USBRAUUQ6VK5445JW3YT4N/payments?order=asc&limit=200) | A | 16 Nov 2026 |
| Pump-day deposits to `GAO6XKBJ` | [4 Mar](https://explorer.xdbchain.com/transaction/87c73ec798ec4b3830f196d3fd49784b57abc6c2e3d5bdca75f527cb0def1002) · [19 Mar](https://explorer.xdbchain.com/transaction/6ff8699ba3a3d7eab321e1ee5840c1ffd84927d09cd32a1f67a983cd177694fd) · [22 Apr](https://explorer.xdbchain.com/transaction/d90fb8090c01589f83380e4445c40f45881d2e335858395e464b10fb21dd277b) · [24 Apr](https://explorer.xdbchain.com/transaction/4f670b45cd25d0ac36bc5bff39bfcc05b80ccdba85c4da005c293006b2dfa18c) · [27 Apr](https://explorer.xdbchain.com/transaction/cd12545e768e5ffe5887cde1452adb598af91df5798596c8079d4cafc0fe333f) | A | 16 Nov 2026 |
| `GAO6XKBJ` holds 1.08B, many memo deposits | [account](https://horizon.livenet.xdbchain.com/accounts/GAO6XKBJKJIK6BAH3UOV6UA5LDOJ4PLZXZDOQ45XDAOUIMKIMLTNR5UA) · [transactions](https://horizon.livenet.xdbchain.com/accounts/GAO6XKBJKJIK6BAH3UOV6UA5LDOJ4PLZXZDOQ45XDAOUIMKIMLTNR5UA/transactions?order=desc&limit=50) | A | 16 Nov 2026 |
| Treasury 28 Oct 2026 21.6M | [tx](https://explorer.xdbchain.com/transaction/6d4e4445048e40afda842c392581feabadec53d5ce75853c38888a03ae45c118) | A | 16 Nov 2026 |
| Burn Event #7, CBPAY sold OTC | [XDB news](https://xdbchain.com/news/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Which exchange owns `GAO6XKBJ` and `GDXOD6WU`** | Compare with the XDB deposit address shown in a KuCoin and a Gate account (XDB deposit page), using the addresses linked in this report | Free (exchange login) |
| 2 | **Who controls `GDMLQS4L` and `GACZS4QX`** | Ask the XDB Foundation to disclose treasury disbursements; check the network paper for updates | Free |
| 3 | **Other insider wallets** | Horizon has no rich list; ask the foundation or use a third-party XDB indexer | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
