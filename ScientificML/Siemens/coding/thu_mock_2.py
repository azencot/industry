"""Unseen mock. 25 minutes.

    params:   a list of parameter tensors
    lr:       positive float
    max_norm: positive float
    return the global L2 norm of the gradients, before any scaling

Every parameter has a .grad of the same shape as the parameter.
The global norm is the square root of the sum, over all parameters,
of the sum of squares of that gradient.

If the global norm is greater than max_norm, multiply every gradient
by max_norm / global_norm before the step. Otherwise leave the
gradients as they are. If the global norm is 0, change nothing.

Then take one SGD step: each parameter decreases by lr times its
(possibly scaled) gradient. Do this under torch.no_grad(). These are
leaves. The step itself is not part of the graph.

Do not call clip_grad_norm_ or an optimizer.

Write 2–3 tests before you trust it:
- a norm already under the cap moves each parameter by lr times its gradient
- a norm over the cap scales every parameter's gradient by the same factor
- an all-zero gradient leaves the parameters unchanged and does not divide by zero
"""

import torch


def sgd_clipped_step(params, lr, max_norm):
    
    global_grad_norm = 0.0
    for p in params:
        global_grad_norm += torch.sum(p.grad ** 2)
    global_grad_norm = torch.sqrt(global_grad_norm)

    if global_grad_norm > max_norm and global_grad_norm > 0:
        for p in params:
            p.grad = p.grad * max_norm / global_grad_norm

    with torch.no_grad():
        for p in params:
            p -= lr * p.grad

    return global_grad_norm

    
