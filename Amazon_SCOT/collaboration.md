# Collaboration — NeurIPS 2026 (paper + workshop)

Status as of Sun 2 Aug 2026. Artifacts in-repo under [`papers/`](papers/) and [`workshops/`](workshops/).

**Confidentiality:** Paper is under review (anonymous). Do not post publicly; on Monday with Boris, OK to discuss status and technical substance.

---

## Joint forecasting paper — KGO

| | |
|---|---|
| **File** | [`papers/neurips2026_kgo_koopman_generative_operator.pdf`](papers/neurips2026_kgo_koopman_generative_operator.pdf) (47 pp; submission id 27300) |
| **Venue** | NeurIPS 2026 |
| **Status** | Under review (anonymous author block in PDF) |
| **Reviews** | Rebuttal **written + submitted**. R1: concerns addressed (responded). R2: no response yet (wait till deadline). Remaining: respond to AC **meta-review** — summary of responses + revision changes; wait for R2 window |
| **Title** | Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting |
| **Collaborators** | Boris Oreshkin + others (full list not in anonymous PDF — confirm with Boris if needed). Ongoing generative forecasting thread also involves **Mayank Jauhari** |
| **One-line problem** | Probabilistic forecasting needs structured dynamics + expressive uncertainty + **fast inference**; diffusion/flow are flexible but iterative/expensive |
| **Method (speakable)** | **KGO** = forecasting as evolution of structured uncertainty: **KoPE** + **KoFM** (single-step) + **AUG** (adaptive **aleatoric** — **results already in paper**) |
| **Open thread (Boris)** | **Side:** epistemic uncertainty (aleatoric/AUG already done); offered, not finished — mention only if natural ([`contribution-plan.md`](contribution-plan.md)) |
| **Main contribution bet** | Bridge existing sim→FM line into modern diffusion/FM generative (efficient sampling) |
| **Headline results** | ProbTS: best CRPS on **12/17**, best NMAE on **11/17**; strong long-horizon; ablations: −KoPE/−KoFM/−AUG hurt CRPS up to ~12% / ~26% / ~16%; **≥25×** faster inference vs iterative generative models |
| **Your IC contribution** | Technical ownership of **flow matching** and **Koopman mechanics** in KGO (the structured transport / dynamical pieces — not only experiments/writing) |

### Rebuttal crib — KoPE stability (if Boris / AC digs)

**Reviewer concern:** repeated application of the same \(K\) (\(\tilde{z}_{N+i}=K^i z_N\)) can explode (spectral radius > 1 → unstable rollout).

**Response (three layers):**

1. **Bounded power via patching** — horizon is in patches, not raw steps; in practice \(K^i\) with \(i \lesssim 30\), not hundreds of matrix apps.
2. **Normalize after each \(K\)** — activation normalization after every application of \(K\) (submission behavior) damps runaway growth.
3. **Spectral constraints (rebuttal add-on)** — added in rebuttal; stabilizes the operator properly. **Fixes the issue**; slightly more expensive; **not in the original submission** — flag honestly as revision / rebuttal work for the AC summary.

**Speakable (~20s):**

> On KoPE stability — fair concern with repeated \(K\). Patching keeps the power small — under about thirty — and we already normalize after each apply. In the rebuttal we also added spectral constraints on \(K\); that closes it cleanly, with a small cost bump, and we’ll call it out as a revision change for the AC.

### Technical crib — KoFM closed form vs ODE (if Boris presses math)

**Issue:** Main text writes \(\dot{z}=Az+b\) then \(z^{(1)}=e^{(1-\tau)A}z^{(\tau)}+(1-\tau)b\). Exact integration of that ODE is
\(z(1)=e^{A(1-\tau)}z(\tau)+\int_0^{1-\tau}e^{Au}b\,du\) (= \(A^{-1}(e^{A(1-\tau)}-I)b\) if \(A\) invertible) — **not** \((1-\tau)b\).

**What is exact:** Homogeneous piece \(e^{(1-\tau)A}z\) (App. B.2.1). Affine at inference \(\Delta\tau=1\): App. B.2.3 uses \(z_1=z_0C+b\) with learned bias — equivalent to absorbing the true inhomogeneous integral into \(b\).

