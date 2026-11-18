"""Causal scaled dot-product attention.

45-minute drill. Implement causal_attention below. Write and run your own checks.

q, k, v: float tensors of shape [B, H, T, D]
returns: float tensor of shape [B, H, T, D]

B is batch, H is heads, T is sequence length, D is head dimension.
q, k, and v share that shape. The output at query position i may use only
keys and values at positions 0..i inclusive. Scale the scores by 1/sqrt(D)
and softmax over the key axis. No output projection, dropout, RoPE, or bias.

Constraints:
- PyTorch tensor ops only. Do not call scaled_dot_product_attention
  or nn.MultiheadAttention.
- Do not modify q, k, or v.
- Batch and head dimensions are independent.
- Finite inputs with T >= 1 and D >= 1 must produce a finite output.
- Correct for float32. State your assumption for float16 and bfloat16.
"""

from __future__ import annotations

import math
import torch


def causal_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    # q, k, v in [B, H, T, D]
    B, H, T, D = q.shape
    qkt = q @ k.transpose(-2, -1) / math.sqrt(D)                        # [B, H, T, D] @ [B, H, D, T] -> [B, H, T, T]

    # causal mask
    mask = torch.triu(torch.ones(T, T, dtype=bool, device=q.device), diagonal=1)    # [T, T] -> [T, T]
    scores = qkt.masked_fill(mask[None, None, :, :], float("-inf"))     # [T, T] -> [1, 1, T, T] -> [B, H, T, T]

    scores = torch.softmax(scores, dim=-1)                             # [B, H, T, T] -> [B, H, T, T]

    return scores @ v                                                   # [B, H, T, T] @ [B, H, T, D] -> [B, H, T, D] 



if __name__ == "__main__":
    # Replace this runner with your tests after the function is implemented.
    raise SystemExit("causal_attention is not implemented.")
