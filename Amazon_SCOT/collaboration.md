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
| **Method (speakable)** | **KGO** = forecasting as evolution of structured uncertainty: **KoPE** (temporally consistent latent traj) + **KoFM** (single-step generation via closed-form matrix exp in Koopman space) + **AUG** (per-variable / per-horizon adaptive **aleatoric** uncertainty) |
| **Open thread (Boris)** | He flagged **aleatoric uncertainty**; you offered follow-up work; **not done** in submission cycle — strong Monday / 90-day charter ([`contribution-plan.md`](contribution-plan.md)) |
| **Headline results** | ProbTS: best CRPS on **12/17**, best NMAE on **11/17**; strong long-horizon; ablations: −KoPE/−KoFM/−AUG hurt CRPS up to ~12% / ~26% / ~16%; **≥25×** faster inference vs iterative generative models |
| **Your IC contribution** | TODO — lock one sentence before Monday: what *you* owned (KoPE / KoFM / AUG / experiments / writing). Avoid “we” |

### Why this sells SCOT (IC bridge)

- Same cost/latency theme as Mengfei dinner and March talk — but here you have a **number** (≥25×) and a concrete mechanism (single-step KoFM), not a roadmap slide
- Complements Boris’s sim/foundation line: expressive generative forecasting that can actually *serve*
- Quantile-vs-trajectory story: full predictive distributions / trajectories with calibrated AUG

### 30–45s spoken update (draft)

> On the NeurIPS paper — Koopman Generative Operators for efficient probabilistic forecasting — it’s still under review; initial reviews were positive. The bet is forecasting as evolution of structured uncertainty: KoPE for latent trajectories, KoFM for single-step generation instead of iterative diffusion sampling, and AUG for per-variable, per-horizon uncertainty. On ProbTS we’re strongest on most CRPS/NMAE settings, and dropping iterative sampling buys at least about twenty-five times faster inference. On my side I owned **[TODO: your slice]**. Happy to dig into rebuttal experiments or how this continues after the cycle.

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
| **Next logistics** | Website, CFP, OpenReview, review load, panel — lock ownership with Boris / Danielle |

### 30s spoken update (draft)

> The workshop was accepted — Foundation Models for Temporal Systems: From Forecasting to World Modeling. Scope is forecasting plus simulation and reliability, which matches what SCOT actually cares about in production. Invited slate is locked with people like Mahoney, Chronos (Ansari), Rose Yu, Januschowski. Next I want to lock website and CFP ownership and make sure the program stays useful for SCOT forecasting, not only the academic TS crowd. What would make this most valuable from your side?

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
- Paper / next science: reopen the **aleatoric uncertainty** thread from KGO — still a priority for him / SCOT?
- Workshop: who owns website + CFP; SCOT-useful invited/panel topics?
- After NeurIPS cycle: natural follow-on inside SCOT Forecasting / Labs (KGO serving cost? synthetic pretrain + KGO?)?

Full question list (incl. career/fit): [`questions-for-boris.md`](questions-for-boris.md).
