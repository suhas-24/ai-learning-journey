# Chapter 2 - Building and Calling MCP Tools

MCP is most valuable when you treat it as an interface design problem, not just a transport detail. A good MCP tool is narrow, typed, and easy to reason about in failure cases.

## Mental Model

An MCP interaction usually looks like this:

1. the server advertises tools and resources
2. the client inspects available capabilities
3. the model chooses a tool
4. the client sends structured arguments
5. the server validates, executes, and returns structured output

The key benefit is that the model does not have to guess the contract from prose alone.

## Anatomy of a Good Tool

Good MCP tools have:

- a verb-based name such as `create_issue`
- a short description that describes action and constraints
- a JSON schema for arguments
- explicit error behavior
- bounded side effects

See the sample schema in [../snippets/mcp-tool-schema.json](../snippets/mcp-tool-schema.json).

## Example Tool Contract

```json
{
  "name": "create_issue",
  "description": "Create a GitHub issue in a pre-approved repository.",
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
        "minLength": 20
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

Why this is better than a loose prompt:

- titles cannot be empty
- random extra keys are rejected
- labels are bounded
- the repo can remain server-side so the caller cannot target arbitrary repos

## Server Design Guidelines

Ask these questions before implementing the server:

1. Which arguments should the model provide?
2. Which values should stay hidden on the server side?
3. What errors should be returned to the model?
4. What should be logged for audit and debugging?

Good default pattern:

- model provides intent fields like `title` and `body`
- server owns secrets, hostnames, and allowlists
- server returns compact structured status

## Example Pseudocode

```python
def create_issue_tool(arguments: dict) -> dict:
    validated = validate_against_schema(arguments)
    payload = {
        "title": validated["title"],
        "body": validated["body"],
        "labels": validated.get("labels", []),
    }
    response = github_client.create_issue(repo="org/project", payload=payload)
    return {
        "status": "ok",
        "issue_number": response["number"],
        "url": response["html_url"],
    }
```

## Common MCP Failure Modes

### Schema too broad

Bad:

```json
{
  "type": "object",
  "additionalProperties": true
}
```

This invites junk arguments and weak tool use.

### Tool description too vague

Bad description: "Works with GitHub."

Better description: "Create a GitHub issue in the incident-tracker repo using a validated title, body, and optional labels."

### Returning prose instead of structured results

Bad result:

```text
I think the issue was probably created successfully.
```

Better result:

```json
{
  "status": "ok",
  "issue_number": 142,
  "url": "https://github.com/org/project/issues/142"
}
```

## Decision Rule

If the tool needs to be reused across clients and you care about typed discoverability, MCP is a strong default. If not, Chapter 3 may give you a cheaper option.

Continue to [Chapter 3](./03-cli-and-direct-api-workflows.md).
