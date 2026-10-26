# Where the control is chosen

Logged 26 Oct 2026 from the prep discussion on MamKO versus bilinear MamKO. The confusion was whether the network emits the controls. It does not.

Meeting use: [`2026-10-27_technical-deep-dive.md`](2026-10-27_technical-deep-dive.md). Reading log: [`2026-10-26_koopman-control-prep.md`](2026-10-26_koopman-control-prep.md).

---

## The split

The learned model is a step \(z_{k+1} = F(z_k, u_k)\). The controller is a separate program that chooses the sequence \(u\) so that the rollout of \(F\) tracks a reference, subject to constraints. Only the first input is applied. The plant moves. The program runs again.

Predicted states are not a second decision. They are what \(F\) does once \(z_0\) and the candidate \(u\) are fixed. In the bilinear implementation the states are eliminated and the quadratic program is in the input increment. MamKO writes the same fact as an equality constraint inside the program (their equation 10b).

---

## MamKO, inside one solve

Li et al., ICLR 2025, equation (9g) and Section 4. At real time \(k\) the history net emits a **sequence** of matrices for the whole horizon, from observed history only:

\[
\bar A_{k:k+H-1\mid k},\;
\bar B_{k:k+H-1\mid k},\;
C_{k:k+H-1\mid k}
= \phi(z_{k-H:k-1},\, u_{k-H:k-1}).
\]

Section 4 says those sequences are generated **before** the optimization. The program then chooses \(u_{k:k+H-1}\) with those matrices held as data. Horizon in their experiments is 30.

That is option B from the discussion, not a single frozen matrix (option A) and not a recompute along the candidate future (option C). Each step of the horizon can have its own \(\bar A_{j\mid k}\), and every one of them is a function of the past window, not of the \(u\) the solver is trying. Option C would put candidate controls back into \(\phi\) and the one-shot program would stop being a convex QP. They refuse that on purpose: the appendix says generating \(B\) from a sequence that contains the current \(u\) produces a bilinear term and a non-convex program.

At the next real sample the history includes the input just applied and the state just observed, and \(\phi\) emits a new sequence. Regeneration is once per real step, from real history. It is not once per candidate trajectory inside the solve.

Their bilinear paper describes the same constraint as \(\bar A_k \perp u_k \mid X_{\mathrm{hist}}\), and the stale-plan experiment freezes that backbone for \(d\) real steps (`regen=never`). The flag is about real-time replanning, not about the solver peeking at candidate futures.

Code could still diverge from this text. The paper’s claim is the sequence-from-history version. That is the thing to confirm with Matan, not an open reading of the PDF.

---

## Bilinear, inside one solve

The history net still supplies the diagonal eigenvalues and \(B_k\). The new term is \(\sum_i u^{(i)} G_i z\), and the implemented step is the Lie–Trotter map. \(G_i\) is a learned constant, not a network of the future.

Because this step is nonlinear in the pair \((z, u)\), one QP is the wrong program. Sequential convex programming:

1. Roll the current candidate \(u\) through \(F\) to get a nominal \(z\).
2. Linearize \(F\) there. The state Jacobian is analytic. The input Jacobian is reverse-mode automatic differentiation of the Lie–Trotter step.
3. Solve a QP in the input correction, with a trust region and the original input bounds.
4. Update the candidate and repeat.

Five iterations are the controller in the headline cell (time-varying reactor). One iteration does not beat linear there. Wall-clock in their Table 3 is about 0.1 s for the linear QP and about 0.9 s for five bilinear steps, against an 18 s reactor sample. Those times are their reimplementation, not MamKO’s Table 2.

What changes with the candidate \(u\) is the bilinear term and the linearization around it. The history net is not described as being re-run on imagined future states inside the SCP loop. The stale-plan writeup is explicit that \(A_{\mathrm{eff}}(u)\) moves along a committed input while the backbone stays fixed. Ask him whether SCP also re-encodes the nominal rollout. The paper’s mechanism does not require that.

---

## What to ask, given this

The four questions from the discussion, narrowed.

1. Does your MamKO match Li et al. Section 4: one history window in, a horizon of matrices out, then a QP that does not call the net again? Or do you re-encode along the candidate rollout?
2. The bilinear term is the structured way to let the operator see the candidate \(u\) without giving up the QP. A general net \(F(z, u)\) would be option C with no convex subproblem. Which constraints have to sit inside the iteration — input bounds only, or state limits from the twin?
3. On the asset you care about, is the budget one SCP pass or five, and what is the sample period next to the 0.9 s in Table 3?
4. Training \(u\) is uniform excitation. When the solved \(u\) leaves a historian’s band, the matrices from \(\phi\) were fit on a different support. What do you measure?

---

## Bottom line

Mamba emits the dynamics for the horizon from the observed past. MPC emits the controls. MamKO can do that with one quadratic program because the matrices do not depend on the controls being chosen. Bilinear MamKO lets the drift depend on those controls, so it linearizes and re-solves. The iteration is still choosing \(u\), not a second state trajectory.
