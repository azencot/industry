"""8. Streaming top-K in a time window — SOLUTION.

Deque of live events (time order). Expire from the left while
t - t_old > window. Top-k with heapq.nlargest on the live deque.

    add: amortized O(1) expire + O(W log k) nlargest
    Space: O(W) live events

nlargest is a min-heap of size k. Say that. Do not hand-roll unless
they ask. Follow-up lazy heap avoids scanning W when W is huge.

Tie-break: (-score, timestamp) so later events win ties — a later
spike at the same score is usually the one you want to surface.

Follow-ups:
1. Out-of-order: if t < last_t, either drop, or insert into a sorted
   structure and expire from an absolute now they define.
2. Lazy heap: push every event onto a max-heap; on query pop until the
   top is still in the window (id set / cutoff time). Amortized cheaper
   when k << W and expire is frequent.
3. Per user: dict[user] -> TopKWindow.
4. Expiring the current k-th can promote a lower score; always recompute
   (or lazy pop) — do not cache top-k across a drop without checking.
"""

from __future__ import annotations

import heapq
from collections import deque


class TopKWindow:
    def __init__(self, k, window):
        if k <= 0:
            raise ValueError("k must be positive")
        self.k = k
        self.window = window
        self.q = deque()  # (timestamp, score)

    def add(self, timestamp, score):
        self.q.append((timestamp, score))
        cutoff = timestamp - self.window
        while self.q and self.q[0][0] < cutoff:
            self.q.popleft()

        top = heapq.nlargest(
            self.k,
            self.q,
            key=lambda e: (e[1], e[0]),
        )
        return top


if __name__ == "__main__":
    w = TopKWindow(2, 5)
    assert w.add(1, 10) == [(1, 10)]
    assert w.add(2, 3) == [(1, 10), (2, 3)]
    assert w.add(7, 8) == [(7, 8), (2, 3)]

    # Inclusive window: t=10, window=5 keeps t=5.
    w = TopKWindow(3, 5)
    w.add(5, 1)
    w.add(7, 9)
    got = w.add(10, 2)
    assert got[0] == (7, 9), got
    assert (5, 1) in got and (10, 2) in got, got

    # Fewer than k live events.
    w = TopKWindow(5, 100)
    assert w.add(0, 4) == [(0, 4)]

    # Score tie: later timestamp first.
    w = TopKWindow(2, 10)
    w.add(1, 5)
    got = w.add(2, 5)
    assert got == [(2, 5), (1, 5)], got

    print("08_topk_window_solution: PASS")
