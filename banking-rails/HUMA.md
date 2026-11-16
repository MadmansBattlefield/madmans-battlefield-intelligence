---
ticker: HUMA
name: Huma Finance
chain: solana
contract: "HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw"
overall_score: 4.4
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 6
  insider_holdings: 3
  selling_behavior: 5
  tokenomics_supply: 3
  liquidity_market: 4
  product_development: 7
  adoption_customers: 7
  security_audits: 7
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found on the protocol; an early LP's own wallet was hacked on 22 Oct 2026 and ~12M airdropped HUMA were sold (Huma's account, Tier B)"
  mint_path_live: "no (Solana mint authority is null; supply fixed at 10B; BSC side is a LayerZero OFT backed 1:1 by the Solana escrow)"
  team_wallet_to_exchange_during_pump: "not found in the vaults traced; but 671.5M HUMA left the 'Huma Investors' and 'Huma Treasury Unlocked' Squads vaults for six fresh wallets on four pump days (30 Sep to 4 Oct 2026); still unsold as of 16 Nov 2026"
  one_hop_sale_status: none_found
  treasury_in_single_key_wallets: "no for the labelled vaults (Squads 3-of-4 and 4-of-5, zero timelock); 671.5M sits in six unlabelled plain wallets that the vaults funded"
  unlock_cliff: "first investor and team unlock on 26 Nov 2026 (investors 20.6% and team/advisors 19.3% of supply, 12 quarterly releases); investor tokens sit in a Huma-controlled Squads multisig, not a vesting contract"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "All yield goes to LPs; the buyback is still a plan."
pump_day_price_source: "Gate HUMA/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.006616
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### HUMA · Overall grade **4.4 / 10 · ❌ FAIL**

**Summary:** Huma runs a real payment-financing ("PayFi") credit business. Its PST yield token has about $367M in TVL and more than 100k LPs, and the protocol has been audited by Halborn, Sec3, Spearbit and Certora. But **the HUMA token earns nothing**: DefiLlama records $18.2M of yield in the last year, all of it paid to LPs, and **$0** of protocol or holder revenue ("the permissionless pool has no protocol fee configured"). The token fell **−77% in 30 days** and sits **−94% below ATH**. The first investor and team unlock lands on **26 Nov 2026**, ten days from now. Only 17.3% of supply circulates, and about 59% sits in Huma-controlled Squads multisigs with no timelock. Revenue trips the hard gate.

