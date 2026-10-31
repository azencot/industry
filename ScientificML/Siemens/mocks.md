# Siemens mock log

One file for every Siemens mock (behavioral, coding, system design, ML depth, and ML breadth). Append a section. Add a row to the index. Do not open a new file per mock.

Story source: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Coding drills: [`coding/README.md`](coding/README.md).

## Index

| Date | Kind | Focus | Break |
|------|------|-------|-------|
| 2026-10-16 | Behavioral, ~15 min | Story A — ImagenTime | GAF off-diagonal called zero. "My students." No number. EDM not separated. |
| 2026-10-21 | Behavioral | Story C — TR kill | Reasoning average said as 28. Tempting gain called overall. Left the kill for the audit. 0.8B deltas not said. |
| 2026-10-21 | Behavioral | Story B — dual tower | Controls landed. TSExam first called a win, then corrected to flat. Gain grouped prediction with decision-making. |
| 2026-10-21 | Behavioral, full transcript | Story A — ImagenTime | Attribution held. Opening still has no number and still says "my students." Four-week plan stayed generic. |
| 2026-10-22 | Behavioral, full transcript | Story E — Bosch | EM loop told in place of interpolation plus an observation mask. No number. Collaboration stayed general. Maintenance named as compute. |
| 2026-10-26 | System design, ~15 min | 500 machines, five sensors, anomaly alerts | Supervised labeling on 20 failures. Synthetic prevalence used as the eval. No shadow or rollout. 6.5/10. |
| 2026-10-26 | ML depth, ~15 min | VAE, diffusion, flow matching | Objectives and TSTR landed. Marginal field called straight. Optimal velocity called a moving average. 8/10. |
| 2026-10-28 | ML breadth, stopped early | 10,000 machines, 0.5% failures, 20 inspections | Cost threshold 0.99% landed. Capacity left as unconstrained FP/FN. Precision@K unknown. 6.5/10 provisional. |
| 2026-10-28 | ML depth, Koopman | Lift, linear latent dynamics, long horizon, ablations | Idea and the encoder–A–decoder baseline landed. Unit-circle constraint underspecified. Low-data win read as “the system is Koopman.” 7.5/10. |
| 2026-10-28 | Behavioral, stopped | Story A — ImagenTime, disagreement | Kill tests and EDM landed. Still “my students.” No number. “Insist” on the POC. Vote instead of the decision. Q7 unanswered. 8.0/10. |
| 2026-10-29 | System design, Vivek | One million PDE trajectories | Clarification and the 100,000-trajectory shortfall landed. Later counts used wall-clock instead of the node-hour budget. Storage and PDE residuals not said. 7.0/10. |
| 2026-10-29 | ML depth, Closing the Loop | Co-evolving EM, irregular series | Motivation and the four missingness regimes landed. The monotone quantity and the E-step distribution were not stated. 7.0/10. |
| 2026-10-29 | ML breadth, stopped | New factory, 1% failures, 200 inspections | Shift and the random-window split landed. Calibration unnamed. No expected-cost threshold. Q4 unanswered. 6.5/10. |
| 2026-10-29 | Behavioral | Story C — TR kill | Gates and 26.9 to 21.9 landed. Reasoning still said as 28 to 29.2. “We agreed.” The lever, not the project. 8.0/10. |
| 2026-10-30 | ML breadth | 100M transformer, validation rises after 6,000 | Overfit named. The step-6,000 checkpoint was not the first move. Larger models, then a learned map, then resampling. No weight decay or dropout. 6.5/10. |
| 2026-10-30 | System design, Vivek | Industrial time-series foundation model | CFD surrogate aborted, unscored. Three holdouts landed. Decoder-only plus a mask, then a metadata token. 500 factories treated as 500 machines. 7.0/10. |
| 2026-10-30 | ML depth | Qwen3-VL, chart and delay | Two-stage train and the view dropout landed. Fusion was not a token. Causal split of information, perception, and reasoning was invertibility, a target embedding, and attention. 7.5/10. |

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

## 2026-10-26 — System design, industrial sensor anomaly detection

**Kind:** ML system design mock he ran elsewhere and asked to keep. About 15 minutes. Not a behavioral story, and not the Bosch project. Scenario: 500 machines of one type, five sensors at 1 Hz (temperature, pressure, vibration, current, voltage), six months of history, about 20 documented failures, thresholds that alarm too often, at most five maintenance alerts a day, near-real-time inference, operating conditions that vary. Design the anomaly system.

**Score he was given:** 6.5/10. Clarification 9. ML fundamentals 8. Modeling judgment 7.5. Experimental methodology 6. Operational constraints 6. Deployment and monitoring 4. Communication 7.5. Practice scores, not a hiring prediction.

### What he said

He clarified what counts as abnormal, whether that is an extreme value, a dead sensor, or a bad relationship across sensors, how many types exist, whether the sensors can show it, the cost of a miss against a false alarm, how hard labeling is, and whether a rule can define it.

He then started supervised. Engineers would label suspicious segments, about half their time labeling and half checking automated labels. Candidates would come from the existing thresholds and from high-variance stretches. A decision tree or a regression model would be the baseline, scored with a train/test split or cross-validation, and its predictions on unlabeled data would propose more candidates. A neural model would come after that. Alerts would respect five a day, and severity would outrank mild anomalies inside that budget.

Pushed off the 20 failures, he switched to a masked autoencoder on the unlabeled streams, with reconstruction error as the score, expert review of high scores, and a separate model per anomaly duration.

For evaluation he proposed synthetic failures, sets at 1% and 0.1% prevalence, precision, recall, and F1 against the thresholds, an alert threshold from the average score of the top-k events that day, and cross-validation that holds out five documented failures per fold.

### What landed

The opening questions distinguished kinds of anomaly, observability, labeling cost, and the business cost of a mistake. He started from a simple baseline and a person in the loop, and he named the alert cap and severity. When the positive count was challenged, he dropped the supervised plan and used the unlabeled history. He also noticed that one duration will not fit every failure.

### What broke

The first design needed labels the data does not have. About 7.8 billion multivariate observations and 20 documented failures. Thresholds can miss whole anomaly types, so mining candidates from them biases the labeled set. He did not say how the rest of the unlabeled stream is used until he was asked.

Reconstruction error is not the anomaly. A strong autoencoder can reconstruct a fault, and a rare normal operating mode can score as a fault. Several masking scales inside one model were preferred to a model per duration. The comparison he was given: the existing thresholds, a statistical or feature detector, then the masked model, and the extra complexity has to move an operational number. Condition the score on the operating mode.

Synthetic failures and a chosen prevalence do not measure alert precision in the plant. Changing how often failures appear changes precision. Twenty documented failures are not the prevalence of anomalous windows. Synthetic cases can stress a known pattern. They do not replace the real failures.

Precision, recall, and F1 are not the decision. The metrics he was given: event-level recall on documented failures, false alerts per day, detection lead time, precision inside the alert budget, and the same cuts by operating condition. The number to lead with is event-level recall at a fixed alert budget, plus lead time.

