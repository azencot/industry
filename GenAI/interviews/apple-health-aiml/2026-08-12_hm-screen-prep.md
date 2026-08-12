# Prep — HM screen with Shirley Ren (Health AIML)

**When:** **Friday, August 21, 2026 · 11:05–11:50 AM PDT** (confirmed invite)  
**Length:** **45 min**  
**Format:** Webex · **fit conversation** with Shirley Ren (1). Invite may still list CoderPad — **ignore it; this is not a coding round.**  
**HM:** **Shirley Ren** (Shirley You Ren) — Senior ML Manager / Principal Engineer, Health & Fitness  
**Recruiter:** **Tyler** — briefed the three topics below  
**Prior:** [`2026-08-12_recruiter-debrief.md`](2026-08-12_recruiter-debrief.md) · [`2026-08-12_recruiter-prep.md`](2026-08-12_recruiter-prep.md)

**Independent check (2026-08-12):** an Apple scientist said the HM chat is **mostly fit**, not a coding exercise. Matches Tyler. Prep **only** the three topics.

**Her public signal (use carefully — don’t name-drop papers unless natural):** sensor foundation models, LLMs for health/fitness, shipped fitness/health features; research adjacent to **time-series reasoning with LLMs**, multimodal sensor fusion, wearable motion FMs. Your multimodal + TS story is on-theme.

**Your goal:** She leaves thinking: *genuinely wants health AI at Apple, can own multimodal LLM training end-to-end, IC depth not lab-PI, worth advancing to tech screen.*

---

## Tyler’s three topics (this is the entire round)

1. **Specific interest in health AI**
2. **Interest in Apple**
3. **Walk through most impactful LLM training run** (spoken narrative — not a pad, not a live code)

Everything else is supporting color. Do not turn this into a coding screen, a paper quiz, or a full on-site research talk.

---

## 0. Confirmed logistics (do today)

**Reply to Tyler** confirming you are available for Fri Aug 21, 11:05–11:50 AM PDT.

| Item | Detail |
|------|--------|
| Join | Webex — **no more than 10 min early** (invite rule). **Device test done 2026-08-12** — skip re-testing unless something breaks. |
| Coding | **None.** Tyler + Apple scientist: HM is **fit**. Calendar CoderPad is template noise. Do not log into a pad, grind LeetCode, or sketch architecture “just in case.” |
| Dress | Whatever presents your best self in a work setting (invite language). |
| After | Write `2026-08-21_hm-screen-debrief.md` and update [`README.md`](README.md). |

**Daily budget until the call:** **45–75 min** on weekdays, **one 45-min mock** on the weekend. Stop when Tyler’s three topics are clean out loud. Do **not** prep the 5-interview on-site this week.

**Do not mix tracks:** TTD / forecasting stories stay parked. Lead with multimodal LLM training. TS credibility only if she asks.

---

## Prep schedule — Wed Aug 12 → Fri Aug 21

Source of truth for *what* to say: this file §§2–6. Depth for the training run: [`.cursor/skills/debrief/vlm_multimodal_project.md`](../../../.cursor/skills/debrief/vlm_multimodal_project.md) + [`.cursor/skills/debrief/omri_azencot_experience.md`](../../../.cursor/skills/debrief/omri_azencot_experience.md). IC verbs only.

### How to use each day

- **Speak**, don’t only read. If you can’t say it in the time box, cut.
- End each session by recording (or saying once more) the **weakest** of the three pillars.
- Skip a day if life happens — **never skip Thu Aug 20 dress rehearsal** or **Fri morning skim**.

---

### Wed Aug 12 — confirm + lock the spine (~45 min)

**Done if you already wrote this file; still do the reply + one spoken pass.**

1. Reply confirming the slot.
2. Say **60s intro** (§2) out loud twice — kill any lab-PI / “my students” language.
3. Say **health AI** + **why Apple** (§3A–B) once each (~45–60s).
4. Pick **2 questions** from §6 and write them at the top of a notepad for Aug 21.
5. Logistics one-liner once: Seattle · green card / PR · FT · on-site fine.

**Exit check:** intro does not sound like a PI pitch.

---

### Thu Aug 13 — training-run walkthrough (core of the call) (~60–75 min)

Tyler’s topic 3. Spoken walkthrough of the most impactful LLM training run — still **fit**, not a tech screen. She may probe, but you are telling a story, not writing code.

