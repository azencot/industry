# Apple — Agentic AI Researcher

Meeting with Miriam Farber | November 2026

| | |
|---|---|
| **Role** | Agentic AI Researcher |
| **Location** | Herzliya, Israel |
| **Role ID** | 200690118-0865 |
| **Who** | Miriam Farber, hiring manager |

## 1. Primary objectives

Determine three things:

1. **Seniority.** Is this an ICT4, ICT5, or potentially ICT6 position? Is there flexibility for a senior research hire?
2. **Scope.** Is this a research leadership opportunity with ownership of technical direction, or primarily an individual contributor role implementing existing ideas?
3. **Location.** Is there flexibility to work remotely from Seattle, potentially with periodic visits to Israel? Could the role be based in Apple’s Seattle organization?

Secondary objectives:

- Understand the team, its maturity, and its relationship to other Apple AI/ML groups.
- Determine how much of the work involves original research versus product engineering.
- Understand the expected timeline and hiring process.

## 2. Introduction (60–90 seconds)

“I’m currently an Associate Professor of Computer Science at Ben-Gurion University, where I lead a research group working on generative modeling, sequential learning, and, more recently, multimodal foundation models.

Over the past couple of years, we’ve been increasingly focused on connecting visual representations with language models, particularly for reasoning over sequential data. My recent work has been quite hands-on, including model architecture, fine-tuning, and evaluation.

I’m currently on leave from the university and exploring opportunities to bring this research into industry, particularly where there’s room to develop new ideas while working toward real products.

Your team’s work caught my attention because of the combination of multimodal reasoning, visual understanding, and agentic systems. I’d love to hear more about what you’re building and where you see the biggest research challenges.”

## 3. Technical fit — what to emphasize

Strongest connections to the role:

### A. Multimodal VLM research

- Recent project: Qwen3-VL-8B with two complementary visual representations of time series.
- Chart representations capture numerical information; delay embeddings capture transformed dynamics.
- Hands-on experience with DINO, LoRA fine-tuning, multimodal alignment, and evaluation.
- Research question: How can we determine which representation is best for a given reasoning task?

### B. Visual tokenization and representation

- Direct connection to the job description’s interest in efficient visual tokenization.
- Experience studying how representations affect downstream reasoning.
- Potential relevance to adaptive perception and efficient visual processing.

### C. Sequential and temporal modeling

- Extensive background in sequential learning and temporal dynamics.
- Natural connection to video understanding, temporal grounding, and agent memory.
- Experience with state-space models and structured temporal representations.

### D. Generative modeling

- Diffusion models, generative modeling, and representation learning.
- Multiple NeurIPS/ICLR publications.
- Experience moving from theoretical ideas to working model implementations.

**Important limitation.** My strongest experience is in multimodal foundation models and sequential reasoning, rather than deployed autonomous agent systems.

Position this as an opportunity to contribute complementary expertise, not as existing production-agent experience.

## 4. Questions — research scope

Start here to understand the opportunity.

### Q1. Team mission

“Could you tell me a little about the team and what you’re trying to build? What are the main research challenges you’re currently facing?”

Follow-ups:

- Is the team building a general-purpose visual agent framework or agents for specific applications?
- Are the main challenges in perception, planning, reasoning, tool use, or evaluation?
- What capabilities are missing from current VLMs?

### Q2. Research versus engineering

“How much of the role involves developing new research ideas versus integrating and adapting existing models into products?”

Follow-ups:

- Is there room to propose new architectures or research directions?
- Are researchers expected to own projects from initial research through deployment?
- Is publishing encouraged?

### Q3. Technical ownership

“How are research directions typically determined? Would someone joining at a senior level have the opportunity to define and lead a research direction?”

Look for:

- Independent research agenda.
- Technical leadership across projects.
- Opportunities to mentor researchers and engineers.
- Influence over architecture and long-term strategy.

### Q4. Success criteria

“What would success look like for someone joining this team over the first 6–12 months?”

This helps distinguish research leadership from execution-focused engineering.

## 5. Questions — seniority and level

Apple’s ICT levels are not stated in the job description.

Primary question:

“Given my background leading an academic research group and my interest in taking ownership of substantial research directions, I’m curious how you’re thinking about the seniority of this position.”

Then:

“Is the position targeted at a particular ICT level, or is there flexibility depending on the candidate?”

If needed:

“Would you consider someone at the ICT5 level, potentially with broader technical leadership responsibilities?”

What to establish:

- Target ICT level.
- Whether ICT5 is genuinely within scope.
- Whether ICT6 is possible or requires a different opening.
- Expectations for technical leadership.
- Whether the role has an independent research mandate.

