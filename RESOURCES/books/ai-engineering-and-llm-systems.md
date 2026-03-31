# AI Engineering And LLM Systems

This guide covers the books that teach how LLM applications become real systems. The main shift here is moving from "the model answered well once" to "the product behaves predictably across users, inputs, and failures."

If you are new here, a quick translation helps:

- an `LLM` is a large language model, which means a model trained on lots of text so it can continue text in useful ways
- a `token` is one small piece of text the model works with
- `embeddings` are number-based representations of meaning
- a `retrieval system` finds the right information before the model answers
- an `eval` checks whether the system is actually getting better

## AI Engineering by Chip Huyen

### What this book teaches

This book teaches AI engineering as a discipline of feedback loops, system boundaries, and production tradeoffs. It is useful because it treats prompts, data, evals, deployment, and user trust as one connected problem.

### Major topics and subtopics

- Problem framing: defining a useful task, success criteria, and failure boundaries.
- Model behavior: understanding capability, inconsistency, and why outputs change with context.
- Prompt and context design: instruction quality, examples, constraints, retrieval context, and output shaping.
- Data and feedback loops: collecting examples, building datasets, and using user interactions to improve the system.
- Evaluation: qualitative review, task-specific metrics, test sets, regression checks, and offline versus online evaluation.
- Production tradeoffs: latency, cost, reliability, fallback strategies, and rollout discipline.

### When to use it

- Use it in Phase 2 when raw API usage starts to feel easy but product design still feels fuzzy.
- Revisit it in Phases 7 to 9 when orchestration, evals, and monitoring begin to matter.
- Use it in Phase 11 when you need portfolio language that explains decisions rather than just features.

### Best companion resources

- [../courses/prompting-and-api-basics.md](../courses/prompting-and-api-basics.md)
- [../tools/model-api-tools.md](../tools/model-api-tools.md)
- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)

## Hands-On Large Language Models by Jay Alammar and Maarten Grootendorst

### What this book teaches

This book teaches the bridge between intuition and implementation. It is especially good when you can call a model but do not yet have a clean mental model for embeddings, tokenization, semantic search, and generation behavior.

`Tokenization` means splitting text into the small pieces the model actually sees. That matters because the model does not read your sentence the way a person does.

### Major topics and subtopics

- Tokenization and representation: how text becomes tokens and why token boundaries matter.
- Embeddings: semantic similarity, dense vectors, clustering intuition, and search behavior.
- Generation patterns: decoding, prompting, structured output, and model variability.
- Retrieval workflows: vector search, context injection, and answer grounding.
- Application patterns: simple LLM pipelines, task decomposition, and experimentation loops.

### When to use it

- Use it in Phase 2 for API fluency with stronger intuition.
- Reuse it in Phase 5 when RAG concepts need a more grounded explanation.
- Skim it in Phase 10 if you want a gentler lead-in before deeper model internals.

### Best companion resources

- [../courses/rag-and-retrieval-courses.md](../courses/rag-and-retrieval-courses.md)
- [../tools/retrieval-data-tools.md](../tools/retrieval-data-tools.md)

## The LLM Engineering Handbook

### What this book teaches

This book teaches application architecture. It helps you see an LLM system as a composition of ingestion, retrieval, tool use, control flow, evaluation, and deployment choices rather than one prompt wrapped in a web app.

An `orchestration loop` is the repeatable path the system follows when it plans, acts, checks the result, and decides whether to continue. That loop is what turns a single model call into a dependable workflow.

### Major topics and subtopics

- LLM system architecture: services, interfaces, request flow, and operational boundaries.
- Retrieval design: chunking, embeddings, indexing, re-ranking, and context assembly.
- Agent patterns: tool use, planning, state, iterative loops, and delegation.
- Production constraints: latency budgets, maintainability, logging, and debugging.
- Deployment discipline: staging, measurement, and change management.

### When to use it

- Best in Phase 5 when you start retrieval systems.
- Strong again in Phase 7 when orchestration and harness design become central.
- Useful in Phase 9 when you need observability attached to application structure.

### Best companion resources

- [../tools/retrieval-data-tools.md](../tools/retrieval-data-tools.md)
- [../tools/agent-orchestration-tools.md](../tools/agent-orchestration-tools.md)
- [../by-phase.md](../by-phase.md)

## Building LLMs For Production

### What this book teaches

This book teaches what changes once a system has users, uptime expectations, and business consequences. The key lesson is that "working" is not the same as "operating well."

### Major topics and subtopics

- Reliability engineering: failure handling, retries, fallbacks, and graceful degradation.
- Observability: tracing, logs, prompt versioning, and issue isolation.
- Performance and cost: response time, throughput, caching, and budget discipline.
- Release safety: evaluation gates, staging environments, and controlled rollout.
- Team operations: repeatable workflows for debugging, measuring, and improving.

### When to use it

- Phase 7 for harness and workflow discipline.
- Phase 8 for governance and operational safety.
- Phase 9 for monitoring, regression detection, and quality control.

### Best companion resources

- [../courses/evals-and-mlops-courses.md](../courses/evals-and-mlops-courses.md)
- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)
- [../tools/deployment-and-safety-tools.md](../tools/deployment-and-safety-tools.md)

## Reading Strategy

- Read one book deeply instead of skimming four at once.
- Extract reusable concepts such as chunking tradeoffs, eval loops, fallback design, and state management.
- When the same idea appears in a book and a tool guide, trust the concept over the framework branding.
