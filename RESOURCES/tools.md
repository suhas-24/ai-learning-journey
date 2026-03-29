# Tools Reference

This file tracks the tools that matter across the roadmap and why they matter. The goal is not to learn every tool deeply. The goal is to know what problem each tool solves and when it becomes worth using.

## Development Environment

| Tool | Purpose | Phase | First real use |
| --- | --- | --- | --- |
| Poetry | Dependency management and virtualenvs | 1 | Create and manage `agent-cli` |
| Ruff | Fast linting and formatting | 1 | Add it to every Python project from the start |
| Pyright | Type checking | 1 | Catch type mistakes once projects become modular |
| Docker | Reproducible environments and sandboxing | 1, 8 | Package `agent-cli`, later isolate risky code paths |
| Typer | Clean CLI construction | 1 | Build the Phase 1 CLI project |
| Git and GitHub Actions | Source control and automation | 1 | Run tests and evals on every important change |

## LLM APIs

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| Anthropic SDK | Claude API integration | 2 | messages, tools, streaming, usage |
| OpenAI SDK | GPT API integration | 2 | cross-provider comparison and structured outputs |
| Ollama | Local model experimentation | 2 | local inference tradeoffs and privacy-first workflows |

## Retrieval And Data

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| ChromaDB | Simple local vector DB | 5 | early retrieval experimentation |
| Qdrant | Production-grade vector database | 5 | collections, metadata, query behavior |
| LlamaIndex | Retrieval framework | 5 | pipeline design and retrieval patterns |
| Microsoft GraphRAG | Graph-based retrieval | 5 | entity relationships and multi-hop reasoning |

## Protocols And Integration

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| MCP SDK | Standardized tool integration | 4 | typed tools, discovery, server/client model |
| A2A | Agent-to-agent communication | 4 | capability discovery and delegation patterns |
| `gh` CLI | GitHub automation from shell | 4 | token-efficient local tool usage |

## Orchestration

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| LangGraph | Stateful multi-step agents | 7 | persistence, branching, checkpoints |
| CrewAI | Role-based agent teams | 7 | delegation and crew structure |
| PydanticAI | Typed agent pipelines | 7 | strong schemas and structured outputs |

## Guardrails And Safety

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| NeMo Guardrails | Policy and behavior control | 8 | prompt-injection handling and policy design |
| Guardrails AI | Input and output validation | 8 | validators, re-ask flows, schema enforcement |
| Docker sandboxing | Isolation for risky code paths | 8 | reducing blast radius |

## Observability

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| Langfuse | Tracing, prompts, and cost tracking | 9 | end-to-end observability |
| LangSmith | Datasets and prompt testing | 9 | evaluation workflows |
| RAGAS | RAG evaluation | 9 | faithfulness, relevance, and retrieval quality |

## Agentic IDEs

| Tool | Purpose | Phase | What to learn |
| --- | --- | --- | --- |
| Cursor | AI-native editor | 6 | repo rules and interactive pair programming |
| Claude Code | Goal-based CLI coding agent | 6 | task framing and diff review discipline |
| Windsurf | Alternative AI-native IDE | 6 | contrast in workflow and model orchestration |
| Aider | Git-native coding assistant | 6 | lightweight terminal-centric collaboration |

## Personal Notes

- Tool choice should be driven by problem shape, not social media hype.
- CLI tools are often underrated in agent workflows because they are simple, cheap, and extremely capable.
- Every new tool should earn its place by making one real project meaningfully better.