Holding out five failures does not stop leakage. Windows are correlated in time, failures on one machine are related, operating conditions are shared, and a random fold can train on times after the period being scored. He was told to use a chronological split, a gap in time, a held-out machine when that is possible, and to say that 20 events cannot support a tight confidence interval.

The alert rule is not the average of the top-k scores. Calibrate on a historical validation window, group consecutive hits into an event, suppress repeats, rank by severity, require a minimum score, and apply the budget. Five a day is not a quota to fill. Ask whether a sixth urgent alert may go out, or whether five is a hard cap.

He did not describe a rollout. The sequence he was given: replay the recorded streams, run in shadow next to the thresholds with no operational alert, have engineers review disagreements, pilot on a subset of machines, then widen while watching alert quality, latency, reliability, and maintenance outcomes. Keep a rollback.

### Lesson from that session

The gap is the frame, not the model menu. He went data, model, experiment, better model. The order he was given is requirements, data, baseline, model, evaluation, deployment, and the system comes before the architecture.

Opening he was handed, and it is not something he said: three phases. First, the operational requirement and a baseline on the historical data. Second, a detector trained mostly on unlabeled streams, with experts reviewing selected events. Third, a historical replay and a shadow run before any alert is enabled. The objective the whole way is event-level detection inside the five-alert budget.

### Next mock

The session named a 15-minute follow-up: real-time probabilistic forecasting for 1,000 industrial sensors, with uncertainty, heterogeneous behavior, a latency bound, continuous monitoring, and drift. Ask one question at a time. Do not hand the design over while he is answering. Feedback after, not during. Track whether these move:

- Unlabeled data and selection bias before a supervised model.
- A score that is not raw reconstruction error, and a condition or context on it.
- Real failures for the decision metric. Synthetic data only as a stress test.
- Event-level recall under an alert budget, plus lead time.
- A chronological split and, if possible, a held-out machine.
- An alert policy that aggregates, deduplicates, ranks, and can emit fewer than five.
- Shadow, then a limited pilot, then rollback. Say this before a second model.

## 2026-10-26 — ML depth, VAE, diffusion, flow matching

**Kind:** ML depth mock he ran elsewhere and asked to keep. About 15 minutes. Four questions on generative models for multivariate industrial sensor series. Practice scores, not a hiring prediction.

**Score he was given:** 8/10. Fundamentals 8.5. Mathematical precision 7. Diffusion versus flow matching 7.5. Experimental methodology 9. Research judgment 9. Compute tradeoffs 8. Communication 8. Stronger than the same day's system-design mock (6.5). The gap is precision, not judgment.

### Question 1 — the three families (8.5)

He said a VAE trains on the posterior and maps a latent code to a simple prior. Diffusion is an SDE: the forward process adds noise and is not learned, the reverse process denoises. Flow matching fits a vector field on each time segment and integrates from noise to data. Objectives: ELBO, noise-matching \(L_\text{simple}\), velocity matching. A VAE samples the prior and decodes in one pass. Diffusion and flow matching integrate. He would take diffusion or flow matching when high-frequency detail matters and latency can wait, and a VAE when a fast, somewhat blurry sample is enough.

What landed: the three objectives, one-pass versus iterative sampling, and quality against latency.

What he was corrected on: blur is a likelihood and a decoder, not a property of every VAE. Flow matching learns one time-dependent velocity, not a separate field per segment. Diffusion and flow matching are both continuous-time models, and the cost depends on the parameterization and the solver. Training cost cannot be ranked without an architecture, a dataset, and a procedure.

### Question 2 — why fewer steps (7.5)

He said flow matching optimizes a straight path, the linear interpolation between noise and data, so the integral is easier than an unconstrained diffusion path. He did not remember the curvature-to-error link and said he would not invent it. He named EDM as a diffusion integrator that shrinks the gap.

What landed: geometry matters, and he refused a formula he did not have. EDM is the right example.

The correction: conditional flow matching can use the straight path \(x_t = (1-t)x_0 + t x_1\). The learned marginal field is an average over endpoint pairs, so those trajectories need not be straight. Fewer steps are not guaranteed. They depend on the coupling, the path, the learned field, and the solver. A probability-flow ODE plus a good solver can sample diffusion cheaply too.

Euler on \(\dot x = v(x,t)\) is \(x_{n+1} = x_n + h\, v(x_n, t_n)\). Local truncation error is \(O(h^2)\). Global error is \(O(h)\). The acceleration is \(\partial v/\partial t + J_v(x,t)\, v(x,t)\). A smaller acceleration can allow a larger step at the same tolerance. Curvature alone does not set the difficulty. Stiffness, the time grid, and the solver order do too.

### Question 3 — the field that is learned (7)

Conditional target velocity is \(u_t(x_t \mid x_0, x_1) = x_1 - x_0\). The network sees only \(x_t\) and \(t\). He said the objective averages many pairs, so the field at one \(x_t\) points toward several \(x_1\), all toward the data, and that an exact repeat of \(x_t\) has probability zero, so training sees a neighborhood.

What landed: the field is shared, and it averages endpoints rather than memorizing one path.

The identity he did not say: the MSE optimum is \(v^*(x,t) = \mathbb{E}[x_1 - x_0 \mid x_t = x]\), a conditional expectation. Individual conditional velocities can oppose each other. That expectation is the marginal velocity. It satisfies the continuity equation \(\partial p_t/\partial t + \nabla\cdot(p_t v^*) = 0\), so integrating \(\dot x = v^*\) carries the prior along the prescribed path to the data, given capacity, optimization, and regularity.

### Question 4 — which model to ship (9)

The table he was given: VAE 0.18 / 1 step / 5 ms, diffusion 0.10 / 50 steps / 250 ms, flow matching 0.11 / 10 steps / 55 ms. Synthetic series for a downstream trainer. He said the aggregate quality number can miss the part of the distribution the downstream task needs. He would train on synthetic and test on real, and also look at coverage and variability, for all three models. He would rather buy quality than latency, because latency inside one family is usually easier to move.

What landed: he refused the table as the decision, named train-on-synthetic test-on-real, and asked for a controlled comparison. This was the strongest answer.

Still add: train-on-real test-on-real, and train on real plus synthetic, on the same held-out real set. Cut rare failures, rare operating regimes, cross-sensor dependence, and temporal structure, not only the average. Ask how many sequences, how often they are regenerated, and what the budgets are. 55 ms versus 250 ms is a different decision at millions of sequences than at a handful. Repeat seeds. A 0.10 versus 0.11 gap may be noise. Prefer flow matching when the downstream result is indistinguishable and the cost is lower. Prefer diffusion only when the gain on the important failures pays for the extra compute.

### Refresh before the loop

About an hour, not a survey of generative modeling.

- Conditional flow matching versus the marginal field. The conditional expectation above. The continuity equation. A straight conditional path is not a straight marginal trajectory.
- Score or noise prediction, the reverse SDE, the probability-flow ODE, DDPM versus DDIM, and the Euler errors above.
- Train-on-real, train-on-synthetic, and real-plus-synthetic. Rare slices. Uncertainty. Cost at the customer's volume.

### Next mock

