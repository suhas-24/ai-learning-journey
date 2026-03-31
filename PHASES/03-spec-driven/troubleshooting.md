# Phase 3 Troubleshooting

## "My spec sounds nice, but it does not guide behavior"

That usually means the language is too vague. Replace adjectives like "helpful" or "careful" with explicit scope, constraints, and done conditions. `Scope` means what the system is supposed to cover. A `done condition` means how you know the task is finished.

## "I do not know where a rule should live"

Ask what the rule is about:

- repo-wide convention
- one agent’s identity and boundaries
- one reusable workflow

The answer usually tells you the right file layer.

## "My rules keep repeating across multiple files"

Pick one `source of truth`, which means the main place where the rule officially lives. Keep the broad rule at the highest appropriate layer, then reference it instead of rephrasing it everywhere.

## "The code and the spec disagree"

Treat that as a real bug. Either the `implementation`, which is the actual code, drifted or the spec became stale. Do not ignore the mismatch.

## "I am writing giant spec files"

That often means unrelated concerns are being mixed together. Split rules by responsibility instead of by document length alone.
