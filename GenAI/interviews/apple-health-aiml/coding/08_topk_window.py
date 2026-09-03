"""8. Streaming top-K in a time window — PROBLEM.

Stream of (timestamp, anomaly_score). After each event, return the K
highest-scoring events whose timestamps lie in (t - window, t], i.e.
the last `window` time units, inclusive of the current timestamp.

    k = 2, window = 5
    add(1, 10) -> [(1, 10)]
    add(2, 3)  -> [(1, 10), (2, 3)]
    add(7, 8)  -> [(7, 8), (2, 3)]    # t=1 expired: 7-1=6 > 5

Target: expire old events in amortized O(1) per add; top-k via a heap
over the live window (heapq.nlargest is a heap of size k).

Assumptions to state before coding:
- Timestamps are numeric and non-decreasing.
- Window is inclusive: keep if t - t_old <= window.
- If fewer than k live events, return all of them.
- Ties: higher score first; if scores tie, later timestamp first.
- Empty window before any add does not happen; first add returns that
  one event.

Follow-ups:
1. Timestamps can go backwards (buffer / drop).
2. Do not scan the whole window: lazy-delete heap.
3. Multiple users: one window per user_id.
4. Return only scores, or also rank stability as events expire.
"""

from __future__ import annotations


class TopKWindow:
    def __init__(self, k, window):
        raise NotImplementedError

    def add(self, timestamp, score):
        raise NotImplementedError


if __name__ == "__main__":
    w = TopKWindow(2, 5)
    assert w.add(1, 10) == [(1, 10)]
    assert w.add(2, 3) == [(1, 10), (2, 3)]
    assert w.add(7, 8) == [(7, 8), (2, 3)]
    print("08_topk_window: PASS")
