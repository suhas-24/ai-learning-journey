# Troubleshooting

## Symptom: the system still follows malicious instructions from retrieved text

Likely causes:

- retrieved content is treated as trusted
- no suspicious-content detector
- tool permissions are too broad

Fix:

- label retrieval as untrusted context
- detect instruction-like text
- reduce permissions on downstream tools

## Symptom: validators reject too many legitimate requests

Likely causes:

- policy is too narrow
- business exceptions were never modeled
- validator logic mixes formatting with business semantics

Fix:

- review rejection logs
- separate schema validation from policy validation
- expand allowlists through explicit review, not ad hoc bypasses

## Symptom: approval exists, but actions still feel unsafe

Likely causes:

- approval happens too late
- approved payload is not fixed
- action lacks idempotency

Fix:

- gate before the external side effect
- store exact approved payload
- attach an idempotency key

## Symptom: incident reviews are inconclusive

Likely causes:

- logs are missing actor, action, and reason
- blocked actions are not recorded
- traces and approval records are disconnected

Fix:

- log both allowed and blocked actions
- attach run id to every policy event
- make audit records queryable

Next phase connection:

- quality and regression loops continue in [Phase 09 Evals](../09-evals/README.md)
