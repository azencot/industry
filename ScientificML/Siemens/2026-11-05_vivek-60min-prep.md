SIEMENS — VIVEK GOVINDAN

60-MINUTE OFFLINE ML SYSTEM DESIGN PREPARATION

November 5, 2026 | Principal Applied Scientist — Physical AI

Interviewer: Vivek Govindan
Expected focus: ML System Design
Preparation goal: Demonstrate that I can design, evaluate, deploy, and operate ML systems—not merely develop models.

⸻

PART 0 — HOW TO USE THIS GUIDE

Suggested 60-minute schedule:

Minutes	Activity
0–5	Review the design framework
5–25	Scenario A: Industrial predictive maintenance
25–40	Scenario B: Foundation model for industrial time series
40–50	Infrastructure, reliability, and scaling
50–57	Rapid-fire system design questions
57–60	Questions for Vivek and final reminders

Important: Try answering each scenario yourself before reading the proposed solution.

⸻

PART 1 — THE SYSTEM DESIGN FRAMEWORK

The first 90 seconds

When given a problem, do not immediately propose a neural network.

Start with:

“Before choosing a model, I’d like to clarify the operational objective, the data available, and the constraints on the system.”

Ask questions in five categories.

1. Objective

* What exactly are we predicting?
* What action follows the prediction?
* What is the cost of a wrong prediction?
* What is the required prediction horizon?

2. Data

* How many machines, plants, and sensors?
* Sampling frequency?
* Historical coverage?
* Label quality and delay?
* Missing observations?
* Different operating conditions?

3. Scale

* Predictions per second?
* Number of concurrent devices?
* Training data volume?
* Real-time or batch inference?
* Edge or cloud deployment?

4. Evaluation

* What metric reflects operational value?
* What baseline currently exists?
* What is the acceptable false-alarm rate?
* How do we evaluate unseen machines?

5. Deployment

* What happens if the model is unavailable?
* Can predictions trigger physical actions?
* What latency is acceptable?
* How frequently can models be updated?

The seven-step answer

Use this sequence throughout the interview.

1. Define the prediction target and decision.
2. Quantify the data and serving scale.
3. Design data ingestion and preprocessing.
4. Establish baseline and candidate models.
5. Specify training and validation.
6. Design serving and monitoring.
7. Discuss failure modes, tradeoffs, and iteration.

Key principle: Every architecture decision should connect to a requirement.

⸻

PART 2 — SCENARIO A: INDUSTRIAL PREDICTIVE MAINTENANCE

Interview Prompt

“Siemens operates thousands of industrial machines. Each machine has multiple sensors recording temperature, vibration, pressure, and electrical signals. Design a system that predicts equipment failures sufficiently early to schedule preventive maintenance.”

This is a plausible practice scenario, not a prediction of Vivek’s actual question.

STEP A1 — CLARIFY REQUIREMENTS

Ask:

* What constitutes a failure?
* Is the goal failure classification, remaining useful life, or anomaly detection?
* What is the warning horizon?
* Are labels available?
* Are failures rare?
* Can machines differ significantly?
* How frequently must predictions be produced?
* What is the cost of unnecessary maintenance?

Assume:

* 1,000 machines across 20 plants.
* 50 sensors per machine.
* Sampling frequency: 1 Hz.
* Two years of historical data.
* Failure prevalence is low.
* Predictions generated every five minutes.
* Maintenance teams need 24-hour advance warning.
* Cloud training, edge or local serving.

STEP A2 — ESTIMATE SCALE

Raw measurements per second:

1,000 machines × 50 sensors × 1 sample/s = 50,000 values/s.

Assuming float32:

50,000 × 4 bytes = 200 KB/s.

Per day:

200 KB/s × 86,400 ≈ 17.3 GB/day.

Per year:

Approximately 6.3 TB of raw numerical values.

This excludes timestamps, identifiers, metadata, replication, and storage overhead.

Predictions:

1,000 machines / 300 seconds ≈ 3.3 predictions/second on average.

Important insight: Data ingestion may be much more demanding than inference.

