# Chapter 1 - Request Shape and Message Roles

The first thing to learn is that a model call is not "send prompt, get magic." It is a structured request with explicit pieces.

## 1. A Useful Mental Model

Think of an LLM call as a function:

```text
response = model(messages, tools, settings, extra_context)
```

Your code decides what goes into that function call. That means your code controls far more behavior than the model itself.

## 2. Common Message Roles

Most modern APIs use some variation of these roles:

- `system`: broad rules, tone, boundaries, operating instructions
- `user`: the task or question
- `assistant`: earlier model outputs in the conversation
- `tool`: results produced by external code after a tool call

Example conversation shape:

```json
[
  {"role": "system", "content": "You are a careful research assistant."},
  {"role": "user", "content": "Summarize the project risks."},
  {"role": "assistant", "content": "I should inspect the latest notes first."},
  {"role": "tool", "content": "{\"risks\": [\"missing tests\", \"unclear scope\"]}"}
]
```

Even if a provider uses slightly different field names, the same idea remains: you are sending structured context, not one mysterious paragraph.

## 3. Generation Settings

Typical settings include:

- temperature: how much randomness to allow
- max output size: how long the answer may become
- streaming: whether results arrive incrementally
- tool definitions: what actions the model is allowed to request

### Practical explanation of temperature

- low temperature: safer and more repeatable
- medium temperature: more variety
- high temperature: more exploration, more drift

Use low temperature for extraction, classification, or structured tasks. Use higher temperature only when creativity truly matters.

## 4. Worked Example: Same Task, Better Request

Weak request:

```text
Help with this project.
```

Better request:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a concise software project assistant. Call a tool if repo evidence is required."
    },
    {
      "role": "user",
      "content": "List the top three project risks from the provided notes."
    }
  ],
  "temperature": 0.2
}
```

Why the second request is better:

- clearer role
- concrete task
- lower randomness for a ranking problem

## 5. Failure Cases

### Failure case: conflicting instructions

If your system message says "be concise" but the user message says "write a 2,000-word essay," your prompt stack contains tension. The model may try to satisfy both and do neither cleanly.

### Failure case: missing history

If your program forgets to resend earlier facts, the model does not truly remember them. Conversation state only exists if your code includes it again.

### Failure case: overstuffed context

If you paste ten documents when only one matters, the answer may become noisy or generic. More tokens do not automatically mean better context.

## 6. What To Practice

- write one short request for a factual task and one for a creative task
- explain which settings you would change and why
- inspect a message list and explain what each role contributes

Next: [Chapter 2: Structured Output and Tool Calling](./02-structured-output-and-tool-calling.md)
