# Deployment And Safety Tools

This guide covers the tools that teach containment, validation, and operational safety. The important idea in this phase is that safety is layered: input handling, output validation, isolation, and policy controls all matter.

## Docker

### What it teaches

Docker teaches isolation and repeatability. It helps you package a system, separate host and runtime concerns, and create safer execution boundaries.

### Major topics and subtopics

- Images and containers.
- Dockerfiles and reproducible environments.
- Runtime isolation and dependency control.
- Sandboxed execution patterns.

### Best phases

- Phase 1 for basic environment understanding.
- Phase 8 for sandboxing and execution safety.

## NeMo Guardrails

### What it teaches

NeMo Guardrails teaches policy-oriented control over model behavior. It is useful for learning how to express allowed behavior, blocked behavior, and conversation constraints outside the prompt alone.

### Major topics and subtopics

- Safety policy design.
- Conversation constraints.
- Blocking and redirecting risky requests.
- Behavior control layered over model responses.

### Best phases

- Phase 8.

## Guardrails AI

### What it teaches

Guardrails AI teaches validation-first thinking. Instead of trusting the model output directly, you define checks, schemas, and recovery paths.

### Major topics and subtopics

- Output validation.
- Schema enforcement.
- Re-ask flows and failure recovery.
- Reliability through explicit checks.

### Best phases

- Phase 8.

## Why These Tools Matter Together

- Docker handles execution boundaries.
- Guardrails-style tools handle output boundaries.
- Evaluation tools from [evals-observability-tools.md](./evals-observability-tools.md) tell you whether the safety layer is actually working.

## Companion Guides

- [agent-orchestration-tools.md](./agent-orchestration-tools.md)
- [../books/ai-engineering-and-llm-systems.md](../books/ai-engineering-and-llm-systems.md)
- [../newsletters/strategy-policy-and-ecosystem.md](../newsletters/strategy-policy-and-ecosystem.md)
