# industry — repo index

Personal workspace for industry job prep: Amazon FinTech Senior Applied Scientist interviews, LeetCode practice, and compounding interview artifacts.

**New session?** Read in order: this file → [`AGENTS.md`](AGENTS.md) → [`Amazon_FinTech/INDEX.md`](Amazon_FinTech/INDEX.md).

---

## Directory map

| Path | What it is | When to read |
|------|------------|--------------|
| [`AGENTS.md`](AGENTS.md) | Onboarding for AI sessions: conventions, behavior, skills | Start of every Cursor session |
| [`Amazon_FinTech/`](Amazon_FinTech/) | Role-specific prep: plan, stories, debriefs, mocks, CV | Before interview work |
| [`code/`](code/) | LeetCode solutions (Python); `_practice` = scratch attempts | Coding prep, timed drills |
| [`.cursor/skills/`](.cursor/skills/) | Repeatable prep workflows (`/mock-lp`, `/timed-code`, etc.) | When running a structured drill |

---

## Amazon FinTech (active target)

- **Role:** Senior Applied Scientist, FinTelligence
- **PS1:** Tue 30 Jun 2026, 21:00 Asia/Jerusalem — Karan Aggarwal (Senior Applied Scientist)
- **Format:** intro + ML/LLM depth + Leadership Principles + 1 medium live code (Amazon Live Code)
- **Details:** [`Amazon_FinTech/INDEX.md`](Amazon_FinTech/INDEX.md), [`.cursor/skills/debrief/omri_azencot_experience.md`](.cursor/skills/debrief/omri_azencot_experience.md), [`Amazon_FinTech/prep-plan.md`](Amazon_FinTech/prep-plan.md)

---

## Code practice (`code/`)

66 Python files. Naming: `{leetcode#}_{slug}.py`; suffix `_practice` = earlier attempt kept for comparison.

**Reference PDF:** `code/ML_code.pdf` — ML coding patterns (review before ML-heavy rounds).

### PS1-priority patterns (Amazon Applied Scientist screens)

| Pattern | Files | Notes |
|---------|-------|-------|
| **Hash map / counter** | `1_2sum.py`, `49_Group_Anagrams.py`, `242_valid_anagram.py`, `217_contains_duplicate.py`, `560_subarr_sumEqK.py`, `128_Longest_Consecutive_Sequence.py` | High yield; know duplicate handling |
| **Sliding window** | `3_longest_substring_no_repeat.py`, `76_Minimum_Window_Substring.py`, `438_Find_All_Anagrams_in_a_String.py` | State invariants out loud in interview |
| **Two pointers** | `15_3sum.py`, `125_valid_palindrome.py`, `658_k_closest_elem.py` | Clarify sorted vs unsorted input |
| **Binary search** | `33_Search_in_Rotated_Sorted_Array.py`, `875_koko_eating_banans.py`, `540_single_elem_in_arr.py` | Boundaries and loop invariant |
| **BFS / DFS / graph** | `200_nr_of_islands.py`, `127_Word_Ladder.py`, `207_course_schedule.py`, `721_Accounts_Merge.py` | Topological sort = course schedule family |
| **Heap / top-K** | `215_Kth_Largest_Element_in_an_Array.py`, `347_topk_freq_elem.py`, `973_k_closest_pts2origin.py` | O(n log k) vs O(n log n) |
| **Intervals** | `56_Merge_Intervals.py`, `57_Insert_Interval.py`, `435_Non_Overlapping_Intervals.py` | Sort by start; overlap logic |
| **Trie** | `208_Implement_Trie.py`, `211_Design_Add_and_Search_Words_Data_Structure.py` | Prefix / wildcard search |
| **Linked list** | `206_reverse_linked_list.py`, `141_Linked_List_Cycle.py`, `19_Remove_Nth_Node_From_End_of_List.py`, `143_Reorder_List.py` | Fast/slow pointers |
| **Tree** | `102_binary_tree_level_order_traversal.py`, `98_Validate_Binary_Search_Tree.py`, `124_Binary_Tree_Maximum_Path_Sum.py`, `236_LCA_bindary_tree.py` | Recursion vs iterative BFS |
| **DP** | `70_Climbing_Stairs.py`, `322_Coin_Change.py`, `121_best_time_to.py` | Bottom-up vs memoization |
| **Design** | `146_LRU_cache.py`, `380_Insert_Delete_GetRandom.py` | Less common in PS1; know LRU |

### Timed attempt log

