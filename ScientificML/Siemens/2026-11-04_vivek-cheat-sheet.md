# Vivek Govindan — Siemens ML System Design Interview Cheat Sheet
**Interview:** November 5, 2026 | Principal Applied Scientist, Physical AI
**Expected emphasis:** End-to-end ML system design, scientific/industrial data, scaling and reliability. Danielle identified Vivek as the system-design interviewer, possibly including PDE data generation. His public profile suggests an engineering/systems perspective; exact questions are unknown.

## 1. Natural introduction (25–35 seconds)
I'm an Associate Professor of Computer Science at Ben-Gurion University. My research focuses on time series, generative modeling, and dynamical systems. I've also been working hands-on with multimodal models, from data preparation and training to evaluation. I'm now exploring industry research roles, and I'm particularly interested in how scientific ML systems can generalize across real industrial settings.

## 2. Universal whiteboard framework — use in this order
**Objective and action → prediction unit and horizon → data/labels → scale/latency → baseline/model → evaluation → serving → monitoring/failures.**

Open with: "Before picking a model, can I clarify what decision the prediction supports, what data is available at decision time, and the operational constraints?"

Ask: What constitutes success? False-positive/false-negative costs? Who acts on outputs? Prediction frequency and lead time? Number of plants/machines/sensors? Sampling rate, missingness, labels and delays? Edge vs cloud? Hard safety constraints? What changes at new plants/meshes/operating regimes?

Principal-level signals: **quantify** the scale; name the simplest baseline; distinguish offline metrics from operational utility; explain failure modes and tradeoffs; propose phased rollout and rollback.

## 3. Scenario A — Manufacturing defect prediction (previous mock)
**Given:** 20 lines × 500 components/day = **10,000 components/day**; 2% defective = **200 defects/day**; 30 inspections/line/day = **600 alerts/day**. Four stages, 30 min total; predict after stage 2 at minute 15.

- **Prediction unit:** ONE component; features use only information available by minute 15; target = final inspection defect label.
- **Features:** multiscale per-sensor mean/std/extrema/slope, threshold excursions, cross-sensor relations, operating settings, material, machine/line ID, missingness. Preserve transient events rather than only global averages.
- **Models:** rules and logistic regression/XGBoost first; temporal neural model only if justified by performance/scale.
- **Validation:** chronological holdout; group by component; additional unseen-line/plant tests. Never split overlapping windows randomly.
- **Metrics:** PR-AUC, event-level recall, calibration, **precision/recall at 30 alerts per line/day**, cost saved. At 600 alerts, even perfect capture of all 200 defects gives precision **200/600 = 33.3%** (if all slots used).
- **Policy:** rank by calibrated expected benefit, respecting each line's capacity; human review initially.
- **Deployment:** shadow → canary → assisted rollout; monitor input missingness, per-line drift, alerts, calibration, inspection outcomes, inference latency; rollback.
- **Past mock pitfall:** Do not treat sliding 5-minute windows as separate labeled components when the decision is once per component.

## 4. Scenario B — Predictive maintenance
**Prompt:** 1,000 machines, 50 sensors/machine at 1 Hz, 2 years history; score every 5 min; need **at least 24 h warning**.

- **Clarify label:** If *minimum* 24 h warning is required, target failure in an actionable future interval such as **[t+24 h, t+7 d]**; don't accidentally define it as failure *within* the next 24 h. Define maintenance interventions and censoring.
- **Scale:** 1,000×50×1 = **50,000 measurements/s**; float32 payload ~**200 KB/s**, **17.3 GB/day** before metadata/storage overhead. Scoring: 1,000/300 ≈ **3.3 predictions/s**. Ingestion can dominate inference.
- **Pipeline:** sensors → gateway/buffer → durable stream → validated time-series store + object store → rolling features → inference → alert service. Partition by machine; use event time, watermarks, idempotent processing and late-event handling.
- **Model:** engineering thresholds → XGBoost on rolling stats/spectral energy/slopes/load-adjusted baselines → TCN/Transformer/SSM if incremental value.
- **Eval:** temporal, machine and plant holdouts; PR-AUC, **failure-event recall at minimum warning lead time**, false alerts/machine/month, precision@maintenance capacity, calibration, realized maintenance utility.
- **Bias:** preventive maintenance changes observed failures; consider intervention bias, censored outcomes and survival modeling.
- **Failure mode:** edge buffering, missingness indicators, safe deterministic fallback, human approval for physical actions.

## 5. Scenario C — Industrial time-series foundation model (strong Siemens relevance)
**Prompt:** Many plants, heterogeneous sensors and rates, scarce real data, synthetic simulations; zero/few-shot forecasting or anomaly detection.

1. Clarify tasks, conditioning information, target-domain adaptation allowance, and real-world operating regimes.
2. Data ingestion: preserve sensor **units/semantics**, timestamps, controls, machine metadata, masks; resample carefully (anti-aliasing) or use irregular-time encoding. Never assume channel 3 means the same thing on all machines.
3. Architecture: sensor/metadata embeddings → temporal backbone (patch Transformer, TCN, SSM) → cross-sensor module → task head; compare to strong univariate and XGBoost baselines.
4. Objectives: forecasting, masked reconstruction, generative modeling; ablate rather than assume multitask helps.
5. **Synthetic data:** physics simulators or generative models; train real-only vs synthetic-only vs combined, then evaluate on **untouched real-world** holdouts. Watch simulator-to-real gap and unrealistic artifacts.
6. Transfer tests: seen machine/future; unseen machine/same plant; unseen plant; new machine type; unseen operating regime; changed sampling frequency; missing sensors. Keep zero-shot target labels out of tuning.
7. Serving: large model offline or centralized; smaller distilled model at edge; benchmark throughput, P95 latency, memory, cost/machine, and fallback.

