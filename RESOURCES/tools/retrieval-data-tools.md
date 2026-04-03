# Retrieval And Data Tools

This guide covers the tools that teach how knowledge is stored, indexed, retrieved, and assembled into grounded answers. These tools matter because most RAG failures come from data and retrieval design, not from the final prompt alone.

If `RAG` is a new term, it means retrieval-augmented generation. That is a system where the model looks up useful information before it writes the answer.

`Semantic search` means search by meaning instead of exact word matching.

## How To Use This Guide

- Start here when the model needs outside evidence to answer well.
- Learn how the data is prepared before you learn the final answer logic.
- Keep separating retrieval quality from generation quality.

## ChromaDB

### What it teaches

ChromaDB is good for learning local vector retrieval. It makes semantic search concrete and lets you inspect how embeddings and metadata affect the quality of retrieval.

### Core topics and subtopics

- Vector storage and similarity search.
- Collections and document organization.
- Metadata filtering and query refinement.
- Prototype retrieval loops.

### Best phases

- Phase 5.

### Watch for

- The value here is understanding the retrieval path, not just spinning up a local database.

## Qdrant

### What it teaches

Qdrant teaches production-oriented vector retrieval. It introduces the operational side of collections, filtering, query control, and scaling retrieval behavior beyond a toy project.

### Core topics and subtopics

- Collection design and indexing strategy.
- Payload metadata and filtering.
- Query tuning and retrieval tradeoffs.
- Operational thinking for deployed retrieval systems.

### Best phases

- Phase 5.
- Useful again in Phase 9 when evaluating retrieval behavior in production-like settings.

### Watch for

- Production retrieval is less about one perfect query and more about keeping quality stable as the data grows.

## LlamaIndex

### What it teaches

LlamaIndex teaches the flow from ingestion to answer generation. It helps you reason about readers, nodes, indexes, retrievers, and response synthesis as separate moving parts.

### Core topics and subtopics

- Document ingestion and parsing.
- Chunking and node creation.
- Index construction and retrieval strategies.
- Query engines and response synthesis.

### Best phases

- Phase 5.

### Watch for

- This is a good place to learn the pipeline shape: input data in, grounded answer out, with several steps in between.

## Microsoft GraphRAG

### What it teaches

GraphRAG teaches multi-hop retrieval and entity-centric reasoning. It is useful when a normal vector search finds locally similar text but misses the relationships across a corpus.

### Core topics and subtopics

- Entity extraction and relationship modeling.
- Graph construction from documents.
- Multi-hop query logic and connected reasoning.
- When graph structure outperforms flat chunk retrieval.

### Best phases

- Phase 5.
- Useful again in Phase 9 when evaluating hard retrieval cases.

### Watch for

- Graph retrieval is useful when relationships matter. It is not automatically better than simpler retrieval.

## Companion Guides

- [../courses/rag-and-retrieval-courses.md](../courses/rag-and-retrieval-courses.md)
- [evals-observability-tools.md](./evals-observability-tools.md)
- [../books/ai-engineering-and-llm-systems.md](../books/ai-engineering-and-llm-systems.md)