Even a relatively complex model might be affordable if each machine only requires a prediction every five minutes.

Likely follow-up

“What changes if we scale to one million machines?”

Raw ingestion increases approximately 1,000×:

17.3 TB/day of raw values.

Inference increases to roughly 3,333 predictions/second.

At that point, architecture decisions around compression, distributed ingestion, storage, feature computation, and model-serving efficiency become central.

⸻

STEP A3 — DATA ARCHITECTURE

Proposed pipeline:

Sensors
→ Edge gateway
→ Message broker
→ Streaming preprocessing
→ Time-series storage
→ Feature computation
→ Model inference
→ Alert service
→ Maintenance dashboard

Edge gateway

Responsibilities:

* Collect sensor measurements.
* Validate timestamps.
* Buffer during network outages.
* Detect missing or malformed data.
* Compress or aggregate measurements when appropriate.

Message broker

Kafka or an equivalent durable streaming system.

Responsibilities:

* Decouple producers from consumers.
* Support partitioning by machine ID.
* Allow replay.
* Handle transient failures.

Storage

Two logical layers:

Raw historical storage: Object storage for training and retrospective analysis.

Recent time-series storage: Optimized for low-latency access to recent measurements.

Feature computation

Examples:

* Rolling mean and variance.
* Spectral energy in relevant frequency bands.
* Temperature gradients.
* Vibration peaks.
* Autocorrelation.
* Changes relative to machine-specific baselines.

Critical detail

All training features must be computed using only information available at the prediction timestamp.

No future leakage.

⸻

STEP A4 — DEFINE LABELS CORRECTLY

Suppose the system predicts whether a machine will fail within the next 24 hours.

At time t:

y(t) = 1 if failure occurs in (t, t + 24 hours].

Otherwise y(t) = 0.

Potential complications:

* Maintenance can prevent failures.
* Machines may be shut down before failure.
* Failure timestamps may be inaccurate.
* Multiple failure types may exist.
* Nearby windows from the same failure event are highly correlated.

Important follow-up

“What if preventive maintenance means you never observe the failure?”

This introduces intervention bias and potentially censored outcomes.

A simple supervised classifier trained on observed failures may learn biased risk estimates.

Possible approaches:

* Explicitly model interventions.
* Use survival analysis with appropriate censoring assumptions.
* Evaluate using historical maintenance policies.
* Run controlled prospective studies where feasible.

Strong answer: The labels reflect both the physical process and the maintenance policy. I would not treat them as unbiased observations of what would have happened without intervention.

⸻

STEP A5 — MODEL SELECTION

Start simple.

Baseline 1: Rules

Thresholds on temperature, vibration, or other engineering measurements.

Useful because:

* Interpretable.
* Cheap.
* Easy to deploy.
* Establishes a meaningful operational baseline.

Baseline 2: XGBoost

Use engineered temporal features.

Advantages:

* Strong on structured data.
* Efficient training and inference.
* Works well with moderate data.
* Easier to interpret than large deep networks.

Candidate 3: Temporal neural model

Options:

* TCN.
* Transformer.
* State-space model.
* Pretrained time-series foundation model.

Potential benefits:

* Learns complex temporal dependencies.
* Reduces manual feature engineering.
* Can share information across machines.

Selection criterion

Choose the simplest model meeting:

* Detection performance.
* Alert budget.
* Inference latency.
* Robustness.
* Maintenance requirements.

Avoid: Selecting a foundation model simply because it is fashionable.

⸻

STEP A6 — TRAINING AND VALIDATION

Data splitting

Do not randomly split overlapping windows.

That creates leakage through near-duplicate observations.

Use:

Temporal holdout: Train on earlier periods, validate on later periods.

Machine holdout: Evaluate on unseen machines.

Plant holdout: Evaluate on completely unseen plants.

These measure different kinds of generalization.

Class imbalance

Suppose only 0.1% of machine-windows precede failures.

Accuracy is nearly meaningless.

Useful metrics:

* Precision-recall AUC.
* Recall at a fixed alert budget.
* Precision at the operating threshold.
* Event-level detection rate.
* Warning lead time.
* Calibration.

