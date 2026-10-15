"""11. Evaluation loop — PROBLEM.

Do not open 11_eval_loop_solution.py until this file runs.

def evaluate(model, loader, criterion) -> float

model.eval() changes dropout and batch-norm. It does NOT stop autograd.
Wrap the forwards in torch.no_grad().

Do not call optimizer. Return mean loss over batches.
No zero_grad, no backward, no step.
""",

def evaluate(model, loader, criterion):
    raise NotImplementedError
