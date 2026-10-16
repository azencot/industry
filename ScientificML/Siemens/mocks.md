# Siemens mock log

One file for every Siemens phone-screen mock (behavioral and coding). Append a section. Add a row to the index. Do not open a new file per mock.

Story source: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Coding drills: [`coding/README.md`](coding/README.md).

## Index

| Date | Kind | Focus | Break |
|------|------|-------|-------|
| 2026-10-16 | Behavioral, ~15 min | Story A — ImagenTime | GAF off-diagonal called zero. "My students." No number. EDM not separated. |

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