The session named a 15-minute ML breadth pass: classical versus deep models, generalization and regularization, optimization, imbalance, calibration, shift, representation learning, and selection under a constraint. One question at a time. Feedback after. Track whether the conditional-expectation identity and the marginal-versus-conditional distinction are said without a prompt.

## 2026-10-28 — ML breadth, failure prediction under a budget

**Kind:** ML breadth mock. Three questions, then he asked to stop. Industrial failure prediction: model choice, a cost threshold, then a cap of 20 inspections. No hints during the answers. Feedback after. Provisional **6.5/10** on this fragment, not a full breadth interview. The same-day recall log is separate: [`2026-10-28_breadth-recall.md`](2026-10-28_breadth-recall.md).

### Question 1 — which model (8)

10,000 machines. Three years. About 200 features. Fail within seven days. Prevalence about 0.5%.

| | XGBoost | DNN |
|--|---------|-----|
| AUROC | 0.96 | 0.97 |
| AUPRC | 0.31 | 0.35 |
| Recall | 0.85 | 0.90 |
| Precision | 0.18 | 0.15 |

The team wants the DNN for the higher AUROC, AUPRC, and recall. He refused that and asked the cost of a miss against the cost of a false alarm. If misses dominate, he would take the DNN for the higher recall.

What landed: he did not ship the larger AUROC, and he asked for the costs.

What he skipped: the two recalls are one threshold each, and those thresholds may not match. He did not ask for the precision-recall curve or for both models at the same operating point. Ranking quality and the deployed decision are different.

### Question 2 — the threshold (7)

A miss costs $50,000. An unnecessary inspection costs $500. At most 20 inspections a day. He wrote \(p^* = C_{FP}/(C_{FP}+C_{FN}) = 500/50{,}500 \approx 0.99\%\). He would then compare the dollar cost of the extra false negatives against the extra false positives, and he said the counts were hard to do in his head.

The formula is right. It applies when the probabilities are calibrated, the costs are known, inspecting prevents the loss, the machines are independent, and there is no cap. He did not say calibration. He did not use the 20.

### Question 3 — twenty slots (4)

Both models are calibrated. On this day XGBoost puts 80 machines over 0.99%, and the DNN puts 120 over it. The crew can inspect 20. He did not know how to place the cap and stopped.

The gap: a fixed budget is a top-K rank, not a threshold that returns 80 or 120 names. Expected benefit of inspecting a machine is \(U(p) = p\, C_{FN} - (1-p)\, C_{FP}\). With the same costs on every machine, \(U\) rises with \(p\), so the 20 slots are the 20 highest probabilities whose \(U\) is still positive. The 0.99% line is only the eligibility cut. It does not choose among the machines that clear it. If costs differ by machine, rank by \(U\), not by \(p\).

Compare the models under that same policy. The numbers that match the crew are precision at 20 and expected utility at 20. Recall at 20, lead time, false-alert burden, and whether the daily ranking is stable come after. AUROC and AUPRC stay as summaries. They do not score a 20-slot day.

### Precision at K, taught after he stopped

He had not met the @K notation. Precision at K is the positives inside the K highest scores, divided by K. Recall at K divides by all positives, not by K. A threshold lets the selected count move. Top K freezes the count. For this crew, compute them on each day’s ranking, on a temporal holdout, not on one top-20 taken from the whole history. Repeated alerts on one machine and overlapping seven-day windows still need an event definition.

**Exercise, not yet answered.** 1,000 machines, 40 failures. 8 of those failures are in the top 10. 12 are in the top 20. Precision at 10, precision at 20, recall at 10, recall at 20. Why can precision fall from 10 to 20 while recall rises?

### What to say next time

1. The decision, the costs, and the constraint.
2. The policy: eligibility threshold if probabilities are calibrated, then the K highest positive benefits if a cap binds.
3. Score every model with that same policy. Precision at K and utility at K before AUROC.
4. Calibration before any dollar threshold. Heterogeneous costs mean rank by benefit, not by probability.

Next breadth mock should be a different topic. One more constrained-ranking case with unequal inspection costs comes before it, plus the four numbers above.

## 2026-10-28 — ML depth, Koopman

**Kind:** ML depth mock grounded in the CV. Six questions, then he asked to stop before a synthetic-data question. No hints during the answers. **7.5/10.** This is not the 26 Oct depth mock on VAE, diffusion, and flow matching. The interviewer was assumed to know sequence models and not Koopman theory. Do not open this story with the lab title.

CV lines the mock used, not a new story bank: NeurIPS 2026 Koopman generative operators; NeurIPS 2026 co-evolving EM for irregular series in a lifted representation; NeurIPS 2025 distilling Koopman operators; ICLR 2023 multifactor disentanglement via structured Koopman autoencoders; ICML 2020 consistent Koopman autoencoders.

### Question 1 — the idea (8.5)

Nonlinear dynamics can be linear in a lifted space of observables, infinite-dimensional in the theory. He separated lift and projection from the dynamics, and he named interpretability and the link to linear-systems tools.

What he left out: a finite learned matrix is an approximation, not that operator. Powers of the matrix are the practical payoff, a forecast of many steps without a new network call. One physical example was missing.

### Question 2 — the baseline (8)

Encoder, linear map, decoder. Reconstruction loss, latent one-step loss \(Az_t \approx z_{t+1}\), and he named consistency or stability as optional. Forecast either by rolling the observation back in, or by \(A^H\) on a fixed history encoding.

The representative objective he was given, and it is a baseline rather than every paper: \(z_t = E(x_t)\), \(\hat x_{t+1} = D(Az_t)\), and a sum of reconstruction \(\|D(E(x_t))-x_t\|^2\), latent \(\|AE(x_t)-E(x_{t+1})\|^2\), and observation \(\|D(AE(x_t))-x_{t+1}\|^2\). Horizon \(H\) is \(D(A^H E(x_t))\). He did not separate the latent loss from the decoded forecast, and he did not say how a lookback window becomes one \(z_t\).

### Question 3 — a long horizon that dies (7)

He named eigenvalues outside and inside the unit circle, asked for eigenvalues on the unit circle, and if the system is not a long-horizon linear system, a time-dependent operator.

Diagnose before changing the architecture. Reconstruction error asks whether the lift is adequate. One-step latent error against the error of \(A^H\) asks whether the dynamics are the failure. Error versus horizon, rollout versus \(A^H\), and whether the series is stochastic come before a new module. A decaying mode can be the physics. A multi-step loss is a training change, not a new architecture.

### Question 4 — eigenvalues on the unit circle (6.5)

He said the latent dynamics then have no shrinking or expanding modes, so a system with short intervals of growth or decay will not fit.

That is the right restriction and too small a claim. For a diagonalizable \(A\) with every \(|\lambda_i|=1\), the modes persist: oscillation or a constant. Decay and exponential growth are excluded. Damped physical systems need \(|\lambda|<1\). A nontrivial Jordan block can still grow polynomially while every eigenvalue sits on the circle. The constraint is not a certificate of bounded trajectories, and it is not the default for every stable plant.

### Question 5 — the ablation (8)

Same encoder and decoder, Koopman dynamics against a Transformer dynamics module, matched parameter count, data, and training, several datasets and several metrics.

