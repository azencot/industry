# Debrief — 2026-06-24 — Anchor A spoken drill (Jun 24)

## Session

- **Type:** interactive spoken drill (Karan-style Q&A)
- **Duration:** ~45 min
- **Prior context:** Chronos bridge done 23 Jun ([`2026-06-24_chronos-bridge.md`](2026-06-24_chronos-bridge.md)); prep-plan Tue 24 Jun block
- **Covered:** Anchor A — problem, dual tower, collator/M-RoPE deep-dive, Stage A/B/C, training stack, metrics, self-Q&A (Q5–Q7)

## Conclusions

### What went well

- Clear north-star framing (TSRBench), dual-stream architecture, staged curriculum, tiered dev/eval on 0.8B
- Strong IC ownership on collator + DE video-path hijack + `<ts>` token replacement
- Chronos contrast woven naturally (forecast NTP vs exam reasoning + NL)
- TR regression story direction correct (kill bad synth → audit)

### Corrections to drill aloud (memorize)

| Gap | Fix |
|-----|-----|
| Rounded metrics | **Stock 8B: 0.618 / 0.402** → **3ep champion: 0.905 / 0.452** — not ~0.65/~0.3 → ~0.85/~0.45 |
| Dual-view insight | One line: chart = amplitude/trend; delay-embed = topology — *one rendering loses information* |
| Stage B wording | **LM LoRA**, not "train the LLM"; Qwen ViT **frozen all stages** |
| Stage A data arc | Synthetic TS↔text when captions scarce → **CaTS** when synthetic too basic |
| Q5 Chronos kill shot | *"Chronos has no NL head; my task is MCQ, numeric QA, CoT — not quantile forecast."* |
| Q7 ownership numbers | TR **26.9→21.9** (−5 pp gate); reasoning avg **29.5→31.2** misleading alone; killed despite AR/IR +7 pp |
| Infra (if probed) | 162 YAML configs, Slurm DDP 8× GPU, pilot ~15 min, TSExam ±0.3 pp noise floor |

### Dual-stream collator + M-RoPE (session artifact)

- Chart → `image_token_id` + `image_grid_thw` + frozen Qwen ViT
- DE → `video_token_id` + `video_grid_thw` + DINO (`visual_dino`)
- Collator builds fused `input_ids`, separate pixel tensors, **3D Interleaved-MRoPE** position IDs per stream
- **90s spoken:** *"Two visual lanes, two T-H-W grids, M-RoPE preserves spatial structure per stream."*

### Consolidated 15-min script (read aloud once)

1. Problem (2 min) — TSRBench; raw tokens costly + weak structure
2. Insight (2 min) — dual views; Qwen3/3.5-VL 8B/0.8B
3. Architecture (3 min) — frozen ViT + DINO merger; collator/M-RoPE; `<ts>` blocks
4. Curriculum (3 min) — A caption align / B QA+numeric / C VRT-GRPO planned
5. How I ran it (2 min) — 0.8B pilot → full; tiered eval; freeze milestones
6. Results (1 min) — **0.618/0.402 → 0.905/0.452**
7. Honest limit (1 min) — +5 pp real, TR ~29% open, proprietary gap
8. Self-Q&A (2 min) — images for NL reasoning; Stage A grounding; TR kill at gate

## Decisions / artifacts updated

- [x] [`Amazon_FinTech/prep-plan.md`](../../Amazon_FinTech/prep-plan.md) — Anchor A drill done; TMAY + timed-code carried
- [x] [`Amazon_FinTech/INDEX.md`](../../Amazon_FinTech/INDEX.md) — debrief + mock rows
- [x] [`2026-06-24_chronos-bridge.md`](2026-06-24_chronos-bridge.md) — Anchor A gap closed
- [ ] `vlm_multimodal_project.md` — no change (collator detail lives here)

## Open questions

- [ ] TMAY IC paragraph read-aloud (carried from 24 Jun)
- [ ] 1× `/timed-code` medium (carried — do Wed 25 or tonight)
- [ ] Anchor B/C drills Wed 25 per prep-plan

## Next session (one prompt for session B)

> `@Files .cursor/skills/debrief/2026-06-24_anchor-a-spoken-drill.md` + `anchor-cheat-sheet.md` — Wed 25: Anchor B spoken drill (tiered eval, TR kill 26.9→21.9) then Anchor C (task audit). Lead with precise metrics and TR gate numbers from corrections table.
