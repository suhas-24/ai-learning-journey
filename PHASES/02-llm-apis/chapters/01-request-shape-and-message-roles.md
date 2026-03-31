# Chapter 1 - Request Shape and Message Roles

An LLM call is not "send a paragraph and hope." It is a structured request made of parts. If you understand the parts, the behavior stops feeling mysterious.

## 1. Start With the Plain Meaning

An **LLM** is a large language model. It is a program trained on lots of text so it can predict and generate text.

Think of a model call like this:

```text
response = model(messages, tools, settings, extra_context)
```

Your code decides what goes into that call. That means your code has a lot of influence over the result.

## 2. Message Roles

Most APIs use some version of these roles:

- `system`: broad rules, tone, and boundaries
- `user`: the question or task
- `assistant`: earlier model replies
- `tool`: output from outside code after a tool runs

Example conversation shape:

```json
[
  {"role": "system", "content": "You are a careful research assistant."},
  {"role": "user", "content": "Summarize the project risks."},
  {"role": "assistant", "content": "I should inspect the latest notes first."},
  {"role": "tool", "content": "{\"risks\": [\"missing tests\", \"unclear scope\"]}"}
]
```

This is just a structured way of saying "here is the conversation so far."

## 3. Settings

Common settings include:

- `temperature`: how much randomness to allow
- output limit: how long the answer may become
- streaming: whether the answer arrives in pieces
- tool definitions: what actions the model may ask for

### Temperature in plain language

- low temperature: more repeatable
- medium temperature: some variety
- high temperature: more creative, but less predictable

Use low temperature for extraction, classification, and structured tasks. Use higher temperature only when creativity is the point.

## 4. Better Request Shape

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

Why the second request works better:

- it gives the model a job
- it narrows the task
- it uses low randomness for a ranking task

## 5. Common Confusion

### Conflicting instructions

If one instruction says "be concise" and another says "write a long essay," the model sees a conflict. Your job is to remove or resolve the conflict before sending the request.

### Missing history

The model does not truly remember unless your code sends the earlier facts again.

### Too much context

If you paste ten documents when only one matters, the answer can become noisy. More text does not automatically mean better help.

## 6. What To Practice

- write one short request for a factual task and one for a creative task
- explain which settings you would change and why
- inspect a message list and explain what each role contributes

Next: [Chapter 2: Structured Output and Tool Calling](./02-structured-output-and-tool-calling.md)
