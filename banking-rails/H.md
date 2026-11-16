---
ticker: H
name: Humanity Protocol
chain: ethereum
contract: "0xe76c5b78f93909d34404e9eb4c1f19e7582a5de1"
overall_score: 2.4
overall_verdict: FAIL
section_scores:
  revenue: 1
  foundation_team: 2
  insider_holdings: 2
  selling_behavior: 4
  tokenomics_supply: 1
  liquidity_market: 3
  product_development: 4
  adoption_customers: 3
  security_audits: 1
  regulatory: 5
  catalysts: 2
gates_failed: [revenue]
red_lines:
  hack_exploit: "yes, 8 Jun 2026: stolen keys used to mint ~100M H on BSC and move ~141M H on Ethereum; ~$31-36M drained"
  mint_path_live: "yes, uncapped owner mint() and owner burn(account) on the reissued token; owner is a 4-of-9 Safe"
  team_wallet_to_exchange_during_pump: "no large pump-day sale found; 70M H sent to a Bybit deposit on 2 Oct 2026 (not a pump day)"
  treasury_in_single_key_wallets: "yes, six EOAs hold ~7.84B H (78% of supply)"
price_usd: 0.01626398
price_source: "CoinGecko, 16 Nov 2026 8:34 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### H · Overall grade **2.4 / 10 · ❌ FAIL**

