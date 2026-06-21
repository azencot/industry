# Elevator pitch — PS1 intro

**Use:** Opening of the 10–15 min intro with Karan. Stop when he asks a follow-up — that's a win.  
**Target:** ~160 words · ~90 sec at a normal pace (not a monologue).  
**Frame:** IC applied scientist — what *I* built.

---

## Main script (say this)

I'm Omri. Applied ML scientist working on generative and multimodal modeling on sequential data. PhD from Technion. I publish mostly at NeurIPS, ICML, and ICLR, and I care about the full stack: model, data, training, and eval.

Right now my main project is a time-series VLM on Qwen. Same series, two views — a chart and a delay-embedding image — both fed into the LLM. I built the architecture, the two-stage training, and the eval pipeline. Ran 100-plus experiments on eight GPUs. On our exam benchmark, 0.8B hits 0.89, 8B is 0.90.

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
| Flagship | 35 | Dual-view VLM, I built it, 0.89 vs 0.90 |
| Before | 10 | Messy sequential data, eval discipline |
| Why here | 25 | Scale, precision, peers, not solo research |
| Close | 5 | "Go deep on whatever you want" |

---

## 45-second cut

Applied ML on generative and multimodal sequential data — NeurIPS, ICML, ICLR, but I build systems, not just papers. Main project: time-series VLM, dual visual encodings, 100-plus experiments, 0.89 on 0.8B vs 0.90 on 8B. I'm here for FinTelligence — finance docs at scale, precision, eval gates — and to work closely with peer scientists and engineers.

---

## Tone notes (why the old draft felt wrong)

- Real intros are **shorter sentences**, some **fragments**, fewer stacked clauses.
- Drop essay phrases ("methodology meets production constraints", "pressure-test at real scale").
- **One number per beat** — don't recite a metric laundry list.
- Diffusion / ImagenTime: save for ML deep-dive if he asks; intro only needs "generative work on messy sequential data."
- Venues: one quick mention, not a credential flex.

---

## Delivery reminders

- **"I built / I ran / I killed"** — one per block so you don't sound like a lab overview.
- Pause after the 0.89 / 0.90 line; let him bite on eval or model size.
- **"Won't you miss the lab?"** → *I want impact in gated releases and slice metrics, not grant lines.*
- If he interrupts at 30 sec, you already said the important parts.

---

## Practice log

| Date | Time (target ~1:30) | Felt natural? | Notes |
|------|---------------------|---------------|-------|
| 2026-06-21 | | ☐ | v2 — shorter, spoken tone |
| | | ☐ | |
