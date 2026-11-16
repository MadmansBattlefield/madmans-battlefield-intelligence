---
ticker: STBL
name: STBL
chain: bsc
contract: "0x8dedf84656fa932157e27c060d8613824e7979e3"
overall_score: 3.3
overall_verdict: FAIL
section_scores:
  revenue: 2
  foundation_team: 4
  insider_holdings: 3
  selling_behavior: 4
  tokenomics_supply: 3
  liquidity_market: 3
  product_development: 4
  adoption_customers: 2
  security_audits: 5
  regulatory: 5
  catalysts: 3
gates_failed: [revenue]
red_lines:
  hack_exploit: "none found"
  mint_path_live: "yes: only 700M of the 10B cap is minted on BNB Chain; the other 9.3B is issued on the project's revised schedule"
  team_wallet_to_exchange_during_pump: "not proven: BNB Chain transfers could not be read (BscScan API is paid; its pages sit behind a bot check)"
  entity_concentration: "project says vested tokens sit in central treasury wallets; about 95% of the 10B cap is not circulating"
price_usd: 0.02017
price_source: "CoinGecko, 16 Nov 2026 ~9:15 AM MST"
last_updated: 2026-11-16
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### STBL · Overall grade **3.3 / 10 · ❌ FAIL**

**Summary:** STBL is the governance token of a "Stablecoin 2.0" protocol. Users deposit tokenised real-world assets to mint USST, a dollar token, and a separate YLD NFT that keeps the yield. Only 500M of the 10B cap circulates (CoinGecko), so the $10M market cap sits under a **$202M FDV**. The project has rewritten its unlock schedule, and it releases tokens at its own discretion from central treasury wallets. No protocol fees are published, so the revenue gate fails.

**🚨 Top warning:** supply is released at the issuer's discretion. The tokenomics page says vested tokens "are held in the central STBL treasury wallets" and released "in step with protocol adoption". It also cut the Sep 2026–Aug 2027 schedule from 3.866B to 900M STBL ([tokenomics](https://www.stbl.com/tokenomics)). That is up to **9× the current circulating supply in one year**, released whenever the project decides. The token is on BNB Chain, which I could not trace with free tools. Every link is in the 🔗 Evidence trail below.

**Sections passed: 0 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 2/10 | ❌ FAIL (hard gate) |
| 🏛️ Foundation & team | 4/10 | ❌ FAIL |
| 🪙 Foundation / team holdings | 3/10 | ❌ FAIL |
| 📉 Selling behavior | 4/10 | ❌ FAIL (not proven) |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 3/10 | ❌ FAIL |
| 🧑‍💻 Product & development | 4/10 | ❌ FAIL |
| 🤝 Adoption & customers | 2/10 | ❌ FAIL |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 5/10 | ❌ FAIL |
| 📅 Catalysts & calendar | 3/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 STBL · STBL · 3.3 / 10 · ❌ FAIL

> **One line:** A $10M token with a $202M FDV whose unlocks the issuer controls.

| 📊 Market (CoinGecko, 16 Nov 2026 ~9:15 AM MST) | 🔗 On-chain (BNB Chain public RPC, 16 Nov 2026 ~9:20 AM MST) |
|---|---|
| **Price** $0.02017 | **Minted** 700,000,000 STBL (`totalSupply`) |
| **24h / 7d / 30d** 🟢 +2.5% / 🔴 −9.9% / 🔴 −9.9% | **Cap** 10,000,000,000 STBL |
| **Market cap** $10.1M · **FDV** $201.7M | **Circulating** 500M (CoinGecko; 5% of cap) |
| **24h volume** $1.22M (PancakeSwap V3 $0.51M, BTCC $0.19M, BloFin $0.11M, Toobit, MEXC, BingX) | **Holders / transfers** not read (BscScan wall) |
| **ATH** $0.5992 (24 Sep 2025) · now −96.6% | |
| **Pump days** 58 in the last year (largest +48.8% on 30 Dec 2025) | |

---

## 💰 Revenue — Does it make money? · 2/10 · ❌ FAIL (hard gate)

