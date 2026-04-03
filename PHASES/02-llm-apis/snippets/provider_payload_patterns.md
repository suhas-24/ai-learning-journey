# Provider Payload Patterns

The exact fields vary by provider, but the learning goal stays the same: send messages, choose settings, and optionally describe tools. A `payload` is just the data you send in one request.

## Generic Message Payload

```json
{
  "messages": [
    {"role": "system", "content": "You are a careful assistant."},
    {"role": "user", "content": "Extract the key risks from the note."}
  ],
  "temperature": 0.2
}
```

## Generic Tool Definition

```json
{
  "name": "read_file",
  "description": "Read a local text file and return its contents.",
  "input_schema": {
    "type": "object",
    "properties": {
      "path": {"type": "string"}
    },
    "required": ["path"]
  }
}
```

## What To Notice

- the tool has a narrow job
- the input shape is explicit
- the model still needs your code to execute the tool
