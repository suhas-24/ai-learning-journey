# Eval Plan - Production RAG System

## Eval Questions

- Did retrieval surface the right evidence?
- Did the answer stay grounded in that evidence?
- Did citations point to the correct sources?
- Did quality improve after hybrid retrieval or reranking?

## Eval Dataset

Build a set of 80 to 150 questions spanning:

- fact lookup
- section lookup
- comparison across documents
- multi-hop or synthesis questions
- known difficult edge cases

For each item, store:

- question
- expected source documents
- optional reference answer
- difficulty tag

## Metrics

Track:

- context precision
- context recall
- answer relevance
- faithfulness
- citation accuracy
- abstention quality on weak-context questions

## Manual Review

Manually review at least 20 hard queries every major iteration. Record:

- missing evidence
- irrelevant chunks
- unsupported claims
- citation mistakes

## Success Criteria

- retrieval metrics improve from baseline after hybrid tuning
- citations are correct on at least 90 percent of reviewed samples
- weak-context cases prefer abstention over fabrication

## Demo Eval Guidance

In the demo, show:

- one query where baseline retrieval failed
- the same query after a retrieval improvement
- one score table or chart from the eval report
