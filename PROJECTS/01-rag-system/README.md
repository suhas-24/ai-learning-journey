# Project 1 - Production RAG System

Build a document-grounded question answering system that can ingest a real corpus, retrieve relevant evidence, generate answers with citations, and prove quality through evaluation instead of demos alone.

A RAG system, short for retrieval-augmented generation, is a setup where the model first looks up relevant text and then uses that text to answer. The retrieval part finds the evidence. The generation part turns that evidence into a response. Grounding means the answer stays tied to the evidence instead of guessing.

## Project Goal

The project is successful when a reviewer can see:

- a reproducible ingestion pipeline
- intentional retrieval design
- answer grounding with visible evidence
- measurable quality on a fixed eval set

In plain language, the project should show that the system can find the right information and use it responsibly.

## Target Users

- internal teams searching policy or operations documents
- technical users searching manuals or runbooks
- research users querying papers or long-form notes

## Suggested Stack

- Python + FastAPI
- vector database of your choice
- BM25 or equivalent lexical retrieval
- reranker
- optional graph store for relationship-heavy corpora
- eval toolkit such as RAGAS plus manual review

If those names are new, use this plain-English translation:

- `FastAPI` is a Python web framework that makes it easier to expose your system through an API
- a `vector database` stores embeddings, which are number-based representations of text meaning
- `BM25` is a classic keyword-search method that works well when exact words matter
- `lexical retrieval` means searching by words and terms rather than by meaning alone
- a `reranker` is a second scoring step that reorders retrieved results so the most useful evidence rises to the top
- a `graph store` keeps entities and relationships when the knowledge is better represented as connected facts
- `RAGAS` is a toolkit people often use to evaluate retrieval-augmented systems

## Recommended Folder Layout

```text
01-rag-system/
├── README.md
├── architecture.md
├── build-plan.md
├── eval-plan.md
└── rubric.md
```

When you implement the repo itself, aim for:

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
2. Build a baseline vector-search pipeline.
3. Add hybrid retrieval and reranking.
4. Add grounded answer generation with citations.
5. Build an eval set and track quality.
6. Add optional graph reasoning only if the corpus needs it.

`Vector-search` means retrieving documents by meaning using embeddings. `Hybrid retrieval` means combining meaning-based search with keyword-based search so you get the strengths of both.

## Core Artifacts

- ingestion config
- sample corpus
- retrieval pipeline
- answer schema
- eval set
- metric report
- short demo or walkthrough

## Success Criteria

- answers cite the exact source chunks used
- retrieval quality is measured, not guessed
- the repo explains retrieval tradeoffs clearly
- a stranger can run or understand the system without private context

## Demo Guidance

Show:

- one retrieval success case
- one hard case
- one evaluation summary
- one limitation such as weak results on comparison questions or sparse documents
