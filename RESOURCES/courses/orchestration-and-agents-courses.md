# Orchestration And Agents Courses

This guide covers the resources that explain how multiple model calls, tools, and saved state become a system instead of an unstructured loop.

An `agent` is a model-enabled system that can choose actions. `Orchestration` means coordinating those actions step by step so the system does not just wander. A simple `loop` is not enough if you cannot see where state lives or how to recover after failure.

## How To Use This Guide

- Start here when a single prompt is no longer enough.
- Keep track of where state lives, who changes it, and what happens if a step fails.
- If a framework name starts to dominate the explanation, step back and restate the workflow in plain language.

## LangChain For LLM Application Development

### What it teaches

This course teaches the first layer of orchestration abstractions. The real value is seeing how prompts, retrieval, tools, and application logic get composed, even if you later choose a different framework.

### Core topics and subtopics

- Chain composition: breaking work into ordered steps.
- Retrieval integration: adding grounded context to a workflow.
- Tool use: extending model capability through external actions.
- Reusable abstractions: separating model logic from application glue.

### When to use it

- Best as an early bridge into Phase 7.
- Also useful in Phase 4 when you are learning how tool boundaries shape agent behavior.

### Watch for

- The useful lesson is the composition pattern, not the framework label.

## Broader AI Engineering Programs

### What they teach

Longer programs help when you need a guided build sequence across APIs, retrieval, agents, and deployment. Their best contribution is usually repetition across projects, not novel theory.

### Core topics and subtopics

- End-to-end app construction.
- Tool selection and framework comparison.
- Project decomposition and iteration loops.
- Deployment and productization habits.

### When to use them

- Use them selectively in Phases 5 to 7.
- Avoid turning them into passive content consumption. Extract the build patterns and move back into your own repo quickly.

### Watch for

- If a program keeps adding more frameworks without showing the control flow, it is probably hiding the important lesson.

## What To Practice After This Guide

- Rebuild one chain as an explicit state graph.
- Add one tool call and define the input and output contract clearly.
- Write down where state lives, who updates it, and how you recover after a failure.

## Companion Guides

- [../tools/agent-orchestration-tools.md](../tools/agent-orchestration-tools.md)
- [../people/tool-builders-and-practical-operators.md](../people/tool-builders-and-practical-operators.md)
