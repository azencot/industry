"""Day 1 — causal multi-head attention + next-token CE.

Study object: every tensor shape. Screen is spoken; this is not CoderPad.

    x:        [B, T, C]
    q,k,v:    [B, H, T, d]     d = C / H
    scores:   [B, H, T, T]
    attn:     [B, H, T, T]
    y:        [B, T, C]
    logits:   [B, T, V]
    loss:     scalar  (predict token t+1 from position t)

Run:  python3 day1_attention.py
Then close the file and re-implement CausalSelfAttentionFromMemory.
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalSelfAttention(nn.Module):
    """nanoGPT-style: one Linear for QKV, causal mask, project back to C."""

    def __init__(self, n_embd: int, n_head: int, block_size: int, dropout: float = 0.0):
        super().__init__()
        assert n_embd % n_head == 0
        self.n_head = n_head
        self.n_embd = n_embd
        self.head_dim = n_embd // n_head
        self.c_attn = nn.Linear(n_embd, 3 * n_embd)
        self.c_proj = nn.Linear(n_embd, n_embd)
        self.attn_drop = nn.Dropout(dropout)
        self.resid_drop = nn.Dropout(dropout)
        # [1, 1, T, T] lower-triangular 1s — broadcast over B and H
        bias = torch.tril(torch.ones(block_size, block_size)).view(1, 1, block_size, block_size)
        self.register_buffer("bias", bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, C = x.shape
        # [B, T, 3C] → three [B, T, C]
        q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
        # [B, T, C] → [B, H, T, d]
        q = q.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        # [B, H, T, T]
        att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(self.head_dim))
        att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float("-inf"))
        att = F.softmax(att, dim=-1)
        att = self.attn_drop(att)
        y = att @ v  # [B, H, T, d]
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.resid_drop(self.c_proj(y))


class CausalSelfAttentionFromMemory(nn.Module):
    """Rewrite this from a blank page. Same contract as CausalSelfAttention."""

    def __init__(self, n_embd: int, n_head: int, block_size: int, dropout: float = 0.0):
        super().__init__()
        raise NotImplementedError("Day 1: implement from memory after tracing CausalSelfAttention.")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError


def next_token_loss(logits: torch.Tensor, input_ids: torch.Tensor) -> torch.Tensor:
    """logits [B, T, V], input_ids [B, T] → CE on shifted pairs.

    Position t predicts token t+1. Last logit and first token are unused.
    """
    return F.cross_entropy(
        logits[:, :-1, :].reshape(-1, logits.size(-1)),
        input_ids[:, 1:].reshape(-1),
    )


def demo_shapes(B: int = 2, T: int = 8, C: int = 32, H: int = 4, V: int = 50) -> None:
    torch.manual_seed(0)
    x = torch.randn(B, T, C)
    attn = CausalSelfAttention(n_embd=C, n_head=H, block_size=T)
    y = attn(x)
    print("x      ", tuple(x.shape), "  # [B, T, C]")
    print("y      ", tuple(y.shape), "  # same as x (residual stream)")
    ids = torch.randint(0, V, (B, T))
    logits = torch.randn(B, T, V)
    loss = next_token_loss(logits, ids)
    print("logits ", tuple(logits.shape), "  # [B, T, V]")
    print("loss   ", float(loss), "  # scalar")
    print("CE uses logits[:, :-1] vs ids[:, 1:]  →", (B * (T - 1)), "token predictions")


if __name__ == "__main__":
    demo_shapes()
