# Siemens loop — prep plan — revised 29 Oct 2026

Replaces the 28 Oct rotation where the two conflict. Source is **Danielle Robinson**, 29 Oct: she works with Bing Xiang and Ramesh Nallapati and described the hours. Do not quote her on the call. Danielle Chandler is the recruiter. Two different people.

**Loop:** Tue 3 Nov 2026, 1:00–4:00 PM PST. Wed 4 Nov, 4:00–7:00 AM Thailand.
**Window:** 29 Oct through 2 Nov. About 5 hours 10 minutes a day. 2 Nov is consolidation. No new topic that day.
**Logs:** [`mocks.md`](mocks.md). Recall: [`2026-10-28_breadth-recall.md`](2026-10-28_breadth-recall.md). Screen: [`2026-10-23_huzefa-debrief.md`](2026-10-23_huzefa-debrief.md). Stories: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md).

## What she confirmed

| Hour | Person | Domain |
|------|--------|--------|
| 1:00–2:00 PM PT | Bing Xiang | Breadth **or** depth. He leads the applied-science team. |
| 2:00–3:00 PM PT | Vivek Govindan | **System design.** He is an engineer. High-level, open-ended, then how you would optimize it. |
| 3:00–4:00 PM PT | Ramesh Nallapati | The other of breadth and depth. |

She did not say which of Bing and Ramesh takes depth. Do not assign it.

Likely, not guaranteed: design may be PDE data generation and how to scale it. Breadth will probably look like the phone screen. Depth is usually a paper on the CV, including one where he is not the main author.

Not established: the questions, the breadth subtopics, and which of Bing or Ramesh takes depth. Coding is still unconfirmed. Public titles stay unverified. The cards are in [`README.md`](README.md).

## What the three hours are for

1. **Depth.** Defend any paper on the submitted CV: problem, why prior work failed, contribution, algorithm, objective, training, inference, result, ablation, limit, and what he personally did. Do not claim implementation he did not do.
2. **System design.** Design a scientific pipeline and then optimize it. PDE data generation and scale come before predictive maintenance. Maintenance and alerting stay as a fallback, not the default.
3. **Breadth.** Applied reasoning in the style of the Huzefa screen, not a definition drill.

## Time

Rotate which technical block is last. The extra depth and design time is her feedback. It is not a claim that breadth is easy.

| Block | Time |
|-------|------|
| ML depth | 100 min |
| ML system design | 100 min |
| ML breadth | 70 min |
| Behavioral | 20 min |
| Review and log | 20 min |

One question, then wait. No hints until the end. Score after. He may stop. A short answer is not a miss. A design with no bottleneck and no optimization does not get credit for the architecture. A depth or design mock is 20–25 minutes: one opening question and at most three follow-ups.

The same miss keeps showing up. A first answer names one mechanism and skips the other: the M-step when the E-step is frozen, reconstruction error when the fault is the anomaly, calibration when the task is a rank. The second miss is a list of fixes before a measurement: node-hours, a profile of \(K(T_E+T_M)\), precision at K. The third is a formula he cannot say for a paper on the CV. The fourth, from 30 Oct, is a larger model and a learned map before the checkpoint at step 6,000. Depth questions go to a paper not yet defended. Breadth mocks wait until early stopping, AdamW, and dropout can be said cold.

## CV papers

The submitted PDF is not in this repo. This matrix is only the titles the Siemens notes already call “on the submitted CV.” Anything else on the PDF is still uncovered. Do not fill the gap from the FinTech experience file. That file uses different years and different numbers.

Level A is a 20-minute defense. Level B is 5–10 minutes plus follow-ups. Level C is 2–3 minutes: motivation, contribution, result. C is the floor for every line on the PDF.

| Paper | Venue | Target | Now |
|-------|-------|--------|-----|
| Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting | NeurIPS 2026 | A | Partial. The 28 Oct depth mock was the Koopman baseline, not this paper’s generative model, sampling, or cost. |
| Closing the Loop: Co-Evolving EM for Irregular Time Series Generation in Lifted Representations | NeurIPS 2026 | A | Motivation said, 29 Oct, 7.0. The theorem was not stated. The classical ELBO write-up is not the paper. Read the PDF before another telling. Not the Bosch story. |
| Distilling the Knowledge of Koopman Operators | NeurIPS 2025 | A | Not defended. |
| ImagenTime | NeurIPS 2024 | A | Behavioral only. No paper defense: objective, training, inference, ablation. |
| Multifactor Sequential Disentanglement via Structured Koopman Autoencoders | ICLR 2023 | B | Named only. |
| Forecasting Sequential Data Using Consistent Koopman Autoencoders | ICML 2020 | B | Named only. |

For a Level A paper: why this approach, the algorithm, the objective, training, inference, the bottleneck, the strongest baseline, the ablation that carries the claim, where it fails, and which decisions were his. Depth mocks pick a paper at random, including a paper he did not lead. Do not keep returning to Koopman generative operators.

## System design — Vivek

Open-ended. Clarify, then architecture, then he changes a constraint or names a bottleneck. Optimize after a profile. Do not open with more GPUs or a surrogate. Keep a mock to 20–25 minutes and three follow-ups.

Design mock 1 is logged (29 Oct, PDE generation, 7.0): [`mocks.md`](mocks.md). The 100,000-trajectory shortfall landed. The later counts used wall-clock instead of the remaining node-hours. Storage and a PDE residual were not said. The repair-versus-resimulate choice stays unscored.

Design mock 2 is logged (30 Oct, industrial time series, 7.0). The CFD opening is unscored. Say the sensor-time token, the observed-only loss, and latency separate from throughput before another design. Two design mocks, both 7.0.

