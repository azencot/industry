# Siemens loop — prep plan — 28 Oct 2026

**Loop:** Tue 3 Nov 2026, 1:00–4:00 PM PST. Wed 4 Nov, 4:00–7:00 AM Thailand. Bing Xiang, Vivek Govindan, Ramesh Nallapati, one hour each, no break in the note.
**Window:** Wed 28 Oct through Mon 2 Nov. About 5.5 hours a day. Tue 3 Nov is a light review only. Sleep for a 4:00 AM start.
**Spec:** Danielle named ML breadth, ML depth, and ML system design. She did not assign an hour to a person. STAR, “I,” a number, different projects, about 10 minutes of questions, and a specific Why Siemens. Coding is still unconfirmed. One hour of refresh, not a new coding round.
**Logs:** [`mocks.md`](mocks.md). Stories: [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). Why Siemens: [`2026-10-14_recruiter-prep.md`](2026-10-14_recruiter-prep.md).

Scores already on the board: system design **6.5** (highest priority), depth **8**, breadth unfinished. Targets by 3 Nov: system design 8, breadth 8, depth 8.5.

---

## What not to change

The Sunday story list in the source brief does not match the bank. Use the bank.

| Brief label | Use |
|-------------|-----|
| Innovation | **A** ImagenTime. One number. GAF is dense. The sparse image is the line plot. EDM is the sampler, separate from the image. |
| Cross-functional | **E** Bosch. Interpolation plus an observation mask. Research baseline. No product ship. No invented number. |
| Learning from a failure | **C** TR kill. Gates before the run. 26.9 to 21.9. Reasoning average is not 28. |
| Leadership under uncertainty | **B** Dual tower. TSExam was flat. Matched controls. Do not chase scores. |

Do not add a vector-field project as a fourth story unless he names it and it is already his. Do not lead with students or a lab. IC verbs.

Danielle Robinson: his questions to her are about seniority and what a strong design answer contains. Do not ask her for the interview questions. Do not quote her on the call.

---

## Days

| Day | Theme | Deliverable |
|-----|--------|-------------|
| **Wed 28** | Breadth: imbalance, calibration, leakage, shift, classical vs deep. Recall log: [`2026-10-28_breadth-recall.md`](2026-10-28_breadth-recall.md). The mock is still separate. | Weight vs threshold vs Platt. Reliability diagram, Brier, ECE. FPR times the negative count. Rank vs probability. |
| **Thu 29** | System design. Redo the 500-machine anomaly case, then a probabilistic forecast for 1,000 sensors. Two short mocks. | Two 10-minute end-to-end explanations. Open with requirements, baseline, evaluation, deployment. |
| **Fri 30** | Breadth: SGD vs AdamW, weight decay, clipping, contrastive and masked representation, ablations, uncertainty. | One breadth mock with no open conceptual gap. |
| **Sat 31** | Depth. Conditional vs marginal flow, the conditional expectation, continuity equation, Euler errors, probability-flow ODE, DDIM, EDM. Then ImagenTime and the multimodal project. | Two five-minute defenses that survive a follow-up. |
| **Sun 1** | Shadow, canary, rollback, drift, delayed labels. Then A, B, C, E out loud. One system-design mock. | Four stories, 2–3 minutes, bank method and one metric. |
| **Mon 2** | One hour each: breadth, depth, system design. Then stories and the questions below. | Readiness note: remaining misses, the identities, the design checklist. |
| **Tue 3** | 60–90 min on the misses only. 30 min on the four stories. 20 min on the call setup. No new topic. | Sleep. |

System-design order, every time: requirements, data and leakage, baseline, model, offline metric that can kill it, serving, shadow then rollout, monitor and rollback. A strong model with no deployment is not a pass.

Breadth identities still open from the stopped mock: `scale_pos_weight` is not a calibrated probability. AUROC 0.96 with AUPRC 0.35 and precision 20% is not a reason to ship. Reliability diagram, Brier, ECE. Platt or isotonic on a held-out set that matches deployment prevalence. Threshold from cost, not from 0.5.

