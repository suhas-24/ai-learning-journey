# Phase 05 Troubleshooting

Use this page when the system feels impressive in a demo but weak in practice.

## The retrieved chunks are related but not useful

Likely reasons:

- the chunks are too large
- exact words matter more than meaning
- metadata is missing

Try:

- chunk by section
- use hybrid search
- add filters based on document type

## The citation points to the wrong section

Likely reasons:

- the chunks are too coarse
- reranking kept a related but less specific chunk
- answer writing merged evidence too loosely

Try:

- smaller chunks
- tighter reranking
- explicit citation instructions

## GraphRAG looks fancy but answers are weak

Likely reasons:

- entity extraction is poor
- the graph is not grounded in source text
- the question did not need a graph

Use Chapter 4 as a decision point, not a justification for complexity.

## The memory store returns stale facts

Check:

- whether the records have timestamps
- whether you separated facts from instructions
- whether old summaries are hiding the original evidence

Memory should help retrieval, not confuse it.