**Summary:** Humanity Protocol is a proof-of-personhood identity network. **On 8 Jun 2026 an attacker used keys stolen from one director's laptop to upgrade a bridge proxy, mint ~100M H on BNB Chain and move ~141M H on Ethereum, then sold it all and crashed the price ~89%** ([issuer's Quantstamp summary](https://www.humanity.org/hincidentupdate)). The project then reissued H as a new ERC-20, [`0xe76c…5de1`](https://etherscan.io/address/0xe76c5b78f93909d34404e9eb4c1f19e7582a5de1), airdropped 1:1. **The new contract has an uncapped `mint` and a `burn(account)` that lets the owner burn anyone's H.** The owner is a 4-of-9 Safe. Only ~2.16B of 10B H circulates, and ~286M unlocks every month into 2027. The price is −98% from its Jun 2026 ATH and −66% this week. There is no tracked revenue. Revenue trips the hard gate.

**🚨 Top warning:** Key-control failure, followed by a token that can still be minted or confiscated at will. Six single-key EOAs, all filled by the reissue distributor [`0xc2bc…189e`](https://etherscan.io/address/0xc2bc47b9293c3acc90c7c5da2f79c5136e16189e) on 16 Jun 2026, hold ~7.84B H (78% of supply). The 286M-H unlock due ~25 Nov 2026 is ~13% of circulating [Tier B ×2]. The largest wallet sent [70M H to a Bybit deposit address on 2 Oct 2026, not a pump day](https://etherscan.io/tx/0x678ac69d1be2228351b2d7bd0bb6f87d02ba6b77e4296e522ad3b5d5f7338924).

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 1/10 | ❌ FAIL |
| 🏛️ Foundation & team | 2/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL |
| 📊 Tokenomics & supply | 1/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 3/10 | ❌ FAIL |
| 🛡️ Security & audits | 1/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 2/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 H · Humanity Protocol · 2.4 / 10 · ❌ FAIL

> **One line:** A June 2026 key-theft exploit, a reissued token with unlimited admin mint and burn, and a heavy unlock calendar.

| 📊 Market (CoinGecko, 16 Nov 2026 8:34 AM MST) | 🔗 On-chain (Ethereum, 16 Nov 2026) |
|---|---|
| **Price** $0.01626 · 24h / 7d / 30d 🔴 −5.9% / −65.6% / −72.3% · 1y −89.9% | **ERC-20** [`0xe76c…5de1`](https://etherscan.io/address/0xe76c5b78f93909d34404e9eb4c1f19e7582a5de1) · 10,000,000,000 supply · 183,322 holders |
| **Market cap** $35.1M · **FDV** $162.6M · rank #517 | **Circulating** 2.16B (21.6%) |
| **24h volume** $3.36M: Gate $1.81M (54%), Bybit $0.36M, Toobit $0.30M | **Owner** Safe [`0xa7b3…9fdc`](https://etherscan.io/address/0xa7b36650621b413a36cbae0ae0676e41f4519fdc) (4-of-9); ProxyAdmin [`0xb3b3…ac90`](https://etherscan.io/address/0xb3b355a9bfc10073055100d36a05269ab888ac90) |
| **ATH** $0.8537 (2 Jun 2026) · now −98.1% | **Implementation** `HToken`: `mint` / `burn(account)` onlyOwner |

---

## 💰 Revenue — Does it make money? · 1/10 · ❌ FAIL

- DefiLlama lists Humanity (Identity & Reputation) with no fees, revenue or TVL [Tier A].
- No buyback or fee sharing to H holders.

**What it means:** no revenue. **1 (hard gate).**

## 🏛️ Foundation & team — Who is in charge? · 2/10 · ❌ FAIL

- Quantstamp's summary for the issuer found that one director's compromised Windows machine held the Ethereum operations key, all three BSC Safe signer keys and ~150 operational wallets ([humanity.org](https://www.humanity.org/hincidentupdate), Tier A; [CoinDesk](https://www.coindesk.com/tech/2026/06/09/humanity-s-usd36-million-exploit-happened-because-a-multisig-wallet-lived-on-one-laptop), Tier B).
- A recovery programme and the token reissue followed ([claim.humanity.org](https://claim.humanity.org/)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Wallet | H | % of supply | Type |
|---|---:|---:|---|
| [`0x302A…5016`](https://etherscan.io/address/0x302A72459cC96788def89595807f612eF7265016) | 2,572.28M | 25.7% | EOA ([Arkham: H Whale](https://intel.arkm.com/explorer/address/0x302A72459cC96788def89595807f612eF7265016)). Funds Sablier unlock streams; sent 70M to a Bybit Deposit |
| [`0xB712…6624`](https://etherscan.io/address/0xB7127a7343609c1d2D922Ea24660aB9c87176624) | 2,097.57M | 21.0% | EOA, untouched since 16 Jun 2026 |
| [`0xAd0a…6476`](https://etherscan.io/address/0xAd0aeE2cB3230B06991d7668bd5274C6c68F6476) | 1,800.00M | 18.0% | EOA, untouched |
| [`0x4302…133D`](https://etherscan.io/address/0x430253F6eDd32b0569B77c5E6910E57641E6133D) | 600.00M | 6.0% | EOA, untouched |
| [`0x04b1…D0Cc`](https://etherscan.io/address/0x04b1DeBd1d6F8B10D6D143dD980fF8AA90BAD0Cc) | 437.50M | 4.4% | EOA, untouched |
| [`0xee5B…047A`](https://etherscan.io/address/0xee5B5B923fFcE93A870B3104b7CA09c3db80047A) | 360.00M | 3.6% | **Exchange, not insider:** [Arkham: Bybit Hot Wallet](https://intel.arkm.com/explorer/address/0xee5B5B923fFcE93A870B3104b7CA09c3db80047A) (Bybit Proof of Reserves) |
| [`0x74c9…32b0`](https://etherscan.io/address/0x74c95762517fA53A4E65F57ff0B43C9E9b8232b0) | 332.18M | 3.3% | EOA, untouched |

- **Correction:** `0xee5B…047A` is a Bybit exchange hot wallet ([Tier B] Arkham, read 16 Nov 2026 (signed-in account)), not an insider EOA, and it was not among the distributor's 16 Jun 2026 transfers. The insider figure is **six EOAs holding 7,839.5M H (78.4%)**; the 7.8B total already left Bybit out, so Holdings stays **2**. Arkham labels the other six only "H Whale", with no allocation named. The distributor `0xc2bc…189e` (also "H Whale") made small transfers to Crypto.com and Bithumb hot wallets, consistent with crediting exchange users after the reissue.

*Balances: Blockscout holders API; EOA status from `eth_getCode`; funding from Etherscan v2 transfers (the six insider EOAs all from the reissue distributor, 16 Jun 2026, e.g. [2.77B to the largest wallet](https://etherscan.io/tx/0x59b184f6b818a4c887a473187c9ac376feeed73060516ef095f7c1720b0be2f9)).*

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL

*Gate H/USDT daily closes (UTC): 99 pump days in the last 365, spanning the old and new token.*

- Since the reissue, the largest wallet's outflows went to the stream creator [`0x4f3b…9875`](https://etherscan.io/address/0x4f3be262d1358a82b468cf81bfc5a9cc32cf9875), which forwarded 690.7M H into the [`0x93b3…BDCB`](https://etherscan.io/address/0x93b37Bd5B6b278373217333Ac30D7E74c85fBDCB) SablierLockup vesting contract. That is unlocks, not direct sales. One 3.06M transfer fell on a pump day (28 Sep 2026).
- **[70M H to a Bybit deposit address on 2 Oct 2026](https://etherscan.io/tx/0x678ac69d1be2228351b2d7bd0bb6f87d02ba6b77e4296e522ad3b5d5f7338924)** (Etherscan and Arkham label), not a pump day. A further [40M H went to the stream creator on 13 Nov 2026](https://etherscan.io/tx/0x3f69814234fd56fee5dbf27b939603e5ec9270b7544310a3c02e23554dcce090), during this week's crash.
- Stream recipients were not traced.

**What it means:** one direct exchange deposit of 70M; no pump-timed dumps found. **4**.

## 📊 Tokenomics & supply · 1/10 · ❌ FAIL

- 10B cap in the token sale terms, but **the contract has no cap**: `mint(address,uint256)` and `burn(address,uint256)` are `onlyOwner` (verified `HToken` source on Blockscout). The owner Safe needs 4 of 9 signatures.
- 21.6% circulating; ~286M H unlocks a month through 2027 [Tier B ×2] ([AInvest](https://www.ainvest.com/news/humanity-protocol-slides-24-0-037-monthly-unlock-clock-stacks-supply-post-hack-decline-2611/) · [Kriptosignal](https://kriptosignal.net/en/daily-losers-humanity-sheds-a-quarter-pepe-drops-15-and-bitway-pays-for-the-pump/)).

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $3.36M of 24h volume, 54% on Gate. FDV is 4.6× market cap.
- −98% from ATH; −66% in 7 days.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- Palm-scan proof of humanity and zkTLS credentials; mainnet live [Tier B]. No fee-generating usage visible.

## 🤝 Adoption & customers · 3/10 · ❌ FAIL

- 183,322 token holders (largely the 1:1 airdrop base). No published active-user or verification metrics checked this pass.

## 🛡️ Security & audits · 1/10 · ❌ FAIL

- **8 Jun 2026 exploit:** ~141.18M H moved on Ethereum, ~100M H minted on BSC, ~$31–36M taken; Quantstamp tied it to a DPRK-style intrusion ([issuer summary](https://www.humanity.org/hincidentupdate), Tier A; [crypto.news](https://crypto.news/humanity-protocol-sets-new-h-airdrop-after-36m-exploit/), Tier B).
- The reissued token keeps the same owner-mint power, now behind a 4-of-9 Safe.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- Biometric-identity data carries privacy-law exposure. The project publishes a MiCA legal statement. No enforcement found.

## 📅 Catalysts & calendar · 2/10 · ❌ FAIL

| Date | Event |
|---|---|
| ~25 Nov 2026 | ~286M H unlock (≈13% of circulating) |
| Monthly through 2027 | ~286M H unlocks |

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🔴 8 Jun 2026 key compromise, ~$31–36M |
| Team wallet → exchange during a pump | 🟡 70M H to Bybit (not a pump day); no pump-timed dumps found |
| Live mint path | 🔴 Uncapped owner mint and burn-from-any-address |
| Treasury in single-key wallets | 🔴 ~7.84B H in 6 EOAs |

## 📚 Sources

- [Tier A] Blockscout token / holders / verified source; Etherscan v2 transfers; Ethereum RPC (`owner`, ProxyAdmin owner, Safe `getThreshold`), read 16 Nov 2026 ~11:25 AM MST
- [Tier A] [Humanity incident summary (Quantstamp)](https://www.humanity.org/hincidentupdate) · [recovery programme](https://claim.humanity.org/)
- [Tier B] [CoinDesk](https://www.coindesk.com/tech/2026/06/09/humanity-s-usd36-million-exploit-happened-because-a-multisig-wallet-lived-on-one-laptop) · [crypto.news](https://crypto.news/humanity-protocol-sets-new-h-airdrop-after-36m-exploit/) · [AInvest](https://www.ainvest.com/news/humanity-protocol-slides-24-0-037-monthly-unlock-clock-stacks-supply-post-hack-decline-2611/) · [Kriptosignal](https://kriptosignal.net/en/daily-losers-humanity-sheds-a-quarter-pepe-drops-15-and-bitway-pays-for-the-pump/)
- [Tier A] CoinGecko `humanity` (16 Nov 2026 8:34 AM MST); DefiLlama `humanity`; Gate H/USDT daily candles
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): Bybit Hot Wallet on 0xee5B; Bybit Deposit for the 70M; H Whale tags on the six insider EOAs and the distributor; Sablier lockup contracts; owner Safe 0xa7b3 as a Gnosis Safe

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Owner mint / burn functions | [implementation](https://etherscan.io/address/0x85D0B85f290ba575c50a6be38f24F9e99F94E7D3#code) | A | 16 Nov 2026 |
| Owner is a 4-of-9 Safe | [Safe](https://etherscan.io/address/0xa7b36650621b413a36cbae0ae0676e41f4519fdc) | A | 16 Nov 2026 |
| 70M H to a Bybit deposit | [tx](https://etherscan.io/tx/0x678ac69d1be2228351b2d7bd0bb6f87d02ba6b77e4296e522ad3b5d5f7338924) | A | 16 Nov 2026 |
| Reissue distribution to top EOAs | [tx](https://etherscan.io/tx/0x59b184f6b818a4c887a473187c9ac376feeed73060516ef095f7c1720b0be2f9) | A | 16 Nov 2026 |
| June 2026 exploit | [issuer summary](https://www.humanity.org/hincidentupdate) · [CoinDesk](https://www.coindesk.com/tech/2026/06/09/humanity-s-usd36-million-exploit-happened-because-a-multisig-wallet-lived-on-one-laptop) | A + B | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Allocation labels for the six insider EOAs** | Arkham (16 Nov 2026) tags them only "H Whale". Ask Humanity Protocol to publish its allocation wallets | Free |
| 2 | **Who owns the six EOAs** | Match them to the allocation table (team, investors, foundation, ecosystem) via Arkham or the project | Free |
| 3 | **Sablier stream recipients** | List the streams in the SablierLockup funded by `0x4f3b…9875` and trace whether recipients deposit to exchanges on pump days | Free |
| 4 | **Will the mint be capped?** | Ask the project to renounce or cap `mint` and remove `burn(account)` | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
