---
ticker: BP
name: Backpack
chain: solana
mint: BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy
overall_score: 5.1
overall_verdict: FAIL
section_scores:
  revenue: 3
  foundation_team: 7
  insider_holdings: 2
  selling_behavior: 6
  tokenomics_supply: 3
  liquidity_market: 8
  product_development: 8
  adoption_customers: 6
  security_audits: 5
  regulatory: 7
  catalysts: 4
gates_failed: [revenue]
red_lines:
  mint_authority_used: not_used
  treasury_outflow_without_milestone_notice: none_since_tge
  holder_freeze: none_found
price_usd: 0.8097
price_source: "CoinGecko, 14 Nov 2026 12:13 PM MST"
chain_read_slot: 469447370
last_updated: 2026-11-14
layout_version: 3
---

## 🧾 QUICK REVIEW CARD

### BP · Overall grade **5.1 / 10 · ❌ FAIL**

**Summary:** A real, EU-licensed exchange whose token has no claim on the exchange's revenue. BP gives fee perks plus a conditional, non-voting equity election if Backpack ever has an exit. The 750M treasury has not moved since before launch, but Backpack still holds the mint and freeze keys and controls about 94% of supply.

**Sections passed: 6 of 11**

| Section | Score | Result |
|---|:---:|:---:|
| 💰 Revenue | 3/10 | ❌ FAIL |
| 🏛️ Foundation & team | 7/10 | ✅ PASS |
| 🪙 Foundation / team holdings | 2/10 | ❌ FAIL |
| 📉 Selling behavior | 6/10 | ✅ PASS |
| 📊 Tokenomics & supply | 3/10 | ❌ FAIL |
| 💧 Liquidity & market | 8/10 | ✅ PASS |
| 🧑‍💻 Product & development | 8/10 | ✅ PASS |
| 🤝 Adoption & customers | 6/10 | ✅ PASS |
| 🛡️ Security & audits | 5/10 | ❌ FAIL |
| ⚖️ Regulatory | 7/10 | ✅ PASS |
| 📅 Catalysts & calendar | 4/10 | ❌ FAIL |

*Pass = 6 or more out of 10. Full details for every section follow below.*

---


# 🪪 BP · Backpack · 5.1 / 10 · ❌ FAIL

> **One line:** A real, EU-licensed exchange whose token has no claim on the exchange's revenue. BP gives fee perks plus a conditional, non-voting equity election if Backpack ever has an exit. The 750M treasury has not moved since before launch, but Backpack still holds the mint and freeze keys and controls about 94% of supply.

| 📊 Market (CoinGecko + DexScreener, 14 Nov 2026 ~12:13–12:40 PM MST) | 🔗 On-chain (Solana RPC, slot 469,447,370) |
|---|---|
| **Price** $0.8097 (CoinGecko) · $0.8090 (Meteora BP/USDC) | **Mint** `BPxxfRCX…VBjPCy` · SPL · 9 decimals |
| **24h / 7d / 30d** 🔴 −3.2% / −13.3% / −20.5% | **Supply** 999,998,478.21 (999,998,643.70 on 10 Oct) |
| **Market cap** $202.4M · **FDV** $809.5M | **Mint authority** `GySF…MVH` ⚠️ **live** · **Freeze authority** same ⚠️ **live** |
| **24h volume** $4.73M | **Treasury** `GySF…` 750,000,000 (75.0%) |
| **ATH** $1.65 (1 Oct 2026) · now −51% | **Second Backpack multisig** `Eyzz…JiS` 189,217,622 (18.9%) |
| **Circulating (CoinGecko)** 250M | **Holders** 28,410 non-zero owners (10 Oct full read) |

---

## 💰 Revenue — Does it make money? · 3/10 · ❌ FAIL

