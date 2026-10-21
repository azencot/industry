# Siemens mock log

One file for every Siemens phone-screen mock (behavioral and coding). Append a section. Add a row to the index. Do not open a new file per mock.

Story source: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Coding drills: [`coding/README.md`](coding/README.md).

## Index

| Date | Kind | Focus | Break |
|------|------|-------|-------|
| 2026-10-16 | Behavioral, ~15 min | Story A — ImagenTime | GAF off-diagonal called zero. "My students." No number. EDM not separated. |
| 2026-10-21 | Behavioral | Story C — TR kill | Reasoning average said as 28. Tempting gain called overall. Left the kill for the audit. 0.8B deltas not said. |
| 2026-10-21 | Behavioral | Story B — dual tower | Controls landed. TSExam first called a win, then corrected to flat. Gain grouped prediction with decision-making. |
| 2026-10-21 | Behavioral, full transcript | Story A — ImagenTime | Attribution held. Opening still has no number and still says "my students." Four-week plan stayed generic. |
| 2026-10-22 | Behavioral, full transcript | Story E — Bosch | EM loop told in place of interpolation plus an observation mask. No number. Collaboration stayed general. Maintenance named as compute. |

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

---

## 2026-10-21 — Story B, dual tower

**Kind:** Behavioral mock. He stopped it when the follow-ups became a results table.

**Prompt:** Stay with the dual-tower model. The gain could have been a second encoder and a larger visual-token budget. What did you check before you were willing to say the two views were complementary?

### What he said

VLMs are already strong on line plots. Other image representations reveal different features, so he combined chart and delay-embedding views. Charts keep scale and numerics. Delay embeddings keep dynamics and topology. A preliminary comparison on TSExam and a TSRBench subset favored the dual view over either view alone. He did not trust that, because the dual model also had more weights and more tokens. He matched weights, tokens, and data, and compared chart, delay, chart+chart, delay+delay, and chart+delay. Chart+delay won. On TSRBench he gave chart about 45, chart+chart 44.8, delay+delay 42.3, delay unknown, and chart+delay 53.2.

Asked for the full TSExam scores, he corrected the preliminary claim. Single and dual views were about the same, around 89, and that was a check that the second view did not harm basic perception. Asked where the TSRBench gain sat, he said perception stayed similar, most of the gain was prediction and decision-making, and some individual reasoning tasks fell while the overall result still improved.

### What landed

The confound is the point of the story, and he named it before the controls. Chart+chart below chart is the evidence that a second stream is not the gain. He corrected TSExam himself: flat, not a win. The decision stayed in the first person.

### What broke

The first TSExam claim had the dual view ahead. The card is flat at 89.9 for both. Delay+delay was said as 42.3. The card is 42.6. He then put prediction and decision-making together as the gain, and said reasoning tasks decreased. The card concentrates the gain in prediction, 38.0 to 61.7, with smaller gains in reasoning and decision-making.

The follow-ups chased those scores. He stopped that. The next mock stays on the challenge and the decision.

### Next pass

One retell: why a second tower could be a confound, what the matched controls ruled out, and the decision to treat the views as complementary. One sentence that TSExam stayed flat and the TSRBench gain sat in prediction. Then stop.

---

## 2026-10-21 — Story A, ImagenTime, full transcript

**Kind:** Behavioral mock he ran elsewhere and asked to keep in this form. Interviewer: Huzefa Rangwala, simulated. Topic: research leadership, technical judgment, scientific rigor. One opening question and three follow-ups.

**Score he was given:** 8/10. Research leadership 9. Technical depth 8. Scientific rigor 9. Principal-level judgment 7. Communication 8.

### Question 1 — research leadership

Tell me about a time when you proposed a research direction that was technically risky or unconventional, and you had to convince others it was worth pursuing. How did you make that decision, and what was the outcome?

