# Phase 5 - Advanced RAG + GraphRAG + Memory

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 4 weeks

---

## Why This Phase Matters

Models do not know my private notes, my documents, or anything that changed after training. Retrieval-Augmented Generation is the bridge between model capability and real, current knowledge. The trap is that naive RAG looks easy in demos and breaks quickly in production.

This phase is about moving from "vector search toy" to "reliable knowledge system."

---

## Core Ideas To Master

### The Decision Ladder

- prompting for instructions and task framing
- RAG for current, factual, or domain-specific knowledge
- fine-tuning for stable behavior and style
- RAG plus fine-tuning when both behavior and knowledge quality matter

### Retrieval Pipeline Pieces

- chunking strategy
- embeddings and semantic search
- metadata filtering
- hybrid retrieval using keyword plus vector search
- reranking after retrieval
- context compression before generation

### Advanced RAG Patterns

- query rewriting
- HyDE
- multi-query retrieval
- hybrid search
- result fusion
- self-reflective re-retrieval when context is weak

### GraphRAG And Memory

- entity and relationship extraction
- multi-hop reasoning over connected information
- when graph structure adds value over simple chunks
- short-term, long-term, episodic, semantic, and procedural memory layers

---

## What I Need To Understand Deeply

- retrieval errors are different from generation errors
- good chunking is a product decision as much as a technical one
- recall and precision push against each other
- GraphRAG is only worth the extra complexity when relationships matter
- memory is not one thing; it is a stack with different purposes

---

## Phase Project: Personal Knowledge Base Agent With GraphRAG

**Project goal:** build a knowledge system over my own notes and documents that can answer grounded questions and explain where information came from.  
**Planned repo:** a dedicated Phase 5 repository  
**Current project status:** planned, not started

### Must-have capabilities

- ingest Markdown notes, PDFs, and project documents
- store embeddings in a vector database
- support hybrid search
- build a lightweight knowledge graph for important entities and relationships
- decide when to retrieve instead of retrieving blindly every time
- evaluate answer quality and retrieval quality separately

### What this project should prove

- I can build more than a chatbot wrapper
- I understand retrieval quality, not just model prompting
- I can evaluate RAG systems with metrics instead of vibes

---

## Exit Criteria

- I can explain the difference between embedding, retrieval, reranking, and generation.
- I can compare vector search, hybrid search, and GraphRAG honestly.
- I can justify a chunking strategy instead of copying one.
- I can evaluate a RAG system with RAGAS or equivalent metrics.
- I understand the practical role of memory layers in agents.

---

## Common Traps To Avoid

- treating all document types as if one chunk size fits them all
- using GraphRAG because it sounds advanced, not because the data needs it
- stuffing every retrieved chunk into the final prompt
- evaluating answers without checking whether the retrieval step was the real problem

---

## Resources For This Phase

| Resource | Why it matters | How I should use it |
| --- | --- | --- |
| LlamaIndex docs | Strong conceptual material for RAG pipelines | Build one simple pipeline, then add complexity one step at a time |
| Qdrant or Weaviate docs | Needed for real retrieval infrastructure | Focus on collections, metadata, and query patterns |
| Microsoft GraphRAG repo | Best practical starting point for graph-based retrieval | Understand when it is worth the complexity |
| RAGAS docs | Measurement discipline starts here | Use metrics to guide iteration |

---

## Questions I Want To Answer During This Phase

- What retrieval mistakes show up most often in my own data?
- When does GraphRAG outperform simpler retrieval for the kinds of questions I care about?
- Which memory layer should store user history, agent history, and durable knowledge?
- How much complexity is actually justified before a system becomes hard to maintain?