| Metric | Value | Source |
|---|---|---|
| What BP is | A loyalty / utility token: fee and withdrawal discounts, launch access, extra USD yield, free wires, and an optional "Equity Purchase Election" | [Tier A] backpack.exchange/bp, BP Program FAQ ("Last Updated: March 2026") |
| Fee share, buyback or burn to BP holders | **None found** | [Tier A] (absence in FAQ and docs) |
| Supply change since 10 Oct | −165.49 BP | [Tier A] mint reads |
| Exchange revenue | **Not published**; no audited figures | [Unverified] |
| DefiLlama "Backpack SOL" (the staked-SOL token, not BP) | 30-day fees $24,722 · revenue $719 | [Tier A] DefiLlama `backpack-sol` |
| Equity election (if a "Backpack Exit Event" happens) | Base: tokens × 12.5% of equity ÷ 625M after 1 year of staking. Bonus 7.5% over 3 more years. Pool max 20%. Paid as **non-voting** shares in SPVs (Trek ESOP Ltd, BVI; a Blue Coral SPV). Backpack can redeem at a value it calculates, or end the program with 30 days' notice | [Tier A] BP Program FAQ (10 Oct read). The full Terms override it |

**What it means:** The business makes money, but none of it flows to BP today. The only path is a conditional equity election that depends on an IPO or sale that may never happen.

## 🏛️ Foundation & team — Who is in charge? · 7/10 · ✅ PASS

| Item | Finding | Source |
|---|---|---|
| Exchange operator | Trek Labs Ltd (BVI) | [Tier A] BP FAQ |
| Wallet operator | Blue Coral, Inc. (Delaware) | [Tier A] BP FAQ |
| Share counts fixed for equity program | 12,853,914 Trek Labs ordinary · 9,491,900 Blue Coral common (23 Feb 2026 snapshot) | [Tier A] BP FAQ |
| Treasury multisig | Squads v4 `Aj8j59RnzzMhNXqdCzjS2eR7G3hCqzRpEjrBhgozBxqf`, **3 of 5**, **time lock 0**. Members `DArE3uM9…`, `Ev8WSPQs…`, `29FjkS8E…`, `3pdzLa3b…`, `Daf3efsL…` | [Tier A] decoded account (10 Oct) |
| Second multisig | Squads v4 `9Qne3WM4…iC1`, **3 of 7**, shares signer `Ev8WSPQs…` | [Tier A] |
| CEO Armani Ferrante; Series A $17M (Placeholder) | Press and news only | [Unverified] |
| Insider tokens | "No token allocations to investors or insiders … The team receives nothing unless the company IPOs." | [Tier A] BP FAQ |

**What it means:** The legal entities are named, and the EU entity is on regulator registers. People and funding are known only from press.

## 🪙 Foundation / team holdings — How many coins do they hold? · 2/10 · ❌ FAIL

| Wallet | Role | 10 Oct 2026 | 14 Nov 2026 | % supply | Locked? |
|---|---|---:|---:|---:|---|
| `GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH` (token acct `2pWK2b…aU6s`) | Treasury: 37.5% pre-IPO + 37.5% post-IPO | 750,000,000 | 750,000,000 | 75.00% | 🔓 **No on-chain lock** (multisig, 0 time lock) |
| `EyzzXxQcR7NicVhMvHZy5DAeoCrxpCoY11pRneuysJiS` (acct `CBGt4r…aTKE`) | Backpack 3/7 multisig. Refills the hot wallet (see Selling) | 189,667,622 | 189,217,622 | 18.92% | 🔓 |
| `BbHG9GvPActFGogv3iNrpDAj4qpXr8t3jF16uGxXcKci` | Off-curve address, owner [Unverified] | 12,251,149 | 14,608,811 | 1.46% | ? |
| `43DbAvKxhXh1oSxkJSqGosNw3HpBnmsWiak6tB5wpecN` | High-traffic wallet (1,000 txs in <24h, 37,919 SOL). Likely the exchange hot wallet | — | 295,153 | 0.03% | 🔓 |

- Official schedule ([Tier A] backpack.exchange/bp): 25% at TGE (23 Mar 2026). The pre-IPO 37.5% is "progressively unlocked as Backpack hits regulatory, product, and market milestones", with **no dates and no milestone list**. The post-IPO 37.5% is "fully locked until 1 year post-IPO", **but only by promise**.

