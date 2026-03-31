# Glossary

This glossary is intentionally practical. The goal is not to impress anyone. The goal is to make the first important words feel simple enough to use.

## AI

Artificial intelligence is the broad field of building software that can do tasks we usually associate with human thinking, such as recognizing patterns, understanding language, or making decisions.

## Model

A model is a piece of software that has been trained on examples so it can make predictions. In this repo, the models we care about often work with text.

## LLM

An LLM is a large language model. That means a model trained on lots of text so it can predict and generate text. If you ask it a question, it does not "know" facts the way a person does. It uses patterns learned from training and the text you give it right now.

## Token

A token is a small piece of text the model reads or writes. A token can be a whole word, part of a word, punctuation, or even a space. The model does not work with raw sentences the way people do. It works with tokens.

## Tokenization

Tokenization is the step that breaks text into tokens.

For example, the sentence `I like coffee.` might be split into several pieces instead of being treated as one block. The exact split is not important for a beginner. The important idea is that the model sees text in pieces, not as human eyes do.

Why this matters:

- prices are often based on tokens
- model limits are often based on tokens
- speed and latency are often affected by token count

## Context Window

The context window is the total amount of information the model can see in one call. It includes your instruction, the conversation so far, retrieved documents, tool results, and any other text passed into the model.

Think of it as the model’s short-term working space. If something is not inside the context window, the model cannot use it for that call.

## Prompt

A prompt is the instruction or question you give the model. A prompt can be short, like "Summarize this paragraph," or longer, like a detailed task with examples and rules.

## Prompt Engineering

Prompt engineering is the craft of writing prompts that steer a model’s output. It is useful, but it is only one part of building a reliable system.

## Context Engineering

Context engineering is the broader job of deciding what information should go into the model’s context window, in what order, and in what form.

This includes:

- instructions
- examples
- user messages
- retrieved documents
- tool outputs

## API

An API is a way for one program to ask another program to do something. In this repo, an API is often how your code talks to a model service.

## Tool Calling

Tool calling is the pattern where the model asks external code to fetch information or perform an action, then uses the result to continue.

## Harness Engineering

Harness engineering is the design of the system around the model. It includes the code that decides what to send, what to retry, what to log, when to stop, and when to ask for help.

## Retrieval

Retrieval means finding relevant information at question time and adding it to the model’s context.

## RAG

Retrieval-Augmented Generation, or RAG, is a pattern where the system looks up helpful information first and then asks the model to answer using that information.

## GraphRAG

GraphRAG extends retrieval by representing entities and relationships explicitly. That helps when a question depends on connected facts rather than one isolated passage.

## Embedding

An embedding is a numerical representation of text that helps a computer compare pieces of text by meaning.

## Vector Database

A vector database stores embeddings and finds similar items quickly.

## MCP

Model Context Protocol is a standard way for tools and data sources to expose typed capabilities to model-driven systems.

## A2A

Agent-to-agent communication is the pattern used when one agent delegates work to another agent.

## Eval

An eval is a structured way of measuring quality. A good eval checks the behavior you actually care about, not just whether the model sounds fluent.

## Observability

Observability is the ability to inspect what the system did, why it did it, how much it cost, and where it failed.

## Guardrails

Guardrails are the checks and policies that keep model behavior within acceptable safety and quality boundaries.
