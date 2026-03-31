# Chapter 3 - Hybrid Retrieval, Reranking, and Evaluation

The first retrieval stage should be cheap and broad enough to find candidates. The second stage should be smarter and more selective. That is where hybrid retrieval and reranking become operationally valuable.

## Hybrid Retrieval

Hybrid retrieval combines:

- dense retrieval for semantic similarity
- sparse retrieval for exact terms and identifiers

This matters because many real questions contain both.

Example query:

`Why did invoice-worker timeout on ERR-BILL-402 during the March rollout?`

Dense retrieval helps with the natural-language intent. Sparse retrieval helps with `invoice-worker` and `ERR-BILL-402`.

## Reranking

Initial retrieval may return 20 or 50 candidates. A reranker re-scores those candidates with a more precise but more expensive model.

Benefits:

- improves final evidence quality
- reduces junk context before generation
- makes citation sets tighter

## Evaluation Layers

Do not collapse retrieval and answer quality into one subjective score.

Measure retrieval separately:

- recall at k
- precision at k
- mean reciprocal rank
- hit rate

Then measure answer quality:

- faithfulness
- groundedness
- relevance
- citation correctness

## Worked Debug Loop

Problem: the answer is plausible but cites the wrong runbook.

Investigation:

1. inspect top-10 retrieved chunks
2. compare dense-only vs hybrid results
3. rerank the same candidate set
4. check whether the good chunk was present but ranked too low

Possible diagnosis:

- retrieval was fine, ranking was poor
- retrieval missed exact incident identifiers, so hybrid search is needed

## Practical Pipeline

```python
candidates = retrieve_dense(query, top_k=20)
candidates += retrieve_sparse(query, top_k=20)
deduped = deduplicate(candidates)
best = rerank(query, deduped)[:5]
answer = generate_with_citations(query, best)
```

See [../snippets/hybrid-retriever.py](../snippets/hybrid-retriever.py) for a toy implementation.

## Decision Rule

Add reranking before adding more prompt complexity. Add hybrid retrieval before assuming embeddings are broken. Evaluate both before reaching for GraphRAG.

Continue to [Chapter 4](./04-graphrag-and-memory-systems.md).
