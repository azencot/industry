# One-to-many, and where the Koopman paper sits

Study note for the follow-up with **Yochai Pagi** and **Matan Pagi**.

| | |
|---|---|
| **When** | Assumed **Tue 27 Oct 2026, 00:15 Thailand** (ICT). That is **Mon 26 Oct 2026, 20:15 Israel**. The clock date is Tuesday; the evening you prepare for is Monday. Correct this if the invite says otherwise. |
| **Call card** | [`2026-10-27_contribution-and-call.md`](2026-10-27_contribution-and-call.md) |
| **20 Oct call** | [`2026-10-20_founders-call.md`](2026-10-20_founders-call.md). Logged from the meeting summary. |

They said one-to-many on the call: make infrastructure autonomous, one expert capacity covering many facilities, because the buildout is outrunning the people who know the plants. The same sentence is on Yochai’s [Founder Index profile](https://www.globalfounderindex.com/founder-index/editions/q2-2026/psistar). Stage on that card: seed, revenue in the $100K–$1M band. Leave the revenue band off the call.

On the call the stack was two models. A time-series foundation model does the physics-informed forecast. A vision model builds an operational digital twin from the engineering plans. They decided the product is predictive operations: forecast a future state, then optimize, with reaction to the current state as the smaller problem. The advantage they claimed against existing twins is zero-shot into real-time operations. Matan’s own follow-ups were a second paper within about a month, and a write-up of their zero-shot resampler for irregular series. Neither was public as of 25 Oct. The bilinear paper remains the only published cut, and it is the optimize-on-a-forecast piece of the first model. Rosetta, Horizon, PsiFM, and Maverick are names from the site. If they stay with “time-series foundation model” and “vision twin,” use those.

---

## What to read, in order

About three hours if you stop where it says stop.

| Order | Read | Stop when |
|-------|------|-----------|
| 1 | This note, through “What the paper actually buys.” | You can say the two “manys” without notes. |
| 2 | Their post, [Operational know-how, compiled for agents](https://psistar.ai/what-the-best-operator-knows/) (2 Sep 2026). The Plant Model, the four hard problems, and the paragraph that names PsiFM. | You can draw the loop: documents → Plant Model → forecast and agent. |
| 3 | The paper, [arXiv:2605.04793](https://arxiv.org/abs/2605.04793) ([HTML](https://arxiv.org/html/2605.04793)). **§1 through eq. (1), Remark 1, §5.2, Tables 1–3, the last paragraph of §7.** Skip the SCP proof. | You can say which cell is the result, and which cell is a loss. |
| 4 | The [contribution card](2026-10-27_contribution-and-call.md). Say the forty-five seconds out loud once. | |

The two videos are already in the section below. You do not need to rewatch them.

- [World Models explained in 10 min](https://youtu.be/ECWC-YlAk1o) — Kilobright, on Ha and Schmidhuber (2018).
- [What Is Yann LeCun Cooking? JEPA Explained Simply](https://youtu.be/oM4neOyZOi0) — bycloud, 20 Apr 2026. Papers it points at: [I-JEPA](https://arxiv.org/abs/2301.08243), [V-JEPA 2](https://arxiv.org/abs/2506.09985), [LeJEPA](https://arxiv.org/abs/2511.08544).

---

## The problem they named

A control room already has sensors, a historian, and a distributed control system that can read and write every valve. The scarce object is the person who knows what a drift means on this unit and which page applies. That person learned it here, over years. The next plant does not inherit the crew, and the people who have the knowledge are leaving faster than they are replaced. Yochai’s version of this starts from a malfunction at a console: the screens could show the telemetry and retrieve a procedure, and none of them could own the situation.

“One-to-many” is the ratio they want to change. One body of expertise, many facilities. The homepage sentence is the same idea from the operator’s side: the best operator’s judgment should be available at every console, including when the link is down.

A conventional digital twin does not change the ratio. Someone still maps the tags, fits a model of this unit, and redoes it after the next outage. That is one modeling project per plant. Their claim is that the same code, pointed at a station it has not seen, produces something an engineer will trust.

They have split that claim into two different generalization problems. Mixing them is how the pipeline gets drawn backwards.

### The many that is an ingest: Rosetta

[The September post](https://psistar.ai/what-the-best-operator-knows/) is the clearest public description of the product, clearer than the homepage.

A new station arrives as documents: P&IDs, control-logic diagrams, alarm lists, O&M manuals, SOPs. They are scanned, revised, annotated, and named under KKS or ISA plus whatever the site invented. Rosetta is a mixture of discriminative models. Each model makes a checkable claim about a specific place in a specific source: this symbol is a valve, this line joins these nozzles, this row is a limit. Language models orchestrate the prose and the interface. Every fact in the output is supposed to come from a decision an engineer can score.

The output is the **Plant Model**, in four layers:

| Layer | What it holds |
|-------|----------------|
| Physical | Equipment and how it connects. |
| Sensory | Which tag measures what, where it sits, and its limits. |
| Logical | Interlocks and automatic sequences. |
| Operational | How people run it: procedures, envelopes, what to do before the interlock acts. |

Every entry points at a drawing, a page, or a row. The plant’s own engineers correct it and sign it. Maverick, the agent in the control room, sees the model only after that signature, and does not modify it.

A new station is an ingest job. The weights that have to generalize are the weights that *read drawings*. The Plant Model itself is site-specific on purpose. It is how plant B differs from plant A. They list four things that are still hard, and they call them research problems: the inputs are inconsistent across decades of scans; the same code has to read an oil rig, a power plant, and a distillation unit; a wrong edge becomes a wrong recommendation, so review has to be fast; the historian and the documents disagree, and the model has to show the disagreement rather than pick one quietly.

They also say the representation is not settled. A generic format fits any facility. A format committed to one vertical compresses more know-how. They expect to keep moving that tradeoff. That is an opening, if the conversation goes to Rosetta. It is not the Koopman paper.

### The many that is a dynamics model: Horizon, also called PsiFM

The homepage and the IVC card call the perception model **Horizon**: forecast the next physical state from the sensor stream, with a stated ambition of zero-shot on assets the model has not seen. The September post calls the forecasting model **PsiFM** and describes the interface that was missing from the homepage.

The Plant Model is an input to the forecaster. It tells the model which tags belong to which system, and which of those tags are controls, so the forecast is conditioned on what the operator can actually change. In the example loop on that page, the foundation model forecasts a tank level, the limit comes from the alarm list, and the action comes from the manual and the logic diagram.

So the loop, as they now describe it, is:

1. Rosetta reads this site’s documents and produces a signed Plant Model.
2. PsiFM forecasts where the plant is heading, using the Plant Model to know the state variables and the controls.
3. Maverick reads the forecast and the Plant Model and recommends an action that is already in the procedures. The write path to the plant is where the operator allows it.

The forecast does not create the site-specific plan. The plan is already in the documents. The forecast tells the agent which part of a plan that has been signed is the one that applies now.

Names to keep straight on the call: **Rosetta** builds the Plant Model, **PsiFM / Horizon** forecasts, **Maverick** is the agent. The company used to be called Maverick AI. The agent kept the old name.

Public customer names beyond the Siemens Energy pilot (Ori Shpigel, first mentioned 10 Sep 2026, scope withheld) come from a [directory card](https://cetsandbox.com/startup-directory/psistar/), which also lists IAI, Israel Electric, and a confidential data-center operator. Treat that list as a directory claim. Siemens Energy Israel is a different organization from the Siemens Corporation Data & AI loop.

---

## What the Koopman paper is

**Bilinear Mamba-Koopman Neural MPC for Varying Dynamics.** Matan Pagi, Zohar Sorek. [arXiv:2605.04793](https://arxiv.org/abs/2605.04793). Posted by Matan on 7 May 2026 as the first paper out of the company. No venue, no code.

It is a cut inside PsiFM, on one simulated plant at a time. It does not read a drawing, it does not transfer to a second unit, and it does not recommend a procedure. Reading it as their foundation model overclaims it. Reading it as irrelevant underclaims it. The industrial sentence inside it is real, and it is narrower than the homepage.

### The constraint they relax

MamKO (Li et al., ICLR 2025 Spotlight) watches recent state and control history and emits a fresh linear model at each step, then solves a convex quadratic program. The drift matrix is forbidden to depend on the current input. If it did, the next state would contain a product \(u \cdot z\), and the one-shot program would stop being convex.

They put that product back, with the backbone’s eigenvalues left on the diagonal:

\[
z_{k+1} = \Big(\mathrm{diag}(A) + \sum_i u_k^{(i)} G_i\Big) z_k + B_k u_k
\]

\(G_i = 0\) is MamKO again. \(G_i\) is initialized at zero, so training starts as the linear model, and any later difference is the bilinear term. They report the added parameters as under 1% of the backbone. The latent size in the runs is 8 on CartPole and 15 on the reactor–separator. They mention a low-rank factorization of \(G_i\) and do not use it; at those sizes the full matrix is cheap.

Because the map is bilinear, the state Jacobian is analytic. They solve the control problem by sequential convex programming: linearize, solve a QP, repeat. One linearization does not beat the linear controller on the hard cell. Five iterations is where the time-varying result shows up. Wall-clock in Table 3 is about 0.1 s per step for the linear QP and about 0.9 s for five bilinear steps. They say 0.9 s is practical against the reactor’s 18 s sample period, and that the CartPole timings are an offline stress test.

### Two plants, two different reasons the linear model is wrong

- **CartPole.** The force couples into the angle. The equations really do contain a product of input and state. This is the structural case.
- **RSCP.** Liu et al.’s reactor–separator: two reactors, a flash tank, recycle. Nine states, three heat duties. The duties enter the energy balance additively, so the ODE has no \(u \cdot x\) term. The time-varying version lets the reaction rates decay, as catalyst deactivation. This is the “the plant is drifting” case. It is the cell they treat as the result.

Remark 1 in the paper is the honest partition. On CartPole the bilinear model improves open-loop forecast, as the proposition says it must when the coupling is real. On RSCP the heat inputs are additive, so the proposition predicts a tie unless the learned lifting itself creates a product (a lift that contains \(x^2\) turns an additive input into a bilinear term). The tie is what they see once they average the last 50 epochs. A single best checkpoint on RSCP TV makes the linear model look 23% better, because that model’s validation loss oscillates for all 400 epochs and the checkpoint lands on a downward spike. The bilinear model settles in about 50 epochs and stays flat. They treat that stability as part of the result. It is an optimization fact about one simulator, and it is also a deployment fact: a model you retrain on a new site is more useful if the loss curve is a curve.

Closed-loop cumulative cost, Table 1, bilinear with 5 SCP steps against their own re-trained MamKO:

| Cell | Linear | Bilinear-SCP-5 |
|------|--------|----------------|
| CartPole, time-invariant (20 s) | **2.40e-2** | 2.54e-2 |
| CartPole, time-varying (20 s) | 1.79e-2 | **1.73e-2** |
| RSCP, time-invariant (2 h) | 7.90e-4 | **6.43e-4** |
| RSCP, time-varying (2 h) | 4.91e-3 | **3.44e-3** |

The number they emphasize is the last row, about 30% lower cumulative cost, and only after the convex program is iterated. One SCP step does not beat linear there. CartPole time-invariant is a small loss for the bilinear controller, on a regime they themselves call benign. Bands on the plots are \(\pm 0.3\sigma\) over 10 episodes. They note that at \(1\sigma\) some panels overlap.

The other experiment is the one that rhymes with a frozen model on a new site. The controller commits to a control sequence for \(d \in \{0,1,3,5\}\) steps, and during that window both the plan and the backbone stay frozen. MamKO’s drift was computed from history, so it cannot move until the next replan. The bilinear drift still changes along the committed input, because \(A_{\mathrm{eff}}\) depends on \(u\). On RSCP TV the bilinear model degrades more slowly. At a one-step delay the gap in their log-cost is large; at five steps it is still there. They exclude a ten-step delay: both models saturate, and the difference is no longer about the model class.

Their scope paragraph says what they did not do. The encoder still has to find a lifting where the step is approximately linear. The controller’s guarantee is local. This is a structural patch inside the MamKO family. Benchmarks are simulated. Nothing in the paper is a plant, a turbine, or a data hall. The linear baseline is their own re-run, and on CartPole TV that re-run does not match Li et al. (their \(7.8 \times 10^{-3}\) against the published \(4.3 \times 10^{-4}\)). “We beat deep Koopman” would mean MamKO beat it in the original paper, and they beat their own MamKO. There is no deep-Koopman number in this manuscript.

The last paragraph of the conclusion is the invitation. They name three open directions: let the input matrix \(B_k\) be bilinear too; put a structured prior on \(G_i\) that encodes a known coupling topology; and build a benchmark that separates the \(u \cdot x\) axis from the time-varying axis. The middle one is the joint between the two engines. The coupling topology of a real unit is what Rosetta is trying to extract and get signed.

### What the paper buys inside one-to-many

The failure mode of a model that is supposed to cover a new unit is that the new unit is already leaving the distribution the backbone saw: fouling, a feed change, a controller that cannot recompute every sample. The paper’s mechanism is a small, stationary dependence of the drift on the current input, so the step can still change while the backbone is frozen. They showed that mechanism for a few steps of a stale plan, on one time-varying simulator, with the state fully observed and the controls excited at random.

That is a precise piece of “do not refit the whole model on site.” It is not yet “this lift works on a unit we held out.”

---

## The two videos, read against their stack

Both videos are about the same three objects: an encoder, a step in the encoded space, and a way to choose an action by rolling that step forward. Their product is those three objects with an audit constraint the videos do not have. The useful comparison is which object each design chooses to make simple.

### Ha and Schmidhuber, as the first video tells it

The 2018 world model has three pieces.

The vision model is a variational autoencoder. It compresses a frame and throws away detail it can reconstruct from a short code. In their stack this is the encoder \(\psi\) that takes sensors, or a window of sensors, to a latent \(z\). Rosetta is a different encoder: it reads documents, and its output is a graph with provenance, not a code you step forward.

The memory is an RNN with a mixture-density head. Given the latent so far and the action just taken, it predicts a *distribution* over the next latent, a mixture of Gaussians. One history, several plausible next worlds. Roll the mixture and you can sever the real environment and practice inside the model. Their stale-plan experiment is that severance for a deterministic step: freeze the backbone, commit to \(u\), roll \(z\).

The controller is small. It reads the latent and picks an action, and in the paper it is often trained inside the dream rather than on the real environment. Their controller is the SCP quadratic program, and above it Maverick, which is not allowed to invent an action. The action has to be a procedure that is already in the signed Plant Model.

Two differences are worth having ready, because they are the conversation.

Their training data, in the paper, is random open-loop excitation, then a separate planning stage. Ha’s loop trains the controller on the model’s own rollouts. Asking which loop PsiFM uses is a real question: a historian is closed-loop data from a human or a PID, which is a third thing, neither random excitation nor imagination.

Their step is one next \(z\). Ha’s step is a mixture. A plant can go more than one way from the same tags. The homepage and the IVC card say the decision path has no probabilistic component, because a control room has to audit the action. The design that keeps both facts is in the contribution card: several futures are allowed in the latent, and the action is emitted only when those futures agree on the procedure.

### JEPA, as the second video tells it

A view is a partial look at the same underlying state: a crop, a mask, another frame, another sensor. The context encoder embeds the look you have. The target encoder embeds the look you are trying to anticipate. A predictor maps the context embedding to the target embedding. The loss is the distance between those two vectors. Nobody asks the network to draw the missing pixels.

That is the whole idea, and the reason the video is hard to follow is that the object being predicted is a representation the model invented. The failure mode has a name. If the only pressure is “match the other embedding,” both encoders can map every input to one point and the distance is zero. The video’s tour of EMA targets, VICReg, Barlow Twins, and LeJEPA is a tour of guards against that collapse.

V-JEPA 2 adds the action. A predictor trained on video, then a smaller action-conditioned head, predicts the next embedding given the action. Planning searches actions whose predicted embedding lands near a goal embedding. The goal can be “the embedding of the frame where the task is done.” No pixels are rendered while the search runs.

Set next to equation (1) and equation (10), the comparison is specific.

Their predictor is the bilinear map. JEPA’s predictor is a network with no requirement that the step be linear. Linearity, and the small bilinear extension, is what lets them hand the rollout to a quadratic program with an exact Jacobian and a local convergence citation. A JEPA predictor would plan by search in embedding space, the way V-JEPA 2-AC does. That search can score “is the predicted state inside the envelope on this page.” It does not, by itself, give them the audit trail they are selling. The bilinear step is the part of the world model they made simple enough to certify. Offering to replace it with a generic predictor throws away the reason they wrote the paper.

Their loss is the part that is not yet a JEPA. Equation (10) is multi-step mean squared error in the original sensors, plus a penalty that pushes the discrete eigenvalues inside a margin of the unit disk. Reconstruction forces \(z\) to carry whatever is needed to redraw the tags, including noise that belongs to this unit’s instrumentation. A JEPA loss forces \(z\) to carry whatever is needed to predict the next \(z\), and lets the rest go. Across units, the rest is a lot of what differs: which sensor is noisy, which tag is scaled oddly, which mode this plant rarely visits. Predicting the embedding is a hypothesis about transfer. It is the first ablation in the contribution card, not a proposal to adopt the brand.

The guard they already have against a useless latent is the decoder, plus the spectral penalty. A pure embedding loss removes the decoder’s pressure. Any experiment in that direction has to keep a path back to a tag an engineer can check, or the Plant Model’s sensory layer has nothing to attach to.

The goal in their MPC is a setpoint in the latent, decoded toward a tracking cost. The goal in the product, as the September post describes the tank example, is a region defined by an alarm limit and a procedure. Those are embeddings of a kind: “inside the envelope on page 14” is a set of latents, and the Plant Model is what names the set. V-JEPA’s planning picture is useful here as a sentence. Roll the bilinear step, and ask whether the rolled state lands in the set the signed procedure calls acceptable. That is Maverick’s question, asked of a model whose step is still the one in the paper.

---

## The gap, in one place

| Object | What exists in public | What one-to-many still requires |
|--------|------------------------|----------------------------------|
| Plant Model | Rosetta’s four layers, provenance, engineer sign-off. Described, not benchmarked in the paper. | The same reader, no new code, on a drawing convention it has not seen. A measurement for a whole facility, which they say does not exist publicly. |
| Encoder / lift | Assumed. “Expressive enough to find a lifting where the step is approximately linear.” Latent size 8 or 15. | A lift that survives a second unit. The Plant Model’s sensory layer is the proposed dictionary of which tag is which. |
| Step | Bilinear MamKO, \(G_i\) dense, initialized at 0, spectral penalty at train time only. | \(G_i\) with a sparsity pattern taken from the signed physical layer. They list this as future work. |
| Training data | 60-step windows, i.i.d. uniform excitation, full state, regular time. 39,900 windows. | A historian: closed-loop actions, missing tags, irregular samples, one regime, and a short one on a new site. |
| Uncertainty | \(\pm 0.3\sigma\) over 10 simulated episodes. At \(1\sigma\), overlap. | A forecast that can split, and a rule for when that split refuses an action. The decision that ships is still a page number. |
| Action | Setpoint tracking by SCP. | A procedure from the operational layer. The paper never closes that loop. |
| Frozen model | Stale plan, \(d \le 5\), one simulator. | Frozen shared weights, a thin local correction, a held-out unit, and a definition of success that is the procedure an engineer would have picked. |

The paper is evidence that they know the frozen-backbone case is the one that matters, and that they have a mechanism for it inside a single plant. The contribution is the row that says “a second unit.”
