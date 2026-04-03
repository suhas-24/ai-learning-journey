# Phase 2 - Working With Language Models

This phase is about learning how to talk to a language model directly, before a framework hides the pieces. We will keep the moving parts visible so the system feels understandable instead of magical.

Here are the first words in plain language:

- `model` means a piece of software that has learned patterns from examples
- `LLM` means large language model, which is a model trained on lots of text so it can predict and generate text
- `token` means a small piece of text the model reads or writes
- `tokenization` means breaking text into tokens
- `prompt` means the instruction or question you give the model
- `message` means one item in the conversation, such as a system instruction, user request, or tool result
- `API` means a way for one program to ask another program to do work
- `API key` means a secret string that proves your program is allowed to use a service
- `context` means everything the model can see right now
- `tool call` means the model asking your program to use an outside helper

If those words are new, that is completely fine. You do not need to memorize them all at once. You only need enough understanding to follow the examples below. This phase repeats the ideas in small pieces so they feel ordinary instead of magical.

## What This Phase Is Really About

When people first meet an LLM, it is easy to think the model is the whole system. It is not.

The model is only one part of the picture. Your program decides:

- what question to ask
- what background information to include
- what rules the model should follow
- when to trust the answer
- when to ask for outside help
- what to do if the answer is wrong or incomplete

This phase teaches that surrounding work one small step at a time.

## What You Will Learn

- what an LLM is and what it is not
- why tokens and tokenization matter
- how a request is shaped before it reaches the model
- what different message roles do in a conversation
- how to ask for structured output that code can read
- how tool calling works as a back-and-forth loop
- how to choose the right amount of context
- how to think about cost, latency, and failure

`Structured output` means the model returns information in a predictable shape, such as fields with names, so your code can read it without guessing. That shape is often described with a schema, which is just a rule for how the output should look.

## How To Use This Phase

1. Read the chapters in order.
2. Copy or adapt the snippets into a sandbox project.
3. Do the labs with a simulated provider or your own API key.
4. Use [checkpoints.md](./checkpoints.md) to test whether you can explain the ideas in your own words.
5. Use [troubleshooting.md](./troubleshooting.md) when the output feels confusing or inconsistent.

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
- what your program should do if the model asks for a tool

If you can do that, you understand the moving parts well enough to build on them.
