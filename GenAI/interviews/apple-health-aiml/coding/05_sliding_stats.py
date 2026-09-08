"""5. Sliding mean + variance — PROBLEM.

Given x = [x0, ..., xn-1] and window size k, return the mean and
*population* variance of every contiguous window of length k.

    x = [1, 2, 3, 4, 5], k = 3
    windows [1,2,3], [2,3,4], [3,4,5]
    means 2, 3, 4
    vars  2/3, 2/3, 2/3

Naive recomputation is O(n k). Target O(n).

    var = (sum sq)/k - mean^2           # population, not sample (Bessel)
    var = (sum_sq - k * mean^2) / (k-1) # sample (Bessel)

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
    n = len(x)
    if k <= 0 or k > n:
        return []

    tot_sum = sum(x[:k])
    tot_sq_sum = sum([e*e for e in x[:k]])

    ret = []

    for i in range(n - k + 1):
        m = tot_sum / k
        ret.append((m, tot_sq_sum / k - m * m))

        if i+k < n:
            old, new = x[i], x[i+k]
            tot_sum += new - old
            tot_sq_sum += new*new - old*old

    return ret

from collections import deque

class RollingStats:
    def __init__(self, k):
        self.tot_sum = 0
        self.tot_sq_sum = 0

        self.k = k
        self.q = deque()

    def add(self, x):
        self.q.append(x)
        self.tot_sum += x
        self.tot_sq_sum += x*x

        if len(self.q) < self.k:
            return None

        elif len(self.q) > self.k:
            old = self.q.popleft()
            self.tot_sum -= old
            self.tot_sq_sum -= old*old

        m = self.tot_sum / self.k
        return (m, self.tot_sq_sum / self.k - m * m)        


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
