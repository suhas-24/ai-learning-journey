# Chapter 4 - GraphRAG and Memory Systems

GraphRAG is not "better RAG" by default. It is useful when your corpus contains entities and relationships that matter for answering multi-hop questions.

## When GraphRAG Helps

GraphRAG is strong when questions look like:

- "Which team owns the service that depends on the workflow updated after the March incident?"
- "What systems are connected to customer onboarding through identity verification?"

These questions require traversing relationships, not just matching paragraphs.

## GraphRAG Building Blocks

- entity extraction
- relation extraction
- graph storage
- graph traversal or neighborhood retrieval
- text grounding from linked source passages

GraphRAG should still point back to textual evidence. The graph guides retrieval. It does not replace the need for source-backed answers.

## When GraphRAG Is Overkill

Avoid GraphRAG when:

- your corpus is mostly standalone notes
- questions are simple FAQ-style lookups
- you cannot maintain high-quality entity extraction

In those cases, better chunking and hybrid retrieval usually deliver more value per hour.

## Memory Types

### Short-term memory

The active conversation context.

### Long-term semantic memory

Stored facts, summaries, and embeddings from prior work.

### Episodic memory

Records of what happened in previous tasks or sessions.

### Procedural memory

Instructions, playbooks, and reusable workflows.

## Design Rule for Memory

Do not call every persistence layer "memory." Name the job first:

- facts to recall later
- past events to reference
- instructions to follow
- temporary context for the current task

Different jobs need different storage and retrieval patterns.

## Worked Example

Question: "What changed after the billing incident, and which downstream services were affected?"

A useful system might:

1. retrieve the postmortem and remediation tickets
2. extract incident, service, and dependency nodes
3. traverse connected services
4. fetch the source passages for each edge
5. answer with citations to the original documents

## Final Principle

Reach for GraphRAG only after dense retrieval, sparse retrieval, reranking, and metadata design are already competent. Complexity should earn its keep.