Event-level versus window-level evaluation

A failure event may generate many positive windows.

A model could perform well on window-level metrics while failing to provide useful early warnings.

Evaluate:

* Percentage of failure events detected.
* Time between first useful alert and failure.
* False alerts per machine per month.
* Alert persistence and duplication.

Important: A single failure should not count as hundreds of independently detected events.

⸻

STEP A7 — DECISION POLICY

Assume:

* Maintenance can investigate 20 alerts per day.
* There are 1,000 machines.
* The model produces a calibrated failure probability.

Rank machines by estimated risk or expected operational benefit.

A threshold should be selected using:

* Maintenance capacity.
* False-positive costs.
* Missed-failure costs.
* Alert lead time.
* Operational constraints.

Cost-sensitive decision rule

If:

* C_FN = cost of missing a failure.
* C_FP = cost of unnecessary intervention.
* p = calibrated probability of failure.

Then, under a simplified binary decision model:

Intervene when:

p × C_FN > (1 − p) × C_FP.

Equivalently:

p > C_FP / (C_FP + C_FN).

Real maintenance decisions may require a richer cost model incorporating intervention effectiveness and scheduling.

Calibration

Use reliability diagrams, Brier score, and calibration error.

A model with good ranking may still provide poorly calibrated probabilities.

⸻

STEP A8 — SERVING

Option 1: Cloud inference

Advantages:

* Centralized deployment.
* Easier model updates.
* Shared GPU resources.

Disadvantages:

* Network dependence.
* Latency variability.
* Data-transfer costs.

Option 2: Edge inference

Advantages:

* Lower network dependence.
* Local operation.
* Potentially faster response.

Disadvantages:

* Hardware constraints.
* Difficult fleet-wide updates.
* Device heterogeneity.

Recommended approach

For five-minute predictions, cloud or plant-local inference may be sufficient.

If connectivity is unreliable, deploy a lightweight edge model or deterministic fallback.

Deployment strategy

1. Offline validation.
2. Shadow mode.
3. Limited pilot.
4. Human-reviewed alerts.
5. Gradual rollout.
6. Continuous monitoring.

No autonomous shutdown without an explicit safety case and appropriate authorization.

⸻

STEP A9 — MONITORING

Monitor three levels.

Data health

* Missing sensor readings.
* Timestamp irregularities.
* Sensor drift.
* Distribution changes.
* Out-of-range values.

Model health

* Prediction distributions.
* Calibration.
* Event-level recall.
* False-alert rates.
* Performance by machine and plant.

System health

* Ingestion lag.
* Inference latency.
* Queue depth.
* Service availability.
* Failed predictions.
* Model version.

Retraining

Do not retrain automatically just because an input distribution changes.

Investigate whether:

* Sensors changed.
* Operating conditions changed.
* The underlying physical process changed.
* Label definitions changed.

Retrain or adapt when evidence supports it.

⸻

PART 3 — SCENARIO B: FOUNDATION MODEL FOR INDUSTRIAL TIME SERIES

Interview Prompt

“Siemens has time-series data from thousands of industrial systems. We want to train a foundation model that generalizes to new machines with little or no fine-tuning. Design the system.”

This scenario is particularly relevant given Siemens’ emphasis on Physical AI and Ramesh’s comment about data scarcity.

STEP B1 — CLARIFY THE GOAL

Ask:

* Forecasting, anomaly detection, generation, or multiple tasks?
* Zero-shot or few-shot?
* Univariate or multivariate?
* Variable sensor configurations?
* Different sampling frequencies?
* What physical metadata is available?
* How much historical data?
* Is simulation data available?

Assume:

* 100,000 machines.
* Variable numbers of sensors.
* Different operating regimes.
* Real and synthetic data.
* Forecasting and anomaly detection.
* Strong zero-shot generalization is desired.

⸻

STEP B2 — THE CENTRAL RESEARCH CHALLENGE

A machine is not merely a generic sequence.

Different systems have different:

