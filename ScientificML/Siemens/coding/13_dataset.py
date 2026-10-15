"""13. Dataset — PROBLEM.

Do not open 13_dataset_solution.py until this file runs.

class TensorPairs(Dataset)

xs and ys are sequences of equal length (tensors or lists).
__len__ is the number of pairs.
__getitem__(i) returns (xs[i], ys[i]).

A DataLoader will call __getitem__ then your collate. This class does
not pad. It only serves one index.
""",

from torch.utils.data import Dataset


class TensorPairs(Dataset):
    def __init__(self, xs, ys):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError
