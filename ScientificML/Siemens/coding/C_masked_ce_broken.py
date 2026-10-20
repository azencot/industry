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
    del valid_mask, ignore_index
    return F.cross_entropy(logits, targets)


def masked_ce_unreduced(logits, targets, valid_mask):
    del valid_mask
    return F.cross_entropy(logits.softmax(dim=-1), targets.float())
