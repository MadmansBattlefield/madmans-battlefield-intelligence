---
ticker: API3
name: Api3
chain: ethereum
contract: "0x0b38210ea11411557c13457D4dA7dC6ea731B88a"
overall_score: 4.9
overall_verdict: FAIL
section_scores:
  revenue: 4
  foundation_team: 6
  insider_holdings: 6
  selling_behavior: 4
  tokenomics_supply: 7
  liquidity_market: 4
  product_development: 5
  adoption_customers: 4
  security_audits: 6
  regulatory: 5
  catalysts: 5
gates_failed: []
red_lines:
  hack_exploit: none found
  treasury_to_exchange_during_pump: "yes (Etherscan 'API3: Treasury' / Arkham 'API3: V1 Treasury' 0xe7aF… sent 250,000 API3 into a Binance deposit on the 28 Jan 2024 pump day (+28.8%) and 240,000 on 23 Apr 2024 (+11.1%); no matching proposal found)"
  treasury_funded_wallet_to_exchange_during_pump: "yes (DAO Vault multisig 0x8e03… sent 610,000 API3 to 0x9e65… on the 10 Feb 2026 pump day (+13.7%); 609,900 reached a Binance deposit within 71 minutes; 1.83M in total by May 2026; recipient unlabelled on Arkham too)"
  mint_path_live: "no (owner is 0x…dEaD, no minters; read 16 Nov 2026)"
  market_maker_loans: "disclosed (5.1M API3 across 2 deals; loan #2 wallet spread 2.5M to Binance/Gate/Bitget/KuCoin deposits within 3 days, Nov 2025; market maker unnamed, Arkham shows no label)"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Buybacks (about $115k in total) are DAO decisions, not automatic on-chain, and no fee share or fee-funded staking yield is documented. Holders have no live claim on revenue; the score describes the business, not holder accrual."
pump_day_price_source: "Gate API3_USDT UTC daily closes, re-run 16 Nov 2026 with scripts/pump_day_test.py (23 of 360 days); the body's earlier count used CoinGecko daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0xe7af7c5982e073ac6525a34821fe1b3e8e432099"
    label: "API3: Treasury / V1 Treasury"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan tag + Arkham label + DAO ownership"
price_usd: 0.1873
price_source: "CoinGecko, 16 Nov 2026 5:26 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### API3 · Overall grade **4.9 / 10 · ❌ FAIL**

**Summary:** Api3 has cleaned up a lot: supply is now hard-capped at exactly 200,000,000 (owner is the dead address, no minters, checked on-chain), the treasury publishes every wallet, and the team is lean and pivoting to Morpho vault curation. But the DAO's own wallets have twice sent API3 to a Binance deposit address on pump days, and in Feb 2026 a DAO multisig funded a wallet that put 610k API3 on Binance the same pump day. Revenue is real but tiny (about $45k a year of curator revenue on DefiLlama, $115k of buybacks to date). The Selling gate fails.

