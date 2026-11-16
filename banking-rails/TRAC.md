---
ticker: TRAC
name: OriginTrail
chain: ethereum
contract: "0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f"
overall_score: 4.2
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 5
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 6
  liquidity_market: 4
  product_development: 6
  adoption_customers: 4
  security_audits: 6
  regulatory: 6
  catalysts: 5
gates_failed: [revenue]
red_lines:
  hack_exploit: "no hack found; 2018 sale-contract bug minted ~9,606 excess TRACE (no loss of funds, token re-issued as TRAC)"
  mint_path_live: "no: mintingFinished() = true, totalSupply() = 500,000,000"
  team_wallet_to_exchange_during_pump: "yes, small and indirect: a treasury-loop wallet sent 5M TRAC to Wintermute's multisig on a pump day (9 Nov 2021, +16.4%; disclosed market-maker partnership, amount undisclosed); two wallets funded by Trace Labs' main wallet sent 587k TRAC to KuCoin deposit addresses, 550k of it on pump days (Oct 2023 - Feb 2024); attribution of those two wallets [Unverified]"
  one_hop_sale_status: not_proven
  treasury_selling: "development treasury (100M+ TRAC) has no published address, balance or spending rule; 1.5M TRAC to Wintermute (Dec 2023) and 103k to a Gate deposit (Apr 2024) from the main Trace Labs wallet"
methodology_effective: 2026-11-16
revenue_reaches_holders: "yes"
revenue_mechanism: "Publishers pay TRAC that is distributed to stakers on-chain, which counts as staking yield from fees, but no total is published; Revenue stays 2."
pump_day_price_source: "Coinbase TRAC-USD daily closes"
pump_day_disclosure_quality: not_applicable
pump_day_undisclosed_penalty_applied: false
dual_review: not_run
attributions: []
price_usd: 0.28928
price_source: "CoinGecko, 16 Nov 2026 5:11 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### TRAC · Overall grade **4.2 / 10 · ❌ FAIL**

**Summary:** OriginTrail runs a Decentralized Knowledge Graph (DKG V10 on Base and Gnosis, plus the NeuroWeb parachain). TRAC is used to pay for publishing and is staked behind nodes. Supply is fixed at 500M and minting is permanently off. That part is clean. But **the protocol earns nothing for the token**: publishing fees go to stakers, the protocol treasury fee is set to 0%, and no fee data is published (DefiLlama does not track it). That fails the revenue gate. The founders' company (Trace Labs) controls a development treasury of 100M+ TRAC with **no published address, balance or spending rule**. On-chain it moves through a loop of plain wallets and bridges. TRAC is −48.5% in a year and −91.7% from its high.

