# Debrief — 2026-06-26 — Mock LP: Learn and Be Curious (diffusion)

## Session

- **Type:** mock-lp (spoken LP drill, non-VLM diffusion story)
- **Duration:** ~25 min
- **Prior context:** [`learn-be-curious_diffusion-mastery.md`](../../Amazon_FinTech/stories/learn-be-curious_diffusion-mastery.md) (was unrehearsed); [`2026-06-26_coding-and-jd-technical.md`](2026-06-26_coding-and-jd-technical.md)

## Conclusions

First rehearsal of the diffusion Learn & Be Curious story. Four-turn drill: full answer → SDE-enabled decision → risk management → 60s compression. Landed ~85–90% by the end.

### Q1 — knowledge-gap story (full)
- **Landed:** clear gap (VAE/GAN strength vs diffusion depth), technical specifics (score matching, SDE, noise schedules, DDPM/DDIM), ownership (designed curriculum, did heavy lifting, implemented base framework), result (7 top-tier papers).
- **Fix:** less "my group" → more "I owned"; add sharper decision point (paused to build foundations vs chase shallow results); name one concrete artifact (base sampler / training objective / schedule interface); replace vague ending ("hard work, determination") with usable lesson (theory → implement core → test failure modes → build).

### Q2 — SDE-enabled modeling decision (strong)
- **Landed:** single-step sampling via operator/dynamical-systems view → distillation of pretrained diffusion teacher → NeurIPS'25.
- **New material worth adding to story:** this single-step distillation example is the best concrete proof the SDE depth paid off — currently NOT in the story file.
- **Fix:** explain "dualized via operators" in one plain clause; state the approximation tradeoff + that quality vs speed was validated.
- **Prep follow-ups:** teacher model? metric (FID/downstream)? speedup factor? closeness to teacher? vs consistency models / existing distillation?

### Q3 — risk management (good)
- **Landed:** portfolio (kept VAE work active), upside framing, staged checkpoints not open-ended reading, used each block to attack a known open problem (→ found TS generation lagging → ImagenTime).
- **Fix:** drop "this is a great question" and "Feynman 101" in interview mode; add explicit kill/narrow criterion; frame as downside control, not "I knew I'd succeed."

### Q4 — 60s compression (interview-ready)
- Four beats present: gap → curriculum action → 7 papers → risk guardrails.
- **Fix:** grammar ("became started to became", "I and my group", "hunderd"); soften single-step framing to "approximate the reverse process in one step via distillation" (not "change the main equation" — avoids theory fight).

## Recurring corrections to promote

| Observation | Where |
|-------------|-------|
| "I and my group" / "my group" over-used → say "I owned" | story file + general LP habit |
| Filler openers ("great question", "Feynman 101") burn time | this debrief (delivery habit) |
| Name a concrete built artifact in every technical LP | story weak-spots |

## Decisions / artifacts updated

- [x] Story updated: added single-step distillation (NeurIPS'25) as IC-proof example + 60s/delivery fixes
- [x] prep-plan.md — Fri 26 LP drill logged
- [x] mock log [`mocks/2026-06-26_mock-lp-learn-curious.md`](../../Amazon_FinTech/mocks/2026-06-26_mock-lp-learn-curious.md)
- [x] INDEX.md debrief + mock rows; stories/README still ☐ (verify facts before Ready)

## Open questions

- Single-step distillation: lock teacher, metric, speedup, quality gap, baseline comparison.
- Confirm exact "seven papers" count + venues.

## Next session (one prompt for session B)

> Read `@Files .cursor/skills/debrief/2026-06-26_mock-lp-learn-curious.md` and `@Files Amazon_FinTech/stories/learn-be-curious_diffusion-mastery.md`. Drill the full ~5 min version once with the single-step distillation artifact and exact NeurIPS'25 numbers; then flip Ready? to ☑ if it holds.
