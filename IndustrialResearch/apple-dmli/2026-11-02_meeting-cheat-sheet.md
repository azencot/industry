# Meeting cheat sheet — Nick Foti

November 2, 2026. Keep this file open. Say “I.”

| | |
|---|---|
| **Who** | Nick Foti, Principal Research Scientist, Seattle. Hiring manager. |
| **Role** | Sr ML Research Scientist, AIML Data and ML Innovation. Seattle. Req **200668189-3337**. |
| **Order** | Intro. Then Q1 and Q2. Q4 if his paper comes up. Q3 only if the representation gap comes up. Q5 later. |

## Do not

- Open with Health, Sapiro, Ozan, Shirley, or Yujie.
- Claim a record in mechanistic interpretability or Bayesian inference.
- Claim you pretrained a frontier model.
- Claim the probe-and-patch time-series experiment is done. It is a proposal.
- Treat Masha’s internship post as his req.
- Treat a successful activation patch as proof of scientific reasoning.
- Go past a high-level account of his paper. The derivation and the figures are not ready.

If he asks about a previous Apple loop: full loop with Health AIML, on-site in September, no offer. Stop.

## Intro

I’m an Associate Professor of Computer Science at Ben-Gurion University, and I’ve recently moved to the Seattle area. I’ve been leading a research group focused on machine learning, particularly representation learning, generative models, and sequential data.

A recurring theme in my research has been understanding how representations and inductive biases affect what models can learn. Some of my earlier work was more mathematically motivated, looking at things like Koopman-based models and disentangled representations for dynamical systems.

More recently, I’ve been working with foundation models, particularly on how to introduce new modalities, like time series, into vision-language models. I’m interested not only in improving their performance, but also in understanding why certain representations work better than others.

So I think there’s a natural connection between my earlier research and the questions your team is exploring around understanding and improving foundation models.

## Research Intro

My research has largely focused on representation learning, particularly for sequential and scientific data. A recurring question has been how the structure we impose on a model affects what it learns and what it can do with those representations.

For example, in my work on Koopman-based variational autoencoders, we investigated how to learn nonlinear dynamical systems through latent representations with more structured evolution. I’ve also worked extensively on sequential disentanglement, where the goal is to separate different factors underlying observed sequences.

More recently, I’ve been exploring these questions in foundation models. In one ongoing project, we’re studying how different representations of time-series data can be integrated into vision-language models to improve reasoning about temporal patterns. This involves hands-on model training, multimodal alignment, and controlled evaluation.

What interests me across these projects is not just improving performance, but understanding how representations and learning objectives influence model capabilities. That’s one of the reasons I found the research directions described in this role particularly interesting.

## If the paper comes up

*LLMs are not (consistently) Bayesian* (2026). He is corresponding author. arXiv:2605.06915.

Say:

- The question is whether an LLM’s expressed update matches Bayes given its own prior and likelihoods.
- Consistency and accuracy are different. A correct update of a bad likelihood can predict badly. A good prediction need not be a Bayes update.
- The reference posterior is built from the model’s own elicitations, not from the true data-generating distribution.
- Belief propagation is closer to Bayes. Batch is often less Bayesian and often more accurate on the task.
- The suggested reason is a useful implicit map and a weaker explicit likelihood. That is an interpretation, not a located mechanism.

The gap, if he asks what it is: \(\Delta(q)=D_{\mathrm{KL}}(q\parallel p)\). \(q\) is the elicited post-data distribution. \(p\) is Bayes on the elicited prior and likelihoods. Zero only when they match. You have not derived it.

Number, if you need one. Prior 0.6 and 0.4, likelihoods 0.8 and 0.2, Bayes gives about 0.857. A report of 0.65 disagrees with the model’s own numbers.

Do not open: the ELBO link, under- versus over-updating, wrong-direction updates, the oracle likelihood, or a figure-by-figure tour.

## If he asks how you would test a scientific behavior

Three different claims: the information is encoded, the model uses it, a component implements that scientific relation.

A probe shows the first. A patch shows that the intervention changes the output. It does not show the third. The patched activation may be a shortcut or the answer itself.

Controls if you design one: shortcut points the wrong way, a matched example changes only the surface, and a patch from an unrelated example checks that the effect is specific.

