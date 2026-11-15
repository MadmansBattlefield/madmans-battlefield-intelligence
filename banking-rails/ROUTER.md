---
ticker: ROUTER
name: Solrouter
not_to_be_confused_with: "Router Protocol (ROUTE)"
chain: solana
mint: 6SjVTj1VGwFSXn7wEjwFm77LvACeTqB7sQUebYKX8Ds5
overall_score: 2.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 2
  insider_holdings: 2
  selling_behavior: 1
  tokenomics_supply: 4
  liquidity_market: 1
  product_development: 6
  adoption_customers: 1
  security_audits: 5
  regulatory: 2
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  liquidity_below_75k: tripped
  founder_exit: not_confirmed
  paying_customer_by_q1_2027: open_none_found
price_usd: 0.000492
price_source: "DexScreener main Meteora DLMM pool, 14 Nov 2026 9:02 AM MST"
chain_read_slot: 469384534
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### ROUTER · Overall grade **2.2 / 10 · ❌ FAIL**

**Summary:** A real privacy-AI product with honest docs and almost no paying usage. The token's cash flow is trading fees on itself, insiders control ~42% of supply, the founder-linked wallet has sold into pumps, and the main pool holds about $22k of real buy-side money.

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 2/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 1/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 4/10 | ❌ FAIL |
| 💧 Liquidity & market | 1/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 1/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 2/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 ROUTER · Solrouter · 2.2 / 10 · ❌ FAIL

> **One line:** A real privacy-AI product with honest docs and almost no paying usage. The token's cash flow is trading fees on itself, insiders control ~42% of supply, the founder-linked wallet has sold into pumps, and the main pool holds about $22k of real buy-side money.

⚠️ **Not Router Protocol (ROUTE).** Different team, chain and token.

| 📊 Market (14 Nov 2026, ~9:02 AM MST) | 🔗 On-chain (Solana RPC, slot 469,384,534) |
|---|---|
| **Price** $0.000492 (DexScreener) · $0.000489 (CoinGecko) | **Mint** `6SjVTj1V…KX8Ds5` · SPL · 9 decimals |
| **24h / 7d / 30d** 🔴 −19.2% / −12.1% / −71.0% (CoinGecko) | **Supply** 999,010,210.70 (launch 1,000,000,000) |
| **FDV** $488,975 · **Mkt cap** $346,828 (CoinGecko) | **Mint authority** none · **Freeze authority** none |
| **ATH** $0.006017 (24 May 2026) · now **−92%** | **Metadata** immutable (`isMutable = false`) |
| **Main pool liquidity** $38,706 (vs $91,832 on 16 Oct); $36,396 at a recheck later on 14 Nov | **Insider-controlled** 420.7M (**42.1%**) |
| **All venues** ~$51,364 | **Of that, liquid right now** 130.3M (**13.0%**) |
| **24h volume** $3,296 (Meteora) + $984 (Raydium) | **Top-10 owners** 56.2% · **holders** 1,372 |
| **Buy-side cash in main pool** 299.15 SOL ≈ **$21,910** | **Launched** 30 Apr 2026 via OpenServ SERV Launchpad |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

**Product revenue: effectively none you can see.**

