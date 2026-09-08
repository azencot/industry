"""6. XGBoost classifier on engineered temporal features — PROBLEM.

Episodes of variable-length sensor traces. Classify each episode into:

    0 resting | 1 walking | 2 running | 3 cycling

Each episode:

    {
      "accel": [[ax, ay, az], ...],   # 3-axis, variable T
      "hr": [..],
      "timestamps": [...],
      "label": int,
    }

This is NOT forecasting. XGBoost does not consume [T, C]. The work is a
fixed-size feature vector from a variable-length series.

Implement `extract_features(episode) -> 1D np.ndarray`.

Feature design (keep this order so tests can check length):

Accelerometer, per axis: mean, std, min, max, median          # 3 * 5 = 15
Magnitude = sqrt(ax^2+ay^2+az^2): mean, std, max              # 3
Temporal: mean |diff| of magnitude, std of first differences  # 2
HR: mean, std, min, max, median                               # 5
HR slope vs time (ordinary least squares, timestamps aligned) # 1
Metadata: duration, n_accel, n_hr                             # 3
                                                          total 29

Empty / short series: fill the corresponding block with 0.0 so the vector
length is always 29.

Then (solution file): stack X, y; split by **participant** if episodes
share a person; fit XGBClassifier multiclass.

Assumptions:
- Independent episodes at train time only if the split says so.
- Missing channel != measured zero. (Follow-up: NaN + availability flag.)
- If XGBoost matches the deep model, that is evidence, not a failure of DL.

Follow-ups (10 in the solution file): XGBoost vs Transformer; lost temporal
structure; periodic features; missing channels; leakage; fair comparison;
multimodal concat; missing-modality indicators; when order matters; a
bakeoff of stats / spectral / encoder / pretrained.
"""

from __future__ import annotations

import numpy as np


def _stats5(x):
    if len(x) == 0:
        return [0.0, 0.0, 0.0, 0.0, 0.0]
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
    ts = np.asarray(episode["timestamps"], dtype=float)
    feat = []

    if accel.ndim == 1:
        accel = accel.reshape(-1, 1)

    if len(accel) == 0:
        feat.extend([0.0] * 20)  # 15 axis + 3 mag + 2 diffs
    else:
        for c in range(3):
            col = accel[:, c] if c < accel.shape[1] else []
            feat.extend(_stats5(col))
        mag = np.sqrt((accel ** 2).sum(axis=1))
        feat.extend([float(np.mean(mag)), float(np.std(mag)), float(np.max(mag))])
        if len(mag) > 1:
            d = np.diff(mag)
            feat.extend([float(np.mean(np.abs(d))), float(np.std(d))])
        else:
            feat.extend([0.0, 0.0])

    feat.extend(_stats5(hr))

    if len(hr) >= 2 and len(ts) == len(hr):
        t = ts - ts[0]
        t_c = t - np.mean(t)
        den = float(np.sum(t_c * t_c))
        slope = float(np.sum(t_c * (hr - np.mean(hr))) / den) if den > 0 else 0.0
    else:
        slope = 0.0
    feat.append(slope)

    duration = float(ts[-1] - ts[0]) if len(ts) >= 2 else 0.0
    feat.extend([duration, float(len(accel)), float(len(hr))])
    return np.asarray(feat, dtype=float)


if __name__ == "__main__":
    ep = {
        "accel": [[0.1, 0.2, 9.7], [0.4, 0.1, 9.5], [0.2, 0.0, 9.8]],
        "hr": [72.0, 74.0, 76.0],
        "timestamps": [0.0, 1.0, 2.0],
        "label": 0,
    }
    feat = extract_features(ep)
    assert feat.shape == (29,), feat.shape
    assert feat.dtype == np.float64 or feat.dtype == np.float32

    empty = {"accel": [], "hr": [], "timestamps": [], "label": 1}
    z = extract_features(empty)
    assert z.shape == (29,), z.shape
    assert np.all(z == 0.0), z
    print("06_xgboost_features: PASS")
