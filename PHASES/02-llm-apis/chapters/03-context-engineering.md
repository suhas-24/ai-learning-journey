# Chapter 3 - Context Engineering

`Context` means everything the model can see at the moment it answers: instructions, chat history, tool results, retrieved notes, and summaries.

`Context engineering` is the skill of choosing that material carefully. It is a practical way of asking, "What should the model see right now so it can do the next step well?"

## 1. Why Context Matters

If the model answers badly, the problem may not be the model. It may be:

- missing context
- irrelevant context
- stale context
- conflicting context

That means the surrounding program is part of the answer quality.

## 2. A Simple Selection Rule

Before adding anything to context, ask:

1. Does the model need this right now?
2. Is this the smallest useful version of it?
3. Can I summarize it or fetch it later instead?

If the answer to the first question is "not really," leave it out.

## 3. Worked Example

### Bad context

- full meeting transcript
- entire repository README
- all previous user conversations
- irrelevant pricing table

This creates noise.

### Better context

- the user’s current question
- two relevant snippets from the notes
- a short summary of earlier decisions
- the most recent tool result

This creates signal, which means useful information that helps the model answer well.

## 4. Summaries and Compaction

Long-running systems need to shrink earlier history so the request does not grow forever.

A simple pattern is:

- keep the last few turns exactly
- summarize older turns into one compact note
- keep important decisions explicit

See [context_compaction_example.md](../snippets/context_compaction_example.md).

## 5. Retrieval Versus Inline Context

Do not dump a whole knowledge base into every request. Bring in only the pieces that matter now.

`Retrieval` means finding a useful piece of information at question time and adding it to the request instead of pasting the whole library into the prompt. In plain language, it is like looking up the right page instead of photocopying the whole book.

Inline context is best when:

- the data is short
- it is central to the task
- it is unlikely to change during the conversation

Retrieval is best when:

- the documents are large
- only a few pieces matter
- the source material changes over time

## 6. Common Confusion

### Too much history

The model starts answering vaguely because the request is crowded.

### Too little history

The model forgets important decisions and repeats old mistakes.

### Summary drift

A bad summary can change meaning by accident. Summaries should be checked against the original source from time to time.

## 7. What To Practice

- compress five earlier turns into one short summary
- decide what to keep exactly and what to summarize
- compare answers from overloaded context versus focused context

Next: [Chapter 4: Cost, Latency, and Failure Analysis](./04-cost-latency-and-failure-analysis.md)
