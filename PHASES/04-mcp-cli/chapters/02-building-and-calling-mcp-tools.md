# Chapter 2 - How MCP Tools Work

`MCP` is a way to publish tools with a clear shape so a model can use them without guessing.

The useful idea here is simple: if a tool has a strict input shape and a predictable output shape, it is easier to use, easier to test, and easier to share.

## The Basic Flow

An MCP tool usually works like this:

1. the server says what tools exist
2. the client reads the tool list
3. the model chooses one tool
4. the client sends the arguments
5. the server checks the arguments and runs the action
6. the server returns a result

That is all a protocol is doing here. It is just a shared rulebook.

## What Makes A Good Tool

A good tool should be:

- narrow
- named clearly
- strict about its inputs
- honest about its errors
- limited in what it can change

For example, `create_issue` is better than `do_github_thing` because the caller can understand the job immediately.

## Why A Schema Helps

A `schema` is a description of what inputs are allowed.

This matters because the model should not have to invent the contract from prose alone. The schema can say:

- which fields are required
- how long a string may be
- whether extra keys are allowed
- how many labels are allowed

## Example Tool Contract

```json
{
  "name": "create_issue",
  "description": "Create a GitHub issue in one pre-approved repository.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "title": {
        "type": "string",
        "minLength": 8,
        "maxLength": 120
      },
      "body": {
        "type": "string",
        "minLength": 20,
        "maxLength": 5000
      },
      "labels": {
        "type": "array",
        "items": { "type": "string" },
        "maxItems": 5
      }
    },
    "required": ["title", "body"],
    "additionalProperties": false
  }
}
```

Why this is helpful:

- the caller cannot send random extra fields
- the text must be long enough to be useful
- the tool stays focused on one job
- the repository choice can stay server-side

## What The Server Should Keep For Itself

Not everything should come from the model.

Keep these server-side:

- secrets
- allowlists
- repository names
- retry policy
- logging policy

Let the model provide the intent:

- title
- body
- labels

## Example In Plain Python

```python
def create_issue_tool(arguments: dict) -> dict:
    validated = validate_against_schema(arguments)
    payload = {
        "title": validated["title"],
        "body": validated["body"],
        "labels": validated.get("labels", []),
    }

    response = github_client.create_issue(
        repo="org/project",
        payload=payload,
    )

    return {
        "status": "ok",
        "issue_number": response["number"],
        "url": response["html_url"],
    }
```

## Common Mistakes

### The schema is too open

If `additionalProperties` is `true`, the caller can send junk the server never wanted.

### The description is too vague

Bad: `Works with GitHub.`

Better: `Create one GitHub issue in the incident-tracker repository using a validated title, body, and optional labels.`

### The result is only prose

The caller should get a result it can read programmatically, not a guess.

## Simple Rule

Use MCP when you want one shared, typed tool that multiple clients can discover and call. If you only need one local command or one direct HTTP request, Chapter 3 may be simpler.

Next: [Chapter 3](./03-cli-and-direct-api-workflows.md).
