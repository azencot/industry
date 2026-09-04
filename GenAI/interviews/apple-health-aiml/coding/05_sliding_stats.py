"""5. Sliding mean + variance — PROBLEM.

Given x = [x0, ..., xn-1] and window size k, return the mean and
*population* variance of every contiguous window of length k.

    x = [1, 2, 3, 4, 5], k = 3
    windows [1,2,3], [2,3,4], [3,4,5]
    means 2, 3, 4
    vars  2/3, 2/3, 2/3

Naive recomputation is O(n k). Target O(n).

    var = (sum sq)/k - mean^2     # population, not sample (Bessel)

Also implement a streaming class `RollingStats` with add(x) -> (mean, var)
or None until the window is full.

Assumptions:
- k <= 0 or k > n: return [].
- Population variance (divide by k, not k-1).
- This one-pass formula can cancel when values are large and variance is
  small (e.g. 1e9+1, 1e9+2, 1e9+3). Mention Welford; sliding-window Welford
  is harder because you must remove samples.

Follow-ups:
1. Population vs sample variance.
2. Multichannel [T, C].
3. Time-based window rather than count-based.
4. Irregular arrival times.
5. Missing values.
"""

from __future__ import annotations


def sliding_stats(x, k):
    raise NotImplementedError


class RollingStats:
    def __init__(self, k):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError


if __name__ == "__main__":
    got = sliding_stats([1, 2, 3, 4, 5], 3)
    assert len(got) == 3, got
    for (m, v), em, ev in zip(got, [2.0, 3.0, 4.0], [2.0 / 3.0] * 3):
        assert abs(m - em) < 1e-9, (m, em)
        assert abs(v - ev) < 1e-9, (v, ev)

    assert sliding_stats([1, 2], 3) == []
    assert sliding_stats([1, 2, 3], 0) == []

    rs = RollingStats(3)
    assert rs.add(1) is None
    assert rs.add(2) is None
    m, v = rs.add(3)
    assert abs(m - 2.0) < 1e-9 and abs(v - 2.0 / 3.0) < 1e-9
    m, v = rs.add(4)
    assert abs(m - 3.0) < 1e-9 and abs(v - 2.0 / 3.0) < 1e-9
    print("05_sliding_stats: PASS")
