---
ticker: S
name: Sonic
chain: sonic
contract: "native (Sonic chain, chain id 146); wrapped wS 0x039e2fB66102314Ce7b64Ce5Ce3E5183bc94aD38"
overall_score: 3.0
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 0
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 6
  adoption_customers: 2
  security_audits: 6
  regulatory: 5
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "none on Sonic found; Fantom-era incidents (Multichain bridge collapse, Jul 2023) predate S"
  mint_path_live: "yes: no hard cap; governance has approved repeated new issuance (airdrop 190.5M, ongoing funding 47.6M a year for 6 years, 472.4M institutional issuance on 4 Sep 2025, plus a possible $50M ETF issuance)"
  team_wallet_to_exchange_during_pump: "yes: the Fantom Foundation-labelled wallet sent 40.5M S to a Binance deposit on 21 Aug 2026 (+29.8% day); a Sonic issuance-signer wallet sent 76.6M S on 9-10 May 2025 pump days to a market-maker-like wallet"
  treasury_selling: "292.5M S (~$11.7M) from the 150M-S 'Sonic USA'-sized issuance wallet, the Fantom Foundation wallet and the ongoing-funding wallet went to one Binance deposit address (Mar-Aug 2026); not disclosed as sales"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "About $6k a month of revenue; no burn, buyback or fee share of size."
pump_day_price_source: "Gate S_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (50 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions:
  - address: "0xbea8fecf6535592eebfc68f227a434f8373792f0"
    label: "Issuance wallet (received exactly the approved 150M S)"
    confidence: high
    independent_corroboration: true
    basis: "Sonicscan + governance vote"
price_usd: 0.03218
price_source: "CoinGecko, 16 Nov 2026 6:58 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### S · Overall grade **3.0 / 10 · ❌ FAIL**

**Summary:** Sonic (formerly Fantom) is a fast EVM layer-1. Usage has collapsed: **TVL is $12.6M** and the chain earned **$75.7k of revenue in 12 months**. S is −97% from its January 2025 high and −75% in a year. There is no supply cap, and governance keeps approving new issuance (supply is up from 3.175B to 3.885B). Wallets tied to the Foundation and Sonic's issuance have moved **hundreds of millions of S into Binance**, some of it on pump days. Both hard gates fail.