- DefiLlama has no protocol or fee record for STBL. Yield from the collateral goes to minters through YLD, not to STBL holders ([site](https://www.stbl.com/)). **2 → hard-gate FAIL.**

## 🏛️ Foundation & team — Who is in charge? · 4/10 · ❌ FAIL

- Leaders are described by role only. The founders extended their cliff by 15 months and investors by 12 months ([tokenomics](https://www.stbl.com/tokenomics)).

## 🪙 Foundation / team holdings — How many coins do they hold? · 3/10 · ❌ FAIL

- Allocation: team and advisors 25%, staking 20%, private and public sales 19%, treasury 15%, ecosystem 11%, liquidity and market making 10% ([tokenomics](https://www.stbl.com/tokenomics)). Vested tokens stay in central treasury wallets. Of the 700M minted, about 200M is not counted as circulating.

**Top holders on BNB Chain** ([Arkham token page](https://intel.arkm.com/explorer/token/stbl), [Tier B] Arkham, read 16 Nov 2026 (signed-in account); % of the 700M minted):

| Holder | STBL | % | Arkham label |
|---|---:|---:|---|
| `0x5437…BB3A3` | 197.49M | 28.2% | Unlabelled |
| Gate | 112.65M | 16.1% | Gate: Cold Wallet (exchange) |
| STBL_MFS | 74.39M | 10.6% | Project-named contract |
| stblgovernanc.eth | 52.72M | 7.5% | Project-named ENS |
| PancakeSwap V3 pool | 40.65M | 5.8% | DEX pool |

- The next holders are a Binance wallet proxy (4.4%) and Kraken, MEXC and KuCoin hot wallets.
- STBL_MFS and stblgovernanc.eth look like project wallets (18.1% together), though neither is tagged as treasury. The largest holder, `0x5437…BB3A3`, is unlabelled; the same address is also a top-5 holder of SHARE (see the SHARE report), so it is likely a custodian, launch platform or market maker rather than STBL's own treasury [Unverified].
- Concentration is high and the owner of the largest wallet is unknown. Holdings stays **3**.

## 📉 Selling behavior — Do insiders sell into pumps? · 4/10 · ❌ FAIL (not proven)

- BNB Chain transfers could not be read: Etherscan's free API doesn't cover BNB Chain, and BscScan pages return a bot check. Arkham's first page for the token shows only small exchange-wallet deposits and nothing from the pump window. I found no pump-day evidence either way. **Not proven → 4.**
- The project says that any "meaningful token activity" will be communicated, and that unlocks don't mean sales [Tier A, self-reported].

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

- 5% circulating. Tokenomics.com still lists a 211.7M unlock for 16 Nov 2026, but the project's revised schedule replaces it [conflicting sources].

## 💧 Liquidity & market · 3/10 · ❌ FAIL

- $1.22M of 24h volume. 42% is on one PancakeSwap pool, and the price is down 96.6% from ATH.

## 🧑‍💻 Product & development · 4/10 · ❌ FAIL

- USST minting and the YLD split are live on the dapp. ESS (ecosystem stablecoins) are still at the pitch stage.

## 🤝 Adoption & customers · 2/10 · ❌ FAIL

- USST supply and partner counts were not found in an independent source.

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- The site lists a smart-contract audit and a USST peg audit report. I did not review them. No exploit found.

## ⚖️ Regulatory · 5/10 · ❌ FAIL

- A stablecoin issuer using RWA collateral. No enforcement found, and licensing was not checked.

## 📅 Catalysts & calendar · 3/10 · ❌ FAIL

- Unlocks on the revised schedule run monthly through Aug 2027 (900M), and investors unlock in Sep 2027.

## 🚩 Red lines status

| Red line | Status |
|---|---|
| Hack / exploit | 🟢 None found |
| Team wallet → exchange during a pump | ⚪ Not proven (BNB Chain not traceable with free tools) |
| Live mint path | 🟠 9.3B left to issue on the issuer's schedule |
| Entity concentration | 🔴 ~95% of the cap held or unissued by the project |

## 📚 Sources

- [Tier A] [STBL tokenomics](https://www.stbl.com/tokenomics), [STBL site](https://www.stbl.com/)
- [Tier A] BNB Chain public RPC `totalSupply` = 700,000,000 (16 Nov 2026)
- [Tier A] CoinGecko `stbl` (market, venues, 365-day daily prices for pump days)
- [Tier B] [Tokenomics.com STBL unlocks](https://app.tokenomics.com/tokenomics/stbl/unlocks), [Bitrue unlock note](https://www.bitrue.com/blog/stbl-token-unlock)
- [Tier B] Arkham, read 16 Nov 2026 (signed-in account): token label STBL_Token; top holders from the [Arkham token page](https://intel.arkm.com/explorer/token/stbl) (Gate: Cold Wallet, STBL_MFS, stblgovernanc.eth, PancakeSwap V3 pool; 0x5437 unlabelled)

## 🔗 Evidence trail

*Every link below opens the primary record (block explorer, indexer, filing or official page) for the claim. Click through to check any number yourself.*

| Claim | Evidence link(s) | Tier | Date read |
|---|---|---|---|
| Revised unlocks, treasury custody | [tokenomics](https://www.stbl.com/tokenomics) | A | 16 Nov 2026 |
| 700M minted | [BscScan token page](https://bscscan.com/token/0x8dedf84656fa932157e27c060d8613824e7979e3) (RPC read) | A | 16 Nov 2026 |
| Market and venues | [CoinGecko](https://www.coingecko.com/en/coins/stbl) | A | 16 Nov 2026 |

---

## 🔎 Open items and how to close them

| # | Open item | Exactly how to close it | Cost / access |
|---|---|---|---|
| 1 | **Who owns `0x5437…BB3A3` (28.2%), and do the project wallets deposit on pump days** | Arkham (16 Nov 2026) leaves 0x5437 unlabelled. Trace STBL_MFS and stblgovernanc.eth transfers with a BNB Chain indexer | Free |
| 2 | **USST supply and collateral** | Read the USST peg audit report and on-chain supply | Free |

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.

- Research only. Not investment advice.
