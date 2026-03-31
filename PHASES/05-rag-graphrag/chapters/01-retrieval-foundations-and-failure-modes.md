# Chapter 1 - Retrieval Foundations and Failure Modes

RAG exists because the model should not guess facts that can be retrieved from a trusted corpus. That sounds simple, but the engineering challenge starts before generation: bad retrieval means the model never sees the right evidence.

## Core Pipeline

A retrieval pipeline usually has these stages:

1. ingest documents
2. split them into chunks
3. generate embeddings or sparse indexes
4. retrieve candidates
5. rerank or filter results
6. compress context
7. generate an answer with citations

If you cannot name the stage that failed, you cannot fix the system responsibly.

## Retrieval Failure vs Generation Failure

### Retrieval failure

The right evidence never reaches the model.

Examples:

- chunk boundaries separated the crucial sentence from its context
- the query used exact jargon but vector retrieval ignored it
- metadata filters removed the best document

### Generation failure

The model had the right evidence but answered badly anyway.

Examples:

- it ignored the cited chunk
- the synthesis prompt over-compressed the evidence
- the model stitched together conflicting passages incorrectly

## Worked Example

User question: "Which service owns the nightly billing retry workflow?"

Bad answer path:

- documents are chunked every 1,000 characters
- the ownership table is split away from the workflow description
- vector search retrieves a general billing design doc
- the model guesses the wrong team name

Better answer path:

- chunk by section boundaries
- retain metadata like `service`, `team`, and `doc_type`
- use hybrid retrieval because ownership names are exact-match sensitive
- rerank by relevance before answering

## Why Naive RAG Breaks

Naive RAG often assumes:

- one chunk size fits every document
- semantic search is enough for all queries
- top-k retrieval quality is obvious from answer quality
- more context always helps

All four assumptions are weak.

## Diagnostic Questions

When a grounded answer looks wrong, ask:

1. Was the right document ingested at all?
2. Was it chunked in a retrievable way?
3. Was the query represented well?
4. Was retrieval mode appropriate for the query?
5. Did reranking select the best evidence?
6. Did answer synthesis distort the evidence?

## Retrieval-First Mindset

Before changing the model or prompt, inspect:

- retrieved chunks
- scores
- metadata filters
- missing evidence patterns

That discipline prevents wasted work and makes the system explainable.

Continue to [Chapter 2](./02-chunking-indexing-and-metadata-design.md).
