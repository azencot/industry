# Debrief — 2026-06-24 — Chronos bridge (late 23 Jun session)

## Session

- **Type:** exploration / learning plan (Chronos vs VLM contrast for Karan)
- **Duration:** ~45 min (late 23 Jun)
- **Prior context:** Imry referral pivot; [`prep-plan.md`](../prep-plan.md) Day 3 Chronos item; [`INDEX.md` Chronos note](../INDEX.md#chronos-team-stack-imry)

## Conclusions

### Chronos family (don't conflate generations)

| Gen | Input | Output | Speed story |
|-----|-------|--------|-------------|
| **v1 (T5)** | Mean-scale → **1 quantized bin token per timestep** | AR decode: sample **20 trajectories × 64 steps**; aggregate for quantiles | Slow (many decoder passes + sampling) |
| **Bolt** | Patch-16 → MLP → **continuous encoder token** (vocab ≈ 2) | **Direct multi-step quantile** forecast (9 levels × 64 steps, one pass) | ~250× faster vs v1 (patching + no AR sampling) |
| **Chronos-2** | Bolt + multivariate / covariates | Universal forecaster | Production path (SageMaker / AutoGluon) |

**Imry's "patch → few tokens" = Bolt**, not v1 per-step binning.

### v1 sampling mechanics (common confusion)

- **One fixed history** (512 context tokens) for all 20 paths — not 20 contexts to choose from.
- Each path: autoregressively sample 64 future bin tokens; stochasticity from categorical sampling (temperature/top-k).
- Final forecast: **median or quantiles across 20 paths** — empirical predictive distribution.

### Binning / theory

- No clean theoretical upper bound on forecast quality given B bins.
- Rabanser et al. 2020: empirical — binning often *helps* neural forecasters vs real-valued I/O.
- Chronos §5.6–5.7: vocab tradeoff; precision ≈ `30s/(B-1)` in original units; fails on exponential trends / overflow.
- CE is **not distance-aware** on bins (ordinal loss = future work).

### Your project — parallel and divergence

**Shared philosophy:** streamlined backbone; win on representation + data curriculum + eval — not bespoke TS transformer.

| Dimension | Chronos | Your VLM |
|-----------|---------|----------|
| Task | Forecast next values | Reason (MCQ, TR, numeric QA, CoT) |
| Representation | Value bins / patches | Dual views: chart (Qwen ViT) + delay embed (DINOv3) |
| Data scale | ~890K series pretrain | ~tens of K curated (ChatTS 105K align, TSExam 20K, CaTS ~16K) |
| Training | Massive pretrain (+ TSMixup, KernelSynth) | Stage A align → B MCQ reason → C GRPO on CoT |
| Eval | 42 forecast datasets (MASE/WQL) | Tiered gates; TSRBench north star; parse-miss ≠ accuracy |
| Zero-shot | Unseen **datasets** | Unseen **TSRBench items** (overlap with TSExam — report slices) |

**Dual tower compression:**
1. Line chart → ViT patchify (e.g. 16×16 patches) → visual tokens → projector → LLM.
2. Delay-embedding image → DINOv3 (self-supervised ViT; patch tokens, not one vector) → merger (LoRA Stage A) → projector → LLM.

**Hybrid / fine-tune Chronos for reasoning — no:**
- No natural-language interface on Chronos outputs.
- Task gap: forecasting NTP ≠ reasoning + CoT.
- Partial overlap today: TSRBench prediction slices as MCQ only; full numeric forecast from VLM = out of scope (output head design).

**Production routing answer:** Chronos-class for trajectories; VLM for explain / QA / compliance slices; shared eval gates per task.

### Interview one-liners (memorize)

1. *"Same problem — efficient TS into a general model. Chronos quantizes or patches for forecast quantiles; I use dual visual encodings because the task is exam-grade reasoning, not next-value NTP."*
2. *"Bolt kills AR sampling — one decoder pass, direct quantiles. My speed story is different: frozen ViT + staged LoRA, not forecast head design."*
3. *"Stage A is LLaVA-style align; Stage C optimizes CoT correctness — Chronos has no analogue because it never outputs reasoning traces."*

## What went well

- User correctly challenged Block 1 (patching = newer Bolt, not v1).
- Strong articulation of NTP vs reasoning and hybrid scope boundaries.
- Block 3 self-synthesis (staged curriculum, smaller corpus, richer eval) was interview-ready.

## Gaps / still drill aloud

- ~~**Anchor A** spoken run~~ — **done 24 Jun** → [`2026-06-24_anchor-a-spoken-drill.md`](2026-06-24_anchor-a-spoken-drill.md). Memorize exact metrics; TR kill numbers sharpen in **Anchor B** (Wed).
- "What broke" depth continues in **Anchors B/C** (Wed): TR kill gates, task audit.

## Decisions / artifacts updated

- [x] [`Amazon_FinTech/prep-plan.md`](../prep-plan.md) — Chronos bridge completed; session notes in Days 1–2 section
- [x] [`Amazon_FinTech/INDEX.md`](../INDEX.md) — v1/Bolt/Chronos-2 table; routing one-liner
- [ ] `vlm_multimodal_project.md` — no change needed (Chronos is interview bridge, not project doc)
- [ ] `AGENTS.md` — no promote (one-time Chronos clarification)

## Open questions

- Exact DINO/Qwen image resolution → token count in your stack (nice-to-have if Karan asks compression ratio).
- Verify TSRBench leaderboard rank before PS1 (Deliver Results story).

## Next session (24 Jun)

**One item:** Spoken **Anchor A** drill end-to-end (15 min), weaving in the three self-Q&A answers.

> Read `@Files Amazon_FinTech/debrief/2026-06-24_chronos-bridge.md` `@Files Amazon_FinTech/anchor-cheat-sheet.md` — run Anchor A spoken drill; if Chronos comes up, use routing one-liner from this debrief. Then one `/timed-code` medium.
