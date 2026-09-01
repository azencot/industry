"""6. XGBoost on engineered temporal features — SOLUTION (native API).

Same 29-d features and participant split as 06_xgboost_features_solution.py.
This file fits with xgboost.train + DMatrix, not sklearn's XGBClassifier.

Native vs sklearn wrapper (say this if they ask):

    XGBClassifier.fit(X, y)     convenience; numpy / pandas in, .predict out
    xgb.train(params, DMatrix)  the library's own loop; DMatrix owns labels,
                                missing-value routing, feature names, evals

Same trees. Different I/O. Map:

    sklearn              native
    n_estimators    ->   num_boost_round
    learning_rate   ->   eta
    eval_metric     ->   params["eval_metric"]
    .fit            ->   xgb.train
    .predict_proba  ->   bst.predict  (objective multi:softprob)

DMatrix missing=np.nan by default: trees route around NaN. Filling 0.0
for an empty channel (this file) collides with a true zero measurement.
Follow-up: leave missing as NaN and add an availability bit.

Feature importance (gain) is not causal. Prefer permutation / SHAP.
"""

from __future__ import annotations

import numpy as np

N_FEATURES = 29  # 15 axis + 3 mag + 2 diff + 5 hr + 1 slope + 3 meta
N_CLASSES = 4

FEATURE_NAMES = (
    [f"a{axis}_{stat}" for axis in "xyz" for stat in ("mean", "std", "min", "max", "median")]
    + ["mag_mean", "mag_std", "mag_max", "mag_mean_abs_diff", "mag_std_diff"]
    + ["hr_mean", "hr_std", "hr_min", "hr_max", "hr_median", "hr_slope"]
    + ["duration", "n_accel", "n_hr"]
)
assert len(FEATURE_NAMES) == N_FEATURES


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


def stack_xy(episodes):
    X = np.stack([extract_features(e) for e in episodes])
    y = np.array([e["label"] for e in episodes], dtype=np.int32)
    return X, y


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
    X_train, y_train = stack_xy(train_eps)
    X_test, y_test = stack_xy(test_eps)
    assert X_train.shape[1] == N_FEATURES
    assert len(set(e["participant"] for e in train_eps) & {"p0"}) == 0

    try:
        import xgboost as xgb
    except ImportError:
        print("06_xgboost_features_solution_native (features): PASS")
        print("06_xgboost_features_solution_native (xgb fit): SKIP")
    else:
        dtrain = xgb.DMatrix(
            X_train, label=y_train, feature_names=FEATURE_NAMES, missing=np.nan,
        )
        dtest = xgb.DMatrix(
            X_test, label=y_test, feature_names=FEATURE_NAMES, missing=np.nan,
        )
        params = {
            "objective": "multi:softprob",
            "num_class": N_CLASSES,
            "max_depth": 3,
            "eta": 0.2,
            "subsample": 0.9,
            "colsample_bytree": 0.9,
            "eval_metric": "mlogloss",
            "verbosity": 0,
        }
        booster = xgb.train(
            params,
            dtrain,
            num_boost_round=40,
            evals=[(dtrain, "train"), (dtest, "eval")],
            verbose_eval=False,
        )
        # multi:softprob -> (n_test, num_class). multi:softmax -> class ids.
        proba = booster.predict(dtest)
        assert proba.shape == (len(y_test), N_CLASSES), proba.shape
        pred = proba.argmax(axis=1)
        acc = float((pred == y_test).mean())
        assert acc >= 0.5, acc  # synthetic classes are well separated
        print(f"06_xgboost_features_solution_native: PASS (acc={acc:.2f})")
