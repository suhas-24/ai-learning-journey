# AI Engineering And LLM Systems

This guide is for the moment when a model answer stops being enough and you need to think about the full system around it. The big change is moving from "the model answered once" to "the product behaves predictably across users, inputs, and failures."

If some of the vocabulary is new, here is the simple version:

- An `LLM` is a large language model. It reads text and predicts more text.
- A `token` is a small piece of text the model works with.
- `Embeddings` are number-based stand-ins for meaning.
- `Retrieval` means finding useful information before the model answers.
- An `eval` is a test that tells you whether the system is improving.
- An `orchestration loop` is the repeated path a system follows when it plans, acts, checks, and decides what happens next.

## How To Read This Guide

- Start with the book that matches the kind of problem you are trying to solve.
- Read for the idea, not for completion.
- After each chapter, write one sentence about a design decision you would make differently now.

## AI Engineering by Chip Huyen

### What this book teaches

This book explains AI engineering as a system of feedback loops, boundaries, and tradeoffs. It connects prompts, data, evals, deployment, and user trust so you can see why a "good answer" is only one part of a product.

### Core topics and subtopics

- Problem framing: what the task is, what success means, and where the system can fail.
- Model behavior: why output changes with context, wording, and examples.
- Prompt and context design: instructions, examples, constraints, retrieval context, and output shape.
- Data and feedback loops: collecting examples, building datasets, and using real usage to improve the system.
- Evaluation: qualitative review, task metrics, test sets, regression checks, and offline versus online testing.
- Production tradeoffs: latency, cost, reliability, fallback strategies, and release discipline.

### When to use it

- Use it in Phase 2 when raw API usage starts to feel easy but product design still feels fuzzy.
- Revisit it in Phases 7 to 9 when orchestration, evals, and monitoring become central.
- Use it in Phase 11 when you want portfolio language that explains decisions, not just features.

### Watch for

- It is easy to read this book as a list of techniques. The more important lesson is how those techniques connect into one system.

### Best companion resources

- [../courses/prompting-and-api-basics.md](../courses/prompting-and-api-basics.md)
- [../tools/model-api-tools.md](../tools/model-api-tools.md)
- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)

## Hands-On Large Language Models by Jay Alammar and Maarten Grootendorst

### What this book teaches

This book bridges intuition and implementation. It is especially useful when you can call a model but do not yet have a clear mental model for tokenization, embeddings, meaning-based search, and generation behavior.

`Tokenization` means splitting text into the small pieces the model actually sees. That matters because the model does not read your sentence the way a person does.

### Core topics and subtopics

- Tokenization and representation: how text becomes tokens and why token boundaries matter.
- Embeddings: semantic similarity, dense vectors, clustering intuition, and search behavior.
- Generation patterns: decoding, prompting, structured output, and model variability.
- Retrieval workflows: vector search, context injection, and answer grounding.
- Application patterns: simple LLM pipelines, task decomposition, and experimentation loops.

### When to use it

- Use it in Phase 2 for API fluency with stronger intuition.
- Reuse it in Phase 5 when RAG concepts need a more grounded explanation.
- Skim it in Phase 10 if you want a gentler lead-in before deeper model internals.

### Watch for

- This book makes small ideas feel concrete, which is helpful. The risk is stopping at the intuition and never tying it back to product design.

### Best companion resources

- [../courses/rag-and-retrieval-courses.md](../courses/rag-and-retrieval-courses.md)
- [../tools/retrieval-data-tools.md](../tools/retrieval-data-tools.md)

## The LLM Engineering Handbook

### What this book teaches

This book teaches application architecture. It shows how ingestion, retrieval, tool use, control flow, evaluation, and deployment combine into one system instead of one prompt wrapped in a web app.

An `orchestration loop` is the repeatable path the system follows when it plans, acts, checks the result, and decides whether to continue.

### Core topics and subtopics

- LLM system architecture: services, interfaces, request flow, and operational boundaries.
- Retrieval design: chunking, embeddings, indexing, re-ranking, and context assembly.
- Agent patterns: tool use, planning, state, iterative loops, and delegation.
- Production constraints: latency budgets, maintainability, logging, and debugging.
- Deployment discipline: staging, measurement, and change management.

### When to use it

- Best in Phase 5 when you start retrieval systems.
- Strong again in Phase 7 when orchestration and harness design become central.
- Useful in Phase 9 when you need observability attached to application structure.

### Watch for

- If a chapter starts sounding framework-specific, step back and ask what general system idea it is actually teaching.

### Best companion resources

- [../tools/retrieval-data-tools.md](../tools/retrieval-data-tools.md)
- [../tools/agent-orchestration-tools.md](../tools/agent-orchestration-tools.md)
- [../by-phase.md](../by-phase.md)

## Building LLMs For Production

### What this book teaches

This book explains what changes once a system has users, uptime expectations, and business consequences. The key lesson is that "working" is not the same as "operating well."

### Core topics and subtopics

- Reliability engineering: failure handling, retries, fallbacks, and graceful degradation.
- Observability: tracing, logs, prompt versioning, and issue isolation.
- Performance and cost: response time, throughput, caching, and budget discipline.
- Release safety: evaluation gates, staging environments, and controlled rollout.
- Team operations: repeatable workflows for debugging, measuring, and improving.

### When to use it

- Phase 7 for harness and workflow discipline.
- Phase 8 for governance and operational safety.
- Phase 9 for monitoring, regression detection, and quality control.

### Watch for

- The best ideas here are operational. If you only remember the architecture diagrams, you will miss the point.

### Best companion resources

- [../courses/evals-and-mlops-courses.md](../courses/evals-and-mlops-courses.md)
- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)
- [../tools/deployment-and-safety-tools.md](../tools/deployment-and-safety-tools.md)
