# Phase 5 - Advanced RAG + GraphRAG + Memory

**Status:** 🔴 Not Started  
**Started:** Not started yet  
**Completed:** Not completed yet  
**Estimated Duration:** 4 weeks

---

## Why This Phase Exists

Large language models are powerful at language, but they are not naturally aware of my files, my organization, my current data, or the facts that changed after training. Retrieval-Augmented Generation, or RAG, solves that by moving relevant information into the model's context at query time.

The hard part is not "can I fetch text." The hard part is building retrieval that stays accurate as the corpus grows, the documents vary, and the questions become more complex. This phase turns retrieval from a convenience feature into a system design problem.

---

## Chapter Map

### 5.1 Why Retrieval Beats Guessing

RAG exists because the model should not hallucinate answers that already live in a trusted source. If the information changes often, belongs to a private corpus, or needs citations, retrieval is better than hoping the model remembers it.

### 5.2 What An Embedding Actually Represents

An embedding is a numerical representation of meaning. Similar ideas should land near each other in vector space. That is why semantic search works: the system compares vectors instead of exact keywords.

### 5.3 How A Retrieval Pipeline Is Built

Documents are split into chunks, converted into embeddings, stored in a vector database, retrieved using similarity search, reranked, compressed, and then passed to generation. Each step can help or hurt.

### 5.4 Why Naive RAG Breaks

Naive RAG usually assumes that one chunk size, one retrieval method, and one answer prompt are enough. In practice, different document types need different chunking strategies, and different questions need different retrieval routes.

### 5.5 Why GraphRAG Exists

Some corpora are not just collections of text. They are networks of people, events, entities, and relationships. GraphRAG adds structure so the system can answer multi-hop questions that plain chunk retrieval might miss.

### 5.6 Memory As A System

Memory is not one thing. Short-term context, long-term vector memory, episodic logs, and procedural instructions all serve different jobs.

---

## Core Concepts

### Decision Ladder

- Prompting is for behavior and framing.
- RAG is for dynamic or corpus-specific knowledge.
- Fine-tuning is for stable behavior or style.
- RAG plus fine-tuning is for systems that need both current knowledge and consistent behavior.

### Retrieval Pipeline Pieces

- Chunking decides what a retrievable unit looks like.
- Embeddings turn chunks into meaning-based vectors.
- Metadata filtering narrows the search space.
- Hybrid retrieval mixes keyword search with vector search.
- Reranking scores the best candidates more carefully.
- Context compression keeps the final prompt within budget.

### Advanced RAG Patterns

- Query rewriting improves retrieval by restating the user question in a more searchable form.
- HyDE generates a hypothetical answer and uses that as a retrieval hint.
- Multi-query retrieval explores several phrasings at once.
- Result fusion merges multiple retrieval routes into one better context set.
- Self-reflection checks whether the retrieved context is enough before answering.

### GraphRAG And Memory

- Entity extraction identifies the important nouns and relations in documents.
- Community detection groups related nodes so the graph becomes searchable at higher levels.
- Multi-hop reasoning connects distant facts through shared nodes.
- Short-term memory is the active conversation.
- Long-term memory stores summaries and facts for future sessions.
- Episodic memory records what happened in past tasks.
- Procedural memory stores instructions and workflows.
- Semantic memory stores facts about the world or corpus.

---

## Learning Sequence

1. Build naive RAG over a tiny corpus and see where it fails.
2. Improve chunking and metadata before changing the model.
3. Add hybrid retrieval and reranking.
4. Evaluate retrieval and answer quality separately.
5. Add graph structure only if the corpus clearly benefits from relationships.
6. Introduce memory layers only after the retrieval path is stable.

---

## Phase Project: Personal Knowledge Base Agent With GraphRAG

**Project goal:** build a knowledge system over my own notes and documents that can answer grounded questions and explain where the answer came from.  
**Planned repo:** a dedicated Phase 5 repository  
**Current project status:** planned, not started

### Implementation Plan

- ingest Markdown notes, PDFs, and project documents
- extract metadata such as source, date, topic, and file type
- choose chunking by document shape, not by habit
- index chunks in a vector database
- add keyword search for cases where exact terms matter
- build a light knowledge graph for named entities and relationships
- decide when to retrieve, when to compress, and when to answer directly
- evaluate both retrieval quality and grounded answer quality

### What This Project Should Prove

- I can build more than a chatbot wrapper.
- I understand the difference between retrieval failure and generation failure.
- I can explain why a specific chunking and reranking strategy exists.
- I can use metrics to improve a RAG system instead of guessing.

---

## Exit Criteria

- I can explain embedding, retrieval, reranking, and generation in the correct order.
- I can compare vector search, hybrid search, and GraphRAG honestly.
- I can justify a chunking strategy for different document types.
- I can explain the role of each memory layer in an agent system.
- I can evaluate a RAG system with RAGAS or equivalent metrics.

---

## Common Traps To Avoid

- using one chunk size for every document type
- treating GraphRAG as a mandatory upgrade instead of a selective tool
- stuffing every retrieved chunk into the final prompt
- measuring only answer quality and ignoring retrieval quality
- over-compressing context until important evidence disappears

---

## Resources And What They Teach

| Resource | What It Teaches |
| --- | --- |
| LlamaIndex docs | How RAG pipelines are assembled from ingestion, indexing, retrieval, and synthesis |
| Qdrant or Weaviate docs | How vector collections, filtering, and query behavior work in practice |
| Microsoft GraphRAG repo | How entity graphs and multi-hop retrieval change the answer path |
| RAGAS docs | How to measure faithfulness, relevance, precision, and recall instead of relying on vibes |

---

## Questions I Want To Answer During This Phase

- Which retrieval failure patterns show up most often in my own corpus?
- When does GraphRAG beat plain retrieval for my kinds of questions?
- Which memory layer should store user history, agent history, and durable knowledge?
- How much complexity is actually justified before the system becomes hard to maintain?
