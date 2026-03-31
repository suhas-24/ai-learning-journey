# Model API Tools

This guide covers the tools that teach direct interaction with language models. The point is not just calling an endpoint. The point is learning how messages, schemas, streaming, and model tradeoffs shape application behavior.

If you are new, the simplest picture is this: your code sends a request, the model returns text, and your job is to make that exchange predictable enough to build on.

## OpenAI SDK

### What it teaches

The OpenAI SDK teaches structured model interaction: request construction, output shaping, tool use, and provider-level features that affect application design.

### Major topics and subtopics

- Message-based request design.
- Structured outputs and schema-shaped responses.
- Tool calling and application coordination.
- Streaming and partial output handling.

### Best phases

- Phase 2.
- Useful again in Phase 9 for evaluation and testing flows.

## Anthropic SDK

### What it teaches

The Anthropic SDK teaches a slightly different interface philosophy around messages, tool use, and long-context interaction. Comparing it with other providers helps you learn what is model-specific and what is system design.

### Major topics and subtopics

- Message structure and context packing.
- Tool use and structured interaction.
- Streaming response handling.
- Usage awareness and operational constraints.

### Best phases

- Phase 2.

## Ollama

### What it teaches

Ollama teaches local inference tradeoffs. It is useful for understanding privacy, offline workflows, hardware limits, and the difference between cloud APIs and local model serving.

### Major topics and subtopics

- Local model serving.
- Hardware and latency tradeoffs.
- Privacy and offline experimentation.
- Prompt and model comparison under local constraints.

### Best phases

- Phase 2.
- Useful again in Phase 10 when comparing model behavior and adaptation choices.

## Companion Guides

- [../courses/prompting-and-api-basics.md](../courses/prompting-and-api-basics.md)
- [retrieval-data-tools.md](./retrieval-data-tools.md)
- [../people/model-builders-and-research-explainers.md](../people/model-builders-and-research-explainers.md)
