# Agent And Orchestration Tools

This guide covers the tools that teach coordination, delegation, tool boundaries, and workflow state. The core lesson across all of them is that an agent system succeeds when control flow is explicit.

If these words are unfamiliar, here is the quick version:

- `control flow` is the order in which a system does things
- `state` is the information the system remembers while it is working
- a `tool boundary` is the line between what the model can decide and what an external tool can do

## MCP SDK

### What it teaches

The MCP SDK teaches how tools are described and exposed in a standard way. In plain language, it helps you describe what a tool can do, what input shape it expects, how another system can discover it, and how a model-facing client stays separate from the server that actually performs the work.

### Major topics and subtopics

- Tool schemas and typed boundaries.
- Capability discovery.
- Client-server communication.
- Safe integration of external actions into an agent workflow.

### Best phases

- Phase 4.

## A2A

### What it teaches

A2A teaches agent-to-agent communication. The valuable idea is not just message passing. It is designing delegation so one system can hand off work without losing context or accountability.

Here, a `delegation contract` means the shared understanding of what work is being handed off, what inputs are provided, what result is expected, and who is responsible for the outcome.

### Major topics and subtopics

- Delegation contracts.
- Capability routing.
- Multi-agent coordination patterns.
- Failure surfaces in distributed agent work.

### Best phases

- Phase 4 and Phase 7.

## gh CLI

### What it teaches

The GitHub CLI teaches local automation against a remote system. It is excellent for understanding how a model or agent should trigger well-scoped actions instead of browsing blindly.

### Major topics and subtopics

- Scriptable GitHub workflows.
- Authentication and repository context.
- Pull request and issue operations from the terminal.
- Repeatable command-based automation.

### Best phases

- Phase 4.

## LangGraph

### What it teaches

LangGraph teaches stateful orchestration. It makes it easier to reason about branching, retries, checkpoints, and the difference between a linear chain and a durable workflow graph.

`Stateful orchestration` means the workflow remembers what already happened, what the current step is, and what should happen next.

### Major topics and subtopics

- State graphs and transitions.
- Checkpointing and persistence.
- Branching logic and loops.
- Tool nodes and controlled execution paths.

### Best phases

- Phase 7.

## CrewAI

### What it teaches

CrewAI teaches role-based agent collaboration. It is most useful when you are comparing centralized orchestration with delegated specialist-style workflows.

### Major topics and subtopics

- Agent roles and responsibilities.
- Task sequencing.
- Hierarchical or team-like coordination patterns.
- Delegation benefits and overhead.

### Best phases

- Phase 7.

## PydanticAI

### What it teaches

PydanticAI teaches typed agent pipelines. Its strongest lesson is that schemas reduce ambiguity in both inputs and outputs, which is critical when agents call tools or exchange structured state.

Here, a `schema` means a clear description of what fields are expected in the data and what shape that data should have.

### Major topics and subtopics

- Typed prompts and structured results.
- Validation and schema-driven parsing.
- Cleaner contracts between agent steps.
- Stronger reliability in automated workflows.

### Best phases

- Phase 7.

## Agentic IDEs

### What they teach

Cursor, Claude Code, Windsurf, and Aider teach different interaction models for AI-assisted development. The important concept is workflow shape: repo awareness, terminal integration, diff review, and how much control stays with the developer.

### Major topics and subtopics

- In-editor versus terminal-first collaboration.
- Repo context and scoped edits.
- Diff review and version control boundaries.
- Task framing and iterative prompting.

### Best phases

- Phase 6.

## Companion Guides

- [../courses/orchestration-and-agents-courses.md](../courses/orchestration-and-agents-courses.md)
- [deployment-and-safety-tools.md](./deployment-and-safety-tools.md)
- [../people/tool-builders-and-practical-operators.md](../people/tool-builders-and-practical-operators.md)
