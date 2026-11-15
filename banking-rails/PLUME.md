---
ticker: PLUME
name: Plume
chain: plume
contract: "0x4C1746A800D224393fE2470C70A35717eD4eA5F1"
overall_score: 3.5
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 6
  insider_holdings: 2
  selling_behavior: 3
  tokenomics_supply: 3
  liquidity_market: 6
  product_development: 6
  adoption_customers: 3
  security_audits: 5
  regulatory: 6
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  upgradeable_mintable_token: "yes (contradicts MiCA paper)"
  exchange_inflows_on_pump_days: "yes (bridge → Binance, 23 Sep and 13 Oct 2026; sender not traced)"
  issuer_wallets_published: "no"
price_usd: 0.012343
price_source: "CoinGecko, 14 Nov 2026 12:12 PM MST"
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### PLUME · Overall grade **3.5 / 10 · ❌ FAIL**

**Summary:** A real RWA chain with a proper EU MiCA white paper and a US-registered transfer agent, but the token earns almost nothing (about $2.3k of chain fees a month). The Ethereum token is an upgradeable proxy with live mint, burn and pause roles, which contradicts the white paper's "no ongoing minting" line. About 212M PLUME unlocks every month, and hundreds of millions moved from the bridge to Binance on pump days.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 3/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 6/10 | ✅ PASS |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 PLUME · Plume · 3.5 / 10 · ❌ FAIL

> **One line:** A real RWA chain with a proper EU MiCA white paper and a US-registered transfer agent, but the token earns almost nothing (about $2.3k of chain fees a month). The Ethereum token is an upgradeable proxy with live mint, burn and pause roles, which contradicts the white paper's "no ongoing minting" line. About 212M PLUME unlocks every month, and hundreds of millions moved from the bridge to Binance on pump days.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:12 PM MST) | 🔗 On-chain (Ethereum RPC + Blockscout; explorer.plume.org) |
|---|---|
| **Price** $0.012343 | **Token (Ethereum)** `0x4C17…A5F1` · "PProxy" EIP-1967 → impl `0x8ab0…5Ae9` "Plume" (0.8.25, verified) |
| **24h / 7d / 30d** 🔴 −11.3% / −6.8% / −36.0% | **Total supply** 10,000,000,000 |
| **Market cap** $84.08M · **FDV** $123.3M | **Roles** MINTER / BURNER / PAUSER / UPGRADER ⚠️ live · `paused()` = false |
| **24h volume** $11.1M | **Bridge** `0x3538…EF83` holds 4,511,760,175 (45.12%) |
| **ATH** $0.2475 (19 Mar 2025) · now −95% | **Holders (Ethereum)** 25,646 |
| **Circulating (CoinGecko)** 6.818B of 10B (68%) | **Plume chain** 254.99M total txs · 419,735 today · 973,425 addresses |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| Plume mainnet chain fees | 24h **$74** · 30d **$2,343** · all-time $1.04M | [Tier A] DefiLlama `plume-mainnet` |
| Plume vaults | 30d fees $1,084,205 · **revenue $0** | [Tier A] DefiLlama `plume-vaults` |
| Fee share, buyback or burn to PLUME holders | **None found.** The MiCA paper says "no burn mechanism" | [Tier A] MiCA white paper |
| Company revenue | Not published | Not found |

**What it means:** Chain fees are about $2.3k a month against an $84M market cap. Vault fees go to vault users and curators, not to the token.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Issuer | **Plume Ltd** (BVI), registration 2147684, registered 2024-05-01, LEI 254900FXSZXTZUJLP764. Registered office: SHRM Trustees (BVI), Road Town | [Tier A] MiCA white paper |
| Parent and sole director | **Plume Foundation SEZC** (Cayman, Genesis Building, George Town) | [Tier A] MiCA |
| Service provider | Kimber Labs, Inc. | [Tier A] MiCA |
| Transfer agent | Kimber Transfer Agency LLC, CIK 0002083132, Form TA-1 filed 2025-08-29, file 084-07011 | [Tier A] SEC EDGAR |
| Public profile | General Counsel Salman Banaei testified to the House on 25 Mar 2026 | [Tier A] congressional record (earlier scan) |
| Funding | $30M raised in 2024 (Galaxy, Haun, Brevan Howard, Lightspeed) | [Tier A] MiCA |

