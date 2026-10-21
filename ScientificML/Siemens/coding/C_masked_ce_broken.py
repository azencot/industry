"""C. Masked cross-entropy — START HERE. This file is wrong on purpose.

No solution file. Run it. Say the bug before you edit.
Then make both functions match the contract.

logits [B, T, C], targets [B, T] long, valid_mask [B, T] bool, True = valid.
Return a scalar mean over valid positions only.

masked_ce_ignore: flatten to [B*T, C] and [B*T], use ignore_index.
    You choose how a bool mask becomes that index. Pad targets must not
    be a real class.

masked_ce_unreduced: reduction="none", then the mask.
    Divide by the number of valid positions.

Tests:
- editing a padded logit does not change the loss
- editing a padded target does not change the loss
- when the mask is all True, the loss matches F.cross_entropy on the
  flattened tensors
- padded logit positions have zero gradient
- a tiny linear model can drive the loss down
- an all-False mask does not divide by zero
"""

import torch
import torch.nn.functional as F


def masked_ce_ignore(logits, targets, valid_mask, ignore_index=-100):
    C = logits.shape[-1]
    logits_r = logits.reshape(-1, C)
    targets_r = targets.reshape(-1)

    targets_r = targets_r.masked_fill(~valid_mask.reshape(-1), ignore_index)

    return F.cross_entropy(logits_r, targets_r)


def masked_ce_unreduced(logits, targets, valid_mask):
    C = logits.shape[-1]
    loss = F.cross_entropy(logits.reshape(-1, C), targets.reshape(-1), reduction='none')           # [B*T, C], [B*T] -> [B*T, C] ??

    valid_count = torch.sum(valid_mask)
    if valid_count == 0:
        return torch.zeros(()).to(logits.device)

    return torch.sum(loss[valid_mask.reshape(-1)]) / valid_count
