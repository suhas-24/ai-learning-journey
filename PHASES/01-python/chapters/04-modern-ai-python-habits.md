# Chapter 4 - Modern AI Python Habits

This chapter introduces the habits that show up all the time in modern Python work for AI systems: type hints, validation, async waiting, logging, and command-line tools.

## 1. Type Hints Help Humans

A **type hint** is a short note in code that tells readers what kind of value to expect.

```python
def load_usernames(path: str) -> list[str]:
    ...
```

This helps answer three beginner questions:

- what goes in?
- what comes out?
- what shape should I expect?

Type hints do not make the code magically safer by themselves. They make the code easier for humans and tools to understand.

## 2. Validation Protects the Program

When data comes from a file, environment variable, or API, do not assume it is correct. Check it.

`Validation` means checking that data has the shape and type you expect before the rest of the program uses it.

```python
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    project_name: str
    retry_limit: int = Field(ge=0, le=5)
```

If the data is wrong, the program should complain early and clearly. That is much better than carrying a bad value into later code.

See [config_model.py](../snippets/config_model.py).

`Pydantic` is a library that helps Python check and organize data by the shape you expect.

## 3. Async Helps With Waiting

Use `async` when a program spends time waiting for outside work to finish.

`asyncio` is the Python library that gives you the basic tools for async waiting.

```python
import asyncio


async def fake_request(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} finished"
```

The important idea is simple:

- synchronous code waits on one thing before moving to the next
- asynchronous code can let one task wait while another keeps going

If the job is heavy number crunching, async is not the main fix.

## 4. Logging Gives You Memory

Print statements are fine at the start. Logging becomes useful when the script matters and you want to know what happened later.

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading tasks from tasks.json")
```

Logging helps you answer:

- what happened?
- when did it happen?
- with which input?

The `INFO` level means "show normal useful messages." Logging is like a diary for the program, so you can understand what it did after the run is over.

## 5. CLIs Make Small Tools Easy To Reuse

A **CLI** is a command-line interface. It lets people run your Python code with commands instead of editing the file every time.

`Typer` is a library that helps turn a Python function into a command-line command.

```python
import typer

app = typer.Typer()


@app.command()
def greet(name: str) -> None:
    print(f"Hello, {name}")


if __name__ == "__main__":
    app()
```

That matters because many useful tools begin as small scripts and later become commands other people can run.

## 6. What Good Looks Like At The End Of Phase 1

You should be able to explain:

- why a function returns data instead of only printing it
- why validation belongs near the input boundary
- why async is mostly about waiting efficiently
- why tests and linting reduce future pain

Next step: do the labs, then grade yourself with [checkpoints.md](../checkpoints.md).
