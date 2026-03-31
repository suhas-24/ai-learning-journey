# Phase 1 - Python Fluency + Modern Dev Environment

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 6-8 weeks

---

## Why This Phase Matters

Everything later in the roadmap depends on this phase. Agents, RAG systems, eval pipelines, and orchestration frameworks are all built on plain Python files, shell commands, environment setup, logging, and tests. If I rush this stage, every future phase becomes slower and more fragile.

The real goal is not "learn Python syntax." The goal is to become comfortable reading, writing, running, and debugging small programs without fear.

Think of this phase as learning the alphabet, grammar, and sentence structure of the whole roadmap. If I can explain what a variable is, why a function exists, why a list is different from a dictionary, and how a script becomes a project, later AI topics become much easier to reason about.

---

## Chapter Map

### Chapter 1: Python Core

This chapter is about the raw language. A variable is a named container for a value. A function is a reusable block of logic that takes inputs and returns outputs. A loop repeats work. A condition branches based on a yes-or-no question. These are the building blocks of every later script.

### Chapter 2: Data Structures

Lists preserve order, dictionaries map keys to values, sets hold unique items, and tuples describe values that should not change. In AI work, lists often hold messages or search results, dictionaries often hold structured config or API payloads, and sets help with deduplication.

### Chapter 3: Files And Errors

Real programs read and write files. That means understanding JSON, CSV, and text handling. It also means understanding exceptions. A program that crashes without explanation is not production-ready; a program that catches everything blindly is also not production-ready. The goal is controlled failure.

### Chapter 4: Modular Code

One large script is easy to start and hard to maintain. Modules, packages, and imports let me split responsibility into pieces that can be tested and reused. This is the step where Python stops feeling like notebook scraps and starts feeling like a codebase.

### Chapter 5: Modern AI Python

Type hints, Pydantic, async, structured logging, and pytest are not advanced extras. They are normal AI engineering habits. They make configuration safer, APIs easier to reason about, and code easier to debug.

### Chapter 6: Tooling

Poetry, Ruff, Git, Docker, and Typer are the environment layer. They make projects repeatable, readable, and collaborative. A small toolchain used consistently beats a fancy one used inconsistently.

---

## Topic Guide

### Variables And Types

- strings hold text
- integers hold whole numbers
- floats hold decimals
- booleans hold true/false values
- `None` represents missing or unavailable data

### Flow Control

- `if` and `else` decide which path to take
- `for` loops iterate over collections
- `while` loops repeat until a condition changes
- nested conditions and loops should be used carefully because they can become hard to read

### Functions

- inputs are arguments
- outputs are return values
- defaults make common cases easier
- `*args` and `**kwargs` appear in flexible APIs
- small functions are easier to test than giant scripts

### File I/O

- JSON is common for configuration and API data
- CSV appears in data exports and spreadsheets
- plain text is useful for logs and documents
- always think about encoding and missing files

### Error Handling

- `try` and `except` should be used to handle expected failure modes
- errors should be specific when possible
- swallowing errors makes debugging much harder
- custom exceptions are useful when one problem needs a clear name

### Types And Validation

- type hints help readers and tools understand intent
- Pydantic checks that config and structured data match expectations
- validation is especially important when data comes from files or APIs

### Async And Concurrency

- async helps when waiting on multiple network calls
- concurrency is about overlapping waiting time
- async is not automatically faster for CPU-heavy work
- use it when the task is I/O-bound, especially API calls

### Logging And Testing

- logs should answer what happened, when, and with what inputs
- tests should protect small units of behavior
- pytest gives a repeatable way to check that code still behaves as expected

### Environment And Packaging

- Poetry manages dependencies and isolated environments
- Ruff keeps code style and linting fast
- Git records history and lets me work in safe increments
- Docker makes the runtime reproducible
- Typer turns functions into CLI commands cleanly

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

## A Mental Model For This Phase

Start with a script, then split it into functions, then split it into modules, then validate it with tests, then package it with tooling. That progression mirrors how a toy idea becomes a real codebase.

If something feels confusing, ask which layer the problem belongs to:

- language problem: syntax, types, data structures
- program problem: logic, control flow, functions
- project problem: file layout, dependencies, testing, packaging
- operational problem: logging, reproducibility, deployment

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

## Resource Notes

### Python Official Tutorial

Start with sections on data types, control flow, functions, and modules. The key idea is not memorizing the whole tutorial. It is learning the shape of Python programs and getting comfortable reading code that uses standard syntax.

### Pydantic Docs

Focus on fields, defaults, validation errors, nested models, and model parsing. This matters because AI projects constantly receive untrusted structured input from files, APIs, and models.

### asyncio Docs

Read enough to understand coroutines, tasks, `await`, and `gather`. The practical lesson is that a program can manage multiple waits at once without blocking.

### Poetry Docs

Focus on project creation, adding dependencies, and lockfiles. The point is reproducible environments, not package management trivia.

### Ruff Docs

Learn linting, formatting, and automatic fixes. This keeps early projects readable and reduces friction when the codebase grows.

---

## Questions I Want To Answer During This Phase

- When should I split code into modules instead of keeping it in one file?
- What is the practical difference between synchronous and asynchronous code?
- How much testing is enough for a small CLI?
- Which Python patterns show up over and over in AI engineering codebases?
