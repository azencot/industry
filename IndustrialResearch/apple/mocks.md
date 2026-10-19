# Ozan mock log

One file for every mock aimed at Ozan Sener. Append a section. Add a row to the index. Do not open a new file per mock.

## Index

| Date | Kind | Focus | Break |
|------|------|-------|-------|
| 2026-10-19 | Technical, ~7 min | KDM, one result he still defends | CIFAR numbers only on the second ask. No one-step teacher control. ImageNet described with no FID. |
| 2026-10-19 | General, ~8 min | Why leave the university | Dodged the job-shape question once. “Technical lead,” then “all of the code.” |

---

## 2026-10-19 — KDM, one result

**Kind:** Technical mock, about seven minutes, four answers. Interviewer was Ozan with Raja’s note only. Answers were not supplied in advance. Stopped when the scaling claim had no number.

**Opening:** Of the work from the last two years, which piece did you build yourself, and which result would you still defend?

### What he said

Offline one-step distillation of a visual diffusion model. The account started from an SDE and a Kolmogorov forward equation: under a time-invariant vector field the equation integrates in one step by a matrix exponential. He called himself the technical lead. The setting he defended was offline: precomputed noise and data endpoints, no trajectory, no further teacher access. He named CIFAR-10 and FFHQ, said ImageNet had not scaled, and said the theory still holds.

Pressed for numbers: KDM FID 4.65 at 1 step, GET 6.91, EDM teacher 2.04 at 35 steps. He then said he had started ImageNet-1k, results were mixed, and compute made him stop.

Asked for the teacher at one step: he did not remember that run, and agreed it would be informative.

Asked for the ImageNet FID and resolution: maybe 128×128, the 1000-class set, overall FID high, some portions better, no pattern he could name, exact numbers gone.

### What landed

The three CIFAR numbers, once asked. Offline was stated as a constraint: endpoints only, teacher weights unused after the pairs exist. He did not invent a one-step teacher FID.

### What broke

- The first answer had no FID and no step count. “Technical lead” is the wrong noun. Say which decision was his.
- 4.65 versus 6.91 compares two students. 4.65 versus 2.04 is the teacher at 35 steps. Neither number is the teacher at one step. Agreeing that the control would be easy does not close it. Say the run was not done.
- ImageNet was described as a run. He could not find those numbers afterward. On a call, say scaling stopped at FFHQ and AFHQv2. The paper also omits ImageNet; an interviewer who has not opened it will not catch that. The failure on the call is quoting a result with no FID.

### Spoken lock

The result I can defend is unconditional CIFAR-10. The EDM teacher is FID 2.04 at 35 steps. My student is 4.65 at one step. GET, the offline method I ran against, is 6.91 at one step. I did not evaluate the teacher at one step, so I do not claim the student beats a truncated teacher. The best online one-step number in that table is CTM at 1.98, and it is better than mine. Scaling in the paper stops at FFHQ and AFHQv2, 64×64, where my FID is about two and a half times the teacher’s.

### Next

CTM at 1.98, and what the offline constraint costs against that online number. Not run in this mock.

---

## 2026-10-19 — why leave the university

**Kind:** General mock, about eight minutes, five answers. No paper. Interviewer was Ozan with Raja’s note: professor, considering industry. Answers were not supplied in advance.

**Opening:** If you left the university, what part of that job are you trying to leave, and what part are you trying to keep?

### What he said

He would leave a compute ceiling. BGU was a good home for six years. He enjoyed scaling the group and widening it across multimodal modeling, generative modeling, and forecasting. Industry would let him compete with better-resourced groups.

Asked whether he would take a job where he writes the code and does not grow a group, he answered with a different pair of reasons: seeing algorithms affect millions of users, and personal reasons to move from Israel to the US.

Asked again, yes or no, he said yes. He described himself as hands-on, then a technical lead, and said he never left that. Being a group director let him run more directions in parallel. The core, he said, stayed a small set of technical problems.

Asked if he would stay on one problem for a year, he said yes, and that the past year was already that: a multimodal time-series reasoning project, new to him, ending in an arXiv preprint submitted to ICLR. He said the group’s other projects continued.

Asked who wrote the training code and how many days a week he ran experiments: Hedi and he wrote all of the code. He was the technical lead, responsible for the architecture and a two-stage training curriculum. Hedi ran ablations. He coded about three days a week on that project.

### What landed

The second yes was direct. Three days a week, the architecture, and the two-stage curriculum are concrete. The move to the US was stated as personal, without a story wrapped around it.

### What broke

- The first answer was about the group. Compute was the only thing he named as the reason to leave. He did not say what he would keep.
- The job-shape question went unanswered the first time. Millions of users and a move to the US were a new subject. “Potentially” and “witness” do not say the job he wants.
- “Technical lead” and “group director” came immediately after he agreed not to build a group. “Director so I could explore more directions” fights the one-problem yes.
- “Hedi and I wrote all of the code” is too closed. The preprint’s equal-contribution authors are Hedi Zisling and Liran Nochumsohn. He will not have the author list in front of him on the call. The sentence is still wrong to practice. Name Liran, or do not say “all.”
- The other two days of the week were never said.

### Spoken lock

I would leave the compute ceiling. I would keep working on one technical problem, and I would take a job where I write the code and train the model without growing a group. This past year was already close to that. About three days a week I worked on one multimodal time-series project that was new to me. I wrote the architecture and the two-stage training curriculum. Hedi wrote code with me and ran the ablations. Liran is an equal-contribution author on that preprint, so I will not say the two of us wrote all of it. The other two days I can account for if you ask.

### Next

The millions-of-users sentence, against a group whose public work is papers and prototypes. Not run in this mock.
