# Phase 05 Checkpoints

## Concept Checks

You are ready to move on if you can explain:

1. the difference between retrieval failure and answer failure
2. why chunk size should change with the document
3. when exact-word search and meaning search work best together
4. what reranking adds
5. when a graph is actually worth the extra work
6. why memory is more than one thing

If those words still feel fuzzy, return to the chapter that defines them and read the tiny example again.

## Practical Checks

- I can show the retrieved chunks for a question.
- I can explain why a metadata field matters.
- I can compare meaning-based search with hybrid search.
- I can tell whether a failure happened before or after reranking.
- I can explain what the graph edge points back to.

These checks matter because a working demo is not the same thing as understanding.

## Mini Quiz

Question: A question has exact error codes and plain-English wording. What search style is a strong default?

Expected answer: `Hybrid retrieval`, because it handles both kinds of signal.

Question: Your system only answers short FAQ questions from independent notes. Should you add GraphRAG first?

Expected answer: No. Improve chunking, metadata, and search first.

Question: If the model sounds confident but cites the wrong source, is the problem automatically the model?

Expected answer: No. First inspect retrieval, chunking, and ranking.
