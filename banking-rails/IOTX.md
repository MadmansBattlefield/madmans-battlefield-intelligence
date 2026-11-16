---
ticker: IOTX
name: IoTeX
chain: iotex
contract: "0x6fb3e0a217407efff7ca062d46c26e5d60a14d69"
overall_score: 3.7
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 4
  selling_behavior: 4
  tokenomics_supply: 5
  liquidity_market: 4
  product_development: 6
  adoption_customers: 3
  security_audits: 2
  regulatory: 5
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes: ioTube bridge exploit on 21 Feb 2026 (compromised validator-owner key; ~$4.4M of reserves drained, 410M CIOTX minted)"
  mint_path_live: "yes, by design (staking rewards mint IOTX; IIP-62 proposes a new 'productive inflation' curve)"
  team_wallet_to_exchange_during_pump: "yes, old: a founder-linked legacy ERC20 wallet sent 10M IOTX to a Coinbase deposit on 18 Jan 2022 (+15.4% over 5 days); no ERC20 sends since 2022; native chain not tested"
  one_hop_sale_status: not_proven
  treasury_in_single_key_wallets: "not found (Foundation treasury wallets are not published); the 2026 bridge hack came from a single compromised owner key"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees are about $28k a year and nothing reaches holders."
pump_day_price_source: "Gate IOTX/USDT daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions:
  - address: "0x2444919721b0b1abef3a21adeb504179ee67888f"
    label: "Founder-linked (unlabelled)"
    confidence: low
    independent_corroboration: false
    basis: "Transfer history only"
price_usd: 0.00241397
price_source: "CoinGecko, 16 Nov 2026 8:20 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### IOTX · Overall grade **3.7 / 10 · ❌ FAIL**

**Summary:** IoTeX is a Layer 1 for devices and AI agents, live since 2019 and still shipping (the Zanzibar hard fork in Oct 2026, post-quantum proposals IIP-64/65, a 1:1 ERC20-to-native redemption portal). But the chain earns almost nothing: **$28k of fees in a year and $0 of protocol revenue** on DefiLlama, with only **$1.3M of DeFi TVL**. In **Feb 2026 the ioTube bridge was drained of ~$4.4M** through one compromised key. Staking is paid with newly minted IOTX. The price is down **99.1% from ATH and 76% in a year**. Revenue trips the hard gate.

**🚨 Top warning:** security and usage. On 21 Feb 2026 an attacker who had compromised an employee's machine took over the Ethereum-side ioTube Validator contract, drained ~$4.4M of reserves and minted 410M CIOTX. IoTeX confirmed it in its own [incident report](https://iotex.io/blog/security-incident-update-iotube-bridge-exploit-and-recovery-roadmap/), and [CoinDesk](https://www.coindesk.com/business/2026/02/23/iotex-bridge-exploit-sparks-debate-over-losses-and-recovery-prospects) and [The Block](https://www.theblock.co/news/ecosystems/2026-02-21-iotex-hit-by-private-key-exploit-draining-up-to-8-8-million-from-bridge-contracts-390698) reported it too. The chain had to be halted and patched to freeze ~45M IOTX in attacker wallets. Meanwhile, the whole chain produced [$28k of fees in 12 months](https://api.llama.fi/summary/fees/iotex?dataType=dailyFees).

**Sections passed: 1 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 4/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 5/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 2/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 IOTX · IoTeX · 3.7 / 10 · ❌ FAIL

> **One line:** A long-lived device-and-AI Layer 1 that keeps shipping, but has almost no fee income, a 2026 bridge hack, and inflation-paid staking.

