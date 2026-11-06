# Meeting cheat sheet — Michael

Sat 7 Nov 2026, 00:05–00:30 Thailand. Fri 6 Nov, 09:05–09:30 Pacific. Twenty-five minutes. Say “I.”

| | |
|---|---|
| **Who** | Michael. Hiring manager Elad Kravi contacted. Last name is not in the intro. |
| **Role** | Research Scientist, Multi-Modal Understanding & Synthesis. Req `2010995136240732`. |
| **Location on the posting** | Pittsburgh, plus one unnamed site. |
| **Order** | Intro, then stop. Q1. Q3. Location only after the research is warm. Next step. Siemens only if he has said there is a path. |

## Do not

- Claim large-scale video world models, human-behavior simulation, or model-based RL.
- Claim you pretrained a frontier multimodal model.
- Open with the table. Baseline first, then the two numbers, only if he asks.
- Open with the group, the student count, or “research leadership.”
- Open with location, leave dates, or Siemens.
- Name Apple or any other process. Siemens only in the script below, and only after he has said there is a fit.
- Attach a CV or explain the calendar.

## Intro — say this, then stop

I’m an Associate Professor of Computer Science at Ben-Gurion University. I’m on leave, based in the Seattle area, and I’m looking for a hands-on research-scientist role.

My work is generative modeling and representation learning for sequential data. One line is diffusion: efficient generation, and using structure in the dynamics. The more recent line is multimodal: how a vision-language model reasons about a sequential signal when I present it through different visual representations.

The thread is learning representations of dynamical processes that support prediction and generation, which is why the world-model side of this role is interesting to me.

I publish at NeurIPS, ICLR, and ICML, and I still design, train, and evaluate the models myself.

I’d like to hear what the team is working on, and where you see the hardest open problems.

## If he wants one project

Charts and delay embeddings of the same series, fused into Qwen3-VL-8B. The chart goes through the native ViT. The delay embedding goes through DINOv3 and a projector. Stage A is perception, with the language model frozen. Stage B is the downstream task, with LoRA. Charts support numerical reasoning. Delay embeddings capture dynamical structure. Either view alone loses information.

Numbers, only if asked. Name the baseline first.

Stock Qwen3-VL-8B, no time-series stack: TSExam-HF **0.618** (n=746), TSRBench overall **0.402** (n=4125). The 3-epoch stack on that same backbone: **0.905** and **0.452**.

## Three connections — use the one he is on

**World models.** Latent dynamics, Koopman models, sequential disentanglement, generative models of trajectories. The question is a representation that captures the dynamics, so it supports prediction and generation, rather than only reconstructing observations. You have not trained large-scale video world models of human behavior. Say that if he asks.

**Multimodal.** Same signal, two visual representations, complementary rather than redundant. Early versus late fusion and whether the model actually uses both views are the discussion, if he goes there.

**Generative.** ImagenTime: an invertible map from a series to an image, then an image diffusion model. Koopman-based distillation to cut the number of sampling steps. Latent diffusion bridges for translation between modalities.

## Questions — this order

**Q1.** The role emphasizes multimodal understanding and world models. How do those connect on your team, and what are you actually pursuing now?

Listen for video and human behavior, and for whether the model is for prediction, generation, planning, or all three.

**Q3.** Where would more expertise change the work: representation learning, temporal reasoning, generative modeling, fusion, or evaluation?

**Location, after the research is warm.** The posting lists Pittsburgh and another location. I’m in Seattle. Is there flexibility for this team?

**Close.** Do you see a fit with this team, or with another group at Meta? If so, what is the next step, and what does the timing look like?

Skip unless he opens the door: how the team is organized, how much of the work is open research versus product, and whether he wants people who have scaled video foundation models.

## If he asks

**Have you worked on world models?** Closely related problems: latent representations of dynamical systems, how those states evolve, and generating trajectories. Koopman models and sequential disentanglement are the relevant work. I have not trained large-scale video world models. A lot of the research questions are the same: what to predict, what supports planning rather than reconstruction, and how to separate predictable dynamics from noise.

**Foundation models?** Hands-on adaptation of Qwen3-VL-8B: architecture, LoRA, ablations, official-protocol eval. Stronger at developing and adapting models than at pretraining one from scratch.

**Why leave academia?** The questions I want now, multimodal foundation models and predictive representations, need a different scale of experiment and collaboration.

**Why Meta?** Foundational multimodal and generative work, at a scale where those questions can be asked together.

**What do you want to work on?** How multimodal models represent dynamic environments, and how to make those representations useful for prediction, reasoning, and possibly planning.

**Leave, only if he asks.** Unpaid leave since 1 October 2026, through October 2027. I can start once an offer is accepted, and I would resign then. Students stay at the university.

**Leadership, only if he asks.** I have defined directions and taken them from a hypothesis through implementation, experiments, and publication, and I have stayed in the architecture, the training, and the eval. NeurIPS 2025 work includes Koopman distillation, irregular series, data-scarce modeling, and latent diffusion bridges. Do not inventory the group.

## Siemens — only after he says there is a path

Do not use this to open, and do not use it if the fit is still unclear.

Just to give you some context on timing, I’m in the final stages of another research opportunity, and the feedback has been very positive. Meta is particularly interesting to me because of the research directions and the scale. If you think there might be a fit, I would like to explore it, and it would help to understand the timeline.

If he asks which company: Siemens, a scientific machine learning research role.

If he asks about an offer: no formal offer. The process has gone well, and I expect more clarity soon.

If he asks about timing: I expect it to move over the next couple of weeks. I would like to understand Meta before I decide.

Do not claim an offer. Do not give him a deadline.

## Close

If he sees a fit: I can see a connection between the questions you described and the ones I have been working on. What would you suggest as the next step?

If the fit is unclear: I would also be interested in other Meta groups on multimodal learning, generative models, or predictive representations. If another group is a better match, I would appreciate the suggestion.

## Remember

1. Lead with generative modeling and multimodal representations. Time series is the domain those methods were built on.
2. World models are the bridge, through predictive dynamics. They are not a video-world-model claim.
3. Be concrete: Qwen3-VL-8B, DINOv3, LoRA, chart versus delay, and the stock baseline before either number.
4. Get his map of the team before a second project.
5. Siemens is the last item, and only if he has already said there is something to explore.