**🚨 Top warning:** The wallet [`0xbea8…92f0`](https://sonicscan.org/address/0xbea8fecf6535592eebfc68f227a434f8373792f0) received [**exactly 150M S on 4 Sep 2025**](https://sonicscan.org/tx/0x6642e7fdc2b4203a9d0ffd013e85a5050e50041bbdf8254087c0d3f05e014c1f). That is the day and the size of the governance issuance for "Sonic USA" per the docs. It sent [**118M S on 11 Mar 2026**](https://sonicscan.org/tx/0x4e6a06d3d55978d295963c85c3531ef2047cb638de97da9e7f295998e93c875d) to [`0xfefa…2ecc`](https://sonicscan.org/address/0xfefa8f05418e53fa0a1b327704014b101f172ecc), which [forwarded it the same day](https://sonicscan.org/tx/0x47558bd4c456aceec0c968959c43d7e406e262af9232e8e0cd1c0a018b437c99) to **Binance 94** (~$4.9M). In all, `0xfefa` passed **292.5M S (~$11.7M) into Binance** from Sonic-linked wallets. That includes [40.5M S from the Fantom Foundation wallet on 21 Aug 2026](https://sonicscan.org/tx/0xb9a1cd08344c1925726bf9271d8769c4a881bd34603bc9e5b2d3beee61d81d9d), a **+29.8% pump day**. Every link is in the 🔗 Evidence trail below.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 S · Sonic · 3.0 / 10 · ❌ FAIL

> **One line:** A rebranded Fantom with fast tech but almost no usage left, an open-ended issuance policy, and Foundation-linked wallets feeding Binance.

| 📊 Market (CoinGecko, 16 Nov 2026 6:58 AM MST) | 🔗 On-chain (Sonic, 16 Nov 2026) |
|---|---|
| **Price** $0.0322 | **Token** native S; wrapped [wS](https://sonicscan.org/address/0x039e2fB66102314Ce7b64Ce5Ce3E5183bc94aD38) |
| **24h / 7d / 30d** 🔴 −4.6% / −11.7% / −40.2% · 1y −75.2% | **Supply** 3.885B (CoinGecko), no cap; 3.175B at the FTM→S launch |
| **Market cap = FDV** $125.0M | **Fantom Foundation** (Sonicscan label) [`0x431e…6354`](https://sonicscan.org/address/0x431e81e5dfb5a24541b5ff8762bdef3f32f96354) |
| **24h volume** $21.4M; **66% on BitDelta** ($14.1M), Binance only $0.96M | **Airdrop / incentives treasury** [`0x2889…6210`](https://sonicscan.org/address/0x2889604E75637D3AfE919201C27ac9d1221E6210) 91.7M S (named in the Sonic Labs blog) |
| **ATH** $1.03 (4 Jan 2025) · now −96.9% | **SonicStrategy DAT multisig** [`0xc9d2…53f6`](https://sonicscan.org/address/0xc9d21b370d7d2a24ee0b08f82323777737a653f6) 126.6M S staked, sale-restricted (Sonic Labs blog) |
| **Pump days, last 365 days** 51 (Binance SUSDT closes) | **TVL** $12.6M (DefiLlama) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$75,967** (30 days: $3,360) | [Tier A] [DefiLlama, `sonic`](https://api.llama.fi/summary/fees/sonic?dataType=dailyFees) |
| Revenue, last 12 months | **$75,713** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/sonic?dataType=dailyRevenue) |
| Fee split | 90% of core-contract fees go to the FeeM vault for apps; holders get only staking rewards | [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/sonic) · [S token docs](https://docs.soniclabs.com/sonic/s-token) |

**What it means:** About $6k a month. **1 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** About $6k a month of revenue; no burn, buyback or fee share of size.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- **Sonic Labs** builds the chain. The **Sonic Foundation** (Cayman Islands, legal form not disclosed) manages the treasury, the 200M-S Innovator Fund and the legacy Opera validators ([Blockworks filing](https://blockworks.com/token-transparency/filing/sonic)).
- On-chain governance votes approve issuance. But the Foundation has not published its internal treasury thresholds or a full admin matrix.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Wallet | Role (source) | Received | Now |
|---|---|---:|---:|
| [`0x2889…6210`](https://sonicscan.org/address/0x2889604E75637D3AfE919201C27ac9d1221E6210) | Airdrop/incentive treasury (Sonic Labs blog) | 190.4M | **91.7M** |
| [`0xc9d2…53f6`](https://sonicscan.org/address/0xc9d21b370d7d2a24ee0b08f82323777737a653f6) | SonicStrategy DAT, 4-of-6 Safe, sale-restricted (blog) | 126.6M | staked in SFC |
| [`0xbea8…92f0`](https://sonicscan.org/address/0xbea8fecf6535592eebfc68f227a434f8373792f0) | Safe that got the 150M "Sonic USA"-sized issuance [inferred] | 158.7M | 7.9M |
| [`0xfcec…a2e7`](https://sonicscan.org/address/0xfcecc79bc12b7c3bb96d9d062ecb7f830961a2e7) | Ongoing-funding wallet (docs) | 47.6M (Jun 2025) | 0 |
| [`0x4c56…c6c`](https://sonicscan.org/address/0x4c5683a9ede3c8b4fb5ad2e980bbf88652ad6c6c) | Safe funded with 1.196B S by the migration bridge operator | 1.22B | 1.4M |
| [`0x431e…6354`](https://sonicscan.org/address/0x431e81e5dfb5a24541b5ff8762bdef3f32f96354) | Fantom Foundation (Sonicscan label) | 1.44B | ~0 |

**What it means:** Most of the Foundation-side S has already been paid out. Where large amounts went (e.g. [949.5M S to a Binance deposit on 14 Jan 2025](https://sonicscan.org/tx/0xdd80b56ca773973555463c0938f7e20c13d9d47d91e4ddb2d73ac57ad0d65c4b), most likely Binance's FTM→S user migration [Unverified]) is only partly explained. **4.**

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

`0xfefa…2ecc` behaves like a Binance deposit address: an EOA that never keeps a balance and sweeps everything to [Binance 94](https://sonicscan.org/address/0xa4e471dbfe8c95d4c44f520b19cee436c01c3267) (Sonicscan label) within hours.

| Date | From | S | Pump? | Evidence |
|---|---|---:|:---:|---|
| 10 Mar 2026 | Ongoing-funding wallet 4.6M, its recipients `0xee46…` 5.2M and `0xfc97…` 2.2M, Foundation-funded `0xb0f4…` 7.0M | 19.0M | — | [ongoing funding](https://sonicscan.org/tx/0x38b45fe9e6cf992a910e451c55085f60b601d2beca293877314fb51bc09563cb) |
| 11 Mar 2026 | "Sonic USA"-sized Safe `0xbea8…` | **118.0M** (~$4.9M) | — | [in](https://sonicscan.org/tx/0x4e6a06d3d55978d295963c85c3531ef2047cb638de97da9e7f295998e93c875d) · [to Binance](https://sonicscan.org/tx/0x47558bd4c456aceec0c968959c43d7e406e262af9232e8e0cd1c0a018b437c99) |
| 9 Apr 2026 | `0xd870…` (funded with 65.6M by the Foundation + 78.6M of unwrapped wS) 100.7M; Foundation 14.4M | 115.1M (~$4.8M) | — | [in](https://sonicscan.org/tx/0x44a3533a9a6249c028edd5c3120b788d61825f9cd99e861ca4156f72890a8b28) · [to Binance](https://sonicscan.org/tx/0xa4c09513f21a701d6a4d2dbdc979f274367af05998f73d3e3a976534eb3fee3c) |
| **21 Aug 2026** | **Fantom Foundation** | **40.5M** (~$1.2M) | **+29.8%** | [in](https://sonicscan.org/tx/0xb9a1cd08344c1925726bf9271d8769c4a881bd34603bc9e5b2d3beee61d81d9d) · [to Binance](https://sonicscan.org/tx/0xad1a2689855e75f29da198040d2248c37866521444b5b95a91db87f32a730189) |
| **9–10 May 2025** | Issuance-signer EOA [`0x6e9f…f6c5`](https://sonicscan.org/address/0x6e9f215876d210e5c8a197df598db2d8fe09f6c5) (it executes Sonic's issuance Safe transactions) → pass-through `0x2cfb…` → high-activity [`0xd9a3…ca39`](https://sonicscan.org/address/0xd9a355e9101d91b1450b8538e57161c3c0deca39), which pays Kraken 75 and others | **76.6M** (~$46M) | **+13.3%, +19.9%** | [9 May](https://sonicscan.org/tx/0xcc539ad614ec4724f1f8ecb1aa95ffbb6488417c68fef363edda9a0a1a17ce4d) · [10 May](https://sonicscan.org/tx/0x761902ae1a66bdc1be36e19d1039a477530c17db94f8311cd23145a05431be53) |

- The Jan–Apr 2025 transfers from `0x6e9f…` to Crypto.com, Gate, BTC Turk and Binance US fall in the FTM→S exchange migration window. They are treated as likely migration swaps [Unverified], not sales.
- Whether Binance sold the 292.5M S or holds it in custody is [Unverified]. No disclosure of these transfers was found.

**What it means:** Issuance and Foundation wallets keep feeding one exchange account, one deposit landed on a pump day, and none of it is disclosed. **2 → hard-gate FAIL.**

- **Disclosure quality (16 Nov 2026 rules): silence.** None of it was disclosed as sales. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. 21 Aug 2026 is a pump day on Gate prices. Pump days from Gate S_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (50 of 360 days); the body's earlier count used CoinGecko daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- No cap. Governance-approved issuance so far: airdrop 190.5M (89.8M issued Jul 2025), ongoing funding 47.6M a year (unused amounts burned), **472.4M on 4 Sep 2025** for the Nasdaq DAT and Sonic USA, and a possible further $50M for an ETF ([docs](https://docs.soniclabs.com/sonic/s-token)).
- Supply has grown about 22% since launch. Validator rewards came from reallocated Opera rewards for the first 4 years.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $21.4M of 24h volume, but **66% is on BitDelta**. Binance shows under $1M. Real depth is thin for a $125M cap.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Live high-throughput EVM L1 since Dec 2024, with the Sonic Gateway bridge to Ethereum and FeeM (fee sharing with apps).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- **TVL $12.6M** (DefiLlama /v2/chains, 16 Nov 2026), down from roughly $1B in 2025. Fees of about $100 a day.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of the Sonic chain found. Fantom-era losses (the Multichain bridge, 2023) predate S.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- There is a US push (Sonic USA, a planned Nasdaq-listed DAT, an ETF pursuit). Under the DAT agreement, 126.6M S are restricted from sale. No enforcement found.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Each June to 2031 | 47.6M S ongoing-funding issuance (unused amounts burned) |
| TBD | Possible $50M ETF issuance; remaining airdrop (~92M S) through 2027 |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found on Sonic |
| Team wallet → exchange during a pump | 🔴 [Foundation → Binance, 21 Aug 2026 (+29.8%)](https://sonicscan.org/tx/0xb9a1cd08344c1925726bf9271d8769c4a881bd34603bc9e5b2d3beee61d81d9d) |
| Live mint path | 🔴 No cap; repeated governance issuance |
| Treasury selling | 🔴 292.5M S into Binance (Mar–Aug 2026) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Fantom Foundation-labelled wallet | Fantom / Sonic Foundation | Sonicscan + Arkham label | high | yes | Selling: 40.5M S to a Binance deposit on the 21 Aug 2026 pump day (+29.8%) |
| [`0xbea8…92f0`](https://sonicscan.org/address/0xbea8fecf6535592eebfc68f227a434f8373792f0) | Issuance wallet (received exactly the approved 150M S) | Sonicscan + governance vote | high | yes | Selling: fed the same Binance deposit |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Sonic chain via Etherscan API v2 (chain 146): native and internal transfers of the wallets above; receipts (status 1) for every linked tx; read 16 Nov 2026 ~7:10–7:25 AM MST
- [Tier A] Sonicscan public labels (Fantom Foundation, Binance 94, Binance US 8, Gate, Crypto.com 22, BTC Turk, Kraken 75) and Etherscan labels of the same addresses (Binance and Gate deposits)
- [Tier A] [Sonic docs: S token](https://docs.soniclabs.com/sonic/s-token) (issuance txs, ongoing-funding wallet); [Sonic Labs blog: airdrop economics update](https://www.soniclabs.com/blog/sonics-airdrop-economics-update/); [Sonic Labs blog: Sonic in 2026 and beyond](https://www.soniclabs.com/blog/sonic-in-2026-and-beyond/)
- [Tier B] [Blockworks token transparency filing](https://blockworks.com/token-transparency/filing/sonic)
- [Tier B] Arkham, read 16 Nov 2026 ~7:35 AM MST (signed-in account): **Sonic is not supported.** The network selector lists only Ethereum, Polygon, BNB Chain, Optimism, Avalanche, Arbitrum, Base, Bitcoin, Tron, Flare, Solana, Dogecoin, Zcash, HyperEVM, Hypercore, Robinhood Chain. Looking up `0xbea8…92f0` returned only the same address's Ethereum-mainnet holdings (a Gnosis Safe holding USDC, USDT and ETH), with no S token or Sonic data ([Arkham](https://intel.arkm.com/explorer/address/0xbea8fecf6535592eebfc68f227a434f8373792f0)). That neither confirms nor rules out Sonic USA. No Arkham labels were available for this report
- [Tier A] DefiLlama `sonic` fees, revenue and TVL; CoinGecko `sonic-3` (16 Nov 2026 6:58 AM MST); Binance SUSDT daily closes
- [Unverified] that `0xbea8…` is Sonic USA (it matches the amount and date only); that `0xfefa…` is a Binance deposit (sweep pattern only); who runs `0xd9a3…`. Arkham does not support Sonic (checked 16 Nov 2026)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 150M S issued to `0xbea8…` on 4 Sep 2025 | [tx](https://sonicscan.org/tx/0x6642e7fdc2b4203a9d0ffd013e85a5050e50041bbdf8254087c0d3f05e014c1f) · [docs](https://docs.soniclabs.com/sonic/s-token) | A chain · identity [Unverified] | 16 Nov 2026 |
| `0xbea8…` → `0xfefa…` → Binance 94, 118M | [in](https://sonicscan.org/tx/0x4e6a06d3d55978d295963c85c3531ef2047cb638de97da9e7f295998e93c875d) · [out](https://sonicscan.org/tx/0x47558bd4c456aceec0c968959c43d7e406e262af9232e8e0cd1c0a018b437c99) | A | 16 Nov 2026 |
| Fantom Foundation → Binance on a +29.8% day | [in](https://sonicscan.org/tx/0xb9a1cd08344c1925726bf9271d8769c4a881bd34603bc9e5b2d3beee61d81d9d) · [out](https://sonicscan.org/tx/0xad1a2689855e75f29da198040d2248c37866521444b5b95a91db87f32a730189) | A | 16 Nov 2026 |
| 76.6M S on May 2025 pump days | [9 May](https://sonicscan.org/tx/0xcc539ad614ec4724f1f8ecb1aa95ffbb6488417c68fef363edda9a0a1a17ce4d) · [10 May](https://sonicscan.org/tx/0x761902ae1a66bdc1be36e19d1039a477530c17db94f8311cd23145a05431be53) | A chain · end use [Unverified] | 16 Nov 2026 |
| 949.5M S to a Binance deposit, 14 Jan 2025 | [largest tx](https://sonicscan.org/tx/0xdd80b56ca773973555463c0938f7e20c13d9d47d91e4ddb2d73ac57ad0d65c4b) | A chain · purpose [Unverified] | 16 Nov 2026 |
| Revenue $75.7k / 12 months | [DefiLlama](https://api.llama.fi/summary/fees/sonic?dataType=dailyRevenue) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Is `0xbea8…` Sonic USA, and why did 118M S go to Binance?** | Arkham does not cover Sonic. Ask Sonic Labs; match `0xbea8…`'s Ethereum Safe signers to Sonic Labs' published multisigs | Free |
| 2 | **Who runs `0xd9a3…` (market maker?)** | Arkham does not cover Sonic; check the same address on Ethereum and look for a disclosed market-making agreement | Free |
| 3 | **Who controls the 1.2B-S Safe `0x4c56…`** | Read Safe owners; match them to Foundation signers | Free |
| 4 | **Was the Jan 2025 Binance transfer the FTM→S user migration?** | Match it to Binance's migration announcement and FTM inflows on Fantom Opera | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
