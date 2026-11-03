# Vivek Govindan — hour 2

**Check the latest invitation before you rely on this hour.** The original slot was 5:00–6:00 AM Thailand (2:00–3:00 PM Pacific) and was being moved. He is the system-design hour: high-level, then how you would optimize it. PDE generation is possible. Do not say Danielle’s name.

## 45–60 seconds

I’m an Associate Professor of Computer Science at Ben-Gurion University, moving into industry research. I work on sequential and generative models: time series, diffusion, and Koopman dynamics. I also run the multimodal training and the eval myself. I take an open problem and turn it into a prediction time, a training row that matches that time, a baseline, and a measurement that can kill the approach. The part I want at Siemens is generalization across physical systems, with a budget.

## The order

Clarify. Name the decision and the prediction time. Data and labels using only what is known then. A simple baseline. Features. Offline eval. Shadow, then a person, then a wider rollout, with a rollback number. Monitor.

Ask: the decision, the horizon, what exists at inference, the two costs, whether the holdout is time or a new plant or a new geometry, and the latency, the hardware, and the intervention.

## A — Defects at minute 15

Twenty lines, 500 components a line, 10,000 a day, 2% defects, 200 defects a day. Thirty checks a line, 600 a day. One score at minute 15. Inspection at minute 30.

One training row per component. Sensors and metadata from minutes 0–15 only. The label is the minute-30 inspection. A five-minute slice is a feature, not another row. XGBoost on multiscale mean, spread, min, max, slope, threshold counts, stage 1 against stage 2, missingness, settings, material, line. Time split for the next week on the same lines. A held-out line or factory is a different number. Unweighted, then weighted. Calibrate. Precision and recall at 30 alerts per line per day. Rank by expected benefit and stop at 30 or at the first non-positive benefit. Shadow, then assisted, then controlled. Watch slices and the fact that a successful intervention changes the label you will see later.

If he asks the precision of catching every defect inside 600 checks: \(200/600 = 33\%\), and only if those checks sit on the lines that have the defects.

## B — A failure at least 24 hours out

Positive when the failure is in \([t+24\mathrm{h},\, t+7\mathrm{d}]\). Negative when nothing fails in seven days. The gap under 24 hours is too late. It is not another positive. Features end at \(t\). Same multiscale stats, plus load and missingness. Group a machine inside one split. Lead time, precision at the daily cap, calibration. Overlapping windows do not cross the cut.

Friday 3 PM failure: Wednesday 3 PM and Thursday 3 PM can be positive. Friday 9 AM is six hours out.

## C — PDE data, if he goes there

Which family, which geometry, which coefficients, which boundary and initial conditions. Field, a scalar, or a rollout. Accuracy, a conservation law, and the inference budget. Interpolation in parameters, or a new geometry.

Trusted solver, mesh, boundary conditions, tolerance, timestep, units, a failure flag, provenance. Split by regime and by geometry. The test set is not in the adaptive sampler. Baseline is the solver, then a reduced-order model, then a neural operator if the holdout says so. Parallel jobs, versioned solvers, seeds, manifests, residual and conservation checks, retries. A fast field that breaks a boundary condition loses to the solver. Fall back when the surrogate is uncertain.

A million trajectories at \(256\times 256\), four variables, 1,000 steps, FP32, is about 1 PB uncompressed. Two node-hours a run and 200,000 node-hours is 100,000 runs. Say the ledger before a second architecture.

## D — An agent harness, only if he asks

Task, tools, permissions, autonomy, and the success test. Model, tool call, schema check, execute, observe, update. Timeouts, bounded retries, idempotency, checkpoints, and a person on a consequential action. Score task success, tool validity, grounding, cost, and latency. Replay with a broken tool. One agent until a second one earns its place.

## If he presses

1. **Train versus serve.** The feature cutoff is the production prediction time. Version the preprocessing.
2. **Leakage.** One component or one machine in one split. No future in the features.
3. **2% positives.** PR-AUC, precision at the cap, calibration, costs. Try a weight. Do not assume it helps.
4. **Threshold.** Expected benefit and the cap. Say whether the cost is paid on every check or only on a false alarm. \(p C_{FN}-(1-p)C_{FP}\) is the second case.
5. **Why a tree.** Data-efficient, CPU, temporal features you can name. A sequence model has to beat that on the decision.
6. **A new factory.** Slice first. A time holdout and a factory holdout are different claims.
7. **Scale the solver farm.** Queue, versions, manifests, residual gates, retries. Profile before more GPUs.
8. **Monitor.** Drift, missingness, calibration, the operational number, cost, latency, and the rollback.

## Ask two, then stop

- Is the bottleneck data generation, training, transfer, or the path into the engineering workflow?
- What has to be true before a learned model sits next to a solver an engineer trusts?
- Do you transfer across physical systems, or go deep on one system?
- How much of the data and eval pipeline does the applied scientist own?

## Close

What end-to-end system would you want this hire to take first?
