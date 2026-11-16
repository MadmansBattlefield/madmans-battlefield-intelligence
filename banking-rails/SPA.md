---
ticker: SPA
name: Sperax
chain: arbitrum (main) · ethereum · bsc
contract: "0x5575552988a3a80504bbaeb1311674fcfd40ad4b (Arbitrum)"
overall_score: 2.2
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 4
  insider_holdings: 2
  selling_behavior: 0
  tokenomics_supply: 3
  liquidity_market: 2
  product_development: 4
  adoption_customers: 2
  security_audits: 4
  regulatory: 4
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "USDs rebase bug exploited 3–4 Feb 2023 (~$309K sold); funds returned (Sperax report)"
  mint_path_live: "Arbitrum SPA is a bridged token minted by the gateway on deposits; 5B max; not tested for an owner mint this pass [Unverified]"
  team_wallet_to_exchange_during_pump: "YES: team Safe 0xe10b… (3-of-5; its funder and co-signer 0xc6e0 is speraxfoundation.eth per Arkham) sent 30M SPA to a Coinbase deposit, 10M to a Gate deposit and 10M to a KuCoin deposit (Arkham) on 2 May 2023, a +51.4% 5-day pump day; also the treasury relay 0x9597 sent 9M to the same KuCoin deposit on the 26 Aug 2026 pump day (+11.2%)"
  team_held_share: "four team-signer Safes hold 1.647B SPA (≈33% of total supply)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "A fee share reaches holders, but only about $3.7k a year; Revenue stays 1."
pump_day_price_source: "Gate SPA_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions: []
price_usd: 0.00196042
price_source: "CoinGecko, 16 Nov 2026 ~5:08 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SPA · Overall grade **2.2 / 10 · ❌ FAIL**

**Summary:** Sperax is the governance token of a small Arbitrum DeFi suite: the USDs stablecoin, Demeter and Sperax Farms. It is down **65% in a year** to a **$3.75M market cap**, with **$107K of daily volume**. DefiLlama counts **$12,044 in fees over 12 months**, and only **$3,731** of that reached holders. USDs has **$0.51M locked**. Four Gnosis Safes run by overlapping team signers hold **1.647B SPA (≈33% of supply)**. One of them paid **50M SPA into Coinbase, Gate and KuCoin deposit addresses on a +51% pump day** in May 2023, and the treasury's relay wallet kept feeding MEXC and KuCoin deposits in 2026, including on the 26 Aug 2026 pump day. Arkham confirms the Safes' funder is **speraxfoundation.eth**. Both the Revenue and Selling gates fail.

