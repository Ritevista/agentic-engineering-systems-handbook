# Appendix: Agentic Patterns, Prompting Techniques, and Protocols

## Purpose

This appendix catalogs related patterns, frameworks, tools, and protocols that support the field manual's core primitives.

These topics are useful, but they are not the spine of the field manual. The spine remains structure, steering, skills, agents, subagents, slash commands, hooks, permissions, context and memory, specs/plans/tasks, artifacts, verification, MCP/tools, repository layout, decision frameworks, anti-patterns, portability, and maturity.

Use this appendix to place adjacent terminology without turning every named method or protocol into a new core primitive.

## Classification

| Category | Terms | Where they fit in the field manual |
|---|---|---|
| Methodology/workflow frameworks | BMAD, GSD | Adoption patterns that combine agents, planning artifacts, and structured workflows. |
| Prompt/program standardization | DSPy | Skills, prompt standardization, eval-backed workflows, and verification. |
| Guardrails and boundaries | LLM Guard | Permissions, context boundaries, input/output safety, prompt-injection defense, and verification. |
| Agent reasoning/orchestration patterns | ReAct, Plan-and-Execute, BDI | Agent design, tool use, subagent delegation, planning, and verification. |
| Prompting/reasoning techniques | Zero-shot, few-shot, chain-of-thought, self-consistency, meta-prompting | Prompt design, skill examples, context discipline, reviewable reasoning summaries, and orchestration. |
| Protocols/interoperability | MCP, A2A, AP2, UCP, AG-UI | External capability layers, agent-to-agent interoperability, agent-user interaction, and commerce-specific scenarios. |

## Methodology and workflow frameworks

### BMAD / BMad Method

BMAD should be treated as an AI-driven development methodology. In this field manual, it maps to role-based agents, planning artifacts, and structured workflows.

Do not make BMAD canonical unless the book explicitly adopts it as a Nexus Engineering Control Plane method.

### GSD

GSD should be treated as lightweight/spec-driven agentic development when the term is used in this book. It maps to specs/plans/tasks and verifiable execution.

TODO: Confirm the intended source and meaning of "GSD" before treating it as a named methodology. Define the acronym explicitly before using it in any chapter.

## Prompt/program standardization

### DSPy

DSPy should be treated as a way to program and optimize language-model workflows rather than rely only on hand-written prompts.

In this field manual, DSPy maps to skills, prompt standardization, eval-backed workflows, and verification. It belongs near repeatable workflows that need measurable behavior, not as a replacement for role contracts, repository steering, or human review.

## Guardrails and boundaries

### LLM Guard

LLM Guard should be treated as one possible scanner or guardrail component.

In this field manual, it maps to permissions, context boundaries, input/output safety, prompt-injection defense, and verification.

Scanners do not replace permission boundaries, sandboxing, review, or audit logs. They are detection and filtering components inside a broader control system.

## Agent reasoning and orchestration patterns

### ReAct

ReAct interleaves reasoning and acting. It is useful for tool-using agents that need to inspect state, call tools, observe results, and continue.

In this field manual, ReAct maps to agents, MCP/tools, and verification. Tool actions still need contracts, permissions, auditability, and evidence.

### Plan-and-Execute

Plan-and-Execute separates planning from execution. It is useful for complex engineering tasks where a plan should be reviewed, decomposed, or delegated before work begins.

In this field manual, Plan-and-Execute maps to specs/plans/tasks, agents, subagents, and verification.

### BDI

BDI can be used as a mental model for agent design:

- Belief = what the agent treats as true.
- Desire = the goal or desired outcome.
- Intention = the committed plan of action.

Use BDI as a design lens, not as a mandatory implementation model.

## Prompting and reasoning techniques

### Zero-shot

Zero-shot prompting uses no examples. It is useful for exploration and simple tasks.

Zero-shot prompting is weak for repeatable team workflows because behavior is usually less constrained than a skill, template, spec, or command.

### Few-shot

Few-shot prompting includes examples. It is useful when output format or behavior must be shaped.

Stable few-shot examples may belong in skills or templates so teams can version, review, and reuse them.

### Chain-of-thought / CoT

Chain-of-thought is a reasoning technique for complex tasks.

Do not require raw chain-of-thought as a durable artifact. Prefer reviewable reasoning summaries, assumptions, trade-offs, plans, and evidence.

### Self-consistency

Self-consistency generates or compares multiple reasoning paths or candidate answers.

