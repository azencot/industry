# Organizational briefing — Koltun’s organization and Ozan Sener

**Date:** 2026-10-19. **Call:** not confirmed. **Reply to Raja’s intro:** still unsent ([`2026-10-17_ozan-intro.md`](2026-10-17_ozan-intro.md)).

**Question this note answers:** What is this research organization trying to accomplish, and where could Omri contribute?

Grades: **VERIFIED** (a cited public source, or Raja’s 2026-10-17 email), **LIKELY** (several indirect signals), **SPECULATIVE**, **UNKNOWN**.

---

## What they are trying to do

Koltun directs an international research organization at Apple. The public 2024–2026 record is a lab that builds systems which perceive, simulate, and act in complex environments, and that pressure-tests whether large models actually have the spatial and sequential competence those systems need. Speed and memory are part of the claim, not a footnote.

Three threads dominate his own publication list and his selected-papers page:

1. **Embodied intelligence at scale.** Self-play driving with no human data ([Robust Autonomy Emerges from Self-Play](https://machinelearning.apple.com/research/robust-autonomy-emerges), ICML 2025). A photorealistic embodied simulator ([SPEAR](https://vladlen.info/publications/), ECCV 2026 spotlight). OpenBot-Fleet (ICRA 2024).
2. **Fast metric spatial perception, and whether multimodal models have spatial understanding.** [SHARP](https://vladlen.info/publications/) (ICLR 2026), Depth Pro and CoMotion (ICLR 2025), the negative SPACE benchmark (ICLR 2025), and [Do multimodal models imagine electric sheep?](https://arxiv.org/abs/2605.09693) (NeurIPS 2026; Raja Giryes is a coauthor).
3. **Making large models trainable and runnable under memory limits.** Cut Your Losses (ICLR 2025 oral). LOOP, a single-copy RL method for long-horizon LLM agents (arXiv 2025). [Learning to Evict from Key-Value Cache](https://arxiv.org/abs/2602.10238) (ICML 2026; Ozan). [Entropy-Preserving Reinforcement Learning](https://arxiv.org/abs/2603.11682) (ICLR 2026; Raja is a coauthor; Koltun is not).

This is not Apple’s product foundation-model organization, and it is not Health AIML. They fine-tune and analyze models such as Qwen3.5 and train a 32B agent, and they publish the systems work required to do that. **UNKNOWN** whether they sit on the critical path of Apple Intelligence.

---

## People and titles

| Claim | Grade | Source |
|---|---|---|
| Koltun is a Distinguished Scientist at Apple since August 2021 and directs an international research organization. | VERIFIED | [CV](http://vladlen.info/documents/koltun-cv.pdf), [homepage](https://vladlen.info/) (still current: NeurIPS 2026 news), LinkedIn, Wikipedia. The homepage states the role. It does not print “Distinguished Scientist”; the CV and LinkedIn do. |
| The organization has a public brand name and a published org chart. | UNKNOWN | He does not give the unit a name on his site. “Apple AI Research” in this repo is our label. |
| Ozan is a research scientist at Apple. | VERIFIED | [ozansener.net](https://ozansener.net/). |
| Ozan heads the machine learning group inside Vladlen’s organization. | VERIFIED as Raja’s wording only | Raja’s email, 2026-10-17. No public page says “head.” Do not use that title back to Ozan. |
| Ozan was at Intel Labs (postdoc, then research scientist) through January 2022, after a Cornell PhD with Ashutosh Saxena and time in Silvio Savarese’s lab. | LIKELY | His site for the degree path; LinkedIn for Intel dates. Apple affiliation is on the 2022 continual-learning preprint with Koltun. Exact Apple start date: UNKNOWN. |
| Approximate headcount, Ozan’s reports, product-embed rate, individual freedom. | UNKNOWN | Do not reuse the Intel-lab size (~30) as an Apple number. |

**Recurring names on Koltun’s 2024–2026 papers, which is a coauthor list and not a roster:** Philipp Krähenbühl, Erik Wijmans, Brody Huval, Alexander Hertzberg, Marco Cusumano-Towner, Aleksei Petrenko, Stephan R. Richter, Santhosh Kumar Ramakrishnan, Raja Giryes, Ozan Sener.

Ozan’s personal site is stale. Its publication list stops around 2020 and omits the papers that matter for this call.

---

## Ozan and Koltun do not currently share one agenda

Joint papers that are real:

- Multi-Task Learning as Multi-Objective Optimization (NeurIPS 2018)
- Learning to Guide Random Search (ICLR 2020)
- MSeg (CVPR 2020)
- Online Continual Learning with Natural Distribution Shifts (ICCV 2021)
- Domain Generalization without Excess Empirical Risk (NeurIPS 2022)
- Improving Information Retention in Large Scale Online Continual Learning (arXiv 2022; Koltun and Sener both Apple)
- Drinking from a Firehose (PAMI 2023)
- **Robust Autonomy Emerges from Self-Play (ICML 2025) — the only recent joint paper**

Ozan’s other 2024–2026 papers do not include Koltun:

- RanDumb (NeurIPS 2024), with Oxford. Fixed random or pretrained features plus a linear head beat continually trained representations.
- Addressing Misspecification in Simulation-based Inference through Data-driven Calibration, RoPE (ICML 2025 oral). Coauthors include Marco Cuturi and Guillermo Sapiro. Koltun is absent.
- Learning to Evict from Key-Value Cache (ICML 2026), with Luca Moschella and Laura Manduchi.

**LIKELY:** inside a broad organization, Ozan’s visible work is the methods slice (learning under shift, calibration, efficient inference), while a large fraction of Koltun’s 2025–2026 output is geometry, simulation, and embodied agents. Raja’s “head of the ML group” is consistent with that split. It is not proof of a reporting line.

Continual learning is their historical joint topic. It is not the center of the 2025–2026 record. Entropy-Preserving RL talks about keeping a policy trainable for sequential learning in new environments. That is a cousin of continual learning, and Ozan is not an author.

---

## Three priorities for the next 6–18 months

Ranked by how hard it would be, given the 2025–2026 papers, to claim the opposite.

### 1. Spatial and embodied intelligence, including implicit world models

**Grade: LIKELY for the organization. Ozan is on one paper in this set.**

The problem is whether an agent can perceive a metric 3D world and act in it when the model class, the simulator, or the human data is inadequate. Apple has an obvious stake in cameras, spatial computing, and on-device perception. The obstacles are simulator generality and speed (SPEAR), closing the gap from simulation to recorded driving without imitating humans (Robust Autonomy: 1.6 billion km, GigaFlow, 17.5 simulated years between incidents), and the fact that frontier models still fail animal spatial tests (SPACE). Electric sheep then reports the opposite kind of result: a fine-tuned Qwen3.5-9B, trained only to predict open-loop actions on spatial puzzles, develops activations that decode into intermediate visual state. Sixteen visual tokens per step move average solve rate from 83% to 89%.

Skills on the table: large-scale RL, simulation systems, geometric vision, multimodal fine-tuning. Omri’s background does not cover self-play driving or metric view synthesis. The discussable piece is the world-model claim: an internal state appeared without an explicit dynamics model.

### 2. Resource-limited learning and inference for large models

**Grade: LIKELY for the organization, and this is Ozan’s own 2026 paper.**

Cut Your Losses cuts the Gemma-2-2B loss footprint from 24 GB to 1 MB by never materializing the full logit matrix. LOOP keeps one copy of the LLM in memory and reports a 32B agent beating o1 on AppWorld. KV Policy learns, from key and value vectors only, a per-head ranking of cache entries by future utility. It does not modify the LLM and does not add inference cost, and it is tested out to 128K on RULER. SHARP and Depth Pro make the same move in vision: state of the art at a fraction of the latency.

The skill in demand is empirical work where the memory or latency number is the result. Omri can talk about compact state and quality–cost tradeoffs. Omri cannot claim kernel work, FSDP, or 32B RL runs. Saying “efficiency” without a baseline and a budget will sound thin in this room.

### 3. Methods that remain valid when the model, the simulator, or the representation is wrong

**Grade: LIKELY for Ozan. MEDIUM as a Koltun-wide priority.**

RoPE treats simulator misspecification as an optimal-transport problem between representations of real and simulated observations, using a small calibration set with ground-truth parameters. It was an ICML 2025 oral. RanDumb is the negative twin: on standard online continual-learning benchmarks, a fixed random feature map plus an online linear classifier beat methods whose contribution was supposed to be the learned representation. The 2022 domain-generalization paper with Koltun has the same taste: do not let an auxiliary penalty damage in-distribution risk.

This is the cleanest technical overlap with generative modeling, uncertainty, and distribution shift. The caveat is authorship. RoPE’s senior Apple coauthors are Cuturi and Sapiro, not Koltun. Sapiro sits in a different Apple orbit from this intro. Treat RoPE as Ozan’s paper, and ask him where it sits, rather than assuming it is the group’s flagship.

**Demoted.** Classical continual learning (replay, forgetting curves, CLOC) is real joint history and a poor bet for a 2027 priority. Improving Information Retention is a 2022 preprint. Do not spend a deep-read slot on it.

**Hiring.** VERIFIED: Koltun’s homepage says “We are hiring” and gives `vladlen.koltun@gmail.com`. A specific req for Ozan’s group was not found. Barcelona MLR postings and the 2026 robotics job cluster are other Apple teams. Do not prepare against those descriptions.

**Product and freedom.** UNKNOWN. The public behavior is a publishing lab with code (Depth Pro, SHARP, [ml-learning-to-evict](https://github.com/apple/ml-learning-to-evict)). Latency and memory are product-shaped constraints. There is no public evidence of a shipped feature owned by this group, and no evidence of how much a new senior researcher would be told what to work on.

---

## Where Omri could contribute

The fit is complementary on two problems and weak on the lab’s main systems. Do not walk in as a time-series forecaster, and do not walk in as someone who already does their embodied stack.

**Connection 1 — generative correction when a simulator is misspecified.** RoPE already uses a small labeled calibration set and optimal transport in representation space. Omri’s advantage is generative models of trajectories, residual structure, and calibrated uncertainty, including cases where the labels RoPE assumes are unavailable. Competing approach: their own RoPE, plus any simpler recalibration that matches it. Weakness: one oral paper is not a program, and the coauthor set may put this work outside Koltun’s main line. Concrete use: a controlled dynamical simulator with a known structural error, generative residual versus affine or OT calibration, with a pre-registered failure if the residual does not improve posterior calibration out of the calibration support.

**Connection 2 — explicit latent dynamics versus the implicit state in electric sheep.** Their result says a world model can appear as a byproduct of action prediction. Omri’s question is when that implicit state is enough, and when an explicit dynamical representation is worth its bias. Raja is on the paper, so this is a natural conversation. The failure mode is claiming Koopman structure would have raised the 83% to 89%. Their gain came from feeding a few decoded visual tokens back into the chain of thought. A serious version compares an explicit latent transition against that visual-token baseline on one of their puzzles, and accepts the result if the explicit model does not win on long-horizon puzzles once the token budget is matched.

**Connection 3 — what is worth remembering — keep this precise and secondary.** KV Policy ranks existing cache entries by predicted future utility. A Koopman or delay state compresses a trajectory into a dynamical coordinate. Both ask what must be retained. They are not the same method, and a “structured KV cache” pitch is easy to demolish. Study the paper so the distinction is clean. Do not open with Idea 1 from the prep plan.

**Weak relative to this org, as of the public record:** metric 3D perception, photorealistic simulation, self-play, policy-gradient systems, and frontier-scale training. Raja’s intro already described Omri as having time-series and 3D-geometry experience. The unsent reply drops the geometry clause and leads with generative and multimodal models, sequential learning, and structured representations. Those two framings should not diverge by accident. Geometry matches Koltun’s perception stack better than forecasting does, and only if it is still something Omri can defend technically.

**Observable practices worth mirroring, from the papers rather than from a guessed personality:**

- A simple or constrained baseline has to lose before a new representation counts. RanDumb is the template.
- The headline number is large and specific: kilometers, years between incidents, gigabytes to megabytes, milliseconds.
- Negative results are publishable. SPACE is titled around “not yet.”
- Generalization is a transfer setting (new homes, real driving logs, longer contexts, misspecified simulators), not a test split of the training distribution.

---

## Four papers to study

Budget: two deep, two moderate, plus one short adversarial skim. Skip Improving Information Retention.

| Slot | Paper | Why this one |
|---|---|---|
| Deep | **Robust Autonomy Emerges from Self-Play**, Cusumano-Towner et al., ICML 2025. Ozan and Koltun. [Apple page](https://machinelearning.apple.com/research/robust-autonomy-emerges). | Only recent joint paper. Shows the empirical standard: scale, a simulator that makes the scale possible, transfer without the obvious data source, a human-realism check. |
| Deep | **Learning to Evict from Key-Value Cache**, Moschella, Manduchi, Sener, ICML 2026. arXiv:[2602.10238](https://arxiv.org/abs/2602.10238). | Ozan’s latest methods paper, and one he can discuss as an owner. Future utility, per-head RL, no change to the LLM. |
| Moderate | **Do multimodal models imagine electric sheep?**, Ramakrishnan, Vondrick, Giryes, Krähenbühl, Koltun, NeurIPS 2026. arXiv:[2605.09693](https://arxiv.org/abs/2605.09693). | Newest statement of the org’s question about implicit world models. Raja is a coauthor. This is the paper that pressures an “explicit structure” introduction. |
| Moderate | **RoPE**, Wehenkel, Gamella, Sener, Behrmann, Sapiro, Jacobsen, Cuturi, ICML 2025 oral. [Apple page](https://machinelearning.apple.com/research/addressing-misspecification). | Closest equation-level overlap with generative modeling and calibration. Remember who is not an author. |
| Skim, ~30 min | **RanDumb**, Prabhu et al., NeurIPS 2024. Ozan. [OpenReview](https://openreview.net/forum?id=TZ5k9IYBBf). | The adversarial paper for a representation-learning pitch. If a fixed random map wins, a structured encoder has to explain why the benchmark was the wrong test. |

SHARP and Depth Pro matter if the conversation turns to geometry or to Raja’s “3D” clause. They are a poor use of the three-hour paper block otherwise.

---

## What this changes in the plan

- Tier 1 for a conversation with Ozan is implicit and explicit state, generative calibration under misspecification, and memory-limited inference. Continual learning moves to familiarity unless he brings it up.
- The candidate sentence about structured generative representations of dynamical systems is a credible identity. It is not a description of their current papers. The version that fits the room asks when an implicit state inside a large model is enough.
- Idea 2 (generative calibration of a misspecified simulator) and Idea 3 (explicit versus emergent temporal state) match the record. Idea 1 (structured KV memory) is the one most likely to sound glued on.

Next block, after confirmation: the four paper notes and the RanDumb skim. No introductions, no mock, no edits to the unsent reply until you say so.