**🚨 Top warning (red line):** The wallet Etherscan labels **"API3: Treasury"** and Arkham labels **"API3: V1 Treasury"** (entity API3, [Arkham](https://intel.arkm.com/explorer/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099)), [`0xe7aF…2099`](https://etherscan.io/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099), sent **250,000 API3 into Etherscan's "Binance Deposit" [`0x3141…12c8`](https://etherscan.io/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8) (Arkham: Binance Deposit, [Arkham](https://intel.arkm.com/explorer/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8)) on 28 Jan 2024, a pump day (+28.8%)** ([in](https://etherscan.io/tx/0x9c5b68350d567bb43b8aa6ad53d1efcf9bb803d7037e0e14316f7d58ca619b3c) → [swept to Binance 14 an hour later](https://etherscan.io/tx/0x2ea16644fc77d3c8087b80ae0e9e4a977c8254250228fd4e9bcd11e2daeb35ea)), and **240,000 more on 23 Apr 2024 (+11.1%)** ([in](https://etherscan.io/tx/0xd0c7779c320b103cd4a72a57aacd81a6d3bd704cb4119919cf8acdb0e8ff4496) → [sweep](https://etherscan.io/tx/0x17dce89f34c7cafe577dc01134cecf0b6fc740183a744b66fd957fb97fe96f38)). **Second warning:** the DAO's published **Vault Multisig** [`0x8e03…8b24`](https://etherscan.io/address/0x8e03609ed680b237c7b6f8020472ca0687308b24) sent 610,000 API3 to [`0x9e65…cc28`](https://etherscan.io/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28) (unlabelled on Arkham too, [Arkham](https://intel.arkm.com/explorer/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28)) on the **10 Feb 2026 pump day (+13.7%)** ([tx](https://etherscan.io/tx/0x0c0a79fe95f787b05982fb76215a45e6ae673416f66fb69322873d91f9cbefcd)), and that wallet paid 609,900 into Binance deposit [`0x4437…8a74`](https://etherscan.io/address/0x4437d9efb54f33c6123777337539f358e7bd8a74) within 71 minutes ([349,900](https://etherscan.io/tx/0xab144c2ac8a1a3bd4dfe88e29158d786b08b8c83b2aad02a94eb4e2138b6081a) · [260,000](https://etherscan.io/tx/0x77da13eb6813c641b66c86cbe55091d2a15c4481b140ba082e3881fbe05165eb)). No DAO proposal or treasury-page entry for either flow was found. Every transfer is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 4/10 | ❌ FAIL |
| 🏛️ Foundation & team | 6/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 6/10 | ✅ PASS |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 7/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 5/10 | ❌ FAIL |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 API3 · Api3 · 4.9 / 10 · ❌ FAIL

> **One line:** A shrunken oracle project turned Morpho vault curator, with a now-fixed 200M supply and an unusually open treasury page, but its DAO wallets keep sending API3 to Binance deposit addresses, three times on pump days, and its revenue is small.

| 📊 Market (CoinGecko, 16 Nov 2026 5:26 AM MST) | 🔗 On-chain (Ethereum, block ~26,427,651, 16 Nov 2026) |
|---|---|
| **Price** $0.1873 | **Token** [`0x0b38…B88a`](https://etherscan.io/address/0x0b38210ea11411557c13457D4dA7dC6ea731B88a#code) |
| **24h / 7d / 30d** 🔴 −2.6% / −21.2% / −34.2% · 1y −67.4% | **`totalSupply()`** 200,000,000 exactly |
| **Market cap** $30.85M · **FDV** $37.46M | **`owner()`** `0x…dEaD` · `getMinterStatus` false for the DAO pool, Treasury Safe and old Agent |
| **24h volume** $1.78M | **DAO pool** [`0x6dd6…6d76`](https://etherscan.io/address/0x6dd655f10d4b9E242aE186D9050B68F725c76d76) ("API3 DAO: Single Staking Pool") 68.65M staked |
| **ATH** $10.30 (6 Apr 2021) · now −98.2% | **Treasury Safe** [`0xb7fa…AE4A`](https://etherscan.io/address/0xb7fa2Cb302C5dC127e61F27b92beC411cbf0AE4A) 17,503,073 API3 (3-of-5) |
| **Holders** 25,101 (Blockscout) | **Pump days, last 365** 24 (Coinbase API3-USD closes; CoinGecko's Jan–Mar 2026 series is corrupt) |

---

## 💰 Revenue — Does it make money? · 4/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Curator fees (yield in Api3-curated Morpho vaults), 30d / 1y | $164,252 / $1,065,826 | [Tier A] [DefiLlama Api3](https://defillama.com/protocol/api3) (16 Nov 2026) |
| Revenue kept by Api3 (curator share), 30d / 1y | **$8,214 / $44,506** | same |
| API3 bought back with revenue | **470,882 API3 for $115,580** (333 fills, last 9 Nov 2026) | [Tier B] [api3.org treasury page](https://api3.org/api3/) |
| Team's own cost picture | ~$1.7M/yr spend before revenue; revenue "expected to bring the net annual cost to under $1M" | [Tier A] [Funding proposal Mar–May 2026](https://moccasin-traditional-bat-376.mypinata.cloud/ipfs/bafkreidq2dqsehj6dyjegyaocgvpvqy2rwjgxjvyp2ibw6r7unzleva4du) |
| OEV recapture | Now "entirely private" after the OEV Network sunset; not measurable on-chain this pass | same · [Unverified] |

**What it means:** Api3 earns real money (curation fees, private OEV, treasury yield) and does spend some of it buying API3. But what is visible is small: ~$45k a year of curator revenue and $115k of buybacks in total, on a $31M token. The project itself expects to lose up to ~$1M a year net. Score **4**.

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Buybacks (about $115k in total) are DAO decisions, not automatic on-chain, and no fee share or fee-funded staking yield is documented. Holders have no live claim on revenue; the score describes the business, not holder accrual.

## 🏛️ Foundation & team — Who is in charge? · 6/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Governance | Legacy on-chain DAO migrated to Snapshot (`api3.eth`); proposals need 500,000 API3 of voting power | [Tier A] [Api3 docs](https://docs.api3.org/dao/api3-token.html) |
| Who holds the keys | Treasury, Vault and Agent are **3-of-5 Safes with the same five signers**, "publicly identified and bound by contract with the API3 Foundation". The funding proposal lists the five signers (three individuals, a law firm and a company) | [Tier B] [api3.org treasury page](https://api3.org/api3/) · [Tier A] [proposal](https://moccasin-traditional-bat-376.mypinata.cloud/ipfs/bafkreidq2dqsehj6dyjegyaocgvpvqy2rwjgxjvyp2ibw6r7unzleva4du) |
| Threshold check | `getThreshold()` = 3 on the Treasury and Agent Safes; four of the five owners are shared | [Tier A] RPC read, 16 Nov 2026 |
| Arkham view | Arkham files the legacy `0xe7aF…` under entity API3 ("API3: V1 Treasury", [Arkham](https://intel.arkm.com/explorer/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099)), but shows the Vault Safe `0x8e03…` only as a "Gnosis Safe Proxy" with no entity ([Arkham](https://intel.arkm.com/explorer/address/0x8e03609ed680b237c7b6f8020472ca0687308b24)). Individual signers are not named here | [Tier B] Arkham, read 16 Nov 2026 ~6:44–6:49 AM MST (signed-in account) |
| Costs | Restructured in Feb 2026; ~$1.7M a year; quarterly funding requests | [Tier A] proposal |

**What it means:** Small, named, multisig-run team with public proposals and a public treasury. That is better than most. The multisig signers can move API3 without a token vote, and they have (see Selling).

## 🪙 Foundation / team holdings — How many coins do they hold? · 6/10 · ✅ PASS

| Bucket | API3 | Notes |
|---|---:|---|
| Treasury Multisig [`0xb7fa…AE4A`](https://etherscan.io/address/0xb7fa2Cb302C5dC127e61F27b92beC411cbf0AE4A) | **17,503,073 (8.75%)** | Includes the final 9,929,000 mint (from 0x0) that closed supply at 200M |
| Agent Multisig [`0xbbe0…13da`](https://etherscan.io/address/0xBBE0dE9757F93e3306aDBfeBE906AB285EDD13DA) | 346,730 | Pays contributors / vesting contracts (e.g. 405k each to two `DelegatedVesting` contracts on 11 Nov 2026, [tx](https://etherscan.io/tx/0xc6ccda6ab01f26712f8de71d826dc514ac16d5e259e7b9a1869d050895e07644)) |
| Uniswap v4 ETH/API3 LP (Vault) | 1,773,417 | per treasury page |
| Market-maker loans | 5,124,703 | Loan #1 2,499,990 (to Apr 2028), loan #2 2,624,713 (to 17 Nov 2026) — agreements, not on-chain |
| Cancelled vestings | 913,972 | claim windows Dec 2026 – Mar 2027 |
| **DAO-controlled total** | **~25.66M (≈ 12.8%)** | all published on [api3.org/api3](https://api3.org/api3/) |
| *Not insiders:* #4 holder [`0xA15b…97B4`](https://etherscan.io/address/0xA15b41801fb5cD518b7Bb4b59EC31b007EA397B4) | 11.52M | Arkham: **Upbit: Cold Wallet** ([Arkham](https://intel.arkm.com/explorer/address/0xA15b41801fb5cD518b7Bb4b59EC31b007EA397B4)), an exchange |
| *Not insiders:* #5 holder [`0xB0bf…898E`](https://etherscan.io/address/0xB0bfC664b44331a8a9c9F6057dF4784E89cd898E) | 5.82M | Arkham: **Coinbase Prime Custody** ([Arkham](https://intel.arkm.com/explorer/address/0xB0bfC664b44331a8a9c9F6057dF4784E89cd898E)), exchange custody |

**What it means:** Every DAO wallet is published and checks out on-chain, and the treasury's own API3 delegates its Snapshot votes to the dead address. About 13% of supply is under the five-signer multisigs, with no lock on the 17.5M in the Treasury Safe. Arkham shows the two large unlabelled top holders are exchanges (Upbit cold storage and Coinbase Prime custody), not hidden insiders. Two other Safes in the DAO's history are not Api3 entities on Arkham: [`0xa742…8d09`](https://etherscan.io/address/0xa742e1d181c59c9c4dd5687172efc119e3868d09) ([Arkham](https://intel.arkm.com/explorer/address/0xa742e1d181c59c9c4dd5687172efc119e3868d09)) relayed 6.07M from the old Primary Agent back to the Vault, and [`0x0c40…2ad4`](https://etherscan.io/address/0x0c4030768601a5b564fcd50ec5957d516b0f2ad4) ([Arkham](https://intel.arkm.com/explorer/address/0x0c4030768601a5b564fcd50ec5957d516b0f2ad4)) received API3 from vesting contracts and sent 636.7k back to the Vault; one of its signers is cheesecakecapital.eth, which points to the fund **Cheesecake Capital** [Tier B, single source]. Score **6**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

**A. Legacy "API3: Treasury" straight into a Binance deposit (2024)**

| Day (UTC) | Route | API3 | Close / 5-day change (Coinbase) | Pump? |
|---|---|---:|---:|---|
| 28 Jan 2024 | Treasury [`0xe7aF…`](https://etherscan.io/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099) → "Binance Deposit" [`0x3141…12c8`](https://etherscan.io/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8) ([in](https://etherscan.io/tx/0x9c5b68350d567bb43b8aa6ad53d1efcf9bb803d7037e0e14316f7d58ca619b3c) · [→ Binance 14](https://etherscan.io/tx/0x2ea16644fc77d3c8087b80ae0e9e4a977c8254250228fd4e9bcd11e2daeb35ea)) | 250,000 | $2.823 / +28.8% | 🔴 Yes |
| 23 Apr 2024 | same route ([in](https://etherscan.io/tx/0xd0c7779c320b103cd4a72a57aacd81a6d3bd704cb4119919cf8acdb0e8ff4496) · [sweep](https://etherscan.io/tx/0x17dce89f34c7cafe577dc01134cecf0b6fc740183a744b66fd957fb97fe96f38)) | 240,000 | $2.568 / +11.1% | 🔴 Yes |
| 2 Jul 2024 | same route ([in](https://etherscan.io/tx/0x8e1b5290cd79577199f8d48f740a3cb244ef5c23c45f0b8a8d218fb1a2ad3421) · [sweep](https://etherscan.io/tx/0xbb02bcf15db4fb1f225e9501a746fa047cf7359ecb5ff13ac345d3657ed19f8f)) | 269,059 | $2.235 / −0.9% | No |

- The deposit address received API3 **only** from the Treasury (6 transfers in its whole history) and swept every lot to Etherscan's "Binance 14" within an hour. [Tier A] chain plus [Tier B] Etherscan labels "API3: Treasury" and "Binance Deposit".
- **Arkham agrees on both ends:** it labels the sender "API3: V1 Treasury" under entity API3 ([Arkham](https://intel.arkm.com/explorer/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099)) and the receiver "Binance Deposit" ([Arkham](https://intel.arkm.com/explorer/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8)), and the Treasury's page shows the 240k, 250k and 269k sends to that deposit. Two Tier B label sources plus Tier A transfers. Arkham does not name whose Binance account it is.
- Pump-day value: 490,000 API3 ≈ **$1.3M** at those days' closes.

**B. DAO Vault Multisig → `0x9e65…` → Binance deposit (2026)**

| Day (UTC) | Route | API3 | 5-day change (Coinbase) | Pump? |
|---|---|---:|---:|---|
| 10 Feb 2026 | Vault → `0x9e65…` 10:04 ([tx](https://etherscan.io/tx/0x0c0a79fe95f787b05982fb76215a45e6ae673416f66fb69322873d91f9cbefcd)) → "Binance Deposit" `0x4437…` 10:51 and 11:15 ([349,900](https://etherscan.io/tx/0xab144c2ac8a1a3bd4dfe88e29158d786b08b8c83b2aad02a94eb4e2138b6081a) · [260,000](https://etherscan.io/tx/0x77da13eb6813c641b66c86cbe55091d2a15c4481b140ba082e3881fbe05165eb)) | 610,000 | +13.7% | 🔴 Yes |
| 12 Feb 2026 | Vault → `0x9e65…` 860,000 + 28,448 ([tx](https://etherscan.io/tx/0xa289664bc96247271efaa510440c93e814ea36e536bbd1007537a2970d62d12f)) → Binance deposit 888,449 ([tx](https://etherscan.io/tx/0x3ca39ee1485783e5e132e02b2d8dfdfc039035e5819d8bcac3390144f85d042b)) | 888,448 | −12.5% | No |
| 19–20 Feb 2026 | 28,448 ([out](https://etherscan.io/tx/0x42f976b9c259fb4c85d96291f82617a4c6c21d14fa642d51d83af5782376e170)) | 28,448 | — | No |
| 18 May 2026 | Vault → `0x9e65…` ([tx](https://etherscan.io/tx/0x5bd5a05d5b3b9783d84bb85688bbbdfcde544ee0c3950a72e101ff5fcbb93d1c)) → Binance deposit 11 min later ([tx](https://etherscan.io/tx/0x42106d231e936b9cefe859a3b45c3b0346372b9c25d737dbcde9013434a4ebb8)) | 300,000 | −9.1% | No |

- `0x9e65…` has only ever received API3 from the Vault and only ever sent it to that one Binance deposit: **1,826,797 API3 in total**. Arkham has no entity for it ([Arkham](https://intel.arkm.com/explorer/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28)), and shows the Vault itself only as a Gnosis Safe Proxy ([Arkham](https://intel.arkm.com/explorer/address/0x8e03609ed680b237c7b6f8020472ca0687308b24)). Who controls `0x9e65…` is [Unverified] (a contributor payout or an OTC/sale account are both possible). The Mar–May 2026 funding proposal describes the restructuring and ETH sales, but **no API3 sale** ([proposal](https://moccasin-traditional-bat-376.mypinata.cloud/ipfs/bafkreidq2dqsehj6dyjegyaocgvpvqy2rwjgxjvyp2ibw6r7unzleva4du)).

**C. Disclosed market-maker loans.** Loan #2 went from the Vault to [`0xcb92…3a81`](https://etherscan.io/address/0xcb92bd118362f834110eb6f08477b5a602393a81) on 15 Nov 2025 ([tx](https://etherscan.io/tx/0x02bac8cb73e969d0ad125d82bbb834d5a3fd324697582df6cd524cd126641064)), which spread ~2.5M into Binance, Gate, Bitget and KuCoin deposits within three days (e.g. [709,990 → Binance deposit](https://etherscan.io/tx/0x94f372932a4e01b0a1d06ee4750f675333f9db48e8b40047f62e66ddbfe8aafd)). Arkham has no label for `0xcb92…` ([Arkham](https://intel.arkm.com/explorer/address/0xcb92bd118362f834110eb6f08477b5a602393a81)); its first page shows a 124.7k lot from the Vault Safe and onward sends to Gate, Binance, Bitget, KuCoin, Bitvavo and Coinbase deposits. **The market maker is unnamed:** neither the treasury page nor Arkham says who it is. [`0xf042…b1c2`](https://etherscan.io/address/0xf042392443ccecf67e8672f57bc59b14710db1c2) still holds the 1.5M it got from the Vault on 10 Apr 2026; Arkham tags it only "API3 Whale" ([Arkham](https://intel.arkm.com/explorer/address/0xf042392443ccecf67e8672f57bc59b14710db1c2)). Whether it is loan #1 is [Unverified]. Not pump days (−11.5%), and disclosed on the treasury page. In 2021 the old Treasury also sent 500,000 API3 to "Wintermute: Multisig" ([tx](https://etherscan.io/tx/0x7cf618c8194160b8c9e2adc19528484eb287f950e5bcdffc4f409b70aed156fa)).

**What it means:** A DAO treasury wallet sending tokens straight into a Binance deposit on two pump days, and a DAO multisig funding a wallet that hit Binance within the hour on a third, with no disclosure found, fails the rule. The amounts are moderate (~1.1M API3 on pump days) and the project is otherwise transparent, so **3**, not lower. That **trips the Selling gate**. Arkham's labels confirm the 2024 sender was Api3's own treasury and the receiver a Binance deposit, so the score does not change.

- **One-hop amendment (16 Nov 2026):** API3 discloses market-maker loans from the DAO treasury (see C. above and the [Api3 token docs](https://docs.api3.org/dao/api3-token.html)), a plausible published reason for treasury-funded wallets reaching Binance. The market maker is unnamed, so the link to a specific loan stays [Unverified]. Neither (a) nor (b) holds: no exchange account is attributed to the team, and no swap, proceeds return or statement shows a sale. Under the amended rule Selling scores **4 (not proven)** with no silence penalty; this replaces the earlier score and penalty described above.

## 📊 Tokenomics & supply · 7/10 · ✅ PASS

- **Fixed at exactly 200,000,000.** `owner()` returns `0x…dEaD`; `getMinterStatus()` is false for the DAO pool, the Treasury Safe and the old Agent (RPC, 16 Nov 2026). The docs say the final mint went to the Treasury multisig and ownership was then sent to the dead address ([docs](https://docs.api3.org/dao/api3-token.html)).
- History: 100M at launch, doubled by staking inflation until 28–29 Oct 2026.
- **Unlocks still ahead:** staking rewards minted before the migration unlock one year after each mint; the last one unlocks **28 Oct 2027**. Circulating 164.7M per CoinGecko.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.78M volume (CoinGecko) on a $31M cap. Coinbase API3-USD traded ~200k API3 (~$38k) on 15 Nov 2026. Main venues: Binance, Coinbase, OKX, Bithumb, BtcTurk (their wallets are top holders).
- Down 98% from the high. The DAO's own Uniswap v4 position (184 ETH + 1.77M API3) is a large share of on-chain depth.

## 🧑‍💻 Product & development · 5/10 · ❌ FAIL

- Oracle products (Airnode, dAPIs) plus **Morpho vault curation** (Core USDC, Kabu USDC). The OEV Network was sunset; OEV is now private.
- GitHub `api3dao`: last commit 4 Nov 2026 (dao-dashboard). Development has narrowed with the restructuring.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- Curated-vault TVL **$10.87M** ([DefiLlama](https://defillama.com/protocol/api3)). Oracle customer counts were not re-measured this pass.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No exploit of the token, DAO pool or treasury found. The token has no admin left (owner dead). Treasury wallets are 3-of-5 Safes.
- Audit reports for the DAO contracts and Morpho vault configs were not read this pass [Unverified].

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No regulator action against Api3 or API3 found. The API3 Foundation's jurisdiction and any licences were not checked this pass. Not proven either way.

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| **17 Nov 2026** | Market-maker loan #2 (2,624,713 API3) expires: watch whether it returns to the Vault |
| 1 Dec 2026 · 1 Feb 2027 · 15 Mar 2027 | Cancelled-vesting claim windows (179,666 / 36,483 / 697,823 API3) |
| Quarterly | DAO funding proposals (next cycle from Jun 2026 onward) |
| 28 Oct 2027 | Last staking-reward unlock; after that nothing is locked |
| 10 Apr 2028 | Market-maker loan #1 (2,499,990 API3) expires |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Treasury → exchange during a pump | 🔴 **Yes:** "API3: Treasury" (Arkham: "API3: V1 Treasury") → Binance deposit on 28 Jan 2024 (+28.8%) and 23 Apr 2024 (+11.1%). [28 Jan](https://etherscan.io/tx/0x9c5b68350d567bb43b8aa6ad53d1efcf9bb803d7037e0e14316f7d58ca619b3c) · [23 Apr](https://etherscan.io/tx/0xd0c7779c320b103cd4a72a57aacd81a6d3bd704cb4119919cf8acdb0e8ff4496) |
| Treasury-funded wallet → exchange during a pump | 🔴 **Yes:** Vault → `0x9e65…` → Binance deposit, 10 Feb 2026 (+13.7%). [Vault tx](https://etherscan.io/tx/0x0c0a79fe95f787b05982fb76215a45e6ae673416f66fb69322873d91f9cbefcd) · [deposit tx](https://etherscan.io/tx/0xab144c2ac8a1a3bd4dfe88e29158d786b08b8c83b2aad02a94eb4e2138b6081a) |
| Live mint path | 🟢 No: owner `0x…dEaD`, no minters. [token](https://etherscan.io/address/0x0b38210ea11411557c13457D4dA7dC6ea731B88a#readContract) |
| Market-maker loans | 🟡 Disclosed (5.1M API3), market maker unnamed; loan #2 went to exchange deposits within 3 days. [tx](https://etherscan.io/tx/0x02bac8cb73e969d0ad125d82bbb834d5a3fd324697582df6cd524cd126641064) |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0xe7aF…`](https://etherscan.io/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099) | API3: Treasury / V1 Treasury | Etherscan tag + Arkham label + DAO ownership | high | yes | Selling: sent 250,000 and 240,000 API3 into a Binance deposit on 28 Jan and 23 Apr 2024 pump days |
| DAO multisig → wallet → Binance within the hour | Api3 DAO | On-chain one-hop funding | high | yes (on-chain) | Selling: third pump-day deposit |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` (API3 token) for the legacy Treasury, Primary and Secondary Agents, Treasury/Agent/Vault Safes, `0x9e65…`, `0xcb92…`, `0x3141…`, `0xf042…`; read 16 Nov 2026 MST
- [Tier A] Ethereum RPC (publicnode): `owner()`, `totalSupply()`, `getMinterStatus()`, Safe `getOwners()`/`getThreshold()`, block ~26,427,651
- [Tier B] Etherscan name tags read 16 Nov 2026: "API3: Treasury", "API3 DAO: Single Staking Pool", "Binance Deposit" (`0x3141…`, `0x4437…`, `0x77ab…`), "Binance 14", "Gate Deposit", "Bitget Deposit", "KuCoin Deposit", "Wintermute: Multisig", "Binance: Cold Wallet 20", "OKX 219", "Bithumb 394", "BtcTurk 13", "eToro 4", "Uniswap V4: Pool Manager"
- [Tier A] Blockscout v2: top holders, holder count
- [Tier A] [Api3 token docs](https://docs.api3.org/dao/api3-token.html) · [Funding proposal Mar–May 2026 (IPFS)](https://moccasin-traditional-bat-376.mypinata.cloud/ipfs/bafkreidq2dqsehj6dyjegyaocgvpvqy2rwjgxjvyp2ibw6r7unzleva4du) · [DAO tech docs](https://dao-docs.api3.org/technical/)
- [Tier B] [api3.org token and treasury page](https://api3.org/api3/) (wallet list, MM loans, buybacks; self-published)
- [Tier A] DefiLlama Api3 fees/revenue; CoinGecko `api3` (16 Nov 2026 5:26 AM MST; its Jan–Mar 2026 daily series alternates between two price levels and was not used); Coinbase Exchange API3-USD daily candles (from 9 Dec 2021) for every pump test
- [Tier B] Arkham, read 16 Nov 2026 ~6:44–6:49 AM MST (signed-in account): "API3: V1 Treasury" [0xe7aF…](https://intel.arkm.com/explorer/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099) · Binance Deposit [0x3141…](https://intel.arkm.com/explorer/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8) · Vault Safe shown only as Gnosis Safe Proxy [0x8e03…](https://intel.arkm.com/explorer/address/0x8e03609ed680b237c7b6f8020472ca0687308b24) · unlabelled [0x9e65…](https://intel.arkm.com/explorer/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28), [0xcb92…](https://intel.arkm.com/explorer/address/0xcb92bd118362f834110eb6f08477b5a602393a81) · "API3 Whale" tag only [0xf042…](https://intel.arkm.com/explorer/address/0xf042392443ccecf67e8672f57bc59b14710db1c2) · Safes [0xa742…](https://intel.arkm.com/explorer/address/0xa742e1d181c59c9c4dd5687172efc119e3868d09) and [0x0c40…](https://intel.arkm.com/explorer/address/0x0c4030768601a5b564fcd50ec5957d516b0f2ad4) (signer cheesecakecapital.eth) · Upbit: Cold Wallet [0xA15b…](https://intel.arkm.com/explorer/address/0xA15b41801fb5cD518b7Bb4b59EC31b007EA397B4) · Coinbase Prime Custody [0xB0bf…](https://intel.arkm.com/explorer/address/0xB0bfC664b44331a8a9c9F6057dF4784E89cd898E). Token filter is Enterprise-only, so only the default transfer page was read
- [Unverified] who controls `0x9e65…`; which market maker took loans #1 and #2; whether the 2024 Treasury → Binance sends had a proposal; OEV revenue; audits; Foundation jurisdiction

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 28 Jan 2024 pump day: "API3: Treasury" 250k → Binance deposit → Binance 14 | [Treasury](https://etherscan.io/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099) · [in](https://etherscan.io/tx/0x9c5b68350d567bb43b8aa6ad53d1efcf9bb803d7037e0e14316f7d58ca619b3c) · [sweep](https://etherscan.io/tx/0x2ea16644fc77d3c8087b80ae0e9e4a977c8254250228fd4e9bcd11e2daeb35ea) · [deposit](https://etherscan.io/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8) | A chain + B tags | 16 Nov 2026 |
| 23 Apr 2024 pump day: 240k, same route | [in](https://etherscan.io/tx/0xd0c7779c320b103cd4a72a57aacd81a6d3bd704cb4119919cf8acdb0e8ff4496) · [sweep](https://etherscan.io/tx/0x17dce89f34c7cafe577dc01134cecf0b6fc740183a744b66fd957fb97fe96f38) | A + B | 16 Nov 2026 |
| 2 Jul 2024 (not a pump day): 269,059, same route | [in](https://etherscan.io/tx/0x8e1b5290cd79577199f8d48f740a3cb244ef5c23c45f0b8a8d218fb1a2ad3421) · [sweep](https://etherscan.io/tx/0xbb02bcf15db4fb1f225e9501a746fa047cf7359ecb5ff13ac345d3657ed19f8f) | A + B | 16 Nov 2026 |
| 10 Feb 2026 pump day: Vault 610k → `0x9e65…` → Binance deposit in 47–71 min | [Vault](https://etherscan.io/address/0x8e03609ed680b237c7b6f8020472ca0687308b24) · [in](https://etherscan.io/tx/0x0c0a79fe95f787b05982fb76215a45e6ae673416f66fb69322873d91f9cbefcd) · [349,900](https://etherscan.io/tx/0xab144c2ac8a1a3bd4dfe88e29158d786b08b8c83b2aad02a94eb4e2138b6081a) · [260,000](https://etherscan.io/tx/0x77da13eb6813c641b66c86cbe55091d2a15c4481b140ba082e3881fbe05165eb) · [deposit](https://etherscan.io/address/0x4437d9efb54f33c6123777337539f358e7bd8a74) · [Arkham](https://intel.arkm.com/explorer/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28) | A + B tag · recipient [Unverified], unlabelled on Arkham | 16 Nov 2026 |
| `0x9e65…` sent 1,826,797 API3 to that Binance deposit by May 2026 | [0x9e65](https://etherscan.io/address/0x9e6538212ca6afccb03e05d929fe415e6621cc28) · [12 Feb](https://etherscan.io/tx/0x3ca39ee1485783e5e132e02b2d8dfdfc039035e5819d8bcac3390144f85d042b) · [18 May](https://etherscan.io/tx/0x42106d231e936b9cefe859a3b45c3b0346372b9c25d737dbcde9013434a4ebb8) | A | 16 Nov 2026 |
| Arkham: `0xe7aF…` is "API3: V1 Treasury" (entity API3); `0x3141…` is a Binance Deposit; Treasury page shows 240k/250k/269k sends to it | [0xe7aF](https://intel.arkm.com/explorer/address/0xe7aF7c5982e073aC6525a34821fe1B3e8E432099) · [0x3141](https://intel.arkm.com/explorer/address/0x314187ab1875039ff4f78bf788b81d4e64d112c8) | B | 16 Nov 2026 ~6:44 AM MST |
| Arkham: top holders `0xA15b…` = Upbit: Cold Wallet, `0xB0bf…` = Coinbase Prime Custody | [0xA15b](https://intel.arkm.com/explorer/address/0xA15b41801fb5cD518b7Bb4b59EC31b007EA397B4) · [0xB0bf](https://intel.arkm.com/explorer/address/0xB0bfC664b44331a8a9c9F6057dF4784E89cd898E) | B | 16 Nov 2026 ~6:49 AM MST |
| Vault Safe is the DAO's published "Vault Multisig" | [api3.org treasury page](https://api3.org/api3/) | B (self-published) | 16 Nov 2026 |
| MM loan #2: 2.5M to `0xcb92…` (market maker unnamed; unlabelled on Arkham), then to Binance/Gate/Bitget/KuCoin deposits | [loan tx](https://etherscan.io/tx/0x02bac8cb73e969d0ad125d82bbb834d5a3fd324697582df6cd524cd126641064) · [→ Binance deposit](https://etherscan.io/tx/0x94f372932a4e01b0a1d06ee4750f675333f9db48e8b40047f62e66ddbfe8aafd) | A + B | 16 Nov 2026 |
| Supply fixed: owner dead, no minters, 200,000,000 | [token read](https://etherscan.io/address/0x0b38210ea11411557c13457D4dA7dC6ea731B88a#readContract) · [docs](https://docs.api3.org/dao/api3-token.html) | A | 16 Nov 2026 |
| Revenue $44,506 / 1y (curator share) | [DefiLlama](https://defillama.com/protocol/api3) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham pass: done 16 Nov 2026.** Confirmed the legacy Treasury and the Binance deposit; top holders are Upbit and Coinbase custody. Still unlabelled: `0x9e65…`, `0xcb92…`, `0xf042…` | Ask Api3 to name the loan market makers and the `0x9e65…` recipient | Free |
| 2 | **Who is `0x9e65…`?** | Ask the multisig signers; search the DAO forum and Snapshot for Feb 2026 API3 transfers | Free |
| 3 | **Were the 2024 Treasury → Binance sends approved?** | Check the DAO tracker's secondary proposals for Jan, Apr and Jul 2024 | Free |
| 4 | **Does MM loan #2 come back on 17 Nov 2026?** | Watch the Vault for 2,624,713 API3 inbound | Free |
| 5 | **OEV and total revenue** | Read the team's Dune dashboard (`ugurmersin/api3-revenue-and-expenses`) and reconcile with Vault inflows | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