Depth identities: \(x_t=(1-t)x_0+tx_1\) is the conditional path. \(v^*(x,t)=\mathbb{E}[x_1-x_0\mid x_t=x]\) is the marginal field, and those trajectories need not be straight. Continuity equation. Euler local error \(O(h^2)\), global \(O(h)\). TSTR plus TRTR plus real-plus-synthetic, on the same real holdout, with a rare slice and a seed interval.

---

## Interviewers

Who owns breadth, depth, or system design is unknown. Do not assign a topic. Titles below are public claims. Scrapers still list old jobs. Do not open by reciting a title.

### Bing Xiang — 1:00 PM PT

**Role.** Danielle Chandler posted on 27 May 2026 that he joined the Data & AI team. A later writeup, not a Siemens page, says he described the job as leading a team on physical AI for industrial applications. Google Scholar still says Head of AI Research, Goldman Sachs. Treat “VP” labels on aggregator sites as unverified.

**Record.** IBM Research, then AWS applied science, then Goldman. Joint work with Nallapati includes abstractive summarization (2016), OCGAN (CVPR 2019), and the SageMaker elastic-training paper (2020). Also ABCNN and the structured self-attentive sentence embedding.

**Hypothesis, not an assignment.** A long NLP and representation record, now in a new industrial org. He can press whether a representation preserves the signal, what the ablation killed, and whether a benchmark win is the decision an engineer needs.

**Overlap.** Representation choice and generative evaluation. ImagenTime and the dual tower are the material. His papers are text and code, not sensors. Do not pretend a shared problem.

**Questions.** What result in the first two quarters would make this group drop an approach? When a representation looks strong on a benchmark and fails the industrial decision, what is the gate? What does a principal own relative to the science group, as opposed to a people-manager seat?

### Vivek Govindan — 2:00 PM PT

**Role.** His public profile says Senior Principal Machine Learning Engineer, Siemens Physical AI, Seattle, from April 2026, on engineering design and simulation. The same profile still lists a current Amazon job, so the scraper is stale. Use the Siemens paragraph. Do not cite both as current.

**Record.** AWS Transcribe and Bedrock inference: streaming ASR, HealthScribe, speculative decoding, KV cache, batching. Coauthor on a neural diarization paper and on Internal Value Functions (NeurIPS 2025 Efficient Reasoning workshop), with other Amazon authors.

**Hypothesis, not an assignment.** The person most likely to ask how it runs: latency, a solver versus a surrogate, what you monitor, and when the classical model stays. That is the 6.5 gap. It is not evidence that his hour is system design.

**Overlap.** Sampling cost (EDM, the step counts in the depth mock) and the deployment half of the anomaly design. Koopman and operator models are the scientific overlap with simulation, if he opens that. Do not lecture his ASR papers.

**Questions.** When the learned model and the numerical solver disagree, what is the rule for which one an engineer trusts? What latency or failure mode keeps the simpler model? In the first month a model runs in shadow, what do you watch before any alert is enabled?

### Ramesh Nallapati — 3:00 PM PT

**Role.** On 27 May 2026 he posted that he joined Siemens as Vice President of Applied Science to lead a science organization for Physical AI in industrial applications. Amazon Science still lists him as a Senior Principal Scientist at AWS. The post is his. The org chart is not confirmed by Danielle.

**Record.** Extractive summarization (SummaRuNNer), the 2016 abstractive model with Xiang, OCGAN with Xiang, code representation learning (ICLR 2024), bifurcated attention for inference (ICML 2024). Text, code, and serving cost.

**Hypothesis, not an assignment.** A science lead with a joint history with Xiang. Likely to test whether the experiment supports the claim, and whether average quality hides the rare failure. Same caution: not assigned to depth.

**Overlap.** Train-on-synthetic test-on-real, ablations, and the limit of a claim. The depth mock’s 9 on model selection is the posture. The continuity-equation identity is the line to have ready if generative models come up. Do not recap his summarization papers back to him.

**Questions.** What has to be true before a model sits next to a simulator an engineer uses? How does a research result become something an engineer runs, and what evidence is required first? Where has a strong average hidden a failure on the rare case?

---

## How a mock is run

One question. Wait. Follow the assumption he stated. Do not hand the design over while he is answering. Score after the block, not during. A system-design answer with no shadow, rollout, or monitor does not get credit for the model.
