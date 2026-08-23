"""Day 2 — toy concat / scatter multimodal LM (shapes left blank).

Fill every `# SHAPE:` from the named constants. Do not look up LLaVA.
RoPE / mask / `-100` / freeze / detach: answer the comments at the bottom.

Scatter path (LLaVA): prompt already reserved T_v image-placeholder ids; length stays T.
Concat path: cat(h_v, h_t) grows the sequence.

Vision encoder is a stub that already emitted patch features z_v. You own the projector
and the insert. LLM is a stand-in Linear so you can see logits + CE, not a real stack.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

# --- named sizes (use these in SHAPE comments) --------------------------------
B = 2
T_v = 4  # vision tokens / reserved placeholders
T = 10  # text length including the T_v placeholders (scatter)
d_v = 8
C = 16  # LLM width
V = 32  # vocab
IMAGE_TOKEN_ID = 1  # reserved id; not a real word


def causal_mask(S, device):
    # additive mask: 0 on allowed, -inf on forbidden (upper triangle)
    m = torch.triu(torch.full((S, S), float("-inf"), device=device), diagonal=1)
    # SHAPE m (unbatched): [T, T]
    return m


class Projector(nn.Module):
    def __init__(self, d_v, C):
        super().__init__()
        self.W = nn.Linear(d_v, C, bias=False)

    def forward(self, z_v):
        # z_v SHAPE: [B, T_v, d_v]
        h_v = self.W(z_v)
        # h_v SHAPE: [B, T_v, C]
        return h_v


class MultiModalLM(nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = nn.Embedding(V, C)
        self.proj = Projector(d_v, C)
        # stand-in "blocks + ln + lm_head" — one Linear so CE is real
        self.lm_head = nn.Linear(C, V, bias=False)

    def scatter_vision(self, h_t, h_v, input_ids):
        """Replace placeholder rows of h_t with rows of h_v. Length stays T."""
        # h_t SHAPE: [B, T, C]
        # h_v SHAPE: [B, T_v, C]
        # input_ids SHAPE: [B, T]
        h = h_t.clone()
        for b in range(input_ids.size(0)):
            slots = (input_ids[b] == IMAGE_TOKEN_ID).nonzero(as_tuple=False).squeeze(-1)
            h[b, slots] = h_v[b]
        # h SHAPE: [B, T, C]
        return h

    def concat_vision(self, h_t, h_v):
        """Prepend vision. Length grows. Compare to scatter."""
        h = torch.cat([h_v, h_t], dim=1)
        # h SHAPE:
        return h

    def labels_scatter(self, input_ids, answer_from):
        """Next-token labels; vision + prompt positions = -100.

        answer_from: first index whose *prediction* (logits[t] -> token t+1)
        is in the loss. Typical: last prompt index, so only the answer is trained.
        """
        labels = input_ids.clone()
        # SHAPE labels (before mask): [B, T]
        vis = input_ids == IMAGE_TOKEN_ID
        labels = labels.roll(-1, dims=1)
        labels[:, -1] = -100
        labels[vis] = -100
        labels[:, :answer_from] = -100
        # SHAPE labels (after mask) — same rank/size; values changed: [B, T]
        return labels

    def forward(
        self,
        input_ids,
        z_v,
        answer_from,
        mode="scatter",
        freeze_encoder=True,
        detach_vision=False,
    ):
        # input_ids SHAPE: [B, T]
        # z_v SHAPE: [B, T_v, d_v]
        if freeze_encoder:          # if z_v is detached, it becomes a leaf, and thus encoder is frozen
            z_v = z_v.detach()

        h_t = self.embed(input_ids)
        # h_t SHAPE: [B, T, C]
        h_v = self.proj(z_v)
        # h_v SHAPE: [B, T_v, C]
        if detach_vision:
            h_v = h_v.detach()      # if h_v is detached, it becomes a leaf, and thus projector is frozen

        if mode == "scatter":
            h = self.scatter_vision(h_t, h_v, input_ids)
            S = input_ids.size(1)
        elif mode == "concat":
            h = self.concat_vision(h_t, h_v)
            S = h.size(1)
        else:
            raise ValueError(mode)
        # h SHAPE (depends on mode): [B, T, C]
        # S = sequence length after insert = T

        # RoPE would apply to Q,K of this fused h, using indices 0..S-1.
        # (not implemented — write where it sits in the comments below)

        m = causal_mask(S, h.device)
        # m SHAPE: [T, T]
        # scores would be (Q K^T)/sqrt(d_k) + m  →  then softmax → A
        # A SHAPE if one head:
        # Y = A V  SHAPE:

        logits = self.lm_head(h)
        # logits SHAPE: [B, T, V]

        if mode == "scatter":
            labels = self.labels_scatter(input_ids, answer_from)
        else:
            labels = None  # concat labels: vision prefix all -100, then same text rule
        # labels SHAPE (scatter): [B, T]

        loss = None
        if labels is not None:
            loss = F.cross_entropy(
                logits.reshape(-1, V),
                labels.reshape(-1),
                ignore_index=-100,
            )
            # CE sees a vector of length B*S; positions with -100 are dropped.
        return {"h": h, "logits": logits, "labels": labels, "loss": loss, "S": S}


def toy_batch():
    """One reserved image span at the front of each row, then prompt, then answer."""
    input_ids = torch.zeros(B, T, dtype=torch.long)
    input_ids[:, :T_v] = IMAGE_TOKEN_ID
    input_ids[:, T_v:] = torch.randint(2, V, (B, T - T_v))
    z_v = torch.randn(B, T_v, d_v)
    # z_v SHAPE: [B, T_v, d_v]
    # input_ids[:, :T_v] SHAPE: [B, T_v]
    answer_from = T_v + 3  # first three text tokens = prompt, rest = answer
    return input_ids, z_v, answer_from


if __name__ == "__main__":
    torch.manual_seed(0)
    model = MultiModalLM()
    input_ids, z_v, answer_from = toy_batch()
    out = model(input_ids, z_v, answer_from, mode="scatter")
    # Fill SHAPE comments first. Then, if you want a sanity check, print:
    #   out["h"].shape, out["logits"].shape, out["labels"].shape, out["S"]
    # Do not print until the comments are filled.
    _ = out


# --- interrogate (write answers here; not shapes) ------------------------------
# Where does RoPE sit? Do text positions restart at 0 after vision?
#   RoPE sit in QK^T, specifically, qi R_{j-i} kj
# Can vis[0] attend to the question? Can the first answer token attend to vis[-1]?
#   vis[0] can not attend to later text due to m; answer can attend back
# Forget -100 on vision. Distinctive CE term? After -100, can first-text still
# attend to last-vis?  (not: can last-vis attend forward — causal already says no)
#   vis_i -> vis_{i+1} (CE). first-text attends to last-vis: yes
# freeze_encoder=True. Who gets grad from CE?
#   answered in code
# detach_vision=True (after projector). Who gets grad from CE?
#   answered in code
# Text gets better, second modality ignored. Name two mechanisms.
#   1st mechanism: data that requires modality use; 2nd mechanism: change text to not reveal answer
