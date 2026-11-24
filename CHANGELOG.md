---
title: Changelog
last_updated: 2026-11-24
timezone: MST
disclaimer: Research only. Not financial advice. Not a recommendation to buy or sell. Not the work of a licensed fiduciary.
---

# Changelog

**Research only. Not financial advice.** Times are in **MST**.

This log records dated changes to the scoring methods, process rules, reported-only research elements, and published reports. It is a public summary of the desk's methodology history, written for readers of this repository. It is not a commit-by-commit git log, and it does not re-score published reports by itself.

Two scorecards appear in this project. They are not interchangeable:

- **v3 scorecard (this repository).** An 11-section, 0–10 grade on each published token report. [METHODOLOGY.md](METHODOLOGY.md) is the v3 rulebook. [HISTORY.md](HISTORY.md) tracks those published scores. As of the last publish on 17 November 2026, this tree holds **184** scored v3 reports.
- **Real Rails triage (currently v69).** A 0–100 first-pass ranking used to prioritize research. The v3 cover sheet describes it as the older triage script, not the grade on the published reports. Version stamps and before/after counts below come from dated ranking snapshots and the internal methodology log.

A project-growth narrative, with counts, is in [TIMELINE.md](TIMELINE.md).

---

## 2026-11-24 — ZBCN treasury advisory published (reported only; badge stays CAUTION)

Approved by Madman. No v3 score, badge, formula, gate, or `revenue_reaches_holders` change. The Real Rails treasury badge for ZBCN stays **CAUTION**, and the front-matter `last_updated` date was left as it was.

- **[ZBCN](banking-rails/ZBCN.md):** appended a dated 24 Nov 2026 (MST) "Treasury advisory" section after the research update. It contains:
  - the full evidence trail (wallets and transaction links) from the published treasury hub and its hop wallets to Nansen-labeled exchange deposit and hot wallets and to the Orca and Meteora pools;
  - the stablecoin feeder wallets;
  - the upstream reserve wallets;
  - a new free on-chain trace (H-22) of about 1.02B ZBCN sent from `71LxiE4P…` to `EsDV3m3x…` from June to November 2026, which followed all 19 recipients to their endpoints.
- **Vesting check:** the `71LxiE4P…` stream from a Zebec streaming-program account ended on 16 Mar 2026. That matches the report's last scheduled unlock, so the 2026 releases are already-unlocked inventory, not a new unlock.
- **Hypothesis:** the assumed purpose (a Zebec-side distribution or selling programme, possibly through a market maker or OTC desk) is labelled Unverified. Alternatives are listed, and the section says more investigation is needed.
- **Labels (rule P12):** Nansen labels are treated as leads from a single third-party labeler. Every balance and transfer figure was checked against direct Solana RPC reads, and all 28 linked transaction signatures were confirmed on-chain on 24 Nov 2026 (MST).
- **JSON:** `data/reports/ZBCN.json` was updated only in its `source_markdown` hash, byte count and extraction time.

---

## 2026-11-24 — Reported-only research updates: ZBCN Super App, the HSBC–Uber Canton pilot, and rails vs tokens

Approved by Madman. No v3 score, badge, formula, or `revenue_reaches_holders` change. Front matter `last_updated` dates on the four reports were left as they were.

New dated 24 Nov 2026 (MST) research sections were added to the published reports as reported-only appendices (after “How scores work”), from a desk review of official primary sources and clearly labelled Unverified leads:

