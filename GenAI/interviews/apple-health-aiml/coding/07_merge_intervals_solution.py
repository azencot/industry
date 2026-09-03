"""7. Merge event intervals — SOLUTION.

Group by type, sort by start, merge overlapping/touching, sum lengths.

    Time  O(n log n)
    Space O(n)

Touching: s <= last_end merges (not only s < last_end). Otherwise a
sleep that ends at 8 and another that starts at 8 would double-count
or leave a hole, depending on the endpoint convention. Here times are
continuous: [0, 8] U [8, 10] = [0, 10], duration 10.

Different types are independent. Overlap across types is a follow-up
(sweep line / two pointers), not this function.

Follow-ups:
1. Streaming: if arrivals are sorted by start, keep the open interval
   per type and close it when the next start is past last_end. Late /
   out-of-order starts force a buffer or a rebuild.
2. Multiple users: group key (user_id, type); same merge.
3. Cross-type overlap: sweep all endpoints; maintain a set of active
   types; accumulate time where |active| >= 2 or a specific pair.
4. Inclusive integers: duration = end - start + 1 per merged run.
"""

from __future__ import annotations

from collections import defaultdict


def duration_by_type(events):
    by_type = defaultdict(list)
    for start, end, event_type in events:
        if end < start:
            raise ValueError("end < start")
        by_type[event_type].append((start, end))

    out = {}
    for event_type, intervals in by_type.items():
        intervals.sort()
        merged_start, merged_end = intervals[0]
        total = 0
        for start, end in intervals[1:]:
            if start <= merged_end:
                if end > merged_end:
                    merged_end = end
            else:
                total += merged_end - merged_start
                merged_start, merged_end = start, end
        total += merged_end - merged_start
        out[event_type] = total
    return out


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

    # Nested + unsorted + extra type.
    nested = [(10, 20, "sleep"), (12, 15, "sleep"), (0, 1, "workout")]
    got = duration_by_type(nested)
    assert got["sleep"] == 10, got
    assert got["workout"] == 1, got

    # Independent types may overlap in time; both durations count.
    overlap_types = [(0, 10, "sleep"), (2, 5, "workout")]
    got = duration_by_type(overlap_types)
    assert got["sleep"] == 10 and got["workout"] == 3, got

    print("07_merge_intervals_solution: PASS")
