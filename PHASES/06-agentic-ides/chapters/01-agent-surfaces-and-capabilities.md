# Chapter 1 - What Coding Agents Do

A coding agent is a program that can read code, suggest changes, and sometimes run commands.

The exact experience depends on where you use it.

## Agentic IDEs

An agentic IDE is an editor that has the agent built into the editing flow.

Good for:

- reading a file and editing it at the same time
- quick back-and-forth while you are exploring code
- staying close to the file you are working in

Harder for:

- big repo-wide jobs
- workflows that need a lot of command-line automation

## CLI Agents

A CLI agent runs from the terminal.

Good for:

- searching many files
- editing several files
- running tests and checks
- following explicit instructions

Harder for:

- visual UI work
- tasks with weak boundaries

## Editor Extensions

An editor extension is the lightest form of help.

Good for:

- quick explanations
- small rewrites
- simple local changes

Harder for:

- big changes across the repo
- complicated workflows that need strong structure

## Simple Decision

- choose an IDE agent for interactive exploration
- choose a CLI agent for repo-wide work and verification
- choose an extension for small in-editor help

## Example

Task: refactor the retrieval pipeline so indexing and querying are separate.

- use a CLI agent if the change crosses several files and needs tests
- use an IDE agent if you are already inside the file and want interactive help

The important part is not the tool label. The important part is whether the task is clear and the checks are clear.

Next: [Chapter 2](./02-task-framing-context-and-prompt-design.md).
