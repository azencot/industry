"""
PS1 live code (Karan, 30 Jun 2026) — trailing-window z-score normalization.

Given a 1D time series and window size k, return a new array where each point is
z-score normalized using only the trailing window of k points ending at that point
(the point itself and the k-1 before it). For the first few points where you do not
have k history yet, use whatever history is available.

z-score = (x - mean) / std  over the trailing window.
"""

import math
from collections import deque


def calc_zscore_arr(ts, k):
    """Return trailing-window z-scores (population std; eps avoids div-by-zero)."""
    eps = 1e-5
    ret = []
    for i in range(len(ts)):
        start = max(0, i - k + 1)
        window = ts[start : i + 1]
        mean = sum(window) / len(window)
        var = sum((x - mean) ** 2 for x in window) / len(window)
        std = math.sqrt(var) + eps
        ret.append((ts[i] - mean) / std)
    return ret


def calc_zscore_arr_deque(ts, k):
    """Same semantics; maintain trailing window with deque (O(n) time)."""
    eps = 1e-5
    ret = []
    q = deque()
    running_sum = 0.0
    running_sumsq = 0.0

    for x in ts:
        q.append(x)
        running_sum += x
        running_sumsq += x * x
        if len(q) > k:
            old = q.popleft()
            running_sum -= old
            running_sumsq -= old * old

        n = len(q)
        mean = running_sum / n
        var = running_sumsq / n - mean * mean
        std = math.sqrt(max(var, 0.0)) + eps
        ret.append((x - mean) / std)

    return ret


if __name__ == "__main__":
    ts = [1.0, 2.0, 3.0, 10.0, 11.0]
    k = 3
    a, b = calc_zscore_arr(ts, k), calc_zscore_arr_deque(ts, k)
    assert all(abs(x - y) < 1e-12 for x, y in zip(a, b))
    print("ok", a)
