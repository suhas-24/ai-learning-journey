# RAG And Retrieval Courses

This guide covers the resources that teach how retrieval improves answer quality, where it fails, and how to evaluate the quality of grounded responses.

## Building And Evaluating Advanced RAG

### What it teaches

This course teaches retrieval as a design problem, not a checkbox. It helps you see how chunk size, embedding quality, retrieval strategy, and context assembly change the final answer.

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
