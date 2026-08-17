#!/usr/bin/python3
# =============================================================================
# _burry_common.py — shared helpers for the Blaque Baux Burry sketches.
# Alpaca SIP daily bars; reads ALPACA_KEY_ID / ALPACA_SECRET_KEY from env. Read-only.
#
# DATA NOTE, up front: Alpaca serves PRICE bars — no fundamentals, no 13F holdings, no
# short-interest feed. So we test the MECHANISM, not the man, with price-only proxies
# the sleeve commits to:
#   "deeply hated / beaten-down"  -> long-term price REVERSAL (DeBondt-Thaler)
#   "deep value / hard assets"    -> tradable style ETFs (RPV, IWN, GLD, DBC, PHO, WOOD)
#   "contrarian short of froth"   -> short ARKK / short high-momentum (MTUM)
# A 13F is a stale, long-only LABEL; the test is whether the style pays net of cost.
# =============================================================================
import os, json, urllib.request, math
import numpy as np

H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
START, END = "2016-01-01", "2026-08-01"
_cache = {}

# tradable proxies for the Burry-style pillars
PILLARS = {"RPV": "deep/pure value", "IWN": "small-cap value", "GLD": "gold",
           "DBC": "broad commodities", "PHO": "water", "WOOD": "timber/farmland"}
FROTH = ["ARKK", "MTUM"]
MKT, CASH = "SPY", "BIL"

# a liquid, cross-sector universe with full 2016 history — for the cross-sectional reversal test
STOCKS = ("AAPL MSFT XOM CVX JPM BAC WFC C GS JNJ PFE MRK ABBV KO PEP PG WMT TGT HD LOW "
          "DIS CMCSA T VZ INTC CSCO IBM ORCL QCOM TXN CAT DE BA GE MMM HON UPS FDX F GM "
          "UNH CVS MCD SBUX NKE").split()

def bars(s):
    if s in _cache: return _cache[s]
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={s}&timeframe=1Day"
         f"&start={START}&end={END}&adjustment=all&feed=sip&limit=10000")
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40))
        _cache[s] = {b["t"][:10]: b for b in d.get("bars", {}).get(s, [])}
    except Exception:
        _cache[s] = {}
    return _cache[s]

def panel(syms):
    D = {s: bars(s) for s in syms}; D = {s: v for s, v in D.items() if len(v) > 250}
    u = list(D); dates = sorted(set.intersection(*[set(D[s]) for s in u]))
    M = np.array([[D[s][d]["c"] for s in u] for d in dates], float)
    return u, dates, M

def rets(syms):
    u, dates, M = panel(syms)
    return u, dates[1:], M[1:] / M[:-1] - 1

def stats(r):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    if len(r) < 30 or r.std() == 0: return dict(sh=float('nan'), cagr=float('nan'), dd=float('nan'), vol=float('nan'))
    cum = np.cumprod(1 + r)
    return dict(sh=r.mean() / r.std() * math.sqrt(252), cagr=cum[-1] ** (252 / len(r)) - 1,
                dd=(cum / np.maximum.accumulate(cum) - 1).min(), vol=r.std() * math.sqrt(252))

def capm(y, x):
    y = np.asarray(y, float); x = np.asarray(x, float)
    m = np.isfinite(y) & np.isfinite(x); y, x = y[m], x[m]
    if len(y) < 30 or np.var(x) == 0: return float('nan'), float('nan')
    b = np.cov(y, x)[0, 1] / np.var(x)
    return (y.mean() - b * x.mean()) * 252, b

def month_ends(dates):
    out = [i for i in range(len(dates) - 1) if dates[i][:7] != dates[i + 1][:7]]
    out.append(len(dates) - 1)
    return out