1. Pick **one** run and freeze it: multimodal Qwen3.5 VLM fine-tune / curriculum at **9B ↔ 27B** (dual visual encodings → LLM). Honest frame: **major multimodal training run you owned**, not pretrain-from-scratch.
2. Speak the **2–3 min** structure in §3C once, timer on: problem → architecture → training design → scale → eval gate → kill decision → result.
3. Lock **numbers you will actually say** (do not mix campaigns):
   - **Current work:** Qwen3.5 **9B / 27B**, multi-stage, LoRA/PEFT, DDP.
   - **Measured campaign you can cite:** earlier **8B / 0.8B** — TSExam HF **~0.90**; TSRBench overall **~0.45** on 8B (open-source strong at that scale then). If 9B/27B numbers are not re-measured, say so: *“those metrics are from the prior scale; current runs are 9B/27B with the same eval gate.”*
4. Write **one sentence** for the kill: data-mix hurt temporal reasoning → **stopped stacking training** → went back to data generation / task coverage.
5. Drill the probe bank in §3C — **one sentence each**, out loud.

**Exit check:** 2–3 min walkthrough without notes; you can name one metric class + one negative result.

---

### Fri Aug 14 — depth she is likely to probe (~60 min)

Assume she interrupts. Have a 20s answer, then stop.

| Probe | What to own in one breath |
|-------|---------------------------|
| Why two visual encoders? | Chart = trend/amplitude; delay embedding = dynamical structure; complementary failure modes |
| Why not text-only TS? | Perception bottleneck; images as inductive bias for shape/amplitude |
| LoRA vs full FT? | Iteration speed / cost vs capacity; when you’d unfreeze (ceiling not moving) |
| DDP / infra? | One real bottleneck you owned (OOM, NCCL, collator, resume across stages) — not a team war story |
| How do you know it generalized? | Held-out tasks, ablations, parse-miss ≠ accuracy, pilots before full TSRBench |
| Pretrain honesty | Fine-tune / adapter / curriculum at 9B–27B — do not claim GPT-scale pretrain lead |

Also rehearse the **curriculum in 30s:** Stage A = see the series (vision/alignment, LLM frozen); Stage B = answer (LM LoRA); eval gates cheap → expensive.

**Exit check:** you can take any row above without restarting the 3-min speech.

---

### Sat Aug 15 — sharpen topic 1 (health AI) with her problem class (~45 min)

Stay on **Tyler topic 1**. Read **abstracts only** so the health-AI answer sounds specific, not generic. Do **not** open with “I read your paper.” Do **not** turn Saturday into a Shirley bibliography.

