# Chapter 3 - Hybrid Retrieval, Reranking, and Evaluation

The first search step should be cheap and broad. The next step should be more careful.

That is the basic idea behind hybrid retrieval and reranking.

## Hybrid Retrieval

`Hybrid retrieval` means using two search styles together:

- dense search, which looks for meaning
- sparse search, which looks for exact words or identifiers

This matters because many questions use both kinds of signal.

Example question:

`Why did invoice-worker time out on ERR-BILL-402 during the March rollout?`

Dense search helps with the natural-language part. Sparse search helps with `invoice-worker` and `ERR-BILL-402`.

## Reranking

`Reranking` means scoring the first search results again with a more careful step.

Why do this?

- the first search can be broad
- reranking can remove weaker matches
- the final context becomes cleaner

## Evaluation

Do not mix search quality and answer quality into one vague score.

Check search quality first:

- did the right chunk appear at all
- was it ranked high enough
- did the search method fit the question

Then check answer quality:

- did the answer stay faithful to the evidence
- did the citation point to the right source
- did the answer actually answer the question

## Debug Loop

If the answer is wrong but sounds reasonable:

1. inspect the top retrieved chunks
2. compare dense-only and hybrid search
3. rerank the same candidate set
4. check whether the good chunk was present but too low

## Simple Pipeline

```python
candidates = retrieve_dense(query, top_k=20)
candidates += retrieve_sparse(query, top_k=20)
deduped = deduplicate(candidates)
best = rerank(query, deduped)[:5]
answer = generate_with_citations(query, best)
```

See [../snippets/hybrid-retriever.py](../snippets/hybrid-retriever.py) for a tiny example.

## Simple Rule

Before you make the prompt more clever, improve retrieval and reranking. Before you assume the embeddings are broken, compare dense search with hybrid search.

Next: [Chapter 4](./04-graphrag-and-memory-systems.md).
