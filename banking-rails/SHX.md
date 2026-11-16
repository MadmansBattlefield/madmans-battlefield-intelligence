---
ticker: SHX
name: Stronghold
chain: stellar
contract: "SHX-GDSTRSHXHGJ7ZIVRBXEYE5Q74XUVCUSEKEBR7UCHEUUEK72N7I7KJ6JH (Stellar); 0x516d31321928700c6b4fb0db0c8c6bc5d6799787 (Ethereum)"
overall_score: 3.6
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 4
  adoption_customers: 3
  security_audits: 6
  regulatory: 6
  catalysts: 4
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "no new minting (fixed 100B), but 60B company SHX sits in a rolling escrow that releases 1B a month"
  team_wallet_to_exchange_during_pump: "not proven: 875M SHX was bridged from Stellar into four Kraken deposit addresses in Jan-Nov 2026, none on a pump day; one 28.1M Kraken deposit on the 28 Sep 2026 pump day came via an unlabelled wallet fed by a 15.3B-SHX Stellar account whose owner is unpublished [Unverified]"
  entity_concentration: "yes: ~81% of supply is held by Stronghold (60B escrow plus other company balances)"
price_usd: 0.003893
price_source: "CoinGecko, 16 Nov 2026 ~9:30 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### SHX · Overall grade **3.6 / 10 · ❌ FAIL**

**Summary:** SHx is Stronghold's token on Stellar, with an Ethereum copy. It is used for merchant rewards and liquidity in Stronghold's payments network. The company created all 100B tokens, airdropped about 5% in 2018, and still holds roughly four-fifths. Since 2025, 60B of that sits in a code-enforced escrow that releases 1B a month, and any unused tokens are re-locked for five years. Token holders get no revenue. Trading is thin and spiky, with 46 pump days in the year. The revenue gate fails.