| Piece | Why it maps to you | Your bridge if it comes up |
|-------|--------------------|----------------------------|
| [Towards Time-Series Reasoning with LLMs](https://machinelearning.apple.com/research/towards-time) (Chow et al., incl. Shirley You Ren) | TS encoder on an LLM + CoT-style reasoning; not just forecast | You also treat **reasoning in language over series** as the goal; you chose **dual visual encodings** instead of a dedicated TS encoder — be ready to defend that tradeoff |
| [Speech FMs generalize to wearable TS](https://machinelearning.apple.com/research/speech-foundation) (Narain, Aldeneh, Ren) | Cross-modal transfer, data-scarce health/fitness sensors | You know **representation transfer under scarcity**; you don’t fake ECG/PPG product work |
| RelCon / wearable motion FMs (Xu, Narain, … Ren) | Sensor/motion foundation models for wearables | Adjacent to dual-representation thinking; stay high-level |

**If she asks how you’d work on health signals:** messy longitudinal TS + another modality + **eval/safety gate** before claiming progress. Not clinical diagnosis.

**Exit check:** 3-sentence overlap (“same problem class: TS reasoning with LLMs”) and 1-sentence difference (“I fused two visual views; they also explore dedicated TS encoders / speech-FM transfer”).

---

### Sun Aug 16 — Mock #1, full 45-min shape (~50 min)

Run the table in §1 against a timer. Talk to a recorder or a person. No slides.

| Block | Time | Pass if… |
|-------|------|----------|
| Warm + intro | 5–8 min | IC spine; current gravity = multimodal TS → LLM |
| Why health AI / why Apple | 10–15 min | Specific; no product trivia; no “I love Apple” |
| Training-run deep dive | 15–20 min | She can interrupt; you still hit kill + eval |
| Your questions + close | 5–8 min | Two questions from §6; close from §7 |

After: write 5 bullets — where you went long, where you sounded managerial, any number you hedged. Fix those tomorrow, don’t add new material.

**Exit check:** you finished in ≤45 min and used “I designed / trained / gated.”

---

### Mon Aug 17 — health AI + Apple pockets under pressure (~45 min)

1. Re-say §3A and §3B. Then answer follow-ups:
   - *Why not a pure FM lab?* → privacy, on-device/platform, safety eval as first-class.
   - *Why not clinical / digital-health startup?* → you want Apple’s data + deployment bar, not a clinician hat you don’t have.
   - *Why Seattle / this seat?* → already local; IC research scientist; multimodal + TS is the JD.
2. Anti-pattern pass (§5): say the “Avoid” column out loud, then the “Do” rewrite.
3. Optional 15 min: JD skim only — multimodal, representation learning, time series, train+eval, safe LLM in health. No Watch internals.

**Exit check:** health-AI answer never claims MD expertise; Apple answer names **foundational multimodal + high cost of error**, not gadgets.

---

### Tue Aug 18 — Mock #2, all three Tyler topics under interruption (~60 min)

Same 45-min shape. Force interruptions on **each** topic, not only the training run:

1. Health AI — “you’re not a clinician; why this domain?”
2. Apple — “why not a pure FM lab / another big-tech health team?”
3. Training run — §3C probe bank + Fri table (spoken; no pad)

If using Cursor: drill from this file + the VLM project note; IC framing only.

**Exit check:** you can restart from any of the three topics without collapsing into a paper list or a coding sketch.

---

### Wed Aug 19 — questions, close, competing-process honesty (~40 min)

1. Finalize **exactly two** questions (§6). Default:
   - What is Health AIML prioritizing in 6–12 months for this seat?
   - What does **strong** look like in year one (papers vs shipped components vs eval infra)?
2. Say the close (§7) once.
3. If she asks competing processes: Apple Health AIML is **high priority** (multimodal + TS + Seattle). Don’t volunteer TTD/SCOT unless asked; if asked, keep it one sentence.
4. Comp: only if she raises it — experience, interview performance, team comps (Tyler’s factors). Prefer level/fit.

**Exit check:** questions are about *her team’s problems*, not Watch sensors or candidate count.

---

### Thu Aug 20 — dress rehearsal + logistics (~40 min, then stop)

1. Full spoken pass once: intro → **health AI** → **Apple** → 2–3 min **training run** → two questions → close. **Timer.**
2. Webex already verified. No CoderPad.
3. Layout: this file + notepad with Tyler’s three topics + 2 questions + logistics line. Close extra tabs.
4. **Stop.** No new papers. Sleep.

**Exit check:** one clean pass; voice is IC; you know the join rule (≤10 min early).

---

### Fri Aug 21 — interview day

**Morning (15 min, not a study block):**

- Skim Tyler’s three topics + kill-decision sentence + two questions.
- 60s intro once.
- Water, quiet room, phone on DND.

**Join:** Webex **after 10:55 AM PDT**, not before (invite: no more than 10 min prior). 11:05–11:50 AM PDT with Shirley Ren.

**During:** let her drive. If the training-run block starts late, **cut** Stage C / GRPO / paper list — keep architecture, eval gate, kill.

**Immediately after:**

1. Notes while fresh: how she asked the three topics, what she probed, any level/team signal.
2. Write `2026-08-21_hm-screen-debrief.md`; update [`README.md`](README.md).
3. Only then start tech-screen depth (LLM training + multimodal fundamentals).

---

### What this week is *not*

| Skip | Why |
|------|-----|
| Coding / CoderPad / LeetCode | Tyler + Apple scientist: HM is **fit**; coding belongs (if at all) later |
| Full on-site (5 themes) | Tyler: HM first; tech screen is the next depth gate |
| Clinical / Watch product trivia | Anti-pattern; IP-adjacent |
| Forecasting / TTD pitch | Wrong track for this call |
| Cold-emailing Shirley | Mid-loop; Tyler owns process |

---

## 1. Call shape (expected — fit, Tyler’s three topics)

| Block | ~time | Tyler topic |
|-------|-------|-------------|
| Warm + your intro | 5–8 min | Who you are; current center of gravity = multimodal TS → LLM |
| Why health AI / why Apple | 10–15 min | **(1) health AI** · **(2) Apple** — specific, not generic |
| Deep dive: impactful LLM training run | 15–20 min | **(3)** spoken narrative; she may probe ablations, scale, failure modes — still not a coding exercise |
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

Comp: only if she raises it — factors already named by Tyler (experience, interview performance, team comps). Prefer level/fit first; public base range known.

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
