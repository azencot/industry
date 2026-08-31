"""6. XGBoost on engineered temporal features — SOLUTION.

Pipeline: variable-length episode -> 29-d vector -> boosted trees.

XGBoost never sees [T, C]. It sees the statistics you chose to expose.
That choice *is* the model.

If this baseline matches a deep sequence model on the same split, do
not conclude "the deep model is better because it is more modern."
Ask what the deep model is buying: low-label transfer, multimodal
reuse, hard temporal slices, waveform morphology, personalization.

Split: if episodes share a participant / device, split by participant
first. Random episode split leaks.

Follow-ups:
1. Why XGBoost not a Transformer? Modest labels, known useful
   summaries, cheaper, debuggable. Deep model must beat it.
2. Lost: precise order, event timing, waveform shape, long-range
   interaction — unless you encoded them (lags, spectra, DTW, ...).
3. Periodic: hour/dow + sin/cos, or band energy.
4. Missing channels: NaN (trees route around it) + an explicit
   availability bit. Zero is a real measurement.
5. Leakage: participant or temporal split FIRST, then features.
   Do not cut overlapping windows and shuffle them into train/test.
6. Fair bakeoff: same split, labels, available signals, prediction
   time, metric. Then quality / robustness / latency / cost / data
   efficiency.
7. Multimodal XGBoost: concat modality blocks (accel, HR, sleep,
   metadata). Classical early fusion.
8. Missing modality: availability flags; leave features NaN.
9. Order matters: add lags / local segments / spectral features
   before jumping to a large Transformer.
10. Experiment: (A) simple stats (B) stats+spectral (C) native TS
    encoder (D) pretrained multimodal — where does each win?

Feature importance (gain) is not causal. Correlated features split
credit. Prefer permutation importance or SHAP if you must explain.
"""

from __future__ import annotations

import numpy as np

N_FEATURES = 29  # 15 axis + 3 mag + 2 diff + 5 hr + 1 slope + 3 meta


def safe_stats(x):
    x = np.asarray(x, dtype=float)
    if len(x) == 0:
        return [0.0] * 5
    return [
        float(np.mean(x)),
        float(np.std(x)),
        float(np.min(x)),
        float(np.max(x)),
        float(np.median(x)),
    ]


def extract_features(episode):
    accel = np.asarray(episode["accel"], dtype=float)
    hr = np.asarray(episode["hr"], dtype=float)
    timestamps = np.asarray(episode["timestamps"], dtype=float)
    features = []

    if accel.ndim == 1:
        accel = accel.reshape(-1, 1)

    if len(accel) > 0:
        n_axes = accel.shape[1]
        for c in range(n_axes):
            features.extend(safe_stats(accel[:, c]))
        # Pad / trim to 3 axes so the vector stays 29-d in tests.
        if n_axes < 3:
            features.extend([0.0] * 5 * (3 - n_axes))
        elif n_axes > 3:
            features = features[:15]

        magnitude = np.linalg.norm(accel, axis=1)
        features.extend([
            float(np.mean(magnitude)),
            float(np.std(magnitude)),
            float(np.max(magnitude)),
        ])
        if len(magnitude) > 1:
            diff = np.diff(magnitude)
            features.extend([
                float(np.mean(np.abs(diff))),
                float(np.std(diff)),
            ])
        else:
            features.extend([0.0, 0.0])
    else:
        features.extend([0.0] * 15)
        features.extend([0.0] * 5)

    features.extend(safe_stats(hr))

    if len(hr) >= 2 and len(timestamps) == len(hr):
        t = timestamps - timestamps[0]
        t_c = t - np.mean(t)
        denom = float(np.sum(t_c ** 2))
        if denom > 0:
            slope = float(np.sum(t_c * (hr - np.mean(hr))) / denom)
        else:
            slope = 0.0
    else:
        slope = 0.0
    features.append(slope)

    duration = float(timestamps[-1] - timestamps[0]) if len(timestamps) >= 2 else 0.0
    features.extend([duration, float(len(accel)), float(len(hr))])
    return np.asarray(features, dtype=float)


def _synthetic_episodes(n_per_class=6, seed=0):
    """Tiny labeled set so the fit path can run without real sensors."""
    rng = np.random.default_rng(seed)
    episodes = []
    # Rest / walk / run / cycle: increasing mag + HR.
    specs = [
        (0, 0.2, 70.0),
        (1, 1.5, 95.0),
        (2, 4.0, 140.0),
        (3, 2.5, 120.0),
    ]
    for label, mag, hr_mu in specs:
        for i in range(n_per_class):
            t = np.arange(20, dtype=float)
            ax = rng.normal(0.0, mag, size=len(t))
            ay = rng.normal(0.0, mag, size=len(t))
            az = rng.normal(9.8, 0.2, size=len(t))
            hr = rng.normal(hr_mu, 3.0, size=len(t))
            episodes.append({
                "accel": np.stack([ax, ay, az], axis=1).tolist(),
                "hr": hr.tolist(),
                "timestamps": t.tolist(),
                "label": label,
                "participant": f"p{i % 3}",
            })
    return episodes


def participant_split(episodes, test_participants):
    train, test = [], []
    test_participants = set(test_participants)
    for ep in episodes:
        (test if ep["participant"] in test_participants else train).append(ep)
    return train, test


if __name__ == "__main__":
    ep = {
        "accel": [[0.1, 0.2, 9.7], [0.4, 0.1, 9.5], [0.2, 0.0, 9.8]],
        "hr": [72.0, 74.0, 76.0],
        "timestamps": [0.0, 1.0, 2.0],
        "label": 0,
    }
    feat = extract_features(ep)
    assert feat.shape == (N_FEATURES,), feat.shape

    empty = {"accel": [], "hr": [], "timestamps": [], "label": 1}
    z = extract_features(empty)
    assert z.shape == (N_FEATURES,)
    assert np.all(z == 0.0)

    # OLS slope of hr = 72 + 2*t is 2.
    assert abs(feat[-4] - 2.0) < 1e-6, feat[-4]

    episodes = _synthetic_episodes()
    train_eps, test_eps = participant_split(episodes, test_participants={"p0"})
    X_train = np.stack([extract_features(e) for e in train_eps])
    y_train = np.array([e["label"] for e in train_eps])
    X_test = np.stack([extract_features(e) for e in test_eps])
    y_test = np.array([e["label"] for e in test_eps])
    assert X_train.shape[1] == N_FEATURES
    assert len(set(e["participant"] for e in train_eps) & {"p0"}) == 0

    try:
        from xgboost import XGBClassifier
    except ImportError:
        print("06_xgboost_features_solution (features): PASS")
        print("06_xgboost_features_solution (xgb fit): SKIP")
    else:
        model = XGBClassifier(
            objective="multi:softprob",
            num_class=4,
            n_estimators=40,
            max_depth=3,
            learning_rate=0.2,
            subsample=0.9,
            colsample_bytree=0.9,
            eval_metric="mlogloss",
        )
        model.fit(X_train, y_train)
        pred = model.predict_proba(X_test).argmax(axis=1)
        acc = float((pred == y_test).mean())
        assert acc >= 0.5, acc  # synthetic classes are well separated
        print(f"06_xgboost_features_solution: PASS (acc={acc:.2f})")
