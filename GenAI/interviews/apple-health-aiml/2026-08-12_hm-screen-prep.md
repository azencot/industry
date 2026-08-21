# Prep — HM screen with Shirley Ren (Health AIML)

**When:** **Friday, August 21, 2026 · 11:05–11:50 AM PDT** (confirmed invite)  
**Length:** **45 min**  
**Format:** Webex · **fit conversation** with Shirley Ren (1). Invite may still list CoderPad — **ignore it; this is not a coding round.**  
**HM:** **Shirley Ren** (Shirley You Ren) — Senior ML Manager / Principal Engineer, Health & Fitness  
**Recruiter:** **Tyler** — briefed the three topics below  
**Prior:** [`2026-08-12_recruiter-debrief.md`](2026-08-12_recruiter-debrief.md) · [`2026-08-12_recruiter-prep.md`](2026-08-12_recruiter-prep.md)

**Independent check (2026-08-12):** an Apple scientist said the HM chat is **mostly fit**, not a coding exercise. Matches Tyler. Prep **only** the three topics.

**Her public signal (use carefully — don’t name-drop papers unless natural):** sensor foundation models, LLMs for health/fitness; research adjacent to **time-series reasoning with LLMs**, multimodal sensor fusion, wearable motion FMs. Group briefing (papers, sensors, shipped-work attribution): [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md). Your multimodal + TS story is on-theme. **Workout Buddy** is a LinkedIn shipped claim, not a paper with her name — do not name-drop it.

**Your goal:** She leaves thinking: *genuinely wants health AI at Apple, can own multimodal LLM training end-to-end, IC depth not lab-PI, worth advancing to tech screen.*

---

## Three topics Shirley will cover (Tyler briefed these)

1. **Specific interest in health AI**
2. **Interest in Apple**
3. **Walk through most impactful LLM training run** (spoken narrative — not a pad, not a live code)

Tyler is **not** on this call. He told you what Shirley is likely to focus on. Everything else is supporting color. Do not turn this into a coding screen, a paper quiz, or a full on-site research talk.

---

## 0. Confirmed logistics (do today)

**Reply to Tyler** confirming you are available for Fri Aug 21, 11:05–11:50 AM PDT.

| Item | Detail |
|------|--------|
| Join | Webex — **no more than 10 min early** (invite rule). **Device test done 2026-08-12** — skip re-testing unless something breaks. |
| Coding | **None.** Tyler + Apple scientist: HM is **fit**. Calendar CoderPad is template noise. Do not log into a pad, grind LeetCode, or sketch architecture “just in case.” |
| Dress | Whatever presents your best self in a work setting (invite language). |
| After | Write `2026-08-21_hm-screen-debrief.md` and update [`README.md`](README.md). |

**Daily budget until the call:** **45–75 min** on weekdays, **one 45-min mock** on the weekend. Stop when the three HM topics are clean out loud. Do **not** prep the 5-interview on-site this week.

**Do not mix tracks:** TTD / forecasting stories stay parked. Lead with multimodal LLM training. TS credibility only if she asks.

---

## Prep schedule — Wed Aug 12 → Fri Aug 21

Source of truth for *what* to say: this file §§2–6. Training-run depth: [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md). Broader project: [`.cursor/skills/debrief/vlm_multimodal_project.md`](../../../.cursor/skills/debrief/vlm_multimodal_project.md). IC verbs only.

### How to use each day

- **Speak**, don’t only read. If you can’t say it in the time box, cut.
- End each session by recording (or saying once more) the **weakest** of the three pillars.
- Skip a day if life happens — **never skip Thu Aug 20 dress rehearsal** or **Fri morning skim**.

---

### Wed Aug 12 — confirm + lock the spine (~45 min)

**Partial:** 3C detail read through **§3**. Resume at [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md) **§4**.

**Done if you already wrote this file; still do the reply + one spoken pass.**

1. Reply confirming the slot.
2. Say **60s intro** (§2) out loud twice — kill any lab-PI / “my students” language.
3. Say **health AI** + **why Apple** (§3A–B) once each (~45–60s).
4. Pick **2 questions** from §6 and write them at the top of a notepad for Aug 21.

**Exit check:** intro does not sound like a PI pitch. Do **not** volunteer green card / Seattle / FT — Tyler already has that.