**🚨 Top warning:** team Safe [`0xe10b…7fc9`](https://arbiscan.io/address/0xe10b88d70b01b956782dc98d7d4f3a931ff59fc7) (3-of-5; signer `0xc6e0…8265`, which Arkham labels **Sperax: speraxfoundation.eth** [Arkham](https://intel.arkm.com/explorer/address/0xc6e00e0e3544c93460cdfb53e85c4528ef348265), signs all four team Safes and funded three of them) sent a single [multisend on 2 May 2023](https://arbiscan.io/tx/0x15c6168eb5f7ea992a24dfde2dd993485d10800e383911e92e3d1625fea250f2): **30M SPA to Coinbase deposit [`0xd7f7…01d9`](https://arbiscan.io/address/0xd7f721a2bfdc29d38400f2fda17e721670b901d9)** ([Arkham: Coinbase Deposit](https://intel.arkm.com/explorer/address/0xd7f721a2bfdc29d38400f2fda17e721670b901d9)), **10M to Gate deposit [`0x2b00…1fb1`](https://arbiscan.io/address/0x2b00867967680b57508a7429f7683ece690e1fb1)** and **10M to [`0xc40e…1ca1f`](https://arbiscan.io/address/0xc40ebbffc42c6c84c82b8c50a350269df212ca1f)**, which Arkham labels a **KuCoin Deposit** ([Arkham](https://intel.arkm.com/explorer/address/0xc40ebbffc42c6c84c82b8c50a350269df212ca1f)). The Coinbase lot [was swept to Coinbase `0xe68e…f2b9` 8 minutes later](https://arbiscan.io/tx/0x27369cb5a0dc51c2157a6f910837da269680073e71e0cb4ddbe918406bd268e1), and the Gate lot [went to "Gate: Wallet" the next day](https://arbiscan.io/tx/0x4dd5b99b2385d63ed5e0b241eb417217e15ec5175c3e29d25258e9ef922bdfde). That day SPA closed at **$0.013359 on Gate, +51.4% over 5 days**. The 50M was worth ≈ **$668K**, and no disclosure was found. More recently the treasury's relay [`0x9597…`](https://arbiscan.io/address/0x9597daa6d22143c59c1818ee08df9d255a9bc9a0) sent [9M SPA to the same KuCoin deposit on 26 Aug 2026](https://arbiscan.io/tx/0x6728bdc5e70e83e4f33e160bb9c9dc4b4f448077c4dbf0c093e3a36284257c07), a +11.2% pump day. All links are in the 🔗 Evidence trail.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 4/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

> **Arkham pass, 16 Nov 2026:** no score change. The big holder `0x5c2f…` (398.9M SPA) is attributed by Arkham to **Coinbase** and was funded only by Coinbase Hot Wallet `0xE68`; this report never counted it as a team or insider wallet (team holdings are the four Safes only), so nothing had to be corrected. Arkham **strengthens** the existing fails: the Safes' funder `0xc6e0…` is **speraxfoundation.eth**, the third 10M of the 2 May 2023 pump-day multisend went to a **KuCoin deposit**, and the treasury relay sent SPA to MEXC and KuCoin deposits in Jul–Aug 2026, one lot on a pump day.

---

# 🪪 SPA · Sperax · 2.2 / 10 · ❌ FAIL

> **One line:** A $3.75M token with about $12K a year in fees, a third of its supply in team Safes run by speraxfoundation.eth, and a team Safe that paid 50M SPA into Coinbase, Gate and KuCoin deposits on a +51% pump day.

| 📊 Market (CoinGecko, 16 Nov 2026 ~5:08 AM MST) | 🔗 On-chain (Arbitrum, 16 Nov 2026) |
|---|---|
| **Price** $0.00196042 | **Token** [`0x5575…ad4b`](https://arbiscan.io/token/0x5575552988a3a80504bbaeb1311674fcfd40ad4b) · Arbitrum supply 4,040,204,577 |
| **7d / 30d / 1y** 🔴 −11.0% / −27.6% / −65.1% | **Team-signer Safes** 1,647M SPA across 4 Safes (all 3-of-5) |
| **Market cap** $3.75M · **FDV** $9.71M | **Largest Safe** [`0xba6c…0c9d`](https://arbiscan.io/address/0xba6ca0b9e7333f5e667816b85704c024ab250c9d) 1,100M |
| **24h volume** $107K | **Exchange-held** Coinbase-labelled wallets (Nansen) ≈1.04B across five top holders; plus `0x5c2f…` 398.9M (Arkham: Coinbase [Arkham](https://intel.arkm.com/explorer/address/0x5c2f85b7c224cb7ca8fab5b739a5d9134b5f9d56)) and Revolut cold wallet `0x15da…` [Arkham](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) |
| **Circulating** 1.913B · total 4.955B · max 5B | **USDs TVL** $0.51M (DefiLlama) |
| **ATH** $0.2395 (23 Mar 2022) · now −99.2% | **Pump days** 36 of the last 365 |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Fees, 30d / 12 months / all time | $1,337 / **$12,044** / $21,326 | [Tier A] [DefiLlama fees API](https://api.llama.fi/summary/fees/sperax?dataType=dailyFees) |
| Holders revenue, 12 months | **$3,731** | [Tier A] DefiLlama `dailyHoldersRevenue` |
| TVL (USDs / Demeter V2 / Demeter) | $510,680 / $27,080 / $7,865 | [Tier A] DefiLlama protocols |

**What it means:** About $3.7K a year reaches holders of a $3.75M token. That is **1**, which **trips the Revenue gate**.

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** A fee share reaches holders, but only about $3.7k a year; Revenue stays 1.

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Sperax Labs builds the products. Treasury and ecosystem SPA sits in **four Gnosis Safes, each 3-of-5**. Signers `0xc6e0…8265`, `0x5468…9a83`, `0x0a8d…e88a`, `0xdca6…26c3`, `0xd902…1ef3`, `0xc856…f1d0`, `0xb35b…0a4d`, `0xe66a…b47e` and `0x4f7c…49f1` overlap across them (`getOwners()` / `getThreshold()` read 16 Nov 2026) [Tier A].
- `0xc6e0…8265` funded three of the four Safes (1,250M + 517M + 391M) and signs all four [Tier A]. Arkham labels it **Sperax: speraxfoundation.eth** ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account), [Arkham](https://intel.arkm.com/explorer/address/0xc6e00e0e3544c93460cdfb53e85c4528ef348265)), so the Safes are the Sperax foundation's.
- Named signers, legal entity and audited accounts: **not found** this pass.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Wallet (Arbitrum) | SPA | Signers / funder | Source |
|---|---:|---|---|
| [`0xba6c…0c9d`](https://arbiscan.io/address/0xba6ca0b9e7333f5e667816b85704c024ab250c9d) | 1,100,000,000 | 3-of-5 · funded 1,250M by `0xc6e0…` | [Tier A] |
| [`0x3702…bd0e`](https://arbiscan.io/address/0x3702e3e2db2b5d037c1dbb23ab7a51d0cc90bd0e) | 418,400,000 | 3-of-5 · funded 517M by `0xc6e0…` | [Tier A] |
| [`0xe10b…7fc9`](https://arbiscan.io/address/0xe10b88d70b01b956782dc98d7d4f3a931ff59fc7) | 82,200,000 | 3-of-5 · funded 391M by `0xc6e0…` | [Tier A] |
| [`0xaf64…f17e`](https://arbiscan.io/address/0xaf64e027d42bac1c14277fd295de9ae318eef17e) | 46,200,000 | 3-of-5 | [Tier A] |
| **Total** | **1,646,800,000** | ≈ **33.2%** of 4.955B total · **86%** of CoinGecko circulating | |

**What it means:** A third of all SPA, close to the whole circulating float, sits with one signer group (the speraxfoundation.eth group), with no published schedule found. That is **2**.

*Not counted as team:* `0x5c2f…` (398.9M) is attributed to **Coinbase** by Arkham, funded only by Coinbase Hot Wallet `0xE68` [Arkham](https://intel.arkm.com/explorer/address/0x5c2f85b7c224cb7ca8fab5b739a5d9134b5f9d56), and `0x15da…` is a **Revolut cold wallet** [Arkham](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7) ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account)). Both are exchange custody.

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

**A. Team Safe → exchange deposits on a pump day (2 May 2023)**

| Day (UTC) | Route | SPA | Gate close / 5-day | Pump? |
|---|---|---:|---:|---|
| 2 May 2023 18:41 | `0xe10b…` → Coinbase deposit + Gate deposit, test ([tx](https://arbiscan.io/tx/0x6b4723255c007d1f1168d6c38e65d03f2c2bf06e24e0bd2f2be3f896be73a4ab)) | 0.0001 each | $0.013359 / **+51.4%** | **Yes** |
| 2 May 2023 19:13 | `0xe10b…` multisend ([tx](https://arbiscan.io/tx/0x15c6168eb5f7ea992a24dfde2dd993485d10800e383911e92e3d1625fea250f2)): 30M → Coinbase deposit `0xd7f7…`, 10M → Gate deposit `0x2b00…`, 10M → **KuCoin deposit** `0xc40e…` ([Arkham](https://intel.arkm.com/explorer/address/0xc40ebbffc42c6c84c82b8c50a350269df212ca1f)) | 50,000,000 | same | **Yes** |
| 2 May 2023 19:22 | `0xd7f7…` → Coinbase `0xe68e…` ([sweep](https://arbiscan.io/tx/0x27369cb5a0dc51c2157a6f910837da269680073e71e0cb4ddbe918406bd268e1)) | 29,999,900 | | |
| 3 May 2023 | `0x2b00…` → "Gate: Wallet" `0x0d07…` ([sweep](https://arbiscan.io/tx/0x4dd5b99b2385d63ed5e0b241eb417217e15ec5175c3e29d25258e9ef922bdfde)) | 10,000,000 | | |
| 8 May 2024 | `0xe10b…` → Coinbase deposit `0xd7f7…` ([tx](https://arbiscan.io/tx/0x91fb6fd5d9586d334bbe3d60f1e3ec0e802ee14c4d345885aa38d632a34b5b0d)) → **Coinbase: Hot Wallet** `0x3dd1…` ([tx](https://arbiscan.io/tx/0xb7011a0e381d1be64acf9a6e97f77f95091ca2c39a7aa2cc55cf0c76679308d2); [Arkham](https://intel.arkm.com/explorer/address/0x3dd1d15b3c78d6acfd75a254e857cbe5b9ff0af2)) | 20,000,000 | $0.013349 / −4.3% | No |

- **Why these are exchange deposits:** Nansen tags `0xd7f7…`, `0xe68e…`, `0x2b00…` and `0x0d07…` as Coinbase / Gate (`0x0d07…` is "Gate: Wallet"). Arkham independently labels `0xd7f7…` **Coinbase Deposit** [Arkham](https://intel.arkm.com/explorer/address/0xd7f721a2bfdc29d38400f2fda17e721670b901d9), `0xc40e…` **KuCoin Deposit** [Arkham](https://intel.arkm.com/explorer/address/0xc40ebbffc42c6c84c82b8c50a350269df212ca1f), and `0x3dd1…` / `0x05e3…` **Coinbase: Hot Wallet** [0x3dd1](https://intel.arkm.com/explorer/address/0x3dd1d15b3c78d6acfd75a254e857cbe5b9ff0af2) · [0x05e3](https://intel.arkm.com/explorer/address/0x05e3a758fdd29d28435019ac453297ea37b61b62) ([Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account)), so the Coinbase label now has two Tier B sources. Both deposits are plain EOAs that forward each lot onward within minutes to hours. `0xd7f7…` also receives withdrawals from KuCoin's and Gate's hot wallets, which is consistent with one trading account [Tier A pattern + Tier B Nansen].
- Closes come from Gate SPA_USDT daily candles (CoinGecko free history covers only 365 days).

**B. Treasury Safe → relay → Gate (30 Oct 2026, not a pump day)**

- The 1.1B Safe `0xba6c…` sent [50M on 12 Feb 2026](https://arbiscan.io/tx/0xed041a844fb188fdced6c2a16ee337c62eaba210a952661b5133241037bcceda) and [100M on 12 Aug 2026](https://arbiscan.io/tx/0x458a59d119be3fb9c548abb8b68bd384b9eac0a3d66169043390d30c33306aaa) to EOA [`0x9597…c9a0`](https://arbiscan.io/address/0x9597daa6d22143c59c1818ee08df9d255a9bc9a0).
- That EOA pays monthly 1.4–2.5M lots to `0x3693…` and `0x391d…` (payroll-like). On 30 Oct 2026 it sent [30M to Gate deposit `0x2b00…`](https://arbiscan.io/tx/0x47298598a0ce3565fbdc6d2fe0a95b6452348aa2ac46ffd2480c8dbbe9871585), [swept to Gate: Wallet an hour later](https://arbiscan.io/tx/0xb9058ff2ff7150046df07db7825fd3bcbd76d757e2e665d1371a8f4db989f094). That is ≈ $74K at the CoinGecko close ($0.002464), and the price fell.

**C. Treasury relay → MEXC and KuCoin deposits (Jul–Aug 2026; Arkham labels)**

| Day (UTC) | Route | SPA | 5-day change (CoinGecko) | Pump? |
|---|---|---:|---:|---|
| 25 and 27 Jul 2026 | `0x9597…` → **MEXC Deposit** [`0x4636…`](https://arbiscan.io/address/0x46364d608274625f09c5b4643761d742e45f5212) ([Arkham](https://intel.arkm.com/explorer/address/0x46364d608274625f09c5b4643761d742e45f5212)) ([7.049M](https://arbiscan.io/tx/0x3ee3befee941bb4495ef528ce467a46fb1c95a3f62f09877860c54e2d2a652b7) · [7.0M](https://arbiscan.io/tx/0x19c4a0c00e7edb770ceca56e504eed50f7530cb24970bc3643030a4e3594806b)) | 14,049,000 | +1.7% / −1.9% | No |
| 30 Jul 2026 | `0x9597…` → KuCoin deposit `0xc40e…` ([tx](https://arbiscan.io/tx/0xa2b0562cde2bd35b89a5f3f7a6507a383afa62b611378cb3af624fc39ff0ce38)) | 4,999,000 | −12.3% | No |
| 11–14 Aug 2026 | `0x9597…` → [`0x4ed8…`](https://arbiscan.io/address/0x4ed88efc52c79e48dcb248d99d7b36439dcf69d1) 22.8M ([10M lot](https://arbiscan.io/tx/0x30f621f1e1425a4469c44bd5531700c37cb364fb10f137b3bf4eb449e1271e00)), which paid ~3,000 small transfers and ≈ 10.0M to four **MEXC deposits** ([Arkham](https://intel.arkm.com/explorer/address/0x4ed88efc52c79e48dcb248d99d7b36439dcf69d1)) | ≈ 10,000,000 to MEXC | +2.2% to +4.8% | No |
| **26 Aug 2026** | `0x9597…` → KuCoin deposit `0xc40e…` ([tx](https://arbiscan.io/tx/0x6728bdc5e70e83e4f33e160bb9c9dc4b4f448077c4dbf0c093e3a36284257c07)) | **9,000,000** | **+11.2%** | **Yes** |

- Payroll-like receivers: [`0x391d…`](https://arbiscan.io/address/0x391d5eca7264515f8efffb82245c9a6a1e7de6ad) swaps SPA through 0x's ArbitrumSettler and sends the USDC to a **Gate deposit** [Arkham](https://intel.arkm.com/explorer/address/0x391d5eca7264515f8efffb82245c9a6a1e7de6ad); [`0x3693…`](https://arbiscan.io/address/0x36930f85ae314995315ddd99ee10fa2775029555) forwarded 7.5M onward to unlabelled `0x3469…` [Arkham](https://intel.arkm.com/explorer/address/0x36930f85ae314995315ddd99ee10fa2775029555). `0x9597…` itself is unlabelled on Arkham [Arkham](https://intel.arkm.com/explorer/address/0x9597daa6d22143c59c1818ee08df9d255a9bc9a0).
- Values are small (9M ≈ $20K), but the route is treasury → relay → exchange deposit, undisclosed.

**What it means:** A team-signer Safe put 50M SPA into three exchanges on a day the price was up 51% in five days, with no disclosure found. This year the treasury relay kept feeding Gate, MEXC and KuCoin deposits, once on a pump day. That **fails Selling at 2** (unchanged after Arkham; the new evidence strengthens it) and **trips the gate**.

- **Disclosure quality (16 Nov 2026 rules): silence.** No disclosure was found. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. Pump days from Gate SPA_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (30 of 360 days); the body's earlier count used CoinGecko daily closes.

- **One-hop amendment (16 Nov 2026):** Still a **proven sale** under the amended rule. (c) holds: no published reason covers the team-signer Safe's exchange deposits, and its payroll-like receivers sell through a DEX (0x Settler). Silence stands, so the penalty above is unchanged.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 5B max, 4.955B total, **1.913B circulating** (CoinGecko). About 3B is outside circulation, mostly in the team Safes and the veSPA/xSPA contracts (`0x2e20…` 241M, `0x0966…` 54.6M) [Tier A balances].
- No public unlock schedule for the Safe balances was found. Arbitrum SPA is minted by the bridge gateway on deposits (e.g. 167M minted to `0xaf64…`). An owner mint path was not tested [Unverified].

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- **$107K** in 24h volume on a $3.75M market cap. The token is −99.2% from ATH and −65.1% over a year, with 36 pump days in the last 365 [Tier A CoinGecko].

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- USDs (an auto-yield stablecoin), Demeter / Sperax Farms (liquidity farms) and veSPA / xSPA are live on Arbitrum. Repo activity was not measured this pass.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- **USDs TVL $0.51M**, Demeter V2 $27K (DefiLlama). Usage is tiny.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- ⚠️ **3–4 Feb 2023 USDs exploit:** a rebase-accounting bug let an attacker inflate a balance to 9.79B USDs and sell ~$309K before the pause. The funds were returned [Tier A [Sperax report](https://medium.com/sperax/usds-feb-3-exploit-report-from-engineering-team-9f0fd3cef00c)]. CertiK notes USDs was outside its audit scope [Tier B].
- ✅ Treasury funds sit in 3-of-5 Safes.

## ⚖️ Regulatory · 4/10 · ❌ FAIL

- No licence or MiCA white paper found for SPA or USDs this pass. Not proven.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| Monthly | Treasury relay `0x9597…` payouts (≈4M a month observed) |
| Ad hoc | Possible further Safe → exchange moves (no schedule published) |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 USDs exploit Feb 2023 (~$309K, returned) |
| Live mint path | 🟡 Bridged L2 token; owner mint not tested |
| Team wallet → exchange during a pump | 🔴 **Yes:** 50M SPA to Coinbase, Gate and KuCoin deposits on 2 May 2023 (+51.4%); 9M from the treasury relay to KuCoin on 26 Aug 2026 (+11.2%). [multisend](https://arbiscan.io/tx/0x15c6168eb5f7ea992a24dfde2dd993485d10800e383911e92e3d1625fea250f2) · [Coinbase sweep](https://arbiscan.io/tx/0x27369cb5a0dc51c2157a6f910837da269680073e71e0cb4ddbe918406bd268e1) · [Gate sweep](https://arbiscan.io/tx/0x4dd5b99b2385d63ed5e0b241eb417217e15ec5175c3e29d25258e9ef922bdfde) |
| Team-held share | 🔴 1.647B (≈33% of supply) in team-signer Safes |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Team-signer Safe | Sperax team | Safe signers on-chain | high | yes (on-chain) | Selling: 50M SPA into three exchanges on a +51% day; treasury relay to Gate, MEXC and KuCoin once on a 2026 pump day |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API, Arbitrum (chain 42161): `tokentx` for the four Safes, `0xd7f7…`, `0x2b00…`, `0x9597…`; `getsourcecode`, `eth_getCode`, `tokensupply`; `eth_call` `getOwners()` / `getThreshold()`, 16 Nov 2026 MST
- [Tier A] DefiLlama fees / revenue / holders-revenue API and protocol TVL (Sperax USD, Demeter)
- [Tier A] CoinGecko `sperax` market data and 365-day closes; Gate SPA_USDT daily candles for 2023–2024
- [Tier A] [Sperax USDs exploit report](https://medium.com/sperax/usds-feb-3-exploit-report-from-engineering-team-9f0fd3cef00c) · [Tier B] [CertiK write-up](https://www.certik.com/blog/inflated-books-the-usd250k-attack-on-sperax-usd)
- [Tier B] Nansen `tgm/holders` (Arbitrum) and `profiler/address/labels`, read 16 Nov 2026 (MST): `0x20c6…`, `0x0515…`, `0xea4d…`, `0xe68e…`, `0x5300…`, `0xd7f7…` Coinbase; `0x2b00…`, `0x0d07…` Gate; `0x03e6…` KuCoin: Hot Wallet
- [Tier B] Arkham, read 16 Nov 2026 ~6:35–6:40 AM MST (signed-in account): **Sperax: speraxfoundation.eth** [0xc6e0…](https://intel.arkm.com/explorer/address/0xc6e00e0e3544c93460cdfb53e85c4528ef348265); Coinbase Deposit [0xd7f7…](https://intel.arkm.com/explorer/address/0xd7f721a2bfdc29d38400f2fda17e721670b901d9); KuCoin Deposit [0xc40e…](https://intel.arkm.com/explorer/address/0xc40ebbffc42c6c84c82b8c50a350269df212ca1f); MEXC Deposit [0x4636…](https://intel.arkm.com/explorer/address/0x46364d608274625f09c5b4643761d742e45f5212); Coinbase: Hot Wallet [0x3dd1…](https://intel.arkm.com/explorer/address/0x3dd1d15b3c78d6acfd75a254e857cbe5b9ff0af2) and [0x05e3…](https://intel.arkm.com/explorer/address/0x05e3a758fdd29d28435019ac453297ea37b61b62); Coinbase-attributed [0x5c2f…](https://intel.arkm.com/explorer/address/0x5c2f85b7c224cb7ca8fab5b739a5d9134b5f9d56); Revolut: Cold Wallet [0x15da…](https://intel.arkm.com/explorer/address/0x15da7556d5ed888306839bed06f868aeaedcb0d7); no label on [0x9597…](https://intel.arkm.com/explorer/address/0x9597daa6d22143c59c1818ee08df9d255a9bc9a0), [0x3693…](https://intel.arkm.com/explorer/address/0x36930f85ae314995315ddd99ee10fa2775029555), [0x391d…](https://intel.arkm.com/explorer/address/0x391d5eca7264515f8efffb82245c9a6a1e7de6ad), [0x4ed8…](https://intel.arkm.com/explorer/address/0x4ed88efc52c79e48dcb248d99d7b36439dcf69d1). Arkham's token filter is Enterprise-only, so counterparties come from the default first page.
- [Tier A] CoinGecko `sperax` 365-day closes for the 2026 pump test (26 Aug 2026 +11.2%)
- [Unverified] individual signer identities; owners of `0x9597…`, `0x3693…`, `0x391d…`, `0x4ed8…`; whether the May 2023 deposits were for market making and disclosed

## 🔗 Evidence trail

*Every link below opens the primary record for the claim.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Four 3-of-5 Safes with overlapping signers hold 1.647B | [`0xba6c…`](https://arbiscan.io/address/0xba6ca0b9e7333f5e667816b85704c024ab250c9d) · [`0x3702…`](https://arbiscan.io/address/0x3702e3e2db2b5d037c1dbb23ab7a51d0cc90bd0e) · [`0xe10b…`](https://arbiscan.io/address/0xe10b88d70b01b956782dc98d7d4f3a931ff59fc7) · [`0xaf64…`](https://arbiscan.io/address/0xaf64e027d42bac1c14277fd295de9ae318eef17e) | A | 16 Nov 2026 |
| 50M to Coinbase / Gate / KuCoin deposits on a +51.4% day | [multisend](https://arbiscan.io/tx/0x15c6168eb5f7ea992a24dfde2dd993485d10800e383911e92e3d1625fea250f2) · [Coinbase sweep](https://arbiscan.io/tx/0x27369cb5a0dc51c2157a6f910837da269680073e71e0cb4ddbe918406bd268e1) · [Gate sweep](https://arbiscan.io/tx/0x4dd5b99b2385d63ed5e0b241eb417217e15ec5175c3e29d25258e9ef922bdfde) | A chain + B labels | 16 Nov 2026 |
| 20M to the same Coinbase deposit, 8 May 2024 | [tx](https://arbiscan.io/tx/0x91fb6fd5d9586d334bbe3d60f1e3ec0e802ee14c4d345885aa38d632a34b5b0d) · [onward](https://arbiscan.io/tx/0xb7011a0e381d1be64acf9a6e97f77f95091ca2c39a7aa2cc55cf0c76679308d2) | A + B | 16 Nov 2026 |
| Treasury → relay → Gate, 2026 | [50M](https://arbiscan.io/tx/0xed041a844fb188fdced6c2a16ee337c62eaba210a952661b5133241037bcceda) · [100M](https://arbiscan.io/tx/0x458a59d119be3fb9c548abb8b68bd384b9eac0a3d66169043390d30c33306aaa) · [30M to Gate](https://arbiscan.io/tx/0x47298598a0ce3565fbdc6d2fe0a95b6452348aa2ac46ffd2480c8dbbe9871585) · [sweep](https://arbiscan.io/tx/0xb9058ff2ff7150046df07db7825fd3bcbd76d757e2e665d1371a8f4db989f094) | A + B | 16 Nov 2026 |
| `0xc6e0…` (Safe funder and signer) is speraxfoundation.eth | [Arkham 0xc6e0…](https://intel.arkm.com/explorer/address/0xc6e00e0e3544c93460cdfb53e85c4528ef348265) | B | 16 Nov 2026 ~6:36 AM MST |
| `0xc40e…` is a KuCoin deposit; `0xd7f7…` a Coinbase deposit | [Arkham 0xc40e…](https://intel.arkm.com/explorer/address/0xc40ebbffc42c6c84c82b8c50a350269df212ca1f) · [Arkham 0xd7f7…](https://intel.arkm.com/explorer/address/0xd7f721a2bfdc29d38400f2fda17e721670b901d9) | B (+ Nansen for 0xd7f7) | 16 Nov 2026 ~6:36 AM MST |
| Treasury relay → MEXC / KuCoin deposits, Jul–Aug 2026; 9M on the 26 Aug pump day | [25 Jul](https://arbiscan.io/tx/0x3ee3befee941bb4495ef528ce467a46fb1c95a3f62f09877860c54e2d2a652b7) · [27 Jul](https://arbiscan.io/tx/0x19c4a0c00e7edb770ceca56e504eed50f7530cb24970bc3643030a4e3594806b) · [26 Aug](https://arbiscan.io/tx/0x6728bdc5e70e83e4f33e160bb9c9dc4b4f448077c4dbf0c093e3a36284257c07) · [Arkham 0x4636…](https://intel.arkm.com/explorer/address/0x46364d608274625f09c5b4643761d742e45f5212) | A chain + B label | 16 Nov 2026 |
| `0x5c2f…` (398.9M) is Coinbase-held, not team | [Arkham 0x5c2f…](https://intel.arkm.com/explorer/address/0x5c2f85b7c224cb7ca8fab5b739a5d9134b5f9d56) | B | 16 Nov 2026 ~6:38 AM MST |
| $12,044 fees in 12 months | [DefiLlama API](https://api.llama.fi/summary/fees/sperax?dataType=dailyFees) | A | 16 Nov 2026 |
| USDs exploit, Feb 2023 | [Sperax report](https://medium.com/sperax/usds-feb-3-exploit-report-from-engineering-team-9f0fd3cef00c) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | ~~Arkham pass on 12 wallets~~ **Done 16 Nov 2026** (the maintainer's `arkham/spa_addresses.csv` list): `0xc6e0…` = speraxfoundation.eth; Coinbase / KuCoin / MEXC deposits and Coinbase hot wallets confirmed; `0x5c2f…` Coinbase, `0x15da…` Revolut. Still unnamed: relay `0x9597…` and its receivers | Re-check with Arkham Enterprise's token filter for full SPA history | Arkham Enterprise |
| 2 | **Was the 2 May 2023 deposit disclosed?** | Search Sperax posts and governance forum for May 2023 (market-maker or listing notices); ask the team | Free |
| 3 | **Safe balance schedule** | Ask Sperax for the unlock plan for the 1.647B in Safes; read any SPA tokenomics page | Free |
| 4 | **Ethereum and BSC legs** | Run the same Safe → exchange test on the Ethereum token `0xb4a3…9008` and BSC `0x1a9f…79b1` | Free (Etherscan) |
| 5 | **Owner mint on Arbitrum SPA** | Read the verified source of `0x5575…ad4b` for `mint` / gateway-only modifiers | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