* Physical dynamics.
* Sensor semantics.
* Units.
* Sampling frequencies.
* Operating regimes.
* Control inputs.

A model trained on one plant may fail on another despite similar-looking time series.

Key question: What information must the model receive to identify the system it is predicting?

Possible conditioning:

* Recent observation history.
* Machine metadata.
* Sensor type and units.
* Control inputs.
* Operating conditions.
* Physical parameters.

This is where the system-design problem becomes scientifically interesting.

⸻

STEP B3 — DATA PIPELINE

Raw time series
→ Validation
→ Sensor metadata alignment
→ Time normalization
→ Window extraction
→ Dataset sampling
→ Training shards
→ Distributed training

Missing observations

Avoid assuming missing values are zeros.

Use:

* Missingness masks.
* Time-since-last-observation features.
* Appropriate interpolation where justified.
* Models supporting irregular sampling.

Variable sampling frequency

Options:

* Resample onto a common grid.
* Use continuous-time representations.
* Encode timestamps explicitly.
* Train across multiple sampling rates.

Be careful about aliasing and information loss.

Variable sensor configurations

Options:

* Sensor-specific embeddings.
* Metadata-conditioned encoders.
* Set-based architectures.
* Shared temporal encoder with cross-channel attention.

Avoid assuming sensor channel 3 means the same thing across machines.

⸻

STEP B4 — MODEL ARCHITECTURE

Baseline

A pretrained univariate forecasting model or simple pooled model.

Candidate architecture

1. Sensor encoder.
2. Temporal encoder.
3. Cross-sensor interaction module.
4. Metadata/control conditioning.
5. Task-specific prediction heads.

Possible temporal backbones:

* Patch-based Transformer.
* State-space model.
* TCN.
* Hybrid architecture.

Why patching?

Reduces sequence length and computation.

Example:

Raw sequence length = 4,096.

Patch size = 16.

Token count ≈ 256.

Full attention interactions fall from approximately:

4,096² ≈ 16.8 million

to:

256² ≈ 65,536.

A 256× reduction in the number of token-pair interactions, ignoring other costs.

Tradeoff: Patching may lose high-frequency information.

⸻

STEP B5 — TRAINING OBJECTIVES

Possible objectives:

Forecasting

Predict future observations conditioned on history.

Masked reconstruction

Reconstruct masked temporal segments.

Contrastive learning

Align related observations or operating conditions.

Generative modeling

Learn the distribution of possible trajectories.

Multitask learning

Combine complementary objectives.

Important: More objectives do not automatically improve transfer.

Evaluate whether each objective improves held-out machine and plant performance.

⸻

STEP B6 — SYNTHETIC DATA

Ramesh explicitly mentioned that Siemens uses synthetic examples because real data is scarce.

This makes synthetic-data design a potentially valuable discussion.

Sources

* Physics-based simulation.
* Generative models.
* Controlled synthetic processes.
* Perturbations of real trajectories.

Benefits

* Rare-event coverage.
* Parameter sweeps.
* Controlled evaluation.
* Additional training diversity.

Risks

* Simulator-to-real gap.
* Unrealistic dynamics.
* Missing sensor artifacts.
* Incorrect noise models.
* Overrepresentation of easy synthetic examples.

Strong evaluation

Train three versions:

A. Real data only.

B. Synthetic data only.

C. Real + synthetic data.

Evaluate all three on untouched real-world test data.

Also vary synthetic-data proportion.

If C beats A, investigate which conditions benefit and whether gains persist on unseen plants.

Critical: Synthetic data quality is defined by downstream real-world utility, not visual plausibility alone.

⸻

STEP B7 — GENERALIZATION EVALUATION

Use multiple test conditions:

1. Seen machine, future time.
2. New machine, same plant.
3. New plant, same machine type.
4. New machine type.
5. New operating regime.
6. Different sampling frequency.
7. Missing or degraded sensors.

Report performance separately.

A single average metric hides important failure modes.

Zero-shot evaluation

Freeze the model.

Do not use target test labels for adaptation or hyperparameter selection.

If calibration or normalization uses target-domain data, document that explicitly.

