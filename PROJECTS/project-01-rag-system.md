# Project 1 - Production RAG System

**Phase:** Phase 5  
**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet

---

## Problem Statement

Build a knowledge-base agent over a real document corpus with hybrid retrieval, optional GraphRAG support, and a measurable evaluation layer. The project should prove that I understand retrieval quality, grounding, and system design well enough to ship more than a chatbot demo.

---

## Target User And Use Case

- primary user: a person who needs answers over a specific document collection
- example corpora: personal notes, technical manuals, research papers, or internal process docs
- key promise: answers should cite evidence and make it obvious where the information came from

---

## Planned Architecture

### Ingestion Layer

- load Markdown, PDF, and text documents
- normalize metadata
- chunk content intentionally by document type
- generate embeddings

### Retrieval Layer

- vector search
- BM25 or equivalent keyword retrieval
- hybrid fusion
- reranking for top results

### Knowledge Graph Layer

- extract important entities and relationships
- store graph connections for multi-hop queries
- use graph retrieval only when relationship reasoning matters

### Answer Layer

- grounded answer generation
- citation formatting
- confidence notes when retrieved context is weak

### Evaluation Layer

- RAGAS metrics
- manual review on difficult queries
- regression set for repeated testing

---

## Milestones

1. Build naive vector-search RAG over a small document set.
2. Add metadata filtering and better chunking.
3. Add hybrid search and reranking.
4. Add evaluation with RAGAS.
5. Add graph layer only if the corpus benefits from connected reasoning.

---

## Evaluation Targets

| Metric | Target | Why it matters |
| --- | --- | --- |
| Faithfulness | > 0.85 | answers must stay close to retrieved context |
| Answer Relevance | > 0.80 | answers should actually solve the question |
| Context Precision | > 0.75 | retrieved context should not be noisy |
| Context Recall | > 0.75 | important evidence should not be missed |

---

## Main Risks

- poor chunking creates bad retrieval no matter how good the model is
- graph extraction may add complexity without enough payoff
- evaluation can become shallow if I only test easy questions

---

## What "Done" Looks Like

- public repo with architecture, setup, and evaluation notes
- reproducible ingestion pipeline
- measurable retrieval quality
- grounded answers with visible sources
- clear explanation of where GraphRAG helped and where it did not

---

## Links

- **Planned GitHub repo:** to be created during Phase 5
- **Live demo:** optional, only if it adds value beyond a good walkthrough
- **Writeup goal:** one post explaining retrieval tradeoffs and evaluation findings
