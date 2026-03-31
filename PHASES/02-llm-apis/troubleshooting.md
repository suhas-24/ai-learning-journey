# Phase 2 Troubleshooting

## "The model keeps ignoring my instructions"

Check for conflicting instructions or weak task wording. A vague user request can overpower a careful system message simply because the task itself is underspecified.

## "The JSON looks right until I try to parse it"

Inspect the raw text. Models often wrap JSON in explanation or markdown fences. Validate the response instead of assuming the visible shape is clean.

## "The tool call keeps coming back with bad arguments"

Your tool description may be too vague, or the argument shape may be underspecified. Make the tool narrower and add one concrete example.

## "Adding more context made the answer worse"

That usually means you added noise, not signal. Reduce the prompt to the smallest relevant evidence set and compare the result again.

## "I do not know whether the failure is the model or my code"

Break the loop apart:

1. inspect the exact request payload
2. inspect the raw model response
3. inspect the validated structure
4. inspect the tool execution result

Once you separate those layers, the bug usually becomes less mysterious.
