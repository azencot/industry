# Call sheet — 27 Oct 2026

Open this during the call. Background stays in the other notes.

| | |
|---|---|
| **When** | **Tue 27 Oct 2026, 00:15 Thailand** (Mon 26 Oct, 20:15 Israel). **45 min.** |
| **Who** | **Yochai Pagi** (CEO), **Matan Pagi** (CTO). **Zohar Sorek** coauthored the bilinear paper. |
| **Already agreed** | Principal Researcher, **40%–60%**. Agenda plus hands-on. Seattle was in your letter and was not restated. |

Say this if you want the hour to have a shape, then let them go where the substance is.

> I want to use the time on four things: the problem you are on now, the solution you have, where I would sit and who I would work with, and what the next six months would need to look like for this to be a fit.

If Matan is in the middle of a real failure of the model, stay there. Cut the last block to five minutes rather than rushing the model.

**0–10. Current / next problem.** Leave with which problem is the six-month job, in their words.

**10–25. Current solution.** Leave with what the model actually is, and where it has broken.

**25–35. Where you fit, and who you work with.** Leave with one direction, and the person you would work with on it.

**35–45. Expectations and mutual fit.** Leave with the artifact at six months, and what you can have in month one.

---

## 1. Current / next problem — 10 min

Ask the level first. Then stay on that branch. Both lists will not fit in ten minutes.

**Ask:** Which level of one-to-many are you on now, and which is next?

Understanding the plant, then operating the plant, then supervising many plants.

**Their level, in their words:**

### If it is one predictive model

The question under that level is which object is supposed to be universal.

> Do you want one dynamical model that covers unseen plants, or one mechanism that identifies a plant-specific model for each new plant?

A universal model would transfer with no plant-specific retraining, from historical observations and, where you have them, structure taken from the engineering documents. A universal mechanism would be allowed to fit something local, and the thing that transfers is the procedure for that fit.

Ask only what their answer leaves open.

- What context is enough to identify the dynamics of a plant the model has not seen?
- What does the model treat as a state?
- What, exactly, is shared across plants?
- What information exists for a new plant?
- What does zero-shot mean here?
- How heterogeneous are the plants?
- How will success be measured?

**Their answer:**

### If it is the higher level

Supervising many plants, past a forecast. Ask these. Do not mix them into the model branch.

- What does one-to-many mean operationally?
- What currently prevents it?
- How do operators actually spend their time?
- What happens when two incidents are live at once?
- How different are the plants?
- How would you demonstrate success?

The concrete version, if the answers stay abstract:

> Suppose the system is deployed at ten power plants and each plant still has a dedicated operator. What are the three most common reasons those operators cannot be removed?

**Their answer:**

---

## 2. Current solution — 15 min

What the bilinear paper supports is this chain. A history net emits time-varying Koopman operators from the observed past. The bilinear term lets the drift depend on the current control. Model-predictive control then chooses the inputs, by one quadratic program in the linear case and by sequential convex programming once the term is bilinear. Five passes are the headline controller, about 0.9 s against 0.1 s. On the time-varying reactor, closed-loop cost is about 30% lower. The calm cart is a little worse.

Operators that depend on context are how one plant adapts as it drifts. That is not the same result as one model shared across plants. The paper has no shared training and no held-out plant. The irregular-series resampler was named on 20 Oct and is unpublished. A link from the vision model into the predictor is not in the paper.

The path that would make the context-dependent operators into zero-shot is one shared map, taking a plant’s history to that plant’s operators, with the shared weights left alone. Whether they want that, or a fresh model per plant, is the question.

**Ask:**

- How do you represent different plants?
- Is the bilinear model trained separately for each plant, or is one model trained across several dynamical systems?
- How do you handle plants with different numbers and types of sensors and controls?
- On a new plant, what does the predictive model need before the predictions are accurate? Historical trajectories, a calibration, or a parameter update?
- Does the plant-specific vision model give structure to the predictive model, or are the two independent?
- Does the irregular-series work cover asynchronous readings from a fixed set of sensors, or can it also take a different sensor set on each plant?

If the answer is still one plant, ask where the formulation has broken, and whether a solve emits the matrices from history once and then stops.

**Their answer:**

**What is still open:**

---

## 3. Where you fit, and who you work with — 10 min

Say this, then the experiment. The other two directions wait unless they pull on them.

> The piece I can take is the step from adaptation inside one plant to a plant you have not trained on. One shared mechanism reads a plant’s history and emits that plant’s operators. The weights stay frozen. A separate model per plant is the thing this replaces.

**First, and the one to own.** Split what the history means. A plant code \(c_i\) is what stays fixed about plant \(i\). A state code \(r_t\) is the recent operating condition. The operators are a function of both, \((A_t, B_t) = G(c_i, r_t)\), with \(G\) shared. That is amortized identification: infer the plant, do not refit it. This is the structured-Koopman and disentangling work.

**Second, if they ask about doubt.** A distribution over operators given a short history, \(p(A_i, B_i \mid \mathcal{H}_i)\), when the context is too thin to name one plant. That is the generative and probabilistic side. It becomes useful once a point estimate already transfers. It is a worse first paper.

**Third, if the vision model is actually connected.** The plant encoder also sees sensor identity, equipment, and topology, \(z = E(x, \mathcal{M})\), with \(\mathcal{M}\) from the documents. This is the multimodal piece. It is the ambitious one, and it depends on how many plants exist and how different they are. Few plants, or plants that are nearly the same, means the transfer needs a physical bias rather than more data.

**The experiment, if they want a concrete start.** Leave one plant out. Train ordinary MamKO across the others. Train the split encoder the same way. On the held-out plant, no gradient steps. Compare both to a model fit on that plant alone. Plot error against how much context the held-out plant is given. Closed-loop cost comes after the forecast number is real.

**Ask:**

- How many plants do you have, and how different are they? That decides whether this experiment can be run.
- Who would I work with week to week, and who decides the paper?
- What stays outside this seat? Drawing ingestion, customer tag mapping, and the pilot backlog.

**Their answer:**

**People:**

---

## 4. Expectations and mutual fit — 10 min

The fraction is settled. This block is the work, the access, and whether both sides want that work.

A fit is one pre-registered experiment and a paper, with you in the runs, at two or three days a week. A poor fit is the seat becoming the on-call path for a pilot.

**Ask:**

- If one problem is solved in six months, which one changes the company?
- What can I train on in month one? A simulator you can check out, or a historian that stays on site?
- What do you need from me in the first month, and what should you have from me at six months?

**Their answer:**

**Agreed next step:**

---

## If you say one technical sentence

> The piece I can take is not a better solver. It is a shared mechanism that reads a plant’s history and emits that plant’s operators, with the weights frozen on a plant that was held out. The first number is prediction error against a model fit on that plant, as a function of how much context you give it.
