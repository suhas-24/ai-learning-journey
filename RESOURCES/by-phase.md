# Resources By Phase

Use this file when you want the minimum useful reading and tooling for a specific phase. Each phase lists the resources that teach the core ideas fastest, plus why they matter at that moment.

## Phase 1: Python Foundations And Build Discipline

- Read [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) for the machine learning vocabulary that keeps later API and evaluation work from feeling magical.
- Use [tools/python-foundation-tools.md](./tools/python-foundation-tools.md) to learn project structure, linting, typing, CLI ergonomics, and container basics.
- Keep [people/model-builders-and-research-explainers.md](./people/model-builders-and-research-explainers.md) nearby when you need fundamentals explained in plain language.

## Phase 2: LLM APIs, Prompting, And Model Behavior

- Start with [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) because it teaches the shape of a prompt, the role of examples, and how API calls become workflows.
- Pair it with [tools/model-api-tools.md](./tools/model-api-tools.md) to understand SDK boundaries, streaming, structured outputs, and local model tradeoffs.
- Read the early sections of [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) to understand why prompt quality alone is not enough for a reliable product.
- Use [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) when you want model updates explained without hype.

## Phase 3: Spec-Driven Development

- Reuse [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) to sharpen instruction writing, output contracts, and structured response design.
- Read [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) for system framing, failure modes, and the difference between a good demo and a dependable workflow.
- Use [tools/python-foundation-tools.md](./tools/python-foundation-tools.md) because typed interfaces, linting, and CLI discipline are what make specs executable instead of vague notes.
- Follow [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) for concrete examples of turning language into reliable software boundaries.

## Phase 4: MCP, CLI Agents, And Tool Boundaries

- Read [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) for MCP SDK, A2A, and `gh` CLI context. The key lesson here is not the syntax. It is how tools expose capabilities safely and predictably.
- Use [courses/orchestration-and-agents-courses.md](./courses/orchestration-and-agents-courses.md) to see how model calls, tools, and workflow state fit together.
- Keep [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) open when you need practical examples of agent tooling and command-line workflows.

## Phase 5: RAG And GraphRAG

- Read [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) for retrieval architecture, chunking tradeoffs, and grounding patterns.
- Use [courses/rag-and-retrieval-courses.md](./courses/rag-and-retrieval-courses.md) for first-pass intuition on chunking, embeddings, evaluation, and retrieval quality.
- Pair that with [tools/retrieval-data-tools.md](./tools/retrieval-data-tools.md) so you understand what vector stores, indexing frameworks, and graph retrieval systems actually do under the hood.
- Scan [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) when retrieval patterns or research claims need interpretation.

## Phase 6: Agentic IDEs And AI-Native Development Loops

- Start with [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) for agent workflow thinking, then read the IDE section in [tools/README.md](./tools/README.md) through the linked tool guide.
- Use [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) because this phase benefits from watching practitioners explain how they prompt, review diffs, and manage agent scope.
- Keep [newsletters/weekly-signal-scanners.md](./newsletters/weekly-signal-scanners.md) lightweight here. The goal is to notice meaningful workflow shifts, not chase every editor launch.

## Phase 7: Orchestration, State, And Harnesses

- Read [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) for system composition, control flow, reliability, and the interaction between prompts, tools, and evaluation.
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