- **[ZBCN](banking-rails/ZBCN.md):** official Super App launch dates (desktop late February 2026; mobile 17 Jul 2026); self-reported volume figures labelled Unverified, unaudited throughput, not revenue; the about $100k Q3 buyback as the only official revenue-linked dollar figure, held not burned; no published company or Super App revenue and no DefiLlama fees adapter found on 24 Nov 2026; marketing claims such as automatic fee conversion and “fully deflationary” noted as conflicting with paused burns and held inventory; official payroll-chain docs wording vs the report’s listed chains recorded as a discrepancy to reconcile (the listed chains were not silently changed); livestream claims including WisdomTree meetings and a Midnight partnership listed as Unverified leads. A rails-vs-tokens evidence table is included, with opinion flagged.
- **[CC](banking-rails/CC.md):** official 30 Oct 2026 HSBC–Uber Canton Network pilot facts (HSBC tokenized deposits, Franklin Templeton Benji money-market fund, Tradeweb, Fireblocks, delivery-versus-payment, a weekend partial redemption). Size is not disclosed. The 1.5-day duration is press-reported and Unverified as an official figure. The livestream hosts’ $1B / $110k pair is labelled an estimate, not a disclosed official figure. The official release does not state a CC fee or payout, so whether CC was burned in this pilot is Unverified. The report’s existing holder-accrual result was not changed.
- **[ONDO](banking-rails/ONDO.md) and [PLUME](banking-rails/PLUME.md):** short context lines only, pointing to the rails-vs-tokens comparison. Their revenue and holder-accrual findings are unchanged.

Primary sources are cited in the sections themselves (Zebec official blogs and docs, the HSBC joint release, Canton tokenomics, Tempo official fee docs, and PYMNTS where a figure is press-reported). YouTube is treated as a lead source, not a primary official publication.

---

## 2026-11-22 — Element #32, report updates, and a v69 triage rerun

Approved by Madman. The v69 score formula and component weights were not changed.

### Element #32 — Revenue / income stream in testing (reported only)