---

### Thu Aug 13 — training-run walkthrough (core of the call) (~60–75 min)

This is topic 3. Spoken walkthrough of the most impactful LLM training run — still **fit**, not a tech screen. Shirley may probe, but you are telling a story, not writing code. Detail: [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md) — **resume at §4** (curriculum); §§1–3 already read 2026-08-12.

1. Pick **one** run and freeze it: multimodal Qwen3.5 VLM fine-tune / curriculum at **9B ↔ 27B** (dual visual encodings → LLM). Honest frame: **major multimodal training run you owned**, not pretrain-from-scratch.
2. Speak the **2–3 min** structure in §3C once, timer on: problem → architecture → training design → scale → eval gate → kill decision → result.
3. Lock **numbers you will actually say** (do not mix campaigns) — detail file §5–6:
   - **Current:** Qwen3.5 **9B / 27B**; 27B FT TSExam **~0.92**; 9B r64 **~0.89**.
   - **8B champion (cite):** stock **0.62 → ~0.90 / 0.926** TSExam; TSRBench **~0.40 → ~0.45**. Do **not** claim 9B/27B won TSRBench (zero-shot 27B ties the 8B champion; FT trades reasoning for perception).
4. Kill sentence: TR synth **26.9 → 21.9** → **killed** → data generation, not more GPU.
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

### Sat Aug 15 — sharpen topic 1 without a JD rewrite (~45 min)

Stay on **topic 1** (interest in health AI), but the answer is **TS representations for LLMs**; health is downstream. Source of truth for group papers / sensors / attribution: [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md). Read **abstracts only** so you can say “same problem class,” not “I became a health person.” Do **not** open with “I read your paper.”

