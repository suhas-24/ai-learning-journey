# Deployment And Safety Tools

This guide covers the tools that teach containment, validation, and operational safety. The important idea in this phase is that safety is layered: input handling, output validation, isolation, and policy controls all matter.

In plain English, safety means the system should not take dangerous actions, reveal secrets, or keep running when it should stop.

## How To Use This Guide

- Start here when a system can act, but you need better control over what it is allowed to do.
- Think in layers: execution boundary, policy boundary, output boundary, and measurement.
- Safety is not a single feature. It is a system design choice.

## Docker

### What it teaches

Docker teaches isolation and repeatability. It helps you package a system, separate host and runtime concerns, and create safer execution boundaries.

### Core topics and subtopics

- Images and containers.
- Dockerfiles and reproducible environments.
- Runtime isolation and dependency control.
- Sandboxed execution patterns.

### Best phases

- Phase 1 for basic environment understanding.
- Phase 8 for sandboxing and execution safety.

### Watch for

- The point is not to containerize everything. The point is to understand what the container keeps separate.

## NeMo Guardrails

### What it teaches

NeMo Guardrails teaches policy-oriented control over model behavior. It is useful for learning how to express allowed behavior, blocked behavior, and conversation constraints outside the prompt alone.

### Core topics and subtopics

- Safety policy design.
- Conversation constraints.
- Blocking and redirecting risky requests.
- Behavior control layered over model responses.

### Best phases

- Phase 8.

### Watch for

- Policies work best when they are simple enough to explain to a teammate.

## Guardrails AI

### What it teaches

Guardrails AI teaches validation-first thinking. Instead of trusting the model output directly, you define checks, schemas, and recovery paths.

### Core topics and subtopics

- Output validation.
- Schema enforcement.
- Re-ask flows and failure recovery.
- Reliability through explicit checks.

### Best phases

- Phase 8.

### Watch for

- Validation is not a punishment for the model. It is a way to make downstream behavior safer and more predictable.

## Why These Tools Matter Together

- Docker handles execution boundaries.
- Guardrails-style tools handle output boundaries.
- Evaluation tools from [evals-observability-tools.md](./evals-observability-tools.md) tell you whether the safety layer is actually working.

## Companion Guides

- [agent-orchestration-tools.md](./agent-orchestration-tools.md)
- [../books/ai-engineering-and-llm-systems.md](../books/ai-engineering-and-llm-systems.md)
- [../newsletters/strategy-policy-and-ecosystem.md](../newsletters/strategy-policy-and-ecosystem.md)
