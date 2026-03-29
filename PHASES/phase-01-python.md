# Phase 1 - Python Fluency + Modern Dev Environment

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 6-8 weeks

---

## Why This Phase Matters

Everything later in the roadmap depends on this phase. Agents, RAG systems, eval pipelines, and orchestration frameworks are all built on plain Python files, shell commands, environment setup, logging, and tests. If I rush this stage, every future phase becomes slower and more fragile.

The real goal is not "learn Python syntax." The goal is to become comfortable reading, writing, running, and debugging small programs without fear.

---

## Core Ideas To Master

### Python Fundamentals

- variables, data types, conditionals, loops, and functions
- lists, dictionaries, sets, tuples, and when each structure is the right tool
- file handling for JSON, CSV, and plain text
- exceptions and how to fail clearly instead of silently
- modules and packages so code can be organized instead of dumped into one file

### Python That Modern AI Codebases Actually Use

- type hints so function contracts stay readable
- Pydantic models for validated configuration and structured data
- async and await because many AI workflows spend time waiting on APIs
- structured logging with `structlog` instead of scattered `print()` calls
- pytest for repeatable confidence instead of "it worked once on my machine"

### Developer Environment

- Poetry for dependency management and virtual environments
- Ruff for linting and formatting
- Git for commits, branches, and safe iteration
- Docker for packaging a project the same way every time
- Typer for building CLI tools that feel professional

---

## Study Sequence

1. Learn the absolute basics: variables, lists, dictionaries, functions, loops, and conditions.
2. Start writing tiny scripts that read files, transform data, and print structured output.
3. Add type hints and Pydantic models so code becomes self-documenting.
4. Learn async well enough to call multiple APIs concurrently without freezing the whole program.
5. Wrap everything in tooling: Poetry, Ruff, pytest, Git, and a small CLI.

---

## Build Plan

### Week 1-2

- write tiny Python scripts every day
- practice reading and writing JSON files
- get comfortable running scripts from the terminal
- start using Git after every meaningful change

### Week 3-4

- introduce type hints and Pydantic
- refactor one messy script into functions and modules
- write tests for basic helpers
- practice error handling instead of letting scripts crash unclearly

### Week 5-6

- learn async by calling multiple HTTP endpoints concurrently
- build the first Typer CLI commands
- add Ruff and pytest to the workflow
- put the project inside Docker once the local version works

### Week 7-8

- polish project structure
- add a README, helpful CLI help text, and tests
- push the project publicly and explain what I built

---

## Phase Project: `agent-cli`

**Project goal:** build a production-ready Python CLI skeleton that will be extended in later phases.  
**Planned repo:** a dedicated `agent-cli` repository or a subproject created during this phase  
**Current project status:** planning complete, implementation not started

### What `agent-cli` should contain

- `pyproject.toml` managed by Poetry
- a Typer entry point with at least two useful commands
- Pydantic config models
- structured logging
- a test suite for helper functions
- a Dockerfile that can run the CLI consistently

### What this project is really teaching

- how to go from zero files to a real Python project layout
- how to think in functions and modules instead of one-off scripts
- how to create a baseline that later agent projects can inherit

---

## Exit Criteria

- I can explain basic Python syntax without looking it up every five minutes.
- I can create a new Poetry project from scratch.
- I can write and run tests with pytest.
- I can lint and format code with Ruff.
- I can explain what async solves and where it is useful.
- I can build a small CLI and package it cleanly.

---

## Common Traps To Avoid

- memorizing syntax without writing any code
- skipping tests because the script "looks simple"
- using AI coding tools to generate Phase 1 code I do not understand
- treating Docker as magic instead of learning what each line does
- postponing Git until a project is already messy

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| Python Official Tutorial | Best source for fundamentals | Read a section, then immediately build a tiny script |
| Pydantic docs | Central to modern AI Python | Focus on models, validation, and parsing |
| asyncio docs | Needed for concurrent API work | Learn just enough to build parallel I/O tasks |
| Poetry docs | Core environment tool | Practice new project creation and dependency management |
| Ruff docs | Fast feedback loop | Make linting part of every coding session |

---

## Questions I Want To Answer During This Phase

- When should I split code into modules instead of keeping it in one file?
- What is the practical difference between synchronous and asynchronous code?
- How much testing is enough for a small CLI?
- Which Python patterns show up over and over in AI engineering codebases?
