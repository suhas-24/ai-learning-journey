# Lab 2 - Debug Retrieval Failures

This lab is about diagnosis, not feature expansion.

## Goal

Take one failed QA example and isolate the exact failure point.

## Workflow

1. Save the question.
2. Save top-10 retrieved chunks with scores.
3. Mark which chunk should have been retrieved.
4. Test whether metadata filters removed it.
5. Test dense-only retrieval vs hybrid retrieval.
6. If the right chunk appears after retrieval but disappears later, inspect reranking and answer synthesis.

## Comparison Table

Use a table like this:

| Query | Expected source | Dense hit? | Sparse hit? | Reranked top 5? | Final answer grounded? |
| --- | --- | --- | --- | --- | --- |

## Optional GraphRAG Extension

Choose one multi-hop question and answer:

- did plain retrieval miss relationship structure?
- would a graph traversal help?
- what entity and edge types would you need?

If the answer is "no," that is a useful conclusion. It means GraphRAG is not yet justified.
