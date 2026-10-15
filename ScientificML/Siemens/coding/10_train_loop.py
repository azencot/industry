"""10. Training loop — PROBLEM.

Do not open 10_train_loop_solution.py until this file runs.

def train_one_epoch(model, loader, optimizer, criterion) -> float

Each batch from loader is (x, y).
Order: model.train(), then for each batch zero_grad, forward, loss,
backward, step.

Return the mean loss over batches (a Python float).

Say why zero_grad is first: backward adds into .grad.
""",

def train_one_epoch(model, loader, optimizer, criterion):
    raise NotImplementedError
