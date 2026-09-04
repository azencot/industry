"""1. Multirate timestamp alignment — PROBLEM.

Two modalities sampled at different, irregular times. Both timestamp arrays
are sorted. For every timestamp in A, return the index of the closest
timestamp in B if |t_a - t_b| <= max_delta; otherwise None.

    times_a = [0.0, 0.1, 0.2, 0.5]
    times_b = [0.03, 0.22, 0.48]
    max_delta = 0.05
    -> [0, None, 1, 2]

Target: O(len(A) + len(B)).

Assumptions to state before coding:
- Both arrays sorted ascending.
- Ties: either neighbor is acceptable if equally close; pick a rule and keep it.
- Empty B: every A maps to None.
- max_delta is inclusive.

Do not resample both streams onto the fastest clock. After you code, say
why (duplication, longer sequences, invented precision).

Follow-ups (think, then check the solution file):
1. A B observation may match only one A observation.
2. Timestamps are not sorted.
3. Linear interpolation instead of nearest neighbor.
4. B is streaming.
5. Preserve the time difference as a feature.
"""

from __future__ import annotations


def align_nearest(times_a, times_b, max_delta):
    raise NotImplementedError


if __name__ == "__main__":
    got = align_nearest(
        [0.0, 0.1, 0.2, 0.5],
        [0.03, 0.22, 0.48],
        0.05,
    )
    assert got == [0, None, 1, 2], got

    assert align_nearest([0.0, 0.1], [], 0.05) == [None, None]
    assert align_nearest([], [0.0], 0.05) == []
    assert align_nearest([0.0], [0.05], 0.05) == [0]
    assert align_nearest([0.0], [0.0500001], 0.05) == [None]
    print("01_align_nearest: PASS")
