# Validator Patterns

Use the smallest validator that reliably catches the failure mode you care about.

Think of a validator as a gatekeeper. It checks whether the thing passing through is the right shape, allowed by policy, or suspicious enough to stop.

`Pydantic` is a Python library that checks and shapes data using fields and types.

## Schema validator

```python
from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    # Only accept the fields we expect from a safe email request.
    recipient: EmailStr
    subject: str
    body: str
```

## Policy validator

```python
def enforce_domain_allowlist(recipient: str, allowed_domains: set[str]) -> None:
    # Stop the action if the recipient is outside the approved company or partner list.
    domain = recipient.split("@")[-1]
    if domain not in allowed_domains:
        raise ValueError("recipient domain not allowed")
```

## Content validator

```python
SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "reveal your hidden prompt",
]

def looks_like_injection(text: str) -> bool:
    # Flag text that is trying to sound like a command to the model.
    lowered = text.lower()
    return any(pattern in lowered for pattern in SUSPICIOUS_PATTERNS)
```

Use these patterns together with [Guardrail Layers and Boundary Validation](../chapters/02-guardrail-layers-and-boundary-validation.md).
