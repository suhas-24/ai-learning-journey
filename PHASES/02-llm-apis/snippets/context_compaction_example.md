# Context Compaction Example

`Context compaction` means shrinking the conversation history into a shorter summary while keeping the facts that still matter. It helps a long conversation stay focused instead of bloated.

In the examples below, a `turn` means one step in the conversation, such as one user message, one assistant reply, or one tool result.

## Before Compaction

```text
Turn 1: user explains project goal in detail
Turn 2: assistant summarizes initial plan
Turn 3: tool fetches repository structure
Turn 4: user narrows scope to docs only
Turn 5: assistant lists candidate files
Turn 6: tool loads three markdown files
```

## After Compaction

```text
Summary so far:
- Goal: improve documentation structure for the repo
- Current scope: docs only, not code changes
- Relevant evidence loaded: repository tree plus three markdown files
- Pending question: which learner path should be optimized first?
```

## Why This Helps

- preserves the key state
- drops wording that no longer matters
- keeps the next request readable
