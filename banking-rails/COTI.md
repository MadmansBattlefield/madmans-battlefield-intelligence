---
ticker: COTI
name: COTI
chain: coti
contract: "0xddb3422497e61e13543bea06989c0789117555c5"
overall_score: 2.1
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 3
  insider_holdings: 2
  selling_behavior: 0
  tokenomics_supply: 2
  liquidity_market: 4
  product_development: 3
  adoption_customers: 2
  security_audits: 4
  regulatory: 3
  catalysts: 3
gates_failed: [revenue, selling_behavior]
red_lines:
  hack_exploit: "Mar 2023 bridge mis-mint on the ERC20 (huge test mints, burned the same day; COTI says no funds left the bridge)"
  mint_path_live: "yes (ERC20 owner can mint without limit; mintingFinished = false; native V2 chain still inflates)"
  team_wallet_to_exchange_during_pump: "yes (wallets funded within hours by the Sep 2026 consolidation sent 68.0M COTI to Gate and KuCoin deposits on pump days 18-20 Sep 2026, 157.4M in total by 10 Oct)"
  treasury_in_single_key_wallets: "yes (the two largest consolidation wallets, 1.29B and 877.6M COTI, are plain EOAs); the ERC20 owner key moved from an EOA to a 3-of-4 Safe on 6 Nov 2026"
methodology_effective: 2026-11-16
revenue_reaches_holders: "no"
revenue_mechanism: "Fees are close to zero and holders have no claim on them."
pump_day_price_source: "Gate COTI/USDT daily closes"
pump_day_disclosure_quality: silence
pump_day_undisclosed_penalty_applied: true
dual_review: not_run
attributions:
  - address: "0x61bf10a1a27b2d99de0a59a06200a62ed579d685"
    label: "COTI consolidation wallet (received 600M minted by the owner key)"
    confidence: high
    independent_corroboration: true
    basis: "Etherscan mint transactions"
price_usd: 0.00845036
price_source: "CoinGecko, 16 Nov 2026 7:13 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### COTI · Overall grade **2.1 / 10 · ❌ FAIL**

**Summary:** COTI is a privacy-focused Layer 2 whose ERC20 is a bridge token: the contract owner mints whenever coins are bridged in. The coin has **no revenue for holders**; chain fees were about $488 over the last year on DefiLlama. In Aug–Sep 2026 the project paused Treasury, COTI Earn and Nodes v2, management stepped down and a new foundation took over direction [Unverified]. In the same weeks about **2.6B ERC20 COTI (≈87% of circulating supply)** was minted or consolidated into a "Genesis" wallet and split into unlabelled EOAs. Wallets funded from that split then **sold into the 17 Sep spike**. The price is down 98.7% from its 2021 high. Revenue and Selling both trip the hard gates.

