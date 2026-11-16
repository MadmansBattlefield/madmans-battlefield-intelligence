---
ticker: XLM
name: Stellar
chain: stellar
contract: "native (Stellar network lumens)"
overall_score: 5.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 7
  insider_holdings: 4
  selling_behavior: 6
  tokenomics_supply: 5
  liquidity_market: 9
  product_development: 8
  adoption_customers: 7
  security_audits: 7
  regulatory: 8
  catalysts: 6
gates_failed: [revenue]
red_lines:
  hack_exploit: none
  network_halt: none_found_in_series
  sdf_exchange_sends_on_pump_days: watch_disclosed
  single_key_sdf_account: tripped
price_usd: 0.140304
price_source: "CoinGecko, 15 Nov 2026 6:45 AM MST"
chain_read_ledger: 65492889
last_updated: 2026-11-15
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### XLM · Overall grade **5.7 / 10 · ❌ FAIL**

**Summary:** A busy, well-run payments and RWA network with a transparent non-profit foundation, but users pay only ~$492k a year in fees, the SDF still holds ~28.6% of the real 50.0B supply, and it releases roughly 2.7B XLM a year into the market to fund operations.

> ⚠️ **Top warning:** SDF "Product & Innovation Hot 2" holds **554,096,554 XLM on a single key with zero thresholds** — one signature can move it ([Stellar.expert](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) · [Horizon signers](https://horizon.stellar.org/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ)). Separately, SDF sent **347.9M XLM straight to exchange-labelled accounts** in 12 months (Bitstamp [`GDBK3AHP…`](https://stellar.expert/explorer/public/account/GDBK3AHPQ7AO2U7JYEBFGJ2PBDVVFANHH4NQANDX6Q4GZ266WZ3IOIXN), Kraken [`GA5XIGA5…`](https://stellar.expert/explorer/public/account/GA5XIGA5C7QTPTWXQHY6MCJRMTRZDOSHR6EFIBNDQTCQHG262N4GGKTM)) — disclosed, and not pump-weighted.

**Sections passed: 8 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 9/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 7/10 | ✅ PASS |
| 🛡️ Security & audits | 7/10 | ✅ PASS |
| ⚖️ Regulatory | 8/10 | ✅ PASS |
| 📅 Catalysts & calendar | 6/10 | ✅ PASS |

*Pass = 6 or more out of 10. Full details for every section follow below. Overall fails the **Revenue gate** (2 ≤ 3).*

---


# 🪪 XLM · Stellar · 5.7 / 10 · ❌ FAIL

> **One line:** A busy, well-run payments and RWA network with a transparent non-profit foundation, but users pay only ~$492k a year in fees, the SDF still holds ~28.6% of the real 50.0B supply, and it releases roughly 2.7B XLM a year into the market to fund operations.

ℹ️ **Adapted for a layer-1 with a foundation.** "Revenue" = network fees and where they go. "Foundation" = the Stellar Development Foundation (SDF). "Holdings / Selling" = the SDF's published mandate accounts and what leaves them.

⚠️ **Correction to the old (10 Nov) draft:** it said the SDF holds "13.7% of the 105.44B total". The ledger still reports 105.44B `total_coins`, but **55.44B of that sits in a dead account** (the 2019 burn; master key weight 0). Real supply is **~50.0B**, so the SDF's share is **~28.6%**, not 13.7%.

| 📊 Market (CoinGecko, 15 Nov 2026 6:45 AM MST) | 🔗 On-chain (Horizon, ledger 65,492,889, 6:48 AM MST) |
|---|---|
| **Price** $0.1403 | **Asset** native lumens · protocol version **29** |
| **24h / 7d / 30d / 1y** 🔴 −1.5% / −7.1% / −23.2% / −46.4% | **Ledger `total_coins`** 105,443,902,087 |
| **Market cap** $4.97B · **FDV** $7.02B · rank #19 | **Burned in 2019 (dead account)** 55,442,115,250 |
| **24h volume** $314.3M | **Real supply** 50,001,786,837 (matches CoinGecko total 50,001,786,837) |
| **ATH** $0.8756 (2 Jan 2018) · now −84% | **Circulating (CoinGecko)** 35.41B (70.8%) |
| **1 year ago** $0.2595 (16 Nov 2025 close) | **SDF mandate accounts** 14,324,301,801 (**28.6%**) |
| | **Fee pool** 11,040,090 XLM · **base fee** 100 stroops (0.00001 XLM) · **base reserve** 0.5 XLM |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| 24h fees | $1,122 | [Tier A] DefiLlama `stellar` fees, 15 Nov 2026 |
| 30-day fees | $28,384 | [Tier A] DefiLlama |
| 12-month fees | $492,295 | [Tier A] DefiLlama |
| All-time fees (since 2020) | $2,147,195 | [Tier A] DefiLlama |
| Fees by month | Nov 25 $83.2k · Dec $77.8k · Jan $59.6k · Feb $21.6k · Mar $25.2k · Apr $20.6k · May $31.9k · Jun $34.9k · Jul $38.7k · Aug $38.1k · Sep $45.7k · Oct $40.4k · Nov 1–14 $10.6k | [Tier A] DefiLlama |
| Cross-check (SDF Q3 report) | 1.04B transactions × $0.00012 average fee ≈ $125k for Q3; DefiLlama Jul–Sep = $122.5k | [Tier A] SDF Q3 2026 report · calculated |
| Where fees go | Into the ledger's **fee pool**. Inflation payouts were switched off in 2019, so the pool is never paid out — fees are effectively taken out of circulation | [Tier A] DefiLlama methodology ("All the fee goes to fee pool") · ledger header |
| Fee pool today | **11,040,090 XLM** (~$1.55M at spot) — the lifetime stock of collected fees | [Tier A] Horizon `/ledgers`, ledger 65,492,889 |
| Validator rewards | **None.** "Stellar validators do not earn rewards" | [Tier A] SDF Q3 2026 report |
| Fees vs SDF release | ~$492k of fees a year vs ~2.7B XLM (~$375M at spot) of SDF deployment a year (see Selling) | Calculated |

**What it means:** Fees are tiny by design (~$0.0001 a transaction). They are effectively burned, which is good, but at ~$0.5M a year on a ~$5B asset (~0.01%) they do not support the token's value. Stellar's case is utility (account reserves, anti-spam, a bridge asset), not cash flow.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Foundation | **Stellar Development Foundation (SDF)**, non-profit. "SDF is not a charity. It is self-funded, pays taxes, and has no shareholders" | [Tier A] [stellar.org/foundation/mandate](https://stellar.org/foundation/mandate) |
| Leadership | Team page lists Denelle Dixon, Jed McCaleb, David Mazières, Tomer Weller, Nicolas Barry, Justin Rice and others; Q3 2026 report opens with "A Letter from Denelle" | [Tier A] [stellar.org/foundation/team](https://stellar.org/foundation/team) · Q3 report |
| Board of directors | Jed McCaleb, Lin-Hua Wu, Ronaldo Lemos, Ginger Baker, Asiff Hirji | [Tier A] team page |
| Legal registration (state, file number) | Not read this pass | [Unverified] — see Open items |
| Reporting | Quarterly "Quarter in Review" reports with XLM spend by mandate category and wallet balances (Q3 2026 published Oct 2026) | [Tier A] [stellar.org/quarterly-reports](https://stellar.org/quarterly-reports) |
| Reference software | `stellar/stellar-core`: last push 14 Nov 2026; **135 commits in the last 13 weeks**; releases v28.0.0 (13 Aug), v28.0.1 (1 Sep), v29.0.0 (5 Oct), **v30.0.0 (16 Oct 2026)** | [Tier A] GitHub API |
| Consensus control | Stellar Consensus Protocol; the Tier 1 validator set grew **from 7 to 10** in Q3 2026 (MoneyGram, Figure Markets and Range joined) | [Tier A] SDF Q3 2026 report |
| Key control on SDF accounts | 11 of 12 mandate accounts need **3 signature weight** (6–8 listed signers, most weight 1). **Product & Innovation Hot 2 ([`GDWXQOTI…`](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ)) has a single key and zero thresholds** | [Tier A] Horizon account reads ([raw signers](https://horizon.stellar.org/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ)) |

**What it means:** It is a known, reporting non-profit with named leaders, a board and real engineering output. The weak spots are that one organisation still steers development and treasury, and one hot account holding ~554M XLM sits behind a single key.

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

Live balances, Horizon, 15 Nov 2026 ~6:50 AM MST. Addresses come from the SDF mandate page, and every balance matched the page to the lumen.

| SDF account | Address | XLM | Signers / threshold |
|---|---|---:|---|
| Direct Development, Available | [`GB6NVEN5HSUBKMYCE5ZOWSK5K23TBWRUQLZY3KNMXUZ3AQ2ESC4MY4AQ`](https://stellar.expert/explorer/public/account/GB6NVEN5HSUBKMYCE5ZOWSK5K23TBWRUQLZY3KNMXUZ3AQ2ESC4MY4AQ) | 1,975,727,280 | 6 / 3 |
| Direct Development Hot 1 | [`GATL3ETTZ3XDGFXX2ELPIKCZL7S5D2HY3VK4T7LRPD6DW5JOLAEZSZBA`](https://stellar.expert/explorer/public/account/GATL3ETTZ3XDGFXX2ELPIKCZL7S5D2HY3VK4T7LRPD6DW5JOLAEZSZBA) | 318,478,275 | 8 / 2 (high 3) |
| Direct Development Hot 2 | [`GAKGC35HMNB7A3Q2V5SQU6VJC2JFTZB6I7ZW77SJSMRCOX2ZFBGJOCHH`](https://stellar.expert/explorer/public/account/GAKGC35HMNB7A3Q2V5SQU6VJC2JFTZB6I7ZW77SJSMRCOX2ZFBGJOCHH) | 151,645,199 | 8 / 3 |
| Direct Development Hot 3 | [`GAPV2C4BTHXPL2IVYDXJ5PUU7Q3LAXU7OAQDP7KVYHLCNM2JTAJNOQQI`](https://stellar.expert/explorer/public/account/GAPV2C4BTHXPL2IVYDXJ5PUU7Q3LAXU7OAQDP7KVYHLCNM2JTAJNOQQI) | 71,978,416 | 8 / 3 |
| Growth 1 | [`GDUY7J7A33TQWOSOQGDO776GGLM3UQERL4J3SPT56F6YS4ID7MLDERI4`](https://stellar.expert/explorer/public/account/GDUY7J7A33TQWOSOQGDO776GGLM3UQERL4J3SPT56F6YS4ID7MLDERI4) | 4,046,891,611 | 6 / 3 |
| Growth Hot 1 | [`GC3ITNZSVVPOWZ5BU7S64XKNI5VPTRSBEXXLS67V4K6LEUETWBMTE7IH`](https://stellar.expert/explorer/public/account/GC3ITNZSVVPOWZ5BU7S64XKNI5VPTRSBEXXLS67V4K6LEUETWBMTE7IH) | 186,517,923 | 8 / 3 |
| Growth 2 | [`GBEVKAYIPWC5AQT6D4N7FC3XGKRRBMPCAMTO3QZWMHHACLHTMAHAM2TP`](https://stellar.expert/explorer/public/account/GBEVKAYIPWC5AQT6D4N7FC3XGKRRBMPCAMTO3QZWMHHACLHTMAHAM2TP) | 974,795,394 | 6 / 3 |
| Product & Innovation 1 | [`GCPWKVQNLDPD4RNP5CAXME4BEDTKSSYRR4MMEL4KG65NEGCOGNJW7QI2`](https://stellar.expert/explorer/public/account/GCPWKVQNLDPD4RNP5CAXME4BEDTKSSYRR4MMEL4KG65NEGCOGNJW7QI2) | 402,786,196 | 6 / 3 |
| Product & Innovation 2 | [`GDKIJJIKXLOM2NRMPNQZUUYK24ZPVFC6426GZAEP3KUK6KEJLACCWNMX`](https://stellar.expert/explorer/public/account/GDKIJJIKXLOM2NRMPNQZUUYK24ZPVFC6426GZAEP3KUK6KEJLACCWNMX) | 2,376,599,180 | 6 / 3 |
| Product & Innovation Hot 2 | [`GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ`](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) | 554,096,554 | **1 / 0 (single key)** |
| Assets & Liquidity | [`GAMGGUQKKJ637ILVDOSCT5X7HYSZDUPGXSUW67B2UKMG2HEN5TPWN3LQ`](https://stellar.expert/explorer/public/account/GAMGGUQKKJ637ILVDOSCT5X7HYSZDUPGXSUW67B2UKMG2HEN5TPWN3LQ) | 3,125,166,934 | 6 / 3 |
| Assets & Liquidity Hot | [`GANII5Y2LABEBK74NWNKS4NREX2T52YTBGQDRDKVBFRIIF5VE4ORYOVY`](https://stellar.expert/explorer/public/account/GANII5Y2LABEBK74NWNKS4NREX2T52YTBGQDRDKVBFRIIF5VE4ORYOVY) | 139,618,839 | 8 / 3 |
| **Total** | 12 accounts | **14,324,301,801** | |

| Bucket | XLM | % of real supply (50.0B) | Source |
|---|---:|---:|---|
| SDF mandate accounts | 14,324,301,801 | **28.6%** | [Tier A] Horizon |
| All 48 accounts tagged `sdf` on Stellar Expert | 14,324,442,874 (the other 36 hold ~141k in total) | 28.6% | [Tier B] Stellar Expert directory (the SDF Q3 report points to it) |
| SDF's own figure | "roughly 14.7 billion" | — | [Tier A] SDF Q3 2026 report (balances as of 12 Oct 2026) |
| Not held by SDF | ~35.68B | 71.4% | Calculated (CoinGecko circulating 35.41B) |
| Original SDF development account | 11,953,799,117 at start → 1,975,727,280 now | — | [Tier A] mandate page |

- **Label mismatch:** the Q3 report's wallet table lists "Growth 1 = 88.3M" and "Growth 3 = 4.11B", while the mandate page calls the 4.05B account "Growth 1". The totals line up, but the names don't. [Tier A] both documents.

**What it means:** The holdings are unusually transparent: the wallets are published and re-read here to the lumen. But one organisation still controls more than a quarter of the real supply, and one hot account holding 554M XLM can move on a single signature.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**Pump test:** CoinGecko daily closes, 16 Nov 2025 – 15 Nov 2026: **38 of 360 testable days (10.6%)** were pump days. Clusters: 27–28 Nov; 5–7 Jan; 14–17 Mar; 17–21 Apr; **28 May – 2 Jun (peak +76.3%)**; 16–20 Jun; 2–5 Jul; 21–25 Aug; 8 Sep; 21–29 Sep. Last pump day was 29 Sep 2026 (+14.9%).

**Disclosure:** the SDF says it "sells XLM from this account on public exchanges like Kraken, Coinbase, and Bitstamp and through direct sales, in order to pay for the operational expenses" ([Tier A] mandate page).

**12-month trace of all 12 SDF mandate accounts** (Horizon `/payments`, 15 Nov 2025 – 15 Nov 2026, 12,060 operations):

| Flow | XLM | Note |
|---|---:|---|
| Moved between SDF accounts | 8,429,718,885 | Internal |
| **Sent to non-SDF accounts** | **3,483,964,224** | 954 recipients (~7% of real supply) |
| … of which on pump days | 440,822,596 (**12.7%** of outflow) | Pump days are 10.6% of days, so roughly in line |
| **Sent straight to exchange-labelled accounts** | **347,925,878** | Bitstamp 159.1M · Kraken 108.5M · Coinbase deposit accounts 80.3M |
| … of which on pump days | 17,038,572 (**4.9%**) | **Below** the pump-day base rate |
| Received from non-SDF accounts | 465,164,397 | Mostly old SDF wallets (e.g. "SDF Growth 1" `GCVJDBAL…`, 253M) and returns |

**Outflow by month (M XLM):** Nov 25 188 · Dec 110 · Jan 161 · Feb 396 · Mar 119 · Apr 279 · May 314 · Jun 344 · Jul 357 · **Aug 447** · Sep 338 · Oct 276 · Nov 1–14 156.

**Largest external recipients (12 months):**

| Recipient | XLM received | On pump days | Label | Balance now |
|---|---:|---:|---|---:|
| [`GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5`](https://stellar.expert/explorer/public/account/GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5) | 631,232,423 (152 payments) | 121,800,000 | None — forwards to [`GC6S2SVX…`](https://stellar.expert/explorer/public/account/GC6S2SVXVMPECWS65YXIX72TF5YUYV2MFKLTINSS3XTWAGQWQAJDLIPM) | 0 |
| [`GDZAI56JE57EAUA46ZVUZ7VHROBDD7X3WF264XDQLWSFWRVJBNUV6ZHY`](https://stellar.expert/explorer/public/account/GDZAI56JE57EAUA46ZVUZ7VHROBDD7X3WF264XDQLWSFWRVJBNUV6ZHY) | 513,608,238 | 0 | None — forwards to [`GAKTGHDI…`](https://stellar.expert/explorer/public/account/GAKTGHDIAQK6ACNHXQMUN7X7P245KRNAKEBJ6A73T5RWCOYHEN6ZAULX) (303M), [`GAH3EBQH…`](https://stellar.expert/explorer/public/account/GAH3EBQHRYZMNGGAJTQJIC7VTNNUMUHKFJFTB3AWYV3T275Q7ALT437S) (87M), [`GDSKF3UL…`](https://stellar.expert/explorer/public/account/GDSKF3ULSQJSIVAZMFQOW6HEDJBWN2NIHFOTXA45JWKRCGM5ADD7AY52) (85M) | 32.5M |
| [`GDDUETSYDSHJMU5J73WHR4SQOAWRUM5SNLHXBQKM36EQ244GHSRS5AHF`](https://stellar.expert/explorer/public/account/GDDUETSYDSHJMU5J73WHR4SQOAWRUM5SNLHXBQKM36EQ244GHSRS5AHF) | 495,000,001 | 9,000,000 | None — forwards 495.8M to [`GCA34HBK…`](https://stellar.expert/explorer/public/account/GCA34HBKNLWN3AOXWBRW5Y3HSGHCWF3UDBRJ5YHGU6HWGJZEPO2NSXI3) | 0 |
| [`GAEPN735I2YWGIW6J4MXMEXLLPKEOV4ERNBVJTTZ7J3PHOSANHDHO3ZE`](https://stellar.expert/explorer/public/account/GAEPN735I2YWGIW6J4MXMEXLLPKEOV4ERNBVJTTZ7J3PHOSANHDHO3ZE) | 185,000,000 | 106,000,000 | None — sent 116M back to SDF Hot 3 and 20M to a Coinbase deposit account; looks like an SDF operating wallet | 0 |
| [`GDBK3AHPQ7AO2U7JYEBFGJ2PBDVVFANHH4NQANDX6Q4GZ266WZ3IOIXN`](https://stellar.expert/explorer/public/account/GDBK3AHPQ7AO2U7JYEBFGJ2PBDVVFANHH4NQANDX6Q4GZ266WZ3IOIXN) | 159,125,661 | 8,000,000 | **Bitstamp** (home domain bitgo.com) | 11.1M |
| [`GA5XIGA5C7QTPTWXQHY6MCJRMTRZDOSHR6EFIBNDQTCQHG262N4GGKTM`](https://stellar.expert/explorer/public/account/GA5XIGA5C7QTPTWXQHY6MCJRMTRZDOSHR6EFIBNDQTCQHG262N4GGKTM) | 108,512,905 | 5,636,708 | **Kraken** | 0.2M |
| [`GDHMJXMHWBX7YKIY7TZBWLETQR5K6KAXYRBME2FIBRP6GLBGGLXQ6MCH`](https://stellar.expert/explorer/public/account/GDHMJXMHWBX7YKIY7TZBWLETQR5K6KAXYRBME2FIBRP6GLBGGLXQ6MCH) | 94,000,000 | 20,000,000 | None | 12.5M |
| [`GC2VWS32ESUQJ5K2K5KQ7NUTCY4XHGVUHWTU7T5KH664PWWFZDERSSTA`](https://stellar.expert/explorer/public/account/GC2VWS32ESUQJ5K2K5KQ7NUTCY4XHGVUHWTU7T5KH664PWWFZDERSSTA) | 64,000,002 | 34,000,002 | None | 4.6M |
| [`GDQP2KPQ…`](https://stellar.expert/explorer/public/account/GDQP2KPQGKIHYJGXNUIYOMHARUARCA7DJT5FO2FFOOKY3B2WSQHG4W37), `GCIL6JNO…`, [`GC5PFAXP…`](https://stellar.expert/explorer/public/account/GC5PFAXPL3BYIRHLMUFD3E353DINA6A52DXJIXLKQEVO2GA7WFWGWCFS) | 80,272,000 combined | 1,453,727 | **Coinbase deposits** | ~0 |

Labels are [Tier B] Stellar Expert directory tags; balances and flows are [Tier A] Horizon.

**SDF's own spend accounting, Q3 2026** ([Tier A] Q3 report, "Lumens Utilized July – September 2026"): SDF Development 140,229,306 · Assets & Liquidity 50,930,231 · Growth 371,421,081 · Product & Innovation 106,063,328 → **668.6M XLM in one quarter** (~2.7B a year at that pace). Named uses include Kaiko, Nium, Ramp Network, Fireblocks, Securitize, MoneyGram, Paxos Trust, Spiko, Ondo Finance and Taurus. The SDF notes that "related XLM sales can exceed or trail spend".

**What it means:** The SDF sells steadily and says so. Its direct exchange deposits were *less* likely than average to land on a pump day (4.9% vs 10.6%), so the trace shows no sign of timing sales to pumps. It passes because the selling is disclosed and not pump-weighted. It is only a 6 because ~3.1B XLM went to unlabelled accounts whose final buyers are not published.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Real supply | 50,001,786,837 XLM (105.44B `total_coins` − 55.44B in the dead burn account) | [Tier A] Horizon ledger + account [`GALAXYVOIDAOPZTDLHILAJQKCVVFMD4IKLXLSZV5YHO7VY74IWZILUTO`](https://stellar.expert/explorer/public/account/GALAXYVOIDAOPZTDLHILAJQKCVVFMD4IKLXLSZV5YHO7VY74IWZILUTO) (master weight 0, thresholds 0) |
| Inflation | Off since 2019; no protocol minting | [Tier A] DefiLlama methodology · ledger (fee pool not paid out) |
| Max supply | None hard-coded (CoinGecko shows "no max"); in practice no new XLM is created | [Tier B] CoinGecko |
| Circulating | 35.41B (70.8%) | [Tier B] CoinGecko |
| New float | SDF deployment ~668.6M a quarter ≈ **2.7B a year ≈ 7.5% of circulating** | [Tier A] SDF Q3 report · calculated |
| Fee "burn" | 11.04M XLM in the fee pool (0.02% of supply) | [Tier A] ledger |
| Asset-level controls | Issued assets can carry freeze and clawback flags (used in the U.S. Bank USBDC pilot); this does not apply to XLM itself | [Tier A] SDF Q3 report |

**What it means:** No inflation and no mint key. The real dilution is the SDF's float, which adds about 7.5% of circulating supply a year. XRP, with a similar company or foundation float of ~5.7% a year, scored 5.

## 💧 Liquidity & market · 9/10 · ✅ PASS

| Venue | Pair | 24h volume | Cost to move price +2% / −2% |
|---|---|---:|---:|
| KuCoin | XLM/USDT | $103.8M | $139k / $183k |
| Coinbase Exchange | XLM/USD | $16.8M | $486k / $739k |
| Binance | XLM/USDT | $15.9M | $394k / $414k |
| Upbit | XLM/KRW | $13.8M | $622k / $671k |
| Kraken | XLM/USD | $9.1M | $371k / $477k |

- 100+ CEX tickers incl. Binance, Coinbase, Kraken, Bitstamp, Bitvavo, Bybit, OKX, Upbit, Bithumb ([Tier A] CoinGecko tickers API, 15 Nov 2026).
- On-ledger DeFi TVL $198.5M ([Tier A] DefiLlama chains, 15 Nov); SDF Q3 report: DeFi TVL $264M at quarter end.
- US futures-based ETFs: Volatility Shares STLR (1×) and STLU (2×), launched 1 Apr 2026 on Cboe, hold XLM futures, not spot ([Tier A] SEC 497K filing · issuer page). **No US spot XLM ETF** as of this pass.

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Mainnet runs **protocol 29** ([Tier A] ledger header). Core v30.0.0 ("Bell", Protocol 30) was released 16 Oct 2026. It adds muxed contract addresses (CAP-84), ML-DSA post-quantum signature verification in smart contracts (CAP-87) and millisecond close times (CAP-88) ([Tier A] SDF upgrade guide).
- Q3 2026: two protocol upgrades shipped, 3,922 monthly active developers on 30 Sep (Electric Capital, ranked #2), and 99.99% availability over 12 years ([Tier A] SDF Q3 report; developer counts are Electric Capital's).
- `stellar-core`: 135 commits in the last 13 weeks; 3,317 stars ([Tier A] GitHub API).

## 🤝 Adoption & customers · 7/10 · ✅ PASS

| Metric (Q3 2026) | Value | vs Q2 2026 | Source |
|---|---:|---:|---|
| Total volume | $33.2B | +71% | [Tier A] SDF Q3 report |
| Stablecoin transfer volume | $25.1B | +121% | [Tier A] |
| RWA market cap | $4.1B | +36% (+548% y/y) | [Tier A] |
| Stablecoin market cap | $496M | +42% | [Tier A] |
| Total transactions | 1.04B | −5% | [Tier A] |
| Stablecoins on Stellar today | $397.5M USD-pegged + $22.5M EUR-pegged | — | [Tier A] DefiLlama stablecoins, 15 Nov |

**Named users** ([Tier A] SDF Q3 report unless noted):
- **Confirmed (own channels):** U.S. Bank live pilot of its USBDC stablecoin (9 Sep 2026); USDT0 launch with ten partners; MoneyGram, Figure Markets and Range now run Tier 1 validators; Franklin Templeton BENJI (SDF case study).
- **RWA issuers:** Spiko raised its Stellar holdings to $1.7B (Q3 report). Realiz, Tradable, Franklin and Ondo at ~$535–559M each — [Unverified], one secondary outlet (Crypto Briefing via BSCN).
- **DTCC Tokenization Service "to connect with" Stellar:** SDF partner spotlight ([Tier A] stellar.org). Scope and live status are not confirmed by DTCC in this pass → [Unverified].

**What it means:** Real institutions settle real value here, so this is one of the stronger adoption cases among layer-1s. Fee revenue stays tiny because transactions cost about $0.0001.

## 🛡️ Security & audits · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Protocol hack | None found | [Tier A] SDF reports (absence) |
| Uptime | 99.99% over 12 years per SDF; a known ~1-hour halt in May 2019 | [Tier A] Q3 report · [Unverified] 2019 halt detail not re-read |
| Validator set | Tier 1 grew 7 → 10 in Q3 2026; no validator rewards, so operators are businesses that rely on the network | [Tier A] Q3 report |
| SDF key hygiene | 11 of 12 mandate accounts are multi-signer (threshold 3); **one 554M-XLM hot account is single-key** | [Tier A] Horizon |
| Upgrade risk | Protocol 30 changes the ledger header (CAP-88). Old decoders will break, so exchanges and indexers must upgrade before 23 Nov | [Tier A] upgrade guide |
| Soroban audits / bug bounty | Not re-read this pass | Not found — see Open items |

## ⚖️ Regulatory · 8/10 · ✅ PASS

- **US:** the SEC's 17 Mar 2026 interpretation (Release 33-11412, joined by the CFTC) names **Stellar (XLM)** as an example of a **digital commodity**, which is not a security ([Tier A] sec.gov).
- **EU:** a MiCA white paper for "Stellar Lumen" (DTI FFG `ZCN8SR2H7`) was notified to BaFin on 15 Jan 2026 by **Crypto Risk Metrics GmbH**, a third party, not the SDF, for 30 EEA states ([Tier A] ESMA interim register `OTHER.csv`, updated 11 Nov 2026). This is a notification, not an approval.
- No US spot ETF yet; futures ETFs only (see Liquidity).

## 📅 Catalysts & calendar · 6/10 · ✅ PASS

| Date | Event | Effect |
|---|---|---|
| **23 Nov 2026, 17:00 UTC (10:00 AM MST)** | Protocol 30 "Bell" mainnet upgrade vote | Product; integrators must upgrade SDKs |
| Ongoing, ~monthly | SDF deployment from mandate accounts (~220M XLM a month at the Q3 pace) | Supply ↑ |
| ~Jan 2027 | SDF Q4 2026 report (spend by mandate, wallet balances) | Disclosure |
| Open | Any US spot XLM ETF filing or approval | Demand (none filed and confirmed this pass) |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Hack / exploit | 🟢 None | — |
| Network halt | 🟢 None found in the series | SDF 99.99% availability |
| SDF exchange sends on pump days | 🟡 Watch (disclosed; 4.9% of exchange sends vs 10.6% base rate) | Selling section |
| SDF treasury account on a single key | 🔴 **Tripped** | [`GDWXQOTI…`](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) 554,096,554 XLM, 1 signer, thresholds 0 · [Horizon signers](https://horizon.stellar.org/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) |

## 📚 Sources

- [Tier A] Horizon ([`horizon.stellar.org`](https://horizon.stellar.org/)): `/ledgers` (ledger 65,492,889, 13:48:07 UTC), `/fee_stats`, `/accounts/{id}` for 12 SDF accounts + the 2019 burn account, `/accounts/{id}/payments` for all 12 SDF accounts (12 months) and 4 second-hop recipients; 15 Nov 2026 ~6:48–7:05 AM MST
- [Tier A] [SDF mandate page](https://stellar.org/foundation/mandate) (balances updated 11–14 Nov 2026) · [team](https://stellar.org/foundation/team) · [quarterly reports](https://stellar.org/quarterly-reports) — Q3 2026 "Quarter in Review" PDF
- [Tier A] [Bell, Protocol 30 upgrade guide](https://stellar.org/blog/developers/bell-protocol-30-upgrade-guide) (updated 23 Oct 2026)
- [Tier A] DefiLlama fees `stellar`, chains TVL, stablecoin chains; 15 Nov 2026
- [Tier A] CoinGecko `stellar` coin data, 365-day daily closes, tickers with depth; 15 Nov 2026 6:45 AM MST
- [Tier A] GitHub API `stellar/stellar-core` (releases, participation)
- [Tier A] SEC Release 33-11412 and the sec.gov crypto-asset taxonomy page · SEC 497K for STLU · ESMA interim MiCA register `OTHER.csv`
- [Tier B] [Stellar Expert](https://stellar.expert/explorer/public) directory labels (`sdf` tag, exchange tags); every account cited is linked inline and in the Evidence trail
- [Tier A] [Stellar.expert account pages](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) and [Horizon raw account JSON](https://horizon.stellar.org/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) for the single-key account; second-hop addresses resolved from Horizon `/payments`, 15 Nov 2026 MST
- [Tier B] Arkham, read 15 Nov 2026 ~11:05 AM MST (signed-in account): **Stellar is not supported** ([`GB4SJVA7…`](https://stellar.expert/explorer/public/account/GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5) returns "Something went wrong / Couldn't load portfolio"; [`GDZAI56J…`](https://stellar.expert/explorer/public/account/GDZAI56JE57EAUA46ZVUZ7VHROBDD7X3WF264XDQLWSFWRVJBNUV6ZHY) and [`GDDUETSY…`](https://stellar.expert/explorer/public/account/GDDUETSYDSHJMU5J73WHR4SQOAWRUM5SNLHXBQKM36EQ244GHSRS5AHF) not opened for the same reason). Open item #1 stays open
- [Unverified] SDF state registration; owners of [`GB4SJVA7…`](https://stellar.expert/explorer/public/account/GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5), [`GDZAI56J…`](https://stellar.expert/explorer/public/account/GDZAI56JE57EAUA46ZVUZ7VHROBDD7X3WF264XDQLWSFWRVJBNUV6ZHY), [`GDDUETSY…`](https://stellar.expert/explorer/public/account/GDDUETSYDSHJMU5J73WHR4SQOAWRUM5SNLHXBQKM36EQ244GHSRS5AHF), [`GAEPN735…`](https://stellar.expert/explorer/public/account/GAEPN735I2YWGIW6J4MXMEXLLPKEOV4ERNBVJTTZ7J3PHOSANHDHO3ZE) and their next hops; per-issuer RWA figures; DTCC connection scope; 2019 halt details

## 🔗 Evidence trail

*Strongest findings first. Each link opens the primary record (block explorer) or the label source (Arkham) for the claim, so any number can be checked by hand.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 🔴 554.1M XLM SDF hot account on 1 key, thresholds 0 | [Stellar.expert](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) · [Horizon account (signers, thresholds)](https://horizon.stellar.org/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ) · [set_options history](https://horizon.stellar.org/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ/operations?order=desc&limit=200) | A | 15 Nov 2026 ~6:48–7:05 AM MST |
| SDF → Bitstamp 159.1M XLM (12 mo) | [`GDBK3AHP…` Stellar.expert](https://stellar.expert/explorer/public/account/GDBK3AHPQ7AO2U7JYEBFGJ2PBDVVFANHH4NQANDX6Q4GZ266WZ3IOIXN) · [Horizon payments](https://horizon.stellar.org/accounts/GDBK3AHPQ7AO2U7JYEBFGJ2PBDVVFANHH4NQANDX6Q4GZ266WZ3IOIXN/payments?order=desc) | A flow / B label | 15 Nov 2026 ~6:48–7:05 AM MST |
| SDF → Kraken 108.5M XLM | [`GA5XIGA5…`](https://stellar.expert/explorer/public/account/GA5XIGA5C7QTPTWXQHY6MCJRMTRZDOSHR6EFIBNDQTCQHG262N4GGKTM) | A flow / B label | 15 Nov 2026 ~6:48–7:05 AM MST |
| SDF → Coinbase deposits 80.3M XLM | [`GDQP2KPQ…`](https://stellar.expert/explorer/public/account/GDQP2KPQGKIHYJGXNUIYOMHARUARCA7DJT5FO2FFOOKY3B2WSQHG4W37) · [`GC5PFAXP…`](https://stellar.expert/explorer/public/account/GC5PFAXPL3BYIRHLMUFD3E353DINA6A52DXJIXLKQEVO2GA7WFWGWCFS) · `GCIL6JNO…` (full address not in saved data) | A flow / B label | 15 Nov 2026 ~6:48–7:05 AM MST |
| Largest unlabelled SDF recipient 631M, forwards to `GC6S2SVX…` | [`GB4SJVA7…`](https://stellar.expert/explorer/public/account/GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5) → [`GC6S2SVX…`](https://stellar.expert/explorer/public/account/GC6S2SVXVMPECWS65YXIX72TF5YUYV2MFKLTINSS3XTWAGQWQAJDLIPM) · [Arkham check (Stellar unsupported)](https://intel.arkm.com/explorer/address/GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5) | A | 15 Nov 2026 ~11:05 AM MST |
| 514M recipient forwards to 3 accounts | [`GDZAI56J…`](https://stellar.expert/explorer/public/account/GDZAI56JE57EAUA46ZVUZ7VHROBDD7X3WF264XDQLWSFWRVJBNUV6ZHY) → [`GAKTGHDI…`](https://stellar.expert/explorer/public/account/GAKTGHDIAQK6ACNHXQMUN7X7P245KRNAKEBJ6A73T5RWCOYHEN6ZAULX), [`GAH3EBQH…`](https://stellar.expert/explorer/public/account/GAH3EBQHRYZMNGGAJTQJIC7VTNNUMUHKFJFTB3AWYV3T275Q7ALT437S), [`GDSKF3UL…`](https://stellar.expert/explorer/public/account/GDSKF3ULSQJSIVAZMFQOW6HEDJBWN2NIHFOTXA45JWKRCGM5ADD7AY52) | A | 15 Nov 2026 ~6:48–7:05 AM MST |
| 495M recipient forwards 495.8M | [`GDDUETSY…`](https://stellar.expert/explorer/public/account/GDDUETSYDSHJMU5J73WHR4SQOAWRUM5SNLHXBQKM36EQ244GHSRS5AHF) → [`GCA34HBK…`](https://stellar.expert/explorer/public/account/GCA34HBKNLWN3AOXWBRW5Y3HSGHCWF3UDBRJ5YHGU6HWGJZEPO2NSXI3) | A | 15 Nov 2026 ~6:48–7:05 AM MST |
| 185M operating wallet (116M back to SDF, 20M to Coinbase) | [`GAEPN735…`](https://stellar.expert/explorer/public/account/GAEPN735I2YWGIW6J4MXMEXLLPKEOV4ERNBVJTTZ7J3PHOSANHDHO3ZE) | A | 15 Nov 2026 ~6:48–7:05 AM MST |
| Real supply 50.0B (55.44B in dead burn account) | [Burn account](https://stellar.expert/explorer/public/account/GALAXYVOIDAOPZTDLHILAJQKCVVFMD4IKLXLSZV5YHO7VY74IWZILUTO) · [Horizon ledgers](https://horizon.stellar.org/ledgers?order=desc&limit=1) | A | 15 Nov 2026 ~6:48–7:05 AM MST |
| 12 SDF mandate accounts and balances | [SDF mandate page](https://stellar.org/foundation/mandate) · each account linked in the holdings table | A | 15 Nov 2026 ~6:48–7:05 AM MST |
| 668.6M XLM spent in Q3 2026 | [SDF quarterly reports](https://stellar.org/quarterly-reports) | A | 15 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exact path to close it | Cost / access |
|---|---|---|---|
| 1 | Who is behind the four large unlabelled SDF recipients ([`GB4SJVA7…`](https://stellar.expert/explorer/public/account/GB4SJVA7KAFDZJFVTSEV2YWZZA3VEANHHK3WSJRHO2XS2GDYJCGWKDB5) 631M, [`GDZAI56J…`](https://stellar.expert/explorer/public/account/GDZAI56JE57EAUA46ZVUZ7VHROBDD7X3WF264XDQLWSFWRVJBNUV6ZHY) 514M, [`GDDUETSY…`](https://stellar.expert/explorer/public/account/GDDUETSYDSHJMU5J73WHR4SQOAWRUM5SNLHXBQKM36EQ244GHSRS5AHF) 495M, [`GAEPN735…`](https://stellar.expert/explorer/public/account/GAEPN735I2YWGIW6J4MXMEXLLPKEOV4ERNBVJTTZ7J3PHOSANHDHO3ZE) 185M) and whether they sold on exchanges | **Arkham checked 15 Nov 2026: Stellar not supported, so path (c) via Arkham is closed; stays open via (a)/(b).** (a) Ask the SDF to label them (they publish wallet names on Stellar Expert, `stellar.expert/directory?tag[]=sdf`); (b) trace 2–3 more hops on Horizon `/accounts/{id}/payments` until a Stellar Expert `exchange` tag appears; (c) Arkham or Nansen entity labels | (a) free, request to SDF (partnerships/press contact on stellar.org) · (b) free, script · (c) paid plan |
| 2 | Real end buyers of the ~3.1B XLM that went to unlabelled accounts | Same as #1, plus the SDF's quarterly "Lumens Utilized" tables (named counterparties) matched to transfer dates | Free; time-heavy |
| 3 | Why the Q3 report and the mandate page name the 4.05B "Growth" wallet differently (Growth 1 vs Growth 3) | Compare the Q3 PDF wallet table with Stellar Expert's `sdf` tag list; ask the SDF | Free |
| 4 | Why a 554M-XLM SDF hot account ([`GDWXQOTI…`](https://stellar.expert/explorer/public/account/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ)) runs on one key | Horizon `/accounts/GDWXQOTIIDO2EUK4DIGIBLEHLME2IAJRNU6JDFS5B2ZTND65P7J36WQZ` (signer history via `/operations?type=set_options`); ask the SDF whether it is HSM- or custodian-held | Free |
| 5 | SDF's legal registration (state and file number) | Delaware Division of Corporations entity search (icis.corp.delaware.gov) for "Stellar Development Foundation"; IRS Form 990 search if it files as exempt (it says it is "not a charity" and pays taxes, so it may not) | Free (captcha) |
| 6 | Soroban audit list and bug-bounty payouts | `developers.stellar.org` security/audit pages; SDF Audit Bank announcements; Immunefi or HackerOne program page | Free |
| 7 | Per-issuer RWA figures (Realiz, Tradable, Franklin, Ondo ~$535–559M each) | rwa.xyz Stellar network page, or each issuer's Stellar asset on Horizon `/assets?asset_code=…&asset_issuer=…` (supply × NAV) | rwa.xyz free tier; Horizon free |
| 8 | DTCC Tokenization Service connection to Stellar: scope and live date | DTCC press room (dtcc.com/news) for a matching release; SDF case study page | Free |
| 9 | May 2019 network halt details | SDF blog post-mortem (stellar.org/blog) for 15 May 2019 | Free |
| 10 | Whether any US spot XLM ETF S-1 or 19b-4 is on file | SEC EDGAR full-text search for "Stellar" + "S-1"; Federal Register for 19b-4 notices | Free |

**Unverified items: 10**

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
