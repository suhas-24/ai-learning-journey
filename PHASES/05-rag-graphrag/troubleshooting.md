# Phase 05 Troubleshooting

Use this page when your retrieval system feels "smart" in demos but brittle in practice.

## Retrieved chunks look vaguely related but not useful

Likely causes:

- chunk size is too large and smears multiple topics together
- exact terms matter more than semantic similarity
- metadata filters are missing

Try:

- structure-aware chunking
- hybrid retrieval
- doc-type filters

## Citations point to the wrong section

Likely causes:

- chunk boundaries are too coarse
- reranking kept a related but less specific chunk
- answer synthesis merged evidence from several places carelessly

Try:

- smaller section-aware chunks
- tighter top-k after reranking
- explicit citation instructions in the generation prompt

## GraphRAG gives impressive diagrams but weak answers

This usually means:

- entity extraction quality is low
- graph traversal is not grounded back to source text
- the problem did not require graph structure

Use [Chapter 4](./chapters/04-graphrag-and-memory-systems.md) as a decision gate, not a justification layer.

## Memory store keeps retrieving stale or irrelevant facts

Check:

- whether records have timestamps
- whether you distinguish procedural memory from semantic memory
- whether old summaries are replacing primary evidence

Memory should support retrieval, not pollute it.
