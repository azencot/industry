# Debrief — 2026-08-20 — Apple Health AIML: LLM training-run drill

**Type:** Prep — 5-question spoken drill (HM topic 3)  
**Track:** GenAI / Apple Health AIML HM screen  
**Duration:** ~25 min, 5 Qs  
**Call:** Fri 2026-08-21, 11:05–11:50 AM PDT · Shirley Ren · fit, no coding  
**Prior:** [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md) · [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md)  
**Artifacts:** this file (drill); spoken spine still lives in the 3C detail file §1

---

## Session

Five questions on **most impactful LLM training run** (not why-Apple). Q1 opening walkthrough, then pull-thread: pick one run, why kill if average up, was the drop an eval bug, images vs native TS encoder on wearables.

---

## Conclusions

**Drill — what landed**

- Q2 was the real run: synthetic TR mix on **8B dual**, gates **−3 pp overall / −5 pp slice** set before training, average looked like a win (~+1.7, some slices +7), TR **26.9 → 21.9**, killed the mix, next move is task audit not more GPU.
- Held the kill when pressed (Q3). Did not talk himself into shipping the average.
- Mix-only Stage B as a second condition (Q4). Audit framed as missing **operators**, not a vibe.
- Q5: images as a stolen visual prior, not “plots are the true TS object.” Keep that. Already said **not married to TS-as-image** in the why-Apple drill.

**Drill — what broke (repeat tomorrow and she will filter you)**

| Said | Why it fails | Do instead |
|------|----------------|------------|
| “Developing and leading a project” | PI / lab-lead; prior loops flagged this | “I designed / trained / gated” |
| Benchmark list + Qwen family, no deltas | Project overview, not a **run** | 8B stock **0.62 → ~0.90** TSExam; TSRBench **~0.40 → ~0.45**; 27B FT **~0.92**; then the kill |
| “Your group’s workshop paper” unprompted | Name-drop; sounds like you reverse-engineered her CV | Same two-stage shape **only if she goes there** |
| “Thresholds to keep or kill” with no decision | Process without judgment | TR synth **26.9 → 21.9** → killed |
| “Could be a bug / deeper understanding / unpredictable mixes” | Confusion, not a gate | Pre-declared −5 pp on TR. Average up **is** the failure mode |
| “I verified the eval is correct” | Assertion, no check | Same harness; parse-miss ≠ accuracy; mix-only B: TSExam **0.826 → 0.714** |
| “Images keep all information” | Contradicts own ablation (delay num **0.17** vs chart **0.71** vs dual **0.79**) | One view **loses** information; that’s why two |
| “TS encoders / losses aren’t locked” | Dunks on RelCon + their native TS encoder paper | Field hasn’t converged like DINO; **compare families on their signals** |
| Vision-community scaling sermon | Generic FM-lab talk; skipped wearables | Would **not** port matplotlib onto PPG |

**Locked 2–3 min — say once tonight, once Friday morning, then stop:**

> The problem I actually train on is that an LLM does not see a time series if you dump numbers into context. I represent each series two ways — a line chart for trend and amplitude, and a delay-embedding image for dynamical structure — and fuse both into the LLM. I owned the dual routing, the collator, and the recipe. Training is two-stage: Stage A aligns vision with the language model frozen; Stage B teaches the LM to answer. LoRA, multi-GPU DDP, config-first sweeps. I don’t promote on loss: cheap TSExam, then a TSRBench slice, then the full north star, gates set before the run. I proved the recipe on Qwen3-VL-8B — stock 0.62 to about 0.90 on TSExam, TSRBench about 0.40 to 0.45. Current runs are Qwen3.5 9B and 27B; 27B fine-tune lands about 0.92 TSExam, near the 8B champion. When a synthetic mix was supposed to fix temporal reasoning and instead dropped TR 26.9 to 21.9, I killed it and went back to data generation. Architecture plus data plus an honest gate beat more GPU hours on a bad mix.

**If she pulls the kill (~25s):** pre-declared gate; average up is the failure mode; more of the same synth is doubling down; later epochs + TR-CoT still left reasoning **~0.27–0.30**.

**If she says “could be a bug” (~20s):** same harness / adapter chain / parse-miss; mix-only B val looked fine (shared generator); real TSExam **0.826 → 0.714**. You’ve already caught eval bugs (adapter-chain +13 pp, Q35 thinking/EOS) — don’t dump the list.

**If she asks why images / why not their encoder (~30s):**

> Images were a way to steal a visual prior when the LLM couldn’t see the series — not because plots are the true representation. One view still loses information; that’s why I used two, and why delay-only collapsed on numbers. A native TS encoder is the more honest bias if you have the data. I wouldn’t reprint charts on PPG. Year one I’d compare encoder families on your signals with the same eval gate. Same bottleneck: the model does not perceive the series until you represent it.

Do **not** volunteer her paper.

---

## Decisions / artifacts updated

- [x] [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md) — locked §1 + drill anti-patterns + kill/eval/encoder pockets
- [x] [`2026-08-12_hm-screen-prep.md`](2026-08-12_hm-screen-prep.md) — 3C pointer + anti-patterns
- [x] [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md) — open question closed
- [ ] `omri_azencot_experience.md` — no; Apple-loop specific
- [ ] `AGENTS.md` — no; not a global convention

---

## Open questions

- None for the three HM **fit** topics. Do **not** prep the 5-interview on-site before this call.

---

## Next session (Fri morning, 15 min — then stop)

Skim locked **why-Apple 50s** + this **2–3 min** + kill sentence (TR 26.9 → 21.9). Join Webex **after 10:55 AM PDT**. After the call: write `2026-08-21_hm-screen-debrief.md`.

**Handoff prompt**

```
@GenAI/interviews/apple-health-aiml/2026-08-20_why-apple-health-drill.md
@GenAI/interviews/apple-health-aiml/2026-08-20_training-run-drill.md
@GenAI/interviews/apple-health-aiml/2026-08-20_shirley-group-briefing.md
@GenAI/interviews/apple-health-aiml/2026-08-12_hm-screen-prep.md
HM screen was Fri 2026-08-21 with Shirley Ren. Write 2026-08-21_hm-screen-debrief.md from the call notes; do not invent.
```