**🚨 Top warning:** **supply overhang.** About 18.8B SHx circulates, and Stronghold controls most of the other ~81B. The escrow can release **1B a month**, about 5% of today's float, to the company. Stronghold says unused amounts are re-locked, but its promised public dashboard tracking how much is actually used wasn't found ([escrow announcement](https://stronghold.co/learn/stronghold-locks-60-billion-shx-escrow)). Every link is in the 🔗 Evidence trail below.

**🔎 Exchange-deposit finding (Arkham + Etherscan, 16 Nov 2026):** four addresses first suspected to be Stronghold treasury wallets are **Kraken deposit addresses** ([0x2a90](https://intel.arkm.com/explorer/address/0x2a906e2aed080e3e85ef04d2b72765e21039bf67), [0xe84c](https://intel.arkm.com/explorer/address/0xe84ce212001f7c0eb70ac98278d17c70d4918bae), [0x5086](https://intel.arkm.com/explorer/address/0x50861fe4fc61c2137387ff7cf47c41fa8ef87b18), [0x63dc](https://intel.arkm.com/explorer/address/0x63dc28d45ef5536c03a238ae01bda5a4f0b79504)). Between 14 Jan and 6 Nov 2026 they received **875M SHX** in ten lumps of 25–200M and forwarded each to the [Kraken Hot Wallet 0xf213](https://intel.arkm.com/explorer/address/0xf213ac78ca8ff79f54eab193836053eea163f190) within minutes. 800M of it arrived as Axelar bridge mints from five Stellar accounts, and 75M via the unlabelled wallet `0x28c4`. **These are bridge deliveries of existing Stellar SHX, not new supply**, and none fell on a pump day (Kraken closes −14.0% to +6.3%). Separately, `0x28c4`, which is funded mostly by a Stellar account holding **15.3B SHX**, sent [28.1M SHX (~$146k) to a Kraken deposit on the 28 Sep 2026 pump day (+44.7%)](https://etherscan.io/tx/0x15b838a61a6af1fd79e93f7007a77cffa534693763e78d14eac4c97578bec298). The Stellar senders carry no public label, so whether this is Stronghold supply is [Unverified]. Selling stays **not proven (4)**; if they are shown to be Stronghold's, Selling becomes 3, the gate fails, and the overall drops to 3.5.

**Sections passed: 2 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 SHX · Stronghold · 3.6 / 10 · ❌ FAIL

> **One line:** A company-held payments token with 81% insider supply, a monthly 1B escrow release and no revenue share.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:30 AM MST) | 🔗 Chain (Stronghold, Horizon, Etherscan) |
|---|---|
| **Price** $0.003893 | **Supply** 18.8B circulating · 99.75B total · 100B max |
| **24h / 7d / 30d** 🟢 +1.1% / 🔴 −8.9% / 🔴 −35.5% | **Escrow** 60B in 60 × 1B Soroban accounts, one expiring monthly |
| **Market cap** $73.2M · **FDV** $388M | **Distribution** ~5% airdrop (2018), no ICO |
| **24h volume** $0.69M (Gate $0.19M, Kraken USD $0.15M, StellarTerm, MEXC, Kraken EUR, Aquarius) | **Ethereum copy** (Axelar Interchain Token) top holders: upgrade contract 419M, Uniswap V4 308M, Kraken hot wallet 0xf213 287M |
| **ATH** $0.0557 (16 May 2021) · now −93% | |
| **Pump days** 46 in the last year (Kraken SHXUSD; largest +90.8% on 1 Oct 2026) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- Stronghold earns from payments and merchant financing, but no fee goes to SHx holders through a burn, buyback or share. SHx is spent as rewards. **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

- An operating US payments company with a MiCA white paper and a public executive team. How the company is doing financially isn't disclosed.

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- The company holds about 81% of supply. 60B is in a public, code-enforced escrow ([announcement](https://stronghold.co/learn/stronghold-locks-60-billion-shx-escrow)), which is good for transparency but is still company supply.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- Company distribution wallets aren't published. Stellar's issuer account only receives tokens back.
- **Correction:** `0xf213…f190` is not a trading desk. Arkham labels it [Kraken: Hot Wallet](https://intel.arkm.com/explorer/address/0xf213ac78ca8ff79f54eab193836053eea163f190) ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)). The four wallets that sent it 100–200M lumps are **Kraken deposit addresses**, and so is [0x504c](https://intel.arkm.com/explorer/address/0x504ce9e51e508c85a161058c12e970a903d482fc) (80.0M).
- **How SHX reached those Kraken deposits (Etherscan, every transfer of 1M+):** Ethereum SHX is an Axelar Interchain Token, so a "mint from the null address" is a bridge delivery of SHX locked on Stellar. Source accounts are decoded from the Axelar messages.

| Date (UTC) | Kraken deposit | SHX | Arrived from | Kraken close vs 5 days earlier | Tx |
|---|---|---:|---|---:|---|
| 14 Jan 2026 | 0x5086 | 100M | Stellar `GB5P…TDICQF` (bridge) | +0.7% | [0x8ee7…](https://etherscan.io/tx/0x8ee7f1f8e2ed9afecb323047e1102973abcd77c28d9985e1df0ae57108c730b3) |
| 16 Jan 2026 | 0x2a90 | 100M | Stellar `GB5P…TDICQF` | +0.8% | [0x01af…](https://etherscan.io/tx/0x01af9cd7a6ebc35bb28a147c1a809094283b5594d03ac9398f187674368914f3) |
| 13 Mar 2026 | 0x63dc | 100M | Stellar `GA73…C3K6F5Z` | +2.7% | [0xb9fa…](https://etherscan.io/tx/0xb9faaa7e08e063fca6ba19e2520e7693b7394d2ce615535473489c916acf07c9) |
| 19 Mar 2026 | 0x2a90 | 100M | Stellar `GA73…C3K6F5Z` | +3.4% | [0xa326…](https://etherscan.io/tx/0xa32654d6e3f3be69eec3a058e6b2014f1d3495554f29f610b9f580eec6278e5c) |
| 20 Mar 2026 | 0xe84c | 200M | Stellar `GAKL…DPIWQFU` | +0.2% | [0x41f5…](https://etherscan.io/tx/0x41f5f8f9ee6fd272afc204dd20cffb4001342585f11f37e5c81762b9a21e4f33) |
| 4 Jun 2026 | 0x2a90 | 50M | Stellar `GAXG…AU2HRVM` | −14.0% | [0x446c…](https://etherscan.io/tx/0x446cbff2991d77db097547773dffd565d5c11b94bda0bbc01dc4e0dbc3101df6) |
| 2 Jul 2026 | 0x2a90 | 100M | Stellar `GC6Z…FNLANIY` | +3.0% | [0x2c2b…](https://etherscan.io/tx/0x2c2bc239f85e08badb72cecf6684b4366f14128aadd3a69f7156f299f4c24669) |
| 4 Sep 2026 | 0x2a90 | 50M | Stellar `GAXG…AU2HRVM` | +5.3% | [0xffb6…](https://etherscan.io/tx/0xffb6ed5d43b4b16ab95092146bdc7a4c643c9c8e75c63729fd7e5bfcdad569cc) |
| 24 Sep 2026 | 0x2a90 | 50M | wallet `0x28c4` | +6.3% | [0x4691…](https://etherscan.io/tx/0x4691de28063607018913f3e2488d68e58d0c05a2f75da8453cdac74b101d853e) |
| 6 Nov 2026 | 0x2a90 | 25M | wallet `0x28c4` | +2.4% | [0x566e…](https://etherscan.io/tx/0x566eb7baf8323d0ef8cf08b765317bc0b905055931be7880e419374a92d8094e) |

- **None of the 875M arrived on a pump day.** Each lump moved on to the Kraken hot wallet within about ten minutes, which is how exchanges sweep customer deposits. These are deposits by a Kraken account holder, not Kraken's own supply.
- **The Stellar senders are unlabelled** (no home domain, no stellar.expert directory entry). [GB5P…](https://stellar.expert/explorer/public/account/GB5PZZXRRZYF4KA4OUZUOMOSK6DEXA5A6FZ4OETLUV36ERSZQHTDICQF) still holds 2.0B SHX and sent 1.3B to `GA73…` on 2 Apr 2026, and `GA73…` created `GAXG…`, so these look like one holder. [GAKL…](https://stellar.expert/explorer/public/account/GAKLLZ4EAFFH7CZBOIFK5NJMYOA7H7EOMCEU5NFK4YWFB4YIXDPIWQFU) holds 318.7M.
- **The pump-day deposit:** the unlabelled Ethereum wallet [`0x28c4…2166`](https://etherscan.io/address/0x28c4c81d30a98d17fe5657fee17afa694a452166) (a plain account, not a contract) gets most of its SHX bridged from the Stellar account [GCMK…JQT5](https://stellar.expert/explorer/public/account/GCMKEWP6BZ2NUSE3YSVN37HLPD5H2P6XTYWJZY5J2WDHS7WR37JKJQT5), which holds **15.3B SHX** (about 15% of supply, 82% of the float) on a single key. That account sent 499M (Oct 2025), 10M (Nov 2025), 50M (21 Oct 2026) and 100M (5 Nov 2026), and another Stellar account sent 180M on 16 Sep 2026. `0x28c4` trades through Uniswap V4 and pays 10–60M lumps into one-off addresses that forward to Kraken. One of those, **[28.1M SHX on 28 Sep 2026](https://etherscan.io/tx/0x15b838a61a6af1fd79e93f7007a77cffa534693763e78d14eac4c97578bec298), landed on a pump day (+44.7%; ~$146k at the $0.00521 close)** and went straight on to the Kraken hot wallet.
- A Stellar account with 15.3B SHX fits Stronghold's own non-escrow balance (the company holds ~81% of supply, 60B of it in escrow), but it is not published or labelled, and `0x28c4` behaves like a market maker. Under the v3 rule the selling must be tied to a team or treasury wallet, so this stays **not proven → 4**. If Stronghold confirms `GCMK…` is its own, Selling becomes 3, the gate fails, and the overall drops to 3.5.
- The large Ethereum holder [0x1a9d](https://intel.arkm.com/explorer/address/0x1a9d699aee3a56ca49d0cc3b542ae3a37885a3e1) (279.9M) is unlabelled and was funded from Kraken withdrawals; it looks like a private holder, not Stronghold.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- A fixed 100B cap, but up to 12B a year can be released from escrow. That's 64% of today's float, and 81% of supply is insider-held.

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $0.69M a day across Gate, Kraken, MEXC and Stellar DEXs. It's spiky: +90.8% in five days in Oct 2026.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Payments network, rewards program, merchant-financing liquidity pools, and wallet support (Freighter, Lobstr, Ledger, Tangem) ([SHx page](https://stronghold.co/shx)).

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- No public usage figures for the rewards or financing programs.

## 🛡️ Security & audits · 6/10 · ✅ PASS

- Stellar-native asset with no known exploit. The Ethereum copy has an upgrade contract.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- No ICO, IEO or TGE, and a published MiCA white paper ([SHx page](https://stronghold.co/shx)). No enforcement found.

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

- An escrow-tracking dashboard (promised), plus merchant network growth.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | 🟠 Not proven: 875M bridged into Kraken deposits (no pump days); 28.1M to Kraken on the 28 Sep 2026 pump day via an unlabelled wallet funded by a 15.3B-SHX Stellar account [Unverified owner] |
| Live mint path | 🟡 No minting, but 1B a month escrow release |
| Entity concentration | 🔴 ~81% company-held |

## 📚 Sources

- [Tier A] [SHx page and FAQ](https://stronghold.co/shx), [Escrow announcement](https://stronghold.co/learn/stronghold-locks-60-billion-shx-escrow)
- [Tier A] Stellar Horizon (issuer and sender accounts); Etherscan token holders and transfers for `0x516d…9787`; Axelarscan GMP messages for the bridge mints (source chain and account)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Kraken Hot Wallet on 0xf213; Kraken Deposit on 0x2a90, 0xe84c, 0x5086, 0x63dc and 0x504c; 0x1a9d and 0x28c4 unlabelled
- [Tier A] CoinGecko `stronghold-token` (market, venues); pump days from Kraken SHXUSD daily closes (CoinGecko's price series for SHx has bad spikes in Mar 2026, so it wasn't used)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| 60B escrow, 1B a month | [Stronghold](https://stronghold.co/learn/stronghold-locks-60-billion-shx-escrow) | A | 16 Nov 2026 |
| No ICO, ~5% airdrop | [Stronghold](https://stronghold.co/shx) | A | 16 Nov 2026 |
| 0xf213 is a Kraken hot wallet; four Kraken deposits got 875M | [Etherscan](https://etherscan.io/address/0xf213ac78ca8ff79f54eab193836053eea163f190) · [Arkham](https://intel.arkm.com/explorer/address/0xf213ac78ca8ff79f54eab193836053eea163f190) | A + B | 16 Nov 2026 |
| 28.1M to Kraken on a pump day via 0x28c4 | [tx 0x15b8…](https://etherscan.io/tx/0x15b838a61a6af1fd79e93f7007a77cffa534693763e78d14eac4c97578bec298) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Whose are Stellar accounts `GCMK…JQT5` (15.3B SHX) and `GB5P…TDICQF` (2.0B)** | Ask Stronghold to publish its treasury and distribution accounts; a match settles the Selling gate | Free |
| 2 | **Monthly escrow usage** | Read the Soroban escrow events on stellar.expert (paid API) or a public dashboard | Free once published |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
