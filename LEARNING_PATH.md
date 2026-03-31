# Learning Path

This file is the navigation map for the full curriculum. Use it when you want to understand how the phases build on one another instead of treating them as disconnected topics.

If words like `model`, `token`, `retrieval`, or `quality check` (`eval`) feel fuzzy, read [FOUNDATIONS/README.md](./FOUNDATIONS/README.md) first. This page is the map, but the Foundations pages explain the vocabulary.

## The Dependency Chain

### Foundation Layer

- [Phase 1: Python + Dev Tooling](./PHASES/01-python/README.md)
- [Phase 2: Raw LLM APIs + Context Engineering](./PHASES/02-llm-apis/README.md)
- [Phase 3: Spec-Driven Development](./PHASES/03-spec-driven/README.md)

These phases teach how to write code, call models directly, and define agent behavior clearly. In plain words, this is the part where you learn how to make a computer program, ask a text model for help, and tell it what you want in a way that is hard to misunderstand.

If the phrase `call a model` feels vague, it just means your code sends text to a model and gets text back. You do not need to know the math first. You only need to know what goes in, what comes out, and how your own code should handle the result.

### Integration Layer

- [Phase 4: Model Context Protocol (MCP), command-line tools, and agent handoffs](./PHASES/04-mcp-cli/README.md)
- [Phase 5: retrieval-augmented generation, graph retrieval, and memory](./PHASES/05-rag-graphrag/README.md)
- [Phase 6: Agentic IDEs + Coding Agents](./PHASES/06-agentic-ides/README.md)

These phases teach how models connect to tools, knowledge, and coding workflows. This is where the model stops being a text box by itself and starts becoming part of a larger system that can look things up, act on information, and help you build software.

If the word `tool` feels broad, think of it as a helper program that can do one specific job, like search, fetch, save, or validate. The model can ask for help, but the tool does the actual outside work.

### Systems Layer

- [Phase 7: orchestration and control software around the model](./PHASES/07-orchestration/README.md)
- [Phase 8: guardrails, security, and operating rules](./PHASES/08-guardrails/README.md)
- [Phase 9: quality checks, observability, and eval-driven development](./PHASES/09-evals/README.md)

These phases teach how to turn an interesting agent into a durable system. In other words, you learn how to make it repeatable, safe, measurable, and easier to debug when something goes wrong.

If the word `system` feels abstract, think of it as the model plus the code, rules, logs, checks, and recovery steps around it.

### Specialization + Proof Layer

- [Phase 10: Fine-Tuning](./PHASES/10-finetuning/README.md)
- [Phase 11: Portfolio + Job Readiness](./PHASES/11-portfolio/README.md)

These phases teach when advanced adaptation is worth it and how to present real capability publicly. This is the part where you decide whether the system should learn new behavior from examples, and how to show other people what you can build.

If `fine-tuning` or `portfolio` feel distant, that is normal. They come later, after you have learned the basics of building, checking, and explaining a system.

Use [PHASES/README.md](./PHASES/README.md) if you want the full module list in one place. Pair phase study with [RESOURCES/by-phase.md](./RESOURCES/by-phase.md) so you read and watch material that matches the current learning goal.

## Recommended Order

1. Finish enough of Phase 1 that you can build and debug small Python programs.
2. Do Phase 2 before committing to any framework.
3. Do Phase 3 early so later agent workflows stay disciplined.
4. Treat Phase 6 as parallel support, not a substitute for core learning.
5. Only go deep on Phase 10 if prompting, context engineering, and retrieval are no longer enough.

If any step feels too abstract, return to the Foundations pages. Slow is fine. Clear is better than fast.

## Project Path

The portfolio projects align with later phases:

- [PROJECTS/01-rag-system/README.md](./PROJECTS/01-rag-system/README.md) after Phase 5
- [PROJECTS/02-multi-agent-harness/README.md](./PROJECTS/02-multi-agent-harness/README.md) after Phase 7
- [PROJECTS/03-enterprise-agent/README.md](./PROJECTS/03-enterprise-agent/README.md) after Phases 8 and 9

## What You Should Be Able To Do Before Moving On

### Before Phase 2

- create and run a small Python project
- use Git without fear
- debug simple errors in the terminal

### Before Phase 5

- call model APIs directly
- understand context windows and tool calls
- explain the role of specs and tool contracts

### Before Phase 7

- understand retrieval and tool integration
- know the difference between model behavior and system behavior

### Before Phase 11

- have at least one serious project with metrics and a coherent README
- be able to explain tradeoffs you made, not just tools you used