Add rows after `/timed-code` drills:

| Date | Problem | Min | Pass? | Verbal / bug notes |
|------|---------|-----|-------|-------------------|
| 2026-06-24 | `2026-06-24_567_permutation_in_string_practice.py` | ~50 | pass | sliding window; `while`+`le` restart; fixed `for`/precedence bugs — over 25 min |
| 2026-06-25 | `2026-06-25_200_number_of_islands_practice.py` | ~35 | pass | DFS + visited; fixed `.length`/`'1'`/call-site/pre-mark bugs in 2 retries — over 25 min |
| 2026-06-26 | `2026-06-26_347_top_k_frequent_elements_practice.py` | ~15 | pass | heap / top-K; size-k min-heap on `(freq,num)`; strong approach narration; one bug — `heappop(h)` instead of draining `h` in return — **under 25 min** |
| 2026-06-26 | `2026-06-26_56_merge_intervals_practice.py` | ~19 | pass | intervals; sort by start + scan; `start > max_end` flush else extend `max_end`; touching/nested/unsorted covered; clean first pass — **under 25 min** |
| 2026-06-26 | `2026-06-26_153_find_min_rotated_sorted_array_practice.py` | ~16 | pass | binary search; shrink window on `nums[si] > nums[mi]`; post-loop pivot check + no-rotation fallback; all edges pass — **under 25 min** |
| 2026-06-27 | `2026-06-27_19_remove_nth_node_from_end_of_list_practice.py` | ~18 | pass | linked list / fast-slow; invariant: keep `node2` n ahead, delete when `node2` falls off; bugs: off-by-one (deleted node before target) + head-removal crash + `return []` vs `None` — fixed with dummy node + `while node2 != None`; **under 25 min** |
| 2026-06-27 | `2026-06-27_207_course_schedule_practice.py` | ~26 | pass | graph / topological sort (Kahn); invariant: queue holds indegree-0 nodes, cycle iff `count != numCourses`; bugs: `list + int` concat + `if prereq not in courses` dropped multi-edges + `courses[course]` KeyError — fixed with `get(...)+[course]` / `.get(course,[])`; **just over 25 min**; call it Kahn not DFS |
| 2026-06-27 | `2026-06-27_211_design_add_and_search_words_practice.py` | ~17 | pass | trie + DFS wildcard; invariant: `do_dfs(suffix, node)` matches suffix from node; bugs: `true`/`false` → `True`/`False` + `word[i+1]` (single char) → `word[i+1:]` (suffix); explicit for-loop on `.` is fine — skip `any()`; **under 25 min** |
| 2026-06-27 | `2026-06-27_3_longest_substring_without_repeating_practice.py` | ~15 | pass | sliding window + last-index map; invariant: `si` = start of valid no-repeat window, jump only if `last_index[c] >= si`; bugs: max only on repeat + `len(s)-si` instead of `i-si+1`; fixed in 2 iterations — **under 25 min** |
| 2026-06-28 | `2026-06-28_15_3sum_practice.py` | ~29 | pass | two pointers; sort + fix `i` + `lo`/`hi`; invariant: skip dupes at `i`/`lo`/`hi`, break if `nums[i]>0`; bugs: initial 2Sum/slice + indices not values, early `return`, wrong dup-skip neighbors — fixed in 2 iterations — **just over 25 min** |
| 2026-06-28 | `2026-06-28_560_subarray_sum_equals_k_practice.py` | ~18 | pass | prefix sum + hash; invariant: count `prefix_count[curr_sum-k]` before update, seed `{0:1}`; clean first pass — **under 25 min** |

---

## Skills (quick reference)

| Skill | Use when |
|-------|----------|
| `/mock-lp` | Behavioral / Leadership Principle drill |
| `/timed-code` | 25-min coding simulation |
| `/ml-deep-dive` | 3-min ML/LLM spoken answer + follow-ups |
| `/debrief` | After mock or real interview — update stories & config |
| `/log-timed-drill` | Log a finished timed-code result to INDEX + prep-plan |
| `/commit-push` | Commit and push changes; no Cursor attribution |

---

## Closing the loop

After each prep session:

1. Log debriefs → `Amazon_FinTech/debrief/YYYY-MM-DD_{topic}.md`; mock drills → `Amazon_FinTech/mocks/`
2. Refine STAR stories → `Amazon_FinTech/stories/`
3. Promote recurring fixes → `AGENTS.md` or relevant skill

Remote: `git@github.com:azencot/industry.git`
