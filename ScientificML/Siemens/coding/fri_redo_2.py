"""Friday redo 2. One training step, next-token cross-entropy. 20 minutes.

Do not open F_minigpt.py or L_wont_learn.py.

    token_ids: [B, T] long
    model(token_ids) -> logits [B, T, V]
    opt: an optimizer already built on the model's parameters

Position t predicts token t+1. Mean cross-entropy over those pairs.
Pass raw logits in. Do not softmax first.

If T < 2, return a 0-dim zero on the logits' device and do not step.

Otherwise run one update that actually changes a parameter, and return
the loss as a 0-dim tensor detached from the graph.

Checks:
- T == 1 returns 0 and leaves parameters unchanged
- after one step, some parameter moved
- the loss matches cross-entropy on the shifted pairs
"""

import torch
import torch.nn as nn


def train_step(model, token_ids, opt):
    if token_ids.shape[-1] < 2:
        return torch.zeros(()).to(token_ids.device)
        
    model.train()

    opt.zero_grad()
    logits = model(token_ids)           # [B, T] -> [B, T, V]

    V = logits.shape[-1]
    loss = nn.CrossEntropyLoss()(logits[:, :-1].reshape((-1, V)), token_ids[:, 1:].flatten())

    loss.backward()
    opt.step()

    return loss.detach()