**🚨 Top warning:** Trace Labs' main wallet [`0x599c…3ee1`](https://etherscan.io/address/0x599c59081d9b673bbddafbc933b669aa84ea3ee1) is proven to be theirs: it is a signer on the 2-of-3 multisig that owns the V10 Hub on Base. (Arkham has no entity label for it or any other wallet here, [Arkham](https://intel.arkm.com/explorer/address/0x599c59081d9b673bbddafbc933b669aa84ea3ee1), so this rests on the on-chain signer proof alone.) It received **235.8M TRAC (47% of supply)** from the 2018 team multisig. It then cycled 100M+ TRAC through plain wallets: out [100M on 3 May 2020](https://etherscan.io/tx/0x8496ab2207d4ea0b2bf552735a368491a62d004fa04a09e5e5aad47164bbe785) and back as [120.5M on 14 Oct 2025](https://etherscan.io/tx/0x57d60f0747eca62d02e21a3528adc47b8d0f44ef52fabefff6287e5af153c3aa). The same day it bridged all 120.5M to Polkadot via [Snowbridge](https://etherscan.io/tx/0xac7cc5a8240d35ada8f880fd328ab827ced6f0c68b1f782f306eb05565ebb0cc). **60M TRAC came back out of Snowbridge on 13 Apr 2026 to a fresh wallet [`0x786b…a0c5`](https://etherscan.io/address/0x786b09025a77d32d3f454fc41ae34e90437fa0c5)**, which still holds it. Arkham shows the 60M arriving as two 30M transfers from Snowbridge's "Agent (0xd80)" but gives no owner ([Arkham](https://intel.arkm.com/explorer/address/0x786b09025a77d32d3f454fc41ae34e90437fa0c5)). Its owner is [Unverified]. Separately, a wallet in that loop sent [5M TRAC to Wintermute on a +16.4% pump day](https://etherscan.io/tx/0x3d3710311433034dd80a9502be01bef23eb61a39afaa85ee6f71f7ed1a85dabc) (9 Nov 2021). Every link is in the 🔗 Evidence trail below.

**Sections passed: 4 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 5/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 6/10 | ✅ PASS |
| 💧 Liquidity & market | 4/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 6/10 | ✅ PASS |
| 🤝 Adoption & customers | 4/10 | ❌ FAIL |
| 🛡️ Security & audits | 6/10 | ✅ PASS |
| ⚖️ Regulatory | 6/10 | ✅ PASS |
| 📅 Catalysts & calendar | 5/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 TRAC · OriginTrail · 4.2 / 10 · ❌ FAIL

> **One line:** A real knowledge-graph network with a fixed-supply token, but no protocol revenue, and a founder-controlled treasury of 100M+ TRAC that moves through unlabeled wallets and bridges with no published accounting.

| 📊 Market (CoinGecko, 16 Nov 2026 5:11 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.2893 | **Contract** [`0xaa7a…0a6f`](https://etherscan.io/token/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f) (verified `TracToken`) |
| **24h / 7d / 30d** 🔴 −1.6% / −12.2% / −27.4% · 1y −48.5% | **`totalSupply()`** 500,000,000 · **`mintingFinished()`** true · `owner()` = [deployer `0xe80d…471a`](https://etherscan.io/address/0xe80d171dbe7898ef93d0b2be621d2978921c471a) |
| **Market cap** $129.4M · **FDV** $144.7M | **Circulating (CoinGecko)** 447.27M (89.5%); the project says all tokens circulate |
| **24h volume** $1.43M (HTX $887k, Upbit $714k, then GroveX, KuCoin, Uniswap, Coinbase $185k) | **Locked in bridges** 120.2M (24%): [Gnosis OmniBridge](https://etherscan.io/token/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f?a=0x88ad09518695c6c3712ac10a214be5109a655671) 68.2M · [Base Bridge](https://etherscan.io/token/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f?a=0x3154cf16ccdb4c6d922629664174b904d80f2c35) 32.9M · [Snowbridge](https://etherscan.io/token/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f?a=0xd803472c47a87d7b63e888de53f03b4191b846a8) 19.1M |
| **ATH** $3.50 (3 Nov 2021) · now −91.7% | **Base token** [`0xa81a…ba23`](https://basescan.org/token/0xa81a52b4dda010896cdd386c7fbdc5cdc835ba23) |
| **Pump days, last 365 days** 42 (Coinbase TRAC-USD closes) | **V10 Hub owner (Base)** [`0x4cd6…4068`](https://basescan.org/address/0x4cd6467b797846e63a27c92350d040c428394068), 2-of-3 multisig |

*Note: volumes are self-reported by exchanges via CoinGecko; HTX and Upbit together are ~112% of the CoinGecko 24h total because other venues report in different windows. Treat as approximate.*

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

| Metric | Value | Source |
|---|---:|---|
| Protocol revenue | **None.** The protocol treasury fee is governance-set, default 3%, cap 10%, and **stays at 0%** until a recipient is set | [Tier A] [OriginTrail docs: Conviction and Economics](https://docs.origintrail.io/) · [Tier B] [Blockworks Token Transparency filing](https://blockworks.com/token-transparency/filing/origintrail) |
| Fees paid by publishers | Paid in TRAC to stakers / node operators; **no public total** | Not found on DefiLlama ([`origintrail` → "not found"](https://api.llama.fi/summary/fees/origintrail?dataType=dailyFees), 16 Nov 2026) |
| Money to Trace Labs | None from the protocol; Trace Labs sells its own nOS enterprise product (revenue not published) | [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/origintrail) |

**What it means:** Stakers earn TRAC that publishers pay, but no total is published and nothing accrues to the protocol or to holders who don't stake. Revenue cannot be shown, so it is scored as not proven. **2 → hard-gate FAIL.**

- **Reaches holders (binary test, 16 Nov 2026 rules): Yes.** Publishers pay TRAC that is distributed to stakers on-chain, which counts as staking yield from fees, but no total is published; Revenue stays 2.

## 🏛️ Foundation & team — Who is in charge? · 5/10 · ❌ FAIL

| Item | Finding | Source |
|---|---|---|
| Issuer / dev company | Trace Labs Ltd. (Hong Kong), the for-profit core developer; it ran the Jan 2018 sale. A separate OriginTrail d.o.o. licenses the node software (Apache 2.0) | [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/origintrail) · [Tier A] [TracToken source](https://etherscan.io/address/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f#code) |
| Foundation / DAO | **None.** No foundation and no tokenholder voting; protocol changes go through OT-RFCs written by core developers | [Tier B] same filing |
| Founders | Public and long-standing (named in the filing; not repeated here) | [Tier B] same filing |
| Who controls V10 | The Hub owner on Base is a **2-of-3 MultiSigWallet**. `required()` = 2; `getOwners()` = [`0x599c…3ee1`](https://basescan.org/address/0x599c59081d9b673bbddafbc933b669aa84ea3ee1), [`0x30be…cd75`](https://basescan.org/address/0x30be8edf5ee202660af0814a3f3fc341a11ecd75), [`0x17f5…2a38`](https://basescan.org/address/0x17f5ad6192e24f5c7cd888742532124780a42a38). It can swap in new contracts and add staking tiers | [Tier A] `eth_call` on Base RPC, 16 Nov 2026 · [multisig](https://basescan.org/address/0x4cd6467b797846e63a27c92350d040c428394068) |

**What it means:** The team is public and has built for 8+ years. But all control sits with a 2-of-3 company multisig, and there is no DAO, foundation or published treasury policy. **5.**

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

**Launch allocation** (from the verified contract and the filing): sale 250M (50%) · future development 100M (20%) · team/founders 75M (15%, time-locked to Jan 2020) · pre-ICO and advisors 40M (8%) · liquidity 25M (5%) · bounty 10M (2%). The development, liquidity and bounty buckets (135M) plus released team tranches all went to the **team multisig** [`0x20e2…4d5e`](https://etherscan.io/address/0x20e2ab81e11d4d02fe71b8cf9e8e3c9e2f714d5e) (named in the token's constructor).

| Wallet | Role (how we know) | Flow | Balance now |
|---|---|---|---:|
| [`0x20e2…4d5e`](https://etherscan.io/address/0x20e2ab81e11d4d02fe71b8cf9e8e3c9e2f714d5e) | Team multisig (constructor arg, Tier A; unlabelled on Arkham, [Arkham](https://intel.arkm.com/explorer/address/0x20e2ab81e11d4d02fe71b8cf9e8e3c9e2f714d5e)) | Got 143M minted + 50.7M released from contract locks; sent **235.8M to `0x599c…`** (e.g. [164.4M on 3 May 2020](https://etherscan.io/tx/0xd97c822949de046b7de3f81ff877a1378a425f262deaedc3240a756f06289497)) and 15.5M to `0x30be…` | 0 |
| [`0x599c…3ee1`](https://etherscan.io/address/0x599c59081d9b673bbddafbc933b669aa84ea3ee1) | Trace Labs main wallet (V10 Hub signer, Tier A; ENS `origintrail.base.eth`; unlabelled on Arkham, [Arkham](https://intel.arkm.com/explorer/address/0x599c59081d9b673bbddafbc933b669aa84ea3ee1)) | Received and sent 484.6M in total, incl. round-trips; see loop below | 0 |
| [`0x30be…cd75`](https://etherscan.io/address/0x30be8edf5ee202660af0814a3f3fc341a11ecd75) | Trace Labs (V10 Hub signer, Tier A; unlabelled on Arkham, [Arkham](https://intel.arkm.com/explorer/address/0x30be8edf5ee202660af0814a3f3fc341a11ecd75)) | Paid out ~53M in 2018–2025, incl. [11M on 25 Jul 2018](https://etherscan.io/tx/0xc722195f5ee8764c21fc158fd61b9d7c8d131cc8449624e1d4009050242c0993) | 0 |
| [`0x786b…a0c5`](https://etherscan.io/address/0x786b09025a77d32d3f454fc41ae34e90437fa0c5) | **[Unverified]** (Arkham: no entity, tags "TRAC Whale" only, [Arkham](https://intel.arkm.com/explorer/address/0x786b09025a77d32d3f454fc41ae34e90437fa0c5)) fresh wallet that got [30M](https://etherscan.io/tx/0x8ad391b4b815ee42fa8fc95e2540a065e22b786305fa44e88a59f30323856495) + [30M](https://etherscan.io/tx/0xf4b96c7e80904547e615f0936cf807ea8e16842cc739a90025bfe44c37ce3318) out of Snowbridge on 13 Apr 2026, six months after Trace Labs bridged 120.5M in | — | **60,000,000** |

**The treasury loop (all on Ethereum, all verified tx):**
1. `0x599c…` → [`0x3868…bbd4`](https://etherscan.io/address/0x386814732655e06ceabdb1aa6014bac9cf5ebbd4) **100M** ([3 May 2020](https://etherscan.io/tx/0x8496ab2207d4ea0b2bf552735a368491a62d004fa04a09e5e5aad47164bbe785))
2. `0x3868…` → [`0x801e…c100`](https://etherscan.io/address/0x801e8f44f01ee5cf0318593715391a465cedc100) 92.5M (5M [9 Nov 2021](https://etherscan.io/tx/0x295f2154a2ba73c8f57e859507fb928c076df4d3b055bc0d1b38022bbf53ad99), 2.5M Apr 2024, [85M 30 Dec 2024](https://etherscan.io/tx/0x1ab6b9c7c1389f6b026a4d96e4077cd150dc9118072e54fe8d224329b4ea082f))
3. `0x801e…` → [`0x26a8…9bb3`](https://etherscan.io/address/0x26a88e89c518f7cb93e25853e4e7c2ccddbb9bb3) [60M](https://etherscan.io/tx/0xd5f491ab5d09b60bed289e144848d21ae3868c9067030cfccbf35fe881a5378d) and → [`0x5624…9283`](https://etherscan.io/address/0x5624de5ccde31a5de34eba0eddca961eb7509283) [25M](https://etherscan.io/tx/0x2557014afc0e93643ab8879e009b240f1ca57251391636db29b50267c7f3e3a8) (30 Dec 2024); and → **Wintermute 5M** (9 Nov 2021, see Selling; Arkham shows `0x801e…` sending to a "Wintermute: Gnosis Safe Proxy", [Arkham](https://intel.arkm.com/explorer/address/0x801e8f44f01ee5cf0318593715391a465cedc100))
4. `0x26a8…` → [`0x248f…d65d`](https://etherscan.io/address/0x248fca4d916a78c9c24a9e80c228f7c6bfb8d65d) [61.1M](https://etherscan.io/tx/0x7b1a7f11bcb792d0bd32a341a1ff0afb0f2cfe5b65646d470634d68ae66bd115) (15 Jan 2025)
5. `0x248f…` → back to `0x599c…` [120.5M](https://etherscan.io/tx/0x57d60f0747eca62d02e21a3528adc47b8d0f44ef52fabefff6287e5af153c3aa) (14 Oct 2025) → **Snowbridge 120.5M** the same day ([20M](https://etherscan.io/tx/0x3953ba1e0ab4246201802b6415fb266ec2c8811bc2092691c3b882bf737645a6), [40M](https://etherscan.io/tx/0xac7cc5a8240d35ada8f880fd328ab827ced6f0c68b1f782f306eb05565ebb0cc), [40M](https://etherscan.io/tx/0x209d2b97359045289182131c0a38aba0e08df8abf46f9b69b4fa4273f429b295), [20.5M](https://etherscan.io/tx/0x143a27ba97e6d24d2cef856b92827976f8292d65c0922d0e81175a60ce9e6842))
6. `0x599c…` also sent [**100M to `0x0585…8122`** on 17 Sep 2021](https://etherscan.io/tx/0xa1ba1e98ba376709687c9139e792f20ec634b1ca237c65092bd95d1a3c3898a2), which paid it out to 285+ addresses in 2021 (purpose not found; 1.2M left; Arkham shows only unlabelled recipients, [Arkham](https://intel.arkm.com/explorer/address/0x0585a5e5aa9bf79e1788749d6b7ed08f87148122)).

**What it means:** Every Ethereum wallet we can tie to Trace Labs is now empty. The treasury (100M+ TRAC by the project's own account) sits on NeuroWeb/Polkadot, Base, Gnosis or in unlabeled wallets, and no balance is published. With 47% of supply having passed through one company wallet and no accounting, holdings are not proven. **3.**

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

Pump days come from Coinbase TRAC-USD daily closes (available from 2 Nov 2021); 42 in the last 365 days. Every exchange- or market-maker-tagged address (Etherscan labels) reached by the Trace Labs wallets above, directly or one hop out, is listed here:

| Date | From | To | TRAC | Pump day? | Tx |
|---|---|---|---:|:---:|---|
| 9 Nov 2021 | `0x801e…` (treasury loop) | Wintermute: Multisig (Etherscan) = "Wintermute: Gnosis Safe Proxy" (Arkham, [Arkham](https://intel.arkm.com/explorer/address/0x801e8f44f01ee5cf0318593715391a465cedc100)) | 5,000,000 | **Yes, +16.4%** (close $2.13) | [tx](https://etherscan.io/tx/0x3d3710311433034dd80a9502be01bef23eb61a39afaa85ee6f71f7ed1a85dabc) |
| 27 Oct 2023 | [`0x66f7…4434`](https://etherscan.io/address/0x66f77bacdeed009d2076413689924ee41d584434) (funded by `0x599c…`: [500k on 26 Oct 2023](https://etherscan.io/tx/0x3939af44bde2cb972c5eee14a740041f3f9db4ebb9acf85ddb6145a9a940d47b)) | KuCoin deposit | 200,000 | **Yes, +15.6%** | [tx](https://etherscan.io/tx/0x1ebf82d51add7cfdfd40e8ea72b551271482646f423df1cddd37cac50ca374fc) |
| 21 Dec 2023 | `0x599c…` (Trace Labs) | Wintermute `0xdbf5…c080` | 1,499,990 | No | [tx](https://etherscan.io/tx/0xda7c0bbce375328238e3388371cefca3f4a5672bf7e417968d92965a7ac39867) |
| 2 Feb 2024 | [`0x1430…ae77`](https://etherscan.io/address/0x14307e11cf7a330d58a8a83badffac5dafa3ae77) (funded by `0x599c…`: [910k on 8 Dec 2023](https://etherscan.io/tx/0x285347a409e90535e9169bc314d61051e734a805734865047e558636ff75527b) + 390k) | KuCoin deposit | 250,000 | **Yes, +15.2%** | [tx](https://etherscan.io/tx/0x197604f6416196358f0e92f22c410bb78a7f6ea3c69d02cb4dfc6bb9fdbae08a) |
| 23 Feb 2024 | `0x1430…` | KuCoin deposit | 100,000 | **Yes, +26.3%** | [tx](https://etherscan.io/tx/0xf918642de0c8fb3476b4954205897eba1ea0ed1edb901f2bd57c34541f994c7e) |
| 4 Apr 2024 | `0x66f7…` | KuCoin deposit | 37,181 | No | [tx](https://etherscan.io/tx/0x1ee597d6117b621251acb413b9266d02d0e869b3c9c386d2eb18e0902e1e510e) |
| 24 Apr 2024 | `0x599c…` (Trace Labs) | Gate deposit | 103,000 | No | [tx](https://etherscan.io/tx/0xe7778171179cecfb9b7f87d699bdf97296bb0211cc742777f0a7d29f9a18c0af) |

- **Wintermute:** Trace Labs [announced a market-making partnership with Wintermute in Nov 2021](https://origintrail.io/blog/trace-labs-core-origintrail-development-company-partners-with-wintermute-the-leading-market-making-firm). It said Wintermute stays market-neutral. **The TRAC amount and terms were never disclosed.** On-chain, 6.5M TRAC went to Wintermute, 5M of it on a pump day.
- **KuCoin and others:** `0x66f7…` and `0x1430…` got 1.9M TRAC from Trace Labs' main wallet, then sent 587k to KuCoin deposit addresses, **550k of it on pump days**. Arkham ([Tier B] Arkham, read 16 Nov 2026 ~6:53 AM MST (signed-in account)) shows both feeding more exchanges than Etherscan tags: `0x66f7…` to a KuCoin hot wallet, a Crypto.com deposit and a Coinbase deposit ([Arkham](https://intel.arkm.com/explorer/address/0x66f77bacdeed009d2076413689924ee41d584434)), and `0x1430…` (still 703k TRAC) to KuCoin deposits and a Bitget hot wallet ([Arkham](https://intel.arkm.com/explorer/address/0x14307e11cf7a330d58a8a83badffac5dafa3ae77)). Neither has an entity label, so whether they are Trace Labs, contractors or buyers stays [Unverified].
- **Last 12 months:** none of the Trace Labs-linked wallets sent TRAC to a tagged exchange. Their outflows went to bridges (Gnosis, Base, Snowbridge). Sales on L2 DEXs or after bridging were not traced.

**What it means:** No large direct dump was found, but treasury-funded wallets reached exchanges and a market maker on pump days, and the market-maker amounts were not disclosed. Per the rules (funding a wallet that sells on a pump day without disclosure), this fails. It is not at gate level, because the amounts are small against supply and the main flows are bridges. **4, unchanged after the Arkham pass:** Arkham confirms the Wintermute route and shows the two KuCoin-feeding wallets also reaching Crypto.com, Coinbase and Bitget, but labels none of the 11 wallets as Trace Labs, so it neither strengthens nor weakens the attribution.

- **Disclosure quality (16 Nov 2026 rules): not applicable** (cleanup 16 Nov 2026: the sale is not proven under the one-hop amendment, so no disclosure grade applies). Context: The market-maker partnership was announced but the amount was not, so disclosure is partial and no penalty applies; Selling stays 4. Pump days from Coinbase TRAC-USD daily closes.

## 📊 Tokenomics & supply · 6/10 · ✅ PASS

- **Fixed supply, minting off:** `totalSupply()` = 500,000,000 and `mintingFinished()` = true (`eth_call`, 16 Nov 2026). The [verified source](https://etherscan.io/address/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f#code) has no pause, burn or upgrade path.
- All contract time-locks (team, pre-ICO, advisors) ended by early 2020.
- **Overhang:** the 100M+ development treasury is unlocked, has no published balance, and could be sold at any time. About 24% of supply sits in bridges, so the real float on each chain is hard to see.

## 💧 Liquidity & market · 4/10 · ❌ FAIL

- $1.43M of 24h volume on a $129M cap (~1.1% a day). It is concentrated on HTX and Upbit; Coinbase is only $185k (CoinGecko tickers, 16 Nov 2026 5:11 AM MST).
- On-chain pools are thin: the [Uniswap V2 TRAC/WETH pair](https://etherscan.io/address/0x1a58aa618df8f1ec282748fef6185c1a1cc2faa6) holds 44k TRAC and the [Uniswap V3 "TRAC 2" pool](https://etherscan.io/address/0xb1914469141ebb6e244e75cee3f35d43bf6b85e5) holds 0.92M TRAC.
- Price −48.5% in a year and −27.4% in 30 days.

## 🧑‍💻 Product & development · 6/10 · ✅ PASS

- DKG V10 runs on Base and Gnosis. TRAC is bridged to Base (Superbridge), Gnosis (OmniBridge) and NeuroWeb (Snowbridge). Staking uses "Conviction" NFT positions with 1–12 month locks ([OriginTrail docs](https://docs.origintrail.io/); [Tier B] [Blockworks filing](https://blockworks.com/token-transparency/filing/origintrail)).
- Code is public in the [OriginTrail GitHub](https://github.com/OriginTrail). The V10 pre-mainnet bug bounty with a live honeypot on Base ran from June 2026.

## 🤝 Adoption & customers · 4/10 · ❌ FAIL

- 120M+ TRAC is bridged to the chains where the DKG runs, which suggests real staking use. But **no published, verifiable count** of paid publishing volume, Knowledge Assets or paying customers was found this pass. Enterprise pilots are described by the project, not proven on-chain. [Unverified]

## 🛡️ Security & audits · 6/10 · ✅ PASS

- No hack of TRAC found. The 2018 sale contract had a bug that minted ~9,606 excess tokens; the token was re-issued as TRAC and the excess was taken from the founders' pool. No funds were lost ([TracToken source](https://etherscan.io/address/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f#code); [Tier B] filing).
- Risks: the V10 Hub can be upgraded by a **2-of-3 company multisig**, and TRAC on L2s depends on three bridges. Bounties run, but no formal verification is disclosed.

## ⚖️ Regulatory · 6/10 · ✅ PASS

- Listed on regulated venues (Coinbase, Kraken, Binance.US, Bitstamp, Bitvavo). No enforcement action against TRAC or Trace Labs was found.
- No MiCA white paper for TRAC was found. The V10 terms call TRAC a utility token and put compliance on the user ([Tier B] filing).

## 📅 Catalysts & calendar · 5/10 · ❌ FAIL

| Date | Event |
|---|---|
| 2026 | DKG V10 mainnet on Base/Gnosis; V8 publisher commitments now emit to stakers over up to 2 years (front-loaded rewards) |
| Open | Governance could switch on the 0–10% protocol treasury fee (no date) |
| Risk | Any move of the 60M TRAC in `0x786b…` or of the unpublished treasury |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found (2018 sale-contract bug, no loss) |
| Team wallet → exchange during a pump | 🟡 Indirect: 5M to Wintermute on a +16.4% day ([tx](https://etherscan.io/tx/0x3d3710311433034dd80a9502be01bef23eb61a39afaa85ee6f71f7ed1a85dabc)); treasury-funded wallets sent 550k to KuCoin on pump days ([tx](https://etherscan.io/tx/0x197604f6416196358f0e92f22c410bb78a7f6ea3c69d02cb4dfc6bb9fdbae08a)) and, per Arkham, also fed Crypto.com, Coinbase and Bitget ([0x66f7](https://intel.arkm.com/explorer/address/0x66f77bacdeed009d2076413689924ee41d584434) · [0x1430](https://intel.arkm.com/explorer/address/0x14307e11cf7a330d58a8a83badffac5dafa3ae77)); attribution [Unverified] |
| Live mint path | 🟢 No: `mintingFinished()` = true |
| Treasury selling | 🟡 Treasury of 100M+ TRAC with no published address or policy; 1.6M to Wintermute/Gate from the main wallet |

## 🏷️ Attribution confidence (16 Nov 2026 rules)

*Only a verified entity label with on-chain proof, or a second independent source, can move Selling or Holdings. Unlabelled or low-confidence attributions are described but do not move a score on their own. Dual review of Selling and Holdings: not run (single scorer).*

| Address | Label | Source | Confidence | Independent corroboration | Effect on score |
|---|---|---|---|---|---|
| Treasury-loop wallet → Wintermute multisig (9 Nov 2021) | Trace Labs treasury | Etherscan + disclosed MM partnership | high | yes | Selling: disclosed partnership, amount undisclosed |
| Two wallets funded by Trace Labs' main wallet → KuCoin | Attribution [Unverified] | Etherscan | low | no | None: cannot move Selling |

## 📚 Sources

- [Tier A] Methodology update 16 Nov 2026: no new Arkham lookups; the attribution table uses evidence already cited in this report.
- [Tier A] Ethereum via Etherscan API v2: TRAC `totalSupply`, `mintingFinished()`, `owner()`, `tokenbalance`; contract creation and constructor args; full TRAC `tokentx` for 0x20e2, 0x599c, 0x30be, 0x248f, 0x296e, 0x3868, 0x801e, 0x26a8, 0x5624, 0x0585, 0x9cf1, Snowbridge (1,620 rows), the Gnosis OmniBridge (2,621 rows) and 45 second-hop wallets; `getsourcecode` contract names; receipts for every linked tx (status 1), 16 Nov 2026 ~8:00–9:30 AM MST
- [Tier A] Base RPC: V10 Hub owner multisig `required()` and `getOwners()`, 16 Nov 2026
- [Tier A] Etherscan public labels (Wintermute, KuCoin/Gate deposit, Snowbridge, Base Bridge, Origin Trail: Deployer); [Gnosis docs: OmniBridge](https://docs.gnosischain.com/bridges/About%20Token%20Bridges/omnibridge) for `0x88ad…5671`
- [Tier A] [Trace Labs × Wintermute announcement](https://origintrail.io/blog/trace-labs-core-origintrail-development-company-partners-with-wintermute-the-leading-market-making-firm) · [OriginTrail docs](https://docs.origintrail.io/) · [TRAC token page](https://origintrail.io/technology/trac-token)
- [Tier B] [Blockworks Token Transparency filing: OriginTrail](https://blockworks.com/token-transparency/filing/origintrail) (compiled from public records and possibly project input)
- [Tier A] CoinGecko `origintrail` market data and tickers (16 Nov 2026 5:11 AM MST); Coinbase TRAC-USD daily closes (from 2 Nov 2021); DefiLlama (no fee or revenue listing)
- [Unverified] owner of `0x786b…a0c5`; owners of `0x66f7…` and `0x1430…`; purpose of the 2021 `0x0585…` payout; treasury balances on NeuroWeb, Base and Gnosis
- [Tier B] Arkham, read 16 Nov 2026 ~6:53 AM MST (signed-in account): none of the 11 wallets checked has an entity label (`0x20e2…`, `0x599c…`, `0x30be…`, Base `0x17f5…`, `0x786b…`, `0x801e…`, `0x248f…`, `0x5624…`, `0x0585…`, `0x66f7…`, `0x1430…`), so Arkham does **not** confirm Trace Labs; that rests on the V10 Hub signer proof. Arkham does label the counterparties: "Wintermute: Gnosis Safe Proxy" (from [0x801e…](https://intel.arkm.com/explorer/address/0x801e8f44f01ee5cf0318593715391a465cedc100)), Snowbridge "Agent (0xd80)" (into [0x786b…](https://intel.arkm.com/explorer/address/0x786b09025a77d32d3f454fc41ae34e90437fa0c5)), KuCoin, Crypto.com, Coinbase and Bitget (from [0x66f7…](https://intel.arkm.com/explorer/address/0x66f77bacdeed009d2076413689924ee41d584434) and [0x1430…](https://intel.arkm.com/explorer/address/0x14307e11cf7a330d58a8a83badffac5dafa3ae77)). Token filter is Enterprise-only; first transfer page only

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Fixed 500M supply, minting finished, team multisig in constructor | [TracToken source](https://etherscan.io/address/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f#code) · [creation tx](https://etherscan.io/tx/0xfc3ca47c82e84519592a955fe0c89ea319ad3611bf62dee516f155719978985a) | A | 16 Nov 2026 |
| `0x599c…` and `0x30be…` are Trace Labs keys (V10 Hub 2-of-3 signers) | [Hub owner multisig](https://basescan.org/address/0x4cd6467b797846e63a27c92350d040c428394068#readContract) | A | 16 Nov 2026 |
| Team multisig → `0x599c…` 235.8M | [164.4M, 3 May 2020](https://etherscan.io/tx/0xd97c822949de046b7de3f81ff877a1378a425f262deaedc3240a756f06289497) · [wallet](https://etherscan.io/address/0x20e2ab81e11d4d02fe71b8cf9e8e3c9e2f714d5e) | A | 16 Nov 2026 |
| Treasury loop 100M out (2020) → 120.5M back (2025) | [out](https://etherscan.io/tx/0x8496ab2207d4ea0b2bf552735a368491a62d004fa04a09e5e5aad47164bbe785) · [85M](https://etherscan.io/tx/0x1ab6b9c7c1389f6b026a4d96e4077cd150dc9118072e54fe8d224329b4ea082f) · [60M](https://etherscan.io/tx/0xd5f491ab5d09b60bed289e144848d21ae3868c9067030cfccbf35fe881a5378d) · [61.1M](https://etherscan.io/tx/0x7b1a7f11bcb792d0bd32a341a1ff0afb0f2cfe5b65646d470634d68ae66bd115) · [back](https://etherscan.io/tx/0x57d60f0747eca62d02e21a3528adc47b8d0f44ef52fabefff6287e5af153c3aa) | A | 16 Nov 2026 |
| 120.5M bridged to Polkadot via Snowbridge, 14 Oct 2025 | [40M](https://etherscan.io/tx/0xac7cc5a8240d35ada8f880fd328ab827ced6f0c68b1f782f306eb05565ebb0cc) · [40M](https://etherscan.io/tx/0x209d2b97359045289182131c0a38aba0e08df8abf46f9b69b4fa4273f429b295) · [20M](https://etherscan.io/tx/0x3953ba1e0ab4246201802b6415fb266ec2c8811bc2092691c3b882bf737645a6) · [20.5M](https://etherscan.io/tx/0x143a27ba97e6d24d2cef856b92827976f8292d65c0922d0e81175a60ce9e6842) | A | 16 Nov 2026 |
| 60M out of Snowbridge to `0x786b…`, 13 Apr 2026 | [30M](https://etherscan.io/tx/0x8ad391b4b815ee42fa8fc95e2540a065e22b786305fa44e88a59f30323856495) · [30M](https://etherscan.io/tx/0xf4b96c7e80904547e615f0936cf807ea8e16842cc739a90025bfe44c37ce3318) · [Arkham](https://intel.arkm.com/explorer/address/0x786b09025a77d32d3f454fc41ae34e90437fa0c5) (2 × 30M from "Agent (0xd80)", no owner) | A chain + B · owner [Unverified] | 16 Nov 2026 |
| 5M to Wintermute on a pump day; partnership disclosed, amount not | [tx](https://etherscan.io/tx/0x3d3710311433034dd80a9502be01bef23eb61a39afaa85ee6f71f7ed1a85dabc) · [announcement](https://origintrail.io/blog/trace-labs-core-origintrail-development-company-partners-with-wintermute-the-leading-market-making-firm) · Arkham Wintermute Safe [Arkham](https://intel.arkm.com/explorer/address/0x801e8f44f01ee5cf0318593715391a465cedc100) | A + B | 16 Nov 2026 |
| Treasury-funded wallets → KuCoin on pump days | [funding](https://etherscan.io/tx/0x285347a409e90535e9169bc314d61051e734a805734865047e558636ff75527b) · [2 Feb 2024](https://etherscan.io/tx/0x197604f6416196358f0e92f22c410bb78a7f6ea3c69d02cb4dfc6bb9fdbae08a) · [23 Feb 2024](https://etherscan.io/tx/0xf918642de0c8fb3476b4954205897eba1ea0ed1edb901f2bd57c34541f994c7e) · [27 Oct 2023](https://etherscan.io/tx/0x1ebf82d51add7cfdfd40e8ea72b551271482646f423df1cddd37cac50ca374fc) | A chain · attribution [Unverified] | 16 Nov 2026 |
| Main wallet → Wintermute 1.5M, → Gate 103k | [Wintermute](https://etherscan.io/tx/0xda7c0bbce375328238e3388371cefca3f4a5672bf7e417968d92965a7ac39867) · [Gate](https://etherscan.io/tx/0xe7778171179cecfb9b7f87d699bdf97296bb0211cc742777f0a7d29f9a18c0af) | A | 16 Nov 2026 |
| 100M to `0x0585…`, paid out to 285+ addresses | [tx](https://etherscan.io/tx/0xa1ba1e98ba376709687c9139e792f20ec634b1ca237c65092bd95d1a3c3898a2) · [wallet](https://etherscan.io/address/0x0585a5e5aa9bf79e1788749d6b7ed08f87148122) | A chain · purpose [Unverified] | 16 Nov 2026 |
| No protocol revenue; treasury fee 0% | [Blockworks filing](https://blockworks.com/token-transparency/filing/origintrail) · [DefiLlama: not listed](https://api.llama.fi/summary/fees/origintrail?dataType=dailyFees) | B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Where is the 100M+ development treasury now?** | Trace `0x599c…`'s Snowbridge transfers to their AssetHub/NeuroWeb destination on Subscan; read Trace Labs-linked balances on Base and Gnosis | Free |
| 2 | **Who owns the 60M TRAC in `0x786b…a0c5`?** Arkham (16 Nov 2026) has no label | Trace the matching Snowbridge message back to its Polkadot/NeuroWeb sender on Subscan; ask Trace Labs | Free |
| 3 | **Are `0x66f7…` and `0x1430…` Trace Labs, contractors or buyers?** Arkham has no entity label (16 Nov 2026) | Funding history beyond TRAC (ETH gas sources, e.g. `0x66f7…`'s first funder `0x3372…`); ask Trace Labs | Free |
| 4 | **What was the 2021 `0x0585…` 100M payout?** | Search OriginTrail's 2021 announcements (staking/liquidity programs) against the 285 recipients | Free |
| 5 | **Publishing fee volume** | Read DKG V10 publishing/staking contracts on Base and Gnosis (Hub registry) or an official dashboard | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
