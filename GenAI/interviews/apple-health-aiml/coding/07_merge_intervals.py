"""7. Merge event intervals — PROBLEM.

Irregular wearable events as (start, end, event_type). Intervals of the
SAME type may overlap or touch. Merge those and return total duration
per type.

    events = [
        (0, 5, "sleep"),
        (3, 8, "sleep"),      # overlaps sleep
        (8, 10, "sleep"),     # touches previous merged sleep
        (1, 2, "workout"),
        (4, 6, "workout"),    # disjoint from the first workout
    ]
    -> {"sleep": 10, "workout": 3}

Target: O(n log n) from the sort. Linear scan after that.

Assumptions to state before coding:
- start <= end. Zero-length (start == end) contributes 0.
- Touching intervals of the same type merge (end == next start).
- Different types do NOT merge with each other even if they overlap
  in time (sleep 0-8 and workout 4-6 both count).
- Unsorted input.
- Unknown types just appear as keys.
- Empty input -> {}.

Do not discretize onto a 1 Hz grid.

Follow-ups (think, then check the solution file):
1. Streaming: intervals arrive online, possibly with late starts.
2. Multiple users: key by (user_id, type).
3. Duration of overlap *across* types (sleep AND workout).
4. Inclusive integer endpoints (end is a last included sample).
"""

from __future__ import annotations


def duration_by_type(events):
    raise NotImplementedError


if __name__ == "__main__":
    events = [
        (0, 5, "sleep"),
        (3, 8, "sleep"),
        (8, 10, "sleep"),
        (1, 2, "workout"),
        (4, 6, "workout"),
    ]
    got = duration_by_type(events)
    assert got["sleep"] == 10, got
    assert got["workout"] == 3, got

    assert duration_by_type([]) == {}
    assert duration_by_type([(2, 2, "nap")]) == {"nap": 0}
    print("07_merge_intervals: PASS")