**Important.** Do not assume that an academic Associate Professor automatically maps to ICT5/ICT6. Focus on the responsibilities and expected impact.

## 6. Questions — remote work / Seattle

Discuss after establishing technical fit and seniority.

Suggested transition:

“There’s also one practical consideration I’d like to understand. I’m currently based in the Seattle area, although I maintain strong ties to Israel.”

Primary question:

“How much flexibility does the team have regarding location? Would it be possible to contribute from Seattle, with periodic visits to Herzliya?”

Follow-up if necessary:

“Does the team collaborate with Apple researchers in the US? I’m wondering whether there might be an option to be formally based in Seattle while working closely with your team.”

If remote is not possible:

“Is that a team-specific requirement, or something that might be flexible for the right candidate?”

If the answer is firmly no:

“I understand. The research direction sounds interesting, so I’d still be happy to stay in touch, particularly if opportunities involving the US teams emerge.”

Do not:

- Promise relocation to Israel.
- Suggest that you can regularly commute internationally without understanding the expectations.
- Negotiate a specific remote arrangement before determining whether the team is interested.

## 7. Questions — team and organization

Choose one or two depending on time.

- “How large is the team, and what’s the balance between researchers and engineers?”
- “Is this a new initiative, or an established team expanding its capabilities?”
- “How closely does the team collaborate with Apple’s broader foundation-model and vision research groups?”
- “Where does the team have the most freedom to innovate independently?”
- “What motivated opening this particular position now?”

## 8. Research ideas to discuss if relevant

### Idea A — Adaptive visual representations

Different visual representations preserve different information.

Could an agent dynamically choose the appropriate representation based on the question or task?

Potential benefits:

- Improved reasoning accuracy.
- Reduced visual-token consumption.
- Better latency/quality tradeoffs.

Direct connection to efficient visual tokenization and agentic perception.

### Idea B — Temporal representations for video agents

Agents processing video need to reason about events, changes, and temporal dependencies.

Could structured temporal representations improve long-horizon reasoning without requiring every frame to be processed?

Potential connections:

- Temporal abstraction.
- Efficient memory.
- Event-based reasoning.
- Spatio-temporal grounding.

### Idea C — Adaptive computation and routing

Not every query requires a frontier cloud VLM.

Could a lightweight model estimate task complexity or uncertainty and decide when to invoke a stronger model?

Research challenges:

- Reliable confidence estimation.
- Cost/latency/accuracy tradeoffs.
- Privacy constraints.
- Learning effective routing policies.

## 9. Questions to expect

**Why Apple / why industry?**

“I’ve enjoyed building my research group and developing new ideas in academia. What attracts me to industry research is the opportunity to work on larger-scale systems, collaborate closely with strong engineering teams, and see research translate into capabilities that people actually use.”

**Why agentic AI?**

“My recent work has increasingly focused on how foundation models interpret and reason over complex inputs. Agentic systems introduce another interesting dimension: deciding what information to acquire, how to represent it, and what actions to take. I see a natural connection between my work on multimodal and sequential reasoning and these challenges.”

**Have you built agentic systems?**

“My direct experience is stronger in multimodal foundation models than in production agent orchestration. However, I’ve worked extensively on the underlying problems of perception, representation, sequential reasoning, and model adaptation. I think these are important building blocks for reliable visual agents.”

**Are you willing to relocate to Israel?**

“I’m currently established in the Seattle area, so my preference would be to remain based there. I’d be very open to regular collaboration with the team in Israel, including periodic visits. I’d be interested to understand whether there’s flexibility around that.”

## 10. Closing

“This has been very helpful. I see several interesting connections between the team’s direction and my recent work, particularly around multimodal reasoning and efficient visual representations.

From your perspective, do you think my background could be a good fit for what you’re looking for?”

If positive:

“What would be the next step in exploring this further?”

## 11. Post-meeting decision framework

**Strong opportunity**

- ICT5 or higher is possible.
- Meaningful research ownership.
- Team has substantial technical challenges.
- Seattle-based arrangement is feasible.

**Potential opportunity**

- ICT5 possible.
- Strong research fit.
- Location flexibility requires organizational approval.

**Weak opportunity**

- ICT4 only.
- Primarily implementation/integration work.
- Full-time presence in Herzliya required.
- Limited independent research ownership.

## 12. Priorities if time is short

Ask these four questions:

1. “What are the main research challenges the team is trying to solve?”
2. “How much opportunity is there to define and lead independent research directions?”
3. “What seniority level are you targeting, and is there flexibility for ICT5?”
4. “Would a Seattle-based arrangement with periodic visits to Israel be possible?”
