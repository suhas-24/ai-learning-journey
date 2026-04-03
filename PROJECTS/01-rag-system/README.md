# Project 1 - Production RAG System

This project teaches how to build a question-answering system that answers from documents instead of from guesswork.

If the term `RAG` is new, it means `retrieval-augmented generation`. That sounds complicated, but the idea is simple:

- `retrieval` means finding useful text first
- `generation` means having the model write the answer after it sees that text
- `grounded` means the answer stays tied to the evidence instead of inventing facts

Think of it like this: before answering, the system checks its notes.

If the word `citation` is new, it is just a pointer back to the place where the evidence came from.
If the word `corpus` is new, it means the document library your system searches.

## What You Will Build

You will build a system that can:

- ingest a real document collection
- break documents into smaller pieces called `chunks`
- search for the most relevant chunks
- generate an answer with citations
- evaluate whether the answer is actually good

The project starts simple on purpose. You first build a baseline that can find evidence. Then you make the answer clearer, more trustworthy, and easier to inspect.

## Before You Start

Here are the main words in plain language:

- a `corpus` is the set of documents you want to search
- a `chunk` is a small piece of a document
- an `embedding` is a numeric representation of text meaning
- a `vector database` is a place to store and search embeddings
- `retrieval` means finding the most useful evidence
- `reranking` means reordering results so the best evidence rises to the top
- a `citation` points back to the source chunk used for the answer

## Why This Project Matters

Many beginner AI demos stop at “the answer sounds nice.” This project goes further. It shows whether the system can:

- find the right source material
- avoid unsupported claims
- explain where its answer came from
- improve when you tune the retrieval step

If those ideas are new, imagine the system as a careful student. It should look up the notes, pick the right passages, and then answer with receipts instead of vibes.

## How To Use This Folder

- `README.md` explains the project in simple language
- `architecture.md` shows how the parts fit together
- `build-plan.md` gives the build order
- `eval-plan.md` explains how to measure quality
- `rubric.md` gives a quick readiness check

## Suggested Repo Layout

```text
01-rag-system/
├── README.md
├── architecture.md
├── build-plan.md
├── eval-plan.md
└── rubric.md
```

When you turn this into code, a clear layout often looks like this:

```text
src/
  ingest/
  retrieve/
  answer/
  eval/
data/
configs/
tests/
reports/
```

## Milestones

1. Ingest and normalize a real document corpus.
2. Build a baseline search flow that returns chunks.
3. Add hybrid retrieval and reranking.
4. Generate answers with visible citations.
5. Create an eval set and measure quality.
6. Add graph reasoning only if the documents truly need it.

## Core Artifacts

- ingestion config
- sample corpus
- retrieval pipeline
- answer schema
- eval set
- metric report
- short demo or walkthrough

## Success Looks Like

A good reviewer should be able to see that:

- the system uses evidence, not vibes
- retrieval quality is measured, not guessed
- citations are easy to inspect
- the repo explains the tradeoffs clearly

## Demo Guidance

Show one example of each:

- a question the baseline system answers well
- a hard question that reveals a weakness
- a retrieval improvement
- an eval result that proves the improvement
- one limitation the system still has
