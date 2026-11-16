---
ticker: ZRO
name: LayerZero
chain: ethereum
contract: "0x6985884C4392D348587B19cb9eAAf157F13271cd"
overall_score: 5.3
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 5
  tokenomics_supply: 4
  liquidity_market: 9
  product_development: 8
  adoption_customers: 7
  security_audits: 6
  regulatory: 5
  catalysts: 4
gates_failed: []
red_lines:
  hidden_mint: none_found
  foundation_outflow_on_pump_day: none_found_in_window
  foundation_to_exchange_undisclosed: "1M ZRO, 28 Apr 2026, LayerZero 1 → Binance deposit (not a pump day)"
  fee_switch_on: "no (4 votes, all Off)"
price_usd: 1.52
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ZRO · Overall grade **5.3 / 10 · ❌ FAIL**

**Summary:** LayerZero is heavily used, deep-liquidity cross-chain infrastructure, but token holders get only a small buyback funded by Stargate (about $300k a month). The protocol fee switch has been voted down four times. About 49% of supply is still vesting, and the Foundation's "re-locked" 183M is a promise held in plain multisigs, not a lock in code.

**🚨 Top warning:** On 28 Apr 2026 the Foundation-labelled wallet "LayerZero 1" [`0x1f90…3909`](https://etherscan.io/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909) sent **999,999 ZRO (~$1.5M) to Binance deposit address** [`0xCeF2…5bfe`](https://etherscan.io/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe), forwarded to Binance 14 nine minutes later. No public note of it was found (not a pump day). Check: [send tx](https://etherscan.io/tx/0x054d08ebe2c2f6c9bab7e21cac0b7f491ffb97642caddff96507d976acfe333e) · [forward to Binance 14](https://etherscan.io/tx/0x38c187e58eb80d31513594120fcbbc55f32bfe02a14860b9e3c3699db1b78925) · [Arkham “Binance Deposit”](https://intel.arkm.com/explorer/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe). Bigger structural risk: the Foundation's "re-locked" 183M sits in plain multisigs such as [`0x8F64…449C`](https://etherscan.io/address/0x8F6449530606A9EFddaC42e05612427dDeBA449C).

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ZRO · LayerZero · 5.3 / 10 · ❌ FAIL

> **One line:** LayerZero is heavily used, deep-liquidity cross-chain infrastructure, but token holders get only a small buyback funded by Stargate (about $300k a month). The protocol fee switch has been voted down four times. About 49% of supply is still vesting, and the Foundation's "re-locked" 183M is a promise held in plain multisigs, not a lock in code.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12 PM MST) | 🔗 On-chain (Ethereum RPC + Blockscout, 14 Nov 2026) |
|---|---|
| **Price** $1.52 | **Token** [`0x6985…71cd`](https://etherscan.io/address/0x6985884C4392D348587B19cb9eAAf157F13271cd) · LayerZeroToken (OFT) · Solidity 0.8.22 · verified |
| **24h / 7d / 30d** 🔴 −5.5% / −6.4% / −27.0% | **Ethereum totalSupply** 951,083,167 (the rest of 1B is bridged to other chains) |
| **Market cap** $607.0M · **FDV** $1.518B | **owner()** [`0xf2c6…8ef8`](https://etherscan.io/address/0xf2c6ebc0aad6e8024a2bd2623f97fea5d0ca8ef8) "OneSig", **5 of 8** signers (deployed 13 Apr 2026) |
| **24h volume** $80.2M | **Mint after constructor** none · **pause / blacklist / tax** none |
| **ATH** $7.47 (6 Dec 2024) · now −79.7% | **Largest holder** Future Initiatives multisig, 106.06M (11.15%) |
| **Circulating (CoinGecko)** 399.98M of 1B | **Holders** 26,261 (Blockscout) |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| Protocol fees (messaging) | 30d **$408,354** · all-time **$76.6M** | [Tier A] DefiLlama `layerzero` |
| Protocol revenue to the token | 30d **$0** (zero since Oct 2026) · all-time $3.39M | [Tier A] DefiLlama |
| Protocol fee switch | **INACTIVE.** Votes #1 (Dec 2024), #2 (Jun 2025), #3 (Dec 2025) and #4 (20–27 Jun 2026) all came back **"Off"**. #4 failed quorum. Next vote about 6 months later (~Dec 2026) | [Tier A] layerzero.foundation fee-switch page |
| Stargate revenue → ZRO buybacks | **ACTIVE.** Stargate sends 100% of its revenue to buybacks (since Apr 2026). Stargate was acquired in Aug 2025 for $120M | [Tier A] layerzero.foundation/zro-buybacks · blog "The ZRO Token" (3 Jun 2026) |
| Tracked Stargate buybacks | **2,721,665 ZRO** for **$3,980,541** (0.27% of supply) | [Tier A] zro-buybacks |
| Monthly buybacks | Oct 2026 183,875 ZRO ($299,716) · Sep 162,433 ($351,543) · Aug 183,904 ($193,467) · Jul 160,271 ($131,976) · Jun 141,557 | [Tier A] zro-buybacks |
| Total buybacks claimed since Sep 2025 | **$112.7M**, including the 50M strategic-partner repurchase and a $10M Labs purchase (Nov 2025) | [Tier A] blog (company claim) |
| Fee change | Stargate OFT fee up to 2 bps from 1 Sep 2026; executor minimum $0.25 | [Tier A] LayerZero pricing update, 11 Aug 2026 |

**What it means:** Real fees exist, but almost nothing reaches holders on a recurring basis. Buybacks of about $0.3M a month are small next to an investor unlock rate in the millions of tokens a month. Most of the $112.7M total was one-off treasury repurchases.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Entities | LayerZero Foundation (token, governance, buybacks) and LayerZero Labs (developer) | [Tier A] layerzero.foundation |
| Token owner / admin | `owner()` = [`0xf2c6ebc0aad6e8024a2bd2623f97fea5d0ca8ef8`](https://etherscan.io/address/0xf2c6ebc0aad6e8024a2bd2623f97fea5d0ca8ef8), a **"OneSig"** contract (v0.0.1). **5-of-8** threshold. Deployed 13 Apr 2026 ([tx `0x17147c4b6da8…`](https://etherscan.io/tx/0x17147c4b6da8886dc65aa8abdaca10a2537bdb8298b7b7754f64e13589de8e95)). Signers `0x0cb72c1f…`, `0x771dcacb…`, `0x5bc6aa6a…`, `0x73e9c017…`, `0xe67db04d…`, `0xdfe40272…`, `0x2be094f1…`, `0xd144dad1…` | [Tier A] eth_call `threshold()`, `getSigners()` |
| Earlier owner | 3-of-5 Safe [`0xcDa8e3ADd00c95E5035617F970096118Ca2F4C92`](https://etherscan.io/address/0xcDa8e3ADd00c95E5035617F970096118Ca2F4C92) (v2 note). The transfer date was **not pinned** (log range not available on free RPC) | [Tier A] Safe still 3 of 5 |
| Treasury Safes | `0x8F64…449C` and `0x744D…DA24`, both **3 of 5** | [Tier A] `getThreshold()` |
| CEO Bryan Pellegrino; funding (2023 Series B at a reported $3B) | Public materials and press only | [Unverified] |

**What it means:** Control sits with multisigs that have reasonable thresholds, and the owner moved to a larger 5-of-8 signer set this year. Signer identities are not published.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Wallet | Label | 14 Nov 2026 | % of ETH supply | Locked? |
|---|---|---:|---:|---|
| [`0x8F6449530606A9EFddaC42e05612427dDeBA449C`](https://etherscan.io/address/0x8F6449530606A9EFddaC42e05612427dDeBA449C) | "LayerZero: Future Initiatives Multisig" (Safe 3/5) | 106,064,069 | 11.15% | 🔓 No code lock |
| [`0x744Dbc48D11415ec5cB2f78609DeA5E1E738DA24`](https://etherscan.io/address/0x744Dbc48D11415ec5cB2f78609DeA5E1E738DA24) | Safe 3/5 (sent 11M to GSR and 6.65M to Wintermute in Jun 2024) | 69,549,762 | 7.31% | 🔓 |
| [`0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909`](https://etherscan.io/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909) | "LayerZero 1" ([Arkham](https://intel.arkm.com/explorer/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909)) | 28,999,991 | 3.05% | 🔓 |
| [`0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431`](https://etherscan.io/address/0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431) ([Arkham](https://intel.arkm.com/explorer/address/0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431)) | Safe, created 9 May 2024. Funded 4 Jun 2024 by the genesis Safe in the original allocation batch (see below). **Never moved since.** Arkham: no entity, "Dormant Address" | 22,500,000 | 2.37% | 🔓 (role [Unverified]) |
| [`0x6e0e32684df6e3aE415aB1146A305bFd03E42427`](https://etherscan.io/address/0x6e0e32684df6e3aE415aB1146A305bFd03E42427) ([Arkham](https://intel.arkm.com/explorer/address/0x6e0e32684df6e3aE415aB1146A305bFd03E42427)) | **BitGo custody wallet** (verified contract "WalletSimple", created 20 Jan 2026; Arkham: "WalletSimple (BitGo)"), not a Safe. Received 22,499,999 on 20 Jan 2026 ([tx `0x30ac6cfe…`](https://etherscan.io/tx/0x30ac6cfe765236e03e217c77abfff13e60405798f60200afadb049fbec240219)) from [`0x1d4A12A0…19F5`](https://etherscan.io/address/0x1d4a12a09c293b816bff3625abda3ae07dee19f5), which got its 22.5M in the same 4 Jun 2024 batch. **No outflows** | 22,500,000 | 2.37% | 🔓 (role [Unverified]) |
| `0xF977…` | Binance 8 (exchange) | ~35M | ~3.7% | n/a |

- **The two 22.5M wallets (traced 15 Nov):** the genesis Safe [`0x3437f6f7…9ed3`](https://etherscan.io/address/0x3437f6f7bd47d75780981d0b5a0ce9a038f19ed3) received the whole 1B mint on 17 Apr 2024. On **4 Jun 2024 16:52 UTC** it paid **218,966,392 ZRO to 23 addresses in one transaction** ([tx `0x9f4c16f296f5…`](https://etherscan.io/tx/0x9f4c16f296f5ea5576496a4c4eaff7cf2411fb23baabd40c85844c45ac6e0b18)), including 22.5M to `0x806f…` and 22.5M to `0x1d4A…`. Identical 22.5M lots in a one-off pre-launch allocation batch look like **partner or investor allocations rather than Foundation treasury**, but nothing official says so [Unverified]. Neither has ever sent ZRO to an exchange ([Tier A] Etherscan v2 `tokentx`; [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account)).
- Official split ([Tier A] blog "The ZRO Token", 3 Jun 2026): 1B total. **514M unlocked, 486M still vesting** across the Foundation, strategic partners (now 312M) and contributors (individual terms).
- The Foundation started with 383M; 250M unlocked at launch. The remaining **183M** (including 50M repurchased in Sep 2025) is "**re-locked until Zero's mainnet launch**". No vesting or lock contract was found. The 183M appears to sit in ordinary Safes, so the lock is **policy only**.

**What it means:** Insiders and partners hold roughly half of supply, and the largest "locked" pile can move whenever 3 of 5 signers agree.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

**Pump test:** 65 of 360 days had a ≥10% 5-day rise (CoinGecko, 15 Nov 2025–14 Nov 2026). Recent runs: 19–28 Sep, 2–8 Oct, 1 Nov (+14%) and 4 Nov (+23%).

| Check | Result | Source |
|---|---|---|
| Future Initiatives [`0x8F64…`](https://etherscan.io/address/0x8F6449530606A9EFddaC42e05612427dDeBA449C) | Last outflows: **13 Nov 2025**, 29,999,999 to "LayerZero 1" ([tx `0xa31988c8f04a…`](https://etherscan.io/tx/0xa31988c8f04a87292ecd5492f203d12eb920288cd9fc17b5baddf42a824436f4)), and 11 Nov 2025, 3,333,333 to Safe [`0x7b0aC510…`](https://etherscan.io/address/0x7b0aC51037f43754275BD87446d35351f58448FE) ([tx `0x4c7f3b0c…`](https://etherscan.io/tx/0x4c7f3b0cd36630747dfdbfd57c922133b05b0ff0238fc0440ea39ebe39fd4a4f)). Both are before the pump window. Last inflow 15 Apr 2026 (128,980; [tx `0x9ff36d49…`](https://etherscan.io/tx/0x9ff36d4983b1e3b424361b87325a97fe38ba1bcbebfc67e7aec940980a6c3b74)). **No outflow on any pump day** | [Tier A] Blockscout transfers |
| `0x744D…` | No outflow since 25 Jul 2025 | [Tier A] |
| The two 22.5M wallets `0x806f…` and `0x6e0e…` (new) | `0x806f…`: one transfer ever (the 4 Jun 2024 funding). `0x6e0e…`: only the 20 Jan 2026 inflow (5-day +6.5%, not a pump), a move from a plain wallet into BitGo custody. **No exchange sends** | [Tier A] Etherscan v2 · Arkham |
| "LayerZero 1" [`0x1f90…`](https://etherscan.io/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909) | 28 Apr 2026: 10 ZRO test at 06:18 UTC ([tx `0xdfc7be91…`](https://etherscan.io/tx/0xdfc7be910a233c26cbca4f66a59925307079b1b53bf6f61ee127b9c22b4b6ec5)), then **999,999 at 06:53 UTC to [`0xCeF2E387…`](https://etherscan.io/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe)** ([tx `0x054d08eb…`](https://etherscan.io/tx/0x054d08ebe2c2f6c9bab7e21cac0b7f491ffb97642caddff96507d976acfe333e)), which forwarded **1,000,009 to Binance 14 at 07:02 UTC** ([tx `0x38c187e58eb8…`](https://etherscan.io/tx/0x38c187e58eb80d31513594120fcbbc55f32bfe02a14860b9e3c3699db1b78925)). Arkham labels `0xCeF2…` **"Binance Deposit"** ([Arkham](https://intel.arkm.com/explorer/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe)); Binance 14 is tagged by Etherscan and Arkham (two Tier B), so this was **a ~$1.5M Foundation-labelled deposit to Binance**. 5-day −6.2%, **not a pump**. No public note of it was found | [Tier A] Etherscan v2 · [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account) |
| Investor selling (disclosed) | As of 31 May 2026, 134.7M unlocked to investors and 85.9M (63.8%) still held. Public sales average **4.9M per month**. One entity accounts for 37.9% of sales and unlocks 2.05M a month | [Tier A] blog (company disclosure) |

**What it means:** No Foundation wallet sold into a pump in the last year. The two 22.5M wallets are now traced: neither has ever sent ZRO to an exchange. Arkham confirms that the 1M from "LayerZero 1" in April went to a Binance deposit, an undisclosed exchange send, though on a falling day. Investors sell steadily, and LayerZero discloses that in aggregate. Wider investor wallets are still untraced, so the score stays 5.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Max / total | 1,000,000,000, minted once in the constructor | [Tier A] verified source |
| Circulating | 399.98M (CoinGecko) vs **514M unlocked** (official). The gap is mostly Foundation and treasury balances | [Tier B] CoinGecko · [Tier A] blog |
| Still vesting | **486M (48.6%)** | [Tier A] blog |
| Strategic-partner unlock | Gross **12.7M per month** (cut from 15M by the 50M buyback) | [Tier A] blog |
| Next unlock | ~**23.6M** around 19–20 Nov 2026 (calendar figure) | [Unverified] Tokenomist; not read from a vesting contract |
| Cross-chain supply | OFT. Burned on Ethereum when bridged out and minted elsewhere. Integrity depends on the owner's peer and DVN configuration | [Tier A] code |

**What it means:** About 49% of supply is still to come, and buybacks offset only a fraction of the monthly unlock flow.

## 💧 Liquidity & market · 9/10 · ✅ PASS

| Venue | 24h volume (approx.) | Source |
|---|---:|---|
| Binance | $9.9M | [Tier B] CoinGecko tickers |
| OKX | $5.8M | [Tier B] |
| Bybit | $5.7M | [Tier B] |
| Coinbase | $4.3M | [Tier B] |
| Kraken | $3.7M | [Tier B] |
| Upbit | KRW / BTC / USDT markets listed | [Tier B] |
| DEX total | ~$1.03M liquidity; largest is Aerodrome (Base) ZRO/WETH at ~$300k | [Tier A] DexScreener API |

**What it means:** Deep, multi-venue market led by tier-1 exchanges. Total 24h volume is $80.2M.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Live omnichain messaging protocol with OFT token standard; Stargate bridge owned by the Foundation since Aug 2025 ([Tier A] blog).
- Claimed reach: 165 chains, 71 DVNs (company claim, [Tier A] blog).
- "Zero" chain announced; the Foundation's 183M re-lock is tied to its mainnet launch. Launch date not found ([Unverified]).

**What it means:** It is a shipping, widely integrated product. The next major milestone (Zero mainnet) has no date.

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- Company claims: ~70% of cross-chain stablecoin flow, **$260B** moved ([Tier A] blog, company claim, not independently audited).
- Partners named for Zero: DTCC, ICE, Citadel, Tether, Google Cloud ([Tier A] blog; partner-side confirmation [Unverified]).
- On-chain fees of $76.6M all-time confirm real usage ([Tier A] DefiLlama).

**What it means:** Usage is real and large. The institutional names come from LayerZero itself.

## 🛡️ Security & audits · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Token code | No mint after constructor, no pause, no blacklist, no tax | [Tier A] verified source |
| Admin | OneSig 5-of-8 owner can set peers, DVNs and libraries. A bad configuration could mint ZRO on a remote chain via a forged message | [Tier A] code |
| Incident | KelpDAO bridge incident involving LayerZero infrastructure, Apr 2026 (~$292M reported) | [Unverified] no primary post-mortem read |
| Audits | Not re-read this pass | Not found |

**What it means:** The token contract itself is simple and safe. The cross-chain configuration is the main trust point, and the Apr 2026 incident is still unresolved in this note.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No MiCA white paper, SEC filing or licence for ZRO was found in this pass (Not found).
- Listed on Coinbase, Kraken and Upbit ([Tier B] tickers), which suggests the main exchanges' own reviews passed.
- The Foundation's jurisdiction was not verified ([Unverified]).

**What it means:** No negative actions were found, but there is no positive filing either.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event | Source |
|---|---|---|
| ~19–20 Nov 2026 | Monthly unlock, ~23.6M | [Unverified] Tokenomist |
| Monthly | Strategic-partner unlock, gross 12.7M | [Tier A] blog |
| ~Dec 2026 | Fee switch vote #5 | [Tier A] fee-switch page ("about 6 months") |
| TBA | Zero mainnet, which ends the Foundation's 183M re-lock | [Tier A] blog; date not found |

**What it means:** Near-term events are mostly supply events. The fee switch has failed four times.

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hidden mint function | 🟢 None | Verified source |
| Foundation outflow on a pump day | 🟢 None found in 360-day window | Blockscout transfers for 0x8F64, 0x744D, 0x1f90; Etherscan v2 for the two 22.5M wallets |
| Foundation-labelled send to an exchange, undisclosed | 🟡 Once: 1M ZRO to a Binance deposit, 28 Apr 2026 (not a pump day) | [send](https://etherscan.io/tx/0x054d08ebe2c2f6c9bab7e21cac0b7f491ffb97642caddff96507d976acfe333e) · [forward](https://etherscan.io/tx/0x38c187e58eb80d31513594120fcbbc55f32bfe02a14860b9e3c3699db1b78925) · [Arkham label](https://intel.arkm.com/explorer/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe) |
| Fee switch turned on | 🔴 No | 4 votes, all Off |
| Foundation 183M moved before Zero mainnet | 🟢 Not observed | [0x8F64](https://etherscan.io/address/0x8F6449530606A9EFddaC42e05612427dDeBA449C) no outflow since Nov 2025 |

## 📚 Sources

- [Tier A] Ethereum RPC `eth_call` (owner, threshold, signers, balances) and eth.blockscout.com transfers / holders, 14 Nov 2026
- [Tier A] Verified LayerZeroToken source (Solidity 0.8.22)
- [Tier A] layerzero.foundation: zro-buybacks page, fee-switch page, blog "The ZRO Token" (3 Jun 2026), pricing update (11 Aug 2026)
- [Tier A] DefiLlama `layerzero` fees and revenue · DexScreener tokens API
- [Tier B] CoinGecko markets, tickers and daily closes, 14 Nov 2026
- [Tier A] Etherscan v2 API (ZRO `tokentx`, `getsourcecode`, `getcontractcreation`, tx receipt) for `0x806f…`, `0x6e0e…`, `0x1d4A…`, `0xCeF2…` and the 4 Jun 2024 batch tx; read 15 Nov 2026 ~11:20 AM MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:00 AM MST (signed-in account): "LayerZero" entity (420.8K addresses, ~$274M, 194.8M ZRO; deposits in Arkham's window $1.63M, all Binance; Enterprise-locked all-time view); `0x806f…` "Gnosis Safe Proxy" (dormant); `0x6e0e…` "WalletSimple (BitGo)"; `0xCeF2…` "Binance Deposit"; Binance 14 "Binance: Hot Wallet". Relative ages only; dates above come from on-chain reads
- [Tier A] Explorer pages used (Etherscan): [`LayerZero 1`](https://etherscan.io/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909) · [`0xCeF2…`](https://etherscan.io/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe) · [`0x8F64…`](https://etherscan.io/address/0x8F6449530606A9EFddaC42e05612427dDeBA449C) · [`0x744D…`](https://etherscan.io/address/0x744Dbc48D11415ec5cB2f78609DeA5E1E738DA24) · [`0x806f…`](https://etherscan.io/address/0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431) · [`0x6e0e…`](https://etherscan.io/address/0x6e0e32684df6e3aE415aB1146A305bFd03E42427) · [`0x1d4A…`](https://etherscan.io/address/0x1d4a12a09c293b816bff3625abda3ae07dee19f5) · [`genesis Safe`](https://etherscan.io/address/0x3437f6f7bd47d75780981d0b5a0ce9a038f19ed3) · [`OneSig owner`](https://etherscan.io/address/0xf2c6ebc0aad6e8024a2bd2623f97fea5d0ca8ef8) · [`Binance 14`](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60)
- [Tier B] Arkham address pages used: [LayerZero 1](https://intel.arkm.com/explorer/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909) · [0xCeF2…](https://intel.arkm.com/explorer/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe) · [0x806f…](https://intel.arkm.com/explorer/address/0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431) · [0x6e0e…](https://intel.arkm.com/explorer/address/0x6e0e32684df6e3aE415aB1146A305bFd03E42427) · [Binance 14](https://intel.arkm.com/explorer/address/0x28C6c06298d514Db089934071355E5743bf21d60)
- [Unverified] Nov unlock amount (Tokenomist); KelpDAO incident; funding rounds; CEO; owners of the two 22.5M wallets (partner / investor allocation is an inference); Zero mainnet date; owner-transfer date

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer) or the label source (Arkham) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| **"LayerZero 1" → Binance deposit:** 10 ZRO test, then 999,999 ZRO to `0xCeF2…` on 28 Apr 2026, forwarded 1,000,009 to Binance 14 | [test](https://etherscan.io/tx/0xdfc7be910a233c26cbca4f66a59925307079b1b53bf6f61ee127b9c22b4b6ec5) · [send](https://etherscan.io/tx/0x054d08ebe2c2f6c9bab7e21cac0b7f491ffb97642caddff96507d976acfe333e) · [forward](https://etherscan.io/tx/0x38c187e58eb80d31513594120fcbbc55f32bfe02a14860b9e3c3699db1b78925) · [Arkham “Binance Deposit”](https://intel.arkm.com/explorer/address/0xcef2e3879b5089bcc758a8d3e915ae9e451e5bfe) · [Binance 14 tag](https://etherscan.io/address/0x28C6c06298d514Db089934071355E5743bf21d60) | A + 2× B | 15 Nov 2026 ~11:20 AM MST |
| "LayerZero 1" was funded with 29,999,999 ZRO by the Future Initiatives multisig (13 Nov 2025) | [tx](https://etherscan.io/tx/0xa31988c8f04a87292ecd5492f203d12eb920288cd9fc17b5baddf42a824436f4) · [LayerZero 1](https://etherscan.io/address/0x1f903473376fBe98cc763F1Bc459C8fdB6AC3909) | A | 14 Nov 2026 |
| Future Initiatives multisig `0x8F64…` holds 106.06M (11.15%); no outflow since Nov 2025 | [Etherscan](https://etherscan.io/address/0x8F6449530606A9EFddaC42e05612427dDeBA449C) · last outflows [13 Nov](https://etherscan.io/tx/0xa31988c8f04a87292ecd5492f203d12eb920288cd9fc17b5baddf42a824436f4) / [11 Nov](https://etherscan.io/tx/0x4c7f3b0cd36630747dfdbfd57c922133b05b0ff0238fc0440ea39ebe39fd4a4f) | A | 14 Nov 2026 |
| Two 22.5M wallets came from one 4 Jun 2024 allocation batch (218,966,392 ZRO to 23 addresses) | [batch tx](https://etherscan.io/tx/0x9f4c16f296f5ea5576496a4c4eaff7cf2411fb23baabd40c85844c45ac6e0b18) · [0x806f…](https://etherscan.io/address/0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431) · [0x1d4A…](https://etherscan.io/address/0x1d4a12a09c293b816bff3625abda3ae07dee19f5) · [Arkham 0x806f…](https://intel.arkm.com/explorer/address/0x806f68Bb6ce8f3100D4745C8b13b36e4f40D8431) | A + B | 15 Nov 2026 |
| `0x1d4A…` moved its 22.5M into BitGo custody wallet `0x6e0e…` (20 Jan 2026); no outflows since | [tx](https://etherscan.io/tx/0x30ac6cfe765236e03e217c77abfff13e60405798f60200afadb049fbec240219) · [0x6e0e… Etherscan](https://etherscan.io/address/0x6e0e32684df6e3aE415aB1146A305bFd03E42427) · [Arkham “WalletSimple (BitGo)”](https://intel.arkm.com/explorer/address/0x6e0e32684df6e3aE415aB1146A305bFd03E42427) | A + B | 15 Nov 2026 |
| Token owner is OneSig 5-of-8 `0xf2c6…8ef8`, deployed 13 Apr 2026 | [Etherscan](https://etherscan.io/address/0xf2c6ebc0aad6e8024a2bd2623f97fea5d0ca8ef8) · [deploy tx](https://etherscan.io/tx/0x17147c4b6da8886dc65aa8abdaca10a2537bdb8298b7b7754f64e13589de8e95) | A | 14 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns the two 22.5M wallets** (`0x806f…` Safe, `0x6e0e…` BitGo) | Read `getOwners()` on `0x806f…`; match the 23 recipients of the 4 Jun 2024 batch to LayerZero's partner / investor list; Arkham or Nansen labels for the other 21 recipients | Free / Nansen paid |
| 2 | **Was the 28 Apr 1M to Binance disclosed, and what was it for?** | LayerZero Foundation buyback / treasury reports for Apr–May 2026; ask the Foundation | Free |
| 3 | **Exact Nov unlock (~23.6M) and its recipients** | Read the vesting contracts or the Foundation's unlock post; trace recipients after 19–20 Nov | Free |
| 4 | **Owner-transfer date to the OneSig** | `OwnershipTransferred` log on the token, via Etherscan v2 `getLogs` | Free |
| 5 | **KelpDAO incident** | Primary post-mortem from KelpDAO or LayerZero | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
