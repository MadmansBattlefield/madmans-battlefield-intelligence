# Vetted public sources

Checked 12 October 2026. Times in this repository are in **MST**.

Tiers: **A** = primary or official data · **B** = reputable journalism · **C** = opinion or hype (kept separate and labeled).

A fact is treated as **verified** only if it has one Tier A source or is carried by two Tier B outlets. Everything else is labeled **unverified**.

## 1. Primary data (Tier A)

| Source | URL | Feed / access | Frequency | Conflicts |
|---|---|---|---|---|
| SEC press releases | [sec.gov/newsroom](https://www.sec.gov/newsroom) | [RSS](https://www.sec.gov/news/pressreleases.rss) | Business days | None (regulator) |
| CFTC general press | [cftc.gov](https://www.cftc.gov) | [RSS](https://www.cftc.gov/RSS/RSSGP/rssgp.xml) | Several a week | None |
| CFTC enforcement | [cftc.gov](https://www.cftc.gov) | [RSS](https://www.cftc.gov/RSS/RSSENF/rssenf.xml) | Weekly | None |
| Federal Reserve (all press) | [federalreserve.gov](https://www.federalreserve.gov) | [RSS](https://www.federalreserve.gov/feeds/press_all.xml) | Daily | None |
| Coinbase status | [status.coinbase.com](https://status.coinbase.com) | [RSS](https://status.coinbase.com/history.rss) | When incidents happen | Self-reported |
| Kraken status | [status.kraken.com](https://status.kraken.com) | [RSS](https://status.kraken.com/history.rss) | When incidents happen | Self-reported |
| Kraken blog | [blog.kraken.com](https://blog.kraken.com) | [RSS](https://blog.kraken.com/feed) | Weekly | Company PR |
| Ethereum Foundation blog | [blog.ethereum.org](https://blog.ethereum.org) | [RSS](https://blog.ethereum.org/feed.xml) | Weekly | Protocol PR |
| Solana news | [solana.com/news](https://solana.com/news) | [RSS](https://solana.com/news/rss.xml) | Weekly | Foundation PR |
| Coinbase blog | [coinbase.com/blog](https://www.coinbase.com/blog) | Public RSS has been unreliable (403 or empty); use the site | Weekly | Company PR |
| Binance announcements / status | [binance.com support](https://www.binance.com/en/support/announcement) | Often bot-blocked | Daily | Company PR, regulatory history |
| DefiLlama (TVL, fees, unlocks, hacks) | [defillama.com](https://defillama.com) | Free JSON API: `api.llama.fi/protocols`, `api.llama.fi/hacks` | Live | Open-source, low |
| mempool.space (Bitcoin chain) | [mempool.space](https://mempool.space) | Free API `/api/blocks/tip/height` | Live | Low |
| Etherscan / Solscan explorers | [etherscan.io](https://etherscan.io), [solscan.io](https://solscan.io) | Free-tier API may need a key | Live | Show ads / sponsored tokens |
| Chainalysis blog | [chainalysis.com/blog](https://www.chainalysis.com/blog) | [RSS](https://blog.chainalysis.com/feed/) | Weekly | Sells to governments and exchanges |
| Glassnode Insights | [insights.glassnode.com](https://insights.glassnode.com) | Often 403 to automated fetch; use a browser | Weekly | Paid-product upsell |
| CoinGecko | [coingecko.com](https://www.coingecko.com) | Public price API | Live | Aggregator |
| DexScreener | [dexscreener.com](https://dexscreener.com) | Public pool API | Live | Aggregator |

## 2. Hack and exploit trackers

| Source | URL | Feed | Freq | Tier / notes |
|---|---|---|---|---|
| DefiLlama Hacks | [defillama.com/hacks](https://defillama.com/hacks) | JSON `api.llama.fi/hacks` | Live | A- (aggregated, cites sources) |
| rekt.news | [rekt.news](https://rekt.news) | [RSS](https://rekt.news/rss/feed.xml) | A few a week | B. Post-mortems, snarky tone |
| SlowMist | [slowmist.medium.com](https://slowmist.medium.com) | [RSS](https://slowmist.medium.com/feed) | Weekly | B+. Security firm, sells audits |
| PeckShield | [x.com/PeckShieldAlert](https://x.com/PeckShieldAlert) | Medium feed is rarely updated; X is fastest | Real-time on X | B+. Sells audits |
| CertiK Alert | [x.com/CertiKAlert](https://x.com/CertiKAlert) | No reliable public RSS | Real-time | B. Sells audits; past "audited then hacked" criticism |

## 3. News outlets (Tier B)

| Source | Feed | Freq | Conflicts |
|---|---|---|---|
| CoinDesk | [RSS](https://www.coindesk.com/arc/outboundfeeds/rss/) | Hourly | Owned by Bullish (exchange) since 2023 |
| The Block | [RSS](https://www.theblock.co/rss.xml) | Hourly | Ex-CEO's undisclosed SBF/Alameda loans (2022). Now disclosed |
| Blockworks | [RSS](https://blockworks.co/feed) | Hourly | Runs paid research and events |
| DL News | [RSS](https://www.dlnews.com/arc/outboundfeeds/rss/) | Hourly | Fairly independent (journalist-led) |
| Decrypt | [RSS](https://decrypt.co/feed) | Hourly | Spun out of ConsenSys origins |
| The Defiant | [RSS](https://thedefiant.io/feed) | Daily | DeFi-friendly slant |
| Unchained (Laura Shin) | [RSS](https://unchainedcrypto.com/feed/) | Daily | Sponsors disclosed |
| Reuters crypto | No official RSS. Workaround: [Google News query](https://news.google.com/rss/search?q=crypto+site:reuters.com) | Daily | Gold standard. Feed is Google-aggregated |
| Bloomberg crypto | Official feed has been empty; Google News query `crypto site:bloomberg.com` | Daily | Paywall |
| FT crypto | [RSS](https://www.ft.com/cryptocurrencies?format=rss) | Daily | Paywall |
| Cointelegraph | [RSS](https://cointelegraph.com/rss) | Hourly | Tier B-/C. Past paid-content and fake-headline incidents. Verify everything |

## 4. Unlock and catalyst calendars

| Source | Access | Tier |
|---|---|---|
| Tokenomist (ex-TokenUnlocks) [tokenomist.ai](https://tokenomist.ai) | Website; automated fetch is often blocked. No public RSS found | A-. Compiled from vesting contracts and docs |
| DefiLlama Unlocks [defillama.com/unlocks](https://defillama.com/unlocks) | Website + API | A- |
| Fed FOMC calendar [federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) | Official | A |
| SEC / CFTC feeds above, for ETF decisions and rule actions | RSS | A |

## 5. Opinion and newsletters (Tier C unless noted)

| Source | Access | Freq | Tier / conflicts |
|---|---|---|---|
| Bankless | [RSS](https://www.bankless.com/rss/feed) | Daily | C+. Founders invest in projects they cover. Bullish ETH bias |
| Milk Road | Site; `/feed` has been empty | Daily | C. Ad and affiliate driven, hype tone |
| Altcoin Daily (YouTube) | [channel](https://www.youtube.com/channel/UCbLhGKVY-bJPcawebgtNfbw), [RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCbLhGKVY-bJPcawebgtNfbw) | ~Daily | C. Affiliate exchange promotions |
| The Block Daily, CoinDesk newsletters, Blockworks Daily, Unchained Daily | Signup on each publisher's site | Daily | Same tier as the parent outlet |

## Avoid or treat as hype-only

- Telegram or Discord "signal" groups, and DMs claiming to be a channel host (common scam pattern).
- Paid press-release wires reprinted as news (for example "PRNewswire / Chainwire / sponsored" posts on aggregators).
- Influencer YouTube or X price calls without on-chain or official backing (Tier C at best).
- Sites with past fabricated or paid stories (Cointelegraph needs a second source; skip low-tier aggregators such as U.Today and CoinGape for facts).
- Unverified "whale alert" style X accounts unless they link to an explorer transaction.

## How these sources are used in the daily brief

1. Official (A): SEC, CFTC, Fed, exchange status pages, and protocol blogs, from the last 24 hours.
2. Security: DefiLlama hacks, rekt, SlowMist, PeckShield / CertiK on X.
3. News (B): CoinDesk, The Block, Blockworks, DL News, and Reuters. A story is confirmed only if two Tier B outlets carry it or it has an A source.
4. Calendar: unlocks from DefiLlama / Tokenomist, plus FOMC.
5. Hype corner (C), clearly labeled: Altcoin Daily, Bankless, Milk Road.