Add an MLP dynamics module and a linear forecast. Cut by horizon and by how much data there is. Several seeds. Latency and memory next to accuracy. A shared tuning budget.

### Question 6 — low data, then the Transformer catches up (7)

He would select Koopman or the Transformer from the data limit and the inference budget. He read the low-data win as evidence that the system respects the Koopman assumptions, and that more data reveals complexity the linear latent model cannot hold. He also said there is a regime where Koopman wins on both accuracy and cost.

The low-data win supports a useful bias. It does not establish that the plant is a Koopman system. Regularization, optimization, and effective capacity can produce the same curve. A selector is extra machinery. Prefer one model on the accuracy-cost frontier unless two operating regimes pay for the switch. If Koopman meets the accuracy bar, the cheaper inference is the reason to ship it. If the Transformer’s gain on the decision is large and the latency is affordable, ship that.

### Not answered

How to judge synthetic sensor sequences when real failures are scarce: fidelity to the real series, and whether a failure model trained on the synthetic data improves on real holdout. Out of the score. A later depth pass can start there, on the CV’s generative papers, not on flow matching unless he brings it up.

### What to redo

Answers were short. The shape he was given: the idea, the mechanism, what it changes in practice, and the limit. On a failure, name the candidate causes and the measurement that separates them before naming a new architecture. Qualify the spectral claim. A low-data win is a bias, not a proof about the plant.

## 2026-10-28 — Behavioral, ImagenTime disagreement

**Kind:** Behavioral mock. He picked the story. Seven questions were planned. He stopped before the last. No hints during the answers. **8.0/10.** Do not retell ImagenTime as the next behavioral mock. Source: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md), story A.

### What he said

After a VAE, the obvious next step was a native time-series diffusion model, probably a Transformer. He wanted the vision diffusion stack, so he proposed mapping series to images. He called the hesitation his students’. He did not pull rank. He owned a proof of concept with three kill tests: reconstruction, a basic benchmark, and compute. Line plots were too sparse. GAF did not scale. Delay embeddings and STFT passed reconstruction and the benchmark. He watched compute against native time-series baselines. The result he named was NeurIPS 2024 and state of the art from short to ultra-long sequences.

On mixed results he would show both the promising findings and the cost, then discuss how to proceed. He treated the compute objection as mostly inference, because training happens once, and he took EDM himself. After EDM, inference cost was comparable to the non-vision methods, so he continued.

On dissent he said the group puts two or more options through a minimal proof of concept, and that in other projects the idea came from the students. On this one, a student proposed a learnable image map. Delay embeddings and STFT were already strong, so a learnable map meant rerunning the study. The student ran a proof of concept. Discriminative score was about 10% worse. The deadline was close, so they left it for later.

He said that 10% did not prove the idea was bad. He thinks a learnable map is better than a fixed one. A few more days would have been needed, and those days would have weakened the submission or slipped the cycle. The team voted to postpone.

Looking back, he wished he had put a student on the proof of concept even though they disliked the idea, because doing the work informs the judgment. In later projects he said he will insist on a role for teammates on the proof of concept, even a small one.

If a senior person refuses the direction, he would allow a bounded detour with a kill-or-continue schedule, the same standard he used on himself.

He did not answer how he would tell that person, at the deadline, that another two weeks will not be granted.

### What landed

The fork was native diffusion versus a representation change. The three kill tests were his, and they were cheap. He compared transforms and he separated EDM from the image step: the sampler is what made inference comparable. He did not treat the learnable map as disproved. He named the deadline as the reason to postpone it. The line to keep is that disagreement became a test with a stop rule, not a demand that the group agree first.

### What broke

- **“My students.”** Same break as 16 Oct and 21 Oct. Name who owned the native stack and what they said. The interpersonal half was thin: how the concern was phrased, what he changed because of it, and how he said the postponement was a deadline, not a verdict on the idea.
- **No number.** “State of the art” is still the result. The bank’s pair is about 58% on short-series discriminative score, or about 133% on long-series classification. One.
- **GAF.** “Did not scale” is the right failure and still incomplete. The field is dense. The sparse image is the line plot.
- **Training happens once.** He said the compute objection then applies only to training. A production system retrains and adapts. Split training cost, latency, throughput, and hardware before calling inference “solved.”
- **“Insist.”** Putting teammates on the proof of concept so the evidence is shared is the lesson. Requiring people who oppose the idea to staff it is the reading to avoid. Say he would invite them into the design of the test and keep the implementation if they declined.
- **The vote.** Input is not the decision. He still has to say who decided, on what criterion, when the group did not agree.
- **Question 7 is open.** The researcher still wants two more weeks after the stop rule failed. How he says no without making it a verdict on their judgment.

### Against the bank

Use the bank on the facts. Do not promote this telling’s new lines into the bank from one mock.

- The learnable-map proof of concept and the 10% discriminative drop are this telling. They are not in the bank. Keep them only if he confirms the number and the source.
- EDM was correctly separated here. That part matches the bank. The drop from about 1,000 evaluations to about 35 is the sampler, if he wants the figure.
- The chat’s extra portfolio (a vector-field failure, a struggling student, influence without a title, leading the group) is not a new story. Next behavioral mock is not ImagenTime. Use **C**, **B**, or **E**. Do not open with the lab.

### Next pass

One retell that is not this prompt. If ImagenTime comes up anyway: who disagreed, the three tests, one number, EDM as the sampler, and the postponement said as a deadline. Drop “my students” and “insist.” The unanswered close is still the stop rule after someone wants two more weeks.

## 2026-10-29 — System design, one million PDE trajectories

**Kind:** System design, Vivek Govindan simulated. One million 2D fluid trajectories for a foundation model. He stopped before the last question. That question is not scored. **7.0/10.** Do not repeat PDE data generation as the next design mock. Keep the next one to 20–25 minutes and three follow-ups.

### What he was given

2D fluids. Initial conditions, boundary conditions, and physical parameters vary. An existing validated CPU solver. 256×256, four variables, 1,000 time steps. 500 CPU nodes, 64 cores each. 32 A100s. Two CPU node-hours per high-fidelity trajectory. Budget: 200,000 CPU node-hours, 10,000 GPU-hours, four weeks.

He asked the cost of one trajectory and the budget before proposing a system. Clarification 9/10. Architecture 8/10.

### What he said

200,000 node-hours at two hours each is 100,000 high-fidelity trajectories, short of one million. He would spend week one on about 42,000 high-resolution runs, downsample them to 32, 64, and 128, train a super-resolution network in week two, then generate low-resolution trajectories and upsample them. If quality failed, raise the input resolution. He assumed solver cost scales with the number of grid points.

On turbulence, low MSE and high structural similarity still left the foundation model weak, and small-scale energy was low. He would cut evaluation by regime, use a physical metric per regime, look at Fourier error by frequency, try a finer resolution ladder, check whether hard regimes were underrepresented, and add data or input resolution there. 8/10.

