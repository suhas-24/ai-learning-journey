# Lab 1 - Build a Grounded QA Pipeline

This lab walks you through a minimal but real retrieval pipeline.

## Goal

Build a QA flow over a small corpus of Markdown documents and make the system return answers with citations.

## Steps

1. Create a corpus of 10 to 20 Markdown files.
2. Chunk the files by headings instead of raw character count.
3. Attach metadata such as `source_path`, `topic`, and `doc_type`.
4. Embed the chunks and store them.
5. Retrieve top candidates for a test question.
6. Feed only the best evidence into generation.
7. Return an answer that cites source paths.

## Command Skeleton

```bash
python ingest.py --input-dir docs/ --chunking markdown-headings
python query.py --question "Which workflow changed after incident 42?"
```

## What To Inspect

- the actual chunks retrieved
- whether citations point to real source material
- whether the system retrieved too much or too little context

## Deliverable

Write a short report with:

- one query that worked well
- one query that failed
- whether the failure was retrieval or generation

Then move to [Lab 2](./lab-02-debug-retrieval-failures.md).