Few-shot evaluation

Specify the exact amount of target-domain data.

Compare against strong local baselines trained on the same data budget.

⸻

STEP B8 — SERVING AND COST

Foundation models may be too expensive for all machines.

Possible strategy:

* Large model for offline or periodic analysis.
* Small distilled model for frequent predictions.
* Shared encoder with lightweight task heads.
* Cache representations when possible.
* Batch predictions across machines.

Measure:

* Predictions per second.
* P50/P95/P99 latency.
* Memory.
* Compute cost per machine.
* Accuracy versus latency.

Key insight: The optimal training architecture and optimal serving architecture may differ.

⸻

PART 4 — ENGINEERING DEPTH: WHAT VIVEK MAY PROBE

Given Vivek’s engineering background, I would prepare especially carefully for this section.

Q1. How do you prevent training-serving skew?

Use the same feature definitions and transformations in training and inference.

Version preprocessing code and metadata.

Validate online/offline feature parity.

Test representative production inputs before rollout.

Q2. What happens when Kafka delivers duplicate messages?

Assume at-least-once delivery unless stronger guarantees are explicitly established.

Use event identifiers and idempotent processing.

Deduplicate by machine ID, timestamp, and event identity where appropriate.

Handle late and out-of-order events using event-time semantics and watermarks.

Q3. What happens if a sensor stops sending data?

Detect missingness.

Mark sensor health.

Apply a justified fallback.

Avoid silently replacing missing values with normal readings.

Alert when data quality is insufficient for reliable prediction.

Q4. How would you handle a model outage?

Use:

* Last-known-good model.
* Deterministic safety rules.
* Retry with bounded backoff.
* Circuit breakers.
* Clear degraded-mode behavior.

Never let an unavailable ML service silently disable safety-critical protection.

Q5. How do you roll out a new model?

Shadow deployment → canary → gradual rollout.

Compare:

* Prediction differences.
* Latency.
* Alert rates.
* Calibration.
* Operational outcomes.

Keep a rollback path.

Q6. What if model quality degrades after deployment?

Determine whether the cause is:

* Data pipeline failure.
* Sensor change.
* Covariate shift.
* Concept drift.
* Incorrect labels.
* Model-serving bug.

Do not immediately retrain without diagnosis.

Q7. How do you choose between GPU and CPU inference?

Measure actual workload.

CPU may be sufficient for:

* Small models.
* Low inference rates.
* Tight deployment constraints.

GPU may help with:

* Large neural models.
* High-throughput batching.
* Heavy matrix operations.

Include utilization, memory, latency, and total cost.

Q8. How do you reduce inference latency?

First profile.

Then consider:

* Batching.
* Quantization.
* Distillation.
* Smaller sequence lengths.
* Optimized kernels.
* Caching.
* Better hardware placement.

Avoid sacrificing accuracy without measuring the tradeoff.

Q9. How do you ensure reproducibility?

Version:

* Raw data snapshots.
* Train/validation/test splits.
* Feature code.
* Model configuration.
* Random seeds.
* Training environment.
* Checkpoints.
* Evaluation scripts.

Every deployed model should be traceable to its training inputs and evaluation results.

Q10. How do you manage multiple model versions?

Maintain a model registry.

Associate each version with:

* Training dataset.
* Evaluation results.
* Configuration.
* Deployment status.
* Compatibility requirements.

Support rollback and staged migration.

⸻

PART 5 — RAPID-FIRE QUESTIONS

Try answering each aloud in 30–60 seconds.

1. Why not use a Transformer for every problem?

Because the best architecture depends on data volume, temporal dependencies, serving constraints, and available baselines. For structured industrial data, gradient-boosted trees may be competitive and substantially cheaper.

2. What is the difference between batch and streaming inference?

Batch processes groups of records on a schedule. Streaming processes incoming events continuously or in small microbatches.

Choose based on freshness requirements and throughput.

3. What is the difference between data drift and concept drift?

Data drift often refers to changes in input distributions. Concept drift refers to changes in the relationship between inputs and targets.

Input drift does not necessarily imply degraded predictions.

