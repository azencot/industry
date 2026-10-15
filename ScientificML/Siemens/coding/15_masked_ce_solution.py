"""15. Masked cross-entropy — SOLUTION.

Flatten B and T, ask for an unreduced loss per position, then put the
mask back. Divide by the number of valid positions.
""",

import torch
import torch.nn.functional as F


def masked_cross_entropy(logits, targets, mask):
    b, t, c = logits.shape
    per = F.cross_entropy(
        logits.reshape(b * t, c),
        targets.reshape(b * t),
        reduction="none",
    ).view(b, t)
    m = mask.to(dtype=per.dtype)
    return (per * m).sum() / m.sum().clamp_min(1.0)


if __name__ == "__main__":
    logits = torch.tensor([[[10.0, 0.0], [0.0, 10.0], [10.0, 0.0]]])
    targets = torch.tensor([[0, 1, 0]])
    mask = torch.tensor([[True, True, False]])
    loss = masked_cross_entropy(logits, targets, mask)
    assert loss.ndim == 0
    assert loss < 0.01
    # The pad position is a wrong class. It must not move the loss.
    bad_pad = logits.clone()
    bad_pad[0, 2] = torch.tensor([0.0, 10.0])
    assert torch.allclose(
        masked_cross_entropy(bad_pad, targets, mask),
        loss,
    )
    none = torch.zeros(1, 3, dtype=torch.bool)
    assert masked_cross_entropy(logits, targets, none).item() == 0.0
    print("15_masked_ce_solution: ok")
