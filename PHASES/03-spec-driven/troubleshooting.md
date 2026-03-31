# Phase 3 Troubleshooting

## "My spec sounds nice, but it does not guide behavior"

That usually means the language is too vague. Replace adjectives like "helpful" or "careful" with explicit scope, constraints, and done conditions.

## "I do not know where a rule should live"

Ask what the rule is about:

- repo-wide convention
- one agent’s identity and boundaries
- one reusable workflow

The answer usually tells you the right file layer.

## "My rules keep repeating across multiple files"

Pick one source of truth. Keep the broad rule at the highest appropriate layer, then reference it instead of rephrasing it everywhere.

## "The code and the spec disagree"

Treat that as a real bug. Either the implementation drifted or the spec became stale. Do not ignore the mismatch.

## "I am writing giant spec files"

That often means unrelated concerns are being mixed together. Split rules by responsibility instead of by document length alone.