**🚨 Top warning:** the investor lock is a promise, not code. All 2.06B investor tokens went into a Squads vault labelled **"Huma Investors"** ([`DZaR8…R44U`](https://solscan.io/account/DZaR8LfPXAQfqFptp34zy5TcePCbZw9piYSqXePRR44U)). That vault is a **3-of-4 multisig with a 0-second timelock**, not a vesting program. On **1 Oct 2026**, a +16.3% pump day, it sent **471,521,700 HUMA** to the unlabelled wallet [`3xfvk…qF3`](https://solscan.io/account/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3) ([tx](https://solscan.io/tx/2PEgFDTXNSiPi4AyjjDAFqXjo9JZptMaKhhXgzGkzHb3qGyo4EFMWyqUM6uACZQiBGKsYGgeA2LYab4LTmeodxxp)). Between 30 Sep and 6 Oct 2026, "Huma Treasury Unlocked" also sent **200M** to five fresh wallets, each after a tiny test send (e.g. [50M on 30 Sep](https://solscan.io/tx/4ZzhJFEyZXACAmxX45LaByMRvXVkKvz96KYjMH9R4LidsaSCakRz2BQAu3LqA2qQj2v4DU3hPPyisCqcYdk4DzGk)). None of these 671.5M tokens has been sold yet. They equal **39% of today's circulating supply**, and they sit in wallets Huma has not named. The first scheduled unlock is [26 Nov 2026](https://blog.huma.finance/huma-build-to-last). Every transfer is linked in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 5/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 7/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 HUMA · Huma Finance · 4.4 / 10 · ❌ FAIL

> **One line:** A real PayFi lending business, but none of its yield reaches the token. The token is down 94% from its high, with a ten-day countdown to the first investor and team unlock, and the investor tokens are held in a multisig Huma controls rather than in a vesting contract.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (Solana, 16 Nov 2026) |
|---|---|
| **Price** $0.006616 | **Mint** [`HUMA1821…wGw`](https://solscan.io/token/HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw) SPL token, 6 decimals |
| **24h / 7d / 30d** 🔴 −2.0% / −36.0% / −77.0% · 1y −72.9% | **Supply** 9,999,994,216 · **mint authority: none** · freeze authority: none |
| **Market cap** $11.47M · **FDV** $66.2M | **Circulating (CoinGecko)** 1,733,333,333 (17.3%) |
| **24h volume** $5.06M | **BSC** [`0x9251…a8e6`](https://bscscan.com/token/0x92516e0ddf1ddbf7fab1b79cac26689fdc5ba8e6) LayerZero OFT, `totalSupply()` 457.0M, owner [2-of-2 Safe](https://bscscan.com/address/0x3f30376053f29f20fd3a015f96d4800092512896) |
| **ATH** $0.1156 (26 May 2025, TGE day) · now −94.3% | **Huma Squads vaults** ≈ 5.88B (≈ 59% of supply), see Holdings |
| **Holders** Not found (no free Solana holder count) | **Exchanges in top 20** Binance 3 · Bithumb · Bitget |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees (yield credited to PST/mPST), last 30 days / 1 year | **$2.83M / $18.2M** | [Tier A] [DefiLlama Huma](https://defillama.com/protocol/huma-finance), read 16 Nov 2026 5:26 AM MST |
| Protocol revenue, last 30 days / 1 year | **$0 / $0** | [Tier A] DefiLlama: "Zero — the permissionless pool has no protocol fee configured; all PayFi yield flows to LPs." |
| Holders revenue | **$0** | [Tier A] DefiLlama `dailyHoldersRevenue` |
| Buyback | Proposed only: "a portion of Vault income goes to $HUMA buybacks" (Project Flywheel, Oct 2025); no buyback found on-chain | [Tier A] [Huma blog](https://blog.huma.finance/introducing-project-flywheel) |
| TVL | **$367M** (Solana $237M, Ethereum $125M, Stellar $2.7M, Monad $2.1M) | [Tier A] DefiLlama |

**What it means:** The business is real, but all of its yield goes to LPs, and the token's value case rests on staking "Feathers", governance that is not live yet, and a buyback that is still a plan. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** All yield goes to LPs; the buyback is still a plan.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Entity | **Huma Foundation** issues the token. The credit business runs through **Arf**, a Swiss-regulated entity, and TradeFlow (trade finance) | [Tier A] [Huma blog, 25 Aug 2026](https://blog.huma.finance/huma-built-payfi.-now-institutions-build-on-huma) |
| Team | Public co-founders; the company is four years old (founded April 2022) | [Tier A] same post |
| Governance | Not live. The Foundation promised "onchain governance tools by Nov. 26, 2026" | [Tier A] [Built to Last](https://blog.huma.finance/huma-build-to-last) |
| Wallet disclosure | Solscan carries named Squads vaults ("Protocol Treasury", "Huma Investors", "Huma Internal", "Ecosystem-unlocked", "Huma Treasury Unlocked", "Huma Ecosystem/Treasury", "MM & Onchain Liquidity", and per-person "Team-…" vaults) | [Tier B] Solscan account labels, 16 Nov 2026 |

**What it means:** A known team, a regulated operating arm and unusually open wallet labelling. However, the Foundation controls every token decision until governance ships.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

| Vault (Squads label) | HUMA | Control |
|---|---:|---|
| "Protocol Treasury" [`7tsye…ZmV`](https://solscan.io/account/7tsyeZinyiUFQUK1k9pUvyjKuWDw9E1GUjpsRBtLmZV) | **2,087,065,118** | Squads [3-of-4](https://solscan.io/account/7f4sJXNiDFJSV5kLbtxq4JW4iw1yyBkrFpqRgteE54cE), timelock 0 |
| "Huma Investors" [`DZaR8…R44U`](https://solscan.io/account/DZaR8LfPXAQfqFptp34zy5TcePCbZw9piYSqXePRR44U) | **1,588,478,202** | Squads [3-of-4](https://solscan.io/account/5ekZ81AsgM1Ja8b11tXXNS32G9zQ56wcQJc7j9ZW5W1r), timelock 0 |
| "Huma Internal" [`2uH2d…wwP`](https://solscan.io/account/2uH2dToBgDnKkc9bRfojE9wGwqBUvGVarjF45WxwXwwP) | 694,119,943 | Squads [3-of-4](https://solscan.io/account/4iMTnZxZ13k44BV3Y5dzW4JfPY4hXm4j2Ttwt5bzJgJr), timelock 0 |
| "Ecosystem-unlocked" [`8fcsW…c1z5`](https://solscan.io/account/8fcsW3dpTMLbvJ8pypVyJZ5bBLK5LRcWASQRv7vic1z5) | 562,006,928 | Squads |
| "Huma Treasury Unlocked" [`4YkUG…aiq`](https://solscan.io/account/4YkUGNThbLnTLNs8r5q1348tT6HK2Mf9vUMiHwsj8aiq) | 441,241,581 | Squads [4-of-5](https://solscan.io/account/FCfvg4xjHcZGk9vuh673q9Pae4ghZReFrKtFGVaFCerx), timelock 0 |
| "Huma Ecosystem/Treasury" [`ApNmb…edh`](https://solscan.io/account/ApNmbpGbbtuHiEkYL86AAJkQhEjKQ1ja3u3PZfiApedh) | 378,750,000 | Squads [3-of-4](https://solscan.io/account/57roTmQveiH5rrWxW2FkqoV6FQfJAvu2Vq8dgQFnP1M2), timelock 0 |
| "MM & Onchain Liquidity" [`5UicV…dxUF`](https://solscan.io/account/5UicVi3dLBCZRsSjftWABgFGPHKYRVqRkdYeXMsYxdUF) | 130,000,000 | Squads |
| **Labelled Huma vaults, total** | **≈ 5.88B (≈ 59% of supply)** | |
| Funded by those vaults on 30 Sep – 6 Oct 2026, unlabelled | **671.5M** | [`3xfvk…`](https://solscan.io/account/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3) 471.5M plus five wallets holding 200M (see Selling) |
| Team vesting | Team tokens left "Huma Internal" in a single [16 May 2025 split](https://solscan.io/tx/4KQfsyZkhxyuQ3WwDs1MkTZt5t9ZUgtWi59WHbfGt6TYsN7icSasY1cV7bwQbXTgQsRCCFvmvPxjoHDv4E4pTTHS) to per-person vaults. Their balances now sit in **Magna** vesting accounts (e.g. [`2wt4…`](https://solscan.io/account/2wt4GcqWfgwamCptZoX2ULyzYuQDUtskG8WHaACjxnDa) and [`5tbU…`](https://solscan.io/account/5tbUhbMkTxsxjivDr4e1K6pSaMGcYsCbaCU4R4PcarYS), 483.5M each) | on-chain vesting (program "Magna Core") |

**What it means:** The labelling is unusually honest, and the team's tokens do sit in an on-chain vesting program. But the **investor allocation (20.6%) sits in a plain 3-of-4 Squads vault with no timelock**, so the 26 Nov "lock" is enforced by policy, not code, and 471.5M of it has already moved to a wallet nobody has named. Insiders control about 59% of supply and can move it at will.

## 📉 Selling behavior — Do insiders sell into pumps? · 5/10 · ❌ FAIL

*Pump test uses Gate HUMA/USDT daily closes (UTC), which start 26 May 2025 (TGE). 70 of the last 365 days were pump days. Every HUMA transfer of the seven labelled vault token accounts was traced (108 transactions, full history), plus one hop from each recipient that took more than 1M.*

| Day (UTC) | Route | HUMA | 5-day change | Pump? | Outcome |
|---|---|---:|---:|---|---|
| 22–26 May 2025 (pre-TGE / TGE) | Ecosystem/Treasury → fresh wallets → **Binance 2** (e.g. [250M in](https://solscan.io/tx/4pjePChWgdQfNxARUbM5DitXGbxhs91FA6R7iR1tYuV5YgXk5sesEomaJUgC2XgwTn692gmemYSQo9jAEpajPs1H), [250M to Binance](https://solscan.io/tx/5kFyhFNUsBJ26rkgnm51kAe8ndzHQoaC5jtn6fNfksqzp8UL3U3Zk41aX4e1T96eQCWTtuUn76Ytsx2tve3zB1Nm)), OKX hot wallets (85M), Meteora pools (≈ 270M) and Bybit (15.1M, [tx](https://solscan.io/tx/5faEftiMQrBBr89eksXKPWgAVPM7sr3r3e8TeLk9JKaSighyuoX65rNRSPyzbEMfHPgqcED3gub9XyafRxHj7Dqd)) | ≈ 354M to Binance | n/a (no price yet) | n/a | Launch allocations: exchange airdrops, listing and liquidity [purpose Unverified] |
| 4 Jul 2025 | "MM & Onchain Liquidity" → [`611J…`](https://solscan.io/account/611J4HQBM1ApG2ew3WJd8QDG8EtnLPymwF7mo16gkRho) → **Bithumb Hot Wallet 1** ([tx](https://solscan.io/tx/4uYHVK2LKgSdQTJuY5Md3K5gWDqgrG3rC1tUFkud8tapUaPncVuzjR9WHefb4W2aiGLRvn91zLfgPd7Dr7zkaaTD)) | 5,000,000 | −12.7% | No | Market-making vault; likely Bithumb listing inventory |
| 29 Aug 2025 | Ecosystem/Treasury-funded [`7MXf…`](https://solscan.io/account/7MXfVa5C6cT6t4kE6uPLMzdyY2e3Kvje5k6zBqGJNaZT) → [`3C4e…`](https://solscan.io/account/3C4etxNWwYBjMtan43qaDzsFePLsZvrDsXsKdKPEpy3L) → **Binance 2** ([tx](https://solscan.io/tx/2G7rrhZhyUpdcKZtWACCcpqf29x5bry6WwzCTqntYvKycJPVsCkVrK5SHwNftyJ1773EVe9Zq9tMf79VG6Tt7bKC)) | 40,000,000 | −9.1% | No | Arkham: unlabelled sender, recipient a Binance deposit ([Arkham](https://intel.arkm.com/explorer/address/7MXfVa5C6cT6t4kE6uPLMzdyY2e3Kvje5k6zBqGJNaZT)). Recipient unknown (Arkham item) |
| 16 Apr 2026 | **GSR** Fireblocks custody → Huma wallet [`GBv2…`](https://solscan.io/account/GBv2Vt19CGAmuJMmH4y3xdRz1irvc3dmitfPenYEjmbX) ([30M back](https://solscan.io/tx/2SazAH8y1n5gCxDXeErzToYQnvysC8G3u4jTgb4SK8XVAgoJBgmCWEz5CMGCmkAsriKQ9ybHkT1kqCQxGvHxTa65)) → MM vault 15M ([tx](https://solscan.io/tx/4Qj8Y6mRSxvjuHyEyiqEnCD9LPtX7HnkD82esPfYjmuyPgbhQUHNz6WX7Ne88gSA8vU76a7Pc1UNKegvpyHGCXRz)), and 15M to [`HRsH…`](https://solscan.io/account/HRsH5vTBW9wfv2NUfYUN6DJvXsHsndot1s6a1YJ4GtB8), which split it four ways the next day (see the 17 Apr row) | 30,000,000 | +22.8% | 🔴 Yes | **Inbound**: a market-maker loan coming back. But half of it was sent on toward exchanges within a day |
| 17 Apr 2026 | `HRsH…` → Binance deposit [`HfVU…`](https://solscan.io/account/HfVUW4widrC95Tu7oXkkwe9npJGYj8qFxL98w75jqZ9C) ([1,000](https://solscan.io/tx/4FvVdHbetwknyuhxKH3TBoeD2qjCY1gBEuRrUCktkjrgzCYLyZNKufvDa4L4JY4i6xNKKiUNhbHN4aDvkE3ubDN8) · [4,999,000](https://solscan.io/tx/3YE8PiQkafUkSJGaCigrDbereMiWRNQRftZ4yKzekNEMan7QDV7BYmjHmmGpAHDcRDiPtaBRpXvDLpXGbYT9gFa6)), Bitget deposit [`4SDL…`](https://solscan.io/account/4SDLqA3Z42aisEvWN2uARXAUdZ214U89CUnr9edd6vug) ([4,000,000](https://solscan.io/tx/oDo7NDwLA7ViP6BEGEM8uuwfN2yiVWmtuPYF1piQngnqd7H8y2EpsF4Cx9JBudYTxENZNg4pvg5kYWBfk2hfJuF)), Bybit deposit [`DaF3…`](https://solscan.io/account/DaF3kQW1fGbmjPCd7TEbLrpvac9KMTbmHDaq5eJR4TZx) ([2,000,000](https://solscan.io/tx/5XxVeg6VjayLqs1W43sxxdY2RzLSBF9NbX22hvJvzEdXLvnJu1nvNmyteyMV3SSuHyQGxPFUBdsnnvBWz6JLfmQd)); plus 4,000,000 to unlabelled [`AS56…`](https://solscan.io/account/AS565JcHANEtzU3uGaiQFvJcUhserfHKZLgHnGyjR3RQ) ([tx](https://solscan.io/tx/2tL4LwmcHeUnNZjHCsPE8QqyB4G27DLYGMTpYrFDQnTXkKZk9n8TSLX4H1BE4DA3FoyiWnd9tHkD7nRQ6NHDtfUW)) | 11,000,000 to exchanges | +6.0% | No | Deposit labels per Arkham ([HRsH on Arkham](https://intel.arkm.com/explorer/address/HRsH5vTBW9wfv2NUfYUN6DJvXsHsndot1s6a1YJ4GtB8)); fits fresh market-maker inventory on three venues [Unverified] |
| 30 Sep 2026 | "Huma Treasury Unlocked" → [`E9gm…`](https://solscan.io/account/E9gmN6epA4X3Cgc5NwfjcGqHSHzEqUVr1qmeHU62guyk) ([tx](https://solscan.io/tx/4ZzhJFEyZXACAmxX45LaByMRvXVkKvz96KYjMH9R4LidsaSCakRz2BQAu3LqA2qQj2v4DU3hPPyisCqcYdk4DzGk)) | 49,999,920 | +21.6% | 🔴 Yes | Still held |
| 1 Oct 2026 | Treasury Unlocked → [`2ADn…`](https://solscan.io/account/2ADnqYntRmDcDDKEcLgk2TyXN9GBMjqr42GuPJ7MJzKj) ([tx](https://solscan.io/tx/dRmSHqy8mjUTn59VobKWEuzNvc29onTyv1qWwxHNwRizBTFf9NERyXi7xqUDfTUEm4DJUHQS1dp6cXbBSDmq3D9)) | 29,999,900 | +16.3% | 🔴 Yes | Still held |
| 1 Oct 2026 | **"Huma Investors"** → [`3xfvk…`](https://solscan.io/account/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3) ([tx](https://solscan.io/tx/2PEgFDTXNSiPi4AyjjDAFqXjo9JZptMaKhhXgzGkzHb3qGyo4EFMWyqUM6uACZQiBGKsYGgeA2LYab4LTmeodxxp)) | **471,521,700** | +16.3% | 🔴 Yes | Still held; test send of 98 HUMA on [17 Aug](https://solscan.io/tx/22KbtUQvh4CD6i86wrCGWRTFiFkYX6TN8oSpu8crgakvjgtfjV4G9UxUxPQ5YRaiPFWe2zzTxHd75v71eHMKYtbt) |
| 3 Oct 2026 | Treasury Unlocked → [`GZw6…`](https://solscan.io/account/GZw6S8U8ZCXAkaQL5oTh57aCDWjrEWXHLp57XGJbURwW) ([tx](https://solscan.io/tx/5P3W1rdhRh4kFDc1LnVBztvri4QBNY3AxbkjAN1phLkRCzJiA4jhc7SGEvffixu7bkdrGpNsMDRQiyNi1DvDcJUq)) | 59,999,890 | +18.2% | 🔴 Yes | Still held |
| 4 Oct 2026 | Treasury Unlocked → [`4s4T…`](https://solscan.io/account/4s4TpJZ6CDkHA2FqrcWCDy2f9wkv5LqqJH28G8KgJF2c) ([tx](https://solscan.io/tx/2Yeab443TXmj9hn52NFFryjQfN9Zu9jqJq1fWbmzQqXVYFaFYBoUZwRF7wH3JXPPDW9yhev4oY4pdnckXmTDXmPn)) | 29,999,970 | +20.4% | 🔴 Yes | Still held |
| 6 Oct 2026 | Treasury Unlocked → [`6Hr5…`](https://solscan.io/account/6Hr5GQh57cQwMYkVs1QfSoT1tv74F2P7YeLrpfEHT2Zu) ([tx](https://solscan.io/tx/2LJXPvuCGdq7WCwpE3f7DWCecJRtKJsA2YLxJ9o4xWbPCKTaWbBiHDGMkqc1AR7cpCr584bsEpmMHUHWnJWt1wns)) | 29,999,940 | −10.0% | No | Still held |

- **The team's account of the crash:** a Huma co-founder said that an early LP's wallet was hacked on 22 Oct 2026 and about 12M airdropped HUMA were sold. He blamed the rest of the drop on short sellers: open interest went from ~620M to 1.1B tokens between 2 and 7 Nov, with perp volume at 7–10x spot. He also said the Foundation and its affiliates had made **"no HUMA transactions/trades in the past three months"** and had no plans to sell in the unlock window ([Phemex](https://phemex.com/news/article/huma-finance-blames-wallet-hack-for-huma-price-crash-denies-foundation-selling-103288) · [TokenPost](https://www.tokenpost.com/news/investing/55411), Tier B ×2).
- **What the chain shows:** within those three months, the vaults moved **671.5M HUMA to six fresh wallets**. These were transfers, not trades on any venue we could see, and none of the six wallets has sent HUMA onward. So the "no trades" claim survives this check, but the transfers themselves are undisclosed.
- **Quarterly sends:** "Protocol Treasury" pays a Huma-vanity wallet [`HumaDeaz…`](https://solscan.io/account/HumaDeazKoZZkTyE9MYcQHKxdQm74Fm6DSFs8nawPNTt) each quarter (e.g. [157.1M on 1 Sep 2026](https://solscan.io/tx/2WfehVnmEmfScNHTDpQjCeXA13rUspDrotcXNSpgk9npn5WqHha2rruzcWyFXsCmHfE2vRDb3qgfa5e8yeYDfDzQ)). The timing matches the Feathers airdrop seasons [Unverified]; Arkham shows Ecosystem-unlocked and Protocol Treasury flows but does not call it the airdrop distributor ([Arkham](https://intel.arkm.com/explorer/address/HumaDeazKoZZkTyE9MYcQHKxdQm74Fm6DSFs8nawPNTt)).

**What it means:** No Huma vault was caught depositing to an exchange on a pump day. The one pump-day flow with an exchange-side party was a **GSR loan coming back**. **Corrected after the Arkham pass:** this is not purely inbound. Huma passed 15M of the returned 30M to `HRsH…` on the same pump day, and on 17 Apr (+6.0%, not a pump day) `HRsH…` sent 11M into Binance, Bybit and Bitget deposit addresses and 4M to an unlabelled wallet. That looks like the loan being re-deployed to new market makers' exchange accounts, but no disclosure says so [Unverified]. It is about 0.1% of supply and the deposits missed the pump day, so it does not move the score. But four pump days in a row saw 671.5M tokens leave the vaults for unnamed wallets, three weeks before the market collapsed and eight weeks before the unlock. "Not proven" counts as a fail. **5, unchanged after the Arkham pass.** Arkham ([Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account)) confirms the vault names ("Huma Investors", "Huma Treasury Unlocked", "Ecosystem-unlocked", Huma Finance "Protocol Treasury") but names none of the six recipient wallets: [`3xfvk…`](https://solscan.io/account/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3) ([Arkham](https://intel.arkm.com/explorer/address/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3), 471.522M), [`E9gmN…`](https://solscan.io/account/E9gmN6epA4X3Cgc5NwfjcGqHSHzEqUVr1qmeHU62guyk) ([Arkham](https://intel.arkm.com/explorer/address/E9gmN6epA4X3Cgc5NwfjcGqHSHzEqUVr1qmeHU62guyk)), [`2ADnq…`](https://solscan.io/account/2ADnqYntRmDcDDKEcLgk2TyXN9GBMjqr42GuPJ7MJzKj) ([Arkham](https://intel.arkm.com/explorer/address/2ADnqYntRmDcDDKEcLgk2TyXN9GBMjqr42GuPJ7MJzKj)), [`GZw6S…`](https://solscan.io/account/GZw6S8U8ZCXAkaQL5oTh57aCDWjrEWXHLp57XGJbURwW) ([Arkham](https://intel.arkm.com/explorer/address/GZw6S8U8ZCXAkaQL5oTh57aCDWjrEWXHLp57XGJbURwW)), [`4s4Tp…`](https://solscan.io/account/4s4TpJZ6CDkHA2FqrcWCDy2f9wkv5LqqJH28G8KgJF2c) ([Arkham](https://intel.arkm.com/explorer/address/4s4TpJZ6CDkHA2FqrcWCDy2f9wkv5LqqJH28G8KgJF2c)), [`6Hr5G…`](https://solscan.io/account/6Hr5GQh57cQwMYkVs1QfSoT1tv74F2P7YeLrpfEHT2Zu) ([Arkham](https://intel.arkm.com/explorer/address/6Hr5GQh57cQwMYkVs1QfSoT1tv74F2P7YeLrpfEHT2Zu)). So who received the 671.5M is still open. **Symbol note:** Arkham's Solana portfolio shows these balances as HUMA, but the matching rows on its transfer pages show the symbol **HOLD**. We read the HOLD rows as the same HUMA mint because the amounts and counterparties match the Solscan HUMA transfers above, but Arkham's own display is inconsistent.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate HUMA/USDT daily closes.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- **Fixed supply:** 10B, with mint authority and freeze authority both null ([mint](https://solscan.io/token/HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw)). The BSC OFT supply (457.0M) equals the HUMA held in the Solana OFT escrow [`dSeoc…`](https://solscan.io/account/dSeocUVUmgsnQW2mgK6ywsvR9oDF3TANdohBsrQqGkd) (457,002,912), so there is no double count.
- **Allocation:** investors 20.6% (2.06B) and team & advisors 19.3% (1.93B) unlock over 12 quarterly releases after the cliff. **First unlock: 26 Nov 2026**, about 171.67M (investors) plus 160.83M (team) ([Tokenomist](https://tokenomist.ai/huma-finance/tokenomics) · [Tokenomics.com](https://app.tokenomics.com/tokenomics/huma-finance/unlocks), Tier B ×2). Huma itself confirms the date: the team, advisors and major investors agreed to move the first unlock "from May 26 to Nov. 26, 2026" ([Built to Last](https://blog.huma.finance/huma-build-to-last), Tier A).
- **Overhang:** about 332M per quarter against 1.733B circulating, or **+19% of float every quarter** for three years. Only 17.3% of supply circulates today.
- **Emissions cut:** Maxi mode (mPST) was retired, and its rewards ended 26 May 2026 ([Built to Last](https://blog.huma.finance/huma-build-to-last)).

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $5.06M of volume in 24h on an $11.47M cap (44% turnover). Huma says perp volume ran **7–10x spot** in early November (Tier B).
- Top-20 holders include Binance 3 (226.7M), Bithumb Hot Wallet 1 (138.9M) and Bitget (107.1M) (Solscan labels). Meteora HUMA-USDC pools were seeded from the Ecosystem/Treasury at launch.
- The price is down **−94.3% from ATH** and **−77% in 30 days**. On Gate, the daily close fell from $0.02835 (31 Oct) to $0.006558 (15 Nov 2026).

## 🧑‍💻 Product & development · 7/10 · ✅ PASS

- **Huma 2.0** (permissionless PST on Solana) lends stablecoins to licensed payment institutions for T+0 cross-border settlement, with each credit repaid in 1–7 days. Trade finance runs with TradeFlow, with insured cargo and 30–90 day tenors.
- Launched on Chainlink CCIP (June 2026) with an Ethereum Morpho market. PST is also on Fluid, Kamino and RateX, and in RockawayX RFQ ([25 Aug 2026 post](https://blog.huma.finance/huma-built-payfi.-now-institutions-build-on-huma)).
- PST reserves are verified by Accountable, with monthly attestations by Swiss audit firm Wadsack (same post).

## 🤝 Adoption & customers · 7/10 · ✅ PASS

- TVL is **$367M** (DefiLlama, Tier A). Huma also reports PST at a **$220M+** market cap, **$17B+** of cumulative transaction volume, **$1B+ a month**, "zero credit defaults to date" and 100k+ LPs (Tier A, Huma's own figures; the default record is [Unverified] independently).
- Named partners: Bitwise, Sentora, Galaxy Digital, Coinbase Asset Management, RockawayX and Circle Payments Network (via Arf).

## 🛡️ Security & audits · 7/10 · ✅ PASS

- Solana programs are audited by **Halborn** and **Sec3**, including an incremental review on [8 Jun 2026](https://github.com/sec3-service/reports/blob/master/reports/sec3_huma_permissionless_pr407_incr_20260608.pdf). EVM contracts are audited by **Spearbit** ([report](https://github.com/00labs/huma-contracts-v2/blob/develop/audit/spearbit.pdf)) and Stellar contracts by **Certora** ([docs list](https://docs.huma.finance/ecosystem-resources/security-audits)).
- The docs say admin roles are multisigs and that the design keeps the treasury separate from LP funds.
- No protocol exploit was found. The 22 Oct 2026 incident was one LP's own wallet (Tier B).
- The BSC token is owned by a **2-of-2** Safe ([`0x3f30…2896`](https://bscscan.com/address/0x3f30376053f29f20fd3a015f96d4800092512896)), and the Solana vaults have **timelock 0**.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Arf, the main credit counterparty, is Swiss-regulated (Tier A, Huma).
- Huma retired the Maxi mode and the PST staking boost "to better comply with evolving global regulations" ([Built to Last](https://blog.huma.finance/huma-build-to-last)).
- HUMA is described as "a utility and governance token". No legal opinion or regulator filing for the token was found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| **26 Nov 2026** | First investor and team unlock (~332M), then quarterly releases for 3 years |
| By 26 Nov 2026 | On-chain governance tools promised |
| 2026 (no date) | "New ways to use HUMA" and "deflationary mechanics": no details yet |
| Quarterly | Protocol Treasury → `HumaDeaz…` distribution (airdrop seasons, inferred) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None on the protocol; one LP wallet hack (22 Oct 2026, Tier B) |
| Team wallet → exchange during a pump | 🟡 No vault → exchange deposit found on a pump day; but [471.5M from "Huma Investors"](https://solscan.io/tx/2PEgFDTXNSiPi4AyjjDAFqXjo9JZptMaKhhXgzGkzHb3qGyo4EFMWyqUM6uACZQiBGKsYGgeA2LYab4LTmeodxxp) and 200M from "Treasury Unlocked" went to fresh wallets on pump days |
| Live mint path | 🟢 None: [mint authority null](https://solscan.io/token/HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw) |
| Treasury in single-key wallets | 🟡 Labelled vaults are 3-of-4 / 4-of-5 Squads with 0 timelock; 671.5M sits in six unlabelled wallets of unknown control |
| Unlock cliff | 🔴 [26 Nov 2026](https://blog.huma.finance/huma-build-to-last): investor lock not enforced by a vesting contract |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| `HRsH…` (received 15M of a returned GSR loan) | Huma-funded wallet | Solana RPC + Arkham | medium | no | None: its exchange sends were on 17 Apr, not a pump day |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Solana RPC (Tatum public gateway): `getTokenSupply`, mint account (`mintAuthority`/`freezeAuthority`), `getTokenLargestAccounts`, `getSignaturesForAddress` and `getTransaction` for the full history of all seven labelled vault token accounts (108 tx) and every recipient over 1M; Squads v4 multisig account data (threshold, timelock, member count); read 16 Nov 2026 ~7:00–8:00 AM MST
- [Tier A] BSC RPC (publicnode): OFT `totalSupply()`, `decimals()`, `owner()`; Safe `getThreshold()`/`getOwners()`; Etherscan v2 `getsourcecode` (LayerZero OFT), 16 Nov 2026
- [Tier B] Solscan account labels, 16 Nov 2026: the Squads vault names above, "Binance 2", "Binance 3", "Bithumb Hot Wallet 1", "Bitget Exchange", "OKX: Hot Wallet 5", "OKX Hot Wallet (C68a6)", "Bybit Hot Wallet (AC5RD)", "GSR Markets: Fireblocks Custody", "Meteora (HUMA-USDC) Market", "Magna Core", "Huma Staking", "HUMA LayerZero OFT Program"
- [Tier A] [DefiLlama Huma](https://defillama.com/protocol/huma-finance) fees, revenue and TVL with methodology, 16 Nov 2026 5:26 AM MST
- [Tier A] Huma blog: [Built to Last (17 Apr 2026)](https://blog.huma.finance/huma-build-to-last) · [Project Flywheel](https://blog.huma.finance/introducing-project-flywheel) · [Staking rewards](https://blog.huma.finance/huma-staking-rewards) · [Next chapter (25 Aug 2026)](https://blog.huma.finance/huma-built-payfi.-now-institutions-build-on-huma); [Huma docs, security & audits](https://docs.huma.finance/ecosystem-resources/security-audits)
- [Tier B] [Tokenomist](https://tokenomist.ai/huma-finance/tokenomics) · [Tokenomics.com unlocks](https://app.tokenomics.com/tokenomics/huma-finance/unlocks) · [Phemex News](https://phemex.com/news/article/huma-finance-blames-wallet-hack-for-huma-price-crash-denies-foundation-selling-103288) · [TokenPost](https://www.tokenpost.com/news/investing/55411)
- [Tier A] CoinGecko `huma-finance` market data (16 Nov 2026 5:26 AM MST); Gate HUMA/USDT daily candles (UTC)
- [Tier B] Arkham, read 16 Nov 2026 ~7:07–7:18 AM MST (signed-in account): Squads vault labels "Huma Investors", "Huma Treasury Unlocked", "Ecosystem-unlocked", "Protocol Treasury" · unlabelled [`3xfvk…`](https://solscan.io/account/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3) ([Arkham](https://intel.arkm.com/explorer/address/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3)), five recipients (linked in Selling), [HumaDeaz…](https://intel.arkm.com/explorer/address/HumaDeazKoZZkTyE9MYcQHKxdQm74Fm6DSFs8nawPNTt), [Huma9X… (Binance hot wallet activity)](https://intel.arkm.com/explorer/address/Huma9XhQaaiHKS22UrNPWtECqMHNLYvqqyDjvkNsDyYE), [7MXf… (40M to a Binance deposit)](https://intel.arkm.com/explorer/address/7MXfVa5C6cT6t4kE6uPLMzdyY2e3Kvje5k6zBqGJNaZT), [HRsH… (Binance/Bybit/Bitget deposits)](https://intel.arkm.com/explorer/address/HRsH5vTBW9wfv2NUfYUN6DJvXsHsndot1s6a1YJ4GtB8) · BSC owner Safe [0x3f30…](https://intel.arkm.com/explorer/address/0x3f30376053f29f20fd3a015f96d4800092512896) shows no assets. Arkham shows the token as HUMA in portfolios and HOLD in transfer rows. First transfer page only
- [Tier A] Solana RPC `getSignaturesForAddress` / `getTransaction` for `HRsH…` (16–17 Apr 2026 outflows), read 16 Nov 2026 ~7:25 AM MST
- [Unverified] who controls `3xfvk…` and the five Treasury Unlocked recipients; whether `HumaDeaz…` is the airdrop distributor; what the launch-time sends to Binance/OKX/Bybit were for; Huma's zero-default record

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Supply fixed at 10B; mint authority null | [mint](https://solscan.io/token/HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw) | A | 16 Nov 2026 |
| 2.06B moved "Huma Internal" → "Huma Investors" (21 May 2025) | [tx](https://solscan.io/tx/2HAR2k2XQFCaHd8TjsF6aQyUsLAoc7stqRz8i54VzyLZuQ1Y2d4mhXBzm8B4jVSLYkcqf4HzWKSh54EguUJy7h7x) | A + B label | 16 Nov 2026 |
| "Huma Investors" is a 3-of-4 Squads multisig with timelock 0 | [multisig](https://solscan.io/account/5ekZ81AsgM1Ja8b11tXXNS32G9zQ56wcQJc7j9ZW5W1r) · [vault](https://solscan.io/account/DZaR8LfPXAQfqFptp34zy5TcePCbZw9piYSqXePRR44U) | A | 16 Nov 2026 |
| 1 Oct 2026 pump day: Investors 471.5M → `3xfvk…` (still held) | [tx](https://solscan.io/tx/2PEgFDTXNSiPi4AyjjDAFqXjo9JZptMaKhhXgzGkzHb3qGyo4EFMWyqUM6uACZQiBGKsYGgeA2LYab4LTmeodxxp) · [wallet](https://solscan.io/account/3xfvkYgkm6XEchUiTdTJicg7spq8jLj45e5oKqpnUqF3) | A | 16 Nov 2026 |
| 30 Sep – 6 Oct 2026: Treasury Unlocked 200M → five wallets (still held) | [30 Sep](https://solscan.io/tx/4ZzhJFEyZXACAmxX45LaByMRvXVkKvz96KYjMH9R4LidsaSCakRz2BQAu3LqA2qQj2v4DU3hPPyisCqcYdk4DzGk) · [1 Oct](https://solscan.io/tx/dRmSHqy8mjUTn59VobKWEuzNvc29onTyv1qWwxHNwRizBTFf9NERyXi7xqUDfTUEm4DJUHQS1dp6cXbBSDmq3D9) · [3 Oct](https://solscan.io/tx/5P3W1rdhRh4kFDc1LnVBztvri4QBNY3AxbkjAN1phLkRCzJiA4jhc7SGEvffixu7bkdrGpNsMDRQiyNi1DvDcJUq) · [4 Oct](https://solscan.io/tx/2Yeab443TXmj9hn52NFFryjQfN9Zu9jqJq1fWbmzQqXVYFaFYBoUZwRF7wH3JXPPDW9yhev4oY4pdnckXmTDXmPn) · [6 Oct](https://solscan.io/tx/2LJXPvuCGdq7WCwpE3f7DWCecJRtKJsA2YLxJ9o4xWbPCKTaWbBiHDGMkqc1AR7cpCr584bsEpmMHUHWnJWt1wns) | A | 16 Nov 2026 |
| Team split into per-person vaults, now in Magna vesting accounts | [16 May 2025 tx](https://solscan.io/tx/4KQfsyZkhxyuQ3WwDs1MkTZt5t9ZUgtWi59WHbfGt6TYsN7icSasY1cV7bwQbXTgQsRCCFvmvPxjoHDv4E4pTTHS) · [`2wt4…`](https://solscan.io/account/2wt4GcqWfgwamCptZoX2ULyzYuQDUtskG8WHaACjxnDa) | A + B label | 16 Nov 2026 |
| `HRsH…` sent 11M to Binance/Bybit/Bitget deposits and 4M to an unlabelled wallet on 17 Apr 2026 | [Binance 4.999M](https://solscan.io/tx/3YE8PiQkafUkSJGaCigrDbereMiWRNQRftZ4yKzekNEMan7QDV7BYmjHmmGpAHDcRDiPtaBRpXvDLpXGbYT9gFa6) · [Bitget 4M](https://solscan.io/tx/oDo7NDwLA7ViP6BEGEM8uuwfN2yiVWmtuPYF1piQngnqd7H8y2EpsF4Cx9JBudYTxENZNg4pvg5kYWBfk2hfJuF) · [Bybit 2M](https://solscan.io/tx/5XxVeg6VjayLqs1W43sxxdY2RzLSBF9NbX22hvJvzEdXLvnJu1nvNmyteyMV3SSuHyQGxPFUBdsnnvBWz6JLfmQd) · [4M other](https://solscan.io/tx/2tL4LwmcHeUnNZjHCsPE8QqyB4G27DLYGMTpYrFDQnTXkKZk9n8TSLX4H1BE4DA3FoyiWnd9tHkD7nRQ6NHDtfUW) · [Arkham deposit labels](https://intel.arkm.com/explorer/address/HRsH5vTBW9wfv2NUfYUN6DJvXsHsndot1s6a1YJ4GtB8) | A + B label | 16 Nov 2026 |
| GSR returned 30M on the 16 Apr 2026 pump day | [GSR → Huma](https://solscan.io/tx/2SazAH8y1n5gCxDXeErzToYQnvysC8G3u4jTgb4SK8XVAgoJBgmCWEz5CMGCmkAsriKQ9ybHkT1kqCQxGvHxTa65) · [→ MM vault](https://solscan.io/tx/4Qj8Y6mRSxvjuHyEyiqEnCD9LPtX7HnkD82esPfYjmuyPgbhQUHNz6WX7Ne88gSA8vU76a7Pc1UNKegvpyHGCXRz) | A + B label | 16 Nov 2026 |
| Launch: 250M Ecosystem/Treasury → `DiPHe4…` → Binance 2 (22 May 2025) | [in](https://solscan.io/tx/4pjePChWgdQfNxARUbM5DitXGbxhs91FA6R7iR1tYuV5YgXk5sesEomaJUgC2XgwTn692gmemYSQo9jAEpajPs1H) · [out](https://solscan.io/tx/5kFyhFNUsBJ26rkgnm51kAe8ndzHQoaC5jtn6fNfksqzp8UL3U3Zk41aX4e1T96eQCWTtuUn76Ytsx2tve3zB1Nm) | A + B label | 16 Nov 2026 |
| MM vault 5M → Bithumb (4 Jul 2025, not a pump day) | [tx](https://solscan.io/tx/4uYHVK2LKgSdQTJuY5Md3K5gWDqgrG3rC1tUFkud8tapUaPncVuzjR9WHefb4W2aiGLRvn91zLfgPd7Dr7zkaaTD) | A + B label | 16 Nov 2026 |
| 40M → Binance 2 via `3C4e…` (29 Aug 2025, not a pump day) | [tx](https://solscan.io/tx/2G7rrhZhyUpdcKZtWACCcpqf29x5bry6WwzCTqntYvKycJPVsCkVrK5SHwNftyJ1773EVe9Zq9tMf79VG6Tt7bKC) | A + B label | 16 Nov 2026 |
| Binance 2 sent 300M to Huma wallet `Huma9X…`, bridged 299M to BSC (18 Nov 2025) | [in](https://solscan.io/tx/4YYYPw7Pp9uU2Xn3ZkXfMcuye1JH9jkF5r5V3Q9EkXPMJBsKPZLghE38wbfTPoAfb34Nrf3UkUiWwyvjZxgMZta9) · [bridge](https://solscan.io/tx/3W852Pe3FUVpuupXMjUaQo42fMygxTT7Kb4eD3xRyaGMaY14QPaqeArGCPczNv132f1dkhiu9LtVgV3aYsNsUcp4) | A + B label | 16 Nov 2026 |
| BSC OFT supply 457.0M = Solana OFT escrow; owner 2-of-2 Safe | [BSC token](https://bscscan.com/token/0x92516e0ddf1ddbf7fab1b79cac26689fdc5ba8e6) · [Safe](https://bscscan.com/address/0x3f30376053f29f20fd3a015f96d4800092512896) · [escrow](https://solscan.io/account/dSeocUVUmgsnQW2mgK6ywsvR9oDF3TANdohBsrQqGkd) | A | 16 Nov 2026 |
| Protocol revenue $0; fees $18.2M (1y) to LPs | [DefiLlama](https://defillama.com/protocol/huma-finance) | A | 16 Nov 2026 5:26 AM MST |
| First unlock moved to 26 Nov 2026; governance by 26 Nov | [Built to Last](https://blog.huma.finance/huma-build-to-last) | A | 16 Nov 2026 |
| Foundation: no HUMA trades in 3 months; LP wallet hack 22 Oct | [Phemex](https://phemex.com/news/article/huma-finance-blames-wallet-hack-for-huma-price-crash-denies-foundation-selling-103288) · [TokenPost](https://www.tokenpost.com/news/investing/55411) | B ×2 | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026** (first transfer page per wallet). Vault labels confirmed. Not named: `3xfvk…` and the five Treasury Unlocked recipients, `HumaDeaz…`, `Huma9X…`, `7MXf…`, `HRsH…`. `HRsH…`'s counterparties are Binance, Bybit and Bitget deposits. Arkham shows transfer rows as HOLD, not HUMA | Ask Huma who received the 671.5M and the 17 Apr exchange deposits | Free |
| 2 | **Who owns `3xfvk…`, and is the investor lock enforced anywhere?** | Ask Huma whether the 471.5M is an investor's custody wallet and whether investor tokens will move to a vesting contract before 26 Nov | Free |
| 3 | **Watch the 26 Nov 2026 unlock** | Watch `DZaR8…`, `3xfvk…` and the Magna team accounts for transfers to exchange wallets (Binance 2/3, Bithumb, Bitget, OKX, Bybit) from 26 Nov | Free (Solscan) |
| 4 | **What the launch exchange sends were for** (≈ 354M to Binance, 85M to OKX, 15M to Bybit) | Match them to Binance HODLer / exchange campaign announcements | Free |
| 5 | **Is `HumaDeaz…` the airdrop distributor?** | Compare its outflows with airdrop-season claim data | Free |
| 6 | **Who holds the Squads and BSC Safe keys?** | Ask Huma to publish its signer sets (Squads 3-of-4 / 4-of-5; BSC Safe 2-of-2) | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
