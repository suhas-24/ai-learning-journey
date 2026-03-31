# Resources By Phase

Use this page when you want the smallest set of resources that still explains a phase well. The goal is not to read everything. The goal is to understand the ideas deeply enough that the rest of the journey feels less mysterious.

For each phase below, the resource picks are ordered from concept-first to practice-supporting.

## Phase 1: Python Foundations And Build Discipline

This phase is about learning the basic building blocks of software work. You are learning how to name things, organize files, run commands, and keep a small project understandable.

- [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) teaches the basic vocabulary for models, training, and evaluation in plain language.
- [tools/python-foundation-tools.md](./tools/python-foundation-tools.md) shows how to keep a Python project tidy, repeatable, and easy to check.
- [people/model-builders-and-research-explainers.md](./people/model-builders-and-research-explainers.md) helps when you want a hard idea explained slowly and clearly.

## Phase 2: LLM APIs, Prompting, And Model Behavior

This phase is about learning how to talk to a model and how to turn a single model answer into something you can depend on.

`LLM` means large language model. `API` means a structured way for one program to send a request to another.

- [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) teaches the first pass on prompts, API calls, and structured outputs.
- [tools/model-api-tools.md](./tools/model-api-tools.md) explains the surrounding machinery, such as messages, streaming, and output shape.
- [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) explains why one good answer is not the same as a reliable product.
- [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) helps you understand model changes without hype.

## Phase 3: Spec-Driven Development

This phase is about making instructions, outputs, and rules explicit so people and tools can check them.

- [courses/prompting-and-api-basics.md](./courses/prompting-and-api-basics.md) gives practice writing clearer instructions.
- [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) shows how those instructions fit into a dependable workflow.
- [tools/python-foundation-tools.md](./tools/python-foundation-tools.md) reinforces typed interfaces, linting, and command-line discipline.
- [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) shows how experienced builders turn vague ideas into reliable boundaries.

## Phase 4: Model Context Protocol (MCP), Command-Line Agents, And Tool Boundaries

This phase is about controlled actions. A model is useful only when it can ask for tools in a safe, explicit way.

`MCP` is a protocol for exposing tools in a structured way. `Command-line` means working through typed commands instead of buttons.

- [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) explains tools, boundaries, handoffs, and workflow state.
- [courses/orchestration-and-agents-courses.md](./courses/orchestration-and-agents-courses.md) shows how model calls and tools fit into one path.
- [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) gives practical examples of command-line and agent workflows.

## Phase 5: Retrieval-Augmented Generation (RAG) And GraphRAG

This phase is about making answers grounded in evidence instead of guessing from memory.

`RAG` means retrieval-augmented generation: find evidence first, then answer. `GraphRAG` adds relationships between entities so retrieval can use both text and connections.

- [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) connects retrieval, grounding, and system design.
- [courses/rag-and-retrieval-courses.md](./courses/rag-and-retrieval-courses.md) explains chunking, embeddings, retrieval, and failure modes.
- [tools/retrieval-data-tools.md](./tools/retrieval-data-tools.md) shows what vector stores, indexing tools, and graph retrieval systems actually do. A `vector store` is a database for meaning-based text search.
- [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) helps when new retrieval ideas need careful interpretation.

## Phase 6: Agentic IDEs And AI-Native Development Loops

This phase is about using AI inside the development workflow without losing control of the codebase.

An `IDE` is an integrated development environment, which means the app where you write and inspect code.

- [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) helps you think about agent workflow shape.
- [people/tool-builders-and-practical-operators.md](./people/tool-builders-and-practical-operators.md) shows how practitioners prompt, review diffs, and keep oversight.
- [newsletters/weekly-signal-scanners.md](./newsletters/weekly-signal-scanners.md) is enough to stay aware of editor and workflow changes.

## Phase 7: Orchestration, State, And Harnesses

This phase is about workflows that remember what happened, check their own work, and recover from failure.

A `harness` is the system around the model or agents that keeps the workflow organized and safe.

- [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) explains how a model becomes part of a larger workflow.
- [courses/orchestration-and-agents-courses.md](./courses/orchestration-and-agents-courses.md) gives concrete examples of step-by-step workflows, branching workflow graphs, and multi-role agent systems.
- [tools/agent-orchestration-tools.md](./tools/agent-orchestration-tools.md) helps you choose the right orchestration style for branching and checkpoints.

## Phase 8: Guardrails, Sandboxing, And Security

This phase is about limiting harm. Safety is not one check; it is a stack of checks that happen before, during, and after the model acts.

- [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) explains why safety is a systems problem.
- [tools/deployment-and-safety-tools.md](./tools/deployment-and-safety-tools.md) covers validation, sandboxing, isolation, and policy controls. `Sandboxing` means running risky code in a contained place.
- [people/systems-thinkers.md](./people/systems-thinkers.md) and [newsletters/strategy-policy-and-ecosystem.md](./newsletters/strategy-policy-and-ecosystem.md) add broader risk context.

## Phase 9: Evals, Monitoring, And Observability

This phase is about measurement. If you cannot see what changed, you cannot know whether the system improved.

`Observability` means you can see what happened during a real run, not just whether the final answer looked good.

- [courses/evals-and-mlops-courses.md](./courses/evals-and-mlops-courses.md) turns quality into datasets, metrics, and comparisons.
- [tools/evals-observability-tools.md](./tools/evals-observability-tools.md) explains tracing, prompt versioning, and RAG evaluation. `Tracing` means recording the step-by-step path of one run.
- [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) gives the operational mindset behind drift and iteration. `Drift` means the data or user behavior changes over time, so old assumptions stop holding.

## Phase 10: Finetuning And Model Internals

This phase is about what changes inside a model when you train it further.

`Fine-tuning` means training a base model again on your own examples so it improves on one narrow task.

- [books/model-internals-and-finetuning.md](./books/model-internals-and-finetuning.md) explains attention, optimization, data shaping, and weight updates. In plain language, this means how the model focuses, learns, and changes during training.
- [people/model-builders-and-research-explainers.md](./people/model-builders-and-research-explainers.md) helps when the math or training story feels dense.
- [newsletters/technical-analysis-and-research-interpretation.md](./newsletters/technical-analysis-and-research-interpretation.md) helps separate real progress from shallow summaries.

## Phase 11: Portfolio, Positioning, And Storytelling

This phase is about explaining your work clearly so other people can see the decisions behind it.

- [books/ml-foundations-and-thinking.md](./books/ml-foundations-and-thinking.md) and [books/ai-engineering-and-llm-systems.md](./books/ai-engineering-and-llm-systems.md) help you talk about tradeoffs and outcomes.
- [people/systems-thinkers.md](./people/systems-thinkers.md) helps you borrow clear systems language.
- [newsletters/weekly-signal-scanners.md](./newsletters/weekly-signal-scanners.md) helps your story stay current without becoming jargon-heavy.

## Cross-Reference

- Master index: [README.md](./README.md)
- Books: [books/README.md](./books/README.md)
- Courses: [courses/README.md](./courses/README.md)
- Tools: [tools/README.md](./tools/README.md)
- People: [people/README.md](./people/README.md)
- Newsletters: [newsletters/README.md](./newsletters/README.md)
