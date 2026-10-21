# Siemens mock log

One file for every Siemens phone-screen mock (behavioral and coding). Append a section. Add a row to the index. Do not open a new file per mock.

Story source: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Coding drills: [`coding/README.md`](coding/README.md).

## Index

| Date | Kind | Focus | Break |
|------|------|-------|-------|
| 2026-10-16 | Behavioral, ~15 min | Story A — ImagenTime | GAF off-diagonal called zero. "My students." No number. EDM not separated. |
| 2026-10-21 | Behavioral | Story C — TR kill | Reasoning average said as 28. Tempting gain called overall. Left the kill for the audit. 0.8B deltas not said. |

---

## 2026-10-16 — Story A, ImagenTime

**Kind:** Behavioral mock, about 15 minutes. Interviewer asked; answers were not supplied in advance.

**Prompt:** Tell me about a time you set a technical direction that the people around you did not think was the obvious next step.

### What he said

After a VAE baseline, the obvious next step was native 1D diffusion. He proposed turning series into images and reusing vision diffusion. Objections he named: extra compute, vision backbones were uncommon for time series, and vision diffusion was shown on natural images. He refused to settle it by seniority and named three kill tests: reconstruction fidelity, a small-scale study, and compute. He screened transforms, kept ones he called numerically exact, saw a preliminary signal, and logged compute. Outcome he gave: one framework, lengths 24 to about 17,000, better than strong baselines, reused in follow-up projects.

On attribution he was careful. Representation and architecture moved together, so he would not claim the image step alone caused the gain. Ablation he described: matched weights, steps, and data size, against a time-series architecture and against several image transforms. Delay embeddings and STFT won; other transforms were weaker. He narrowed the claim to one working configuration, then added that it is still state of the art as far as he knows.

Asked to kill one representation, he picked Gramian angular field. He said it stores the series on the diagonal, scales badly at 17k steps, lost on discriminative and predictive benchmarks, and is mostly empty off the diagonal so convolutions see a weak 2D signal. Asked what one off-diagonal cell holds, he said zero.

### What landed

The fork was clear: native 1D diffusion versus a representation change. The objections were real. He would not pretend the gain was pure representation, and the matched-compute ablation is the right posture. "A configuration that works" is the claim to keep.

### What broke

- **GAF.** An off-diagonal cell is not zero. Map \(x_i\) to \(\phi_i = \arccos(x_i)\). A summation field stores \(\cos(\phi_i + \phi_j)\); a difference field stores \(\sin(\phi_i - \phi_j)\). The matrix is dense. The diagonal encodes the series; the rest is a pairwise field. A 17k series is a huge dense matrix, which is the scaling failure. The mostly empty image is a **line plot** (sparse, weak 2D signal, not cleanly invertible). Delay embeddings and STFT survived because the series could be reconstructed.
- **"My students"** and "I did not use my seniority" read as lab lead. Name the people who owned the 1D stack, and what evidence changed the decision.
- No comparison number. Have one ready from the story bank (short-series discriminative score about 58% over prior diffusion models; one long-series pair such as Traffic). Do not lead with "still SOTA."
- The drop from about 1,000 model evaluations to about 35 is the EDM sampler, not the image transform.
- "Numerically exact reconstruction" is stronger than the bank. Delay embeddings and STFT passed a high-fidelity reconstruction test.

### Next pass

One clean retell of the killed representations: line plot, then GAF, then why delay embeddings and STFT stayed. Include one number, and separate EDM from the representation.

---

## 2026-10-21 — Story C, TR kill

**Kind:** Behavioral mock. He stopped it once the questions had left the kill for the audit.

**Prompt:** Tell me about a time a result contradicted what you expected, and what you changed because of it.

### What he said

Multimodal time-series reasoning with several image views in a VLM, judged on TSRBench. He said the model still struggled on reasoning, with temporal reasoning near a 28% versus 25% baseline. He built extra data for temporal-reasoning tasks and set failure gates at −3 points overall and −5 points on a specific task. After fine-tuning, overall improved and some tasks rose by as much as 7 points, while temporal relations fell from 26.9 to 21.9. He killed that data and started a reasoning audit.

Asked to reconcile 28-versus-25 with 26.9-to-21.9, he separated them. 28% is the reasoning segment, an average of 5–6 tasks. 25% is the approximate random baseline for that segment. 26.9 to 21.9 is the single temporal-relations task.

On the five-point line: the exact threshold mattered less than setting it before the run. Five points is a large loss against a temporal-relations score of 26.9. A one-point drop would not kill the mix; it would need more analysis.

Asked what he did the next week, he described the audit. Three gaps: domain knowledge (seismology), format (a forecast horizon as numbers rather than a letter), and complexity (two or three segments in training versus seven or eight at inference). He tested complexity and format first, from a frequency count, with synthetic data and another fine-tune. Both the killed mix and the later fix started at 0.8B and then went to 8B. He said he used the same gates. He stopped before saying what the 0.8B run moved, or what would have blocked the 8B run.

### What landed

The kill is tied to the task the data was built for. The gates appear before the result. 26.9 to 21.9 is the right pair, and 25% is the random baseline already in the ownership card. The five-point answer matches the card: pre-commit first, and a one-point drop does not kill the direction. The three audit regimes are the right split, with seismology as the knowledge example. He kept the decision in the first person.

### What broke

The first pass hung 28-versus-25 on temporal reasoning itself. The repair of the structure is right, and the segment number is not: the card is about 29–30% before this work, and this run moved the reasoning average from 29.5 to 31.2. He also called the tempting gain "overall." Overall TSRBench had plateaued near 46%. The pre-committed floors were 3 points on overall and 5 points on any reasoning subtask.

The kill was left behind. The seven-or-eight figure in the card counts operators, not segments at inference. The 0.8B probe was judged with the kill's regression floors. A small gain passes those floors. The probe's own numbers were not said: overall about 38.2 to 40.5, reasoning about 24.5 to 25.5, and a positive 0.8B result still does not validate 8B.

### Next pass

One retell that stays on the kill: the plateau, the gate before the run, reasoning average 29.5 to 31.2 and two tasks up about 7 points, temporal relations 26.9 to 21.9, kill the mix, keep the objective. If asked what came next, one sentence that the question changed, then stop.
