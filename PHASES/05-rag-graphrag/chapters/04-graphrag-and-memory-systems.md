# Chapter 4 - GraphRAG and Memory Systems

`GraphRAG` means using a graph to help retrieval.

A `graph` is a set of things and the connections between them. If that sounds abstract, think of people and who knows whom, or services and what they depend on.

## What A Graph Is

In plain language, a graph is just a map of relationships.

The things are called `entities`.
The links between them are called `relationships`.

Example:

- `invoice-worker` is an entity
- `billing-platform` is an entity
- `invoice-worker` depends on `billing-platform` is a relationship

## When GraphRAG Helps

GraphRAG is useful when the question needs relationships, not just matching text.

Example questions:

- Which team owns the service that depends on the updated workflow?
- What systems connect to customer onboarding through identity verification?

Those questions need a chain of connections.

## What GraphRAG Usually Adds

- entity extraction, which means finding named things
- relation extraction, which means finding how those things connect
- graph storage, which means keeping those links in a searchable form
- graph traversal, which means walking the connections
- grounding, which means still pointing back to source text

The graph should help you find evidence. It should not replace evidence.

## When GraphRAG Is Too Much

Skip it when:

- the documents are mostly standalone
- the questions are simple lookup questions
- the entity extraction is not reliable yet

In those cases, better chunking and better retrieval are usually more valuable.

## Memory Types

Not every saved thing is the same kind of memory.
The names sound fancy, but each one is just a different way of saving information for later use.

- short-term memory: what the current conversation can see
- long-term factual memory: saved facts or summaries
- episodic memory: what happened in a past task or session
- procedural memory: instructions and playbooks to follow

## Simple Rule For Memory

Say what the storage is for before you call it memory.

Ask:

- is this a fact to recall later
- is this a past event
- is this an instruction
- is this just temporary working context

Different jobs need different storage.

## Example

Question: `What changed after the billing incident, and which downstream services were affected?`

A useful system might:

1. retrieve the postmortem and remediation notes
2. extract the services and incidents
3. follow the connections to downstream systems
4. fetch the source passages for those connections
5. answer with citations to the original documents

## Final Rule

Only reach for GraphRAG after chunking, metadata, hybrid search, and reranking are already working well.