Adopted as methodology §12. A named fee, revenue or income mechanism counts only when a primary artifact exists (an improvement or governance proposal, merged code or a config flag, a testnet or sandbox release, a testnet contract, or the project's own beta page). Price talk and unsourced "could earn" claims stay Unverified leads and do not become Element #32 items.

Stages, always labelled "In testing, stage Rn", never as live revenue:

| Stage | Meaning |
|---|---|
| R0 | Proposed (draft spec or governance post only) |
| R1 | Spec approved by the relevant body |
| R2 | Code shipped in production, switched off |
| R3 | On a public test network or a closed hosted sandbox (say which) |
| R4 | Switched on for mainnet; fee published; little or no observed usage |
| R5 | Live revenue observed in a primary source |

Each item records who pays, where the money goes (burn, staking rewards, node rewards, treasury, company, or LPs), a value-accrual grade (Direct, Indirect, Weak, None, or Unverified), whether a fee level is set, and any dated target from the project. Targets go to the promises ledger and are scored only when due. No credit to token necessity, usage/revenue or promise delivery through R4. At R5, observed revenue enters the normal usage formula and the item graduates to "Live revenue." Items stuck at R2–R3 for more than 12 months are flagged "stalled" (report only).

A daily scan flag (REV-TEST) queues a primary-source check when a top-50 coin is named next to a revenue term and a stage term. The flag writes nothing into scores, badges, the ledger or report files until a reviewer proposes a stage and Madman approves it.

First items logged the same day: **HBAR CLPR** (R2 on mainnet, R3 in a closed sandbox; value accrual Indirect, small; HBAR's 0–100 score stayed 51.8) and **ICP Cloud Engines** (R4 early access; 20% of revenue to an ICP buy-and-burn in the Mission 70 whitepaper; value accrual Direct but small; launch status Unverified). **CRO** Prop 37 (100% of product revenue to a monthly buy-and-burn) was logged as a dated, unscored promise due 31 December 2026.

### Other 22 November approved research updates

- **HBAR fee routing** was corrected from primary sources (HIP-1259 and the mirror node): all fees go to account 0.0.802; the node fee goes to the submitting node and the rest splits about 80/10/10 to 0.0.98, 0.0.800 (staking rewards) and 0.0.801 (node rewards). Staking payouts are mostly reserve-funded; fees cover under 0.2%. Component values were not changed. The Hedera Council exit date was corrected to 30 September 2026 (it had been written as September 2025). A dated report note was added for the Council's non-binding letter of intent to acquire Hashgraph (11–12 November) and Apex Group joining the Council on 11 November.
- **INJ** circulating supply was set to 123,844,674 from the on-chain bank module; CoinGecko's 100M figure was flagged as wrong.
- **CFG** Ethereum supply was reconciled at 705,907,685; the same address holds 0 on the other checked chains. Legacy wrapped CFG remains partly in a probable migration escrow (Unverified).
- **APT:** about 2.2M burned per year vs about 54M unlocked per year; supply 1,211,972,831.
- **ONDO:** the 1.94B FIP-08 unlock (18 January 2027) was added to the promises ledger as an unscored dated item.
- **JST:** the 18 November buyback-mechanism change (reserves exhausted, revenue-funded buybacks, $50M buffer) was added as an unscored dated promise.
- **SKY:** a 19 November PSM outflow was documented as a dated report update. One address rotated about $1.49B from sUSDS and USDS through the PSM into Aave USDC between 8:46 and 10:05 AM MST; USDS supply fell from 5.23B to 3.29B that day. A 7-day, 750K USDS/day buyback announced 19 November was tracked as an unscored promise due about 27 November. No badge or 0–100 score change.
- **ENA:** issuer filings show 4.4M ENA sold in Q3 and no later sale through 16 November. Three unused wallets totalling 3,029.0M ENA have not moved since 9 July; the owner is Unverified. A conditional fee-switch / buyback (14-day average USDe supply at or above 7.5B; StablecoinX 8-K exhibit, 16 November; the Ethena vote itself Unverified) was tracked as an unscored promise with no calendar due date. No badge change.
- **PACT:** a dated advisory update was added (no new reserve outflow, no DAO vote). Two 11 November recipients were corrected from "fresh" to established addresses (in use since December 2025 and July 2026). The badge stayed Under Investigation.
- **Fact-check verdicts** updated from primary sources: SOL (Minna Bank) and ARB (Plume) to Confirmed; AXL (MAS), DOT (LCX) and TRAC (OriginTrail partners) to Partly true.
- **@CheekyCryptoPlus** was added to the daily video scan as lead-only: claims stay Unverified and never score; they may only queue a primary-source check.
- Coin reports were rebuilt. Unique coins written: **284** (each as Markdown and JSON, **568** files).

### v69 triage after the 22 November fixes

One rerun after the morning batch, and later reruns after the afternoon batches, used the unchanged v69 formula:

- SOL 62.6 → 62.9, still #1. AXL #31 39.2 → #26 40.1. TRAC #60 32.9 → #39 37.6. DOT #51 34.9 → #50 35.4. ARB #59 33.0 → #57 33.7.
- Top 10 unchanged. Top-50 entries: DOT, TRAC. Top-50 exits: RED (#49 → #51), ACH (#50 → #52).
- The two later reruns produced no further score or rank changes.
- An unlogged 18 November rebuild, from a dated-promise update, was found and written into the methodology log; one mid-list coin had already moved, with no formula change.

A 16 November weekly self-review had already recorded process-rule status keys for a 226-coin universe, confirmed no top-50 change from a live DefiLlama pull, and left several proposed upgrades unapplied.

---

## 2026-11-13 — Process rules P8–P11, and three display corrections

Approved by Madman. No score-formula or weight change. Methodology stayed **v69**. Live ranking files were not edited by these process additions.

Four process rules were added after a re-audit of the EDEL report:

- **P8 — Resolve every proxy before publishing.** Tighten P2: decode EIP-1167 and other minimal proxies, look up the implementation's verified name, and call the obvious view functions (`stakingToken`, `owner`, `token`, `asset`). Do not leave a proxy labelled "unidentified" if those checks can name it.
- **P9 — Staked or receipt-token positions count toward the depositor.** A transfer into a gauge, staking contract or vault is not by itself a transfer to a third party.
- **P10 — Snapshot figures after the last material event.** Price, market cap, FDV and other heading snapshot figures must be timestamped after the last material event in the report, or clearly flagged as pre-event.
- **P11 — Liquidity-move destination and announcement.** When liquidity moves, record the destination venue's creation date, transaction and creator, and whether an official announcement exists.

EDEL report wording was corrected; the 0–100 score stayed 21.3, rank #123, badge CAUTION. P8–P11 were not back-filled to other coins.

Earlier the same morning, three approved display and research corrections were applied, still with no formula change:

1. **EDEL (P2):** the attacker address was relabelled. At Ethereum block 26,405,684 (4:16:23 AM MST) it was EIP-7702 delegated to a verified EIP7702StatelessDeleGator implementation, not a plain first-use address.
2. **ZAMA (P1):** LayerZero peers were enumerated (BSC, Solana, HyperEVM, and Zama Gateway; Polygon has no OFT peer). Unique supply equals the Ethereum `totalSupply` of 11,391,483,307.901033 (4:21:47 AM MST). Remote tokens are backed by the adapter lock. That is 3.5589% above the 11 billion figure at admission to trading, consistent with documented inflation, not an unbacked bridge surplus. No surplus advisory and no score change.
3. **Fees and revenue line (P5, display only).** 83 of 84 DefiLlama-mapped coin reports gained a sourced line for 30-day and all-time fees and revenue (pull time 4:22:33 AM MST). EDEL already printed all four figures. v69 usage scores still use 30-day revenue and TVL. Ranking files were confirmed unchanged.

---

## 2026-11-12 — Process rules P1–P7

Approved by Madman after an outside audit of the 12 November 2026 EDEL report. Process rules only. **No score-formula or weight change.** Methodology stayed **v69**. The back-fill produced a proposed-corrections list; report text and live ranking files were not edited from that pass.

- **P1 — Bridge peer enumeration.** For a bridged or multi-chain token, enumerate every remote chain from the bridge or adapter contract itself, then cross-check CoinGecko platforms and, for the top 50, any wallet-label source already in use. Never flag a bridge surplus or shortfall until every identified peer's supply has been summed.
- **P2 — Address typing.** Never label an address as an EOA, a contract, a liquidity venue, a locker, or "unknown" without a code check and, where a free RPC or explorer exists, a creator or factory lookup. "Unlabelled" is not "EOA."
- **P3 — Documented sweep for absence claims.** A claim that something was not found needs a logged sweep of official posts, obvious keywords, and team-wallet outflows to known payout rails. An unlogged search cannot support a negative claim.
- **P4 — Latest-status rule.** Words such as paused, live, sunset or restarted require the latest official post about that product, not the most recent post already cited.
- **P5 — Standard source before calling a figure unsourced.** Dropping a number requires the same evidence as keeping it. For DefiLlama, pull both `dailyFees` and `dailyRevenue`.
- **P6 — Reconcile against prior research.** Load any prior dossier on the coin and confirm or explicitly overturn each prior finding before publishing.
- **P7 — Blind review of negative claims.** A second reviewer is given only the absent, unknown, unsourced or "not evidenced" lines and tries to disprove each one from primary sources.

---

## 2026-11-17 — Public v3 report fixes (this repository)

Last commit to `main` as of this writing. Three published-report changes:

- CoinGecko pump-day dates were corrected (stamp D = close of D−1) and a predecessor-ATH rule was added to [METHODOLOGY.md](METHODOLOGY.md).
- Confirmed report fixes after that date-convention patch were applied.
- ONDO: the 0xEA57 Coinbase payouts were treated as a proven one-hop sale.

[HISTORY.md](HISTORY.md) and the base-rate files were generated at 5:38–5:39 AM MST from the published v3 reports (universe: 184).

---

## 2026-11-16 — Public v3 upgrades, 184 scored reports, and catalog cleanup

The public tree grew from 27 scored notes (15 November, evening) to **184** published v3 reports, plus the not-a-token and dead lists. The [All Projects](banking-rails/ALL-PROJECTS.md) catalog was added (first published as 293 coins, then 292 after a duplicate of RISE was removed). As of 16 November it lists **184** scored reports, **15** not-a-token entries, and **93** dead or wound down (21 of those Unverified). **7** of the 184 reports pass; **177** fail.

The 16 November 2026 v3 methodology upgrades were published in this repository and applied to reports first published, or substantively updated, on or after that date. They do not re-score reports already on the ranking from before that date, except where a later commit says a named report was updated. The upgrades include:

- a machine-readable companion JSON next to each scored report
- Arkham label confidence
- pre-registered pump-day rules, including the later one-hop amendment (when a one-hop transfer counts as a proven sale)
- the holder-accrual test for revenue
- dual, blind review of Selling and Holdings
- score history and base rates
- the dead list and not-a-token list
- the reproducibility package

Passing reports were upgraded to the 16 November rules; SYRUP Revenue 7→5 on the holder-accrual test and lost its pass. Named Selling-gate or penalty updates from the upgrade batches are in the git history for this repository.

---

## 2026-11-15 — Public repository first published

The public GitHub repository was created on 14 November 2026 at 7:48 AM MST. The first commit landed on 15 November at 6:07 AM MST, with the research desk credited to **Sentinel**. The ranking already in that tree is dated 14 November and lists **18** scored v3 reports. A later 15 November commit added 9 reports (27 notes) and clickable evidence trails.

Twenty-six daily market reports, dated 16 October through 13 November 2026, were included in that first tree.

---

## 2026-11-10 — Real Rails ranking v69

Approved by Madman. Frozen snapshot dated 1:19 PM MST. Partner-claim routing, off-thesis disqualifications, a token value-accrual section, and any hack-math change were **not** approved and were not done.

Data fixes applied first: native-supply contracts restored for several bridged or mis-joined tickers; DefiLlama joins moved to a reviewed protocol map (181 symbols keep at least one protocol); licence false hits removed for four coins; 15 unsourced Confirmed claims re-linked to exact primary pages; 4 untraceable Confirmed claims downgraded to Unverified.

Rule changes (reviewer recommendations 1–7):

1. **Treasury score is badge-driven (Option B).** PASS 10, CAUTION 5, Under Investigation 1.5, Unverified 1.5, FAIL 0. The old colour scale (green 10 / yellow 5 / red 0 / missing 5) was retired. The top-50 gate now keys off a FAIL badge rather than a red colour.
2. **FAIL bar.** A new Under Investigation badge and advisory block. Four earlier FAILs (AVAX, PACT, DUSK, BKN) were re-checked against chance baselines and moved to Under Investigation, with a review reminder of 24 November 2026.
3. **Missing evidence uses one low default** (15% of each component's maximum). Every coin carries an evidence count (of 9) and a low–high range. **Watch tier:** fewer than 3 of 9 components evidenced → scored but unranked (70 coins; they were ranked in v68).
4. Hand overrides keep a reason, sources and date; reports show formula vs hand value.
5. Every ranking file and report is stamped **v69**. A fact-check validator treats a Confirmed claim without a primary link as Unverified for scoring.
6. A dated frozen snapshot and an outcomes log (hacks, verified dead or migrated names, drawdowns above 80%) were started.
7. A report-only language-layer pilot was opened on ZBCN and PLUME.

Results, v68 → v69: ranked 225 → **155**, plus **70** Watch; **812** disqualified (unchanged). Mean 0–100 score 35.0 → 26.4, mostly from the lower defaults and from 70 coins leaving the numbered list. Rank movements are in the internal methodology log; they are not v3 scores.

---

## 2026-11-09 — v66, v67, Elements #30–#31, and v68

Several approved changes landed the same day. None of them changed scan scores. Elements #30 and #31 are reported only; they have no score weight.

- **v66 (self-review).** Four fact-check upgrades from primary sources. BNKR moved #20 → #7 and ZK #47 → #45 on the 0–100 list. No top-50 entries or exits.
- **v67 scoring fixes A and B.** Each fact-check claim is assigned to exactly one score component, and hit ratios shrink toward the prior 0.25 by n/(n+3), stopping single-claim amplification. Negative DefiLlama 30-day revenue is clamped at 0 for the usage formula; the raw negative value is still stored. A proposed "Unverified-only creator record is neutral" change was **not** applied. Several top-50 members rotated vs v66.
- **Elements #30 and #31 (approved 1:04 PM MST, reported only).** #30 Real burn vs marketing burn: a claimed burn must show tokens at a burn address or a falling `totalSupply`, not just an announcement, a remint, or a burn of never-circulating treasury. #31 Unlock and inflation pressure: unlocks at 3, 6 and 12 months as a share of circulating supply, the emission rate, and who receives the tokens. Weighting proposals were recorded and not applied.
- **v68 (1:12 PM MST).** Midnight (**NIGHT**), Ethena (**ENA**) and Backpack (**BP**) went through the full pipeline and entered the provisional top 50 (ENA #19 48.5, NIGHT #24 46.8, BP #38 42.4; all CAUTION). Ranked coins: **225** (812 disqualified). Crypto Bellwether was **not** added to the daily video scan and remains an Unverified lead-only source.
- By 1:40 PM MST the burn and unlock checks were closed for all 225 ranked coins (reported only). A later quality check required a primary URL before a file could be marked done; files without one were set to partial or Unverified. Material 12-month unlock pressure at or above 20% included KTA 37.5%, RED 33.4%, PLUME 26.6%, CRO about 30%, and XPL 27%. Fake, paused or reminted burns flagged: PACT (unverifiable buyback), CRO (70B 2021 burn reminted in 2025), ZBCN (ZIP-4 pause).

---

## 2026-11-08 — Ledger correction, hack-response grading, and Element #29

Approved by Madman. Snapshots: v63 (ledger and hack-response), v64 (ORAI incident confirmed from official posts), v65 (evidence follow-up; zero score or rank changes).

- The dated-promise ledger math was corrected so Late or Partial items cannot raise a score, and Abandoned items pull a positive baseline down. Confirmed curated 2025–26 incidents cost −1 each. A flat −5 exploit penalty was rejected.
- The response rubric is conservative and symmetric, in the range [−2, +2], not an asymmetric bonus/penalty. Four dimensions (acknowledgement, containment, transparency, restitution) are graded modestly. Missing evidence is never treated as concealment. Any Unverified dimension makes the overall response grade Unverified and the adjustment 0.
- Primary sources were reopened for the qualifying incidents. Overall response grades remained Unverified (neutral) because acknowledgement timing, independent chain reconciliation and/or final restitution were still incomplete. This was a first evidence pass, not a completed hack-response audit. ORAI was confirmed from official posts in a follow-up (v64); MAPO's compensation workbook was not treated as independent proof of payment.
- **Element #29 — whole-core-team verification** (reported only). The personnel register widened from named leaders to the full listed executive set, founders, and every developer a project claims. Executives need a filing, registry officer record, regulator record or verified institutional bio; developers need verifiable commits. "Team unverifiable" is a red flag for the report, not a formula change.

---

## 2026-11-06 — Reported-only elements #22–#28, and the standing back-fill rule

Approved by Madman as evidence-only additions (no score effect), with a standing rule that every new research element is back-applied to all previously investigated projects. At that date the universe was 222 ranked plus 59 hand-reviewed non-ranked coins (**281**). Status is kept per element per coin; an element is complete only when all of them are done or marked n/a.

New reported-only elements: admin keys and upgrade or freeze authority; holder concentration; smart-contract audits; real yield (fees or revenue vs emissions); reserve attestations for stablecoins and tokenized assets; company-level litigation, enforcement, sanctions and jurisdiction.

Elements #1–#21 (screening, token necessity, usage and revenue, partners, licences, creator fact-check, decay, evidence tiers, the promise ledger, GitHub activity, treasury health, source re-open, deep hand review, legal-entity registries, team pages, the daily video scan, a confidence pass, on-chain treasury trails, whitepaper vs reality, the personnel register, and a recurring self-evaluation) were already in use. Several of those still had incomplete back-fill, which the standing rule requires to be finished rather than left as a top-50-only pass.

---

## 2026-11-03 — Real Rails first-pass triage (v60–v62)

Dated ranking snapshots v60, v61 and v62 were generated on 3 November 2026. Each has **222** ranked coins and **815** disqualified, with a note that scores are first-pass proxies from existing scans, fact-checks, connections and DefiLlama, not verified rankings, and that scan scores were unchanged. The internal element table dates screening, token necessity, usage, partners, licences, creator fact-check, decay, evidence tiers, the promise ledger, GitHub activity and the treasury rubric to this day (methodology v0.2 through v0.5). **1,037** coins were screened.

This changelog does not invent rule differences among v60, v61 and v62 beyond those dated snapshots.

---

## How this file will be updated

New methodology versions, process rules, reported-only elements, and approved report changes should be added at the top of the dated-entry list, in MST, after Madman approves them. [HISTORY.md](HISTORY.md) remains the place for published v3 score time-series. [TIMELINE.md](TIMELINE.md) remains the place for project-growth counts.