This was the ImagenTime project. A VAE generative project for time series had just finished. Diffusion was a natural continuation. A time-series-native architecture, such as a Transformer, was the standard approach. The observation was that vision diffusion had advanced in both modeling and implementation, so he suggested transforming time series into images to use that progress.

Pushback he attributed to his students: representing 1D signals as 2D images would take more compute, and time-series images are not natural images. He did not settle it by seniority. Three conditions could kill the idea cheaply: reconstruction fidelity, promise on small benchmarks, and a manageable compute burden. He coded and ran those experiments. The preliminary results were encouraging, so they invested more compute and time. Outcome: a NeurIPS 2024 paper, then a series of papers, six so far, based on this idea.

### Follow-up 1 — technical decision

A lossless transformation does not necessarily produce a representation that is useful for generative modeling. What representations did he investigate, why did he select one, and what evidence made the 2D representation worth the extra compute?

Four representations, all of which he said respected reconstruction: line plots, Gramian angular fields, delay embeddings, and short-time Fourier transforms. Line plots and Gramian angular fields required too much resolution and did not scale. Delay embeddings and STFT were compact and strong on the benchmarks. Tests were discrimination and prediction, against strong baselines including the previous VAE. The image representations were robust. The same framework handled sequences from about 24 to 17,000 steps, which competing methods did not show in that evaluation. That range was a main reason to accept the extra cost.

### Follow-up 2 — causal attribution

How did he establish that the improvement came from representing time series as images, rather than from a stronger diffusion architecture or a better sampler? What does the evidence support, and what remains unproven?

The claim that representing time series as images is inherently better remains unproven. What was shown is that time-series image representations, with standard vision diffusion models and samplers, reached state-of-the-art generative results across benchmarks against strong baselines. Ablations matched compute, number of parameters, and training time. Isolating the image representation, the architecture, and the sampler is difficult: an image uses an image diffusion architecture, and a raw series uses a time-series architecture. One ablation tested multiple transformations. The representations were not equivalent. Delay embeddings and STFT were particularly robust. The results support the combined framework. They do not establish that the 2D representation alone caused the improvement.

### Follow-up 3 — principal-level judgment

Three scientists, a limited compute budget, four weeks, a similarly unconventional idea. How would he structure the weeks, and how would he decide to stop?

Start with the minimal experiment that can show a positive signal or kill the idea cheaply, as on ImagenTime. Test the main hypothesis in a small setup, or use the best available proxy. Week 1: design the experiment, and define the hypothesis, failure gates, and expected outcomes. Week 2: data, implementation, and the evaluation pipeline. Week 3: run the experiments. Week 4: analyze, and make a pass-or-kill decision.

### Evaluation from that session

Strengths he was given: he set an unconventional direction without using seniority; the kill tests came before the investment; he coded the preliminary experiments; he separated the combined system from the unproven claim that 2D is inherently better; the line became a NeurIPS 2024 paper and follow-up papers.

Improvements he was given:

1. One concrete result in the opening. The answer ended on publications.
2. Reconstruction as practical fidelity at a usable resolution. Do not treat every representation as equally practical or equally lossless.
3. Keep the distinction he already made. Matched compute and parameter count do not isolate the representation.
4. The four-week plan was generic. Name who does what, parallel work, an early checkpoint, explicit thresholds, the compute limit, and a scale, revise, or stop decision.

Improved follow-up 3 from that session: identify the central hypothesis and the cheapest experiment that can falsify it, and set success and failure before seeing results. Week 1, with the team: those criteria and the smallest representative dataset. One scientist on the baseline and evaluation, one on the proposed method, one on data quality and failure analysis. Weeks 2 and 3: implement and run, smallest configurations first, with a checkpoint that stops the work if an assumption fails. Week 4: average performance, failure cases, compute cost, and robustness. The decision is scale, revise, or stop. Four weeks does not need a finished method. It needs evidence that the hypothesis is worth more investment.

Takeaways he was given: keep ImagenTime for direction-setting; keep the three gates; put one number in the opening; be ready to say why delay embeddings and STFT stayed and line plots and Gramian angular fields did not; do not claim the image representation independently caused the gains; connect a future plan to people, compute, and gates. He was told not to over-rehearse it.