| Metric | Value | Source |
|---|---:|---|
| Pricing | Pro $9 / Builder $49 / Scale $99 per 30 days in USDC · $0.02 per sealed call pay-as-you-go | [Tier A] [docs.solrouter.com/docs/use/pricing](https://docs.solrouter.com/docs/use/pricing) |
| On-chain receipts (one per sealed call, program `ATMRatMtsKX4bHax7U4FRdhbE4mjU4NKpDZGqZqAhBKb`) | **1,008 lifetime** | [Tier A] `getSignaturesForAddress`, 14 Nov 2026 |
| Receipts by month | May 46 · Jun 116 · Jul 23 · Aug 12 · Sep 482 · Oct 307 · **Nov 1–14: 22** | [Tier A] |
| Implied pay-per-call revenue, Nov 1–14 | 22 × $0.02 = **$0.44** (upper bound if every receipt were paid; plans could add more) | Calculated |
| Burns since 10 Oct 2026 | 999,014,055.72 → 999,010,210.70 = **3,845 ROUTER burned (~$2)** | [Tier A] mint supply reads |
| Burns since launch | **989,789 ROUTER (0.099%)** | [Tier A] |
| USDC in team wallet | 0.000111 USDC | [Tier A] token accounts, 14 Nov |

**How the docs say value should reach the token** ([Tier A] [docs.solrouter.com/docs/token](https://docs.solrouter.com/docs/token)):
- "50% of USDC revenue buys back $ROUTER on the open market through Jupiter. The rest stays in treasury."
- "50% of every buyback is burned. The other 50% stays in treasury."
- "50% of every $ROUTER fee paid directly is burned on receipt."
- So only **25% of USDC revenue** ends up burned. 3,845 burned in 35 days implies USDC revenue on the order of single-digit dollars, **if** burns come only from this path.

**The cash flow that does exist: trading fees on its own token.**

| Item | Value | Source |
|---|---:|---|
| Launchpad LP fee split | 1% or 2% swap fee · **creator 67% / platform 33%**, paid every 4 hours | [Tier A] [docs.openserv.ai/launch/for-builders.md](https://docs.openserv.ai/launch/for-builders.md) |
| Main Meteora pool lifetime volume / fees | $9,891,363 / **$171,105** | [Tier A] Meteora pool API |
| Main pool fees, last 24h | $46.28 (protocol share $11.48) | [Tier A] Meteora API |
| Fee drips from launchpad `7Da5dp…cpwPh` → team wallet | **2,558 transfers · 55.7M ROUTER + ~361.6 SOL** since 30 Apr | [Tier A] team-wallet tx scan, 3,958 txs |
| Same, Nov 1–14 only | 1.085M ROUTER + 3.58 SOL (≈ $790 at today's prices) | [Tier A] |

**What it means:** The team gets paid when people trade the token, not when people use the product. Product usage is about 1–2 sealed calls a day this month.

## 🏛️ Foundation & team — Who is in charge? · 2/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Legal entity | **None yet.** "Router Labs, institutional division of Solrouter. **Incorporating in Cyprus.**" | [Tier A] routerlabs.ai footer |
| Privacy notice | "Registered company name, number and address will be stated here once incorporation completes: ENTITY NAME, HE NUMBER, REGISTERED ADDRESS. ADD ON INCORPORATION." | [Tier A] routerlabs.ai/privacy (updated 20 Aug 2026, "Draft, not yet in force") |
| Terms | Governing law "Republic of Cyprus, with the courts of CITY. CONFIRM ON INCORPORATION" — **unfilled template text** | [Tier A] routerlabs.ai/terms |
| GitHub org | `Router-Labs`, created 15 May 2026 · 4 repos (`solrouter-docs`, `router-sdk`, `tempRouter`, `.github`) | [Tier A] GitHub API |
| Named contributors | `Sarthib7` / `Sarthiii` (most commits) · `noahhaufer` (13–14 commits per repo; display name "GhostHash") | [Tier A] GitHub API |
| Founder name in circulation | Noah Haufer — matches the `noahhaufer` GitHub login. Biography beyond that | [Unverified] |
| Founder's last public commit | **30 Sep 2026** (`solrouter-docs`); 27 Sep in `router-sdk` | [Tier A] GitHub API |
| Team multisig `2EfTtofXxj939kWHwJwD1t8HpzrAwa2uoqfsuNd7XzmK` | Squads v4 · **2 of 3** · time lock **0** · 52 executed proposals · members: `2df1NHQj1k5vqpsGnLybtxyiNSfSLYeQjYJcrq7vxpCb`, `7k5ReRiNfrJfmhEdhXd76H6H2DZFz9QskY49rmhMuRvR`, team wallet `HdcrLZ2HcJkoEpMtw7XQKJ9b7YjHYfsNoiAQb1R1dzaK` | [Tier A] decoded Squads account |
| Treasury multisig `8z56bUciNH4pEbn7udwfRBJsNreATBwEJ1UXUUFmxTQ4` | Squads v4 · **2 of 3** · time lock **0** · 16 executed proposals · members: `7k5ReRi…`, `DqVsnN3PiqdKpv9QgQWd96acsdMaKyLovZ9gLPDNM8zB`, `HnsHBemR7VasqPrPYwqHgGSdqJcSm7iSu84ktp1rkS7q` | [Tier A] |
| Overlap | `7k5ReRi…` signs on **both** multisigs. Team wallet signs the team multisig | [Tier A] |
| Investors / priced round | None found. Only the launchpad's "algorithmic fundraising" bands | [Tier A] docs (absence) |

**What it means:** There is no company yet. Two or three anonymous keys control everything the "foundation" owns, with no delay on any move.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

Live reads, 14 Nov 2026 (slot 469,384,534), compared with the 10 Oct 2026 forensic read:

| Wallet | Role | 10 Oct 2026 | 14 Nov 2026 | % of supply | Locked? |
|---|---|---:|---:|---:|---|
| `FE3dRU27viJ3qiNXuuMQpyBo8rwSkAKZ468ca39rjp36` | Streamflow "ROUTER Team Vesting" escrow | 171,666,667 | 171,666,667 | 17.18% | 🔒 partly — see below |
| `8iq4s7vD8A6wJKs1672v9kMHyghwQ6LXUqd2K7a2cawC` | Streamflow "treasury" escrow | 118,750,000 | 118,750,000 | 11.89% | 🔒 partly — see below |
| `DiCPkTF2P4moPxC1P2uEUbHuoh9zuxnR1fUAdZqcyYAi` | Vault 0 of team multisig `2EfTt…` | 113,750,000 | 113,750,000 | 11.39% | 🔓 **No lock** |
| `HdcrLZ2HcJkoEpMtw7XQKJ9b7YjHYfsNoiAQb1R1dzaK` | Team wallet (vesting recipient, multisig signer) | 14,845,706 | **16,581,289** | 1.66% | 🔓 liquid |
| `2fwJ66qu3qsvkMCisV2dV4AF3bhUvZ2tAKTJ9i4pfRyx` | Vault 0 of treasury multisig `8z56b…` | 0 | 0 | 0% | (passes tokens through) |
| `FQgy7aHg…tQeN` | Matches "OpenServ (SERV drop) 5%" allocation; never moved since 30 Apr | 50,000,000 | 50,000,000 | 5.00% | 🔓 unlocked at TGE (control [Unverified]) |
| **Team + treasury total** | | | **420,747,955** | **42.1%** | |
| **Liquid today** (multisig vault + team wallet) | | | **130,331,289** | **13.0%** | |

**Vested but not yet claimed (can be pulled any time):**
- Team stream: 200M total, cliff 29 Jul 2026, ~555,556/day to 25 Jul 2027. By 14 Nov: ~60.0M vested, 28.33M claimed (18 Sep 2026) → **~31.7M claimable now**.
- Treasury stream: 150M total, 6.25M every ~30.4 days to Apr 2028. 6 releases vested, 5 claimed → **6.25M claimable now**.

**Other assets in insider wallets** (Tier A, 14 Nov): team multisig vault holds **125.34 hSOL** (Helius staked SOL) and 0.43 SOL; team wallet holds **12.14 SOL** plus several other launchpad tokens.

**Official allocation vs chain** ([Tier A] token docs): LP 45% (450M), Treasury 24.5% (245M: 9.5% at TGE + 24-month linear), Team 20% (200M: 3-month cliff, 12-month linear), OpenServ 5%, Algorithmic Fundraising 5%, Superteam Germany 0.5%. The streams on-chain match the team and treasury schedules. Docs say vesting runs on Sablier; ROUTER actually uses **Streamflow**.

**What it means:** Insiders hold about 42%. About 13% can be sold today with no contract in the way, and another ~38M is unlocked and waiting to be claimed.

## 📉 Selling behavior — Do insiders sell into pumps? · 1/10 · ❌ FAIL

**Pump test:** a "pump day" is a daily close ≥10% above the close five days earlier (GeckoTerminal daily closes, main pool, 15 May – 14 Nov 2026). **57 of 184 days** qualified — this token pumps a lot.

### A. Team multisig → fresh wallet → sold into the September pump

| Time (UTC) | Tx | What happened |
|---|---|---|
| 13 Sep 2026 16:06 | `2FqcHNs2KM63GsMsY81B6R6p…` | Team multisig vault `DiCPk…` sent **5,000,000 ROUTER** to `7sgL1aGHpCJzYrydouy1QWmnm4H3eqoWdQWYVCWEs11F` (a plain wallet, 0.086 SOL) |
| 20 Sep 11:15 | `4UKszMeX1LKdrKjrLYgAzTkc…` | Sold 1,200,000 into Meteora + Raydium · Meteora paid out 21.66 SOL · 5-day move **+195%** |
| 20 Sep 14:16 | `3dZG8WyHAnrrbRXkX6SAawqi…` | Sold 800,000 · 16.14 SOL out of the pool |
| 20 Sep 15:36 – 18:40 | `5WSz3H7e…`, `2xFyYetb…` | 1,000,000 sent to owner `4r1ZxG8ALLYakoHFk7m3GMJewDJXbL22aML4nkcWvmgx` |
| 21 Sep 01:37 | `4ZH3d5F7LHpmg1xo9i1nmJeP…` | Sold 270,000 · 5.89 SOL · 5-day move **+139%** |
| 21 Sep 01:40 | `3BMHnUPcaa4HdMs5Hs1scqFi…` | 350,000 to `4r1ZxG8…` |
| 21 Sep 14:07 | `GNwe7AAy3ndh2URnP5g737cA…` | Sold 435,000 · 10.77 SOL |
| 21 Sep 20:28 | `3W6peLov7UjoKNpQeQbXfiEn…` | Sold 800,675 · 18.96 SOL |
| 21 Sep 20:55 | `eCFvieAEuKnRPnW7hgdDF2b3…` | Last 283,753 to `4r1ZxG8…` · wallet now empty |

- **~3.51M ROUTER sold for ~73.4 SOL** within 8 days of leaving the team multisig, all on pump days. ~1.63M went to `4r1ZxG8…` (now 0 ROUTER).
- That transfer needed 2 of 3 multisig signatures, one of which is the team wallet. Who owns `7sgL1a…` is [Unverified] — it could be a contractor, market maker or OTC buyer. No disclosure found.

### B. The team wallet itself trades in both directions — including sells into pumps

From a full scan of all **3,958** transactions on the team wallet's ROUTER account (30 Apr – 14 Nov 2026):

| Window | ROUTER sold (swaps) | SOL received by team wallet on sells* | ROUTER bought (swaps) | SOL spent on buys* |
|---|---:|---:|---:|---:|
| Pump days (5-day ≥ +10%) | **28,360,628** | 215.9 | 60,652,314 | 85.8 |
| Normal days | 22,389,329 | 32.1 | 24,533,146 | 193.3 |
| 30 Apr – 19 May (before price series) | 54,007,193 | 225.6 | 22,174,889 | 128.8 |

\* Only counts SOL that landed directly in the team wallet; some swaps routed proceeds elsewhere.

Selected pump-day sells by the team wallet (5-day move in brackets):

| Time (UTC) | Sold | SOL to team wallet | Tx |
|---|---:|---:|---|
| 20 May 14:38 | 398,000 | — | `3zWwLZY7vsUsEFjU…` (+140.5%) |
| 23–24 May | 1,430,000 in 4 swaps | — | `4am1Rc8u…`, `3RQj2Lbi…`, `3mWJ7hiB…`, `4U8cEv1s…` (+50–56%) |
| 7 Sep 14:24 | 897,000 | 6.86 | `4yYfy3XkLBUB1ztX…` (+144.6%) |
| 8 Sep 11:36 / 15:55 | 2 × 1,000,000 | — | `26ad3Wex…`, `227WXdGS…` (+266%) |
| 11 Sep 13:03–13:18 | 1,876,000 in 4 swaps | — | `2HYyyQW3…`, `3GtmCvas…`, `5KYtfenD…`, `4wzYpUeP…` (+358%) |
| 19 Sep 08:03 – 23:53 | 1,130,000 in 3 swaps | 33.5 | `SXT3AfZe…`, `4d13B8py…`, `5CD5Dsk7…` (+191%) |

**Liquidity placed into the pool during the Sep pump** (DLMM, one-sided ROUTER — this works like a ladder of sell orders above the price):

| Time (UTC) | ROUTER in | Tx |
|---|---:|---|
| 7 Sep 23:14 | 20,000,000 | `4k7eC5LCT6op7QjG…` (+144.6%) |
| 11 Sep 22:33 | 17,000,000 | `63k7DARanMCKCVco…` (+358%) |
| 17 Sep 10:04 | 13,200,000 | `4ZZk3Jj56MdWn3GW…` (+33.5%) |
| 18 Sep 21:06 | 13,200,000 (13,198,950 withdrawn 5 min earlier) | `2uquYxLX…` / `41EwzsxjErsWZ6oW…` |
| 19 Sep 18:08 | 13,000,000 | `5irSDmMwvwtEUsN8…` (+190.6%) |

### C. Treasury → team wallet (internal, but into a wallet that trades)

| Time (UTC) | From → To | Amount | 5-day move |
|---|---|---:|---:|
| 21 Aug 06:28 | Treasury multisig vault → team wallet | 6,250,000 | **+61.1%** |
| 10 Sep 22:12 | Treasury multisig vault → team wallet | 6,250,000 | **+220.9%** |
| 31 May / 7 Jul / 1 Oct | Treasury multisig vault → team multisig vault | 86.25M / 6.25M / 6.25M | −30.6% / +13.8% / +4.8% |
| 18 May 13:45 | Treasury multisig vault → **10 wallets × 2,000,000** | 20,000,000 | (before price series) |

**Since 10 Oct:** no ROUTER left the team multisig, treasury multisig or either vesting escrow. The team wallet's balance grew by 1.74M from fee drips. The 13 Nov +35% day showed **no insider outflow**.

**What it means:** Yes. A team-controlled multisig funded a wallet that sold into the September pump, and the founder-linked team wallet sold tens of millions of tokens on pump days while also buying. Under this layout's rule that is a FAIL; it would clear only if the team discloses `7sgL1a…` as an arm's-length buyer and the team wallet's trading as disclosed market-making.

## 📊 Tokenomics & supply · 4/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Supply | 999,010,210.70 | [Tier A] RPC |
| Mint / freeze / metadata | None / none / immutable. Update authority + sole creator `7Da5dpUbNG8nbvCCJMennTssbhkpZNi8NfE6uawcpwPh` (OpenServ launchpad) | [Tier A] RPC, Metaplex |
| Circulating at TGE (docs) | 53.04% · 6 mo 66.50% · 12 mo 83.29% · 24 mo 100% | [Tier A] token docs |
| Circulating (CoinGecko) | 708.59M (70.9%) | [Tier B] CoinGecko |
| Unlock flow | ~555,556/day team + 6.25M/month treasury ≈ **23M/month (~2.3% of supply)** | [Tier A] Streamflow streams |
| Unlock flow vs pool | 23M/month ≈ **68%** of the ROUTER in the main pool (33.76M) | Calculated |
| Algorithmic fundraising | 50M over 14 FDV bands, $500K → $100M; band 1 is $500K–$750K, 0.30% of supply | [Tier A] token docs |
| FDV vs band 1 | FDV today **$489k**, just **under** the $500k band-1 trigger | Calculated |
| Launch protection | Buy caps for first 130 seconds (100k/tx, 1M/wallet to 70s) | [Tier A] token docs |
| Genesis (30 Apr 2026 15:13 UTC, tx `3LzBJTHY9eJQdqJN…`) | 700M → launchpad, 250M → team wallet, 50M → `FQgy7a…` | [Tier A] |

**What it means:** The code is clean, but about 2.3% of supply unlocks every month into a pool that only holds about 3.4% of supply.

## 💧 Liquidity & market · 1/10 · ❌ FAIL

**Pools (DexScreener + Meteora API, 14 Nov 2026 9:02 AM MST):**

| Pool | Pair | Liquidity | 24h volume | 24h txns, buys / sells (later 14 Nov recheck) |
|---|---|---:|---:|---|
| Meteora DLMM `DJ8qzBm3ZoRi4YiVmpiLBBuc67cq737vqaTNbMRJGcvZ` | ROUTER/SOL · bin step 250 · base fee 1% | **$38,706** (33.76M ROUTER + 299.89 SOL) | $3,296 | 81 / 39 |
| Raydium CLMM `Aq4jqjq4gQuxFoB4cVMZZLVPhBE8Q1yum7y9YKestqM4` | ROUTER/NVDAx | $12,624 | $984 | 27 / 71 |
| Meteora DLMM `8frM6fa414PfDdUxXW7hHcEBvyy58KpRS7zk5NgwSZcK` | ROUTER/SOL | $24 | $2 | 3 / 13 |
| Meteora DYN2 `2nBXSgowoxgM2Ps7cfFernV6GHdWw3siiGLHCFZbTyLP` | ROUTER/SOL | $10 | $1 | 1 / 10 |

**Main-pool history** (daily-report snapshots, MST mornings; 14 Nov is today's live read):

| Date | Price | Main Meteora pool | All venues |
|---|---:|---:|---:|
| 16 Oct 2026 | $0.002009 | $91,832 | $121,408 |
| 26 Oct 2026 | $0.001199 | $69,369 | $92,066 |
| 30 Oct 2026 | $0.000897 | $59,169 | $78,675 |
| 4 Nov 2026 | $0.000834 | $56,535 | $75,280 |
| 7 Nov 2026 | $0.00052 (−39% day) | $45,800 | ~$60,000 |
| 11 Nov 2026 | $0.000445 | $39,700 | $52,000 |
| 12 Nov 2026 | $0.00045 | $39,200 | $50,700 |
| 13 Nov 2026 | $0.00062 (+35% day) | $45,100 | $59,000 |
| **14 Nov 2026** | **$0.000492** | **$38,706** | **$51,364** |

**Monthly volume** (GeckoTerminal, main pool): May $3.58M · Jun $897k · Jul $198k · Aug $138k · Sep $2.43M · Oct $633k · **Nov 1–14 $88.8k**. Last 7 days: $36.5k.

**Sell impact** — estimated from the real SOL side of the main pool (299.15 SOL × $73.24 = **$21,910**), using constant-product math. DLMM bins can make it better or worse:

| Sell size | Estimated price drop |
|---:|---:|
| $250 | −2.2% |
| $500 | −4.4% |
| $1,000 | −8.5% |
| $2,500 | −19.4% |
| $5,000 | −33.7% |
| $10,000 | −52.9% |

- Insider-liquid 130.3M ROUTER is ~**3.9×** the ROUTER in the main pool and worth ~$64k at spot — about 3× all the SOL in it.

**What it means:** A $2,500 sale moves the price about 20%. The insiders' liquid stack cannot exit at anything close to the quoted price.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

What it is ([Tier A] [docs.solrouter.com](https://docs.solrouter.com/docs)): private AI chat and API. Prompts are encrypted on the user's device (X25519 + Arcium RescueCipher), relayed as ciphertext, and opened inside an Intel TDX enclave on Phala. Each sealed call writes a Light Protocol compressed receipt on Solana.

| Item | Detail | Source |
|---|---|---|
| Surfaces | Web chat (solrouter.com), TypeScript SDK `@solrouter/sdk`, MCP server (Claude Code, Cursor, Claude Desktop), Agent Privacy API (private swaps, x402 pay-per-call) | [Tier A] docs |
| Models | GPT-OSS 20B, Qwen 3.8 27B, Qwen3 Coder 30B on Nosana GPUs; Qwen3.5 122B in an H200 GPU enclave | [Tier A] docs |
| Honest limit (their words) | "The GPU node that runs the model sees the prompt while it works on it, and Solrouter does not control that hardware." | [Tier A] docs |
| Attestation | "SDK attestation verification is not built" — users must check by hand | [Tier A] docs |
| npm | `@solrouter/sdk` 1.0.0 (20 Jan 2026) → 1.0.1 (21 Mar) → 1.1.0 (5 Jun) → **1.2.0 (28 Sep 2026)** — no release in 47 days | [Tier A] npm registry |
| GitHub | `router-sdk` 21 commits in last 90 days (last 9 Oct); `solrouter-docs` pushed 9 Nov 2026 | [Tier A] GitHub API |
| Not shipped | Agent Tools SDK "not on npm yet (Soon)"; Umbra private swaps "Soon" | [Tier A] docs |

**What it means:** The product is real and the docs are unusually candid about what is and is not private. Development slowed after early October.

## 🤝 Adoption & customers · 1/10 · ❌ FAIL

- **Paying enterprise customer:** none announced in any primary source through 14 Nov 2026.
- **Usage:** 22 sealed-call receipts on-chain in Nov 1–14 (about 1.6 a day). Peak month Sep 2026: 482.
- **Third-party integrations:** Not found.
- **Partner allocations:** OpenServ 5% and Superteam Germany 0.5% (token docs). Neither is a customer.

**What it means:** No evidence anyone pays for this at scale.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Token-level rug vectors | None: no mint, no freeze, immutable metadata | [Tier A] |
| Hacks / exploits | None found | [Tier A] |
| Audit | None found in official docs | [Tier A] (absence) |
| Admin keys | Both multisigs are 2-of-3 with **zero time lock**; one key (`7k5ReRi…`) signs both | [Tier A] |
| Privacy claim | Three of four models run outside the enclave on hardware Solrouter does not control | [Tier A] docs |

**What it means:** The token cannot be rugged at the code level. The treasury can be moved instantly by two keys.

## ⚖️ Regulatory · 2/10 · ❌ FAIL

- No incorporated entity, no licence, no registered address (see Foundation & team).
- The docs describe private swaps where "Solrouter routes the swap through a mixer so the two ends are not linked" (the Umbra mixer, marked **"Soon"**), plus "Managed wallet (Mode A)… where Solrouter creates and holds a wallet for your agent" ([Tier A] docs, llms-full.txt). Mixing and custody are the kinds of services regulators target, even before launch.
- No court or enforcement records found.

**What it means:** An unincorporated team planning a mixer-style feature and custodial wallets has open regulatory exposure.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Every day | ~555,556 ROUTER team unlock | Supply ↑ |
| ~Every 30.4 days | 6.25M treasury release (next ~mid/late Nov 2026) | Supply ↑ |
| If FDV > $500k | Algorithmic fundraising band 1 opens (0.30% of supply sold) | Sell pressure on any bounce |
| "Soon" | Umbra private swaps / Agent Tools SDK launch | Product news; mixer adds regulatory risk |
| Pending | Cyprus incorporation of Router Labs | Would fill the entity gap |
| Q1 2027 | Paying-customer test (red line below) | |
| 25 Jul 2027 | Team stream fully vested | |
| ~29 Apr 2028 | Treasury stream fully vested | |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Main-pool liquidity under $75,000 | 🔴 **Tripped** since late Oct 2026 | $38,706 on 14 Nov |
| Founder exit | 🟡 Not confirmed | Founder-linked GitHub account last committed 30 Sep 2026; no departure notice found |
| No paying customer by Q1 2027 | 🟡 Open — none found so far | No announcement; 22 receipts in Nov 1–14 |
| Insider selling into pumps | 🔴 **Tripped** (Sep 2026) | Section 📉 above |

## 📚 Sources

- [Tier A] Solana mainnet RPC (`api.mainnet-beta.solana.com`): mint, token accounts, Squads multisig accounts, Streamflow escrows, `getSignaturesForAddress` + `getTransaction` for the team wallet (3,958 txs), team/treasury multisig vaults, escrows, `FQgy7a…`, `7sgL1a…`, and the attestation program; 14 Nov 2026, slot ~469,384,534
- [Tier A] Prior forensic read, 10 Oct 2026 (slots 455,264,193–455,264,399), and full holder list, 10 Nov 2026
- [Tier A] [Solrouter docs](https://docs.solrouter.com/docs) — [token](https://docs.solrouter.com/docs/token), [pricing](https://docs.solrouter.com/docs/use/pricing), [models](https://docs.solrouter.com/docs/how-it-works/models), [llms.txt](https://docs.solrouter.com/llms.txt)
- [Tier A] [OpenServ launchpad docs](https://docs.openserv.ai/launch/for-builders.md) · [programmatic fundraising](https://docs.openserv.ai/launch/programmatic-fundraising.md)
- [Tier A] [routerlabs.ai](https://routerlabs.ai) · [privacy](https://routerlabs.ai/privacy) · [terms](https://routerlabs.ai/terms)
- [Tier A] [GitHub Router-Labs](https://github.com/Router-Labs) · npm `@solrouter/sdk`
- [Tier A] [DexScreener](https://dexscreener.com/solana/DJ8qzBm3ZoRi4YiVmpiLBBuc67cq737vqaTNbMRJGcvZ) · Meteora DLMM pool API · GeckoTerminal daily OHLCV
- [Tier B] CoinGecko `solrouter` market data, 14 Nov 2026 9:08 AM MST
- [Tier A] Daily report snapshots in [../daily/](../daily/) (`pools.ROUTER`)
- [Unverified] Founder biography; owner of `7sgL1a…`, `4r1ZxG8…` and the ten 2M-ROUTER recipients of 18 May; control of `FQgy7a…`

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
