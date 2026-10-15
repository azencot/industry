"""13. Dataset — SOLUTION.

Dataset does not batch. DataLoader stacks __getitem__ results, or calls
collate_fn when the items cannot stack (variable length).
""",

import torch
from torch.utils.data import DataLoader, Dataset


class TensorPairs(Dataset):
    def __init__(self, xs, ys):
        if len(xs) != len(ys):
            raise ValueError("xs and ys must have the same length")
        self.xs = xs
        self.ys = ys

    def __len__(self):
        return len(self.xs)

    def __getitem__(self, index):
        return self.xs[index], self.ys[index]


if __name__ == "__main__":
    xs = torch.randn(6, 3)
    ys = torch.randn(6, 1)
    data = TensorPairs(xs, ys)
    assert len(data) == 6
    x0, y0 = data[0]
    assert torch.equal(x0, xs[0]) and torch.equal(y0, ys[0])
    loader = DataLoader(data, batch_size=4, shuffle=False)
    xb, yb = next(iter(loader))
    assert xb.shape == (4, 3) and yb.shape == (4, 1)
    print("13_dataset_solution: ok")