**Honest framing:** \((1-\tau)b\) in the main text is a convenient parameterization / learned affine offset (scaling into network \(b\)), not the literal variation-of-constants formula for all \(\tau\). Fine under CRPS training; don’t overclaim “we integrate \(\dot{z}=Az+b\) closed-form verbatim.”

**Speakable (~15s):**

> Homogeneous transport is exact matrix-exp. The bias term is written as \((1-\tau)b\) for simplicity — at single-step inference that offset is just a learned vector equivalent to the true affine integral; during training it’s a parameterization of the inhomogeneous piece rather than spelling \(A^{-1}(e^{A\Delta\tau}-I)b\).

### Technical crib — AdaGN in KoFM (easy to forget)

**Job:** Inject each KoPE future latent into the FM interpolate **before** matrix-exp transport. History enters as affine modulation, not concat into the ODE.

**Pipeline slice:** \(x^{(\tau)}=(1-\tau)\epsilon+\tau x\) → MLP → \(h^{(\tau)}\) → **AdaGN** with \(\tilde{z}_{N+i}\) → \(\tilde{z}^{(\tau)}\) → \(e^{(1-\tau)A}(\cdot)+(1-\tau)b\) → decode.

**Formula:**
\[
\tilde{z}^{(\tau)}_{N+i}=\mathrm{AdaGN}(h^{(\tau)}\mid\tilde{z}_{N+i})=\gamma(\tilde{z}_{N+i})\,\mathrm{GN}(h^{(\tau)})+\beta(\tilde{z}_{N+i})
\]

| Piece | What |
|-------|------|
| **GN** | GroupNorm on lifted interpolate — stabilize scale |
| **\(\gamma,\beta\)** | Learned linear maps from KoPE vector → scale & shift (FiLM / Dhariwal–Nichol AdaGN) |
| **Per patch** | Each horizon patch \(i\) uses its own \(\tilde{z}_{N+i}\) → its own \(\gamma,\beta\) |

**Is / isn’t**
- **Is:** FiLM-style conditioning of generative features on structured dynamics
- **Isn’t:** concatenating lookback into noise; isn’t AUG; isn’t the matrix \(A\)
- AUG ablation “conditioning underperforms” = det/prob coupling, **not** this AdaGN block

**One-liner:** AdaGN turns each KoPE latent into \(\gamma,\beta\) that restyle normalized FM features so closed-form transport starts from a history-conditioned state.

---

### Why this sells SCOT (IC bridge)

- Same cost/latency theme as Mengfei dinner and March talk — but here you have a **number** (≥25×) and a concrete mechanism (single-step KoFM), not a roadmap slide
- Complements Boris’s sim/foundation line: expressive generative forecasting that can actually *serve*
- Quantile-vs-trajectory story: full predictive distributions / trajectories with calibrated AUG

### 30–45s spoken update (draft)

> On the NeurIPS paper — Koopman Generative Operators — rebuttal is in. One reviewer already said their concerns are addressed; we’re waiting through the window for the second. Next write-up is mainly a short AC meta-review response summarizing changes. Technically: forecasting as evolution of structured uncertainty — KoPE for latent trajectories, KoFM for single-step generation instead of iterative sampling, AUG for per-variable/horizon aleatoric uncertainty. ProbTS: strongest on most CRPS/NMAE settings; ≥25× faster inference than iterative generative. I owned the flow matching and Koopman mechanics. Happy to sync on the AC note if useful.

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
- Paper: AC meta-review response — who drafts the summary of responses + revision diffs? (rebuttal already submitted; R1 closed; wait on R2)
- Paper / next science: main line = efficient generative forecasting at SCOT scale; side = epistemic thread from KGO if he still cares
- Workshop: light — congratulate acceptance; attracting strong papers (ops later if needed)
- After NeurIPS cycle: natural follow-on inside SCOT Forecasting / Labs (KGO serving cost? synthetic pretrain + KGO?)?

Full question list (incl. career/fit): [`questions-for-boris.md`](questions-for-boris.md).
