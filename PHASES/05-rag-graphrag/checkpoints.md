# Phase 05 Checkpoints

## Concept Checks

You are ready to advance if you can explain:

1. the difference between retrieval failure and generation failure
2. why chunking strategy should vary by document type
3. when hybrid retrieval beats vector-only retrieval
4. what reranking adds to the pipeline
5. when GraphRAG is justified and when it is not
6. why memory is not one single storage concept

## Practical Checks

- I can show retrieved chunks for a question instead of only showing the final answer.
- I can justify a metadata schema that actually drives filtering.
- I can compare dense retrieval and hybrid retrieval on the same query set.
- I can identify whether a failure happened before or after reranking.
- I can explain what evidence a graph edge should map back to.

## Mini Quiz

Question: A query includes exact error codes and fuzzy natural-language intent. Which retrieval approach is a strong default?

Expected answer: `Hybrid retrieval`, because it captures both lexical and semantic signals.

Question: Your system answers simple FAQ questions over independent notes. Should you add GraphRAG first?

Expected answer: No. Improve chunking, metadata, hybrid retrieval, and reranking first.
