# Depth recall — 30 Oct 2026

**Kind:** Active recall with a score after each answer. Not a mock. Depth-mock average stays 7.25. Mocks stay in [`mocks.md`](mocks.md).
**Scope:** Koopman, controlled Koopman, diffusion, VAE versus diffusion versus GAN. EM was skipped.
**Status:** He stopped after four questions. Scores 9, 7, 8.5, 8. Average 8.1. Diffusion stays at this level. No EDM derivation unless a paper talk needs it.

The corrections are the review. They are not what he said.

---

## 1. Koopman — 9

\(x_{t+1}=f(x_t)\). He said the operator acts on observables, and it is linear because composition is linear in the observable, even when \(f\) is not. A finite model is exact on a Koopman-invariant subspace. One-step error can still blow up over a long horizon if the subspace is only approximately invariant or an eigenvalue is unstable.

Add two limits. An invariant subspace does not reconstruct the state unless the observables carry the state. A spectral radius below 1 does not rule out a large transient. A non-normal matrix can grow before it decays.

Do not drill this again.

## 2. Control and MPC — 7

Autonomous \(f(x)\) has no place to put \(u\). He also said the usual move is to concatenate state and control, embed, and map, while a controller still wants the raw \(u\). That is the right split. An autonomous model on the concatenated pair also needs a model of how \(u\) itself evolves.

Linear control is \(z_{t+1}=Az_t+Bu_t\). Bilinear control is \(z_{t+1}=Az_t+\sum_i u_{t,i} B_i z_t\). The extra term is the state-dependent effect of \(u\). He named that, and he named that the bilinear program is not convex. Both are right. That part was a 9. The closed-loop part was a 4.

One-step accuracy is not a good MPC. He said only that the program is nonconvex and an iteration may not converge. Also say: the horizon adds the one-step errors; the optimizer can leave the controls seen in training; it can exploit a wrong model; and a small state error can hide a wrong \(\partial f/\partial u\). The check is a multi-step rollout, that sensitivity, constraint violations, and the closed loop. Not the one-step loss.

**Say again before the interview.** This is the depth gap that is still open.

## 3. Diffusion — 8.5

He said a forward pass adds noise and the network is trained to remove it. Sampling iterates: denoise, then add a weaker noise, because the clean step is a Gaussian mean and the denoise is approximate. Slow sampling is the cost. Training is more stable than a GAN, which can collapse.

Training samples a noise level and builds that noisy point. It does not walk every forward step. The target can be the noise, the clean point, or a velocity. A reverse step does not have to add noise. DDIM and the probability-flow ODE are deterministic. Many steps are the reverse process, not only a sign that the network is imperfect. Stable training is not the same claim as cheaper training than a GAN.

Enough for a general depth question. Do not add an EDM session.

## 4. VAE, diffusion, GAN — 8

A VAE maximizes an ELBO: reconstruction plus a KL. He called the reconstruction MSE. Diffusion, he said, is one denoising loss of a cleaned sample against the clean one. Blur, he said, is because MSE punishes large errors and tolerates small ones, while diffusion’s MSE is spread over steps so the error shrinks. For 10,000 samples a second he would use a VAE, one network evaluation.

The ELBO is right. The reconstruction term is the decoder’s log-likelihood. MSE is the Gaussian case, not every VAE. In that Gaussian case the optimum is the conditional mean. Several sharp \(x\) for one \(z\) average into a blur, and a latent that dropped the detail makes it worse. Diffusion is not “the same MSE, just in steps.” A GAN is also one forward pass. Put it next to the VAE when the requirement is throughput. A usual diffusion sampler is the expensive one.

## 5. EM — skipped

He stopped before the question. No score. Not a miss.

The intended question was ordinary EM: E-step \(q^{(k)}(z)=p_{\theta^{(k)}}(z\mid x)\), M-step maximize \(\mathbb{E}_q[\log p_\theta(x,z)]\). Exact EM makes the observed-data log-likelihood nondecreasing because the bound is tight at \(\theta^{(k)}\) and the M-step raises it. An approximate \(q\) drops that guarantee unless something else keeps the bound moving up.

That is standard EM. It is not the Closing the Loop theorem. Five minutes, later, if there is time. Do not recite it as the paper.

## What not to repeat

Koopman as an idea, and diffusion as noise then denoise, are in good shape. The open depth items are the closed-loop check, a five-minute EM that stays labeled as standard EM, and papers not yet defended: distillation, ImagenTime as a paper, the two older Koopman autoencoders. Koopman generative operators is still the paper, not this recall.
