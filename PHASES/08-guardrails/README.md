# Phase 08 - Guardrails, Threat Models, and Safe Execution

This module teaches how to keep an agent useful without letting it become reckless. The emphasis is architectural safety: model behavior, tool boundaries, approval rules, least privilege, and incident-ready logs.

Recommended order:

1. [Threat Models for AI Systems](./chapters/01-threat-models-for-ai-systems.md)
2. [Guardrail Layers and Boundary Validation](./chapters/02-guardrail-layers-and-boundary-validation.md)
3. [Policy, Approvals, and Least Privilege](./chapters/03-policy-approvals-and-least-privilege.md)
4. [Failure and Incident Walkthroughs](./chapters/04-failure-and-incident-walkthroughs.md)
5. [Labs](./labs/01-build-a-threat-model.md)
6. [Checkpoints](./checkpoints.md)
7. [Troubleshooting](./troubleshooting.md)

Supporting references:

- [Risk Register Schema](./snippets/risk-register-schema.md)
- [Validator Patterns](./snippets/validator-patterns.md)

## What you will learn

- how prompt injection, data leakage, unsafe tool use, and poisoned retrieval show up in real systems
- where to place validation before model calls, before tool calls, and before external actions
- how approval policy, role permissions, and sandboxing reduce blast radius
- how to turn failures into repeatable safety checks

## Completion standard

You are done with this phase when you can write a small threat model, define layered controls for a real workflow, and explain what the system should do under unsafe input, malicious retrieved text, or rejected human approval.
