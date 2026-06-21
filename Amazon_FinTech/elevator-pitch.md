# Elevator pitch — PS1 intro

**Use:** Opening of the 10–15 min intro with Karan. Stop when he asks a follow-up — that's a win.  
**Target:** ~160 words · ~90 sec at a normal pace (not a monologue).  
**Frame:** IC applied scientist — what *I* built.

---

## Main script (say this)

I'm Omri. Applied ML scientist working on generative and multimodal modeling on sequential data. PhD from Technion. I publish mostly at NeurIPS, ICML, and ICLR, and I care about the full stack: model, data, training, and eval.

Right now my main project is teaching VLMs to **reason over time series** — questions, numeric answers, how things relate over time. You can feed series as text, but it's **inefficient**; from **ImagenTime and similar projects** we learned VLMs do better when we **render series as images**. I built the training and eval stack — 100-plus experiments on eight GPUs. On **TSRBench**, the public north-star benchmark, our **open 8B model** scores **~46% overall** — the first open-source model at that scale that sits **just below frontier proprietary systems**, GPT-class models orders of magnitude larger.

Before that, generative work on messy sequential data — gaps, irregular timing. Same habit: fix data and eval before you trust the headline number.

Why FinTelligence? I want to see this at real scale — multimodal finance docs, precision actually matters, eval before ship. I've built research stacks; I want to do it with peer scientists and engineers when the workload is payment ops, not in a vacuum.

Happy to go deep on whichever part you want.

---

## If he stays quiet (~30 sec more)

One thing I'd flag: I killed a training mix that looked good overall but regressed on hard reasoning slices. I'd rather catch that in eval than ship it. That mindset is why this team fits.

---

## Beat map

| Block | ~sec | One line |
|-------|------|----------|
| Who | 15 | Name, generative + multimodal sequential, full-stack IC |
| Flagship | 40 | Goal → images → I built stack → TSRBench ~46%, open 8B vs frontier |
| Before | 10 | Messy sequential data, eval discipline |
| Why here | 25 | Scale, precision, peers, not solo research |
| Close | 5 | "Go deep on whatever you want" |

---

## 45-second cut

Applied ML on generative and multimodal sequential data — NeurIPS, ICML, ICLR, but I build systems, not just papers. Main project: **TS reasoning via image-based VLMs**; on **TSRBench**, our open **8B** scores **~46%** — first open-source model at that scale just below trillion-scale proprietary frontier. I'm here for FinTelligence — finance docs at scale, precision, eval gates — and to work closely with peer scientists and engineers.

---

## Depth ladder (right level for Amazon)

Intro = **problem → approach → you built it → one number**. Save mechanics for when he pulls the thread.

| If he asks… | Say (one layer deeper) |
|-------------|-------------------------|
| "What's the goal?" | Exam-grade reasoning on general time series — MCQ, numbers, temporal relations — not classic UCR classification. |
| "Why images, not text tokens?" | Text works but is inefficient; ImagenTime and our generative TS-as-images line showed stronger results; VLMs already have a vision stack. |
| "How exactly?" | Two complementary views — line chart plus delay-embedding plot — fused into one LLM. *(only here)* |
| "What did you personally build?" | Dual-tower architecture, two-stage training, tiered eval harness, 100+ config sweeps on 8 GPUs. |
| "TSRBench numbers?" | 8B **~46%** overall on 12 tasks; strongest **open 8B** — verify exact leaderboard rank before PS1. TSExam (~90%) is internal sanity check in tiered eval, not the headline. |
| ML deep-dive (5–7 min) | Full stack from experience profile: curriculum, eval gates, 0.8B vs 8B, negative TR result. |

**Your risk:** skipping straight to architecture (old draft) *or* staying abstract ("reasoning over modalities") with no "I built" and no metric. This version splits the difference.

---

## Tone notes (why the old draft felt wrong)

- Real intros are **shorter sentences**, some **fragments**, fewer stacked clauses.
- Drop essay phrases ("methodology meets production constraints", "pressure-test at real scale").
- **One number per beat** — don't recite a metric laundry list.
- **TSRBench in intro, TSExam in follow-up** — external benchmark = credibility; internal exam = eval discipline, not the hook.
- ImagenTime: one name in intro as *why images*; generative TS line in "before that" paragraph stays high-level.
- Venues: one quick mention, not a credential flex.

---

## Delivery reminders

- **"I built / I ran / I killed"** — one per block so you don't sound like a lab overview.
- Pause after the **TSRBench / open 8B vs frontier** line; let him bite on eval, leaderboard, or why images.
- **"Won't you miss the lab?"** → *I want impact in gated releases and slice metrics, not grant lines.*
- If he interrupts at 30 sec, you already said the important parts.

---

## Practice log

| Date | Time (target ~1:30) | Felt natural? | Notes |
|------|---------------------|---------------|-------|
| 2026-06-21 | | ☐ | v2 — shorter, spoken tone |
| | | ☐ | |