With two weeks and 60,000 node-hours left: 32 and 64 miss turbulent structure, 128 works on about 90% of trajectories, 256 is reliable, and highly turbulent flows are 20% of the target distribution. He asked how 20% turbulence becomes a 10% failure rate. Half of the turbulent cases fail. He would spend about half the remaining time on high resolution for turbulence and half on 128 for the rest, and augment to grow the set. 6/10. His trajectory counts used the nodes and the wall clock, and they exceeded the node-hour budget.

On turning 15,000 turbulent trajectories into 200,000 examples, he said rotation might work and that he would need to look up physics-specific augmentation. The alternative he offered was a generative model constrained to the PDE and the boundary conditions. 6.5/10.

On a diffusion model whose spectra look right but whose trajectories break mass conservation or time evolution, he split statistical scores (discriminative, predictive, FID) from physical scores (mass, temporal consistency), and he would threshold with the downstream model and the requirement. 7/10.

He did not answer the last choice: 200,000 synthetic trajectories, 40,000 pass the physics checks, repair costs 20% of a new high-fidelity run. Use all, use the 40,000, or repair. Unscored.

### What landed

The budget was the first fact, and 100,000 versus one million was the right shortfall. The design was a resolution ladder plus a learned upsampler, with a fallback to a finer input. The turbulence pass diagnosed a hidden regime instead of trusting MSE. He separated a pretty spectrum from a conserved quantity.

### What broke

- **The ledger.** Remaining node-hours are the constraint, not how many nodes exist. At 256, 60,000 / 2 = 30,000 trajectories. If 128 costs a quarter of that, 0.5 node-hours, the same budget is 120,000. An even split of the hours is 15,000 at 256 and 60,000 at 128. Also keep GPU-hours, the deadline, storage, and the upsampler’s own cost. The linear grid-point assumption was not checked against the solver.
- **Storage.** Four variables, 1,000 steps, 256×256 is about 262 million scalars. FP32 is about 1.05 GB a trajectory. One million uncompressed is about 1 PB. Compression, layout, and streaming were not in the design.
- **What super-resolution cannot invent.** A 32 or 64 field can omit the turbulent scales. A network can sharpen an image and still invent the wrong dynamics. Separate a missing spatial scale from a wrong time evolution, and score the foundation model on a long horizon, not on MSE of the upsampled frame.
- **Augmentation.** A rotation that preserves an equation on an infinite domain can break this run’s boundary condition. He did not say how an augmented sample is checked. The check is a residual against the trusted solver’s tolerance, not a new generative model as the first move.
- **The residual.** For incompressible flow, \(\nabla \cdot u \approx 0\), and the momentum residual is \(\partial_t u + (u\cdot\nabla)u + \rho^{-1}\nabla p - \nu\nabla^2 u - f\), inside the tolerance of the trusted simulations. Also the initial condition, the boundary condition, the energy spectrum, and the energy budget. FID is not that test. A hard constraint and a numerical tolerance are different.

### Next mock

Not this scenario. Train the foundation model on the trajectories: representation, mixed resolution, distributed training, GPU use, throughput, validation, long-horizon rollout. Before that, a short ledger drill only: node-hours, storage, and one residual. Twenty to twenty-five minutes, three follow-ups, no hints until the end. The repair-versus-resimulate choice stays open and unscored.

## 2026-10-29 — ML depth, Closing the Loop

**Kind:** Depth. Paper: Closing the Loop, NeurIPS 2026. Bing or Ramesh simulated. He stopped after four questions. **7.0/10.** Motivation 8.5, the probabilistic step 6.0, the deterioration diagnosis 7.5, the compute tradeoff 7.0. Not the Bosch story. Do not run another full mock on this paper until the theorem is read from the manuscript. The next mock is breadth.

### What he said

The task is to generate a regularly sampled series from an irregular one. Prior work, including one of theirs, treated missingness as random drops, completed the series, and trained a generator on the completion. He named two failures. Real irregularity includes sensor failure and block missingness, and their benchmark has four kinds. A completion trained with MSE pulls toward the conditional mean, so the generator sees a biased distribution and loses coverage. Their alternative is an EM-like loop. The E-step draws a full series from a pretrained posterior \(q_w(x_{\mathrm{full}}\mid x_{\mathrm{partial}})\) and does not train. The M-step trains a diffusion model by denoising, in the same family as ImagenTime and EDM. He said the monotonicity result is for an idealized EM under stated assumptions, not automatically for the neural implementation. He offered the initialization and did not give it. He asked whether a formula belonged in a discussion interview, then said he did not remember the objective.

If quality rose and then fell, he said their runs did not do that. He would look at the M-step first, because that is the step that changes weights: learning rate, step count, convergence, and whether the learned distribution moved. He would also limit how far a new model may move from the previous one. After the challenge that a frozen E-step can still change the completed-data distribution, he proposed a toy set whose complete series are known, corrupt it, and compare each E-step to that set with a distributional score and a discriminative score. He would also watch whether the theoretical objective stops being monotone. A biased completion, once trained on, can make the next completion more biased.

On a 5% gain at five times the training cost, he would not defend it without the decision. In a scientific use the 5% might separate a usable trajectory from a useless one. In a business use it might be a large sum or nothing. To cut training cost in half he named faster samplers on the E-step, and on the M-step a learning-rate and epoch change, a smaller network, or a different generator, including flow matching or a VAE.

### What landed

The problem, the one-shot completion, and the reason a mean completion is the wrong training set. Four irregularity types as an evaluation change, separate from the algorithm. Idealized EM is not the neural loop. He did not invent a theorem he could not remember. The toy series with a known complete trajectory is the right instrument. He did not treat 5% as automatically worth five times the compute.

### What broke

- **The quantity.** He did not say what is observed, what is latent, or which objective the theorem keeps from getting worse. The post-mock write-up is classical EM: missing values as latents, an ELBO, and a nondecreasing observed-data log-likelihood when the E-step is exact and the M-step improves the expected complete-data log-likelihood. That write-up is a reference. It is not this paper’s theorem. The manuscript is not in the repo, and no public PDF turned up. Do not recite the ELBO as the result.
- **Whose posterior.** He called \(q_w\) pretrained and frozen. The project page says the loop samples completions from the generator itself, and that each round uses the current model. Those two sentences are not yet reconciled. PSLR, named on that page as the posterior sampler in the lifted image representation, was not in his answer. Initialization is still unsaid.
- **Mean collapse.** The warning applies to a conditional-mean estimator trained with MSE. It is not a claim about every completion method. The 2025 predecessor’s own abstract says the vision model is masked so completed values are weak conditioning, not a second ground truth. If “our prior” is that paper, say the mask. Do not describe it as training on the imputation as if it were data.
- **A frozen E-step can still bias the next M-step.** The weights do not move. The completed trajectories do, because they are draws from a model that just changed. Likelihood moving the right way does not mean FID, the discriminative score, or a downstream number moves the right way.
- **Profile before the menu.** Cost is outer iterations times E-step plus M-step. First measure which term dominates. Then stop when validation plateaus, warm-start the next M-step if it is not already warm-started, cut sampling steps, cut posterior samples, and shorten the M-step. A new generator, including flow matching, is the last change. Flow matching is not automatically cheaper to train or to sample.

### Public page, not the manuscript