**What it means:** Backpack controls ~94% of supply, and the "lock" is a policy, not code.

## 📉 Selling behavior — Do insiders sell into pumps? · 6/10 · ✅ PASS

**Pump test:** 48 of 232 days since listing had a ≥10% 5-day rise (CoinGecko). The run was heaviest on 7–29 Sep 2026, up to +94%.

| Check | Result | Source |
|---|---|---|
| Treasury token account `2pWK2b…` | **4 transactions ever**, the last on **19 Mar 2026** (pre-TGE). No outflow since launch | [Tier A] `getSignaturesForAddress` |
| `Eyzz…` → `43Db…` (hot wallet) | 10,000,000 on **27 Sep 2026** (5-day **+44.1%**, tx `4XQ19an6pPVH…`) · 600k + 1.0M + 1.5M on 1 Oct · 1.5M 2 Oct · 4.0M 6 Oct · 1.0M 9 Oct · 150k 6 Nov · 300k 11 Nov. **Total 20.05M since TGE** | [Tier A] parsed transactions |
| Original funding of `Eyzz…` | 209,267,622 from `43Db…` on 21 Apr 2026 | [Tier A] |

- The `Eyzz…` ↔ `43Db…` pattern looks like exchange cold storage topping up the hot wallet, which would mean user withdrawals rather than sales. That role is **[Unverified]**. Backpack does not publish wallet labels.

**What it means:** The insider treasury has never moved. One 10M cold-to-hot transfer landed on a pump day. That is consistent with exchange custody, but it is not proven.

## 📊 Tokenomics & supply · 3/10 · ❌ FAIL

| Item | Value | Source |
|---|---|---|
| Supply | 999,998,478.21 (1B launch, small burns) | [Tier A] RPC |
| Mint authority | `GySF…MVH`, **not revoked**. Can create BP beyond 1B | [Tier A] RPC |
| Freeze authority | `GySF…MVH`, **not revoked**. Can freeze any holder | [Tier A] RPC |
| Metadata | `isMutable = true`, update authority `GySF…`. URI on `trek-labs.github.io` | [Tier A] 10 Oct read |
| Unlock schedule | Milestone-based, undated | [Tier A] docs |

**What it means:** The code lets one 3-of-5 multisig mint, freeze, and release 375M whenever it decides.

## 💧 Liquidity & market · 8/10 · ✅ PASS

| Pool | Pair | Liquidity | 24h volume | 24h buys / sells |
|---|---|---:|---:|---|
| Meteora `6qz7THwQvcjF3HyDGLuKaLBUk6EyJKeZXZMWLAeiwfjd` | BP/USDC | **$5,628,956** | $1,819,031 | 1,244 / 1,905 |
| Meteora `7o3bfXje…FDDa` | BP/SOL | $155,651 | $238,076 | 586 / 559 |
| Raydium `6gBdoi5w…yDe` | BP/USDC | $73,466 | $63,139 | 77 / 113 |
| All pools (30) | | ~$6.17M | | |

- CEX: Backpack Exchange ($1.21M 24h), LBank ($1.01M), MEXC ([Tier B] CoinGecko tickers).

## 🧑‍💻 Product & development · 8/10 · ✅ PASS

- Live: Backpack Exchange (spot, staking on-exchange, Backpack EU), Backpack Wallet, Backpack Securities (not US) ([Tier A] official site / FAQ, 10 Oct).
- BP staking is custodial on the exchange. No public on-chain staking program was found ([Tier A] learn.backpack.exchange).

## 🤝 Adoption & customers · 6/10 · ✅ PASS

- 28,410 non-zero on-chain holders (10 Oct). The exchange's user and volume numbers are not audited.
- The claim that Backpack handled "91% of Solana tokenized-stock trading on 2 Nov" comes from a social post ([Unverified]).

## 🛡️ Security & audits · 5/10 · ❌ FAIL

