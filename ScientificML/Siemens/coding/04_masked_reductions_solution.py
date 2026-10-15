"""04. Masked reductions — SOLUTION.

m = mask[..., None] so it lines up with D. Sum over time.
Mean divides by the count of valid steps, clamped at 1 so an all-pad row
contributes 0 instead of NaN. MSE divides by the count of valid elements.
""",

import torch


def _as_float_mask(mask, x):
    return mask.unsqueeze(-1).to(dtype=x.dtype)


def masked_sum(x, mask):
    return (x * _as_float_mask(mask, x)).sum(dim=1)


def masked_mean(x, mask):
    m = _as_float_mask(mask, x)
    denom = m.sum(dim=1).clamp_min(1.0)
    return (x * m).sum(dim=1) / denom


def masked_mse(pred, target, mask):
    err = (pred - target) ** 2
    m = _as_float_mask(mask, err)
    denom = m.sum() * err.shape[-1]
    denom = denom.clamp_min(1.0)
    return (err * m).sum() / denom


if __name__ == "__main__":
    x = torch.tensor([[[1.0], [3.0], [100.0]], [[2.0], [50.0], [70.0]]])
    mask = torch.tensor([[True, True, False], [True, False, False]])
    assert torch.allclose(masked_sum(x, mask), torch.tensor([[4.0], [2.0]]))
    assert torch.allclose(masked_mean(x, mask), torch.tensor([[2.0], [2.0]]))
    empty = torch.zeros(1, 2, dtype=torch.bool)
    assert masked_mean(torch.ones(1, 2, 1), empty).item() == 0.0
    pred = torch.zeros(1, 2, 1)
    target = torch.tensor([[[2.0], [9.0]]])
    m = torch.tensor([[True, False]])
    assert torch.allclose(masked_mse(pred, target, m), torch.tensor(4.0))
    print("04_masked_reductions_solution: ok")
