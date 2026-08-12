# Prep — HM screen with Shirley Ren (Health AIML)

**When:** next week (schedule ASAP — recruiter asked availability)  
**Length:** **45 min**  
**HM:** **Shirley Ren** (Shirley You Ren) — Senior ML Manager / Principal Engineer, Health & Fitness  
**Prior:** [`2026-08-12_recruiter-debrief.md`](2026-08-12_recruiter-debrief.md) · [`2026-08-12_recruiter-prep.md`](2026-08-12_recruiter-prep.md)

**Her public signal (use carefully — don’t name-drop papers unless natural):** sensor foundation models, LLMs for health/fitness, shipped fitness/health features; research adjacent to **time-series reasoning with LLMs**, multimodal sensor fusion, wearable motion FMs. Your multimodal + TS story is on-theme.

**Your goal:** She leaves thinking: *genuinely wants health AI at Apple, can own multimodal LLM training end-to-end, IC depth not lab-PI, worth advancing to tech screen.*

---

## Recruiter’s three focus areas (memorize)

1. **Specific interest in health AI**
2. **Interest in Apple**
3. **Walk through most impactful LLM training run**

Everything else is supporting color. Do not turn this into a full on-site research talk.

---

## 0. Next-hour checklist

1. Say **60s intro** once (§2) — IC verbs only.
2. Lock **health AI** + **why Apple** pockets (§3) — ~45–60s each when asked.
3. Practice **LLM training-run walkthrough** out loud once (§4) — architecture → data/curriculum → infra → eval gate → kill decision → metric.
4. Pick **2 questions** for her (§6).
5. Logistics one-liner: Seattle · green card / PR · FT · on-site fine.

---

## 1. Call shape (expected)

| Block | ~time | What |
|-------|-------|------|
| Warm + your intro | 5–8 min | Who you are; current center of gravity = multimodal TS → LLM |
| Why health AI / why Apple | 10–15 min | Specific, not generic “Apple is great” |
| Deep dive: impactful LLM training run | 15–20 min | Technical narrative; she may probe ablations, scale, failure modes |
| Your questions + close | 5–8 min | Team problems, success bar, next step |

---

## 2. 60-second intro (same IC spine)

> I’m an applied ML research scientist focused on sequential and multimodal data. Recently I’ve been leading the **technical** direction on multimodal time-series models — dual visual encodings into an LLM, multi-stage training curricula, and a strict eval harness so we only keep changes that move the metrics. Before that: generative and representation learning for time series, including image-based transforms and irregular sampling. PhD Technion; publish NeurIPS/ICML/ICLR. I’m a US permanent resident, based in Seattle, looking for a full-time **IC** research role where I own multimodality work hands-on — architecture, training, and gating what ships. Health AIML fits because it’s foundational multimodal models over health and fitness signals, with a high bar for getting answers wrong.

---

## 3. Pillar scripts

### A. Specific interest in health AI (~45–60s)

> I’m not a clinician. What I care about is models that understand **messy longitudinal signals** — activity and physiological-like time series, plus language or other modalities — and that only ship when evaluation supports it. Health and fitness is where that combination is both high-impact and high-cost-of-error: overconfident LLMs are unacceptable. My last few years have been exactly that problem class on the research side — multimodal + time series + cross-modal alignment + eval gates — and I want to apply it where the data is real user health/fitness context and the deployment bar is Apple’s, not a paper leaderboard alone.

**If she probes “why not pure foundation-model lab?”**  
> I want the constraints: privacy, on-device/platform realities, and safety eval as first-class. That’s where the research decisions get interesting.

### B. Interest in Apple (~45–60s)

> Apple already sits on devices people trust with health and fitness data, and Health AIML is explicitly building **foundational multimodal** tech for those experiences — representation learning and time series included. I want to do multimodal research where it reaches people at scale and where wrong answers matter. Seattle + IC research scientist role is the practical fit; the intellectual fit is multimodal + TS under a safety-first product bar.

**Avoid:** product trivia guesses about Watch internals; IP fishing; “I love Apple products” without the research bridge.

### C. Most impactful LLM training run (core of the call)

**Pick one run and stick to it:** multimodal Qwen3.5 VLM fine-tune / curriculum at **9B ↔ 27B** (dual visual encodings → LLM). Frame honestly as **major multimodal training run you owned**, not multi-trillion-token pretrain-from-scratch.

**Spoken structure (~2–3 min, then let her dig):**

1. **Problem** — time-series reasoning with an LLM; single visualization encoding was insufficient.  
2. **Architecture** — line-chart encoding (trend/amplitude) + delay-embedding image (structure); fuse both into the LLM.  
3. **Training design** — multi-stage: (i) align vision to “see” series, (ii) teach LM to answer; LoRA / PEFT; config-driven sweeps; multi-GPU DDP.  
4. **Scale** — **9B and 27B** class; pilots before full runs.  
5. **Eval gate** — tiered eval; cheap pilots → expensive full benchmarks; no ship without metric move.  
6. **Hard call** — when a data-mix idea hurt temporal reasoning, **killed it** and went back to data generation instead of stacking more training.  
7. **Result / learning** — what moved (name the metric class you actually have); lesson = architecture + data + honest eval beat more GPU hours on a bad mix.

**Probe bank (have one sentence each):**

| Probe | Pocket |
|-------|--------|
| Why two visual encoders? | Complementary failure modes: trend vs dynamical structure |
| Why not text-only TS? | Perception bottleneck; images as a strong inductive bias for amplitude/shape |
| LoRA vs full FT? | Cost / iteration speed vs capacity; when you’d unfreeze |
| DDP / infra pain? | One real bug or bottleneck you owned (sync, OOM, data pipeline) |
| How do you know it generalized? | Held-out tasks / ablations / negative results |
| Pretrain vs fine-tune honesty | Fine-tune / adapter / curriculum scale — not claiming GPT-scale pretrain lead |

---

## 4. Logistics pocket (if asked)

> US permanent resident (green card). Based in Seattle. Full-time IC. On-site Seattle is fine. Available now / can align start with the team (BGU academic leave through Oct doesn’t block FT start).

Comp: only if she raises it — factors already named by recruiter (experience, interview performance, team comps). Prefer level/fit first; public base range known.

---

## 5. Anti-patterns for *this* HM

| Avoid | Do |
|-------|-----|
| Lab-PI / grant / “my students…” | “I designed / trained / gated…” |
| Generic Apple fan pitch | Multimodal + health/fitness deployment bar |
| Claiming clinical expertise | Longitudinal multimodal signals + eval/safety |
| Forecasting-company story as lead | TS credibility only if she asks; lead with multimodal LLM training |
| Dumping paper list | One training-run narrative + offer depth |

---

## 6. Questions to ask her (pick 2)

1. What problems is Health AIML prioritizing in the next 6–12 months for someone in this seat — representation learning, multimodal fusion, on-device constraints, eval for safe LLM behavior?  
2. For this role, what does **strong** look like in the first year — papers, shipped model components, eval infrastructure, or something else?  
3. How do you think about the boundary between foundational multimodal research and product-facing health/fitness features on the team?

Skip: exact Watch model internals; competing candidate count; comp as question #1.

---

## 7. Close

> I’m very interested in this role and in working with Health AIML. Happy to go deeper on the training stack or eval harness with whoever runs the technical screen.

After the call: write `YYYY-MM-DD_hm-screen-debrief.md` and update [`README.md`](README.md).
