# Chapter 1 - Why Specs Exist

Specs exist because hidden behavior scales badly.

If an agent’s rules only live inside code, future collaborators have to reverse-engineer the system to understand what it is supposed to do. That creates fragile behavior, slow reviews, and accidental drift.

## 1. The Core Problem

Without specs, important behavior gets buried in places like:

- hardcoded prompts in Python files
- scattered comments
- chat history that nobody can review later
- editor-specific rule files with no clear scope

That means the behavior is real, but not visible.

## 2. What a Good Spec Does

A good spec tells a reader:

- who the agent is
- what work belongs to it
- what it must not do
- when it should escalate
- what success looks like

This is not marketing copy. It is an operational contract.

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

- clear scope
- explicit exclusions
- real escalation rule

## 4. Failure Cases

### Too vague

If a spec says "use best judgment" everywhere, it is not providing enough guidance.

### Too theatrical

If the spec sounds impressive but does not change behavior, it is decorative instead of useful.

### Too duplicated

If the same rule exists in three files, the team will eventually update one and forget the others.

## 5. What To Practice

- find one hidden behavioral rule in code and rewrite it as a visible instruction
- turn one vague sentence into a concrete scope statement

Next: [Chapter 2: Agent Contracts and Constraints](./02-agent-contracts-and-constraints.md)