**Useful connection from Ramesh interview:** Ramesh said Siemens faces a **shortage of real data and uses many synthetic examples**. Ask how synthetic coverage and real-world transfer are measured, rather than assuming synthetic data automatically helps.

## 6. Scenario D — PDE solver surrogate and simulation-data generation
**Clarify:** PDE family; geometry/mesh; coefficients; initial/boundary conditions; forcing; outputs (field vs scalar vs rollout); accuracy and conservation requirements; unseen geometries/parameter regimes; solver cost.

**Pipeline:** sample parameter/geometry space → distributed trusted solver jobs → versioned mesh/BC/tolerance/seed/solver metadata → numerical QA (residuals, conservation, failed runs) → sharded dataset → model training → independent solver validation → inference service.

**Baselines:** reduced-order/POD or simple regression; candidate FNO/DeepONet for suitable function mappings, GNN for meshes, physics-informed approach when constraints justify it. Discretization invariance is not automatic.

**Metrics:** relative field L2 error, physically relevant quantity-of-interest error, conservation/BC violations, long-horizon stability, worst-case and OOD error, wall-clock speedup **including preprocessing**. Hold out geometries/parameter regimes, not just random solver snapshots.

**Scaling:** parallel job queue; idempotent retries, checkpointing, manifests, deduplication, storage cost, adaptive sampling/active learning. Compare marginal cost of new solver data vs training vs serving.

**Safety:** uncertainty/applicability checks and fallback to numerical solver outside validated regimes.

## 7. Engineering follow-ups — 30-second answers
**Training-serving skew?** Shared/versioned feature transformations, identical timestamp cutoffs, parity tests, schema checks.

**Duplicates/late streaming events?** At-least-once delivery assumption, idempotent writes, stable event IDs, event-time windows/watermarks, bounded late-arrival policy.

**Sensor missing?** Detect, mask, distinguish outage from real zero, use justified imputation or abstain/fallback.

**Outage?** Last-known-good version, buffering, bounded retries/backoff, circuit breaker, deterministic safety fallback; do not let ML availability determine machine safety.

**New model rollout?** Offline gate → shadow → canary → staged rollout; monitor latency/alerts/quality; version and rollback.

**Drift?** Separate pipeline errors, sensor recalibration, covariate shift, label/concept drift; assess impact before retraining.

**CPU vs GPU?** Benchmark actual batch size, throughput, P95 latency, utilization, cost and edge constraints.

**Inference 10× faster?** Profile first; optimize data path/batching, then quantization/distillation/patching/caching/kernels; compare at matched quality.

**Reproducibility?** Version data snapshots, splits, feature code, configs, seeds, environment, checkpoints and evaluation.

**Delayed labels?** Log prediction time and cohort; join outcomes when mature; don't treat pending labels as negatives.

**Calibration?** Reliability diagrams/Brier score; good AUROC does not imply reliable probabilities.

**Cost decision rule?** Under a simplified intervention model, intervene if **p·C_FN > (1-p)·C_FP**, subject to action capacity and intervention efficacy.

## 8. Alternative scenario — Streaming audio diarization (secondary)
If he asks outside industrial ML: audio → VAD → ASR → speaker embeddings/diarization → transcript assembly. Clarify streaming latency, speaker count, overlapping speech, privacy. Metrics: WER, diarization error rate, speaker confusion, latency/cost. Handle incremental corrections, noisy audio, state, backpressure and retention. This is a secondary practice case, not a forecast of his questions.

## 9. Agent harness (only if asked)
Task/permissions → model-driven orchestrator → validated tool call → execution → observation/state → next step. Include least privilege, timeouts, bounded retries, idempotency, checkpoints, approval for consequential actions, stopping rules. Evaluate task success, tool correctness, evidence grounding, safety, latency and cost. Start with one agent.

## 10. Questions for Vivek — choose 2
1. "How do you decide which components of an industrial ML system should run at the edge versus centrally, especially when models become larger?"
2. "When sensor data comes from very different equipment, do you see metadata standardization or learning across heterogeneity as the harder engineering challenge?"
3. "What technical constraints have most changed your architecture decisions when moving ML from prototypes to industrial deployments?"
4. "How do you validate synthetic-data pipelines and learned surrogates against real measurements or trusted solvers?"
5. "How closely do applied scientists own the data and deployment architecture versus collaborating with dedicated infrastructure teams?"

## 11. Last-minute reminders
- Start with **the decision and prediction unit**, not the model.
- Compute basic volume, throughput, latency, prevalence and alert capacity.
- One example per component if one component-level decision; avoid overlapping-window leakage.
- Separate **ranking, calibration, and operational utility**.
- Compare **real-only / synthetic-only / mixed** on untouched real-world tests.
- State physical assumptions, units, geometry, solver tolerance, and OOD conditions.
- Explain fallback, monitoring, versioning, and safe rollout.
- Be candid about limited production experience; emphasize hands-on research engineering and rigorous validation.

**One-line anchor:** "I'd first define the operational decision and constraints, establish a simple baseline, and add model or infrastructure complexity only when we can demonstrate its value."
