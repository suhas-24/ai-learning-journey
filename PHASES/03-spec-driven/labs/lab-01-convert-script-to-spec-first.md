# Lab 1 - Convert a Script to Spec-First

This lab helps you feel the difference between hidden behavior and visible behavior.

## Goal

Take a small script or workflow you already understand and write the behavior contract before you touch implementation.

## Suggested Scenario

Imagine a file review assistant that:

- reads markdown files
- flags missing examples
- avoids touching code files

## Deliverables

Write:

- an `AGENTS.md`-style role description
- a repo-level rules file or excerpt
- one reusable skill describing the review workflow

## Questions To Answer

- what does this agent own?
- what must it never do?
- when must it escalate?
- what counts as "done"?

## Stretch Goal

Change one behavior only by editing the spec, then describe what implementation should follow from that change.