**What it means:** The legal structure is unusually well documented for a crypto project. Token-role holders are not.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Issuer retained | **4,666,554,520 PLUME (46.7%)**. **Addresses not published** | [Tier A] MiCA §G.5 |
| Bridge contract (Ethereum) | 4,511,760,175 (45.12%) | [Tier A] balanceOf |
| Top Plume-chain native holders | Binance 8, 813.6M · `0x57b83AAF…` 162.3M · PlumeStaking `0x30c791E4…` 138.3M · WPLUME 66.1M · Gate.io 5, 58.0M | [Tier A] explorer.plume.org |
| Unlabeled Plume-chain wallets | Many holding **45–84M** each with only 1–5 transactions. The pattern suggests vesting or investor wallets | [Unverified] |

**What it means:** Nearly half of supply sits with the issuer in wallets it has not disclosed, so its holdings can't be tracked.

## 📉 Selling behavior — Do insiders sell into pumps? · 3/10 · ❌ FAIL

**Pump test:** 74 of 360 days had a ≥10% 5-day rise (CoinGecko). The runs were 19–29 Sep and 12–16 Oct 2026.

| Date (2026) | Bridge `0x3538…` → "Binance: Internal 2" `0xE69f…3Abb` | 5-day % | Source |
|---|---:|---:|---|
| 4 Sep | 10,000,000 | +1.8% | [Tier A] Blockscout |
| 15 Sep | 20,000,000 | −2.0% | [Tier A] |
| **23 Sep** | **30,000,000** (tx `0xd7f3354ab17b80…`) | **+25.3% 🔴 pump** | [Tier A] |
| 5 Oct | 30,000,000 | +7.4% | [Tier A] |
| 8 Oct | 20,000,000 | −1.7% | [Tier A] |
| **13 Oct** | **30,000,000** (tx `0x097bd9ee589b74…`) | **+17.7% 🔴 pump** | [Tier A] |
| 15 Oct | 20,000,000 | +8.9% | [Tier A] |
| 20 Oct | 50,000,000 (tx `0x7a67d9aa08c9ce…`) | −11.3% | [Tier A] |

- **Total 210M** bridged straight to a Binance wallet in seven weeks, two batches of it on pump days.
- On 9 Oct, ~60.5M also left the bridge to four unlabeled wallets: `0xcFb8896A…` 15.15M, `0xADbDDDa8…` 12.4M, `0xe002B3B5…` 18.4M, `0xeAA553F8…` 14.5M.
- **Not traced:** the Plume-chain sender behind each withdrawal. These could be Binance moving its own inventory rather than issuer sales **[Unverified]**.

