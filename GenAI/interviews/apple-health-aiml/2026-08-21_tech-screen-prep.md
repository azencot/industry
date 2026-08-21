# Prep — Apple Health AIML tech screen (45 min)

**Status:** **Scheduled — Tue 2026-08-25, 1:35–2:20 PM PDT**, Webex. Interviewer **Feng Zhu**.  
**Format (Tyler 2026-08-21, locked):** **45 min** spoken **depth check** on **LLM training** + **multimodality fundamentals**.  
**Coding:** **No.** Invite lists CoderPad — **ignore** (same HM template). Don’t grind LeetCode.  
**Confirm:** reply to Tyler that you are available — template in [`2026-08-21_tech-screen-invite.md`](2026-08-21_tech-screen-invite.md).  
**Group PDFs:** [`papers/README.md`](papers/README.md) — skim **Feng’s periodicity** paper; TS-LLM only for the bakeoff. Do not name-drop.  
**Invite / reply:** [`2026-08-21_tech-screen-invite.md`](2026-08-21_tech-screen-invite.md)  
**HM debrief (what she already heard):** [`2026-08-21_hm-screen-debrief.md`](2026-08-21_hm-screen-debrief.md)

**Your goal:** They leave thinking you can **own an LLM training run and a representation bakeoff** — IC verbs, a kill, transfer to *their* signals without reprinting matplotlib on PPG.

This is **not** a second why-Apple chat. Locked 50s stays in the pocket. Lead with training + encodings.

---

## What already happened (don’t replay the HM)

Shirley already got: 2–3 min multimodal; three encodings (text / patched / images) + bet; three evals; TSRBench (finance question; you blanked on sensors); two-stage + gates; Bosch / no product ship; ImagenFew; “impact at scale”; Seattle.

**Tech screen = one layer down.** Same topics are allowed. Repeating the same 2–3 min without a **number, a kill, or a counterfactual** is a miss.

---

## Two pillars (Tyler)

### 1. LLM training (half the hour if they drive it)

**Project run (must be a run, not a lab tour):** [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md) · [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md)

Say if they didn’t hear it on HM:

> Two-stage: A = see (vision, LM frozen), B = answer (LM LoRA). I don’t promote on loss. Cheap TSExam → TSRBench slice → full north star. Gates **−3 pp overall / −5 pp slice** set before the run. Synthetic TR mix: average looked up, TR **26.9 → 21.9**, I **killed it**. 8B stock **0.62 → ~0.90** TSExam, TSRBench **~0.40 → ~0.45**.

**General LLM judgments (not the VLM story):** [`../../notes/2026-08-20_llm-training-judgments.md`](../../notes/2026-08-20_llm-training-judgments.md) · [`../../notes/2026-08-21_sft-starting-pitfalls.md`](../../notes/2026-08-21_sft-starting-pitfalls.md)

If they leave the project: mixture NLL ≠ task; packing ≠ padding; completion-only SFT; chat template (Qwen ChatML / thinking); LoRA vs unfreeze LR; select ckpt on val, report test once. Don’t jump to RL.

### 2. Multimodal fundamentals (the other half)

Three encodings you already listed — now with **failure modes** and **what you’d do on wearables**.

| Approach | When it works | Failure |
|----------|---------------|---------|
| **TS as text** | Tiny series, scale as numbers in the prompt | Burns context; weak perception; her paper’s named failure too |
| **Patched native encoder → LLM** | Honest bias if you have the data (this is **her** TS-LLM shape) | You must train the encoder; patch rate / multivariate layout matter |
| **TS as images** | Steal a visual prior; dual views beat one | One view **loses** information (delay-only ChatTS num **~0.17** vs chart **~0.71** vs dual **~0.79**). **Do not** say “images keep all information.” **Do not** reprint charts on PPG |

Bakeoff line (30s):

> Text dumps lose structure. A patched encoder is the more honest bias if you have the data — I’d bake that off. Images were a stolen visual prior, not the true object of a series. I used two views because one loses information. Year one on this team: same eval gate, compare encoder families on *your* IMU/PPG/longitudinal signals. I would not port matplotlib onto PPG.

Group facts if they go there (don’t volunteer papers): [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md). RelCon **~3.9M params**, 1B **segments**. LLM seat = **language layer**.

**Feng Zhu angle:** his public paper with this group is multimodal wearable streams + **naturalistic missingness** + periodicity vs a deep TS model. If he pulls “your benches aren’t Watch data,” land on missingness / longitudinal / don’t reprint charts on PPG — not a paper recap of his mood work.

---

## Pockets from the HM (they may re-ask)

**TSRBench ≠ finance.** 4,125 / 15 tasks / 14 domains. Healthcare is in it (**ECG-QA**, **PTB-XL** on decision-making). Also industrial / river sensors / weather / energy. Honest: public ECG ≠ Watch PPG/IMU.

**Product:** still **no consumer ship**. Bosch irregular/noisy → generative adaptation (**ImagenFew** / irregular sampling), not a Watch feature.

**Why this seat (only if asked):** locked 50s in [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md). **Never** “impact at scale.”

**Intro:** IC first. Not associate professor.

**Success bar she named:** curious + **breadth** — show a kill, not a paper list. Work mode: **~3-month concrete slices** of a large problem.

---

## What not to do

| Skip | Why |
|------|-----|
| Full 5-interview on-site bank | Tyler: this screen is the next gate |
| Coding campaign | Not briefed |
| RelCon / Workout Buddy / Feng’s mood paper name-drop | HM didn’t go there; don’t start a paper quiz |
| PI / “my students” / associate professor lead | Prior loop + this HM open |
| “Images keep all information” | Contradicts your ablation |
| Mixing Bosch Watch scripts | Separate track; Sunnyvale reloc vs Seattle on-site |

---

## Until Tuesday

Daily **45–75 min**, speak don’t only read:

1. Training-run **2–3 min** + kill sentence (TR 26.9 → 21.9) out loud once.
2. Encodings bakeoff **30–40s** including wearable transfer / missingness.
3. **One** general SFT/NLL question from the two notes files.
4. TSRBench healthcare pocket once.

Stop when those four are clean. Do **not** start on-site interview 4–5.

**Tue:** 15 min skim; join Webex **after 1:25 PM PDT** (no more than 10 min early). Fallback phone if Webex dies: **425-606-7471**.

---

## After the call

Write `YYYY-MM-DD_tech-screen-debrief.md` (use the actual date). Update [`README.md`](README.md). Do not email Shirley.
