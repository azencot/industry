# Debrief — 2026-06-28 — Coding sprint #2 + JD technical refresh

## Session

- **Type:** timed-code (3 mediums) + JD technical refresh (5-block teach-and-quiz)
- **Duration:** ~2 hrs across the morning (after the agentic-trends drill)
- **Prior context:** Sat 27 Karan full mock (JD probe ~70%); [`2026-06-28_llm-agentic-trends-drill.md`](2026-06-28_llm-agentic-trends-drill.md) earlier same day
- **Format:** narrated timed coding + spoken JD scenario answers with tighten-after

## Conclusions

Strong, productive day. Coding is in good shape across patterns; JD framing is mostly right but still has a few recurring phrasing traps that would cost precision points with Karan.

### Coding (3 mediums, all pass)

| File | Pattern | ~Min | Result |
|------|---------|------|--------|
| `2026-06-28_15_3sum_practice.py` | two pointers | ~29 | pass after 2 fix iterations |
| `2026-06-28_560_subarray_sum_equals_k_practice.py` | prefix sum + hash | ~18 | clean first pass |
| `2026-06-28_875_koko_eating_bananas_practice.py` | binary search on answer | ~23 | pass after fix |

**Coding bugs to watch:**
- 3Sum: started with 2Sum-on-slice (O(n³) + index/value confusion); needed sort + two-pointer reset. Also early `return` inside the loop and wrong duplicate-skip neighbors.
- Koko: wrong search bound (`h` instead of `max(piles)`) and wrong feasibility test (`== h` instead of `<= h`). **Binary-search-on-answer template needs a clean re-rep.**
- Subarray-sum: clean — prefix-sum + complement pattern is solid now.

**Coding keeper:** for "min k such that feasible" → binary search on the answer space, bounds `[1, max]`, feasibility monotonic, count `<= budget`.

### JD technical refresh (5 blocks)

| Block | Score | Note |
|-------|-------|------|
| LLM choices + scaling | ~75% | said CPT first for changing rules — corrected to RAG-first |
| Eval gates + monitoring | ~85% | strong; tiered shadow → selective automation; fix: latency is SLA not "safety metric" |
| Corrections loop | ~90% | best block; log → validate → taxonomy → component fix → selective FT |
| Calibration / abstention | ~75% | used raw p80/p95; corrected to calibrated per-slice thresholds + deterministic gates first |
| Retrieval quality | ~80% | right pipeline breakdown; fix: hybrid/metadata/rerank before "FT retriever from scratch" |

## Recurring corrections (promote)

| Trap | Correct framing |
|------|-----------------|
| CPT first for changing customer rules | **RAG first**; CPT only for missing domain language on large unlabeled corpus |
| Raw confidence thresholds (p80/p95) | **Calibrated** per-slice thresholds; deterministic hard gates first |
| "Fine-tune retriever from scratch" | hybrid (BM25+vector), metadata filters, reranking → retriever FT with hard negatives only if needed |
| Latency as a "safety metric" | latency/cost = SLA; safety/compliance = false auto-match, wrong amount/invoice, unsupported action |
| FT "irrelevant" with limited labels | FT/LoRA shapes **behavior** once corrections accumulate — not irrelevant, just not first |

## Locked memory lines (PS1 crib)

- "RAG updates facts/rules; FT/LoRA shapes behavior; CPT teaches domain language; routing manages cost-risk."
- "Headline accuracy doesn't reduce manual review; slice-level precision and false-action gates do."
- "Corrections become taxonomy and regression tests first; only some become training signal."
- "Deterministic checks first, calibrated thresholds second, automation only on safe slices."
- "Don't fine-tune the generator to fix retrieval; measure evidence recall, fix retrieval, train a retriever only if needed."

## Decisions / artifacts updated

- [x] root [`INDEX.md`](../../INDEX.md) — 3 timed rows
- [x] [`prep-plan.md`](../prep-plan.md) — Sun 28 coding + JD refresh marked done
- [x] [`INDEX.md`](INDEX.md) — debrief + mock rows
- [ ] No story/profile change

## Open / carry to Mon 29 (polish)

- Re-rep binary-search-on-answer once cold (Koko bounds + feasibility).
- Rehearse the 5 locked JD lines aloud; avoid the CPT-first and raw-confidence traps.
- Mon 29 plan otherwise unchanged: anchors from memory, JD crib, weakest LP, 2 questions for Karan.

## Next session (one prompt for session B)

> Read `@Files Amazon_FinTech/debrief/2026-06-28_coding-and-jd-refresh.md`. It's Mon 29 (polish, no new material): run anchors from memory, rehearse the 5 JD crib lines aloud (watch CPT-first + raw-confidence traps), one cold binary-search-on-answer rep, weakest LP once, finalize 2 questions for Karan.
