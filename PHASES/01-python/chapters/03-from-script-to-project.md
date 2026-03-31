# Chapter 3 - From Script to Project

A **script** is one file that gets a job done. A **project** is a small group of files that share a purpose. This chapter shows you when to split one script into a project.

## 1. When One File Stops Being Enough

One file becomes hard to maintain when it tries to do too many different jobs:

- read input
- validate input
- do the main work
- format output
- handle errors

When that happens, the file is not "bad." It is just doing too much for one place.

## 2. A Minimal Project Layout

A `dependency` is a package your project uses. A `pyproject.toml` file is a small project file that records project settings and dependencies.

`TOML` is a simple text format for settings. You can think of it as a neat way to store project rules in a file people can read.

```text
habit_tracker/
  app/
    __init__.py
    main.py
    storage.py
    models.py
  tests/
    test_storage.py
  pyproject.toml
  README.md
```

The goal is not to create lots of folders. The goal is to give each file one main reason to change.

`__init__.py` is a file that helps Python treat a folder like a package. You do not need to master it yet; just know it is part of how importable folders are marked.

## 3. Modules and Imports

A **module** is a Python file you can import. A **package** is a folder of modules.

```python
from app.storage import load_tasks
```

That line means "reuse the code from another file instead of copying it here."

### Common confusion

If `main.py` imports `storage.py` and `storage.py` imports `main.py`, the files depend on each other in a circle. That makes the program confusing.

Fix the problem by moving shared logic into a third file, such as `models.py` or `utils.py`.

## 4. Tests Turn Guessing Into Checking

```python
from app.storage import summarize_done


def test_summarize_done_counts_completed_tasks():
    tasks = [
        {"title": "a", "done": True},
        {"title": "b", "done": False},
    ]

    assert summarize_done(tasks) == 1
```

The point of the test is simple: if the code matters, write down what it should do and check it.

## 5. A Beginner-Friendly Tool Loop

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install pytest ruff pydantic typer
pytest
ruff check .
```

This sequence matters because it teaches a repeatable habit:

- make a clean environment
- install only what the project needs
- run tests
- run lint checks

### Why each step exists

- A `virtual environment` is a private Python area for one project.
- `venv` makes a private Python environment for one project
- `pip` installs packages
- `pytest` runs tests
- `ruff` checks for style issues and some mistakes

## 6. Refactor Example

Start with one crowded file:

```python
def main():
    # reads file
    # counts done tasks
    # prints summary
    ...
```

Refactor toward small focused functions:

```python
def load_tasks(...): ...
def summarize_tasks(...): ...
def format_report(...): ...
def main(): ...
```

Why this is better:

- each function has one job
- each function is easier to test
- bugs are easier to find

## 7. What To Practice Before Moving On

- split one 40-line file into three focused functions
- add one test before changing behavior
- explain why each file exists in a project layout

Next: [Chapter 4: Modern AI Python Habits](./04-modern-ai-python-habits.md)
