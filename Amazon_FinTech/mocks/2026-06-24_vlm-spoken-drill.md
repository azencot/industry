# Mock — 2026-06-24 — vlm-spoken-drill (Anchor A)

## Setup

- **Duration:** ~45 min
- **Focus:** Jun 24 prep-plan — Anchor A production ML/LLM system
- **Topics covered:** Q1–Q7 interactive grill; collator/M-RoPE deep-dive; Stage A/B/C; metrics; self-Q&A (visual vs tokens, decoupling, TR regression)

## What went well

- Architecture path concrete (frozen ViT, DINO, video-path hijack, staged training)
- Chronos contrast without over-explaining v1/Bolt
- Tiered 0.8B dev + eval discipline narrative clear

## What broke

- [x] **Verbal / structure:** Metrics rounded (~0.65/0.3 → ~0.85/0.45) — use **0.618/0.402 → 0.905/0.452**
- [x] **Technical gap:** Dual-view *why* (complementary information) under-stated until coach prompt
- [ ] **LP story weak:** Q7 TR kill missing gate numbers — add 26.9→21.9, −5 pp gate, misleading reasoning avg

## Corrections to promote

| Observation | Update where |
|-------------|--------------|
| Precise 8B before/after metrics | [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md) — already correct; **memorize verbatim** |
| Collator/M-RoPE spoken 90s | [`2026-06-24_anchor-a-spoken-drill.md`](../../.cursor/skills/debrief/2026-06-24_anchor-a-spoken-drill.md) |
| TR kill numbers in self-Q&A | Wed 25 Anchor B drill + [`ownership_killed-tr-synthetic.md`](../stories/ownership_killed-tr-synthetic.md) reframe |

## Next session (one thing)

Anchor B spoken drill — tiered eval + TR kill with full numbers; then 1× `/timed-code`.
