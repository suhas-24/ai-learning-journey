# Chapter 3 - Context Engineering

Context engineering is the discipline of deciding what the model should see at each step. This is broader than prompt wording. It includes history, retrieved content, tool output, summaries, instructions, and what you intentionally leave out.

## 1. Why Context Is the Real Lever

If the model answers badly, the problem may not be the model itself. It may be:

- missing context
- irrelevant context
- stale context
- conflicting context

That means the surrounding program is part of model quality.

## 2. A Useful Selection Rule

Before adding anything to context, ask:

1. Does the model need this right now?
2. Is this the smallest useful form of it?
3. Can I summarize or retrieve it later instead?

If the answer to the first question is "not really," leave it out.

## 3. Worked Example: Bad vs Good Context

### Bad context

- full meeting transcript
- entire repository README
- all previous user conversations
- irrelevant pricing table

This creates noise.

### Better context

- user’s current question
- two relevant snippets from the notes
- short summary of earlier decisions
- tool result from the most recent file lookup

This creates signal.

## 4. Summarization and Compaction

Long-running systems need to compress earlier history. A useful pattern is:

- keep the last few turns verbatim
- summarize older turns into one compact note
- preserve critical decisions explicitly

See [context_compaction_example.md](../snippets/context_compaction_example.md).

## 5. Retrieval vs Inline Context

Do not dump a whole knowledge base into every request. Retrieve the pieces relevant to the current step.

Inline context is best when:

- the data is short
- it is central to the task
- it is unlikely to change during the conversation

Retrieval is best when:

- documents are large
- only a few pieces are relevant
- the corpus changes over time

## 6. Failure Cases

### Too much history

The model starts answering vaguely because the working set is cluttered.

### Too little history

The model loses important decisions and repeats earlier mistakes.

### Summary drift

A bad summary can flatten nuance or accidentally change meaning. Summaries need periodic checks against source material.

## 7. What To Practice

- compress five earlier turns into a one-paragraph summary
- decide what to keep verbatim and what to summarize
- compare answers from overloaded context versus focused context

Next: [Chapter 4: Cost, Latency, and Failure Analysis](./04-cost-latency-and-failure-analysis.md)