4. Why is AUROC insufficient for rare failures?

It can look strong despite poor precision at realistic operating thresholds.

Use PR-AUC, precision at alert capacity, event-level recall, and operational cost.

5. How do you handle delayed labels?

Maintain prediction logs and join them with outcomes when available.

Track metrics by prediction cohort and maturity.

Avoid interpreting incomplete recent labels as negatives.

6. What is the difference between model latency and end-to-end latency?

Model latency measures computation inside the model.

End-to-end latency includes ingestion, preprocessing, queues, network transfer, inference, and downstream actions.

7. Why might synthetic data hurt?

It may introduce incorrect correlations, unrealistic dynamics, or excessive representation of easy cases.

Evaluate on real held-out data.

8. What is the biggest danger in time-series evaluation?

Leakage through overlapping windows, shared machines, future-derived features, or preprocessing fitted on the full dataset.

9. How do you handle uncertainty?

Distinguish:

* Aleatoric uncertainty: inherent variability.
* Epistemic uncertainty: uncertainty from limited knowledge or data.

Use calibrated predictive distributions, ensembles, or other appropriate methods.

Evaluate uncertainty quality, especially under distribution shift.

10. What makes an ML system production-ready?

Reliable data, validated model, monitored serving, appropriate latency, reproducibility, rollback, security, and safe failure behavior.

⸻

PART 6 — POSSIBLE ALTERNATIVE SCENARIOS

Vivek’s public profile also connects him to audio and speaker-diarization research.

If he chooses a problem outside industrial time series, reuse the same system-design framework.

Scenario C: Real-time audio diarization

Prompt:

“Design a service that transcribes meetings and identifies who spoke when.”

Clarify:

* Streaming or offline?
* Latency target?
* Number of speakers?
* Overlapping speech?
* Audio quality?
* Privacy requirements?

Architecture:

Audio ingestion
→ Voice activity detection
→ Speech recognition
→ Speaker segmentation/diarization
→ Speaker assignment
→ Transcript assembly
→ Output

Metrics:

* Word error rate.
* Diarization error rate.
* Speaker confusion.
* Latency.
* Cost per audio hour.

Failure modes:

* Overlapping speech.
* Noise.
* Short utterances.
* Speaker changes.
* Accents.
* Domain-specific vocabulary.

System considerations:

* Streaming state.
* Incremental results.
* Revisions to earlier speaker assignments.
* Backpressure.
* Privacy and retention.

Do not assume this will be asked; it is a secondary possibility based on his public research activity.

⸻

Scenario D: ML surrogate for physical simulation

Prompt:

“An industrial simulator takes hours to evaluate one configuration. Design an ML surrogate that produces predictions in seconds.”

Clarify:

* What are the inputs?
* What are the outputs?
* What physical constraints apply?
* Is the simulator deterministic?
* What accuracy is required?
* Are unseen geometries involved?

Architecture:

Simulator runs
→ Dataset construction
→ Geometry/parameter encoding
→ Surrogate training
→ Physics-aware validation
→ Inference service

Model options:

* MLP for low-dimensional parameters.
* GNN for mesh-based inputs.
* Neural operator for function-to-function mappings.
* Hybrid model using physical structure.

Evaluation:

* Relative error.
* Constraint violations.
* Worst-case error.
* Out-of-distribution performance.
* Speedup versus simulator.

Deployment:

* Confidence or applicability checks.
* Fall back to the full simulator when needed.
* Use uncertain predictions to select new simulation runs.

Strong extension: Active learning

Choose simulation configurations where additional labels would be most informative.

Potential strategies:

* Uncertainty sampling.
* Diversity sampling.
* Expected improvement.
* Coverage of physical parameter space.

Be careful: high uncertainty does not automatically imply high information value.

⸻

PART 7 — QUESTIONS TO ASK VIVEK

Avoid repeating questions asked to Bing and Ramesh.

Vivek’s engineering background creates an opportunity to ask about the practical infrastructure behind Siemens Physical AI.

Question 1 — Research to Production

