# Koopman control prep — logged 26 Oct 2026

What the prep chat assigned, and what was actually covered before the Tue 27 Oct 00:15 Thailand deep dive. Meeting briefing stays in [`2026-10-27_technical-deep-dive.md`](2026-10-27_technical-deep-dive.md). Where the control is chosen: [`2026-10-26_where-control-is-optimized.md`](2026-10-26_where-control-is-optimized.md).

The chat’s goal was the control stack, not another pass on Koopman theory: linear versus time-varying versus bilinear MPC, and SCP versus a fully nonlinear action-conditioned model.

---

## What was done

| Item | Depth |
|------|--------|
| [Korda & Mezić, arXiv:1611.03537](https://arxiv.org/abs/1611.03537) | Skimmed. |
| [MamKO, ICLR 2025](https://openreview.net/pdf?id=hNjCVVm0EQ) | Read. |
| [Bilinear MamKO, arXiv:2605.04793](https://arxiv.org/pdf/2605.04793) | Read. Same manuscript as the Psistar HTML. |
| [Steve Brunton, Model Predictive Control](https://www.youtube.com/watch?v=YwodGM2eoy4) | Watched. Receding horizon: optimize a short input sequence, apply the first move, shift, repeat. Constraints are why the program is re-solved. |
| [XMPro, Agentic Operations for Industrial Enterprises](https://www.youtube.com/watch?v=n2p620UJ8p8) | Watched. Industrial-autonomy product talk, not a control lecture. |
| [The IT OT Insider, Can AI Run Your Plant?](https://www.youtube.com/watch?v=kRcqCR6nwnY) | Watched. Plant-operations talk, not a control lecture. |

Not started from the assigned list: Brunton’s Koopman-with-control and DMDc lectures, a bilinear-Koopman lecture, an SCP lecture, the Annual Reviews overview ([doi:10.1016/j.arcontrol.2025.101035](https://doi.org/10.1016/j.arcontrol.2025.101035)), and the mixed stochastic–deterministic tube paper ([doi:10.1016/j.jprocont.2025.103533](https://doi.org/10.1016/j.jprocont.2025.103533)). The bilinear paper’s own SCP section covers their algorithm. Those two robustness papers are the unread source for stability, recursive feasibility, and tubes. Do not speak as if they were read.

---

## The ladder, as far as the reading goes

**Linear Koopman MPC** (Korda & Mezić). Lift, then \(z_{k+1} = Az_k + Bu_k\). For a fixed \(A, B\), a quadratic stage cost and polyhedral constraints are a convex QP. The trajectory is the constraint. The decision variable is the input sequence. One program, one horizon, then recede.

**Time-varying Koopman MPC** (MamKO). A history network emits \(\bar A_k, \bar B_k, \bar C_k\). “Mamba” here is the selective-state-space idea used as a matrix generator: convolution and fully connected layers, not a language model. \(\bar A_k\) is a function of history and is independent of the current input, so the QP stays convex. Inside one solve the operators are data. They change when the horizon recedes and the history updates. They are not decision variables.

**Bilinear Koopman MPC** (their paper). \(A_{\mathrm{eff}}(u) = \mathrm{diag}(A) + \sum_i u^{(i)} G_i\), Lie–Trotter so \(G = 0\) is MamKO exactly. The product kills the one-shot QP. SCP linearizes the implemented map about a nominal \((z, u)\), solves a QP in the input increment with a trust region, and repeats. Five iterations are the reported controller. The Jacobian is exact (reverse mode), not a finite difference. Convergence they cite is monotone descent and KKT points of that local program under standard trust-region assumptions. That is not closed-loop stability and not recursive feasibility.

**A fully nonlinear action-conditioned operator** would let the whole map depend on \(u\) through a network, with no bilinear Jacobian and no convex subproblem. SCP is the compromise they chose: more expressive than MamKO, still a sequence of QPs. Differentiating through the rollout (single shooting, or backprop through the learned step) drops the per-iterate convex program and the constraint handling that comes with it.

**Robust / tube MPC** is the unread layer. Model mismatch, chance constraints, a tube that keeps the true state inside the constraint set, recursive feasibility. Their manuscript does not claim it. The spectral hinge is training-only.

---

## Questions from that chat

Use these only where they add something the [briefing](2026-10-27_technical-deep-dive.md) does not already ask. Distribution shift, generalization, and “what is the model” are already on that list.

1. **What does the history net contribute beyond a recurrent encoder?** Ask only if he wants to talk architecture. The published answer is a time-varying linear model from a conv–FCNN, with \(A\) independent of current \(u\). If he says the gain is selective memory of the recent window, the follow-up is whether that memory still matters once \(G\) carries input-dependent drift.
2. **Why bilinear, rather than a network that takes \((z, u)\) and emits the next \(z\)?** This is the expressivity-versus-QP question. Their answer in the paper is the exact Jacobian and SCP. Press only if he claims the bilinear class is enough for the plants they care about. CartPole is the coupling case. The reactor is the drift case, and its ODE has no \(u \cdot x\) term.
3. **Could a detached, control-conditioned operator be the cheap surrogate?** Their stale-plan experiment is this object: backbone frozen, \(A_{\mathrm{eff}}\) still evaluated on the committed \(u\). A detached operator is MamKO’s history-only \(A\) replaced by a map that sees the planned inputs and is then held fixed for \(d\) steps. Worth one question if the conversation is already on compute. It is a design inside their method, not a new stack.
4. **Why SCP, rather than differentiating through the learned step?** SCP keeps a constrained QP at each iteration and a local KKT citation. Shooting through the network keeps the nonlinearity and gives up that subproblem. Ask which constraints they need inside the iteration: input bounds only, or state constraints from the twin. Input bounds are in the paper. Twin constraints are not.
5. **Distribution shift when the optimized \(u\) leaves the training support.** Already question 5 in the briefing. Training in their paper is uniform excitation, which is a wide support. The missing arm is a historian.
6. **Closed-loop stability, recursive feasibility, constraint satisfaction.** The honest scope is local KKT of the SCP iterates, plus a train-time spectral hinge. No tube, no recursive-feasibility proof, no runtime spectral check. If he claims a guarantee past that, ask which theorem. The overview and the tube paper are the literature for this, and they are unread.
7. **Unseen regimes and facilities.** Already the shared-lift experiment. Nothing in MamKO or the bilinear paper is a transfer run.

---

## Still optional before the meeting

Only if there is time and the bilinear SCP section feels thin: one SCP lecture, focused on linearize, trust region, repeat, and the difference between convergence of the program and stability of the closed loop. The robustness papers can wait until after he says whether a guarantee is even on their list. The two industrial videos are context for “who else claims autonomous plants,” not material to review with Matan.
