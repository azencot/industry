"""Tuesday shape drills — SOLUTION."""

import torch


def split_heads(x, n_heads):
    b, t, d = x.shape
    if d % n_heads != 0:
        raise ValueError("D must divide n_heads")
    dh = d // n_heads
    return x.reshape(b, t, n_heads, dh).permute(0, 2, 1, 3).contiguous()


def merge_heads(x):
    b, h, t, dh = x.shape
    return x.permute(0, 2, 1, 3).reshape(b, t, h * dh)


def pairwise_dot(x, y):
    return x @ y.transpose(-2, -1)


def flatten_for_ce(logits, targets):
    b, t, c = logits.shape
    return logits.reshape(b * t, c), targets.reshape(b * t).long()


if __name__ == "__main__":
    x = torch.randn(2, 3, 8)
    h = split_heads(x, 4)
    assert h.shape == (2, 4, 3, 2)
    assert torch.allclose(merge_heads(h), x)
    a = torch.randn(2, 3, 4)
    b = torch.randn(2, 5, 4)
    dots = pairwise_dot(a, b)
    assert dots.shape == (2, 3, 5)
    assert torch.allclose(dots[0, 1, 2], a[0, 1] @ b[0, 2])
    logits = torch.randn(2, 3, 5)
    targets = torch.randint(0, 5, (2, 3))
    flat_logits, flat_targets = flatten_for_ce(logits, targets)
    assert flat_logits.shape == (6, 5) and flat_targets.shape == (6,)
    assert flat_targets.dtype == torch.long
    print("tue_shapes_solution: ok")