## Projects, if he stays on your work

Order inside each: the question, what you changed, the control, the result.


### KoVAE — Koopman Variational Autoencoders (ICLR 2024)

In KoVAE, we were interested in understanding how the prior distribution of a sequential VAE affects the representations it learns, particularly whether introducing a specific inductive bias about the underlying dynamics could improve generative modeling. Existing approaches typically used either nonsequential priors or more general sequential priors, often based on Gaussian transitions. Our idea was motivated by Koopman theory, which tells us that nonlinear dynamical systems can be studied through linear evolution in a higher-dimensional space of observables. So we asked whether imposing linear dynamics in a learned latent space could provide a useful inductive bias, even when the observed dynamics are highly nonlinear. We developed a VAE with a Koopman-structured sequential prior and evaluated it against nonsequential and general sequential alternatives. Importantly, we controlled for architecture, parameter count, and optimization to isolate the effect of the prior. Across datasets with different degrees of nonlinearity, we observed a consistent progression: sequential priors improved over nonsequential ones, and the linear-dynamics prior improved further. For me, the interesting takeaway was that relatively simple mathematical structure, when imposed in an appropriate representation space, can substantially improve a model’s ability to learn complex temporal distributions.

### Dual-Time — Multimodal Time-Series Reasoning with Vision-Language Models (2026)

In my recent work, I’ve been investigating how to introduce time-series data into foundation models, particularly vision-language models. The main question that interested me was how the choice of representation affects what a pretrained model can learn and reason about. Most existing approaches represent time series as text or use dedicated encoders, but we explored whether we could leverage the visual capabilities that foundation models already have. Our hypothesis was that complementary visual representations of the same signal could improve reasoning by exposing different properties to the model. We focused on two views: conventional charts, which make numerical values and trends accessible, and delay embeddings, which expose geometric and dynamical properties of the signal. We then designed controlled question-answering tasks targeting numerical and dynamical properties and compared complementary chart–delay inputs against redundant chart–chart and delay–delay inputs. We consistently found that combining the two different views performed better, while each individual representation had its own strengths. What I find particularly interesting is that both views come from the same underlying signal, so we’re not necessarily introducing new information. Instead, we’re changing how that information is presented to a pretrained model, and our results suggest that this can significantly affect what the model is able to extract and use.

## Ask

1. **Agenda.** What are the main research questions your team is currently pursuing around understanding foundation models in scientific domains?
2. **Needs.** Given the team’s current expertise, what kind of research background or perspective would you most like to add?
3. **Masha’s post, only if the gap comes up.** I saw Masha’s post about the gap between what models represent internally and what they express. Is understanding how early training shapes this gap one of your team’s main research directions?
4. **His paper.** How does your recent work on probabilistic consistency and Bayesian belief updating connect to the team’s broader research agenda?
5. **Later.** How much freedom do researchers have to define their own research questions, and what would success look like after the first year?

Optional, if the conversation is already there:

- Studying existing models, or also new training methods?
- Represented, versus actually used?
- How do synthetic controls carry to a large pretrained model?
- Fundamental research and product?


## Research challenges

There are two research directions I’m particularly excited about, and both connect to my previous work on representation learning.

The first is understanding why and when different representations work better for foundation models. In our recent multimodal work, we found that the representation of the same underlying time series can significantly affect reasoning performance. But that raises a more fundamental question: what makes a particular representation effective for a given model and task? I’d like to investigate that, potentially by looking at what information is accessible in the model’s internal representations. And a more ambitious direction would be to automatically select or construct the most effective representation based on the task and model architecture.

The second direction is bringing domain-specific inductive biases back into foundation models. Much of my earlier research, particularly on Koopman-based models, explored how mathematical structure can improve learning. Modern foundation models are remarkably flexible, but they don’t necessarily incorporate the physical or dynamical structure of scientific problems explicitly. I’d be interested in exploring whether we can introduce that structure through representations, training objectives, or architectural components. For example, what would a physics-informed vision-language model look like, and would it generalize better to dynamical systems it hasn’t encountered during training?

What connects these directions is a broader question I’ve been interested in throughout my research: how do representations and inductive biases shape what models can learn and reason about?


