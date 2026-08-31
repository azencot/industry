"""5. Sliding mean + variance — SOLUTION.

Maintain window_sum and window_sq_sum. Each index: add new, drop old if
len > k, emit when len == k.

    var_pop = (sum sq)/k - mean^2
    Time  O(n)
    Space O(k) for the deque (O(1) extra if you index into x)

Numerics: this formula cancels when values are large and variance is
small (1e9+1, 1e9+2, 1e9+3). Welford is stabler for a growing window.
Sliding-window Welford must *remove* a sample, which is messier
(you keep a deque of values anyway).

Follow-ups:
1. Sample variance divides by (k-1). Population by k. Wearable features
   often use population or a robust scale (IQR) instead.
2. [T, C]: run the same recurrences per channel, or on magnitude.
3. Time window: deque of (t, x); popleft while t_new - t_old > dt;
   k is no longer constant — divide by current length.
4. Irregular arrival: same as (3); do not pretend samples are uniform.
5. Missing: skip NaNs and divide by the count of finite values; or
   carry last-obs and flag a missing fraction (see problem 6).
"""

from __future__ import annotations

from collections import deque


def sliding_stats(x, k):
    if k <= 0 or k > len(x):
        return []

    result = []
    window_sum = 0.0
    window_sq_sum = 0.0
    q = deque()

    for value in x:
        q.append(value)
        window_sum += value
        window_sq_sum += value * value

        if len(q) > k:
            old = q.popleft()
            window_sum -= old
            window_sq_sum -= old * old

        if len(q) == k:
            mean = window_sum / k
            variance = window_sq_sum / k - mean * mean
            result.append((mean, variance))

    return result


class RollingStats:
    def __init__(self, k):
        self.k = k
        self.q = deque()
        self.sum = 0.0
        self.sq_sum = 0.0

    def add(self, x):
        self.q.append(x)
        self.sum += x
        self.sq_sum += x * x

        if len(self.q) > self.k:
            old = self.q.popleft()
            self.sum -= old
            self.sq_sum -= old * old

        if len(self.q) < self.k:
            return None

        mean = self.sum / self.k
        variance = self.sq_sum / self.k - mean * mean
        return mean, variance


if __name__ == "__main__":
    got = sliding_stats([1, 2, 3, 4, 5], 3)
    assert len(got) == 3, got
    for (m, v), em, ev in zip(got, [2.0, 3.0, 4.0], [2.0 / 3.0] * 3):
        assert abs(m - em) < 1e-9, (m, em)
        assert abs(v - ev) < 1e-9, (v, ev)

    assert sliding_stats([1, 2], 3) == []
    assert sliding_stats([1, 2, 3], 0) == []

    # Matches naive population variance.
    xs = [1.5, -2.0, 0.0, 4.0, 4.0, 0.5]
    k = 4
    naive = []
    for i in range(len(xs) - k + 1):
        w = xs[i:i + k]
        mu = sum(w) / k
        var = sum(z * z for z in w) / k - mu * mu
        naive.append((mu, var))
    got = sliding_stats(xs, k)
    for (m, v), (em, ev) in zip(got, naive):
        assert abs(m - em) < 1e-12 and abs(v - ev) < 1e-12

    rs = RollingStats(3)
    assert rs.add(1) is None
    assert rs.add(2) is None
    m, v = rs.add(3)
    assert abs(m - 2.0) < 1e-9 and abs(v - 2.0 / 3.0) < 1e-9
    m, v = rs.add(4)
    assert abs(m - 3.0) < 1e-9 and abs(v - 2.0 / 3.0) < 1e-9
    print("05_sliding_stats_solution: PASS")
