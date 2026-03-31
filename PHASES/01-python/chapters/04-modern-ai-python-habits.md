# Chapter 4 - Modern AI Python Habits

This chapter introduces the habits that show up constantly in modern AI repos: structured config, validation, async calls, logging, and command-line interfaces.

## 1. Type Hints Make Code Easier To Read

Type hints are lightweight explanations attached to function signatures and variables.

```python
def load_usernames(path: str) -> list[str]:
    ...
```

They help humans and tools answer:

- what goes in?
- what comes out?
- what shape should I expect?

## 2. Pydantic Validates Untrusted Data

When config comes from a file, environment variable, or API, validate it.

```python
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    project_name: str
    retry_limit: int = Field(ge=0, le=5)
```

Now invalid config fails loudly instead of leaking bad values deeper into the program.

See [config_model.py](../snippets/config_model.py).

## 3. Async Helps With Waiting, Not With Everything

Use `async` when the program spends time waiting on network calls, file-like I/O, or other external responses.

```python
import asyncio


async def fake_request(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished"
```

If the task is heavy number crunching on the CPU, async does not magically make it faster.

### Good mental model

- synchronous: do task A, wait, then task B
- asynchronous: start task A, let it wait, start task B meanwhile

## 4. Logging Beats Random Print Statements

Printing is fine while learning. Logging is better once the script matters.

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading tasks", extra={"source": "tasks.json"})
```

The goal is to answer:

- what happened?
- when?
- with which input?

## 5. CLIs Make Small Tools Reusable

Typer is a clean way to expose Python functions as commands.

```python
import typer

app = typer.Typer()


@app.command()
def greet(name: str) -> None:
    print(f"Hello, {name}")


if __name__ == "__main__":
    app()
```

This matters because many AI workflows start as scripts and later become commands used by other people.

## 6. What Good Looks Like At The End Of Phase 1

You should be able to explain:

- why a function returns data instead of only printing it
- why validation belongs near the input boundary
- why async is mainly about waiting efficiently
- why tests and linting reduce future pain

Next step: do the labs, then grade yourself with [checkpoints.md](../checkpoints.md).
