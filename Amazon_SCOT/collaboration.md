# Collaboration — NeurIPS 2026 (paper + workshop)

Status as of Sat 1 Aug 2026. Artifacts in-repo under [`papers/`](papers/) and [`workshops/`](workshops/).

**Confidentiality:** Paper is under review (anonymous). Do not post publicly; on Monday with Boris, OK to discuss status and technical substance.

---

## Joint forecasting paper — KGO

| | |
|---|---|
| **File** | [`papers/neurips2026_kgo_koopman_generative_operator.pdf`](papers/neurips2026_kgo_koopman_generative_operator.pdf) (47 pp; submission id 27300) |
| **Venue** | NeurIPS 2026 |
| **Status** | Under review (anonymous author block in PDF) |
| **Reviews** | Positive initial reviews (details TBD — paste when safe) |
| **Title** | Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting |
| **Collaborators** | Boris Oreshkin + others (full list not in anonymous PDF — confirm with Boris if needed). Ongoing generative forecasting thread also involves **Mayank Jauhari** |
| **One-line problem** | Probabilistic forecasting needs structured dynamics + expressive uncertainty + **fast inference**; diffusion/flow are flexible but iterative/expensive |
| **Method (speakable)** | **KGO** = forecasting as evolution of structured uncertainty: **KoPE** + **KoFM** (single-step) + **AUG** (adaptive **aleatoric** — **results already in paper**) |
| **Open thread (Boris)** | He was interested in **epistemic** uncertainty; you offered; **not done** — strong Monday / 90-day charter ([`contribution-plan.md`](contribution-plan.md)) |
| **Headline results** | ProbTS: best CRPS on **12/17**, best NMAE on **11/17**; strong long-horizon; ablations: −KoPE/−KoFM/−AUG hurt CRPS up to ~12% / ~26% / ~16%; **≥25×** faster inference vs iterative generative models |
| **Your IC contribution** | Technical ownership of **flow matching** and **Koopman mechanics** in KGO (the structured transport / dynamical pieces — not only experiments/writing) |

### Why this sells SCOT (IC bridge)

- Same cost/latency theme as Mengfei dinner and March talk — but here you have a **number** (≥25×) and a concrete mechanism (single-step KoFM), not a roadmap slide
- Complements Boris’s sim/foundation line: expressive generative forecasting that can actually *serve*
- Quantile-vs-trajectory story: full predictive distributions / trajectories with calibrated AUG

### 30–45s spoken update (draft)

> On the NeurIPS paper — Koopman Generative Operators for efficient probabilistic forecasting — it’s still under review; initial reviews were positive. The bet is forecasting as evolution of structured uncertainty: KoPE for latent trajectories, KoFM for single-step generation instead of iterative diffusion sampling, and AUG for per-variable, per-horizon uncertainty. On ProbTS we’re strongest on most CRPS/NMAE settings, and dropping iterative sampling buys at least about twenty-five times faster inference. On my side I owned the technical pieces around **flow matching and the Koopman mechanics** — the structured transport that makes single-step generation work. Happy to dig into rebuttal experiments or how this continues after the cycle.

---

## Workshop — Foundation Models for Temporal Systems

| | |
|---|---|
| **File** | [`workshops/neurips2026_fm_temporal_systems_proposal.pdf`](workshops/neurips2026_fm_temporal_systems_proposal.pdf) (submission id 84) |
| **Venue** | NeurIPS 2026 workshop |
| **Status** | **Accepted** |
| **Title** | Foundation Models for Temporal Systems: From Forecasting to World Modeling |
| **Tagline** | Foundation models for temporal world modeling: forecasting, simulation, and reliability |
| **Your role** | Co-organizer (listed with Boris, Danielle Maddix Robinson, Ming Jin, Emadeldeen Eldele, Mayank Jauhari, Chenghao Liu, N. Benjamin Erichson, …) |
| **Boris’s role** | Co-organizer; Amazon / SCOT Principal Scientist |
| **Amazon side also** | Danielle Maddix Robinson (AWS); Mayank Jauhari (Amazon) |
| **Confirmed invited** | Rose Yu, Michael Mahoney, Abdul Fatir Ansari (Chronos), Aditi Krishnapriyan, Marinka Zitnik, Tim Januschowski, Daniel F. Schmidt, Mingsheng Long, Flora Salim |
| **Axes** | (1) forecasting & simulation tasks (2) temporal data & environments (3) temporal models (4) evaluation & reliability |
| **Next logistics** | Website, CFP, OpenReview, review load, panel — shared among co-organizers (don’t claim sole ownership with Boris) |

### 30s spoken update (draft)

> The workshop was accepted — Foundation Models for Temporal Systems — great news for us as co-organizers. I’m looking forward to it. Would be great to attract a strong set of papers that connect forecasting research to systems people actually ship. Happy to sync on ops later; doesn’t have to be today.

---

## Folder map

| Path | What |
|------|------|
| [`papers/`](papers/) | NeurIPS paper PDF(s) |
| [`workshops/`](workshops/) | Workshop proposal PDF(s) |
| [`talks/`](talks/) | Group talk slides |

---

## Open collab questions for Monday (ops)

- Paper: Amazon-side constraints on what we can say externally while under review?
- Paper: who owns rebuttal timeline / experiment backlog (your IC slice vs Boris/Mayank)?
- Paper / next science: reopen the **epistemic uncertainty** thread from KGO (aleatoric/AUG already done) — still a priority for him / SCOT?
- Workshop: light — congratulate acceptance; attracting strong papers (ops later if needed)
- After NeurIPS cycle: natural follow-on inside SCOT Forecasting / Labs (KGO serving cost? synthetic pretrain + KGO?)?

Full question list (incl. career/fit): [`questions-for-boris.md`](questions-for-boris.md).