### Against the bank

These lines disagree with [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md) or with the 16 October mock. Use the bank on Friday.

- "My students" is the same break as 16 October. The bank's avoid line is "I convinced my students."
- The opening still has no number. The bank's pair is about 58% on short-series discriminative score over prior diffusion models, and about 133% on long and ultra-long classification. Length 24 to about 17,000 can be the one result if he does not want both percentages.
- Line plots were too sparse and not cleanly invertible. Gramian angular fields scaled poorly. "Too much resolution" covers neither. An off-diagonal Gramian cell is not zero.
- Not every candidate passed practical reconstruction. Delay embeddings and STFT did.
- "Six so far" is this telling. The bank's diffusion-investment line says eight papers. Do not treat those as the same count.
- The drop from about 1,000 model evaluations to about 35 is the EDM sampler, not the image transform. He did not separate them here.

## 2026-10-22 — Story E, Bosch

**Kind:** Behavioral mock he ran elsewhere and asked to keep in this form. Interviewer: Huzefa Rangwala, simulated. Topic: cross-functional collaboration, technical leadership, scientific judgment. One opening question and three follow-ups.

**Score he was given:** 7.5/10. Technical leadership 8.5. Cross-functional collaboration 7. Scientific rigor 8. Product judgment 7.5. Communication 7.

### Question 1 — cross-functional collaboration

Tell me about a time you worked with people outside your area of expertise to solve a difficult technical problem. How did their perspective change your approach, and what was the outcome?

A joint project with Bosch AI on generative modeling for time series. He led the technical component, from observation and ideation through implementation and experimentation. The model worked on offline in-house benchmarks and failed on real Bosch sensor data. His first plan was the ML one: more data, hyperparameters, more capacity. People at the Bosch site pushed him to look at the sensor data. It was irregularly sampled and noisy, so the framework was unlikely to generalize. He decided the fix was an EM-style loop that alternates data completion and sampling, not more data or more training. He called the results strong, and said the method later served as a research backbone at Bosch AI. He does not know whether Bosch productionized it.

### Follow-up 1 — why not interpolate

Why was the EM-style loop preferable to interpolating the irregular observations onto a regular grid and training the existing diffusion model? What did the iterative approach solve that interpolation would not?

He said interpolation ignores the true data distribution, and that a loss on interpolated segments is incorrect. Even with an observation mask, a convolutional model still consumes the interpolated regions as inputs. The completion-and-sampling loop is preferable because the posterior is updated through training, so completion and sampling improve together.

Feedback he was given: the intuition is reasonable and several claims are too loose. Interpolation is a legitimate baseline, especially with an observation mask. Masking the loss keeps interpolated targets out of the objective; interpolated inputs can still change the prediction. The stronger reason for an iterative completion is that it can carry uncertainty over the missing values, instead of one deterministic fill. He needs to say what each stage updates — latent completions, parameters, or both — and to separate a training update from completion at inference. He was told to be ready to write the completion step, the sampling step, and the objective.

### Follow-up 2 — what would justify the extra method

Three approaches: linear interpolation with an observation mask, then a standard diffusion model; a diffusion model trained directly on irregular observations; the iterative completion-and-sampling approach. What would he measure, and what result would convince him the simpler approach is enough?

A discriminative test, same data, matched parameter counts and training budgets, on several datasets. Also a known distribution he can write down, and a comparison of each completion to that distribution, including the irregular-observation model if its samples can be put in one representation. The closer match is the better generative fidelity.

Feedback he was given: matched budgets, more than one dataset, a synthetic ground truth, and fidelity rather than only pointwise reconstruction all landed. A discriminative score does not show that the completion is accurate or that observed measurements are kept. The missing pieces he was given: held-out reconstruction (hide a real measurement and score the prediction), distributional fidelity, more than one missingness rate and pattern, a check that completions respect the observations, and training cost, latency, and memory. The question is whether the iterative method's gain pays for the extra complexity.

