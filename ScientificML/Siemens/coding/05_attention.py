"""05. Scaled dot-product attention — PROBLEM.

Do not open 05_attention_solution.py until this file runs.

    Q [B, Tq, D]
    K [B, Tk, D]
    V [B, Tk, Dv]
    return [B, Tq, Dv]

    softmax(Q K^T / sqrt(D)) V

Narrate every intermediate shape. No mask in this file.
Complexity is about O(Tq * Tk * D). Say why the sqrt(D) is there.
""",
import torch
import math

def scaled_dot_product_attention(q, k, v):
    qkt = q @ k.transpose(-2, -1)                         # [B, Tq, D] @ [B, D, Tk] = [B, Tq, Tk]
    a = torch.softmax(qkt / math.sqrt(q.shape[-1]), dim=-1)    # [B, Tq, Tk] / []
    return a @ v                                        # [B, Tq, Tk] @ [B, Tk, Dv] = [B, Tq, Dv] 
