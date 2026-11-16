---
ticker: QUAI
name: Quai Network
chain: quai
contract: "native coin (no contract)"
overall_score: 4.9
overall_verdict: FAIL
section_scores:
  revenue: 5
  foundation_team: 6
  insider_holdings: 6
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 2
  product_development: 6
  adoption_customers: 4
  security_audits: 5
  regulatory: 5
  catalysts: 6
gates_failed: []
red_lines:
  hack_exploit: none found
  mint_path_live: "ongoing PoW mining emissions (no hard cap), partly offset by SOAP buy-and-burn"
  team_wallet_to_exchange_during_pump: "not proven: genesis-funded wallets and the SOAP burn wallet sent QUAI to an unlabelled high-volume wallet (0x004b…1Db93), including on 16 Jul, 9 Sep and 23 Sep 2026 pump days; whose wallet it is is unknown"
  future_unlocks_cut: "yes, Singularity fork removed 1.667B future genesis unlocks; Polaris (early Nov 2026) forgoes 236.5M more founder unlocks"
price_usd: 0.00632515
price_source: "CoinGecko, 16 Nov 2026 5:55 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### QUAI · Overall grade **4.9 / 10 · ❌ FAIL**

**Summary:** Quai is a proof-of-work Layer 1 with a buy-and-burn program called SOAP: merge-mining rewards from other chains are used to buy QUAI on the market and burn it. **246.6M QUAI** (≈ 21% of circulating supply) now sits in the burn address. The team also cut future genesis unlocks twice (Singularity −1.67B, Polaris −236.5M), which is unusually holder-friendly. But burn revenue is shrinking fast ($1.25M in Jan 2026 → $178K in Oct 2026 per DefiLlama). Trading is about $70K a day, mostly on MEXC. The price is −98% from its ATH. Large genesis wallets are unlabelled, and exchange wallets on Quai have no public labels, so insider selling **could not be proven either way**.

