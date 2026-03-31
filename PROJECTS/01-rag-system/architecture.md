# Architecture - Production RAG System

Before the diagram, here are the key words in simple language:

- a corpus is the set of documents you want to search
- a chunk is a smaller piece of a document
- an embedding is a numerical representation of text that helps similar text sit near each other
- retrieval means finding the most relevant chunks
- reranking means reordering those chunks to improve quality
- citations are the pointers that show where the answer came from

## System Overview

```text
documents -> ingestion -> chunk store + metadata -> hybrid retrieval -> reranking -> answer generation -> citations + eval logging
```

## Components

### 1. Ingestion

Responsibilities:

- load Markdown, PDF, HTML, or plain text
- normalize metadata
- preserve document id, section, and source path
- chunk content by semantic boundaries where possible
- embed chunks and write them to the vector store

Artifacts:

- ingestion manifest
- chunk dataset
- embedding index

### 2. Retrieval

Responsibilities:

- vector retrieval for semantic similarity
- lexical retrieval for exact terms and rare phrases
- fusion or rank combination
- metadata filtering by source, date, topic, or document type

Interfaces:

```python
def retrieve(query: str, k: int = 8, filters: dict | None = None) -> list[dict]:
    ...
```

Return fields should include:

- chunk_id
- document_id
- score
- source_path
- section_title
- chunk_text

### 3. Reranking

Responsibilities:

- reorder top retrieved results using a stronger model or heuristic
- discard noisy chunks
- improve precision before answer generation

### 4. Answer Generation

Responsibilities:

- answer only from retrieved evidence
- produce citations tied to source chunks
- abstain or ask for clarification when evidence is weak

Suggested output schema:

```json
{
  "answer": "The retention policy is 90 days for audit logs.",
  "citations": [
    {"source_path": "docs/security/logging.md", "section": "Retention", "chunk_id": "c_104"}
  ],
  "confidence_note": "High confidence because two policy sections agreed."
}
```

### 5. Evaluation

Responsibilities:

- score retrieval and answer quality
- log hard failures
- compare experiments across retrieval strategies

## Optional Graph Layer

Add a graph layer only if your corpus demands multi-hop reasoning across entities, policies, or relationships. Do not add it for resume theater.

Graph reasoning means following connections between things, like who owns what policy or how one concept links to another.

## Architecture Decisions To Document

- why you chose chunk size and overlap
- why hybrid retrieval was needed or not
- when reranking helped enough to justify cost
- whether graph reasoning earned its complexity
