# Chapter 2 - Project Storytelling

Storytelling for engineers is not marketing fluff. It is structured explanation.

## The Four-Part Project Story

Use this order when explaining a project:

1. Problem: what user or business issue exists?
2. System: what did you build to address it?
3. Evidence: how do you know it works?
4. Tradeoffs: what is still limited or risky?

This structure works in READMEs, interviews, demos, and networking conversations.

## Turning Raw Work Into Strong README Sections

Weak README line:

```text
Built a RAG chatbot with advanced retrieval and vector search.
```

Stronger README line:

```text
Built a document-grounded question answering system over internal policy manuals, combining hybrid retrieval, reranking, and citation-aware answer generation. Evaluated on a 120-question regression set with faithfulness and answer relevance tracking.
```

The second version explains scope, mechanism, and evidence.

## What To Include In A Failure Story

A useful failure story includes:

- what broke
- how you diagnosed it
- what changed
- what metric or behavior improved

Example:

```text
Early retrieval quality looked good in demos but failed on policy comparison questions. Manual review showed chunking had split exceptions away from the main rule text. I changed the chunking strategy to preserve section boundaries, added reranking, and context recall improved on the hard set.
```

That is the kind of explanation interviewers remember.

## Anti-Patterns

Avoid:

- "used cutting-edge AI"
- "built an autonomous system"
- "improved productivity"

Unless you can explain exactly how, these lines weaken credibility.

## Chapter Exercise

Take one project and write:

- a 2-line version for LinkedIn
- a 4-line version for a README intro
- a 90-second spoken version for interviews