| Piece | Why it maps to you | Your bridge if it comes up |
|-------|--------------------|----------------------------|
| [Towards Time-Series Reasoning with LLMs](https://machinelearning.apple.com/research/towards-time) (Chow et al., incl. Shirley You Ren) | TS encoder on an LLM + CoT-style reasoning; not just forecast | You also treat **reasoning in language over series** as the goal; you chose **dual visual encodings** instead of a dedicated TS encoder — be ready to defend that tradeoff |
| [Speech FMs generalize to wearable TS](https://machinelearning.apple.com/research/speech-foundation) (Narain, Aldeneh, Ren) | Cross-modal transfer, data-scarce health/fitness sensors | You know **representation transfer under scarcity**; you don’t fake ECG/PPG product work |
| RelCon / wearable motion FMs (Xu, Narain, … Ren) | Sensor/motion foundation models for wearables | Adjacent to dual-representation thinking; stay high-level |

**If she asks how you’d work on health signals:** same stack — represent the series so the LLM can use them; eval gate before claiming progress. Not clinical diagnosis.

**Exit check:** 3-sentence overlap (“same problem class: TS reasoning with LLMs”) and 1-sentence difference (“I fused two visual views; they also explore dedicated TS encoders / speech-FM transfer”). Health is the downstream, not a new angle.

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

1. Re-say §3A and §3B. Then drill **§3D** (hard questions) — 20–40s, then stop. Priority follow-ups:
   - *Why this domain if you’re not a clinician?* → TS representations for LLMs; health is downstream at scale, not a new scientific identity.
   - *Why not a pure FM / TS lab?* → real series + consequential eval; privacy/on-device constrain the representation.
   - *Why not a clinical / digital-health startup?* → you’re not putting on a clinician hat; you want this representation problem on Apple’s signals.
2. Anti-pattern pass (§5): say the “Avoid” column out loud, then the “Do” rewrite.

**Exit check:** health-AI answer never sounds JD-adapted or clinical; it names **representing series for LLMs** first.

---

### Tue Aug 18 — Mock #2, all three HM topics under interruption (~60 min)

Same 45-min shape. Force interruptions from **§3D**, not only the training run:

1. Health AI — “no health papers / you’ll just continue your VLM.”
2. Apple — “why this team if it’s the same scientific angle?”
3. Transfer — “PPG isn’t a UCR chart; 27B isn’t on-device.”
4. Training run — §3C probe bank + Fri table (spoken; no pad)

If using Cursor: drill from this file + the VLM project note; IC framing only.

**Exit check:** you can restart from any of the three topics without collapsing into a paper list or a coding sketch.

---

### Wed Aug 19 — questions, close, competing-process honesty (~40 min)

1. Finalize **exactly two** questions (§6). Default:
   - What is Health AIML prioritizing in 6–12 months for this seat?
   - What does **strong** look like in year one (papers vs shipped components vs eval infra)?
2. Say the close (§7) once.
3. If she asks competing processes: Apple Health AIML is **high priority** (multimodal + TS + Seattle). Don’t volunteer SCOT unless asked. **TTD is closed (2026-08-19).** If asked: a few science roles; Bosch RTC multimodal FMs is also in process — this seat is the Seattle + health-signals match. Keep it one sentence.
4. Comp: only if she raises it — experience, interview performance, team comps (Tyler’s factors). Prefer level/fit.

**Exit check:** questions are about *her team’s problems*, not Watch sensors or candidate count.

---

### Thu Aug 20 — dress rehearsal + logistics (~40 min, then stop)

1. Full spoken pass once: intro → **health AI** → **Apple** → 2–3 min **training run** → two questions → close. **Timer.**
2. Webex already verified. No CoderPad.
3. Layout: this file + notepad with the three HM topics + 2 questions. Close extra tabs.
4. **Stop.** No new papers. Sleep.

**Exit check:** one clean pass; voice is IC; you know the join rule (≤10 min early).

---

### Fri Aug 21 — interview day

**Morning (15 min, not a study block):**

- Skim the three HM topics + locked why-Apple 50s + locked training-run 2–3 min + kill-decision sentence (TR 26.9 → 21.9).
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

## 1. Call shape (expected — fit with Shirley)

| Block | ~time | Focus |
|-------|-------|--------|
| Warm + your intro | 5–8 min | Who you are; current center of gravity = multimodal TS → LLM |
| Why health AI / why Apple | 10–15 min | **(1)** TS-for-LLM; health = downstream at scale · **(2) Apple** — not a JD rewrite |
| Deep dive: impactful LLM training run | 15–20 min | **(3)** spoken narrative; she may probe ablations, scale, failure modes — still not a coding exercise |
| Your questions + close | 5–8 min | Team problems, success bar, next step |

---

## 2. 60-second intro (same IC spine)

> I’m an applied ML research scientist focused on sequential and multimodal data. Recently I’ve been leading the **technical** direction on multimodal time-series models — dual visual encodings into an LLM, multi-stage training curricula, and a strict eval harness so we only keep changes that move the metrics. Before that: generative and representation learning for time series, including image-based transforms and irregular sampling. PhD Technion; publish NeurIPS/ICML/ICLR. I own this work hands-on — architecture, training, and gating what ships. I want that same problem — **representing series so an LLM can actually use them** — in a setting where the signals are real and the scale is large. Health AIML is that downstream, not a new field for me.

---

## 3. Pillar scripts

### A. Specific interest in health AI (~45–60s)

Shirley is likely to ask this — Tyler named it as an HM focus; he is not in the room. **Do not** rewrite yourself as a health researcher. The honest answer is: your research interest is **TS representations for LLMs**; health is the same problem at scale.

> The thing I actually work on is how to **represent time series so an LLM can work with them** — not dump numbers into context and hope. Dual visual encodings, alignment curricula, eval gates: the bet is that perception of the series is the bottleneck, then language reasoning can sit on top. Health and fitness is not a different scientific angle for me. It’s the same problem downstream, at scale: messy longitudinal signals, often with another modality, and you only keep a change if eval moved. That’s the setting I want — real series, real users — not a pivot into being a health specialist.

**If she probes “why health, then?”**  
> Because that’s where those series already exist densely and the answers get used. The research question doesn’t change; the data and the eval bar do.

**If she probes “why not a pure foundation-model / TS lab?”**  
> I want the series to be real and the eval to be consequential. Privacy and on-device constraints make the *representation* problem more interesting, not a reason I became a clinician.

**If she probes “you’re not a clinician.”**  
> Correct — and I’m not trying to be. I care about the representation and the LLM, not diagnosis. Health is the application surface.

### B. Interest in Apple (~45–60s)

Tyler listed this because **HMs use it as a filter, not a trivia quiz.** Almost every candidate has a rehearsed “I’m excited to work at Apple.” Shirley has heard that sentence this week. She is not scoring product knowledge or brand enthusiasm.

**What she is actually listening for**

| Not the signal | The signal |
|----------------|------------|
| Do you know Watch / Health app features? | Can you say why **this org’s setting** is the right place for *your* work? |
| Are you excited to work for Apple? | Will you still want the job once it’s privacy, on-device, slower publication, health/fitness series — not a ChatGPT lab with Apple on the resume? |
| Did you memorize the JD? | Did you **choose constraints** (device-resident series, foundational TS/multimodal layer, eval that isn’t a leaderboard) rather than the logo? |

It’s a **disambiguation** question: tourist vs someone who picked *this* research setting. A pretty paragraph that would also work at Google Health or OpenAI is a miss. A short, specific choice is a hit.

**Spoken (keep it a choice, not a fan letter):**

> I’m not here for the brand. The reason it’s Apple is the setting of the same problem I already work on: the series already live on the device, Health AIML is building the foundational TS / multimodal layer rather than a chatbot wrapper, and privacy / on-device are constraints on the *representation* — not a side quest. That’s a different place to do TS-for-LLM than a paper lab or a digital-health startup. I don’t need product trivia to mean that.

**If she probes “so you just want a well-resourced lab?”**  
> Resourcing isn’t the discriminator. The discriminator is where the signals are and what the eval is allowed to be. That’s Apple Health AIML for this problem; it wouldn’t be a generic FM lab.

**If she probes “why Apple Health vs Google Health?”** (drill 2026-08-20: do **not** say the company doesn’t matter)  
> I won’t pretend the core question is unique to Apple. Representing wearable series so a model can use them is the same class of problem there or here. What I’m choosing is the setting: the series already live on the device, this team looks like the foundational representation layer rather than a health chatbot, and privacy / on-device change how you build that representation. I’m in Seattle; this seat is that problem — not the logo.

**Avoid:** Watch internals; IP fishing; “I love Apple products”; a second JD-shaped health pitch; excitement as the lead; **impact at scale / millions of users / safe-AI slogans** (generic); “I’m an academic, the company doesn’t matter.”

**Locked ~50s combining health AI + Apple** (after 2026-08-20 drill): [`2026-08-20_why-apple-health-drill.md`](2026-08-20_why-apple-health-drill.md).

### C. Most impactful LLM training run (core of the call)

**Detail (numbers, ablations, bugs, 9B/27B):** [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md) — memorize §1 spoken; pull from the rest. **Drill 2026-08-20:** [`2026-08-20_training-run-drill.md`](2026-08-20_training-run-drill.md) — run not a project; no her paper; no “images keep all information.”

**Pick one run and stick to it:** multimodal Qwen3.5 VLM fine-tune / curriculum at **9B ↔ 27B** (dual visual encodings → LLM). Frame honestly as **major multimodal training run you owned**, not multi-trillion-token pretrain-from-scratch. Cite the **8B** campaign for the measured champion and most ablations.

**Spoken structure (~2–3 min, then let her dig):** full script in the detail file §1.

1. **Problem** — time-series reasoning with an LLM; single visualization encoding was insufficient.  
2. **Architecture** — line-chart encoding (trend/amplitude) + delay-embedding image (structure); fuse both into the LLM.  
3. **Training design** — multi-stage: (i) align vision to “see” series, (ii) teach LM to answer; LoRA / PEFT; config-driven sweeps; multi-GPU DDP.  
4. **Scale** — **9B and 27B** class; recipe proven on 8B; pilots before full runs.  
5. **Eval gate** — tiered eval; cheap pilots → expensive full benchmarks; no ship without metric move.  
6. **Hard call** — TR synth **26.9 → 21.9**; **killed it**; went back to data generation.  
7. **Result** — 8B stock **0.62 → ~0.90** TSExam, TSRBench **~0.40 → ~0.45**; 27B FT TSExam **~0.92**. Do not claim 9B/27B won TSRBench.

**Probe bank (one sentence each; full answers in detail file §10):**

| Probe | Pocket |
|-------|--------|
| Why two visual encoders? | Complementary failure modes: trend vs dynamical structure (ChatTS num 0.17 vs 0.71 vs dual 0.79) |
| Why not text-only TS? | Perception bottleneck; would compare to a native TS encoder on *their* signals |
| LoRA vs full FT? | Cost / iteration; r64/r128 sweet spots; r256 hurt |
| DDP / infra pain? | Sampler 1/8 data, adapter-chain +13 pp, Q35 EOS/thinking eval bugs |
| How do you know it generalized? | Held-out HF + TSRBench; slice gates; parse-miss ≠ accuracy |
| Pretrain vs fine-tune honesty | Fine-tune / adapter / curriculum — not GPT-scale pretrain |

### D. Hard questions under this story

The story’s vulnerability: *“same problem, health is just downstream”* can sound like you don’t care about the team, can’t transfer to wearables, or are shopping any multimodal seat. Drill these until the answer is 20–40s, then stop. **Don’t** repair them by becoming a health person.

#### Fit / motivation (health AI · Apple)

**“If it isn’t a different scientific angle, why this team and not any TS–LLM group?”**  
> The *question* is the same. The *setting* isn’t. Academic TS–LLM is public benchmarks and a leaderboard. Here the series are longitudinal, user-specific, privacy-constrained, and eval is not “did TSExam move.” I want that constraint on the representation problem. I’m not claiming a new identity. I’m claiming the right place to do the work.

**“You have no health papers. Why you instead of someone who does?”**  
> A health-ML hire often has the domain and a classifier. This seat is foundational representation / multimodal / TS + models that reason. That’s what I actually trained. I’ll learn the health-specific failure modes from the team — I won’t fake that I already have them. What transfers: how you represent a series, how you curriculum-train, how you kill a run when the metric you care about moves the wrong way.

**“This sounds like you’ll keep working on your VLM paper on our data.”**  
> If year one is a health-specific encoder or eval harness, that’s the job. I don’t need to keep matplotlib + DINO. What I won’t do is pretend the science is “health” when the science is “how the model sees the series.” I want the representation work *on your signals*, not a reprint of TSRBench.

**“Are you shopping any Seattle GenAI / multimodal role?”**  
> I’m looking for IC work where I own TS / multimodal training. This seat is high priority because the problem matches — represent series so a model can use them, on real signals — not because it’s convenient. *(Don’t volunteer SCOT. TTD is closed. If pressed on other processes: a few science roles, including Bosch RTC multimodal FMs; this is the TS→LLM + real-signals + Seattle match.)*

**“Why Apple, not Google/Meta FM lab or a digital-health startup?”**  
> Apple is where the series already live on the device, and Health AIML is building the foundational TS / multimodal layer, not a chatbot wrapper and not a clinic. I don’t have a Watch roadmap. The pull is representation research that has to survive privacy and platform constraints.

**“Why not forecasting? That’s also time series at scale.”**  
> Forecasting is one task on a series. I moved to *reasoning over series with an LLM* because perception of the series was the bottleneck I wanted. This role’s interesting layer is representation + multimodal, not a pacing or demand model.

#### Transfer to wearables / their methods

**“PPG, ECG, accel aren’t UCR line charts. Why would your encodings transfer?”**  
> They wouldn’t, as a drop-in. Chart + delay was an inductive bias for generic series, not a proposal to plot Watch PPG into Qwen-ViT. The transferable idea is **complementary representations** — one view loses information. On health signals I’d ask which encoding preserves the structure that matters (morphology, time–frequency, long-horizon behavior), then eval. I would not port matplotlib.

**“We use a dedicated time-series encoder into an LLM, not images. Why images?”**  
> Images were a way to steal a strong visual prior when the LLM couldn’t see the series. A native TS encoder is the more honest inductive bias if you have the data. I wouldn’t die on matplotlib. I’d compare encoder families — native TS, visual, speech-FM transfer, maybe both — with the same eval gate. Same bottleneck: the LLM doesn’t perceive the series until you represent it.

**“We’re doing sensor / motion foundation models and probing speech FMs on wearables. You’re a VLM person.”**  
> Same bottleneck, different encoder. They get a representation of a wearable series that transfers; I fused two views into an LLM. I’d rather *compare* those representation families on the team’s tasks than insist on VLMs. Probing a strong pretrained encoder is often the right first move under data scarcity — I’ve lived the “don’t stack more training on a bad mix” version of that.

**“9B / 27B won’t run on-device.”**  
> Those runs were for iteration and ceiling, not a deployment proposal. Validate the representation at a scale you can ablate; then ask what has to freeze, probe, or distill for the platform. I have not shipped on-Watch. I won’t pretend 27B is the product.

**“Wearables are irregular, missing, multi-rate. Your benchmarks look clean.”**  
> Irregular sampling is a first-class representation issue, not a preprocessing footnote — that’s why I worked on irregular TS completion / masking, not only clean UCR. I won’t overclaim I modeled PPG dropouts. I will treat missingness as part of how the model sees the series.

#### Eval / judgment

**“Your metrics are TSExam / TSRBench. That’s not health.”**  
> Correct. Those were instrumentable research north stars. Here I’d expect to **learn the team’s eval** — slices, abstention, the failure that actually matters — not import TSRBench. The transferable habit: don’t ship on a metric that doesn’t measure the error you care about. I already track parse-miss separately from accuracy because format failure isn’t reasoning.

**“LLMs in health are dangerous. Your eval is MCQ accuracy.”**  
> MCQ was a proxy I could iterate on. It is not a safety case. In this setting I’d expect wrong answers and overconfidence to be first-class, including when to abstain. I would not claim my current harness is that eval. I would claim I won’t decorate an LLM until the metric matches the failure mode.

**“What would you refuse to ship / kill here?”**  
> Same as the training run: if a flashy LLM wrapper hurts temporal structure, calibration, or a slice we actually care about, kill it and go back to data or representation. Don’t stack more SFT.

**“What does year one look like if you’re not becoming a health specialist?”**  
> (1) Learn *their* series and the eval that matters. (2) Representation experiments under *their* compute and privacy budget — what encoding lets a model use the signal. (3) Honest negative results. I would not spend year one proposing Watch features or playing clinician.

#### Training-run (only if she goes deep)

Keep §3C one-liners. Extra under this story:

**“Isn’t rendering series as images a hack?”** (drill 2026-08-20: never “keep all information”; don’t dunk on TS-encoder maturity)  
> Images were a way to steal a visual prior when the LLM couldn’t see the series — not because plots are the true representation. One view still loses information; that’s why I used two. A native TS encoder is the more honest bias if you have the data. I wouldn’t reprint charts on PPG. I’d compare encoder families on your signals with the same eval gate.

**“You only fine-tuned. We need foundation-scale training.”**  
> Honest: I owned multimodal training runs at 9B/27B — curriculum, LoRA, DDP, eval gates — not pretrain-from-scratch. The muscle is designing the run and gating it, not claiming GPT-scale pretrain.

---

## 4. Logistics pocket (only if she asks)

Tyler already has work auth, Seattle, FT, on-site. **Do not volunteer.** If she asks:

> US permanent resident (green card). Based in Seattle. Full-time IC. On-site Seattle is fine. Available now / can align start with the team (BGU academic leave through Oct doesn’t block FT start).

Comp: only if she raises it — factors already named by Tyler (experience, interview performance, team comps). Prefer level/fit first; public base range known.

---

## 5. Anti-patterns for *this* HM

| Avoid | Do |
|-------|-----|
| Lab-PI / grant / “my students…” | “I designed / trained / gated…” |
| JD-adapted health passion / “overconfident LLMs in health” as the lead | **Representing TS so LLMs can use them**; health = same problem at scale |
| Claiming clinical expertise | You’re a TS/LLM person; health is the application surface |
| Generic Apple fan pitch | Devices + foundational TS/multimodal layer, not gadgets |
| Forecasting-company story as lead | Forecasting is one use of a series; lead with TS → LLM representations |
| Dumping paper list | One training-run narrative + offer depth |
| Impact at scale / millions of users / “safe AI” as the lead | Device-resident series; privacy as a **representation** constraint |
| “The company doesn’t matter” | Question same; **setting** different; this seat in Seattle |
| Passion / “work you are doing” / reprinting the VLM | Year one: *their* series, *their* eval, ablate encoder families |
| “Leading a project” / name-dropping her workshop paper | One **run**: numbers + kill; two-stage only if **she** goes there |
| “Images keep all information” / “TS encoders aren’t mature” | One view loses information; compare encoder families; don’t port matplotlib |
| “RelCon is too small / they need a billion-param IMU FM” | ~4M is on-device perception. LLM hire is the **language** layer |

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
