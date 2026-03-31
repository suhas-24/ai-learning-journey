# Chapter 2 - Project Storytelling

Storytelling for engineers is not marketing fluff.
It is structured explanation.

This chapter starts with the basic words:

- a `story` is a sequence that helps someone understand what happened
- a `tradeoff` is a choice where you gain one thing and give up another
- a `limit` is something the system still cannot do well

## The Four-Part Project Story

Use this order when explaining a project:

1. Problem: what user or business issue exists?
2. System: what did you build to address it?
3. Evidence: how do you know it works?
4. Tradeoffs: what is still limited or risky?

This structure works in READMEs, interviews, demos, and networking conversations.

## Turning Raw Work Into Clear README Text

Weak line:

```text
Built an advanced AI workflow.
```

Stronger line:

```text
Built a document-grounded question answering system over internal policy manuals, using retrieval, reranking, and citation-aware answer generation. Evaluated it on a 120-question regression set.
```

The stronger line explains scope, mechanism, and evidence.

## What To Include In A Failure Story

A useful failure story includes:

- what broke
- how you diagnosed it
- what changed
- what improved afterward

Example:

```text
Early retrieval looked good in demos but failed on policy comparison questions. Manual review showed chunking had split exceptions away from the main rule text. I changed the chunking strategy, added reranking, and context recall improved on the hard set.
```

That kind of story builds trust because it shows judgment, not just success.

## Anti-Patterns

Avoid lines like:

- "used cutting-edge AI"
- "built an autonomous system"
- "improved productivity"

If you cannot explain exactly how, those lines weaken credibility.

## Chapter Exercise

Take one project and write:

- a 2-line version for LinkedIn
- a 4-line version for a README intro
- a 90-second spoken version for interviews