**A. PDE data generation.** Which PDE family, which systems, resolution, how many runs, parameter ranges, initial and boundary conditions, accuracy, compute, and the downstream task. Solver, sampling, mesh or grid, time integration, stability, validation, storage. Independent runs across workers, CPU versus GPU, scheduling, load balance, failure and checkpoint. Schema, provenance, compression, layout, streaming versus offline. Then the bottleneck: resolution, adaptive sampling, a surrogate, fidelity against throughput. Check convergence, conservation where it applies, coverage, and whether a downstream model improves. The point is the system, not a new specialty in numerical PDE.

**B. Train on the trajectories.** Representation, mixed resolutions, sampling, architecture, GPU use, distributed training, checkpoints, validation, long-horizon rollout, generalization across parameters. Koopman, forecasting, and sequence models are relevant when they answer a design choice.

**C. Ten times the data, same budget.** Baseline, profile, separate solver cost from orchestration, estimate the gain, check that the data is still useful.

**D. A learned surrogate.** Data, architecture, constraints, uncertainty, error over a long rollout, out-of-distribution detection, when to call the solver, validation against that solver.

## Breadth — the screen, not a syllabus

Huzefa, 23 Oct, one hour. He will recommend proceeding.

| Block | What he asked |
|-------|----------------|
| Project | Multimodal model, a few minutes: architecture, the bet, Omri’s role, results. |
| ML | Overfit, underfit, regularization. |
| Coding | He wanted SGD. The platform swapped in bagging. Stating the three steps was enough. He did not require a finished vote. |
| Question | What a principal owns. The sharper kill-result question was not asked. |

That is the screen breadth actually resembled: a resume project, then a diagnosis, then a practical constraint. Robinson’s earlier private examples (DataLoader, padding, attention) were not this hour. Do not prepare as if they were.

Breadth mock 2 is logged (29 Oct, new factory, 6.5): [`mocks.md`](mocks.md). Shift and the time split landed. Calibration and the dollar threshold did not. The review sheet is [`2026-10-29_breadth-review.md`](2026-10-29_breadth-review.md). The 28 Oct precision-at-K exercise in [`mocks.md`](mocks.md) is still unanswered.

Breadth mock 3 is logged (30 Oct, overfitting, 6.5). The checkpoint at step 6,000 was not the first move. No weight decay, dropout, or smaller model. The same-day recall is [`2026-10-30_fundamentals-recall.md`](2026-10-30_fundamentals-recall.md): 8, 4, 7, 3, 7, 8, about 6.2, not a mock. AdamW and layer norm are the two to say again. Question 7, the three experiments, was not taken. Three breadth mocks, each 6.5.

## Days

**Thu 29.** Depth mock 2 is done: Closing the Loop, 7.0. Design mock 1 is done. Breadth: one applied evaluation question in the screen’s style. Behavioral: the 28 Oct corrections only. “My students,” “insist,” one number, EDM as the sampler. Not a second ImagenTime mock.

**Fri 30.** Breadth mock 3 is done: overfitting, 6.5. The fundamentals recall is done and is not a mock. Design mock 2 is done: the CFD opening was aborted and is unscored. The time-series foundation model is 7.0. The token was a metadata prefix, and 500 factories were treated as 500 machines. Say the sensor-time token before another design. Behavioral: story **B**, the two controls, if it was not already done. Do not retell story C, and do not invent the audit.

**Sat 31.** Depth recall, not a mock: Koopman, diffusion from his own papers, and the Closing the Loop objective. The classical ELBO is not that theorem until the PDF says so. One question, then the correction. Design: say the token, the mask, the loss, and the latency path. Not a second scored design. Breadth: AdamW and layer norm from memory. Behavioral: story **E** only with the mask and interpolation.

**Sun 1.** Depth: distillation and structured Koopman, then a random CV line. Design: scenario D, surrogate versus solver. Breadth: one mixed question. Behavioral: the stop rule, on story **C** or **B**. Question 7 from the ImagenTime mock stays unanswered until he answers it on a different story.

**Mon 2.** Consolidation. Random papers, including one he did not lead. One design, training or a surrogate, with the node-hour ledger and one residual. Not another generation pipeline. One mixed breadth question. Story review, not new material. One page: six papers, the design sequence, the screen diagnosis, the open misses (precision at K, the stop rule, no number on ImagenTime, the 60,000 node-hour split).

**Tue 3.** No study block. Sleep for a 4:00 AM Wednesday start.

## Stories

Twenty minutes. “I,” one metric, the decision, the limit. Do not open with the lab, the headcount, or the grant.

Behavioral mock 1 is logged (28 Oct, ImagenTime, 8.0): [`mocks.md`](mocks.md). “My students” and “insist” are still the breaks. The unanswered close is a stop rule after someone wants two more weeks.

Behavioral mock 2 is logged (29 Oct, story C, 8.0). The gates and 26.9 to 21.9 landed. Reasoning was again said as 28 to 29.2. The bank’s pair is 29.5 to 31.2. “We agreed” is the leadership miss. The next behavioral pass is not this story. Do not invent the audit.

| Theme | Use |
|-------|-----|
| A direction others resisted | **A** ImagenTime. Already used. Corrections only. |
| A lever that failed | **C** TR kill |
| Conflicting measurements | **B** dual tower |
| A partner and a constraint | **E** Bosch. Interpolation plus an observation mask. |
| Poor performance, or a conflict that is not technical | Not in the bank. Do not add one this week. |

## By 2 Nov

One Level A defense of a paper not yet used: distillation or Koopman generative operators. Closing the Loop only from the PDF, and not as the Bosch story. The sensor-time token, the observed-only loss, and latency separate from throughput. AdamW and layer norm said without notes. The stop rule, said as his decision.
