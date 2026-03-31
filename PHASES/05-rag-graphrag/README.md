# Phase 05 - Retrieval, Advanced RAG, GraphRAG, and Memory

This module turns retrieval into a systems discipline. Instead of treating RAG as "vector search plus a prompt," you will learn how document shape, chunking, indexing, reranking, graph structure, and memory layers influence answer quality.

## What You Will Learn

- how a retrieval pipeline is actually assembled end to end
- why naive chunking and top-k retrieval often fail
- when hybrid search and reranking outperform plain vector search
- when GraphRAG adds value and when it only adds complexity
- how to separate retrieval failure from generation failure

## Module Map

1. [Chapter 1: Retrieval Foundations and Failure Modes](./chapters/01-retrieval-foundations-and-failure-modes.md)
2. [Chapter 2: Chunking, Indexing, and Metadata Design](./chapters/02-chunking-indexing-and-metadata-design.md)
3. [Chapter 3: Hybrid Retrieval, Reranking, and Evaluation](./chapters/03-hybrid-retrieval-reranking-and-evaluation.md)
4. [Chapter 4: GraphRAG and Memory Systems](./chapters/04-graphrag-and-memory-systems.md)
5. [Labs](./labs/lab-01-build-a-grounded-qa-pipeline.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

## Guiding Principle

The question is never "Should I use RAG?" The real question is "Which retrieval design best fits my corpus, my questions, and my reliability target?"

## Suggested Workflow

1. Read Chapter 1 and list three ways retrieval can fail before generation even starts.
2. Read Chapter 2 and inspect [snippets/chunking-config.json](./snippets/chunking-config.json).
3. Read Chapter 3 and compare vector-only vs hybrid retrieval using [snippets/hybrid-retriever.py](./snippets/hybrid-retriever.py).
4. Read Chapter 4 before deciding that GraphRAG or long-term memory belong in your system.
5. Complete both labs and grade yourself with [checkpoints.md](./checkpoints.md).
