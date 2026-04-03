# Eval Plan - Production RAG System

An `eval plan` is a repeatable way to answer one question: is the system getting better, or just looking better in one demo?

Quick meanings:

- an `eval set` is a saved set of test questions you run again later
- `context precision` asks whether the retrieved text is mostly useful
- `context recall` asks whether the system found the important evidence at all
- `faithfulness` asks whether the answer matches the evidence instead of inventing extra claims
- `abstention` means the system says "I do not have enough evidence" instead of guessing

If `faithfulness` is new, think of it as "does the answer stay true to the documents?"

## What This Plan Checks

- Did retrieval find the right evidence?
- Did the answer stay tied to that evidence?
- Did citations point to the correct source chunks?
- Did the quality improve after you changed retrieval or reranking?

## Build An Eval Set

Create 80 to 150 questions that cover:

- fact lookup
- section lookup
- comparison across documents
- multi-hop questions, which need more than one piece of evidence
- hard edge cases that often fail

For a beginner, the goal is not to build the biggest dataset. The goal is to build a small but honest test set that reveals where the system breaks.

For each question, store:

- the question itself
- the expected source document or documents
- an optional reference answer
- a difficulty label

## Metrics To Track

Measure:

- `context precision`, which checks whether the retrieved context is useful
- `context recall`, which checks whether the right evidence was found
- answer relevance
- faithfulness, which checks whether the answer matches the evidence
- citation accuracy
- abstention quality, which checks whether the system refuses weak questions instead of guessing

Here, `abstention` means the system says "I do not have enough evidence to answer safely" instead of pretending to know.

## Manual Review

Even with metrics, humans still need to read hard cases.

Review at least 20 difficult questions per major iteration and record:

- missing evidence
- irrelevant chunks
- unsupported claims
- citation mistakes

## Success Looks Like

You should be able to show that:

- retrieval metrics improved after tuning
- citations are correct on reviewed samples
- weak-context questions are handled by abstaining, not fabricating

## Demo Guidance

Show:

- one query that baseline retrieval missed
- the same query after an improvement
- one small table or chart from the eval report
