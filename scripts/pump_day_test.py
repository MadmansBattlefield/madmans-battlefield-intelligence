#!/usr/bin/env python3
"""Re-run the pre-registered pump-day test from public daily-close APIs.

A pump day is a UTC daily close at least 10% above the close five calendar
days earlier. This script does not score a token and does not change any
published report. It only prints (or writes) the days that meet the test.

Price-source hierarchy (use the first that returns a usable series):

  1. Binance USDT (or USD) daily klines, when reachable
  2. Gate.io
  3. MEXC
  4. KuCoin
  5. Kraken
  6. CoinGecko daily closes, last resort, and only when named.
     CoinGecko daily points stamped 00:00 UTC on day D are the close of D-1.
     Prefer exchange klines (Gate, then MEXC, then KuCoin) when Binance is unreachable.

Usage (from the repository root):

    python3 scripts/pump_day_test.py --exchange mexc --pair ZANOUSDT --start 2025-11-16 --end 2026-11-16
    python3 scripts/pump_day_test.py --exchange kraken --pair SHXUSD --start 2026-01-01 --end 2026-11-16
    python3 scripts/pump_day_test.py --csv /path/to/daily_closes.csv --date-col date --close-col close

CSV input must already be UTC daily closes (date, close). No API call is made.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

UTC = timezone.utc
LOOKBACK_DAYS = 5
THRESHOLD = 0.10
UA = "MadmansBattlefieldIntelligence/pump-day-test (+https://github.com/MadmansBattlefield/madmans-battlefield-intelligence)"


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def is_pump(close_t: float, close_t_minus_5: float) -> bool:
    if close_t_minus_5 <= 0 or close_t <= 0:
        return False
    return close_t >= close_t_minus_5 * (1.0 + THRESHOLD)


def pct_change(close_t: float, close_t_minus_5: float) -> float | None:
    if close_t_minus_5 <= 0:
        return None
    return (close_t / close_t_minus_5) - 1.0


def _get_json(url: str, timeout: int = 30) -> object:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def from_rows(rows: list[tuple[date, float]]) -> list[dict]:
    rows = sorted((d, c) for d, c in rows if c is not None)
    by_date = {d: c for d, c in rows}
    out = []
    for d, close in rows:
        prior = by_date.get(d - timedelta(days=LOOKBACK_DAYS))
        if prior is None:
            continue
        change = pct_change(close, prior)
        flag = is_pump(close, prior)
        out.append(
            {
                "date_utc": d.isoformat(),
                "close": close,
                "close_5d_earlier": prior,
                "change_pct": None if change is None else round(change * 100, 4),
                "pump_day": flag,
            }
        )
    return out


def load_csv(path: Path, date_col: str, close_col: str) -> list[tuple[date, float]]:
    rows = []
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for rec in reader:
            d = parse_date(str(rec[date_col])[:10])
            rows.append((d, float(rec[close_col])))
    return rows


def fetch_binance(pair: str, start: date, end: date) -> list[tuple[date, float]]:
    # pair like BTCUSDT
    params = {
        "symbol": pair.upper(),
        "interval": "1d",
        "startTime": int(datetime(start.year, start.month, start.day, tzinfo=UTC).timestamp() * 1000),
        "endTime": int(datetime(end.year, end.month, end.day, 23, 59, tzinfo=UTC).timestamp() * 1000),
        "limit": 1000,
    }
    url = "https://api.binance.com/api/v3/klines?" + urlencode(params)
    data = _get_json(url)
    rows = []
    for item in data:
        d = datetime.fromtimestamp(item[0] / 1000, tz=UTC).date()
        rows.append((d, float(item[4])))
    return rows


def fetch_gate(pair: str, start: date, end: date) -> list[tuple[date, float]]:
    # pair like BTC_USDT
    if "_" not in pair:
        # Accept BTCUSDT and split common quote suffixes
        p = pair.upper()
        for quote in ("USDT", "USD", "USDC"):
            if p.endswith(quote) and len(p) > len(quote):
                pair = f"{p[:-len(quote)]}_{quote}"
                break
    params = {
        "currency_pair": pair.upper(),
        "interval": "1d",
        "from": int(datetime(start.year, start.month, start.day, tzinfo=UTC).timestamp()),
        "to": int(datetime(end.year, end.month, end.day, 23, 59, tzinfo=UTC).timestamp()),
        "limit": 1000,
    }
    url = "https://api.gateio.ws/api/v4/spot/candlesticks?" + urlencode(params)
    data = _get_json(url)
    rows = []
    for item in data:
        # [timestamp, volume quote, close, high, low, open, volume base, ...]
        d = datetime.fromtimestamp(int(item[0]), tz=UTC).date()
        rows.append((d, float(item[2])))
    return rows


def fetch_mexc(pair: str, start: date, end: date) -> list[tuple[date, float]]:
    params = {
        "symbol": pair.upper().replace("_", "").replace("-", ""),
        "interval": "1d",
        "startTime": int(datetime(start.year, start.month, start.day, tzinfo=UTC).timestamp() * 1000),
        "endTime": int(datetime(end.year, end.month, end.day, 23, 59, tzinfo=UTC).timestamp() * 1000),
        "limit": 1000,
    }
    url = "https://api.mexc.com/api/v3/klines?" + urlencode(params)
    data = _get_json(url)
    rows = []
    for item in data:
        d = datetime.fromtimestamp(item[0] / 1000, tz=UTC).date()
        rows.append((d, float(item[4])))
    return rows


def fetch_kucoin(pair: str, start: date, end: date) -> list[tuple[date, float]]:
    p = pair.upper().replace("_", "-")
    if "-" not in p:
        for quote in ("USDT", "USD", "USDC"):
            if p.endswith(quote) and len(p) > len(quote):
                p = f"{p[:-len(quote)]}-{quote}"
                break
    params = {
        "symbol": p,
        "type": "1day",
        "startAt": int(datetime(start.year, start.month, start.day, tzinfo=UTC).timestamp()),
        "endAt": int(datetime(end.year, end.month, end.day, 23, 59, tzinfo=UTC).timestamp()),
    }
    url = "https://api.kucoin.com/api/v1/market/candles?" + urlencode(params)
    payload = _get_json(url)
    data = payload.get("data") if isinstance(payload, dict) else payload
    rows = []
    for item in data or []:
        # [time, open, close, high, low, volume, turnover]
        d = datetime.fromtimestamp(int(item[0]), tz=UTC).date()
        rows.append((d, float(item[2])))
    return rows


def fetch_kraken(pair: str, start: date, end: date) -> list[tuple[date, float]]:
    params = {"pair": pair.upper(), "interval": 1440, "since": int(datetime(start.year, start.month, start.day, tzinfo=UTC).timestamp())}
    url = "https://api.kraken.com/0/public/OHLC?" + urlencode(params)
    payload = _get_json(url)
    if payload.get("error"):
        raise RuntimeError(f"Kraken error: {payload['error']}")
    result = payload.get("result") or {}
    series = None
    for key, val in result.items():
        if key != "last":
            series = val
            break
    rows = []
    end_ts = datetime(end.year, end.month, end.day, 23, 59, tzinfo=UTC).timestamp()
    for item in series or []:
        ts = int(item[0])
        if ts > end_ts:
            continue
        d = datetime.fromtimestamp(ts, tz=UTC).date()
        rows.append((d, float(item[4])))
    return rows


def fetch_coingecko(coin_id: str, start: date, end: date) -> list[tuple[date, float]]:
    # CoinGecko market_chart from-to uses unix seconds.
    # A daily point stamped 00:00 UTC on day D is the price at the start of
    # day D, which is the UTC close of day D-1. Label it as D-1.
    # Intra-day samples (hourly or a live tick) stay on their calendar date.
    # Request through 00:00 UTC of end+1 so the midnight stamp that is end's
    # close is included, then drop any partial current-day point.
    today = datetime.now(UTC).date()
    params = {
        "vs_currency": "usd",
        "from": int(datetime(start.year, start.month, start.day, tzinfo=UTC).timestamp()),
        "to": int(datetime(end.year, end.month, end.day, tzinfo=UTC).timestamp()) + 86400,
    }
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?" + urlencode(params)
    try:
        payload = _get_json(url)
    except HTTPError as exc:
        # The public range endpoint often returns 401/429 on long windows.
        # Fall back to daily market_chart, which uses the same midnight stamps.
        if exc.code not in (401, 403, 429):
            raise
        days = min(max((end - start).days + 2, 1), 365)
        fallback = (
            f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?"
            + urlencode({"vs_currency": "usd", "days": days, "interval": "daily"})
        )
        payload = _get_json(fallback)
    # Keep the latest sample for each mapped close date.
    by_date: dict[date, tuple[datetime, float]] = {}
    for ts_ms, price in payload.get("prices") or []:
        dt = datetime.fromtimestamp(ts_ms / 1000, tz=UTC)
        if dt.hour == 0 and dt.minute == 0 and dt.second == 0 and dt.microsecond == 0:
            d = dt.date() - timedelta(days=1)
        else:
            d = dt.date()
        if d < start or d > end or d >= today:
            continue
        prev = by_date.get(d)
        if prev is None or dt >= prev[0]:
            by_date[d] = (dt, float(price))
    return [(d, rec[1]) for d, rec in sorted(by_date.items())]


FETCHERS = {
    "binance": fetch_binance,
    "gate": fetch_gate,
    "mexc": fetch_mexc,
    "kucoin": fetch_kucoin,
    "kraken": fetch_kraken,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exchange", choices=sorted(FETCHERS) + ["coingecko"], help="Public API to read daily closes from")
    parser.add_argument("--pair", help="Market pair as the exchange names it (BTCUSDT, BTC_USDT, SHXUSD, BTC-USDT)")
    parser.add_argument("--coingecko-id", help="CoinGecko id, only with --exchange coingecko")
    parser.add_argument("--start", help="Start date YYYY-MM-DD (UTC)")
    parser.add_argument("--end", help="End date YYYY-MM-DD (UTC)")
    parser.add_argument("--csv", type=Path, help="Read UTC daily closes from a CSV instead of an API")
    parser.add_argument("--date-col", default="date")
    parser.add_argument("--close-col", default="close")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a table")
    parser.add_argument("--out", type=Path, help="Write JSON to this path")
    args = parser.parse_args(argv)

    if args.csv:
        rows = load_csv(args.csv, args.date_col, args.close_col)
        source = f"csv:{args.csv}"
    else:
        if not args.exchange or not args.start or not args.end:
            parser.error("API mode needs --exchange, --start and --end (or pass --csv)")
        start, end = parse_date(args.start), parse_date(args.end)
        try:
            if args.exchange == "coingecko":
                if not args.coingecko_id:
                    parser.error("--coingecko-id is required with --exchange coingecko")
                rows = fetch_coingecko(args.coingecko_id, start, end)
                source = f"coingecko:{args.coingecko_id}"
            else:
                if not args.pair:
                    parser.error("--pair is required with a CEX --exchange")
                rows = FETCHERS[args.exchange](args.pair, start, end)
                source = f"{args.exchange}:{args.pair.upper()}"
        except HTTPError as exc:
            print(f"HTTP {exc.code} from {args.exchange}: {exc.reason}", file=sys.stderr)
            if exc.code == 451:
                print("That venue blocked the request (geo restriction). Try the next source in the hierarchy.", file=sys.stderr)
            return 2
        except (URLError, RuntimeError, TimeoutError, ValueError, KeyError) as exc:
            print(f"Failed to fetch {args.exchange}: {exc}", file=sys.stderr)
            return 2

    series = from_rows(rows)
    pumps = [r for r in series if r["pump_day"]]
    payload = {
        "definition": "utc_daily_close_at_least_10pct_above_close_5_days_earlier",
        "timezone": "UTC",
        "lookback_days": LOOKBACK_DAYS,
        "threshold_pct": 10,
        "methodology_effective_from": "2026-11-16",
        "source": source,
        "candles": len(rows),
        "tested_days": len(series),
        "pump_days": len(pumps),
        "days": series,
    }
    if args.out:
        args.out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.out} ({len(pumps)} pump days / {len(series)} tested)")
        return 0
    if args.json:
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    print(f"Source: {source}")
    print(f"Rule: UTC daily close >= 10% above the close {LOOKBACK_DAYS} days earlier")
    print(f"Tested {len(series)} days, {len(pumps)} pump days")
    if not pumps:
        return 0
    print(f"{'date_utc':<12} {'close':>16} {'close_5d':>16} {'change_pct':>12}")
    for row in pumps:
        print(f"{row['date_utc']:<12} {row['close']:>16.8g} {row['close_5d_earlier']:>16.8g} {row['change_pct']:>11.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
