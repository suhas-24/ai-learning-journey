# Resources By Phase

Use this file when you want the minimum useful reading and tooling for a specific phase. Each phase lists the resources that teach the core ideas fastest, plus why they matter at that moment.

If you are new to the field, read the phase name as the topic you are learning, then treat the resource suggestions as support for that topic. The goal is not to collect everything. The goal is to understand one idea well enough to use it.

## Phase 1: Python Foundations And Build Discipline

- Read [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) for the plain-language ideas behind machine learning, model behavior, and why measuring results matters.
- Use [tools/python-foundation-tools.md](./tools/python-foundation-tools.md) to learn project structure, linting, typing, command-line basics, and how to keep a Python project tidy.
- Keep [people/model-builders-and-research-explainers.md](./people/model-builders-and-research-explainers.md) nearby when you want someone to explain hard ideas slowly and clearly.

## Phase 2: LLM APIs, Prompting, And Model Behavior

- Start with [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) because it shows how to talk to a model in a clear, structured way.
- Pair it with [tools/model-api-tools.md](./tools/model-api-tools.md) to understand the pieces around the model, like messages, streaming, and structured responses.
- Read the early sections of [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) to understand why a good answer once is not the same as a reliable product.
- Use [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) when you want model updates explained without hype.

## Phase 3: Spec-Driven Development

- Reuse [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) to practice clear instructions, output rules, and simple response contracts.
- Read [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) for how to turn a good idea into a dependable workflow.
- Use [tools/python-foundation-tools.md](./tools/python-foundation-tools.md) because typed interfaces, linting, and CLI discipline make rules easier to trust.
- Follow [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) for concrete examples of turning language into reliable software boundaries.

## Phase 4: MCP, CLI Agents, And Tool Boundaries

- Read [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) for tool boundaries, handoffs, and how a model gets permission to do something useful.
- Use [courses/orchestration-and-agents-courses.md](./courses/orchestration-and-agents-courses.md) to see how model calls, tools, and workflow state fit together.
- Keep [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) open when you want practical examples of agent tooling and command-line workflows.

## Phase 5: RAG And GraphRAG

- Read [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) for how retrieval, grounding, and system design fit together.
- Use [courses/rag-and-retrieval-courses.md](./courses/rag-and-retrieval-courses.md) for a first pass on chunking, embeddings, retrieval, and why answers can go wrong.
- Pair that with [tools/retrieval-data-tools.md](./tools/retrieval-data-tools.md) so you understand what vector stores, indexing frameworks, and graph retrieval systems actually do under the hood.
- Scan [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) when retrieval patterns or research claims need interpretation.

## Phase 6: Agentic IDEs And AI-Native Development Loops

- Start with [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) for agent workflow thinking, then read the IDE section in [tools/README.md](./tools/README.md) through the linked tool guide.
- Use [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) because this phase benefits from watching practitioners explain how they prompt, review diffs, and keep control of the work.
- Keep [newsletters/weekly-signal-scanners.md](./newsletters/weekly-signal-scanners.md) lightweight here. The goal is to notice meaningful workflow shifts, not chase every editor launch.

## Phase 7: Orchestration, State, And Harnesses

- Read [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) for how a model becomes part of a larger workflow with steps, checks, and retries.
- Use [courses/orchestration-and-agents-courses.md](./courses/orchestration-and-agents-courses.md) to get concrete examples of chains, graphs, role-based agents, and workflow state.
- Pair it with [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) so you learn which orchestration framework to use for branching, checkpointing, and typed outputs.

## Phase 8: Guardrails, Sandboxing, And Security

- Read the production and governance parts of [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) to understand why safety is a systems problem, not just a moderation call.
- Use [tools/deployment-and-safety-tools.md](./tools/deployment-and-safety-tools.md) to learn validation, sandboxing, isolation, and policy enforcement.
- Read [people/systems-thinkers.md](./people/systems-thinkers.md) and [newsletters/strategy-policy-and-ecosystem.md](./newsletters/strategy-policy-and-ecosystem.md) when you need safety context that connects engineering with real-world risk.

## Phase 9: Evals, Monitoring, And Observability

- Start with [courses/evals-and-mlops-courses.md](./courses/evals-and-mlops-courses.md) because it turns abstract quality ideas into datasets, metrics, regression checks, and experiment tracking.
- Pair it with [tools/evals-observability-tools.md](./tools/evals-observability-tools.md) to learn tracing, prompt versioning, dataset-based testing, and RAG-specific metrics.
- Read [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) for the operational ML mindset behind measurement, drift, and iteration loops.

## Phase 10: Finetuning And Model Internals

- Read [books/model-internals-and-finetuning.md](./books/model-internals-and-finetuning.md) first. It explains attention, optimization, data shaping, and why fine-tuning changes behavior differently than prompting.
- Use [people/model-builders-and-research-explainers.md](./people/model-builders-and-research-explainers.md) when you need hard concepts like training dynamics or representation learning explained clearly.
- Keep [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) for separating genuine model advances from shallow trend summaries.

## Phase 11: Portfolio, Positioning, And Storytelling

- Revisit [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) and [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) to frame your work in terms of decisions, tradeoffs, and measurable outcomes.
- Use [people/systems-thinkers.md](./people/systems-thinkers.md) to strengthen your engineering narrative. The most valuable public voices here model how to explain systems clearly.
- Use [newsletters/weekly-signal-scanners.md](./newsletters/weekly-signal-scanners.md) lightly so your portfolio language reflects the field without becoming jargon-heavy.

## Cross-Reference

- Master index: [README.md](./README.md)
- Books: [books/README.md](./books/README.md)
- Courses: [courses/README.md](./courses/README.md)
- Tools: [tools/README.md](./tools/README.md)
- People: [people/README.md](./people/README.md)
- Newsletters: [newsletters/README.md](./newsletters/README.md)
