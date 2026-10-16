"""06. Masked attention — PROBLEM.

Do not open 06_masked_attention_solution.py until this file runs.

Same inputs as scaled dot-product attention, plus:

    key_padding_mask [B, Tk] bool, True = valid key, False = pad. Optional.
    causal: if True, query i cannot attend to key j > i. Requires Tq == Tk
            for the usual square mask. Here Tq and Tk may differ: block j > i.

Mask BEFORE softmax. Invalid logits get -inf, not 0.
A row that is all -inf becomes NaN after softmax. Those rows should
come out as zeros, not NaN.

Say what happens to the output if you forget the padding mask.
""",
import torch
import math

def masked_attention(q, k, v, key_padding_mask=None, causal=False):    
    d = q.shape[-1]
    scores = q @ k.transpose(-2, -1) / math.sqrt(d)              # [B, Tq, D] @ [B, D, Tk] = [B, Tq, Tk]

    if key_padding_mask is not None:
        scores = scores.masked_fill(~key_padding_mask[:, None, :], float("-inf"))

    if causal:
        B, Tq, Tk = scores.shape
        Mc = torch.ones([Tq, Tk], dtype=torch.bool, device=scores.device)
        Mc = torch.triu(Mc, diagonal=1)
        scores = scores.masked_fill(Mc, float("-inf"))

    a = torch.softmax(scores, dim=-1)
    a = torch.nan_to_num(a, nan=0.0)
    return a @ v
