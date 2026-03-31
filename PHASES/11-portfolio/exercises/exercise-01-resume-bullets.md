# Exercise 1 - Resume Bullets

## Goal

Turn project reality into resume bullets that are specific, technical, and defensible.

`Defensible` means you can explain why the bullet is true if someone asks you about it.

## Instructions

For each of the three portfolio projects, write:

- one long-form bullet for your master resume
- one shorter bullet for tailoring an application
- one interview note explaining the proof behind the bullet

## Quality Bar

Your bullet should include:

- the system type
- the technical choices
- the evaluation or operational proof

Weak:

```text
Built an AI assistant for enterprise workflows.
```

Stronger:

```text
Built a workflow agent with schema-validated tool calls, approval gates, and audit logging; tracked task completion, intervention rate, and latency across staged demo scenarios.
```

If that sentence feels too compressed, unpack it this way:

- `schema-validated` means the data shape was checked before use
- `approval gates` means the system paused for human review before risky steps
- `audit logging` means important actions were recorded so another person could inspect them later
- `intervention rate` means how often a human had to step in
- `latency` means how long one task took from start to finish

## Deliverable

Store your best three bullets in [snippets/resume-bullets-template.md](../snippets/resume-bullets-template.md).
