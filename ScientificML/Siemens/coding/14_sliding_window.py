"""14. Sliding-window time series — PROBLEM.

Do not open 14_sliding_window_solution.py until this file runs.

x: float tensor [T, D]
context L, horizon H.

__len__ is the number of valid windows: T - L - H + 1.
If that is negative, there are 0 windows.

__getitem__(i) returns:
    inputs  x[i : i+L]           [L, D]
    target  x[i+L : i+L+H]       [H, D]

Watch the off-by-one. The last start index is T - L - H.
""",

from torch.utils.data import Dataset


class SlidingWindowTS(Dataset):
    def __init__(self, x, context, horizon):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError
