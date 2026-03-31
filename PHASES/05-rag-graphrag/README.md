# Phase 05 - Retrieval, RAG, Graphs, and Memory

This phase explains how an AI system finds useful evidence before it answers.

A few words you will see a lot:

- `LLM` means large language model, which is a program trained on lots of text so it can predict and write text
- `retrieval` means finding the most relevant pieces of information from a collection
- a `chunk` is a small piece of a document
- an `embedding` is a numerical fingerprint for meaning
- `context` is the text and evidence the model can see at one time

`RAG` means retrieval-augmented generation. That simply means the system looks up evidence first, then writes an answer with that evidence.

## What You Will Learn

- how a retrieval pipeline works from start to finish
- why the wrong chunk can make a good model answer badly
- why exact-word search and meaning-based search often need each other
- when a graph helps and when it is just extra complexity
- how to tell whether a failure happened before or after generation

## Module Map

1. [Chapter 1: What Retrieval Is and Why It Fails](./chapters/01-retrieval-foundations-and-failure-modes.md)
2. [Chapter 2: Chunking, Indexing, and Metadata](./chapters/02-chunking-indexing-and-metadata-design.md)
3. [Chapter 3: Hybrid Retrieval, Reranking, and Evaluation](./chapters/03-hybrid-retrieval-reranking-and-evaluation.md)
4. [Chapter 4: GraphRAG and Memory Systems](./chapters/04-graphrag-and-memory-systems.md)
5. [Lab 1: Build a Grounded QA Pipeline](./labs/lab-01-build-a-grounded-qa-pipeline.md)
6. [Lab 2: Debug Retrieval Failures](./labs/lab-02-debug-retrieval-failures.md)
7. [Checkpoints](./checkpoints.md)
8. [Troubleshooting](./troubleshooting.md)

## How To Study This Phase

1. Start with Chapter 1 so the words are clear.
2. Study Chapter 2 to learn how documents are prepared for search.
3. Study Chapter 3 to learn how to improve the quality of the retrieved evidence.
4. Study Chapter 4 last, after the simpler retrieval ideas are already clear.
5. Do the labs and use the checkpoints to verify understanding.

## Simple Rule

Do not jump to GraphRAG first.

First make sure you can explain:

- what the question is
- what document should answer it
- how the right chunk is found
- how the answer stays grounded in that chunk
