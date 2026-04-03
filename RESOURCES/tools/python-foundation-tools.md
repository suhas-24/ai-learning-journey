# Python Foundation Tools

This guide covers the tools that teach build discipline. These tools matter because they turn a folder of scripts into a maintainable project with repeatable behavior.

## How To Read This Guide

- Start with the problem the tool solves before you worry about the command syntax.
- Ask what part of the project the tool makes more reliable.
- Use one small project to learn the difference between "works once" and "keeps working."

## Poetry

### What it teaches

Poetry teaches dependency discipline. It shows how a Python project declares its packages, isolates its environment, and makes installs reproducible across machines.

### Core topics and subtopics

- `pyproject.toml` structure and dependency declaration.
- Lock files and reproducible installs.
- Virtual environment management.
- Dependency groups for dev and runtime separation.

### Best phases

- Phase 1.
- Reused in every later phase that adds tools, APIs, or evaluation libraries.

### Watch for

- The real lesson is project repeatability, not just one package manager.

## Ruff

### What it teaches

Ruff teaches fast feedback and consistency. The point is not style for style's sake. It is reducing noise so real logic errors are easier to see.

### Core topics and subtopics

- Lint rules and common mistake detection.
- Formatting and consistent code shape.
- Import hygiene and unused code cleanup.

### Best phases

- Phase 1 onward.

### Watch for

- Formatting should make the code easier to read, not just more uniform.

## Pyright

### What it teaches

Pyright teaches type discipline. A `type` is a label that says what kind of value something should be. In AI systems, types are a quiet form of reliability because they make tool contracts, response shapes, and state objects easier to reason about.

### Core topics and subtopics

- Type annotations and data models.
- Narrowing and error detection before runtime.
- Interface clarity for functions and APIs.

### Best phases

- Phase 1.
- Especially valuable again in Phases 3, 4, and 7.

### Watch for

- Type checks help most when you use them to describe the shape of the data you really expect.

## Typer

### What it teaches

Typer teaches command-line design. It helps you think about inputs, outputs, flags, and help text as part of the user experience of a technical tool.

### Core topics and subtopics

- Commands and subcommands.
- Arguments, options, and defaults.
- Help text and discoverability.
- Structured output for automation.

### Best phases

- Phase 1 and Phase 4.

### Watch for

- A good CLI should feel obvious to a new user without needing a tutorial.

## Git And GitHub Actions

### What they teach

These tools teach versioned thinking. They force you to make small decisions explicit, automate checks, and build a habit of repeatability.

### Core topics and subtopics

- Branching and commit hygiene.
- Remote collaboration and review.
- Continuous integration and automatic checks.
- Regression prevention through automation.

### Best phases

- Phase 1 onward.

### Watch for

- Version control is not only about saving code. It is about making change reviewable.

## Companion Guides

- [model-api-tools.md](./model-api-tools.md)
- [../books/ml-foundations-and-thinking.md](../books/ml-foundations-and-thinking.md)
