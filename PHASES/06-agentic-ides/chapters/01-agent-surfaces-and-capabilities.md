# Chapter 1 - Agent Surfaces and Capabilities

Not all coding agents behave the same way. The tool surface changes the rhythm of collaboration, the available context, and the kinds of mistakes you should expect.

## Agentic IDEs

Examples include editors or IDEs with deep built-in model workflows.

Strong at:

- interactive back-and-forth while reading code
- inline edits and fast diffs
- staying close to the visible file context

Weak at:

- large repo orchestration unless rules are strong
- non-interactive automation

## CLI Agents

CLI agents work well when tasks are repo-scoped, command-heavy, or need deliberate planning.

Strong at:

- searching a repo
- editing multiple files
- running tests or checks
- producing explicit plans and summaries

Weak at:

- highly visual UI work without extra tooling
- ambiguous tasks with missing repo context

## Editor Extensions

Extensions are useful when convenience matters, but the workflow often depends heavily on prompt quality.

Good use cases:

- quick explanations
- lightweight transformations
- local refactors in a file you already understand

## Decision Rule

Choose the surface that best matches the task:

- IDE agent for interactive code exploration
- CLI agent for repo-wide implementation and verification
- extension for small in-editor assistance

## Worked Example

Task: "Refactor the retrieval pipeline to separate indexing from querying."

Best fit:

- `CLI agent` if the change crosses several files and needs tests
- `IDE agent` if you are already inside the retrieval module and want iterative pair-programming

The tool matters less than whether the scope and verification loop are explicit.

Continue to [Chapter 2](./02-task-framing-context-and-prompt-design.md).
