# Architecture - Production RAG System

This page explains how the project works from the ground up.

If a word below is new, read its short definition before looking at the diagram:

- a `corpus` is the document collection you search
- a `chunk` is a small piece of a document
- an `embedding` is a number-based representation of meaning
- `retrieval` means finding the chunks most likely to help
- `reranking` means sorting the first results again to improve quality
- a `citation` is the link back to the evidence used in the answer

## System Shape

```text
documents -> ingestion -> chunks + metadata -> retrieval -> reranking -> answer generation -> citations + eval logs
```

## Component Guide

### 1. Ingestion

Ingestion is the step that brings documents into the system.

It usually:

- loads Markdown, PDF, HTML, or text files
- records document name, section, and source path
- splits long documents into chunks
- writes chunk data and embeddings to storage

Why it exists:

- so the system can search documents consistently
- so later steps know where each answer came from

### 2. Retrieval

Retrieval is the step that finds the most useful chunks for a question.

It often combines:

- semantic search, which looks for similar meaning
- keyword search, which looks for exact words
- filters, which narrow results by date, topic, or source

Why it exists:

- the model should not answer from memory alone
- the answer should start with evidence

### 3. Reranking

Reranking is a second sorting step.

It takes the first retrieved results and reorders them so the strongest evidence appears first.

Why it exists:

- the first search pass is fast, but not always perfect
- reranking often helps with accuracy on harder questions

### 4. Answer Generation

This is the step where the model writes the response.

It should:

- use only retrieved evidence
- attach citations to source chunks
- say “I do not know” or ask for more detail when evidence is weak

Suggested output shape:

```json
{
  "answer": "The retention policy is 90 days for audit logs.",
  "citations": [
    {
      "source_path": "docs/security/logging.md",
      "section": "Retention",
      "chunk_id": "c_104"
    }
  ],
  "confidence_note": "High confidence because two policy sections agreed."
}
```

### 5. Evaluation

Evaluation is the step that checks whether the system is actually improving.

It should measure:

- whether retrieval found the right evidence
- whether the answer stayed grounded
- whether citations point to the right place

## Optional Graph Layer

Add a graph layer only if the corpus needs multi-step relationship reasoning.

If that sentence feels vague, think of a graph as a map of connected facts, like “who owns this policy” or “which concept depends on another one.”

## Decisions To Document

- why you chose your chunk size
- why hybrid retrieval was needed or not
- when reranking helped enough to justify its cost
- whether graph reasoning earned its complexity
