"""Prompt prefill and one-token KV-cache decode.

45-minute drill. Implement prefill and decode_one below. Write and run your own checks.

Prefill
    q, k, v: float tensors of shape [B, H, P, D]
    returns: output [B, H, P, D], and a cache of K and V at length P

Decode one new token
    q, k, v: float tensors of shape [B, H, 1, D]
    cache: K and V at length T, each [B, H, T, D]
    returns: output [B, H, 1, D], and a cache of K and V at length T + 1

B is batch, H is heads, D is head dimension. P is the prompt length.
T is the length already stored in the cache. q, k, and v for one call share
a length. Prefill and decode use the same H for Q, K, and V.

The new token attends to every cached key, including its own. A pure prefix
has no padding. Several decode steps must keep matching a full-prefix
recomputation: after t generated tokens, the decode output equals position
P + t - 1 of causal attention on the concatenated prompt and generated tokens.

Constraints:
- PyTorch tensor ops, plus causal_attention from this folder for the prompt
  block and for the full-prefix reference.
- decode_one reads past K and V from the cache. It does not run attention
  over past queries, and it does not call causal attention on the concatenated
  full sequence.
- Do not modify the q, k, v tensors passed into a call.
- Finite float32 inputs with P >= 1 and D >= 1 must produce a finite output.
- State what the cache stores per layer and how its size scales. This file is
  one layer and one head count.
"""

from __future__ import annotations

import math
import torch


def prefill(
    q: torch.Tensor, k: torch.Tensor, v: torch.Tensor
) -> tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
    # q, k, v in [B, H, P, D]
    _, _, P, D = q.shape

    qkt = q @ k.transpose(-2, -1) / math.sqrt(D)

    mask = torch.triu(torch.ones(P, P, dtype=bool, device=q.device), diagonal=1)
    scores = qkt.masked_fill(mask[None, None, :, :], float("-inf"))

    scores = torch.softmax(scores, dim=-1)

    return (scores @ v, (k, v))



def decode_one(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    cache: tuple[torch.Tensor, torch.Tensor],
) -> tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
    # q, k, v in [B, H, 1, D]
    # cache = (K, V) in [B, H, T, D]
    _, _, P, D = q.shape

    K, V = cache
    ka = torch.concatenate((K, k), axis=2)          # [B, H, T, D] & [B, H, 1, D] -> [B, H, T+1, D]

    qkat = q @ ka.transpose(-2, -1) / math.sqrt(D)  # [B, H, 1, D] @ [B, H, D, T+1] -> [B, H, 1, T+1]

    scores = torch.softmax(qkat, dim=-1)            # [B, H, 1, T+1]

    va = torch.concatenate((V, v), axis=2)          # [B, H, T, D] & [B, H, 1, D] -> [B, H, T+1, D]
    return (scores @ va, (ka, va))                  # [B, H, 1, T+1] @ [B, H, T+1, D] -> [B, H, 1, D]


if __name__ == "__main__":
    # Replace this runner with your tests after the functions are implemented.
    raise SystemExit("prefill and decode_one are not implemented.")
