# Glossary

This glossary is intentionally practical. The goal is not to sound fancy. The goal is to make the first important words feel clear enough to use in a real conversation.

## AI

Artificial intelligence is the broad field of building software that can do tasks we usually associate with human thinking, such as recognizing patterns, understanding language, or making decisions.

## Model

A model is software that has been trained on examples so it can make predictions. In this repo, the models we care about usually work with text.

## LLM

An LLM is a large language model. That means a model trained on lots of text so it can predict and generate text.

If you ask it a question, it does not "know" facts the way a person does. It uses patterns learned from training plus the text you give it right now.

## Token

A token is a small piece of text the model reads or writes.

A token can be:

- a whole word
- part of a word
- punctuation
- a space

The model does not work with raw sentences the way people do. It works with tokens.

## Tokenization

Tokenization is the step that breaks text into tokens.

For example, `I like coffee.` may be split into several pieces instead of being treated as one block. The exact split is not the point for a beginner. The important idea is that the model sees text in pieces.

Why this matters:

- prices are often based on tokens
- limits are often based on tokens
- speed and latency are often affected by token count

## Context Window

The context window is the total amount of information the model can see in one call.

It includes things like:

- your instruction
- the conversation so far
- retrieved documents
- tool results
- any other text passed to the model

Think of it as the model’s short-term working space. If something is not inside the context window, the model cannot use it for that call.

## Prompt

A prompt is the instruction or question you give the model.

It can be short, like:

```text
Summarize this paragraph.
```

Or longer, like a task with examples, rules, and a desired output shape.

## Prompt Engineering

Prompt engineering is the craft of writing prompts that steer a model’s output.

It is useful, but it is only one part of building a reliable system.

## Context Engineering

Context engineering is the broader job of deciding what information should go into the model’s context window, in what order, and in what form.

This includes:

- instructions
- examples
- user messages
- retrieved documents
- tool outputs

## API

An API is a way for one program to ask another program to do something.

In this repo, an API is often how your code talks to a model service.

## Tool Calling

Tool calling is the pattern where the model asks external code to fetch information or perform an action, then uses the result to continue.

## Harness

A harness is the software around the model that decides what to send, what to retry, what to log, when to stop, and when to ask for help.

Think of the model as the engine and the harness as the control system around it.

## Retrieval

Retrieval means finding relevant information at question time and adding it to the model’s context.

## RAG

RAG means retrieval-augmented generation.

That is a pattern where the system looks up helpful information first and then asks the model to answer using that information.

## GraphRAG

GraphRAG extends retrieval by representing entities and relationships explicitly.

That helps when a question depends on connected facts rather than one isolated passage.

## Embedding

An embedding is a numerical representation of text that helps a computer compare pieces of text by meaning.

If two pieces of text mean something similar, their embeddings are usually closer together.

## Vector Database

A vector database stores embeddings and finds similar items quickly.

## MCP

MCP means Model Context Protocol.

It is a standard way for tools and data sources to expose typed capabilities to model-driven systems.

## A2A

A2A means agent-to-agent communication.

It is the pattern used when one agent delegates work to another agent.

## Agent

An agent is software that can take steps toward a goal instead of only answering once.

It may plan, call tools, check results, and decide what to do next.

## Eval

An eval is a structured way of measuring quality.

A good eval checks the behavior you actually care about, not just whether the model sounds fluent.

## Observability

Observability is the ability to inspect what the system did, why it did it, how much it cost, and where it failed.

## Guardrails

Guardrails are the checks and policies that keep model behavior within acceptable safety and quality boundaries.

## Fine-Tuning

Fine-tuning means training a model a little more on your own examples so it behaves better on one narrow task.

It is different from prompting, which changes the instructions at run time, and different from retrieval, which changes the information the model can see at run time.
