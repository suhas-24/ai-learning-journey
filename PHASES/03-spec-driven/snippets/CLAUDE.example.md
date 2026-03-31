# CLAUDE.md Example

A repo rule file like `CLAUDE.md` is a shared instruction layer. It holds broad rules that apply across many tasks instead of one narrow assignment.

## Repo Rules

- Prefer ASCII in edited files unless the file already relies on other characters.
- Add runnable examples in learning modules when a concept would otherwise stay abstract.
- Use concise summaries at the end of each worker pass.

## Review Standard

Prioritize correctness, missing learner steps, and hidden failure modes over stylistic polish.

## Coordination Rule

If multiple workers share the repo, each worker must stay inside its owned directory unless the conductor explicitly reassigns ownership.