**🚨 Top warning:** consolidation wallets dumped into the pump. On 16 Sep 2026 the owner key minted 600M ERC20 COTI into [`0x61bf…d685`](https://etherscan.io/address/0x61bf10a1a27b2d99de0a59a06200a62ed579d685) ([250M](https://etherscan.io/tx/0xc997ca0197268b07129ac18b54a0384f79d979f9bf3d01bf33d4765fab2b8c1f) · [350.5M](https://etherscan.io/tx/0x1efd23e70380d297c0b5f726e4f9a6bef0a239b66ef2aea1d95829421a9abab7)), on top of [1.38B on 6 Sep](https://etherscan.io/tx/0x8ca0eebd24c7dbe824d3fe338cdd24a0a0c053be5d29980e359c62ea8f22b3bf). The same day it split ~2.6B between [`0x1a18…f9ce`](https://etherscan.io/address/0x1a184244de9d3e726a3aa3d02b585e6ff8e2f9ce) and [`0xcf26…357f`](https://etherscan.io/address/0xcf26c9c96aa6267d85e67df5cb85acf4b7e3357f). `0xcf26` passed 114M to [`0x07d2…e68c`](https://etherscan.io/address/0x07d2ef1fac34f52fbd86196b5d9154e0a036e68c) and 100M to [`0xaac8…6de8`](https://etherscan.io/address/0xaac8ca81a671829d007d7a860a04cf096dc66de8). The price jumped 47% on 17 Sep (Gate close $0.0173 → $0.0254). From 18 to 20 Sep, `0x07d2` sent **68.0M COTI to Gate and KuCoin deposits on pump days** (5-day change +33%, +15%, +12%), e.g. [4.11M to Gate on 18 Sep](https://etherscan.io/tx/0xbd23d980a565670563fb526f31a1e94215533d61ea3c0e1eb19283b4c8dd1cc5). By 10 Oct the group had sent **157.4M** to Gate, KuCoin and Binance deposits. None of this was disclosed as a sale. The price is now $0.00845, −51% since 16 Sep.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 3/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 0/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 2/10 | ❌ FAIL |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 3/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 4/10 | ❌ FAIL |
| ⚖️ Regulatory | 3/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 COTI · COTI · 2.1 / 10 · ❌ FAIL

> **One line:** A privacy L2 with no holder revenue, a live mint key, a leadership handover, and new consolidation wallets that sold into the first pump after they were funded.

| 📊 Market (CoinGecko, 16 Nov 2026 7:13 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.00845036 | **ERC20** [`0xDDB3…55c5`](https://etherscan.io/address/0xddb3422497e61e13543bea06989c0789117555c5#code) `MintableToken`, `mintingFinished` = false |
| **24h / 7d / 30d** 🟢 +1.2% / 🔴 −13.2% / −23.9% · 1y −76.3% | **ERC20 totalSupply** 5,917,151,748 (vs 2.98B circulating on CoinGecko) |
| **Market cap** $25.18M · **FDV** $25.18M | **Owner** 3-of-4 Safe [`0x842c…0e5b`](https://etherscan.io/address/0x842cbba2e88898a381b493d1e32c707113660e5b) since 6 Nov 2026 |
| **24h volume** $14.95M | **#1 holder** [`0x1a18…f9ce`](https://etherscan.io/address/0x1a184244de9d3e726a3aa3d02b585e6ff8e2f9ce) 1,290,100,543 · **#2** [`0x0354…6acd`](https://etherscan.io/address/0x03548e0f5ef69d5b9b6976c570a20b08b0486acd) 877,565,271 |
| **ATH** $0.668634 (29 Sep 2021) · now −98.7% · CoinGecko tag "Alleged SEC Securities" | **Holders** 28,080 (Blockscout) |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

| Metric | Value | Source |
|---|---:|---|
| Chain fees | **$3.24 (30d) · $488 (1y)** | [Tier A] [DefiLlama COTI](https://defillama.com/chain/coti) |
| Holder revenue rights | **None.** Privacy fees: 50% burned, 50% to the Foundation | [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/coti) |
| Burn commitment | ≥100M COTI within 12 months of Mar 2026 | [Tier B] same filing; not verified on-chain |

**What it means:** Fees are close to zero and holders have no claim on them. **1, which trips the Revenue gate.**

- **Reaches holders (binary test, 16 Nov 2026 rules): No.** Fees are close to zero and holders have no claim on them.

## 🏛️ Foundation & team — Who is in charge? · 3/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Leadership | Management stepped down on 21 Sep 2026; "ZK Foundation" took over direction | [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/coti) [Unverified, single source] |
| Products paused | Treasury, COTI Earn and Nodes v2 paused 18 Aug 2026 | [Tier B] same filing [Unverified, single source] |
| Mint key | Deployer [`0xe0e4…91ae`](https://etherscan.io/address/0xe0e42c70880d57230fb843db5eba6800533e91ae) → EOA [`0xcd50…a577`](https://etherscan.io/address/0xcd50cfd2f94841858e7c702e1505994fa498a577) on [16 Sep 2026](https://etherscan.io/tx/0x5e63499185ed3cd44d3827570e44c7e7f190cb434c6a1954abbf9f1ce0d06788) → 3-of-4 Safe `0x842c…` on [6 Nov 2026](https://etherscan.io/tx/0x893ab192f94f576b86f6f059260d113dc3c2abfa7f87d63e714449f8099c717b). The old EOA is one of the four Safe signers | [Tier A] OwnershipTransferred logs; `getOwners()` / `getThreshold()` |
| Disclosure | Market-maker and custodian balances held but not disclosed; the "two new main addresses" were not published | [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/coti) · [COTI Telegram notice](https://t.me/cotichannel/3245) |

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Holder | COTI (ERC20) | Notes |
|---|---:|---|
| [`0x1a18…f9ce`](https://etherscan.io/address/0x1a184244de9d3e726a3aa3d02b585e6ff8e2f9ce) | **1,290,100,543** | EOA. Got [1.14B](https://etherscan.io/tx/0x9781d96ac94526ef54de86a621ab79f697313230af9cd9e7c79eb187dcb7e928) + 128M from `0x61bf` on 16 Sep and [20M](https://etherscan.io/tx/0x48e79c3ba90c9de98a798d83ad81d6607adaacaebadd452280d5ead17a9fb7d0) from `0x062e`; has never sent |
| [`0x0354…6acd`](https://etherscan.io/address/0x03548e0f5ef69d5b9b6976c570a20b08b0486acd) | **877,565,271** | EOA. Path: `0xcf26` → [`0x062e…dce`](https://etherscan.io/tx/0x61a5c5fd3cb5f092d4485d623ffe48148b40743bfb34e375f3fdb32336af089b) (992.1M, 17 Sep) → [`0x94c8…`](https://etherscan.io/tx/0x78fd67d4d364e23b869b6dd3d8a72aab68ed38819cec69a8446c0aabd50e3ebe) (877.6M, 1 Oct) → `0x0354` in 11 transfers (e.g. [87.76M](https://etherscan.io/tx/0x3733953af5c5a8555595dc8ce1131cac22c65a09427c45937a0c68837390fcf7)) |
| Distribution wallets `0x07d2…`, `0xab5b…`, `0xaac8…` | ~0 now | Got 114M, 106M and 100M from `0xcf26` on 16 Sep; emptied to exchanges and further hops |
| Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) | [`0x1a18…`](https://intel.arkm.com/explorer/address/0x1a184244de9d3e726a3aa3d02b585e6ff8e2f9ce) **1.29B** and [`0x0354…`](https://intel.arkm.com/explorer/address/0x03548e0f5ef69d5b9b6976c570a20b08b0486acd) **877.565M** are confirmed, tagged "COTI Whale" and unlabelled. Arkham's first pages show `0x1a18…` only receiving (1.142B from `0x61bf…`, 20M from `0x062e…`). They also show the 877.56M hop [`0x062e…`](https://intel.arkm.com/explorer/address/0x062e20b531b8e8ce0a17fc1130e27d62d3aeddce) → [`0x94c8…`](https://intel.arkm.com/explorer/address/0x94c8dc3c94533716ee64256812825f4d3da5a43e) → `0x0354…`. No owner is named. The deployer [`0xe0e4…`](https://intel.arkm.com/explorer/address/0xe0e42c70880d57230fb843db5eba6800533e91ae) is labelled **COTI : Deployer** | B |
| Attribution | The chain starts at owner-key mints, and the COTI notice says Foundation tokens were consolidated in a "Genesis wallet" and moved to "two new main addresses" in ~10 tx. That `0x61bf` is the Genesis wallet is inferred | [Tier A] mints · [Tier B] [notice](https://t.me/cotichannel/3245) |

**What it means:** Two unlabelled single-key EOAs hold **2.17B ERC20 COTI, ≈73% of circulating supply**, and the project has not published which wallets are its own. **2**.

## 📉 Selling behavior — Do insiders sell into pumps? · 0/10 · ❌ FAIL

*Pump test uses Gate COTI/USDT daily closes (UTC). 33 of the last 365 days were pump days. Only Ethereum ERC20 flows were tested.*

| Day (UTC) | Route | COTI | 5-day change | Pump? |
|---|---|---:|---:|---|
| 18 Sep 2026 | `0x07d2` → Gate deposit [`0x1720…f3da`](https://etherscan.io/address/0x172075b0f30fe17b1138078844bb3764abe0f3da), 8 tx ([e.g.](https://etherscan.io/tx/0xf60561c017c0388294606f71c8dfc283e7f8544635ad485c86d2d198943f898c)) | 24,409,210 | +33.4% | **Yes** |
| 19 Sep 2026 | `0x07d2` → Gate and KuCoin deposit [`0x0B51…993A`](https://etherscan.io/address/0x0b5109873aa17ad3a044c7d5f9ef2ea8d1bc993a) ([e.g.](https://etherscan.io/tx/0x583b6f426fd9ac360bc361fa013560d631c39fd525d611a65373195d4ea28254)) | 22,268,038 | +14.9% | **Yes** |
| 20 Sep 2026 | `0x07d2` → Gate and KuCoin deposits ([e.g.](https://etherscan.io/tx/0x1944355ed130b8c6d4efd0699741607fc6b1bc1bf516f785570a32863d1806c3)) | 21,346,976 | +12.4% | **Yes** |
| 21–28 Sep 2026 | `0x07d2`, `0xaac8` and `0x4d2a…` (fed by `0xab5b`) → Gate, KuCoin and Binance deposits ([Binance e.g.](https://etherscan.io/tx/0x02954f880062c73597b92b6a2b97cc4aa810efca44c5826cb29df5d78d34e119)) | 85,254,497 | −21% to +2% | No |
| 10 Oct 2026 | `0x07d2` → Gate and KuCoin ([e.g.](https://etherscan.io/tx/0x4bae36c2d648e9f1e1ede6e05e488955f44a6d716f65556f1b6abd49e74be1c8)) | 4,130,080 | −8.5% | No |
| 2020–2024 (history) | Deployer → Binance deposits, incl. 150M on 18 Jul 2021 ([e.g.](https://etherscan.io/tx/0x15f6ab18e18a3c986b478a2ee517a3b7fa6f99f9be71edaf01e1b832a817659d)) and 71.67M on 5 Nov 2024 ([tx](https://etherscan.io/tx/0x5f7cf1b9d7f55fc1c098e2ea75fcacb6518786088a851a26cd58e1cd7ff2fb6e)) | — | −7.2% / −5.7% | No |

- **Total:** 157.4M COTI (≈5.3% of circulating) went to exchange deposits from 18 Sep to 10 Oct; **68.0M of it on pump days**.
- `0x07d2` also *received* ~67M from Binance 15/16, KuCoin 20 and a Gate deposit, which fits market-maker inventory [Unverified]. Even so, the funding came from the consolidation wallets and was not disclosed. **The market-maker question stays open:** the [Arkham page for `0x07d2…`](https://intel.arkm.com/explorer/address/0x07d2ef1fac34f52fbd86196b5d9154e0a036e68c) shows the address unlabelled, and its balance and transfer tables did not load after two attempts, so its Gate/KuCoin flows could not be cross-checked there [Unverified] (Arkham table did not render, 16 Nov).
- **Arkham ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)) confirms the exchange side:** [`0x1720…`](https://intel.arkm.com/explorer/address/0x172075b0f30fe17b1138078844bb3764abe0f3da) is a Gate deposit, [`0x0B51…`](https://intel.arkm.com/explorer/address/0x0b5109873aa17ad3a044c7d5f9ef2ea8d1bc993a) a KuCoin deposit, and [`0x655b…`](https://intel.arkm.com/explorer/address/0x655b7ea956d26eebcc6ec22ee9af9f0f871cd753) and [`0x2Ba9…`](https://intel.arkm.com/explorer/address/0x2ba95ffaaab55160af215bc33d036c8cda34fa09) are Binance deposits. [`0xaac8…`](https://intel.arkm.com/explorer/address/0xaac8ca81a671829d007d7a860a04cf096dc66de8) (85.62 COTI left) shows sends to the KuCoin and Gate deposits. [`0x4d2a…`](https://intel.arkm.com/explorer/address/0x4d2a4b7c76ff71ed4d641135123dabde71f7f10b) shows COTI sent to Binance deposit `0x655b…`. [`0xab5b…`](https://intel.arkm.com/explorer/address/0xab5b62cf058a8fe9a33dc73edb5a38cb53695623) (0.0033 COTI left) fed `0x4d2a…` and two other unlabelled wallets. None of these pages names a market maker.

**What it means:** Wallets funded by the Foundation's consolidation sold on three straight pump days. **2, which trips the Selling gate.**

- **Disclosure quality (16 Nov 2026 rules): silence.** COTI's Telegram notice mentioned "two new main addresses" without publishing them or these sales. **Penalty applied (16 Nov 2026 rules):** a proven pump-day sale with no disclosure fails Selling (ordinary score at most 3) and then loses 2 points, floored at 0: **2 → 0**. Pump days from Gate COTI/USDT daily closes.

## 📊 Tokenomics & supply · 2/10 · ❌ FAIL

- **Live ERC20 mint:** the owner can mint without a cap (`mintingFinished` = false). 1.98B was minted to `0x61bf` in Sep 2026. A notice says "no new COTI is created", and on 16 Sep a native rewards wallet sent 350,490,727 COTI to a dead address, matching the 350.49M ERC20 mint ([Blockworks](https://blockworks.com/token-transparency/filing/coti), Tier B).
- **Supply does not reconcile:** ERC20 `totalSupply` is 5.92B against 2.98B circulating and 4.91B max on CoinGecko.
- **Native inflation:** V2 emits every 103 hours, starting at 0.45% per period and declining; split 58% rewards / 24% Foundation / 18% development. A Mar 2026 update claimed fixed supply, which contradicts this [Tier B].

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $14.95M of 24h volume on a $25.18M cap (59% turnover), listed on Binance, Gate, KuCoin and others.
- −76% over a year and −98.7% from ATH; −51% since the 16 Sep consolidation.

## 🧑‍💻 Product & development · 3/10 · ❌ FAIL

- A privacy L2 with garbled-circuit privacy and its own mainnet. Treasury, COTI Earn and Nodes v2 have been paused since Aug 2026 [Tier B, Unverified].
- Chain fees of $3.24 in 30 days show almost no usage ([DefiLlama](https://defillama.com/chain/coti)).

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- No paying customer found that can be checked. Usage revenue is ~$0.

## 🛡️ Security & audits · 4/10 · ❌ FAIL

- **Mar 2023 bridge incident:** a misconfigured burn test minted huge ERC20 amounts on 22 Mar 2023, all burned the same day ([e.g.](https://etherscan.io/tx/0xd36940dad40aa23e0a0184390090ce40e5f35c26aafa6c28dc67a8698ea6ef00)). COTI says no funds left the bridge.
- Only one CertiK audit (Aug 2021) found [Tier B].
- The mint key has been a 3-of-4 Safe since 6 Nov 2026. Before that it sat in a single EOA for seven weeks, and with the deployer for six years before that.

## ⚖️ Regulatory · 3/10 · ❌ FAIL

- Named as a security in the SEC's Binance complaint (Jun 2023). The case was dismissed with prejudice on 29 May 2025 [Tier B].
- No-KYC travel, card and VPN products raise AML and sanctions risk [Tier B].

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

| Date | Event |
|---|---|
| By Mar 2027 | Promised ≥100M COTI burn [Tier B] |
| TBA | New foundation's plan; whether the paused products restart |
| Ongoing | 2.17B COTI in two EOAs could reach the market |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟡 Mar 2023 bridge mis-mint, burned the same day ([tx](https://etherscan.io/tx/0xd36940dad40aa23e0a0184390090ce40e5f35c26aafa6c28dc67a8698ea6ef00)) |
| Team wallet → exchange during a pump | 🔴 68.0M on 18–20 Sep 2026 from consolidation-funded `0x07d2` ([e.g.](https://etherscan.io/tx/0xbd23d980a565670563fb526f31a1e94215533d61ea3c0e1eb19283b4c8dd1cc5)) |
| Live mint path | 🔴 ERC20 owner mint is open; native emissions continue |
| Treasury in single-key wallets | 🔴 1.29B and 877.6M in EOAs [`0x1a18…`](https://etherscan.io/address/0x1a184244de9d3e726a3aa3d02b585e6ff8e2f9ce) and [`0x0354…`](https://etherscan.io/address/0x03548e0f5ef69d5b9b6976c570a20b08b0486acd) |
| Leadership change | 🟡 Management stepped down 21 Sep 2026 [Unverified] |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| [`0x61bf…d685`](https://etherscan.io/address/0x61bf10a1a27b2d99de0a59a06200a62ed579d685) | COTI consolidation wallet (received 600M minted by the owner key) | Etherscan mint transactions | high | yes (on-chain) | Selling: funded wallets that sent 68.0M COTI to Gate and KuCoin deposits on 18–20 Sep 2026 pump days |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Etherscan v2 API `tokentx` for `0x61bf`, `0xcf26`, `0x1a18`, `0x062e`, `0x94c8`, `0x0354`, `0x07d2`, `0xab5b`, `0xaac8`, `0x4d2a`, the deployer and their hops; Mint and OwnershipTransferred logs; Ethereum RPC `totalSupply()`, `balanceOf()`, `owner()`, Safe `getOwners()` / `getThreshold()`; read 16 Nov 2026 ~8:30–9:15 AM MST
- [Tier B] Etherscan name tags ("Coti: Deployer", "Gate Deposit", "KuCoin Deposit", "Binance Deposit", "Binance 15/16", "KuCoin 20"); Blockscout holder list
- [Tier A] [DefiLlama COTI chain fees](https://defillama.com/chain/coti); CoinGecko `coti` (16 Nov 2026 7:13 AM MST); Gate COTI/USDT daily candles
- [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/coti) · [COTI Telegram consolidation notice](https://t.me/cotichannel/3245)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): deployer labelled COTI : Deployer; `0x1a18…`, `0x0354…`, `0x062e…`, `0x94c8…`, `0xaac8…`, `0xab5b…`, `0x4d2a…` unlabelled; Gate, KuCoin and Binance deposit labels confirmed (links in Holdings and Selling). Pages for `0x07d2…`, `0xcf26…`, `0x61bf…`, `0xcd50…`, the Safe `0x842c…` and its signers, `0x0f9f…`, `0x8e08…`, `0x9365…`, `0x9f4d…`, `0x1ba5…`, `0x0fd7…` and `0xef38…` loaded only the profile; their balance and transfer tables did not load, so nothing on them is used here [Unverified] (Arkham table did not render, 16 Nov)
- [Unverified] Who controls `0x1a18`, `0x0354`, `0x07d2` and `0xaac8`; whether `0x07d2` is a market maker; the leadership change; native-chain Foundation flows

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Owner-key mints to `0x61bf` (1.98B, Sep 2026) | [1.38B](https://etherscan.io/tx/0x8ca0eebd24c7dbe824d3fe338cdd24a0a0c053be5d29980e359c62ea8f22b3bf) · [250M](https://etherscan.io/tx/0xc997ca0197268b07129ac18b54a0384f79d979f9bf3d01bf33d4765fab2b8c1f) · [350.5M](https://etherscan.io/tx/0x1efd23e70380d297c0b5f726e4f9a6bef0a239b66ef2aea1d95829421a9abab7) | A | 16 Nov 2026 |
| `0x61bf` → `0xcf26` and `0x1a18` (1.14B each) | [to 0xcf26](https://etherscan.io/tx/0xa396a38c58ed588f5b60bcd01b616b9790b50cacb4abb5f8fc413daa28d53840) · [to 0x1a18](https://etherscan.io/tx/0x9781d96ac94526ef54de86a621ab79f697313230af9cd9e7c79eb187dcb7e928) | A | 16 Nov 2026 |
| `0xcf26` → distribution wallets | [0x07d2 50M](https://etherscan.io/tx/0xd4b1b5d11ea7efe1f5ec9fc0d1257864b48d69dcc8a3f7a6903e6fed09900fab) · [0xaac8 100M](https://etherscan.io/tx/0x26d8108e3ef51864c6cb02d64fd37e5ce084db9a9873fa717fc8d51b88d5568d) · [0xab5b 42M](https://etherscan.io/tx/0x8a500aa04373df9b958e5aba21d7350d3be29b02249d9cd7f653e46e0a382095) · [0x062e 992.1M](https://etherscan.io/tx/0x61a5c5fd3cb5f092d4485d623ffe48148b40743bfb34e375f3fdb32336af089b) | A | 16 Nov 2026 |
| Pump-day sends to Gate / KuCoin | [18 Sep](https://etherscan.io/tx/0x3eaf4391b4cc9c3f21142c8dbf50d391bf99c951dfdcbe95675db0b3da0f7d03) · [19 Sep](https://etherscan.io/tx/0x2d3cf3ff37f8bf2e468091f4a0dbead7eea262b56569864b5b8345a499a87a9f) · [20 Sep](https://etherscan.io/tx/0x8cb800b6a4f9864de39d88747108db5e815656b0a6d2f491432f70fe5c3fe815) | A + B tag | 16 Nov 2026 |
| Ownership moves | [deployer → EOA](https://etherscan.io/tx/0x5e63499185ed3cd44d3827570e44c7e7f190cb434c6a1954abbf9f1ce0d06788) · [EOA → Safe](https://etherscan.io/tx/0x893ab192f94f576b86f6f059260d113dc3c2abfa7f87d63e714449f8099c717b) | A | 16 Nov 2026 |
| Mar 2023 bridge mis-mint | [tx](https://etherscan.io/tx/0xd36940dad40aa23e0a0184390090ce40e5f35c26aafa6c28dc67a8698ea6ef00) | A | 16 Nov 2026 |
| Leadership change, paused products, fee split | [Blockworks filing](https://blockworks.com/token-transparency/filing/coti) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Arkham rows that did not render** | Retry Arkham for `0x07d2…`, `0xcf26…`, `0x61bf…`, the Safe `0x842c…` and its signers, and the hop wallets `0x0f9f…`, `0x8e08…`, `0x9365…`, `0x9f4d…` [Unverified] (Arkham table did not render, 16 Nov) | Free (Arkham login) |
| 2 | **Which wallets are the "two new main addresses"?** | Ask COTI to publish its Foundation, market-maker and custodian wallets | Free |
| 3 | **Is `0x07d2` a market maker?** (open) | Arkham shows it unlabelled and its tables did not load (16 Nov). Ask COTI for its market-maker agreements; compare net flow (deposits minus withdrawals) | Free |
| 4 | **ERC20 supply vs circulating** | Reconcile 5.92B ERC20 `totalSupply` with the bridge's locked native balance on the COTI chain | Free |
| 5 | **Native-chain Foundation flows** | Trace V2 Foundation and rewards wallets on the COTI explorer and pump-test them | Free |
| 6 | **Leadership change** | Find a second independent source (official COTI post or filing) for the 21 Sep 2026 handover | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
