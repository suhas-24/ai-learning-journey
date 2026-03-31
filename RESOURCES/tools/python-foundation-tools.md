# Python Foundation Tools

This guide covers the tools that teach build discipline. These tools matter because they turn a folder of scripts into a maintainable project with repeatable behavior.

## Poetry

### What it teaches

Poetry teaches dependency discipline. It shows how a Python project declares its packages, isolates its environment, and makes installs reproducible across machines.

### Major topics and subtopics

- `pyproject.toml` structure and dependency declaration.
- Lock files and reproducible installs.
- Virtual environment management.
- Dependency groups for dev and runtime separation.

### Best phases

- Phase 1.
- Reused in every later phase that adds tools, APIs, or evaluation libraries.

## Ruff

### What it teaches

Ruff teaches fast feedback and consistency. The main idea is not style for style's sake. It is reducing noise so real logic errors are easier to see.

### Major topics and subtopics

- Lint rules and common mistake detection.
- Formatting and consistent code shape.
- Import hygiene and unused code cleanup.

### Best phases

- Phase 1 onward.

## Pyright

### What it teaches

Pyright teaches type discipline. In AI systems, types are a quiet form of reliability because they make tool contracts, response shapes, and state objects easier to reason about.

### Major topics and subtopics

- Type annotations and data models.
- Narrowing and error detection before runtime.
- Interface clarity for functions and APIs.

### Best phases

- Phase 1.
- Especially valuable again in Phases 3, 4, and 7.

## Typer

### What it teaches

Typer teaches command-line design. It helps you think about inputs, outputs, flags, and help text as part of the user experience of a technical tool.

### Major topics and subtopics

- Commands and subcommands.
- Arguments, options, and defaults.
- Help text and discoverability.
- Structured output for automation.

### Best phases

- Phase 1 and Phase 4.

## Git And GitHub Actions

### What they teach

These tools teach versioned thinking. They force you to make small decisions explicit, automate checks, and build a habit of repeatability.

### Major topics and subtopics

- Branching and commit hygiene.
- Remote collaboration and review.
- Continuous integration and automatic checks.
- Regression prevention through automation.

### Best phases

- Phase 1 onward.

## Companion Guides

- [model-api-tools.md](./model-api-tools.md)
- [../books/ml-foundations-and-thinking.md](../books/ml-foundations-and-thinking.md)
