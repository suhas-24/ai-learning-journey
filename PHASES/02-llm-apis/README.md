# Phase 2 - Working With Language Models

This phase teaches how to talk to a language model directly, before a framework hides the pieces. If the term "LLM" is new, it means "large language model." That is a program trained on lots of text so it can predict and generate language.

Before anything else:

- a **token** is a small piece of text the model reads
- **tokenization** is the process of breaking text into tokens
- **context** is everything the model can see right now

You do not need to know the math behind the model. You only need to understand what information your code sends, what the model returns, and where your program must take over.

## What You Will Learn

- what an LLM is and what it is not
- what a token is and why tokenization matters
- what a model request usually contains
- how conversation history is represented in code
- how structured output differs from free-form text
- how tool calling works as a loop between the model and your program
- how to decide what belongs in context and what should be left out
- how to think about latency, cost, and failure modes

## How To Use This Phase

1. Read the chapters in order.
2. Copy or adapt the snippets into a sandbox project.
3. Do the labs with a simulated provider or your own API key.
4. Use [checkpoints.md](./checkpoints.md) to make sure you can explain every moving part in plain language.
5. Use [troubleshooting.md](./troubleshooting.md) when responses feel inconsistent or confusing.

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
- what the program should do if the model asks for a tool
