# Phase Index

This directory is the main curriculum. Each phase is a self-contained learning module with a consistent internal shape so you can study, practice, and self-check without guessing where things live.

## How To Use A Phase

1. Read the phase `README.md` for the big picture.
2. Work through the `chapters/` in order.
3. Complete the `labs/` or `exercises/`.
4. Reuse the `snippets/` while building your own examples.
5. Answer the questions in `checkpoints.md`.
6. Open `troubleshooting.md` whenever you hit confusion or bad output.

If a word in a phase title feels new, that is a clue to read the `README.md` slowly before touching the chapters.

## Curriculum

### Foundations

- [01-python](./01-python/README.md): learn the basics of programming, how to debug small mistakes, and how to keep a project organized
- [02-llm-apis](./02-llm-apis/README.md): learn what an LLM is, how to send it text, how to read its output, and how to keep that output predictable
- [03-spec-driven](./03-spec-driven/README.md): learn how to write clear rules for behavior so a person or agent can follow them without guessing

### Integration

- [04-mcp-cli](./04-mcp-cli/README.md): learn how programs connect to outside tools and when to use an API, a command line, or a shared tool language like MCP
- [05-rag-graphrag](./05-rag-graphrag/README.md): learn how to look up useful information before answering, and how to break documents into smaller pieces, find the best pieces, and reuse past information
- [06-agentic-ides](./06-agentic-ides/README.md): learn how AI coding tools fit into a developer’s workflow and how to keep control of your changes

### Systems

- [07-orchestration](./07-orchestration/README.md): learn how a system decides what happens next, remembers progress, and handles failures
- [08-guardrails](./08-guardrails/README.md): learn how to keep a system safe, bounded, and harder to misuse
- [09-evals](./09-evals/README.md): learn how to test a system honestly, watch what it does, and catch regressions

### Specialization And Proof

- [10-finetuning](./10-finetuning/README.md): learn when it makes sense to train a model on your own examples instead of only prompting it
- [11-portfolio](./11-portfolio/README.md): learn how to explain your work clearly so other people can see what you can build

## Pairing Guides

- Use [../FOUNDATIONS/README.md](../FOUNDATIONS/README.md) before Phase 1 if you need the shared vocabulary and mental models.
- Use [../RESOURCES/by-phase.md](../RESOURCES/by-phase.md) to pick books, courses, tools, people, and newsletters that match your current phase.
- Use [../PROJECTS/README.md](../PROJECTS/README.md) when you are ready to turn phase knowledge into portfolio-grade systems.
