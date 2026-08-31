"""1. Multirate timestamp alignment — SOLUTION.

Two-pointer walk on sorted arrays. j only moves forward: if B[j+1] is at
least as close to t as B[j], advance. Then gate on max_delta.

    Time  O(|A| + |B|)
    Space O(|A|) for the result (O(1) extra)

Modeling: the coding problem is nearest timestamps. The architecture
question is whether hard alignment belongs in the pipeline at all.

Resampling both modalities onto the fastest clock:
- duplicates / interpolates values
- inflates sequence length
- invents no information
- implies false temporal precision

Better: native-rate encoding -> local compression -> time-aware fusion.

Follow-ups:
1. One-to-one: greedy left-to-right with a used-set, or Hungarian if
   assignment quality matters. Greedy is O(A+B); optimal is cubic.
2. Unsorted: sort B (and keep original indices) then this walk, or
   binary-search each A in B — O(A log B) after sort.
3. Interpolation: find the bracketing pair in B and lerp; still O(A+B)
   two-pointer. Need a policy outside the B range.
4. Streaming B: you cannot commit to a nearest neighbor until a later B
   timestamp is farther than the current candidate (or a latency bound).
5. Time delta as a feature: return (index, t_a - t_b) or a separate
   channel. Models can learn that a 10 ms offset is not a 2 s offset.
"""

from __future__ import annotations


def align_nearest(times_a, times_b, max_delta):
    if not times_b:
        return [None] * len(times_a)

    result = []
    j = 0
    n_b = len(times_b)

    for t in times_a:
        while j + 1 < n_b and abs(times_b[j + 1] - t) <= abs(times_b[j] - t):
            j += 1
        if abs(times_b[j] - t) <= max_delta:
            result.append(j)
        else:
            result.append(None)

    return result


if __name__ == "__main__":
    got = align_nearest(
        [0.0, 0.1, 0.2, 0.5],
        [0.03, 0.22, 0.48],
        0.05,
    )
    assert got == [0, None, 1, 2], got

    # Full prompt example (A has 0.9 as well).
    got = align_nearest(
        [0.0, 0.1, 0.2, 0.5, 0.9],
        [0.03, 0.22, 0.48, 0.91],
        0.05,
    )
    assert got == [0, None, 1, 2, 3], got

    assert align_nearest([0.0, 0.1], [], 0.05) == [None, None]
    assert align_nearest([], [0.0], 0.05) == []
    assert align_nearest([0.0], [0.05], 0.05) == [0]
    assert align_nearest([0.0], [0.0500001], 0.05) == [None]
    # Later A still uses a later B; j never rewinds.
    assert align_nearest([0.0, 10.0], [0.0, 10.0], 0.01) == [0, 1]
    print("01_align_nearest_solution: PASS")