Use disagreement as a risk signal. Do not treat consensus as proof.

### Meta-prompting

Meta-prompting operates at the orchestration or scaffolding level.

In this field manual, it maps to slash commands, skills, subagents, and Plan-and-Execute workflows.

## Protocols and interoperability

### MCP

MCP is the agent-to-tool/context capability layer. It is core to the field manual's MCP/tools chapter.

### A2A

A2A is an agent-to-agent interoperability protocol. It is useful when separate agents need to discover capabilities or collaborate across boundaries.

### AP2

AP2 is an agent payments protocol. It is commerce/payment-specific and should remain appendix-level unless Nexus later includes commerce workflows.

### UCP

UCP refers here to Universal Commerce Protocol in the Google/commerce context. It is commerce-specific and should remain appendix-level unless the book discusses agentic commerce.

### AG-UI

AG-UI is an agent-user interaction protocol. It is useful when agent backends need to connect to user-facing applications.

## How to use these topics in the main chapters

| Main chapter | Related patterns to mention |
|---|---|
| Core Vocabulary | ReAct, BDI, DSPy, LLM Guard, MCP, A2A |
| Agents | ReAct, Plan-and-Execute, BDI |
| Skills | DSPy, few-shot examples, prompt standardization |
| Slash Commands | Meta-prompting, orchestration |
| Permissions / Approvals / Sandboxing | LLM Guard, prompt injection, data boundaries |
| Context / Memory | Zero-shot, few-shot, context discipline |
| Specs / Plans / Tasks | Plan-and-Execute, GSD |
| Verification | Self-consistency, evals, DSPy metrics |
| MCP / Tools | MCP, A2A, AG-UI |
| Portability | A2A, AG-UI, DSPy, protocol mapping |
| Maturity Model | BMAD, GSD, adoption patterns |

## References and Further Reading

These appendix-specific references should be reconciled with the repository's curated catalog in `../references/bibliography.md` as chapters mature.

### Methodology and workflow frameworks

- BMad Method official documentation - https://docs.bmad-method.org/
- BMad Method GitHub repository - https://github.com/bmad-code-org/bmad-method
- TODO: Confirm the intended meaning/source of "GSD" before treating it as a named methodology. If used, define it explicitly as lightweight/spec-driven agentic development and cite the exact source.

### Prompt/program standardization

- DSPy official documentation - https://dspy.ai/
- DSPy GitHub repository - https://github.com/stanfordnlp/dspy
- DSPy Stanford HAI overview - https://hai.stanford.edu/research/dspy-compiling-declarative-language-model-calls-into-state-of-the-art-pipelines

### Guardrails and boundaries

- LLM Guard official page - https://protectai.com/llm-guard
- LLM Guard GitHub repository - https://github.com/protectai/llm-guard

### Agent reasoning and orchestration patterns

- ReAct paper: "ReAct: Synergizing Reasoning and Acting in Language Models" - https://arxiv.org/abs/2210.03629
- LangChain Plan-and-Execute agents article - https://www.langchain.com/blog/plan-and-execute-agents
- BDI reference: "BDI Agents: From Theory to Practice" - https://link.springer.com/chapter/10.1007/3-540-49057-4_1

### Prompting and reasoning techniques

- Chain-of-thought paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" - https://arxiv.org/abs/2201.11903
- Self-consistency paper: "Self-Consistency Improves Chain of Thought Reasoning in Language Models" - https://arxiv.org/abs/2203.11171
- Meta-prompting paper: "Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding" - https://arxiv.org/abs/2401.12954
- TODO: Add a stable reference for zero-shot and few-shot prompting, preferably from an official model provider guide or a survey paper.

### Protocols and interoperability

- Model Context Protocol official documentation - https://modelcontextprotocol.io/docs/getting-started/intro
- Model Context Protocol GitHub organization - https://github.com/modelcontextprotocol
- A2A Protocol official documentation - https://a2a-protocol.org/latest/
- A2A Protocol specification - https://a2a-protocol.org/v0.3.0/specification/
- AP2: Agent Payments Protocol documentation - https://ap2-protocol.org/
- Google announcement for AP2 - https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- Universal Commerce Protocol on Google - https://developers.google.com/merchant/ucp
- Universal Commerce Protocol specification repository - https://github.com/universal-commerce-protocol/ucp
- AG-UI official documentation - https://docs.ag-ui.com/introduction
- AG-UI GitHub repository - https://github.com/ag-ui-protocol/ag-ui
