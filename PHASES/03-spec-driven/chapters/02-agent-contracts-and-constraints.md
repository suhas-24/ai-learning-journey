# Chapter 2 - Agent Contracts and Constraints

This chapter shows what belongs in a good agent contract and how to write rules that help instead of confuse.

## 1. Core Parts of an Agent Contract

Most useful agent specs include:

- role: what the agent is responsible for
- inputs: what context or files it expects
- tools: what it may use and for what purpose
- constraints: what it must always or never do
- escalation: when it should ask a human instead of guessing
- done condition: how it knows the task is complete

## 2. Writing Good Constraints

Good constraints are concrete.

Weak:

```text
Be careful with files.
```

Better:

```text
Do not edit files outside your ownership. Do not revert work you did not make.
```

The second version changes behavior because a person can check whether it was followed.

## 3. Worked Example Contract

```text
Role: Review markdown learning modules for clarity and missing examples.
Allowed actions: Read owned docs, edit owned docs, add internal links.
Disallowed actions: Do not edit root automation files. Do not touch other modules.
Escalation: If a missing file is owned by another worker, note it for the conductor instead of creating it.
Done: All owned modules include explanations, labs, snippets, checkpoints, and troubleshooting.
```

This is short, but still operational.

## 4. Common Confusion

### Constraint without rationale

Sometimes a rule feels arbitrary because the outcome it protects is not clear. Add enough context to explain why the rule exists, but not so much that the file becomes a novel.

### Constraint conflict

If one section says "act autonomously" and another says "always ask first," the agent has no clean policy. Resolve the tension explicitly.

## 5. What To Practice

- rewrite one vague constraint into a testable instruction
- write one explicit escalation rule
- define a "done" condition that another reviewer could verify

Next: [Chapter 3: Layering Repo Rules, Agent Files, and Skills](./03-layering-rules-and-skills.md)
