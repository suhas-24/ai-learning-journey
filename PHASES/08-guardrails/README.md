# Phase 08 - Guardrails, Threat Models, and Safe Execution

This module teaches how to keep an AI system useful without letting it become reckless.

A `guardrail` is any rule or check that lowers the chance of harm. A `threat model` is a simple way of asking, "How could someone push this system into doing the wrong thing?" We start with those plain ideas, then build toward safer tools, approval rules, and incident handling.

If those words are new, do not worry. This phase starts with the simplest possible version of the problem: an AI system can be helpful, but it can also be tricked, rushed, or given too much power. We learn how to notice those risks early and how to slow the system down in the right places.

First words:

- `guardrail` means a rule or check that reduces harm
- `threat model` means a simple map of how things could go wrong
- `trust boundary` means a place where we stop trusting input automatically
- `least privilege` means giving each part only the permission it truly needs
- `approval` means a human must say yes before a risky action happens
- `sandbox` means a contained place where risky work cannot easily damage the rest of the system

Recommended order:

1. [Threat Models for AI Systems](./chapters/01-threat-models-for-ai-systems.md)
2. [Guardrail Layers and Boundary Validation](./chapters/02-guardrail-layers-and-boundary-validation.md)
3. [Policy, Approvals, and Least Privilege](./chapters/03-policy-approvals-and-least-privilege.md)
4. [Failure and Incident Walkthroughs](./chapters/04-failure-and-incident-walkthroughs.md)
5. [Labs](./labs/lab-01-build-a-threat-model.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

Supporting references:

- [Risk Register Schema](./snippets/risk-register-schema.md)
- [Validator Patterns](./snippets/validator-patterns.md)

## What you will learn

- what a threat model is in plain language
- how prompt injection, data leakage, unsafe tool use, and poisoned retrieval show up in real systems
- where to place validation before model calls, before tool calls, and before external actions
- how approval policy, role permissions, and sandboxing reduce blast radius
- how to turn failures into repeatable safety checks

## Why this matters

Without guardrails, a polite-looking AI can still leak secrets, send the wrong message, or make an expensive mistake very quickly. Safety work is not about being scared of AI. It is about making the system trustworthy enough that real people can use it.

## Completion standard

You are done with this phase when you can write a small threat model, define layered controls for a real workflow, and explain what the system should do under unsafe input, malicious retrieved text, or rejected human approval.
