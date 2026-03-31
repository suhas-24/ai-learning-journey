# Lab 1 - Build a Structured Answerer

This lab helps you stop treating the model like a chat box and start treating it like one step in a program.

## Goal

Build a script that:

- sends a user question plus a clear system instruction
- asks for an answer in a shape code can read
- checks the returned shape before printing it

## Why This Matters

If the model gives you a paragraph, your code has to guess what each part means.

If the model gives you named fields, your code can check them directly.

## Suggested Output Shape

```json
{
  "answer": "short final answer",
  "confidence": "low | medium | high",
  "follow_up_needed": true
}
```

## Recommended Steps

1. Write the shape first.
2. Write the prompt that asks for exactly that shape.
3. Simulate one bad response and handle it.
4. Print only validated output.

## Questions To Ask Yourself

- what happens if the model adds extra prose?
- what happens if `confidence` is missing?
- would another person understand how to use this tomorrow?

## Stretch Goal

Add a retry path that asks the model to fix invalid structure instead of failing immediately.
