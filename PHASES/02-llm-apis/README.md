# Phase 2 - Raw LLM APIs and Context Engineering

This phase teaches how to work with language models before a framework hides the important details. The goal is to make request shape, message history, tool use, and context decisions feel understandable and inspectable.

## What You Will Learn

- what a model request usually contains
- how conversation history is represented in code
- how structured output differs from free-form text
- how tool calling works as a loop between model and program
- how to decide what belongs in context and what should be omitted
- how to think about latency, token cost, and failure modes

## How To Use This Phase

1. Read the chapters in order.
2. Copy or adapt the snippets into a sandbox project.
3. Do the labs with your own API key or a simulated provider wrapper.
4. Use [checkpoints.md](./checkpoints.md) to make sure you can explain every moving part.
5. Use [troubleshooting.md](./troubleshooting.md) when responses become inconsistent or confusing.

## Study Path

1. [Chapter 1: Request Shape and Message Roles](./chapters/01-request-shape-and-message-roles.md)
2. [Chapter 2: Structured Output and Tool Calling](./chapters/02-structured-output-and-tool-calling.md)
3. [Chapter 3: Context Engineering](./chapters/03-context-engineering.md)
4. [Chapter 4: Cost, Latency, and Failure Analysis](./chapters/04-cost-latency-and-failure-analysis.md)

## Practice

- [Lab 1: Build a Structured Answerer](./labs/lab-01-structured-answerer.md)
- [Lab 2: Build a Tool-Augmented Research Loop](./labs/lab-02-tool-augmented-research-loop.md)

## Snippets

- [provider_payload_patterns.md](./snippets/provider_payload_patterns.md)
- [tool_loop_simulation.py](./snippets/tool_loop_simulation.py)
- [context_compaction_example.md](./snippets/context_compaction_example.md)

## Success Standard

You should be able to look at a model request and explain:

- what the model sees
- why each piece of context is present
- what the next program step should be if the model asks for a tool
