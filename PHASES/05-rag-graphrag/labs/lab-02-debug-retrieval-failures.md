# Lab 2 - Debug Retrieval Failures

This lab is about diagnosis.

## Goal

Take one failed question and find the exact step where the system went wrong.

## Workflow

1. Save the question.
2. Save the top retrieved chunks and their scores.
3. Mark which chunk should have won.
4. Test whether metadata filters removed it.
5. Compare meaning-based search with exact-word search.
6. If the right chunk appears early but disappears later, inspect reranking and answer writing.

## Comparison Table

Use a table like this:

| Query | Expected source | Meaning hit? | Exact-word hit? | Reranked top 5? | Final answer grounded? |
| --- | --- | --- | --- | --- | --- |

## Optional Graph Exercise

Pick one question that needs more than one hop.

Ask:

- did plain retrieval miss a relationship?
- would a graph help?
- what things and connections would the graph need?

If the answer is no, that is still a good result.