“Given your experience building large-scale ML systems, what do you think is the biggest difference between developing a strong research model and turning it into a reliable industrial ML system?”

Question 2 — Architecture

“How is the team thinking about the division between large foundation models running centrally and smaller specialized models deployed closer to industrial equipment?”

Question 3 — Data Infrastructure

“With data coming from many different industrial systems, is the larger engineering challenge standardizing the data and metadata, or building models that can handle the heterogeneity directly?”

Question 4 — Collaboration

“How closely do applied scientists work with the infrastructure and product engineering teams when taking a research idea toward deployment?”

Question 5 — Technical Tradeoffs

“Are there particular constraints in industrial environments—latency, connectivity, reliability, or hardware—that have forced the team to make modeling choices different from what you’d choose in a research setting?”

My preference: Questions 2, 3, and 5.

⸻

PART 8 — COMMON MISTAKES FROM MY PREVIOUS MOCKS

These are specific lessons from our earlier preparation.

Mistake 1 — Not defining the prediction unit

In a previous manufacturing scenario, I initially proposed sliding windows when the natural prediction unit was a manufactured component.

Correction: First identify what receives a prediction: machine, component, event, time window, or trajectory.

Mistake 2 — Confusing alert capacity with precision

Suppose:

* 10,000 components/day.
* 2% defective = 200 defects.
* 600 alerts/day allowed.

Even with perfect recall, precision at 600 alerts is at most:

200 / 600 = 33.3%.

Correction: Always compute the base rate and alert-budget constraints before choosing evaluation metrics.

Mistake 3 — Vague feature engineering

Saying “I’ll extract statistical features” is insufficient.

Correction: Name features tied to physical mechanisms.

Examples:

* Temperature slope.
* Vibration spectral energy.
* Pressure oscillation amplitude.
* Change from machine-specific baseline.
* Cross-sensor lag correlation.

Mistake 4 — Incomplete cost analysis

Do not simply say false negatives are more expensive.

Quantify expected costs and explain how thresholds follow from them.

Mistake 5 — Jumping into architecture too early

Spend the first few minutes clarifying the objective and constraints.

A well-chosen XGBoost baseline is often better than an unjustified Transformer.

⸻

PART 9 — FINAL 3-MINUTE REVIEW

The opening

“Before selecting an architecture, I’d like to clarify the prediction target, operational decision, data characteristics, and serving constraints.”

The design sequence

Objective
→ Scale
→ Data
→ Baseline
→ Model
→ Evaluation
→ Serving
→ Monitoring
→ Failure modes

The five things I must not forget

1. Prediction unit: What exactly receives a prediction?
2. Data leakage: Are train and test genuinely independent?
3. Business metric: Does evaluation reflect operational value?
4. Serving scale: Can the architecture meet latency and cost constraints?
5. Failure behavior: What happens when data or model services fail?

Strong principal-level signals

* Quantify assumptions.
* Compare alternatives.
* Explain tradeoffs.
* Connect modeling choices to operational constraints.
* Design for reliability.
* Discuss how to validate and iterate.
* Recognize where physics and domain knowledge matter.
* Prioritize the simplest solution that meets requirements.

If the interviewer challenges my design

Do not defend the original choice reflexively.

Respond:

“That’s a good constraint. Given that, I’d revisit the tradeoff between X and Y. The deciding factor would be…”

Then explain what changes and why.

If I don’t know an implementation detail

Explain the desired system property, propose a reasonable approach, and state how I would validate it.

Avoid inventing experience with technologies I haven’t used.

⸻

FINAL REMINDER

This is a Principal Applied Scientist interview, not a distributed-systems trivia contest.

My strongest advantage is the ability to combine:

* Scientific understanding of sequential data.
* Generative modeling and diffusion.
* Dynamical systems.
* Research methodology.
* Experimental design.
* Practical ML implementation.

The goal is to show that I can translate those strengths into a reliable, scalable ML system.

The single most important sentence to remember:

“I would start with the operational objective and constraints, establish a strong baseline, and only introduce additional modeling or infrastructure complexity when the evidence justifies it.”
