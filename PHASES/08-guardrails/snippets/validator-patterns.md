# Validator Patterns

Use the smallest validator that reliably catches the failure mode you care about.

## Schema validator

```python
from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    recipient: EmailStr
    subject: str
    body: str
```

## Policy validator

```python
def enforce_domain_allowlist(recipient: str, allowed_domains: set[str]) -> None:
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
    lowered = text.lower()
    return any(pattern in lowered for pattern in SUSPICIOUS_PATTERNS)
```

Use these patterns together with [Guardrail Layers and Boundary Validation](../chapters/02-guardrail-layers-and-boundary-validation.md).
