---
ticker: XDC
name: XDC Network
chain: xdc
contract: "native (XDC Network, chain id 50)"
overall_score: 3.8
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 5
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none at protocol level (a 2024 application-layer exploit hit third-party CIFI and XSWAP pools)"
  mint_path_live: "yes, by design (uncapped; masternode rewards exceed the EIP-1559 burn)"
  team_wallet_to_exchange_during_pump: "none found (284.7M XDC from the largest reserve wallet reached FalconX in Oct 2022-Feb 2023, all on non-pump days); deeper hops not tested"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "yes (the 12.45B XDC largest address and the other genesis reserve wallets are plain EOAs; the issuer says reserves sit in centralized custody with no published multisig policy)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "The EIP-1559 base-fee burn is automatic on-chain, but it is below masternode rewards and fees are ~$6k a year; Revenue stays 2."
pump_day_price_source: "Gate XDC/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.02921423
price_source: "CoinGecko, 16 Nov 2026 7:13 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XDC · Overall grade **3.8 / 10 · ❌ FAIL**

**Summary:** XDC is an EVM Layer 1 for trade finance and tokenized assets, issued by a Singapore company, XinFin Fintech. It has 108 KYC'd masternodes (many of them regulated institutions), a MiCA white paper and a 21Shares ETP. But the chain earns almost nothing: **$494.62 of fees in 30 days and $6,219 in a year** on DefiLlama, and DeFi TVL is just $1.93M. Supply is uncapped, and the issuer can unlock up to ~700M XDC a year from team and ecosystem reserves. **About 18B XDC (47% of total supply) sits outside circulation in unlabelled single-key wallets**, and the largest of them moved 1B XDC on 29 Oct 2026. The governance DAO was shut down for lack of participation. Revenue trips the hard gate.

