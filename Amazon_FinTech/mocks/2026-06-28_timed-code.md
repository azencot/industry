# Mock — 2026-06-28 — timed-code (coding sprint #2)

## Setup

- Duration: ~70 min across 3 problems
- Focus: PS1 medium breadth — two pointers, prefix sum, binary search on answer
- Problems: 3Sum (15), Subarray Sum Equals K (560), Koko Eating Bananas (875)

## What went well

- All 3 passed; 560 was a clean first pass (prefix sum + complement)
- Right invariants stated for prefix-sum and two-pointer dedup
- Recovered correctly after review on 15 and 875

## What broke

- [ ] 3Sum: started O(n³) 2Sum-on-slice + index/value confusion; early `return` in loop; wrong dup-skip neighbors
- [ ] Koko: wrong search bound (`h` not `max(piles)`); wrong feasibility (`== h` not `<= h`)
- [ ] Binary-search-on-answer template not yet automatic — needs one cold re-rep

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| Binary search on answer: bounds `[1,max]`, monotonic feasibility, count `<= budget` | INDEX pattern table / debrief |
| 3Sum: sort + two pointers, return values not indices, skip dupes at i/lo/hi | debrief |

## Next session (one thing)

- Mon 29 polish: one cold binary-search-on-answer rep (Koko) to lock bounds + feasibility.
