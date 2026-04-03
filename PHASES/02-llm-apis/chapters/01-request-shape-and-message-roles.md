# Chapter 1 - Request Shape and Message Roles

This chapter starts at the beginning: what actually happens when your code asks a language model for help. The answer is less mysterious than it first looks, because the request is just structured text.

## 1. The Basic Idea

An LLM is a program that reads text and produces text.

That sounds simple, but there is an important detail: your code does not just send a blob of text and hope for the best. It sends a shaped request. That request is made of parts, and each part has a job.

If you understand the parts, the model stops feeling mysterious.

## 2. A Model Call in Plain Language

Think of a model call like this:

```text
response = model(request)
```

Your request usually contains:

- messages
- settings
- optional tool descriptions
- extra context you want the model to use

Your program decides all of that. The model only sees what you include.

## 3. What a Message Is

A `message` is one item in the conversation.

You can think of messages like notes passed between people in a group chat:

- one note explains the rules
- one note asks the question
- one note gives a previous answer
- one note brings back information from a tool

Most model APIs use message roles so the request stays organized.

If that feels abstract, imagine a notebook with labels on each page: rules, question, answer, and tool result.

## 4. Message Roles

Common roles are:

- `system`: broad rules, tone, and boundaries
- `user`: the task or question from the person using the system
- `assistant`: a reply from the model
- `tool`: output from outside code after a tool runs

Example:

```json
[
  {"role": "system", "content": "You are a careful research assistant."},
  {"role": "user", "content": "Summarize the project risks."},
  {"role": "assistant", "content": "I should inspect the latest notes first."},
  {"role": "tool", "content": "{\"risks\": [\"missing tests\", \"unclear scope\"]}"}
]
```

This is not magic. It is just a clean way to say, "Here is the conversation so far, and here is information the model should use next."

## 5. Settings

Settings are small choices your code makes before the request goes out.

Common settings include:

- `temperature`: how much randomness to allow
- output limit: how long the answer may become
- streaming: whether the answer arrives in pieces
- tool definitions: what outside actions the model may ask for

### Temperature in plain language

`Temperature` controls how much variety the model is allowed to show.

- low temperature: more repeatable
- medium temperature: some variety
- high temperature: more creative, but less predictable

For extraction, classification, and other strict tasks, lower temperature usually makes life easier.

## 6. Why Request Shape Matters

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

The second request works better because:

- it gives the model a job
- it narrows the task
- it lowers randomness for a task that needs consistent structure

## 7. Common Confusion

### Conflicting instructions

If one instruction says "be concise" and another says "write a long essay," the model may receive mixed signals. Your job is to remove that conflict before sending the request.

### Missing history

The model does not truly remember past conversations unless your code includes the important parts again.

### Too much context

If you add too much unrelated text, the answer can become noisy. More text is not automatically better.

## 8. What To Practice

- write one short request for a factual task and one for a creative task
- explain which settings you would change and why
- inspect a message list and explain what each role contributes

Next: [Chapter 2: Structured Output and Tool Calling](./02-structured-output-and-tool-calling.md)
