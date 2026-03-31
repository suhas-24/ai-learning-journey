# Model API Tools

This guide covers the tools that teach direct interaction with language models. The point is not just calling an endpoint. The point is learning how messages, schemas, streaming, and model tradeoffs shape application behavior.

If you are new, the simplest picture is this: your code sends a request, the model returns text, and your job is to make that exchange predictable enough to build on.

## How To Use This Guide

- Start here when you want to move from prompt writing to actual application calls.
- Pay attention to the shape of the request and the shape of the response.
- Compare providers so you can see which parts are model-specific and which parts are general software design.

## OpenAI SDK

### What it teaches

The OpenAI SDK teaches structured model interaction: request construction, output shaping, tool use, and provider-level features that affect application design.

### Core topics and subtopics

- Message-based request design.
- Structured outputs and schema-shaped responses.
- Tool calling and application coordination.
- Streaming and partial output handling.

### Best phases

- Phase 2.
- Useful again in Phase 9 for evaluation and testing flows.

### Watch for

- The SDK is a means to an end. The important lesson is how request shape changes model behavior.

## Anthropic SDK

### What it teaches

The Anthropic SDK teaches a slightly different interface philosophy around messages, tool use, and long-context interaction. Comparing it with other providers helps you learn what is model-specific and what is system design.

### Core topics and subtopics

- Message structure and context packing.
- Tool use and structured interaction.
- Streaming response handling.
- Usage awareness and operational constraints.

### Best phases

- Phase 2.

### Watch for

- Provider differences are useful to study because they reveal what your app depends on versus what the model supplies.

## Ollama

### What it teaches

Ollama teaches local inference tradeoffs. It is useful for understanding privacy, offline workflows, hardware limits, and the difference between cloud APIs and local model serving.

### Core topics and subtopics

- Local model serving.
- Hardware and latency tradeoffs.
- Privacy and offline experimentation.
- Prompt and model comparison under local constraints.

### Best phases

- Phase 2.
- Useful again in Phase 10 when comparing model behavior and adaptation choices.

### Watch for

- Local models make some tradeoffs easier to see, but they also make hardware limits real very quickly.

## Companion Guides

- [../courses/prompting-and-api-basics.md](../courses/prompting-and-api-basics.md)
- [retrieval-data-tools.md](./retrieval-data-tools.md)
- [../people/model-builders-and-research-explainers.md](../people/model-builders-and-research-explainers.md)
