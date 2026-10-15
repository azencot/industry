"""14. Sliding-window time series — SOLUTION.

Window i uses times [i, i+L) as input and [i+L, i+L+H) as target.
The last legal i is T - L - H, so the count is T - L - H + 1.
""",

import torch
from torch.utils.data import Dataset


class SlidingWindowTS(Dataset):
    def __init__(self, x, context, horizon):
        if context < 1 or horizon < 1:
            raise ValueError("context and horizon must be positive")
        self.x = x
        self.context = context
        self.horizon = horizon

    def __len__(self):
        return max(0, self.x.shape[0] - self.context - self.horizon + 1)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError(index)
        start = index
        mid = index + self.context
        end = mid + self.horizon
        return self.x[start:mid], self.x[mid:end]


if __name__ == "__main__":
    x = torch.arange(6, dtype=torch.float32).unsqueeze(1)  # [6, 1]
    data = SlidingWindowTS(x, context=3, horizon=2)
    assert len(data) == 6 - 3 - 2 + 1
    inp, tgt = data[0]
    assert torch.equal(inp.view(-1), torch.tensor([0.0, 1.0, 2.0]))
    assert torch.equal(tgt.view(-1), torch.tensor([3.0, 4.0]))
    inp, tgt = data[len(data) - 1]
    assert torch.equal(inp.view(-1), torch.tensor([1.0, 2.0, 3.0]))
    assert torch.equal(tgt.view(-1), torch.tensor([4.0, 5.0]))
    assert len(SlidingWindowTS(x, context=5, horizon=2)) == 0
    print("14_sliding_window_solution: ok")
