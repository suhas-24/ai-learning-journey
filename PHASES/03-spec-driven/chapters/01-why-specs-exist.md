# Chapter 1 - Why Specs Exist

Specs exist because hidden behavior becomes hard to trust.

If an agent’s rules only live inside code, the next person has to reverse-engineer the system to understand what it is supposed to do. That creates fragile behavior, slow reviews, and accidental drift.

## 1. The Core Problem

Without specs, important behavior gets buried in places like:

- hardcoded prompt strings inside code
- scattered comments
- chat history that nobody can review later
- editor-specific rule files with no clear scope

That means the behavior exists, but it is not easy to inspect.

## 2. What a Good Spec Does

A good spec tells a reader:

- who the agent is
- what work belongs to it
- what it must not do
- when it should escalate
- what success looks like

This is not marketing copy. It is a working contract.

## 3. Worked Example

Weak behavioral instruction:

```text
Be helpful and smart.
```

Stronger instruction:

```text
You are a documentation review agent. You identify broken links, missing examples, and unclear learner steps. You do not rewrite product code. You ask for approval before deleting files.
```

Why the second version is better:

- it has a clear job
- it says what not to do
- it gives a real escalation rule

## 4. Common Confusion

### Too vague

If a spec says "use best judgment" everywhere, it is not giving enough guidance.

### Too theatrical

If the spec sounds impressive but does not change behavior, it is decoration, not guidance.

### Too duplicated

If the same rule exists in three files, the team will eventually update one and forget the others.

## 5. What To Practice

- find one hidden behavioral rule in code and rewrite it as a visible instruction
- turn one vague sentence into a concrete scope statement

Next: [Chapter 2: Agent Contracts and Constraints](./02-agent-contracts-and-constraints.md)
