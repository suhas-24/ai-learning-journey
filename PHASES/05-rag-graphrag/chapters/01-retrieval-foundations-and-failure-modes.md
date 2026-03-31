# Chapter 1 - What Retrieval Is and Why It Fails

Retrieval means finding the right evidence before the model answers.

That matters because a language model can only use what it can see. If the wrong evidence is given to it, the answer may still sound confident while being wrong.

## Start With A Simple Picture

Imagine you ask someone a question about a company policy. If they guess from memory, they might be wrong. If they first open the policy document and read the right page, they have a much better chance of answering well.

That is the basic idea behind retrieval. The system looks for the best evidence first, then gives that evidence to the model.

## The Basic Pipeline

A simple retrieval system often does this:

1. collect documents
2. split them into chunks
3. turn each chunk into a searchable form, such as an embedding or keyword index entry
4. look up likely matches for a question
5. rank the matches again if needed
6. give the best evidence to the model
7. ask the model to answer with citations

If the answer looks bad, you need to know which step went wrong.

## Retrieval Failure And Generation Failure

### Retrieval failure

The right evidence never reaches the model.

Examples:

- the chunk split cut a useful sentence in half
- the search method missed an exact error code
- a metadata filter removed the right document

### Generation failure

The evidence was there, but the answer still went wrong.

Examples:

- the model ignored the best chunk
- the answer mixed up two similar passages
- the model compressed the evidence too aggressively

## Why This Is Easy To Miss

A bad retrieval system can still produce a pretty answer.

That is why you should inspect the retrieved chunks before you trust the final response. A polished sentence is not proof that the evidence was correct.

## Worked Example

Question: `Which service owns the nightly billing retry workflow?`

Bad path:

- the document is cut into chunks with no regard for sections
- the ownership table is separated from the workflow description
- search returns a general billing document
- the model guesses the team

Better path:

- chunk by headings or sections
- keep metadata like `service`, `team`, and `doc_type`
- use search that can match both meaning and exact names
- rank the evidence before answering

## Questions To Ask

When an answer looks wrong, ask:

1. Did we ingest the right document?
2. Did we chunk it in a useful way?
3. Did the search method fit the question?
4. Did ranking choose the best evidence?
5. Did answer writing distort the evidence?

## Simple Rule

Look at the retrieved chunks first. Do not start by changing the model or the prompt.

If you cannot explain what the system searched, the rest of the debugging will be guesswork.

Next: [Chapter 2](./02-chunking-indexing-and-metadata-design.md).
