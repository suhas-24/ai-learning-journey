# Lab 1 - Build a Grounded QA Pipeline

This lab helps you build a small question-answering system that is `grounded`, which means it uses evidence instead of guessing first. It looks up evidence first, then writes the answer.

## Goal

Build a QA flow over a small set of Markdown documents and make the system cite its sources.

## Before You Start

You do not need a huge dataset. Ten to twenty Markdown files is enough for this lab.

What matters is that the documents are real enough to expose search problems.

## Steps

1. Collect 10 to 20 Markdown files.
2. Split them by headings instead of by raw character count.
3. Add metadata such as `source_path`, `topic`, and `doc_type`.
4. Turn each chunk into a searchable form.
5. Ask one test question.
6. Look at the retrieved chunks before you look at the final answer.
7. Return an answer with source paths.

## Command Skeleton

```bash
python ingest.py --input-dir docs/ --chunking markdown-headings
python query.py --question "Which workflow changed after incident 42?"
```

## What To Inspect

- which chunks were retrieved
- whether the cited source actually matches the answer
- whether the system pulled too much or too little evidence
- whether the question needed exact-word search instead of meaning search

## Tiny Example

If the question says `incident 42`, the system should not hide the exact incident identifier inside a huge chunk. If the answer comes back without the right source path, the grounding is weak even if the wording sounds good.

## Deliverable

Write a short report with:

- one question that worked well
- one question that failed
- whether the failure came from retrieval or answer writing

Then move to [Lab 2](./lab-02-debug-retrieval-failures.md).
