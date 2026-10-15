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

def masked_attention(q, k, v, key_padding_mask=None, causal=False):
    raise NotImplementedError
