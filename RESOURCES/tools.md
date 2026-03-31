# Tools Reference

This file is the practical map of the stack. It explains what each tool does, which problem it solves, and which phase turns it from a name into a working habit.

## Development Environment

### Poetry

Purpose: dependency management and virtual environments.

### What it teaches

- how Python projects are structured
- how dependencies are locked
- how project metadata is managed cleanly

### Subtopics

- `pyproject.toml`
- virtualenv creation
- dependency groups
- package installation

### Best phase

- Phase 1

### Ruff

Purpose: fast linting and formatting.

### What it teaches

- code style discipline
- fast feedback on mistakes
- consistent formatting across projects

### Subtopics

- lint rules
- formatting
- import hygiene
- fix-on-save workflows

### Best phase

- Phase 1

### Pyright

Purpose: static type checking.

### What it teaches

- type safety
- API contract clarity
- catching mistakes before runtime

### Subtopics

- annotations
- type narrowing
- schema discipline

### Best phase

- Phase 1

### Docker

Purpose: reproducible environments and isolation.

### What it teaches

- packaging a system consistently
- separating host and container environments
- isolation for later safety work

### Subtopics

- images
- containers
- Dockerfiles
- runtime isolation

### Best phase

- Phase 1 and Phase 8

### Typer

Purpose: build clean command-line tools.

### What it teaches

- CLI ergonomics
- command design
- parsing inputs cleanly

### Subtopics

- commands
- options
- help text
- subcommands

### Best phase

- Phase 1

### Git and GitHub Actions

Purpose: version control and automation.

### What it teaches

- working in branches
- committing in small increments
- running repeatable automation

### Subtopics

- commits
- branches
- remote tracking
- CI workflows

### Best phase

- Phase 1 onward

## LLM APIs

### Anthropic SDK

Purpose: direct access to Claude.

### What it teaches

- message structure
- streaming
- tool use
- usage tracking

### Best phase

- Phase 2

### OpenAI SDK

Purpose: direct access to OpenAI models.

### What it teaches

- model invocation patterns
- structured responses
- cross-provider comparison

### Best phase

- Phase 2

### Ollama

Purpose: local model experimentation.

### What it teaches

- local inference behavior
- privacy and offline workflows
- model tradeoffs on constrained hardware

### Best phase

- Phase 2

## Retrieval And Data

### ChromaDB

Purpose: local vector retrieval experimentation.

### What it teaches

- embeddings
- search over semantic representations
- fast prototype retrieval loops

### Best phase

- Phase 5

### Qdrant

Purpose: production-oriented vector storage.

### What it teaches

- collection design
- metadata filtering
- query behavior

### Best phase

- Phase 5

### LlamaIndex

Purpose: retrieval pipeline framework.

### What it teaches

- ingest, index, retrieve, generate
- composable RAG workflow design

### Best phase

- Phase 5

### Microsoft GraphRAG

Purpose: graph-based retrieval and multi-hop reasoning.

### What it teaches

- entity extraction
- graph structure
- connected reasoning

### Best phase

- Phase 5

## Protocols And Integration

### MCP SDK

Purpose: standardized tool integration.

### What it teaches

- typed tool boundaries
- discovery
- client/server integration

### Best phase

- Phase 4

### A2A

Purpose: agent-to-agent communication.

### What it teaches

- delegation
- capability discovery
- multi-agent coordination

### Best phase

- Phase 4

### gh CLI

Purpose: local GitHub automation.

### What it teaches

- shell-based GitHub workflows
- token-efficient local operations

### Best phase

- Phase 4

## Orchestration

### LangGraph

Purpose: stateful orchestration graphs.

### What it teaches

- transitions
- checkpointing
- branching
- persistence

### Best phase

- Phase 7

### CrewAI

Purpose: role-based agent collaboration.

### What it teaches

- agent roles
- delegation
- sequential and hierarchical workflows

### Best phase

- Phase 7

### PydanticAI

Purpose: typed structured agent pipelines.

### What it teaches

- schema-driven agent inputs and outputs
- cleaner structured workflows

### Best phase

- Phase 7

## Guardrails And Safety

### NeMo Guardrails

Purpose: policy control and behavior gating.

### What it teaches

- safety policies
- blocking risky behavior
- controlled model behavior

### Best phase

- Phase 8

### Guardrails AI

Purpose: validation and re-ask flows.

### What it teaches

- output checking
- schema enforcement
- failure handling

### Best phase

- Phase 8

### Docker sandboxing

Purpose: isolate risky execution.

### What it teaches

- blast radius control
- safe code execution

### Best phase

- Phase 8

## Observability

### Langfuse

Purpose: traces, prompts, and cost visibility.

### What it teaches

- end-to-end tracing
- prompt versioning
- cost tracking

### Best phase

- Phase 9

### LangSmith

Purpose: datasets and prompt testing.

### What it teaches

- experiment tracking
- evaluation workflows

### Best phase

- Phase 9

### RAGAS

Purpose: retrieval and answer evaluation.

### What it teaches

- faithfulness
- answer relevance
- context precision and recall

### Best phase

- Phase 9

## Agentic IDEs

### Cursor

Purpose: AI-native editor.

### What it teaches

- in-editor collaboration
- repo-aware changes

### Best phase

- Phase 6

### Claude Code

Purpose: goal-based CLI coding agent.

### What it teaches

- task framing
- diffs
- terminal-first workflows

### Best phase

- Phase 6

### Windsurf

Purpose: alternative AI-native editor.

### What it teaches

- model interaction in a different editor shape

### Best phase

- Phase 6

### Aider

Purpose: Git-native coding assistant.

### What it teaches

- pair programming with explicit version control boundaries

### Best phase

- Phase 6

## Personal Notes

- A tool is only worth learning if it changes a real project outcome.
- The fastest tool is not always the right one, but the right tool is usually easier to justify when I can explain its boundary clearly.
- The stack gets safer and more powerful when I know which tool belongs to which phase.