- No exchange-level hack found in primary records. The 7 Oct "trader key compromise" drain is from social posts only ([Unverified]).
- Mint, freeze and the 750M treasury sit with a 3-of-5 multisig with **0 time lock**.
- No token audit is needed for a standard SPL mint. The risk is in the keys, not the code.

## ⚖️ Regulatory · 7/10 · ✅ PASS

| Register | Entry | Source |
|---|---|---|
| CySEC | Licence **273/15** (23 Apr 2015), trade name "Backpack EU", **previous name FTX EU Ltd**. MiFID services incl. execution, dealing on own account, safekeeping | [Tier A] cysec.gov.cy register, fetched 10 Oct 2026 |
| ESMA interim MiCA register | "Trek Technologies" SIA, LEI 6488C2PNI17093U2YA18, Latvijas Banka, **authorised 27 May 2026**. Custody, exchange, execution, transfer. Passported to 29 EEA states | [Tier A] ESMA CASPS.csv, fetched 10 Oct 2026 |
| US | Fiat deposits and withdrawals not supported. Equity-election eligibility for US persons not confirmed | [Tier A] FAQ · [Unverified] |
| FTX EU sale (court order, $32.7M) | Press release / news only | [Unverified] |

## 📅 Catalysts & calendar · 4/10 · ❌ FAIL

| Date | Event | Effect |
|---|---|---|
| Undated | Pre-IPO milestone releases from the 375M tranche | Supply ↑ |
| Undated | Backpack Exit Event (IPO / sale) | Equity election becomes live |
| ≥ 23 Mar 2027 | Earliest date anyone could have 1 year of continuous staking, if staking opened at TGE (start date [Unverified]) | First eligibility for the base equity amount |

## 🚩 Red lines status

| Red line | Status | Evidence |
|---|---|---|
| Mint authority used (supply above 1B) | 🟢 Not used | Supply 999,998,478 |
| Treasury outflow without a milestone notice | 🟢 None since TGE | Last treasury tx 19 Mar 2026 |
| Holder account frozen | 🟢 None found | — |
| Equity program redeemed or terminated | 🟢 Not found | — |

## 📚 Sources

- [Tier A] Solana mainnet RPC: mint account, `getTokenAccountsByOwner`, `getSignaturesForAddress` and `getTransaction` for the treasury and `Eyzz…` accounts; slot ~469,447,370, 14 Nov 2026
- [Tier A] Prior forensic read, 10 Oct 2026 (full holder list; Squads multisig decode; CySEC and ESMA registers)
- [Tier A] [backpack.exchange/bp](https://backpack.exchange/bp) · BP Program FAQ · learn.backpack.exchange
- [Tier A] DefiLlama `backpack-sol`
- [Tier B] CoinGecko market data, tickers and daily closes · DexScreener pools, 14 Nov 2026
- [Unverified] Role of `Eyzz…` and `43Db…`; owner of `BbHG…`; CEO and funding rounds; FTX EU court documents; US eligibility; 91% tokenized-stock claim; 7 Oct drain

---

### How scores work

- Each section is scored **0–10** from the evidence on the page. **6 or more = ✅ PASS.** Under 6 = ❌ FAIL. "Not proven" counts as a fail.
- **Overall** = weighted average: Revenue ×3, Selling behavior ×2, Holdings ×1.5, Liquidity ×1.5, every other section ×1. Overall PASS needs **6.0 or more**.
- **Hard gates:** if Revenue or Selling behavior scores **3 or below**, the overall verdict is ❌ FAIL regardless of the average.
- **Pump day** = a daily close at least 10% above the close five days earlier. A team, foundation or treasury wallet selling (or funding a wallet that sells) on a pump day, without disclosure, fails Selling behavior.
- Sources: [Tier A] = primary (chain reads, official docs, filings, the DEX's own API). A fact needs 1 Tier A or 2 Tier B, or it is marked [Unverified]. Unknowns say "Not found" and what would answer them.
- Research only. Not investment advice.
