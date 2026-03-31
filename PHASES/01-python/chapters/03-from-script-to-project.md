# Chapter 3 - From Script to Project

Most beginners start with one file. That is normal. The next step is learning when one file stops being enough.

## 1. A Script Is Fine Until It Is Carrying Too Many Jobs

One file becomes painful when it does all of this at once:

- parse user input
- load config
- call helper logic
- format output
- handle errors

That is your signal to split the program.

## 2. A Minimal Project Layout

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

The point is not to create many files for style points. The point is to give each file one main reason to change.

## 3. Imports and Modules

If `storage.py` contains file-reading logic, `main.py` can import it:

```python
from app.storage import load_tasks
```

A module is just a Python file you can import. A package is a directory of modules, usually with `__init__.py`.

### Failure case: circular imports

If `main.py` imports `storage.py` and `storage.py` imports `main.py`, the program becomes tangled.

Fix it by moving shared logic into a third file, such as `models.py` or `utils.py`.

## 4. Tests Turn Guessing Into Verification

```python
from app.storage import summarize_done


def test_summarize_done_counts_completed_tasks():
    tasks = [
        {"title": "a", "done": True},
        {"title": "b", "done": False},
    ]

    assert summarize_done(tasks) == 1
```

The lesson is simple: if a function matters, write a test that proves what it should return.

## 5. Tooling Loop

For a beginner-friendly local workflow:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install pytest ruff pydantic typer
pytest
ruff check .
```

If your machine can repeatedly create the environment, run tests, and lint code, your project is becoming stable.

## 6. Worked Refactor

Start with one file:

```python
def main():
    # reads file
    # counts done tasks
    # prints summary
    ...
```

Refactor toward:

```python
def load_tasks(...): ...
def summarize_tasks(...): ...
def format_report(...): ...
def main(): ...
```

Why this is better:

- each function can be tested alone
- naming reveals intent
- bugs are easier to isolate

## 7. What To Practice Before Moving On

- split one 40-line file into 3 focused functions
- add one test before changing the behavior
- explain why each file exists in a project layout

Next: [Chapter 4: Modern AI Python Habits](./04-modern-ai-python-habits.md)
