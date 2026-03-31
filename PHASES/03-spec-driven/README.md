# Phase 3 - Spec-Driven Development

This phase teaches how to make agent behavior visible, reviewable, and versioned.

Before we go further, here are the plain meanings of the main words:

- a `spec` is a written description of how something should behave
- a `contract` is a clear promise about what something will and will not do
- a `constraint` is a rule that limits behavior so it stays safe and predictable
- a `skill` is a reusable how-to file for one repeated task
- `versioned` means the document can be updated over time and those changes can be tracked

In this phase, a spec usually means the rules for a worker, an agent, or a reusable workflow.

A spec is not just a prompt string. A prompt can be a temporary instruction, while a spec is meant to be read, reviewed, updated, and trusted over time.

The goal is not to write longer prompts. The goal is to move important behavior out of hidden places and into clear documents that people can inspect.

## What You Will Learn

- why specs matter in AI systems
- what belongs in an agent contract
- how to separate repo rules, agent roles, and reusable skills
- how to write constraints that are concrete instead of vague
- how to review a spec the same way you review code
- how to change behavior by editing the contract first

## How To Use This Phase

1. Read the chapters in order.
2. Study the example spec files in `snippets/`.
3. Do the labs by rewriting one small workflow in a spec-first way.
4. Use [checkpoints.md](./checkpoints.md) to make sure you can explain the boundaries and responsibilities of each file.
5. Use [troubleshooting.md](./troubleshooting.md) if your specs feel fluffy, duplicated, or hard to follow.

## Study Path

1. [Chapter 1: Why Specs Exist](./chapters/01-why-specs-exist.md)
2. [Chapter 2: Agent Contracts and Constraints](./chapters/02-agent-contracts-and-constraints.md)
3. [Chapter 3: Layering Repo Rules, Agent Files, and Skills](./chapters/03-layering-rules-and-skills.md)
4. [Chapter 4: Review and Change Management](./chapters/04-review-and-change-management.md)

## Practice

- [Lab 1: Convert a Script to Spec-First](./labs/lab-01-convert-script-to-spec-first.md)
- [Lab 2: Review a Bad Spec and Repair It](./labs/lab-02-review-a-bad-spec.md)

## Snippets

- [AGENTS.example.md](./snippets/AGENTS.example.md)
- [CLAUDE.example.md](./snippets/CLAUDE.example.md)
- [SKILL.example.md](./snippets/SKILL.example.md)

## Success Standard

You should be able to point to one behavior change and say, "that changed because I edited the contract here," instead of "that changed because I hid a new prompt string inside code."