**What it means:** Large, undisclosed exchange inflows lined up with pump days. Because the issuer won't publish its wallets, insider selling can't be ruled out. That trips the selling gate.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Max / total | 10B | [Tier A] totalSupply |
| Circulating | 6.818B (68%). The old "2B" figure was the launch float (~2.65B) | [Tier B] CoinGecko · launch float [Unverified] |
| Unlock pace | ~**212M per month** until 21 Jan 2028 | [Unverified] Tokenomics.com |
| Next unlock | ~21 Nov 2026, ~211.8M (~$2.6M at today's price) | [Unverified] |
| Mint | **MINTER_ROLE can mint with no cap** in the implementation | [Tier A] verified source |
| MiCA claim | "no ongoing minting or inflation; no burn mechanism" | [Tier A] MiCA. **Contradicted by the code's capability**, though no mint above 10B has happened |

**What it means:** About 3% of circulating supply unlocks every month, and the supply cap is a promise, not code.

## 💧 Liquidity & market · 6/10 · ✅ PASS

| Venue | 24h volume (approx.) | Source |
|---|---:|---|
| Binance | $2.58M | [Tier B] CoinGecko tickers |
| HTX | $1.25M | [Tier B] |
| Upbit (KRW / USDT / BTC) | $635k | [Tier B] |
| BTCC, Paribu, Bybit | smaller | [Tier B] |
| DEX total | **~$95k** liquidity (Uniswap PLUME/USDC $42k) | [Tier A] DexScreener API |

**What it means:** Tradable on major CEXs, but on-chain depth is thin.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Plume mainnet live since 5 Jun 2025; token launched 21 Jan 2025 ([Tier A] MiCA).
- Chain activity: 254.99M total transactions, 419,735 today, 973,425 addresses ([Tier A] explorer.plume.org stats).
- Staking contract (PlumeStaking) holds 138.3M ([Tier A] explorer).

**What it means:** The chain is live and busy by transaction count. Fee data says most of that activity is very low value.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- Chain fees of $2,343 in 30 days ([Tier A] DefiLlama) do not match the claimed RWA scale.
- Shinhan MoU, 14 Aug 2026 (PR Newswire; an MoU, not a deployment) [Tier B].
- Plume is **not** on DTCC's 4 May 2026 working-group list ([Tier A] DTCC).
- RWA "total value" on project dashboards is project-reported ([Unverified]).

**What it means:** The partnerships are announcements, and paying usage is minimal.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token | EIP-1967 proxy. `upgradeToAndCall` is gated by UPGRADER_ROLE, and mint, burn and pause are role-gated | [Tier A] verified implementation |
| Role holders | **Not enumerated** (the RoleGranted log scan timed out) | Not found; needs an archive `getLogs` |
| Correction | The earlier Treasury Health scan said PLUME "isn't a proxy". **That was wrong** | [Tier A] |
| Bridge | TransparentUpgradeableProxy → ERC20Bridge impl `0x81be…D9D6` | [Tier A] |
| Hacks | None found for PLUME | [Tier B] |

**What it means:** Whoever holds the roles can upgrade, mint or pause the token, and they are not public.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- **MiCA white paper** published, notification date 2026-03-18 (type: Correction), offer start 2025-01-25 ([Tier A] plume.org PDF).
- SEC-registered transfer agent (Kimber Transfer Agency, TA-1) ([Tier A] EDGAR).
- House testimony by the General Counsel, 25 Mar 2026 ([Tier A]).

**What it means:** Plume engages with regulators better than most. The code contradiction above is a disclosure issue to watch.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event | Source |
|---|---|---|
| ~21 Nov 2026 | Monthly unlock, ~211.8M | [Unverified] Tokenomics.com |
| Monthly to 21 Jan 2028 | ~212M per month | [Unverified] |
| — | No confirmed product or listing catalyst found | Not found |

**What it means:** The calendar is dominated by supply.

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Upgradeable, mintable token | 🔴 Yes | PProxy + MINTER_ROLE / UPGRADER_ROLE |
| Mint above 10B | 🟢 Not used | totalSupply 10,000,000,000 |
| Exchange inflows on pump days | 🔴 Yes (sender not traced) | 23 Sep, 13 Oct |
| Issuer wallets published | 🔴 No | MiCA §G.5 gives amount only |
| Token paused | 🟢 No | `paused()` = false |

## 📚 Sources

- [Tier A] Ethereum RPC and eth.blockscout.com: token proxy, implementation source, balances, bridge transfers, 14 Nov 2026
- [Tier A] explorer.plume.org Blockscout API: native holders, chain stats
- [Tier A] Plume MiCA white paper (plume.org/landing/Plume-MiCA-Modified-White-Paper.pdf)
- [Tier A] SEC EDGAR, Kimber Transfer Agency LLC (CIK 0002083132) · DTCC 4 May 2026 list
- [Tier A] DefiLlama `plume-mainnet`, `plume-vaults` · DexScreener tokens API
- [Tier B] CoinGecko markets, tickers and daily closes · PR Newswire (Shinhan MoU)
- [Unverified] Unlock schedule (Tokenomics.com); launch float; role holders; Plume-chain senders of the bridge withdrawals; identity of unlabeled 45–84M wallets

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