**🚨 Top warning (yellow, unproven):** large wallets that received genesis unlocks without any visible funding transfer ([`0x0051…f1253`](https://quaiscan.io/address/0x0051E12355307e2dcCb2acab181B02d4719f1253), 99.0M QUAI, and [`0x0050…7e89`](https://quaiscan.io/address/0x00504f34C168CC70eE614eD5E5BE4f69234d7e89)) send QUAI in 0.5–2.5M lots to one unlabelled wallet, [`0x004b…1Db93`](https://quaiscan.io/address/0x004b00d6339F5aae012145356c8D5C71AFa1Db93). That wallet has 306,811 transactions and keeps almost no balance, which looks like an exchange or service hot wallet. One lot, [1.0M QUAI](https://quaiscan.io/tx/0x002e0078399569337dcfc505907617c1b3750ab0173f7d245c70432b231c5e21), went on the **16 Jul 2026 pump day (+32.3%)**. The wallet that feeds the SOAP burn address also sent [4M on the 9 Sep pump day (+33.4%)](https://quaiscan.io/tx/0x0044001e21806e9b9be950fdb9b467193ca0e794c054359971403ee32321b715) and [3M on 23 Sep (+17.0%)](https://quaiscan.io/tx/0x0079000626fadd1eeb7b5081a06abe2ad7fdabd765529d863a608fcca29ebffe) to the same wallet. Whose wallet `0x004b…` is, and who owns the genesis wallets, is **not public** [Unverified].

**Sections passed: 5 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 5/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 2/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 QUAI · Quai Network · 4.9 / 10 · ❌ FAIL

> **One line:** Quai is a proof-of-work Layer 1 with a buy-and-burn program called SOAP: merge-mining rewards from other chains are used to buy QUAI on the market and burn it. **246.6M QUAI** (≈ 21% of circulating supply) now sits in the burn address. The team also cut future genesis unlocks twice (Singularity −1.67B, Polaris −236.5M), which is unusually holder-friendly. But burn revenue is shrinking fast ($1.25M in Jan 2026 → $178K in Oct 2026 per DefiLlama). Trading is about $70K a day, mostly on MEXC. The price is −98% from its ATH. Large genesis wallets are unlabelled, and exchange wallets on Quai have no public labels, so insider selling **could not be proven either way**.

| 📊 Market (CoinGecko, 16 Nov 2026 5:55 AM MST) | 🔗 On-chain (Quaiscan, 16 Nov 2026) |
|---|---|
| **Price** $0.006325 | **Native coin** of Quai Network (cyprus1 zone explorer: [quaiscan.io](https://quaiscan.io)) |
| **24h / 7d / 30d** 🔴 −3.2% / −13.2% / −31.0% · 1y −73.1% | **Burn address** [`0x0050AF00…0000`](https://quaiscan.io/address/0x0050AF0000000000000000000000000000000000): 246.6M QUAI, only inflows |
| **Market cap** $7.37M (circulating 1.165B) | **Wrapped QUAI** contract holds 18.0M |
| **24h volume** $70.1K (MEXC $54.8K, Gate $6.3K, XT $6.0K, Kraken $2.2K) | **Addresses** 106,906 · **transactions today** 143,280 ([stats API](https://quaiscan.io/api/v2/stats)) |
| **ATH** $0.3634 (23 Feb 2025) · now −98.3% | **Genesis baseline after forks** 1,096,383,477 QUAI ([supply.qu.ai](https://supply.qu.ai/dashboard/faq)) |

---

## 💰 Revenue — Does it make money? · 5/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| DefiLlama fees / revenue / holders revenue, last 365 days | **$6.88M / $6.02M / $6.02M** | [Tier A] [DefiLlama Quai](https://defillama.com/protocol/quai), API read 16 Nov 2026 |
| Holders revenue by month (SOAP buy-and-burn) | Jan 2026 $1.25M → Apr $681K → Jul $589K → **Oct $178K** | same |
| QUAI in the burn address | **246.6M** (≈ 21% of circulating) | [Tier A] [Quaiscan](https://quaiscan.io/address/0x0050AF0000000000000000000000000000000000) |
| Source of burn funds | Merge-mining rewards from BCH, LTC, DOGE and RVN, swapped into QUAI | [Tier A] [Quai docs: emissions and SOAP](https://docs.qu.ai/learn/tokenomics/quai-emissions) |

**What it means:** Holders do get value: 100% of SOAP flow buys and burns QUAI, and on-chain burns match. But the money is a subsidy from other chains' miners, not user fees, and it fell about 86% from January to October. Score **5**.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Core developer | Dominant Strategies (GitHub org [`dominant-strategies`](https://github.com/dominant-strategies): 59 repos, 9 pushed in the last 90 days) | [Tier A] GitHub API |
| Governance of supply | Supply changes are made by hard forks (Singularity, Polaris) that the team proposes and node operators adopt | [Tier A] [supply.qu.ai FAQ](https://supply.qu.ai/dashboard/faq) |
| Foundation | Genesis plan gives a Foundation ~33% of the original 3B; wallet addresses are not published | [Tier B] [DefiLlama unlocks](https://defillama.com/unlocks/quai-network) · [Tokenomics.com](https://app.tokenomics.com/tokenomics/quai-network) |

**What it means:** Public, active developer company, and supply changes are announced in advance. The weakness is that genesis wallets are not disclosed.

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

- **Future unlocks were cut twice:** Singularity removed **1,667,159,984 QUAI** of future genesis unlocks (3B → 1.333B baseline). Polaris (early Nov 2026, around Prime block 2,425,000) forgoes **236,456,538 QUAI** more of founder unlocks, so the final genesis total is **1,096,383,477**. About 90M QUAI is left to unlock, at ≈ 3.7M a month into early 2029 ([Tier A] [supply.qu.ai](https://supply.qu.ai/dashboard/faq); [docs](https://docs.qu.ai/learn/tokenomics/quai-emissions)).
- **Largest unlabelled holders** (Quaiscan top list): [`0x0051…f1253`](https://quaiscan.io/address/0x0051E12355307e2dcCb2acab181B02d4719f1253) 99.0M (8.5% of circulating; balance appeared without a funding transfer, i.e. a genesis unlock), [`0x0062…Ddb4a`](https://quaiscan.io/address/0x006243e4eE6C2CF6F993036f27f0A88f265Ddb4a) 43.1M (472K txs), [`0x007e…8987`](https://quaiscan.io/address/0x007e2F1a4709B812F339f22E18032118FBcc8987) 41.8M (69K txs), [`0x004c…23c3`](https://quaiscan.io/address/0x004cd3a9997a5170A9234CEddD1ec5DCE7Db23c3) 34.0M, [`0x0050…7e89`](https://quaiscan.io/address/0x00504f34C168CC70eE614eD5E5BE4f69234d7e89) 21.3M. Owners [Unverified].

**What it means:** Insiders gave up most of their future tokens, which is rare. Score **6**, held back because no one can tell which wallets are team, Foundation or investors.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**Method:** Quaiscan (Blockscout) v2 API: top-50 holders, the burn address's inflows, and all outflows of the large genesis-unlock wallets. Quaiscan has **no exchange labels**, so exchange deposits cannot be proven. Pump days use CoinGecko daily closes (67 in the last 365).

| Date (UTC) | From | To `0x004b…1Db93` (unlabelled, 306,811 txs) | QUAI | Pump day? |
|---|---|---|---:|---|
| 14–17 Jul 2026 | genesis wallet `0x0050…7e89` | [0.75M](https://quaiscan.io/tx/0x0054002541c14c7b860b96fd31c163fae15b672e09ce740aeb1d4b9a9b51b289) · [**1.0M**](https://quaiscan.io/tx/0x002e0078399569337dcfc505907617c1b3750ab0173f7d245c70432b231c5e21) · [0.5M](https://quaiscan.io/tx/0x00410027d7643f14a75220317c63dd1d9b8b5960f138e2be6ff20831251c8f15) | 2.25M | **16 Jul: yes, +32.3%** |
| 20–24 Jul 2026 | genesis-unlock wallet [`0x007E…8dA4`](https://quaiscan.io/address/0x007ED4bf47d368DDF884CcE1F395682B68278dA4) | [0.5M](https://quaiscan.io/tx/0x0043006ecd30fe43d8f649c0181c59532b8134ca0dfa8238f6e3e7e0f6d43e92) · [0.5M](https://quaiscan.io/tx/0x004b001f453dc5b7e04ca49f4089ed4b22b9e9725d2ba8365382b180048fb6bb) · [2.54M](https://quaiscan.io/tx/0x001700042773e12514f222347277290d4b7cb54cf9d5c1873cd97797bec20b39) | 3.54M | No (−11% to −13%) |
| 7 Aug – 30 Sep 2026 | SOAP burn feeder [`0x0053…8D06`](https://quaiscan.io/address/0x0053bcdc4F5Af4B35079d4D091fCD1D86A958D06) | [4M, 9 Sep](https://quaiscan.io/tx/0x0044001e21806e9b9be950fdb9b467193ca0e794c054359971403ee32321b715) · [3M, 23 Sep](https://quaiscan.io/tx/0x0079000626fadd1eeb7b5081a06abe2ad7fdabd765529d863a608fcca29ebffe) · others | 17M | **9 Sep +33.4%, 23 Sep +17.0%** |
| 8–16 Oct 2026 | genesis wallet `0x0051…f1253` | [2M](https://quaiscan.io/tx/0x0079007fea95bdddace6523ebcecca1b8d1c1611488721f015a2af8322611f02) · [2M](https://quaiscan.io/tx/0x001a000d76177bb317bf064b92f6dc025d5b3e24a26693c40c4530d2e63f40d1) · [2M](https://quaiscan.io/tx/0x004e00380396e7683985d742bc379b71317c9bcd7926c74923d75a9c251cea1a) | 6M | No |

- `0x004b…` keeps ≈ 0.06M QUAI and makes constant zero-value calls to contract [`0x0074…112e`](https://quaiscan.io/address/0x00740BF840B96dC685e76B0caA3E9e712604112e), so the QUAI may be leaving through Qi conversion or an exchange's internal flow. It could be an exchange, a bridge or a protocol service. **Not proven.**
- `0x0053…8D06` sent 229.0M QUAI to the burn address in 128 transfers, so it is the SOAP burn feeder. It is odd that it also sends QUAI to `0x004b…` [Unverified purpose].
- Pump-day amounts are small: ≈ 8M QUAI (≈ $90K at those days' prices).

**What it means:** No labelled team wallet was seen selling, and the team cut its own unlocks. But genesis wallets and the burn feeder route coins to an unlabelled hot-wallet-like address, sometimes on pump days, and nobody can check who it is. "Not proven" counts as a fail: **4**.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- No hard cap: mining emissions continue (QUAI rewards scale logarithmically with difficulty). Quai's own forecast assumes **~55M QUAI a year net of burns** ([supply.qu.ai](https://supply.qu.ai/dashboard/faq)), about 4.7% of circulating.
- SOAP burns offset some emissions; future genesis unlocks are now small (≈ 90M).
- Dual-token design: Qi (payments) can be converted to and from QUAI at the mining reward ratio.

## 💧 Liquidity & market · 2/10 · ❌ FAIL

- $70.1K a day: MEXC 78%, Gate 9%, XT 9%, Kraken 3% (CoinGecko tickers). Spreads 0.16–0.44%. One venue over 60%.
- 67 pump days in the last 365, with the price down 73% over the year.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Mainnet live since early 2025: PoEM consensus, sharded zones, merged mining with BCH/LTC/DOGE/RVN through AuxPoW, Qi privacy token ([docs](https://docs.qu.ai/learn/tokenomics/quai-emissions)).
- 9 of 59 `dominant-strategies` repos pushed in the last 90 days.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- 143,280 transactions on the day read; 106,906 addresses on cyprus1 ([Quaiscan stats](https://quaiscan.io/api/v2/stats)). Network utilisation 0.28%.
- Few apps: the top holders are the burn address, wrapped QUAI and mining/service wallets. Market cap is $7.4M.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- PoW chain with merge-mined hashrate from larger chains, which adds security. No exploit found.
- No independent audit of the node software was found in this pass [Unverified]. Supply rules have changed by fork twice in a year, which is a governance risk too.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- CoinGecko tags the project "Made in USA" [Tier B]. No enforcement action found. No exchange listing in the US besides Kraken.

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event |
|---|---|
| Early Nov 2026 | Polaris fork (≈ Prime block 2,425,000) ends 236.5M of founder unlocks |
| Monthly to early 2029 | ≈ 3.7M QUAI genesis unlocks |
| Ongoing | SOAP buy-and-burn; watch whether monthly burn keeps falling |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team / treasury wallet → exchange during a pump | 🟡 Not proven: genesis wallet → unlabelled hub [1.0M on 16 Jul 2026](https://quaiscan.io/tx/0x002e0078399569337dcfc505907617c1b3750ab0173f7d245c70432b231c5e21) (+32.3%) |
| Burn feeder → unlabelled hub on pump days | 🟡 [9 Sep](https://quaiscan.io/tx/0x0044001e21806e9b9be950fdb9b467193ca0e794c054359971403ee32321b715), [23 Sep 2026](https://quaiscan.io/tx/0x0079000626fadd1eeb7b5081a06abe2ad7fdabd765529d863a608fcca29ebffe) |
| Live mint path | 🟡 PoW emissions, no hard cap |
| Unlock cuts | 🟢 −1.67B (Singularity) and −236.5M (Polaris) |

## 📚 Sources

- [Tier A] Quaiscan (Blockscout) v2 API: `/stats`, `/addresses` top list, `/addresses/{a}/transactions` for the burn address, `0x0051…`, `0x0050…7e89`, `0x007E…`, `0x0053…`, `0x004b…`; read 16 Nov 2026 ~5:45–6:00 AM MST
- [Tier A] [supply.qu.ai FAQ](https://supply.qu.ai/dashboard/faq) and [Quai docs: emissions](https://docs.qu.ai/learn/tokenomics/quai-emissions) (issuer)
- [Tier A] DefiLlama fees API (`quai`), 16 Nov 2026
- [Tier A] CoinGecko `quai-network` price, tickers and 365-day closes
- [Tier A] GitHub API, `dominant-strategies` org
- [Tier B] [DefiLlama unlocks](https://defillama.com/unlocks/quai-network) · [Tokenomics.com](https://app.tokenomics.com/tokenomics/quai-network) for the original genesis split
- [Unverified] owners of the genesis wallets and of `0x004b…`; node audits

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 246.6M QUAI in the burn address, fed by `0x0053…` | [burn address](https://quaiscan.io/address/0x0050AF0000000000000000000000000000000000) · [feeder](https://quaiscan.io/address/0x0053bcdc4F5Af4B35079d4D091fCD1D86A958D06) | A | 16 Nov 2026 |
| Unlock cuts (Singularity, Polaris) | [supply.qu.ai](https://supply.qu.ai/dashboard/faq) · [docs](https://docs.qu.ai/learn/tokenomics/quai-emissions) | A (issuer) | 16 Nov 2026 |
| SOAP revenue falling | [DefiLlama Quai](https://defillama.com/protocol/quai) | A | 16 Nov 2026 |
| Genesis wallet → hub on the 16 Jul pump day | [tx](https://quaiscan.io/tx/0x002e0078399569337dcfc505907617c1b3750ab0173f7d245c70432b231c5e21) · [wallet](https://quaiscan.io/address/0x00504f34C168CC70eE614eD5E5BE4f69234d7e89) · [hub](https://quaiscan.io/address/0x004b00d6339F5aae012145356c8D5C71AFa1Db93) | A · owners [Unverified] | 16 Nov 2026 |
| Burn feeder → hub on pump days | [9 Sep](https://quaiscan.io/tx/0x0044001e21806e9b9be950fdb9b467193ca0e794c054359971403ee32321b715) · [23 Sep](https://quaiscan.io/tx/0x0079000626fadd1eeb7b5081a06abe2ad7fdabd765529d863a608fcca29ebffe) | A | 16 Nov 2026 |
| `0x0051…` (99M) moved 20.9M to `0x0050…7e89`, then 6M to the hub | [20.9M](https://quaiscan.io/tx/0x007f001749a5b08c56a1b9b1bd2ca910750f6cb2beb5e59097245142b2c54fdc) · [2M, 8 Oct](https://quaiscan.io/tx/0x0079007fea95bdddace6523ebcecca1b8d1c1611488721f015a2af8322611f02) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass on Quai wallets** (hub `0x004b…`, genesis wallets, burn feeder) | **Arkham does not support Quai** (checked 16 Nov 2026), so the maintainer's `arkham/quai_addresses.csv` list cannot be closed there. Ask MEXC/Gate or Dominant Strategies to identify the wallets, or wait for Quaiscan labels | Free |
| 2 | **Is `0x004b…` an exchange (MEXC?) deposit wallet?** | Ask MEXC/Gate support or Quai's team; or deposit a tiny amount to MEXC and see which hot wallet receives it | Free / tiny amount |
| 3 | **Which genesis bucket owns `0x0051…`, `0x0050…7e89`, `0x007E…`?** | Ask Dominant Strategies to publish genesis allocation addresses | Free |
| 4 | **Did Polaris activate on schedule?** | Check the current Prime block and supply.qu.ai genesis line | Free |
| 5 | **Node audits** | Search Quai docs/GitHub for third-party audit reports | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
