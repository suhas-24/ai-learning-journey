# Prompting And API Basics

This guide covers the resources that teach how to talk to models clearly, shape outputs, and turn single calls into simple workflows.

## ChatGPT Prompt Engineering For Developers

### What it teaches

This course teaches the first principles of working with instruction-following models. The value is not the exact prompt wording. The value is learning how models respond to framing, examples, structure, and constraints.

### Major topics and subtopics

- Instruction design: clear tasks, context, and intent.
- Few-shot prompting: examples that teach a pattern.
- Output shaping: schemas, bullet structures, and explicit formatting rules.
- Constraint writing: what the model should do, avoid, or check before answering.
- Iteration loops: comparing outputs, refining prompts, and spotting ambiguity.

### When to use it

- Best at the start of Phase 2.
- Useful again in Phase 3 when you turn instructions into specs and repeatable workflows.

## Building Systems With The ChatGPT API

### What it teaches

This course teaches how one model call becomes a workflow. The central lesson is that prompts sit inside application logic, state, validation, and user interaction.

### Major topics and subtopics

- Request structure: messages, system guidance, and task-specific context.
- Workflow composition: chaining steps together instead of overloading one prompt.
- Structured outputs: parsing predictable responses into downstream logic.
- Conversation state: maintaining context without losing control of behavior.
- Simple automation patterns: classification, extraction, transformation, and routing.

### When to use it

- Best during Phase 2.
- Revisit during Phase 3 to think about specs, interfaces, and response contracts.

## OpenAI Cookbook And Claude Cookbook

### What they teach

These are example libraries more than traditional courses, but they act like lab manuals. They show how SDK calls, tool use, structured outputs, and streaming patterns look in real code.

### Major topics and subtopics

- SDK setup and request construction.
- Streaming patterns and partial output handling.
- Tool invocation and structured results.
- Parsing, validation, and practical application loops.

### When to use them

- Phase 2 when you need working code patterns.
- Phase 9 when you want example evaluation or structured testing flows.

## What To Practice After This Guide

- Rewrite one prompt from memory and compare the output quality.
- Turn one long prompt into a two-step workflow.
- Call two providers on the same task and compare output structure, latency, and failure behavior.

## Companion Guides

- [../tools/model-api-tools.md](../tools/model-api-tools.md)
- [../books/ai-engineering-and-llm-systems.md](../books/ai-engineering-and-llm-systems.md)
