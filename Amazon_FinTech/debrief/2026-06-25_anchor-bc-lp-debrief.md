# Debrief — 2026-06-25 — Anchor B/C spoken + Ownership LP

## Session

- **Type:** spoken drills (Anchor B, C) + technical LP reframe + doc sync
- **Duration:** ~2 hr (continued from Jun 24 close-out)
- **Prior context:** [`2026-06-24_anchor-a-spoken-drill.md`](2026-06-24_anchor-a-spoken-drill.md); metrics commit `26822b4`

## Conclusions

### Anchor B (~84%)

- **Landed:** Tiered eval funnel; cross-benchmark generalization; TR kill narrative; FinTech gold→noisy docs bridge
- **Synced to docs:** Verified gate latencies — loss (free) → TSExam ~35 s → 176-item slice ~12 s → full ~3 min (0.8B) / ~5 min (8B); parse-miss (single-letter MCQ); NR/TSF discovery
- **Dropped:** Pilot harness / ±0.3 pp as eval stop rule — user does not use; kept fast **train** screen separate in `vlm_multimodal_project.md`
- **Memorize:** TR **26.9→21.9**; gates **−3 pp overall / −5 pp per task**; reas **29.5→31.2** misleading; AR/IR **+7 pp**

### Anchor C (~85% avg)

- **Q5 audit:** Three regimes (operator depth · domain defer · format/convention) — **~85%**
- **Q6 targeted gens:** TR/NR/Goldstein examples + verified metrics — **~90%**
- **Q7 Stage A:** IF-only stuck **61.8%** → synthetic captions + CaTS → **~90.5%** — **~85%** (add frozen-LLM / DINO align one-liner)

### Verified 0.8B metrics (audit + Stage C)

| vs `stageb-weak11k` | Control | + data + Stage C | Δ |
|---------------------|---------|------------------|---|
| TSRBench overall | **0.382** | **0.405** | **+2.3 pp** |
| Reasoning | **0.245** | **0.255** | **+1.0 pp** |

### Ownership LP (~78%)

- **Format:** metric anomaly → gates → kill → audit pivot
- **Fix:** Use exact pp numbers; lead with anomaly not “improving TR”; add per-task readout + sunk-cost kill line
- **60s handoff to Dive Deep:** audit → regimes → **+2.3 / +1.0 pp** — no separate Dive Deep drill (redundant with Anchor C)

### Docs updated (committed `26822b4`)

- [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md)
- [`vlm_multimodal_project.md`](vlm_multimodal_project.md)
- [`dive-deep_tsrbench-reasoning-audit.md`](../stories/dive-deep_tsrbench-reasoning-audit.md)
- [`prep-plan.md`](../prep-plan.md) — Jun 24 TMAY done

## Decisions / artifacts updated

- [x] Cheat sheet + project doc + dive-deep story
- [x] [`Amazon_FinTech/mocks/2026-06-25_vlm-spoken-drill.md`](../mocks/2026-06-25_vlm-spoken-drill.md)
- [x] [`Amazon_FinTech/mocks/2026-06-25_mock-lp-ownership.md`](../mocks/2026-06-25_mock-lp-ownership.md)
- [ ] `ownership_killed-tr-synthetic.md` — optional 90s technical script append

## Open (Jun 25 remainder)

- [ ] 1× `/timed-code` (hash or BFS — sliding window done 24 Jun)
- [ ] Optional: Ownership 3 min retake with revised skeleton (~88% target)

## Next session

> `@Files Amazon_FinTech/debrief/2026-06-25_anchor-bc-lp-debrief.md` — `/timed-code` hash map or BFS medium; then Thu 26 coding sprint.
