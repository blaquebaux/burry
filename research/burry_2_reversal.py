#!/usr/bin/python3
# =============================================================================
# burry_2_reversal.py — BLAQUE BAUX BURRY #2: does buying the HATED still pay?
#
# Burry's core entry is contrarian: buy what is deeply out of favour. The price-only
# proxy for "hated / beaten-down" is LONG-TERM REVERSAL (DeBondt-Thaler): the biggest
# multi-year losers. On a liquid cross-sector universe, each month rank names by
# trailing 3y return and hold the WORST third (the hated) vs the BEST third (the loved)
# vs equal-weight vs SPY, net of ~10bps/side. Does the contrarian entry earn its keep?
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _burry_common import panel, stats, month_ends, STOCKS, MKT

COST = 0.0010; LB = 756   # 3-year lookback
u, dates, M = panel(STOCKS + [MKT]); j = {s: u.index(s) for s in u}
names = [s for s in STOCKS if s in j]
R = M[1:] / M[:-1] - 1
me = [m for m in month_ends(dates) if m >= LB and m < len(dates) - 1]

def book(pick):
    out = []; prev = set()
    for k in range(len(me) - 1):
        i0, i1 = me[k], me[k + 1]
        sc = {s: M[i0, j[s]] / M[i0 - LB, j[s]] - 1 for s in names}
        ranked = sorted(sc, key=sc.get)                     # worst -> best
        held = pick(ranked); w = 1.0 / len(held)
        turn = len(set(held) ^ prev) * w
        for t in range(i0 + 1, i1 + 1):
            r = w * sum(R[t - 1, j[s]] for s in held)
            if t == i0 + 1: r -= COST * turn
            out.append(r)
        prev = set(held)
    return np.array(out)

n3 = max(1, len(names) // 3)
hated = book(lambda r: r[:n3])          # worst 3y performers — the contrarian longs
loved = book(lambda r: r[-n3:])         # best 3y performers — the crowd
allw = book(lambda r: r)                # equal-weight the universe
start = me[0] + 1
spy = R[start:start + len(hated), j[MKT]]

print("=" * 80, "\nBURRY #2 — buying the hated: long-term (3y) reversal, net of cost\n" + "=" * 80)
print(f"  {dates[me[0]]} .. {dates[-1]}  |  {len(names)} names, monthly, top/bottom third, {int(COST*1e4)}bps/side\n")
print(f"  {'book':<30}{'Sharpe':>8}{'CAGR':>8}{'vol':>7}{'maxDD':>8}")
for lbl, r in [("HATED (worst 3y) — Burry longs", hated), ("LOVED (best 3y) — the crowd", loved),
               ("equal-weight universe", allw), ("SPY", spy)]:
    st = stats(r)
    print(f"  {lbl:<30}{st['sh']:>+8.2f}{st['cagr']*100:>+7.1f}%{st['vol']*100:>6.1f}%{st['dd']*100:>+7.0f}%")

ls = hated - loved
sl = stats(ls)
print(f"\n  long-hated / short-loved spread: Sharpe {sl['sh']:+.2f}  CAGR {sl['cagr']*100:+.1f}%  maxDD {sl['dd']*100:+.0f}%")
print("\nVERDICT: if HATED does not clear equal-weight and SPY, and the long/short spread is weak,")
print("the contrarian entry is not a standalone edge at large-cap scale in this era — buying the")
print("hated is a value/patience bet whose payoff is lumpy and regime-dependent, not a clean factor.")
print("(Consistent with the base's reversal-by-horizon finding and Backsliders' 'the bounce is the edge'.)")