### Follow-up 3 — engineers prefer the simple version

Bosch engineers are satisfied with interpolation because it is easier to maintain. His experiments show better generative results for the iterative method. How does he resolve that, and what evidence does he need before recommending the complex one?

Maintainability matters, and he would start from the metrics Bosch cares about: generation quality, and compute (peak memory, GFLOPs, latency). He would compare the approaches and set improvement gates in advance. Consistent wins past those gates are the argument for the complex method. Mixed results mean he looks for the cases where interpolation fails and generation quality drops, and uses the complex method only there.

Feedback he was given: he did not assume the sophisticated method should win. Business metrics, compute cost, gates, and a split by use case all landed. The disagreement he was handed was maintenance, not only compute. A principal answer includes engineering complexity, reliability, and the maintenance burden. The closer he was given: even a better generative result does not justify the method unless it pays for the operational and maintenance cost. If the simple approach meets the requirement, use it, and keep the complex method for the cases where the gap is material.

### Evaluation from that session

Strengths he was given: he owned the technical direction and changed it when the benchmark assumption failed; he took the sensor characteristics from Bosch instead of tuning the original model; the experiment sketch had matched budgets and a distribution-level check; he treated compute as a product constraint and left room for the simpler method; he separated a research backbone from a deployment he did not see.

Improvements he was given:

1. One concrete collaboration. Who looked at which measurements, which comment changed an assumption, who owned which part, and how they agreed on the evaluation. Do not invent a meeting that did not happen.
2. The method, precisely. Why the original model failed, how irregular sampling was represented, whether interpolation and an observation mask were used, what the completion step and the sampling step update, and what was a training update versus an inference completion. The evidence for the change.
3. Do not stop at the discriminative score. Reconstruction, distributional fidelity, observation consistency, and robustness to the missingness pattern.
4. Maintenance, reliability, and engineering complexity, not only memory and latency.
5. One real number, if he has one. "Strong results" is not a result. Do not claim a production deployment.

Improved opening from that session, and it is not verified against the bank: he led the technical work with Bosch AI on generative modeling for industrial sensor data. Offline benchmarks were fine. Real Bosch sensor data was not. His first instinct was more data, tuning, or capacity. Domain experts pushed him into the measurements. They were irregularly sampled and noisy, which broke assumptions in the framework. He changed direction to an iterative completion-and-sampling method. The revised approach was substantially stronger on that sensor data and became a research backbone for later work at Bosch AI. He does not claim a product. The lesson he was handed: collaboration is not only listening; it is revising the mathematical assumption when their account of the system contradicts the model.

Takeaways he was given: use this story for cross-functional work, industrial scientific ML, and a real constraint changing the method. The line to keep is that the failure was the data assumption, not insufficient capacity. He led the research. Bosch contributed the measurement knowledge. That knowledge changed the direction. The revision was tested. Research success is not a deployment. Do not say interpolation is always wrong. Do not leave EM imprecise. Do not treat a better generative score as enough to impose the complex system. Do not describe the collaboration without the actual exchange.

### Against the bank

These lines disagree with [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md), Story E. Use the bank until he reconciles them. Do not promote the EM telling into the bank from this one mock.

- The bank's task is modality translation: generate one sensor modality from another. This telling was generative modeling for time series, and the improved opening says industrial sensor data. The modality is missing.
- The bank's technical change is interpolation onto a regular grid together with an observation mask, so filled values are not treated as measurements. This telling's change is an EM-style loop of completion and sampling, and interpolation is described as typically wrong. Those are different methods. Friday uses the mask version unless he confirms the loop was the implementation.
- The bank already refuses a product ship. That part of this telling matches. "Research backbone" is the bank's "strong internal research baseline," said more strongly.
- Neither version has a Bosch number. Do not invent one. If a real figure exists, it belongs in the bank only after he names the source.
