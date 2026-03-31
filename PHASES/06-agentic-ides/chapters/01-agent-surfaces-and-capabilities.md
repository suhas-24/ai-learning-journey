# Chapter 1 - What Coding Agents Do

A coding agent is a program that can help you change code. It may read files, suggest edits, write edits, or run commands you ask for.

That sounds broad because it is broad. The real question is not "what is the agent called?" The real question is "what kind of help do I need right now?"

## Start With The Simple Picture

Think of coding help like asking someone to work beside you at a desk.

- Sometimes you want help inside the editor while you are reading one file.
- Sometimes you want help across many files from the terminal.
- Sometimes you only want a little suggestion while you type.

Those three shapes are the main surfaces.

## Agentic IDEs

An `IDE` is an editor with extra coding features built in. An agentic IDE is an IDE that includes an agent in the editing flow.

In plain language, this means the agent is close to the code you are looking at.

Good for:

- reading and changing one file at the same time
- making small edits while you explore
- keeping the work close to your current cursor position

Harder for:

- big repo-wide tasks
- changes that need many command-line checks

## CLI Agents

`CLI` means command-line interface. That is the text-based terminal where you type commands.

A CLI agent works from the terminal. It is useful when the task needs many file reads, many edits, or many checks.

Good for:

- searching many files
- editing several files
- running tests and checks
- following a detailed task brief

Harder for:

- visual editing work
- vague requests with no boundary

## Editor Extensions

An editor extension is the smallest form of help. It lives inside your editor and gives you small assistance instead of a whole workflow.

Good for:

- quick explanations
- tiny rewrites
- local suggestions

Harder for:

- large changes across the repo
- work that needs strong structure and verification

## Simple Decision Rule

- choose an IDE agent when you want interactive help near one file
- choose a CLI agent when you want repo-wide work and checks
- choose an editor extension when you only need a small local assist

## Example

Suppose the task is: separate indexing code from query code in the retrieval layer.

The choice depends on the shape of the work:

- use a CLI agent if the change crosses several files and needs tests
- use an IDE agent if you are already inside the file and want quick back-and-forth
- use an extension if you only need help rewriting one small function

The label matters less than the fit. A good surface is the one that matches the size and risk of the task.

Next: [Chapter 2](./02-task-framing-context-and-prompt-design.md).