| 📊 Market (CoinGecko, 16 Nov 2026 8:20 AM MST) | 🔗 On-chain (IoTeX + Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.00241397 | **Circulating** 9,441,368,550 IOTX of a 10B max (CoinGecko) |
| **24h / 7d / 30d** 🔴 −1.9% / −19.2% / −36.5% · 1y −76.2% | **Chain TVL** $1.29M ([DefiLlama chains](https://api.llama.fi/v2/chains)) |
| **Market cap** $22.79M · **FDV** $22.79M | **Fees, 12 months** $28,421 · revenue $0 ([DefiLlama](https://api.llama.fi/summary/fees/iotex?dataType=dailyFees)) |
| **24h volume** $814k (Binance, Upbit, Bithumb, WhiteBIT, MEXC) | **Legacy ERC20** [`0x6fB3…4d69`](https://etherscan.io/token/0x6fb3e0a217407efff7ca062d46c26e5d60a14d69): 6.75B sent to null addresses in 2020; 24,831 holders (Blockscout) |
| **ATH** $0.2556 (13 Nov 2021) · now −99.1% | **Redemption** ERC20 → native 1:1 since 12 Oct 2026 |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees, last 12 months | **$28,421** ($199 in the last 30 days) | [Tier A] [DefiLlama fees](https://api.llama.fi/summary/fees/iotex?dataType=dailyFees) |
| Protocol revenue | **$0** | [Tier A] [DefiLlama revenue](https://api.llama.fi/summary/fees/iotex?dataType=dailyRevenue) |
| Burns | Burn-Drop has burned ~400M IOTX since 2020 against device registrations; gas burn and ioID burns are planned under IoTeX 2.0 | [Tier A] [IoTeX docs](https://iotex.gitbook.io/new-docs/readme/tokenomics/iotx-emission-deflation-and-re-staking) |
| Staker income | Newly minted IOTX | [Tier A] [IoTeX docs](https://iotex.gitbook.io/new-docs/readme/tokenomics/iotx-emission-deflation-and-re-staking) |

**What it means:** $28k a year of fees against a $22.8M market cap is effectively no business. **2, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees are about $28k a year and nothing reaches holders.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Organisation | IoTeX Foundation plus a core team; mainnet since Apr 2019 (54M+ blocks) | [Tier A] [IoTeX blog, 11 Nov 2026](https://iotex.io/blog/five-doors-six-months-of-iotex/) |
| Governance | IIP proposals voted by stakers (IIP-59 passed Aug 2026; IIP-64/65 under review). The Marshall DAO funds ecosystem grants from 500M+ IOTX repurposed from Burn-Drop in Q1 2024 | [Tier A] [IoTeX docs](https://iotex.gitbook.io/new-docs/readme/tokenomics/iotx-emission-deflation-and-re-staking) |
| Disclosure | Detailed public incident reports for the bridge hack; no treasury report or Foundation wallet list | [Tier A] [incident review](https://iotex.io/blog/how-iotex-responded-to-the-iotube-bridge-incident-a-full-month-in-review/) |
| Ops security | The hack started with a social-engineered employee machine | [Tier A] same |

## 🪙 Foundation / team holdings — How many coins do they hold? · 4/10 · ❌ FAIL

| Holder | IOTX | Notes |
|---|---:|---|
| Foundation treasury (native chain) | **Not found** | IoTeX publishes no wallet list. It promised to pay hack compensation from the "Foundation Treasury" [Tier A] |
| Marshall DAO | 500M+ | Ecosystem incentives, voted Q1 2024 [Tier A docs] |
| Null addresses `0x…01` to `0x…07` (ERC20) | 6.75B | ERC20 supply sent away in Jan–Mar 2020 (e.g. [148M](https://etherscan.io/tx/0x845e494c4b41956cc8d5fe33f4cc40094a71b82ab81e0c1e5de404627c25530f), [600M](https://etherscan.io/tx/0xcf150e4ee4eeca87e2c0fefb1ccb4159c5e2f48a872cc19b6c8c9f68a8f7d63c)) when holders moved to the native chain; unspendable |
| Legacy "Staking" contract [`0x87C9…9193`](https://etherscan.io/address/0x87c9dbff0016af23f5b1ab9b8e072124ab729193) | 1.97B ERC20 | Dormant since Jun 2020. Arkham: verified contract "Staking", no controlling entity shown |
| **Coinbase custody, not insiders** | 539.5M | Arkham labels [`0x4761…f659`](https://intel.arkm.com/explorer/address/0x4761571eeec2fee2fb9f8d5c08ef7c7606a9f659) (152.5M), [`0x58Bc…4348`](https://intel.arkm.com/explorer/address/0x58bc01f516c8d6986bc0fd67944f2718c2a94348) (149.5M) and [`0xCbE6…510A`](https://intel.arkm.com/explorer/address/0xcbe6523edbfa82f376ee842794128dbf9141510a) (143.1M) **Coinbase: Cold Wallet**, filled from the Coinbase hot wallet, and [`0xc59b…4ea0`](https://intel.arkm.com/explorer/address/0xc59b962be5118a2680cda9d730e5a23a257f4ea0) (94.4M) **Coinbase Prime Custody** |
| Founder-linked legacy wallet [`0x2444…888f`](https://intel.arkm.com/explorer/address/0x2444919721b0b1abef3a21adeb504179ee67888f) | 50M ERC20 | Unlabelled; swapped IOTX back and forth with an individual-labelled ENS wallet in 2019–20 and was topped up by `0x9631` (400M, 9 Nov 2019); last move Aug 2020 [Tier A Etherscan + Tier B Arkham] |
| Unlabelled whale [`0x74a0…b1e0`](https://intel.arkm.com/explorer/address/0x74a09fbf55ed0c31ba5fa3dd78f93e9f3403b1e0) | 169.3M ERC20 | Carries an individual's ENS name on Arkham (not given here); trades other tokens through Uniswap like a bot. Not linked to IoTeX by any label [Unverified] |

**What it means:** The three large ERC20 holders that looked like possible insiders are Coinbase cold storage and Coinbase Prime custody ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)), so they are exchange and client custody, not Foundation stock. That removes a worry but adds no disclosure: the tokens that matter live on the native chain, and the Foundation's share there is still not disclosed. **4** (unchanged).

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Gate IOTX/USDT daily closes (UTC): 30 of the last 365 days were pump days.*

- The two ERC20 wallets that sent the supply to null addresses ([`0x5606…b937`](https://etherscan.io/address/0x56061a93eabbe3ffa94dc817bd0a30cd736fb937), [`0x9631…5660`](https://etherscan.io/address/0x9631ea18e14b3629caf46b141ab215db51465660)) are empty. Arkham shows both were first funded by an individual-labelled ENS wallet, and `0x9631` made the 600M–1B migration burns. **Correction:** `0x5606`'s last moves were not in Jan 2022. After the 2020 migration ([148M burn, 9 Mar 2020](https://etherscan.io/tx/0x845e494c4b41956cc8d5fe33f4cc40094a71b82ab81e0c1e5de404627c25530f)) it received 50.25M IOTX (10 Jul 2020) and sent it out in 2021–22:

| Day (UTC) | To | IOTX | 5-day change (Gate) | Pump? |
|---|---|---:|---:|---|
| 29 Nov 2021 | unlabelled `0x17de…` ([tx](https://etherscan.io/tx/0xc4cc4f237a498b2df62b125351e4a23f29c5b9c40113637c0cf53049ac562237)) | 10,000,000 | −11.5% | No |
| 17 Jan 2022 | unlabelled `0x25b5…` ([tx](https://etherscan.io/tx/0xd66762f141aa2cd4a53a0026be9995e49d1c5b8de2e3d6fdc1f6f5a0a67a93b7)) | 20,000,000 | +2.1% | No |
| **18 Jan 2022** | **Coinbase Deposit** `0xf8d4…` ([tx](https://etherscan.io/tx/0xd7ddcb685b214df98e5761161a22508508fd135f2d2784b7d275bdd16b996253)) | **10,000,000** (~$1.16M) | **+15.4%** | **Yes** |
| 23 Aug 2022 | **Gemini Deposit** `0x6b06…` ([tx](https://etherscan.io/tx/0xa92dea3a5bd491b3dfaed23d307d8aae9181ea8e069a3726357aa732d4b88867)) | 5,000,000 | −5.6% | No |
| 24 Aug 2022 | **Jump Crypto** `0x4f20…` ([tx](https://etherscan.io/tx/0x3d5161890f6a7eaf128a3a31ef3059af92178b86b457fd4a2258a87c1b684402)), a market maker | 5,000,000 | +1.2% | No |
| 30 Dec 2022 | the individual-labelled ENS wallet ([tx](https://etherscan.io/tx/0xae96ca9effbe1cc1aa86d5a58b97873e0022a23b640b9a626d40cf5cd2307de2)) | 173,016 | — | — |

  Exchange and market-maker labels are Arkham's ([`0x5606` on Arkham](https://intel.arkm.com/explorer/address/0x56061a93eabbe3ffa94dc817bd0a30cd736fb937)); dates and amounts are from Etherscan. No disclosure of these transfers was found. They are four years old and the 2024–2026 ERC20 record shows no exchange sends.
- **Native IoTeX chain wallets were not tested.** The Foundation's native addresses are not published, and Etherscan-style tools do not index the IoTeX L1.

**What it means:** A founder-linked team wallet sent 10M IOTX to a Coinbase deposit on a pump day (18 Jan 2022) and another 10M to Gemini and Jump Crypto later in 2022, with no disclosure found. It is old and small next to supply, and the native chain is still untested, so **4** (was 5): proven but small and dated, above the gate.

- **Penalty check (16 Nov 2026 rules):** not applied. **Disclosure quality:** not applicable; no team selling into a pump is proven. Pump days from Gate IOTX/USDT daily closes.

## 📊 Tokenomics & supply · 5/10 · ❌ FAIL

- 9.44B of 10B max is circulating (CoinGecko). The original staking-reward pool is "nearly exhausted", so IoTeX 2.0 moved to **inflationary staking rewards** set by governance ([docs](https://iotex.gitbook.io/new-docs/readme/tokenomics/iotx-emission-deflation-and-re-staking)). The exact current rate was not found [Unverified].
- IIP-62 proposes a new "productive inflation" curve with an 80/20 split between stakers and a DAO ([iotex-core PR](https://github.com/iotexproject/iotex-core/pull/4846)). It is not live yet.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $814k of 24h volume on a $22.8M cap (3.6% turnover), listed on Binance, Upbit, Bithumb, Kraken and Revolut.
- −99.1% from ATH, −76% in a year, −36% in 30 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- Zanzibar hard fork (19 Oct 2026, IIP-59: staking rewards fully on-chain), ERC20 redemption portal (12 Oct 2026), post-quantum IIP-64/65 drafts with reference code ([IoTeX blog](https://iotex.io/blog/five-doors-six-months-of-iotex/); [TokenPost](https://www.tokenpost.com/news/technology/34627)).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- $1.29M chain TVL and $199 of fees in the last 30 days (DefiLlama). Burn-Drop shows ~26k registered devices ([burndrop.iotex.io](https://burndrop.iotex.io/)) [Tier A, single source].

## 🛡️ Security & audits · 2/10 · ❌ FAIL

- **ioTube exploit, 21 Feb 2026:** a compromised Validator-owner key let the attacker upgrade the contract, drain ~$4.4M (converted to ~66.8 BTC) and mint 410M CIOTX. IoTeX halted the chain and froze ~45M IOTX with a patch ([incident report](https://iotex.io/blog/security-incident-update-iotube-bridge-exploit-and-recovery-roadmap/) · [update 2](https://iotex.io/blog/iotube-bridge-incident-update-no-2-chain-resumed-recovery-underway/) · [CoinDesk](https://www.coindesk.com/business/2026/02/23/iotex-bridge-exploit-sparks-debate-over-losses-and-recovery-prospects)).
- Being able to halt the chain and blacklist addresses shows how centralised control is.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- No enforcement action found. The hack was reported to the FBI [Tier A IoTeX].

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event |
|---|---|
| TBA | IIP-62 inflation curve, IIP-64/65 post-quantum votes |
| Ongoing | ERC20 → native redemption; hack-compensation payouts from the Foundation treasury |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 ioTube bridge, 21 Feb 2026, ~$4.4M |
| Team wallet → exchange during a pump | 🔴 Old: 10M IOTX from founder-linked `0x5606` to a Coinbase deposit on 18 Jan 2022 ([tx](https://etherscan.io/tx/0xd7ddcb685b214df98e5761161a22508508fd135f2d2784b7d275bdd16b996253)); none on ERC20 since 2022; native chain not tested |
| Live mint path | 🔴 Inflationary staking rewards |
| Treasury in single-key wallets | 🟡 Unknown; the bridge hack came from one owner key |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x2444…888f`](https://intel.arkm.com/explorer/address/0x2444919721b0b1abef3a21adeb504179ee67888f) | Founder-linked (unlabelled) | Transfer history only | low | no | None: the 18 Jan 2022 pump-day Coinbase deposit cannot move Selling under the attribution rule; Selling stays 4 as "not proven" |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` for the legacy ERC20 wallets, read 16 Nov 2026 ~8:50 AM MST; Blockscout holders and token counters
- [Tier A] DefiLlama `iotex` fees and revenue; DefiLlama chains TVL
- [Tier A] [IoTeX incident report](https://iotex.io/blog/security-incident-update-iotube-bridge-exploit-and-recovery-roadmap/) · [Update 2](https://iotex.io/blog/iotube-bridge-incident-update-no-2-chain-resumed-recovery-underway/) · [Month review](https://iotex.io/blog/how-iotex-responded-to-the-iotube-bridge-incident-a-full-month-in-review/) · [Six months of IoTeX](https://iotex.io/blog/five-doors-six-months-of-iotex/) · [Tokenomics docs](https://iotex.gitbook.io/new-docs/readme/tokenomics/iotx-emission-deflation-and-re-staking)
- [Tier B] [CoinDesk](https://www.coindesk.com/business/2026/02/23/iotex-bridge-exploit-sparks-debate-over-losses-and-recovery-prospects) · [The Block](https://www.theblock.co/news/ecosystems/2026-02-21-iotex-hit-by-private-key-exploit-draining-up-to-8-8-million-from-bridge-contracts-390698) · [TokenPost (Zanzibar)](https://www.tokenpost.com/news/technology/34627) · [TokenPost (redemption)](https://www.tokenpost.com/news/technology/30766)
- [Tier A] CoinGecko `iotex` (16 Nov 2026 8:20 AM MST); Gate IOTX/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Coinbase Cold Wallet and Coinbase Prime Custody labels; exchange, market-maker and first-funder labels on `0x5606`, `0x9631`, `0x2444` (links in Holdings and Selling)
- [Tier A] Etherscan v2 API `tokentx` for `0x5606` and `0x2444`; Gate IOTX/USDT daily closes for Nov 2021 – Aug 2022
- [Unverified] Current inflation rate; Foundation native wallets and their exchange flows; owner of `0x74a0`

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| ioTube hack, ~$4.4M, 410M CIOTX | [IoTeX report](https://iotex.io/blog/security-incident-update-iotube-bridge-exploit-and-recovery-roadmap/) · [CoinDesk](https://www.coindesk.com/business/2026/02/23/iotex-bridge-exploit-sparks-debate-over-losses-and-recovery-prospects) | A + B | 16 Nov 2026 |
| $28k fees, $0 revenue in 12 months | [fees](https://api.llama.fi/summary/fees/iotex?dataType=dailyFees) · [revenue](https://api.llama.fi/summary/fees/iotex?dataType=dailyRevenue) | A | 16 Nov 2026 |
| Founder-linked `0x5606` → Coinbase Deposit on a pump day | [10M, 18 Jan 2022](https://etherscan.io/tx/0xd7ddcb685b214df98e5761161a22508508fd135f2d2784b7d275bdd16b996253) · [Arkham labels](https://intel.arkm.com/explorer/address/0x56061a93eabbe3ffa94dc817bd0a30cd736fb937) | A + B | 16 Nov 2026 |
| ERC20 "insider" wallets are Coinbase custody | [`0x4761`](https://intel.arkm.com/explorer/address/0x4761571eeec2fee2fb9f8d5c08ef7c7606a9f659) · [`0x58bc`](https://intel.arkm.com/explorer/address/0x58bc01f516c8d6986bc0fd67944f2718c2a94348) · [`0xcbe6`](https://intel.arkm.com/explorer/address/0xcbe6523edbfa82f376ee842794128dbf9141510a) · [`0xc59b`](https://intel.arkm.com/explorer/address/0xc59b962be5118a2680cda9d730e5a23a257f4ea0) | B | 16 Nov 2026 |
| ERC20 sent to null addresses in 2020 | [148M, 9 Mar 2020](https://etherscan.io/tx/0x845e494c4b41956cc8d5fe33f4cc40094a71b82ab81e0c1e5de404627c25530f) · [600M, 9 Mar 2020](https://etherscan.io/tx/0xcf150e4ee4eeca87e2c0fefb1ccb4159c5e2f48a872cc19b6c8c9f68a8f7d63c) | A | 16 Nov 2026 |
| Inflationary staking rewards; Marshall DAO 500M+ | [docs](https://iotex.gitbook.io/new-docs/readme/tokenomics/iotx-emission-deflation-and-re-staking) | A | 16 Nov 2026 |
| Zanzibar fork and redemption portal | [IoTeX blog](https://iotex.io/blog/five-doors-six-months-of-iotex/) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who received 30M from `0x5606` in 2021–22, and who controls `0x2444` and `0x74a0`** | Arkham (16 Nov 2026) leaves `0x17de…`, `0x25b5…`, `0x2444` and `0x74a0` without an entity label. Ask IoTeX whether the 2022 Coinbase and Gemini sends were Foundation sales [Unverified] | Free |
| 2 | **Foundation native wallets and their exchange flows** | Ask IoTeX for the Foundation and Marshall DAO addresses, then pull their transfers from iotexscan and pump-test them | Free |
| 3 | **Current inflation rate** | Read the rewarding protocol parameters from an IoTeX node, or IoTeX's staking dashboard | Free |
| 4 | **Hack compensation and recovery** | Follow IoTeX's post-mortem and the Binance freeze outcome | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
