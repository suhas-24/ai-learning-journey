# Glossary

This glossary is intentionally practical. Definitions are written for builders, not for textbooks.

## AI

Artificial intelligence is the broad field of building systems that perform tasks that normally require human-like pattern recognition, decision-making, or language handling.

## LLM

A large language model is a model trained to predict the next token in a sequence of text. In practice, this gives it the ability to generate, transform, summarize, and reason over language-like inputs.

## Token

A token is a chunk of text the model reads or generates. Pricing, limits, and latency are usually measured in tokens rather than words.

## Context Window

The context window is the total amount of information the model can see in one call. It includes instructions, history, retrieved documents, tool results, and the user’s current request.

## Prompt Engineering

Prompt engineering is the craft of writing instructions to steer a model’s output. It matters, but by itself it is not enough for production systems.

## Context Engineering

Context engineering is the broader discipline of deciding what information enters the model’s context window, in what order, and in what compressed form.

## Harness Engineering

Harness engineering is the design of the full system around the model: planning, retries, budgets, state, checkpoints, approvals, logs, and recovery behavior.

## Tool Calling

Tool calling is the pattern where a model asks external code to perform an action or fetch information, then continues reasoning with the result.

## RAG

Retrieval-Augmented Generation is the pattern of retrieving relevant information at runtime and adding it to the model’s context before generation.

## GraphRAG

GraphRAG extends retrieval by representing entities and relationships explicitly, which helps when questions require connected or multi-hop reasoning.

## Embedding

An embedding is a vector representation of content that captures semantic similarity. Embeddings make vector search possible.

## Vector Database

A vector database stores embeddings and retrieves similar items efficiently.

## MCP

Model Context Protocol is a standard way for tools and data sources to expose typed capabilities to model-driven systems.

## A2A

Agent-to-agent communication is the pattern or protocol used when one agent delegates work to another.

## Eval

An eval is a structured way of measuring quality. Good evals test the behavior you actually care about, not just generic fluency.

## Observability

Observability is the ability to inspect what the system did, why it did it, how much it cost, and where it failed.

## Guardrails

Guardrails are the checks and policies that keep model behavior within acceptable safety and quality boundaries.
