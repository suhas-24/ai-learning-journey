# Troubleshooting

Use this page when the guardrails feel either too weak or too strict. Each symptom below is written as a common beginner mistake so you can recognize it in a real project.

If a term feels fuzzy, the safest move is to read the matching chapter again and translate the rule into plain language before changing the code.

## Symptom: the system still follows malicious instructions from retrieved text

Likely causes:

- retrieved content is treated as trusted
- no suspicious-content detector
- tool permissions are too broad

Fix:

- label retrieval as untrusted context
- detect instruction-like text
- reduce permissions on downstream tools

In plain language: do not let copied text act like a boss.

## Symptom: validators reject too many legitimate requests

Likely causes:

- policy is too narrow
- business exceptions were never modeled
- validator logic mixes formatting with business semantics

Fix:

- review rejection logs
- separate schema validation from policy validation
- expand allowlists through explicit review, not ad hoc bypasses

In plain language: the checker is too strict, so normal work keeps getting blocked.

## Symptom: approval exists, but actions still feel unsafe

Likely causes:

- approval happens too late
- approved payload is not fixed
- action lacks idempotency

Fix:

- gate before the external side effect
- store exact approved payload
- attach an idempotency key

In plain language: the human said yes, but the system still has too much freedom.

## Symptom: incident reviews are inconclusive

Likely causes:

- logs are missing actor, action, and reason
- blocked actions are not recorded
- traces and approval records are disconnected

Fix:

- log both allowed and blocked actions
- attach run id to every policy event
- make audit records queryable

In plain language: the system did not leave enough clues for you to understand what happened.

Next phase connection:

- quality and regression loops continue in [Phase 09 Evals](../09-evals/README.md)
