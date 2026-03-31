# RAG And Retrieval Courses

This guide covers the resources that teach how retrieval improves answer quality, where it fails, and how to evaluate the quality of grounded responses.

If the phrase `retrieval` is new, think of it as "find the right information before the model answers." `Grounding` means the answer is tied back to that information instead of being a guess.

## Building And Evaluating Advanced RAG

### What it teaches

This course teaches retrieval as a design problem, not a checkbox. It helps you see how chunk size, embedding quality, retrieval strategy, and context assembly change the final answer.

An `embedding` is a number pattern that stands in for meaning. Similar text should end up with similar number patterns, which is why retrieval can search by meaning instead of exact words alone.

### Major topics and subtopics

- Chunking strategy: how document slicing changes recall and context quality.
- Embeddings: why representation quality affects search quality.
- Retriever design: similarity search, filtering, and ranking decisions.
- Grounding: how retrieved context is turned into an answer.
- RAG evaluation: faithfulness, relevance, and failure analysis.

### When to use it

- Best in Phase 5.
- Revisit in Phase 9 when you need better evaluation discipline.

## How To Study Retrieval Through Courses

- Run the same query against different chunking strategies.
- Inspect a bad answer by tracing which documents were retrieved.
- Separate retrieval failure from generation failure. They are not the same problem.

## Companion Guides

- [../tools/retrieval-data-tools.md](../tools/retrieval-data-tools.md)
- [../books/ai-engineering-and-llm-systems.md](../books/ai-engineering-and-llm-systems.md)
- [../tools/evals-observability-tools.md](../tools/evals-observability-tools.md)