**🚨 Top warning:** one unlabelled wallet holds a third of all XDC, and it just started moving. [`0xd778…Fe03a`](https://xdcscan.com/address/0xd77875df9c9de07a5a701f4431743e3a0e9fe03a) holds **12.45B XDC (32.7% of total supply, ≈62% of CoinGecko circulating, ~$364M)**. It was funded with [14.95B on 3 Dec 2020](https://xdcscan.com/tx/0xa73d2795b514243159f4742c76aa5eca5760fbe61acdfd577a085591b2a1a294), close to the 15B "Founders and Team" allocation (attribution [Unverified]). On **29 Oct 2026** it sent 1B XDC (~$29M) to three fresh wallets: [450M](https://xdcscan.com/tx/0x08ea42bb075196000c6c9c56c77ad08e4c650f721741ef8d6c3ffc4e8abd0f3f), [450M](https://xdcscan.com/tx/0xa572f92c956d1373e7a8b0642a72c241364e55e3ed7b79b6a597a400959b8a14) and [100M](https://xdcscan.com/tx/0x6b8eb19c7f81389cb274af13d80727b72a4e32f1c4eeb40e0f70fd18d2511e59). A day earlier, the busy distribution wallet [`0xb0ef…8383`](https://xdcscan.com/address/0xb0ef2a0337a519d50780e33d268341ce75ce8383) had sent each of them a 1-XDC test. Earlier, 284.7M XDC from this wallet went through [`0xb804…ac67`](https://xdcscan.com/address/0xb80432710beb70e5b5b082e5a417c7bb4fb3ac67) to the **FalconX** OTC desk ([110M, 4 Oct 2022](https://xdcscan.com/tx/0xb9d813591165583bdb3adb51aaa58f39d8259d8a2abf8bf5ef3c3bb8e07cf8c8)). The issuer publishes no reserve addresses and no signing policy ([Blockworks TTF](https://blockworks.com/token-transparency/filing/xdc-network)).

**Sections passed: 3 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 5/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 XDC · XDC Network · 3.8 / 10 · ❌ FAIL

> **One line:** Well-credentialed enterprise L1 with institutional validators but almost no fee income, and an issuer that controls about half the supply through unlabelled wallets.

| 📊 Market (CoinGecko, 16 Nov 2026 7:13 AM MST) | 🔗 On-chain (XDC Network, 16 Nov 2026) |
|---|---|
| **Price** $0.02921 | **Total supply** 38.07B · **circulating** 19.95B (CoinGecko) |
| **24h / 7d / 30d** 🟢 +3.1% / 🔴 −1.5% / −11.5% · 1y −45.9% | **Largest address** [`0xd778…Fe03a`](https://xdcscan.com/address/0xd77875df9c9de07a5a701f4431743e3a0e9fe03a) 12.45B (32.7%) |
| **Market cap** $582.7M · **FDV** $1.112B | **Top 10 addresses** 66.5% of supply ([rich list](https://xdcnetwork.org/rich-list/)) |
| **24h volume** $11.09M | **Staked** 3.71B in validator contract [`0x…0088`](https://xdcscan.com/address/0x0000000000000000000000000000000000000088) |
| **ATH** $0.1928 (20 Aug 2021) · now −84.8% | **Fees** $494.62 (30d) · **DeFi TVL** $1.93M ([DefiLlama](https://defillama.com/chain/xdc)) |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees | **$10.99 (24h) · $494.62 (30d) · $6,219 (1y)** | [Tier A] [DefiLlama XDC fees](https://defillama.com/chain/xdc) |
| Fee burn since Jan 2026 | 62,043 XDC (~$1.8k) | [Tier B] [XDC Watch supply](https://xdcnetwork.org/supply/) |
| Holder rights | **None:** "no revenue distribution right, no treasury claim" | [Tier B] [Blockworks TTF](https://blockworks.com/token-transparency/filing/xdc-network) quoting the MiCA white paper |

**What it means:** A ~$583M chain earning ~$6k a year in fees. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** The EIP-1559 base-fee burn is automatic on-chain, but it is below masternode rewards and fees are ~$6k a year; Revenue stays 2.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer | XinFin Fintech Pte. Ltd. (Singapore, 2017), offeror and issuer in the MiCA white paper; pre-mined ~37.5B XDC | [Tier B] [Blockworks TTF](https://blockworks.com/token-transparency/filing/xdc-network) + [XDC Watch](https://xdcnetwork.org/supply/) |
| XDC Foundation | Cayman not-for-profit (2021); controls no reserves, keys or protocol powers | [Tier B] same |
| Governance | "Largely off-chain and issuer-directed". XDCDAO went offline Mar 2026 and was declared discontinued in Jul 2026 after seven depositors | [Tier B] [Blockworks TTF](https://blockworks.com/token-transparency/filing/xdc-network) [Unverified, single source] |
| Disclosure | No reserve addresses, multisig setup or market-maker deals published | [Tier B] same |

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

*All the wallets below were funded on 3 Dec 2020 by distributor [`0xf46e…4ae7`](https://xdcscan.com/address/0xf46eea9586032e8211a4c6ad5c38a9e3f72c4ae7), which re-sent genesis-sized blocks (14.95B, 8.84B, 4.15B, 4.0B, 2.5B). The genesis allocation is Founders/Team 15B, Ecosystem 10B, Contingency 2.5B, Pre-placement 10B. Matching wallets to buckets is an inference [Unverified].*

| Wallet | XDC now | Notes |
|---|---:|---|
| [`0xd778…Fe03a`](https://xdcscan.com/address/0xd77875df9c9de07a5a701f4431743e3a0e9fe03a) | **12,446,000,006** | Got 14.95B ([tx](https://xdcscan.com/tx/0xa73d2795b514243159f4742c76aa5eca5760fbe61acdfd577a085591b2a1a294)); −1B in the last 30 days |
| [`0xA488…315B`](https://xdcscan.com/address/0xa488b8fdc6df7cad537e88b66841f67b1cbb315b) | 3,609,211,979 | Got 4.0B. CoinGecko excludes 3.6B of Ecosystem Development from supply ([TTF](https://blockworks.com/token-transparency/filing/xdc-network)) |
| [`0x0C98…7d1c`](https://xdcscan.com/address/0x0c98554ae13548c6413105542385619ed1417d1c) | 1,225,814,894 | Got 4.15B; paid out 2.4B in 2020–22 |
| [`0xb942…85F8F`](https://xdcscan.com/address/0xb94249638a3cd070794a6896f65b954547685f8f) | 575,648,248 | Got 8.84B; sent 4.70B to hub [`0x0006…784b`](https://xdcscan.com/address/0x000689bc2983515019ffd14d6f9cf1965bdc784b) (2021–Nov 2026), which feeds distributor `0xb0ef…` (3.43B) |
| [`0xe43D…74C2`](https://xdcscan.com/address/0xe43d90ce00036846b3745229f457fab8058174c2) | 377,999,999 | 2.0B from a 2.5B block (Contingency-sized) via `0x74d4…` |
| New Oct 2026 wallets `0xa1a6…`, `0xe47c…`, `0x8cea…` | 1,000,000,000 | Funded by `0xd778` on 29 Oct 2026 |

**What it means:** Issuer-linked EOAs hold roughly 18B XDC, about 90% of circulating supply, with no published policy. **2**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Pump test uses Gate XDC/USDT daily closes (UTC). 11 of the last 365 days were pump days. Only exchanges tagged on XDCScan were matched, within two hops of the reserve wallets.*

| Day (UTC) | Route | XDC | 5-day change | Pump? |
|---|---|---:|---:|---|
| 4 Oct 2022 | `0xd778` → `0xb804` → **FalconX 1** ([tx](https://xdcscan.com/tx/0xb9d813591165583bdb3adb51aaa58f39d8259d8a2abf8bf5ef3c3bb8e07cf8c8)) | 110,000,100 | −0.7% | No |
| 8 Oct 2022 | same route ([tx](https://xdcscan.com/tx/0xbed9532381cac1a04f7e5079733e8e49a294799c3f43cc8003026b9f9e958a6b)) | 110,000,000 | +4.5% | No |
| 3 and 23 Feb 2023 | `0xd778` → [`0xe99e…`](https://xdcscan.com/address/0xe99e5d7263df4104b1146f9f954788f176b466d7) → `0xb804` → FalconX ([tx](https://xdcscan.com/tx/0x4afc39232d03bbef423c366ece5cdc636a6a7e5d65b9c9fd2c17a95acc3db40d)) | 64,691,780 | −0.4% / −1.9% | No |

- No reserve-linked send to a tagged exchange on a pump day was found.
- The distributor [`0xb0ef…8383`](https://xdcscan.com/address/0xb0ef2a0337a519d50780e33d268341ce75ce8383) has made 6,577 transactions and pays out to many unlabelled wallets. Those sends were not traced to exchange deposits. The TTF says it pays masternode subsidies from the Ecosystem fund [Unverified].

**What it means:** Large OTC transfers happened with no disclosure, and the deeper distribution network is untested. Not proven clean, so **4**.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate XDC/USDT daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- **Uncapped:** masternode rewards of 6,000 XDC per epoch (~50 minutes) plus a manual subsidy of 22,500 XDC per month per masternode. The burn is tiny (62k XDC since Jan 2026) ([XDC Watch](https://xdcnetwork.org/supply/) · [TTF](https://blockworks.com/token-transparency/filing/xdc-network)).
- **Issuer unlocks** of up to 3% a year of the 15B team allocation (450M) and 2.5% a year of the 10B ecosystem allocation (250M) ≈ **700M XDC a year (~3.5% of circulating)**. No smart-contract escrow ([TTF](https://blockworks.com/token-transparency/filing/xdc-network)).
- FDV is 1.9× market cap. CoinGecko (19.95B) and CoinMarketCap (21.48B) disagree on circulating supply.

## 💧 Liquidity & market · 5/10 · ❌ FAIL

- $11.09M of 24h volume on a $582.7M cap (1.9% turnover). Listed on Kraken, Robinhood/Bitstamp, Upbit, Bybit, Gate, KuCoin, SBI VC Trade and others; a 21Shares ETP (XDCN) trades in Europe.
- −46% over a year and −84.8% from ATH.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- XDC 2.0 (HotStuff, ~2s blocks); Cancun upgrade with EIP-1559 burn live 30 Jan 2026 at block 98,800,200; XDC 3.0 staking upgrade targeted Oct 2026 ([TTF](https://blockworks.com/token-transparency/filing/xdc-network)).
- Block times spiked to 13.6s on 11–12 Jan 2026 [Tier B].

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Claimed: 27.7M transactions in Aug 2026 and over $1B tokenized value in May 2026 [Tier B, Unverified].
- Measured: DeFi TVL $1.93M and $494.62 of fees in 30 days ([DefiLlama](https://defillama.com/chain/xdc)).

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Audits: ChainSecurity (2020), SlowMist (2021), CertiK (XDC 2.0, Feb 2025, 57 findings, no critical) [Tier B].
- No protocol exploit found. A 2024 application-layer exploit drained third-party CIFI and XSWAP pools.
- The validator contract `0x…0088` dates from Solidity 0.4.21 and has never had a major upgrade.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- MiCA white paper published Sep 2025 (Ireland home state; not approved by an authority). Listed on Kraken and Binance.US, plus a 21Shares ETP. No enforcement action found [Tier B].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| Oct 2026 (target) | XDC 3.0 staking, rewards and burn upgrade; status not confirmed |
| Ongoing | Up to ~700M XDC a year in issuer unlocks |
| Watch | Where the 1B XDC moved on 29 Oct 2026 goes next |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None at protocol level |
| Team wallet → exchange during a pump | 🟢 None found within two hops; 🟡 distributor network untested |
| Live mint path | 🔴 Uncapped; rewards exceed burn |
| Treasury in single-key wallets | 🔴 ~18B XDC in unlabelled EOAs ([`0xd778…`](https://xdcscan.com/address/0xd77875df9c9de07a5a701f4431743e3a0e9fe03a)) |
| Large unexplained reserve moves | 🟡 1B XDC on [29 Oct 2026](https://xdcscan.com/tx/0x08ea42bb075196000c6c9c56c77ad08e4c650f721741ef8d6c3ffc4e8abd0f3f); 284.7M to FalconX in 2022–23 |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Large OTC transfers | XDC Foundation-linked | XDCScan | medium | no | None: no pump-day exchange send |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API (chain id 50) `txlist` / `txlistinternal` for `0xf46e…`, `0xd778…`, `0xA488…`, `0x0C98…`, `0xb942…`, `0x74d4…` and their recipients; XDCScan top-accounts name tags [Tier B]; read 16 Nov 2026 ~10:00–10:30 AM MST
- [Tier A] [DefiLlama XDC](https://defillama.com/chain/xdc) fees and TVL; CoinGecko `xdce-crowd-sale` (16 Nov 2026 7:13 AM MST); Gate XDC/USDT daily candles
- [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/xdc-network) · [XDC Watch supply](https://xdcnetwork.org/supply/) · [XDC Watch rich list](https://xdcnetwork.org/rich-list/)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): **XDC Network is not supported.** Arkham's network list (Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain) has no XDC chain. Every wallet in this report is native XDC and none has an Ethereum row, so no Arkham labels apply
- [Unverified] Who controls `0xd778…` and the other genesis-funded wallets; what the 29 Oct 2026 transfers are for; the distributor network's exchange deposits

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| `0xd778` funded with 14.95B (3 Dec 2020) | [tx](https://xdcscan.com/tx/0xa73d2795b514243159f4742c76aa5eca5760fbe61acdfd577a085591b2a1a294) | A | 16 Nov 2026 |
| 1B out of `0xd778` on 29 Oct 2026 | [450M](https://xdcscan.com/tx/0x08ea42bb075196000c6c9c56c77ad08e4c650f721741ef8d6c3ffc4e8abd0f3f) · [450M](https://xdcscan.com/tx/0xa572f92c956d1373e7a8b0642a72c241364e55e3ed7b79b6a597a400959b8a14) · [100M](https://xdcscan.com/tx/0x6b8eb19c7f81389cb274af13d80727b72a4e32f1c4eeb40e0f70fd18d2511e59) | A | 16 Nov 2026 |
| `0xd778` → `0xb804` → FalconX | [in 110M](https://xdcscan.com/tx/0x8b590d073375fdedd8355d084da36405b7dfa26729811a099752375c123092ab) · [out 110M](https://xdcscan.com/tx/0xb9d813591165583bdb3adb51aaa58f39d8259d8a2abf8bf5ef3c3bb8e07cf8c8) · [out 110M](https://xdcscan.com/tx/0xbed9532381cac1a04f7e5079733e8e49a294799c3f43cc8003026b9f9e958a6b) · [out 62.7M](https://xdcscan.com/tx/0x4afc39232d03bbef423c366ece5cdc636a6a7e5d65b9c9fd2c17a95acc3db40d) | A + B tag | 16 Nov 2026 |
| Fees $494.62 / 30d; TVL $1.93M | [DefiLlama](https://defillama.com/chain/xdc) | A | 16 Nov 2026 |
| Allocation, unlock caps, holder rights, DAO status | [Blockworks TTF](https://blockworks.com/token-transparency/filing/xdc-network) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who controls the unlabelled XDC wallets** | Arkham does not cover XDC Network. Ask XinFin to label `0xd778…`, `0xA488…`, `0x0C98…`, `0xb942…`, `0x0006…`, `0xb0ef…`, `0xb804…` and the three new Oct 2026 wallets, and check XDCScan name tags | Free |
| 2 | **Which wallets hold which genesis bucket?** | Ask XinFin to publish reserve addresses (the MiCA white paper already gives bucket sizes) | Free |
| 3 | **Where does the 29 Oct 2026 1B go?** | Watch `0xa1a6…`, `0xe47c…` and `0x8cea…`; set an alert | Free |
| 4 | **Distributor `0xb0ef…` exchange deposits** | Trace its 6,577 transactions one more hop, match to exchange hot wallets, and pump-test | Free |
| 5 | **XDC 3.0 status** | Check XinFin release notes for the Oct 2026 mainnet activation | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