[imageni2r.vercel.app](https://imageni2r.vercel.app/) lists Gal Fadlon and Idan Arbiv as the marked first authors and Omri Azencot last. It calls the method a co-evolving Monte Carlo EM and quotes 59% on discriminative score, 73% on context-FID, and four corruption regimes. Those figures are the page. Use one of them only after the PDF confirms it. Do not narrate their implementation as his.

### Before the next telling

Read the PDF and answer, in his words, without filling gaps: the objective, the E-step distribution, whether that posterior is the current generator, a pretrained model, or both, what the M-step updates, whether that step is a likelihood, an ELBO, a denoising loss, or something else, the theorem’s quantity and its assumptions, which of those assumptions the code drops, and the initialization. Two minutes. Then one page: formulation, the loop, initialization, the theorem, where the code departs, the result, the cost, and three hard questions. Not another scored mock unless that reading shows the motivation answer was wrong.

### Papers already used in a depth mock

Koopman as a baseline, 28 Oct, not the generative-operators paper. Flow matching, 26 Oct, only if he brings it up. Closing the Loop, this log. Still unused as a paper defense: Koopman generative operators, distillation, ImagenTime, structured Koopman autoencoders, consistent Koopman autoencoders. The next depth question is one of those.

## 2026-10-29 — ML breadth, new factory

**Kind:** Breadth, Bing Xiang simulated. A transformer predicts failure within 24 hours. Offline AUROC 0.96, precision 0.82, recall 0.88. A new factory: 0.71, 0.35, 0.52. He stopped before the last question. That question is not scored. **6.5/10.** Shift 8, the split 8, the inspection policy 5. Same gap as the 28 Oct breadth mock. Do not run another cost-and-calibration mock until the review sheet is used. Sheet: [`2026-10-29_breadth-review.md`](2026-10-29_breadth-review.md). The next mock is overfitting, regularization, and optimization. About 20 minutes, one opening question, two follow-ups.

### What he said

He called it distribution shift. He would compare the training factory with the new one, and he would look at slices rather than the three headline numbers. Failures might sit in a temperature range or an operating condition the training set does not have. He would collect data at the new factory, split it, and fine-tune, with a gate that the weak slices improve and the others do not fall apart.

On a random split of windows, with the same machines and possibly overlapping times in both sides, and with failures in about 1% of windows: the link between train and test can explain the offline score. He would split in time first and cut windows after. He would also hold out factories. AUROC can look strong when failures are rare. He would rescore at a working threshold, add AUPRC, and set the threshold from the cost of a false positive and a false negative.

On 10,000 machines, about 100 failures a day, at most 200 inspections, a miss at $20,000 and a needless inspection at $500: he would calibrate first. He remembered a sigmoid or another monotonic map and did not remember the names. He would rank the machines. If fewer than 200 were predicted to fail, he would inspect fewer than 200. He then asked to review the rest.

He did not answer why AUROC can stay at 0.85 while maintenance says there are too many needless inspections.

### What landed

Shift before a larger model. Slices, target data, and a gate against regressions. Time split before windowing, and a held-out factory. AUPRC when the positive rate is 1%. The inspection cap is a maximum, not a quota to fill.

### What broke

He did not separate a bad evaluation, a broken pipeline, a shift, and a weak model before naming shift. He did not mention units, sampling rate, or whether “failure” means the same thing at the new factory. He did not separate covariate shift, label shift, and a changed relationship between sensors and failure. He did not hold out machines, and he did not leave a gap at the time boundary. He did not say precision at 200 or recall at 200.

Calibration stayed “a sigmoid.” Ranking and a probability you can multiply by a dollar cost are different jobs. A strictly monotone map does not change AUROC or precision at K. It changes a threshold written in probability.

### Not his answer

The derivation below was written after he stopped. Do not treat it as what he said. It is on the review sheet.

If an inspection prevents the failure, and the $500 is paid only when the inspection was unnecessary, inspect when \(500(1-p) < 20000 p\), so \(p > 500/20500 \approx 2.44\%\). If every inspection costs $500, the line is \(p > 2.5\%\). With the same costs on every machine, benefit \(20500 p - 500\) ranks the same way as \(p\). Inspect the top of that list, and stop at 200 or at the first non-positive benefit, whichever comes first. If costs differ by machine, rank by the benefit, not by \(p\).

Stable AUROC is not stable precision. At a fixed true-positive rate 0.8 and false-positive rate 0.05, precision is 64% when 10% of windows fail and about 13.9% when 1% fail. An inspected machine that does not later fail is not automatically a false positive if the inspection prevented the failure. That last point was also not in his answer.

## 2026-10-29 — Behavioral, TR kill

**Kind:** Behavioral, Bing Xiang simulated. About 15–20 minutes. One opening question and two follow-ups. **8.0/10.** Judgment 9, ownership 8, leadership 7, communication 8, the lesson 8.5. Story **C** in [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Do not retell it as the next behavioral mock. The coaching script in the session still says 28 and 29.2. Do not rehearse that script.

### What he said

On the multimodal time-series project he built a dual-tower model on Qwen3-VL: a chart for scale, a delay embedding for dynamics. TSRBench, which he called 15 task domains, stalled near 50%. Reasoning was about 28%, against a random baseline near 25%. He picked temporal reasoning at 26.9%. The task looked like segment, classify, and order. He built synthetic data for it. Before the run he set two gates: no more than 3 points down overall, and no more than 5 points down on any one task.

Reasoning went from 28% to 29.2%. Some tasks rose about 7 points. Temporal reasoning fell from 26.9% to 21.9%, exactly 5 points, so he stopped that direction. More synthetic data without a cause would not be justified. The others agreed, because the gates were already written. They turned to a benchmark audit.

He showed both the gains and the gate that failed. They had already said that if the extra data did not help temporal reasoning, something else was going on. Continuing would waste more than stopping. On reflection he would audit the task and the model before adding data. The group put that into its research book: name the cause before the next intervention.

### What landed

The gates came before the run. He did not keep the mix because the average moved. He stopped the synthetic-data lever and kept the project. The lesson is a rule he says the group now uses: a hypothesis is not a diagnosis.

### What broke

- **28 and 29.2.** Same slip as 21 Oct. The bank’s pair is about 29.5 to 31.2. Temporal relations 26.9 to 21.9 is the number that held. Also unsaid: numeric reasoning down 3.4 points.
- **The gate’s scope.** He said any individual task. The bank says any reasoning subtask, plus a three-point floor on the overall score, chosen as a research tolerance and not as a statistical test. He did not say whether one seed and a five-point drop could be noise.
- **“We agreed.”** Q1 has the decision in the first person. Q2 and Q3 hand it to the group. The line to keep: he recommended stopping the mix, he said why the gate failed, and he pointed the next work at the audit. Agreement is not the decision.
- **What the audit found.** Not in this telling. Who ran it, what the failures were, and what compute the kill saved are open. Do not invent them. The research book is the one sentence he said. Do not add a chapter.

### Still open, and only if he has the fact

Why three points and five points. Whether the five-point drop was more than one seed. What the audit actually found. What he did for the people who had built the data. What he would do if someone still wanted two more weeks of synthetic data. He did not claim that disagreement happened. Do not add it.

### Not his answer

The session’s rewritten two-minute script is coaching. It still uses 28 and 29.2. Speak the bank’s 90-second version. Kill the lever, not the objective.

## 2026-10-30 — ML breadth, overfitting

**Kind:** Breadth, Ramesh Nallapati simulated. A 100M transformer, AdamW, forecasting. Training loss falls through 10,000 steps. Validation loss falls, then rises after step 6,000. A few small datasets are especially bad. One opening question and two follow-ups. **6.5/10.** Diagnosis 7, method 7.5, generalization tools 5, priority 6. Do not run another breadth mock until the list below can be said in under a minute each. The next design block is still scenario B.

### What he said

He called it overfitting, then checked the setup: the same chunking and normalization on train, validation, and test; that training actually updates the weights; that evaluation reproduces the training loss with gradients off. He would also try the optimizer. If those passed, he would train 250M and 500M models and compare validation.

When the larger models fit the training set better and the validation set worse, he left overfitting. He said a time split with no overlap can mean the validation distribution has moved. He would compare the distributions with KL and histograms, learn a map, and change trend or seasonality in the training series so they look more like validation, without solving the forecast. Augmentation or a linear forecast might bridge the gap. He would check the mapped series against validation, then the forecast metrics.

Told the distributions are similar and the gap remains, especially on small datasets, he called it class imbalance. He would resample so each dataset is drawn about equally often, or up-weight the loss on the small ones. He would resample first, because it needs less tuning.

### What landed

Overfitting was the first name, and the sanity checks were real: protocol, a live update, and a train-set eval with no gradient. A chronological split can change the distribution, and trend and seasonality are concrete places to look. Unequal datasets can dominate a mixed objective, and resampling is a legitimate lever.

### What broke

The curves already say the fit is past the validation minimum. The first action is the checkpoint near step 6,000. That picks a model. It does not change the loss. A larger model was the test he chose. The result he was then given, lower training loss and worse validation, is what extra capacity does when the data are thin. The cheap comparison is a smaller model, weight decay, and dropout, on a short sweep, with the split held fixed and the gap reported per dataset.

Shift stayed possible and stopped being the leading hypothesis once he was told the distributions match. A KL between raw high-dimensional series is a poor first measurement. A map fit so that training looks like validation, especially if it uses validation outcomes, is not a fix. It spends the set you are supposed to be surprised by.

“Class imbalance” is the wrong name. Classes were not the issue. Datasets of different sizes were. Equal sampling can hammer a small set and overfit it harder. Reweighting changes the loss. Neither one is dropout, weight decay, or a smaller net. Asked for regularization, he did not name those three.

### Not his answer

The session’s preferred order was written after the mock. Do not treat it as what he said. Early stopping at the validation minimum, then weight decay and dropout, then a smaller model, then how often each dataset is sampled. Score each change by the per-dataset validation number and the train–validation gap.

AdamW’s weight decay is applied to the weights, separate from the adaptive step. That is not the same as adding \(\frac{\lambda}{2}\|\theta\|^2\) to the loss and letting Adam rescale it. Dropout zeros activations in training. At eval it is off. Inverted dropout scales the kept units by \(1/(1-p)\) during training so the eval pass needs no extra factor. Layer norm is over the features of one token and does not use the batch. Batch norm uses the batch. A transformer uses layer norm.

A larger model can still generalize better. Capacity is not a monotone law. Optimization and the data can dominate it. Say that if asked, and still try the checkpoint first when validation has already turned up.

### Recall before the next breadth mock

Early stopping. Weight decay versus an L2 term under Adam. Dropout in train and at eval. Layer norm versus batch norm. A learning-rate schedule. Proportional sampling, equal sampling, and a temperature in between. How a learning curve separates overfitting from a shift. One minute each. No new breadth mock until AdamW and layer norm are fluent. The 30 Oct recall is [`2026-10-30_fundamentals-recall.md`](2026-10-30_fundamentals-recall.md): AdamW 4, layer norm 3. Question 7 was not taken.

The debrief says a 29 Oct recall produced Platt versus isotonic and \(B_i = 20500 p_i - 500\), so \(p > 500/20500 \approx 2.44\%\). That recall is not a scored mock and has no separate file. The 28 Oct top-10 and top-20 arithmetic is still unanswered.

Logged breadth scores are 6.5, 6.5, and 6.5. Depth is 7.5 and 7.0. Design is 7.0 and 7.0. Behavioral is 8.0 and 8.0. The averages are of these logs only. They are not a hiring scale. The repeated miss is the elaborate test before the cheap one. The aborted CFD opening on 30 Oct is not in the design average.

## 2026-10-30 — System design, industrial time series

**Kind:** System design, Vivek Govindan simulated. The first prompt was a CFD surrogate. He stopped it. That opening is not scored and is not in the 7.0 average. The restart is a foundation model on heterogeneous industrial sensors: forecast, anomaly, failure. About 100 million hours. 64 H100s for two weeks. One opening question and three follow-ups. **7.0/10.** Framing 8, architecture 6.5, pretraining 6.5, transfer 7.5, deployment 7, adaptability 7. Two completed design mocks, both 7.0.

### The aborted opening

Steady 3D velocity and pressure from geometry, about 5,000 CFD runs, 8 A100s, at least 100× faster than the solver. He would search for a physics-informed 3D generator, reproduce two papers whose inference fits the budget, then train on a subset. Split 70/15/15. Generative scores plus incompressibility, mass, and boundary conditions. He stopped when the meshes were unstructured, about 200,000 nodes, and different per geometry, and the field was mostly deterministic. A literature search is not the opening design. A baseline and its tradeoff still have to be said in an unfamiliar domain. Do not score this attempt.

### What he said

Patch the series, encode it, and attach a mask, the sampling rate, and the time range. A decoder-only transformer, because the same stack has been used for classification and for forecasting. Pretrain by completing masked spans with MSE. Split oldest time to train, then validation, then recent test, and also hold out machines and factories. Train an encoder on the series plus the side information, then fine-tune it and train the transformer. The mask tells the model which sensors and times to ignore. The three splits are the three transfer tests: new times, new machines, new factories.

Told that causal attention fights a bidirectional mask, and that one machine has 8 sensors and another 200: he switched to a transformer autoencoder. The encoder completes, the decoder emits the signal. A later stage would forecast with a causal mask and classify without one. A metadata token at the front would carry the sensor count, identities, and units. Variable length would avoid padding. Sampling rate stays in the signal.

After 48 hours, training and validation reconstruction fall, forecasting improves on seen machines and not on unseen factories, and the team wants to keep pretraining. He would check whether those factories sit inside the training distribution, with KL and histograms. If they do, he would treat the forecasting head as overfit and test that with data drawn from unseen factories whose distribution matches training, including by augmenting the training set. If the factories are missing, resample or reweight toward them and retrain. If the head is overfit, early stopping, weight decay, dropout, or a smaller head. Continue if the factories are well represented and overfitting is unlikely. Modify for a mild gap. Stop if the gap is large.

He would not ship one threshold for every factory. Rank alerts that have positive benefit. With false-positive cost \(x\) and false-negative cost \(y\), inspect when \((x+y)p - x > 0\), and \(y\) is much larger than \(x\). If a batched server handles \(z\) sequences a second and each machine sends one sequence a second, the fleet needs \(500/z\) transformers.

### What landed

Three holdouts, not one random window: future time, unseen machines, unseen factories. Unlabeled hours went to masked reconstruction, and the mask, the rate, and the time range were in the input. He dropped the decoder-only stack when causal attention was the objection. A falling reconstruction loss was not, by itself, a reason to keep spending the 64 H100s. The single threshold was refused. The benefit line \((x+y)p > x\) is the same rule as \(p > x/(x+y)\), and a non-positive benefit is not inspected.

### What broke

- **The token.** A metadata prefix is not the sensor stream. A token is one sensor’s patch, its observation mask, a time delta, a sensor identity, and a unit. Say that shape before the architecture. Per-sensor normalization is missing, and MSE across temperature and current will follow the large unit. A natural gap and a span he masked for the loss are different masks. Padding is still required in a batch, or the batch is packed. A new sensor identity needs an unknown-type embedding.
- **Causal versus bidirectional.** He corrected this when asked. The opening had already paired a decoder-only stack with masked reconstruction.
- **Head versus encoder.** KL and a histogram can show a marginal shift and miss a different temporal dependence or a different cross-sensor pattern. Freeze the encoder and train a small head on a little data from the unseen factory. Fast adaptation means the representation transferred. A flat head means it did not. Continue only if the held-out factory’s downstream number is moving and the extra hours are worth it. A lower reconstruction loss is not that number.
- **500 factories, not 500 machines.** \(500/z\) is the server count only if 500 sequences arrive each second. The prompt was 500 factories. Throughput is not the one-second update. Ingestion, the queue, the forward pass, and the alert each add delay. Cache the history, batch across machines, and screen with a cheap score before the transformer. Peak load, not the average.
- **The score is not a probability.** The benefit line needs a calibrated \(p\), per factory and per regime. Also false alarms per machine-day, missed failures, and lead time, inside the inspection cap.

### Not his answer

The session’s thirty-second pitch was written afterward. Do not treat it as what he said. The line to practice is the token, the loss on observed values only, the three holdouts, and a threshold from a calibrated cost. Then the latency path.

### Next

Not another foundation-model design until that token can be said first. The next session is a depth recall: Koopman, diffusion on his own papers, and the Closing the Loop objective. The classical ELBO is still not that paper’s theorem. One question at a time. Feedback after each recall item. No hints during a mock.

## 2026-10-30 — ML depth, multimodal

**Kind:** Depth mock. Feedback after the end. Qwen3-VL on multivariate series: chart, delay embedding, DINOv3. **7.5/10.** Architecture 8.5, alignment 8, experiments 8, the one-run decision 7.5, the causal split 5.5. Loop depth scores in this tracker: Koopman 7.5, Closing the Loop 7.0, this mock 7.5, about 7.3. The 26 Oct flow-matching mock stays 8 and is outside that three. The tables below were given to him. They are not results from the story bank.

### What he said

Series become images. If the budget allows, two views, as in the project: a chart through Qwen3-VL’s ViT, a delay embedding through pretrained DINOv3 and a projector. Stage A is perception on captions, in the LLaVA pattern: the answer is the caption, and the loss is next-token prediction. The LLM stays frozen. He trains the projector and possibly DINO. Qwen’s ViT stays frozen. Stage B is the downstream task. LoRA on the LLM, and possibly on DINO.

To stop the LLM from using only one view, captions must need view 1 or view 2, and training drops one view or keeps both. Stage A is perception of time-series images: trend, seasonality, noise, a segment, a value. It is not yet reasoning. If Stage A’s loss falls and reasoning does not, he would ablate at matched tokens, weights, budget, and data. Swap the visual form for text or patches, or another image. Alignment is cosine similarity or a likelihood against related and unrelated text. Reasoning is TSRBench’s five or six reasoning tasks, against models that are and are not time-series language models.

Given a text oracle at 92%, chart 74%, delay 69%, both 75%, and a longer Stage A at 76%, with the misses on numerical comparison and temporal order, and one training run left: the aggregate is not a bottleneck. Slice those two tasks and audit at inference cost. If the missing pieces are segmentation, value extraction, and sorting, add data for those and run a short LoRA. Native series as text spends too many tokens to compete with an image. A patch encoder might matter, and it would need its own reasoning baseline.

Trend 95%, seasonality 91%, numerical comparison 58%, temporal order 54%. Chart-only and chart-plus-delay make almost the same mistakes. Three hypotheses: the image dropped the fact, the encoder did not extract a fact that is in the image, or the LLM has the fact and cannot reason. Inference only. He would prove invertibility, true for delay embeddings and mostly true for charts, and run no experiment. For perception he would build a toy set whose embeddings are known and compare the system’s vectors to those targets. For reasoning he would read attention maps between text and vision.

### What landed

A real system, not a sketch: which tower is frozen, which loss is stage A, and LoRA only after perception. View dropout plus captions that need a specific view. Stage A named as perception, not as reasoning. On the gap, he refused to pick a bottleneck from the average, and he spent the audit before the one training run. A short LoRA is the right size for that one run.

### What broke

- **The join.** He never said how the two streams become tokens in the LLM: shapes, the projection, concatenation, a view id, and whether a gradient enters DINO. A metadata story is not that sentence. This is the same miss as the foundation-model design.
- **Dropout is not fusion.** A model can solve chart-only items and delay-only items and still never use both on one item. The comparison is chart, delay, and both, on items that are wrong unless both views are present.
- **A caption of a trend is not a numerical comparison.** Say that split. Cosine to a related sentence is not alignment. A matched-versus-mismatched score, a retrieval, or a perception probe is. Matching the parameter count is not required for an engineering comparison under a compute cap.
- **92% is not headroom.** The oracle shows the LLM can answer when the text is given. It does not show the image contains that text. A learned series encoder that emits \(K\) tokens, with \(K\) far below \(T\), is not the same objection as pasting the raw series into the prompt.
- **The causal split, 5.5.** Invertibility of the math is not invertibility of the rendered image. Rasterization, resolution, and a delay plot can keep a shape and drop the order of the peaks. There is no single correct embedding, so a distance to a chosen target does not prove perception. Attention can land on the right patch and the arithmetic can still be wrong. The tests that separate the three: recover the fact from the rendered image without the VLM; ask the VLM a one-step extraction; hand the LLM the true numbers in text and ask the same question. A jump from 54% on the image to 90% on the true numbers shows that skipping vision matters. It does not say which of the three caused it.

### Not his answer

The six-row protocol in the session was written afterward. Do not treat it as what he said. The line to practice is: name the hypothesis, the one change, the result that would support it, and what that result still does not prove.

### Next

Three short cases, feedback after each, not a scored mock. Perception versus a relation. A forecast that dies on a new machine. A one-step model that diverges on a rollout. Then either an unnamed breadth failure or the sensor-time token and the latency path. Stories A and C are still deferred.
