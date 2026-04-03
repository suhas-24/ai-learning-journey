# Phase 05 - Finding Evidence Before Answering

This phase teaches one simple idea: sometimes a model should look up information before it answers.

That may sound obvious, but it matters a lot. A language model is good at writing and transforming text, but it does not automatically know your documents, your policies, or your internal facts. If you want it to answer using your own material, you first need a way to find the right material.

This phase uses a few new words:

- `retrieval` means finding useful information from a collection
- `chunk` means a small piece of a document
- `embedding` means a numerical way to represent meaning so similar text can be compared
- `vector database` means a search system that stores those numerical meaning-representations so similar text can be found quickly
- `context` means the text and evidence the model can see while it is answering
- `ranking` means putting the best matches first
- `citation` means a note that shows where an answer came from
- `RAG` means retrieval-augmented generation, which is a system that looks up evidence first and then asks the model to answer with that evidence
- `GraphRAG` means using relationships between things to help with retrieval

If any of those words feel new, that is normal. We define them slowly in the chapters below.

`QA` means question-answering, which is just a system that tries to answer a question in plain language after finding evidence.

## What This Phase Is Really About

The goal is not to make the model magically smarter.

The goal is to help the model see the right evidence at the right time.

Think of it like asking a person a question while also handing them the correct page from a manual. If you give them the wrong page, even a smart person can give a bad answer. Retrieval is the part that chooses the page.

## What You Will Learn

- what retrieval is in plain language
- why a model can sound confident and still be wrong
- why chunk size changes the quality of search
- how metadata helps the system find the right evidence
- why exact-word search and meaning-based search both matter
- when a graph helps and when it is unnecessary
- how to tell whether a problem happened before or after the model answered

## How To Use This Phase

1. Read Chapter 1 first so the basic idea is clear.
2. Read Chapter 2 to learn how documents are prepared for search.
3. Read Chapter 3 to learn how to improve search quality.
4. Read Chapter 4 after the simpler retrieval ideas make sense.
5. Do both labs.
6. Use the checkpoints and troubleshooting page when something feels fuzzy.

## Study Path

1. [Chapter 1: What Retrieval Is and Why It Fails](./chapters/01-retrieval-foundations-and-failure-modes.md)
2. [Chapter 2: Chunking, Indexing, and Metadata](./chapters/02-chunking-indexing-and-metadata-design.md)
3. [Chapter 3: Hybrid Retrieval, Reranking, and Evaluation](./chapters/03-hybrid-retrieval-reranking-and-evaluation.md)
4. [Chapter 4: GraphRAG and Memory Systems](./chapters/04-graphrag-and-memory-systems.md)

## Practice

- [Lab 1: Build a Grounded QA Pipeline](./labs/lab-01-build-a-grounded-qa-pipeline.md)
- [Lab 2: Debug Retrieval Failures](./labs/lab-02-debug-retrieval-failures.md)

## Snippets

- [chunking-config.json](./snippets/chunking-config.json)
- [hybrid-retriever.py](./snippets/hybrid-retriever.py)
- [entity-graph.cypher](./snippets/entity-graph.cypher)

## Success Standard

You are ready to move on when you can explain:

- what retrieval is
- what a chunk is
- why metadata matters
- what hybrid retrieval adds
- when a graph is worth the extra work
- how to tell whether a bad answer was caused by search or by writing
