"""B. Train step and eval — PROBLEM.

No solution file.

def train_one_epoch(model, loader, optimizer, criterion) -> float
    Each batch is (x, y).
    model.train()
    for each batch: zero_grad, forward, loss, backward, step
    Return the mean loss over batches as a Python float.

def evaluate(model, loader, criterion) -> float
    model.eval() and torch.no_grad().
    Return the mean loss. Parameters must not change.
    Gradients must not accumulate.

Tests to write:
- on a tiny linearly separable set, loss after several epochs is lower
- a parameter tensor actually changes
- after evaluate(), every parameter.grad is unchanged (None, or the same storage)
- criterion is cross-entropy on raw logits

Time box: 30 minutes.
"""
import torch

def train_one_epoch(model, loader, optimizer, criterion):
    # quit if no data (loader is empty)

    device = next(model.parameters()).device

    model.train()

    total_loss = 0.0
    for (x, y) in loader:

        optimizer.zero_grad()
        yp = model(x.to(device))
        loss = criterion(yp, y.to(device))
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(loader)


def evaluate(model, loader, criterion):
    device = next(model.parameters()).device

    model.eval()

    total_loss = 0.0
    with torch.no_grad():
        for (x, y) in loader:
            yp = model(x.to(device))
            loss = criterion(yp, y.to(device))

            total_loss += loss.item()

    return total_loss / len(loader)
            
