# Chapter 2 - Data Structures, Files, and Errors

This chapter shows how Python stores information and how real programs move that information in and out of files.

## 1. Four Basic Containers

A **container** is a value that holds other values. Containers help you organize data so you can find it later.

### Lists

A list keeps items in order.

```python
models = ["small", "medium", "large"]
print(models[0])  # "small"
```

Use a list when order matters or duplicates are okay.

### Dictionaries

A dictionary matches names to values.

```python
request = {
    "model": "reasoning-mini",
    "temperature": 0.2,
    "stream": True,
}
```

Use a dictionary when you want to ask for a value by name instead of by position.

### Sets

A set keeps only unique values.

```python
tags = {"python", "llm", "python"}
print(tags)  # {'python', 'llm'}
```

Use a set when duplicates do not matter.

### Tuples

A tuple is like a list that is meant to stay fixed.

```python
coordinate = (12.9, 77.6)
```

Use a tuple when the order matters and the values should not change.

## 2. Reading and Writing JSON

JSON is a plain-text format that many programs use to store structured data. In this repo, it shows up as config, task lists, and API-style data.

```python
import json
from pathlib import Path

config_path = Path("config.json")

config = {
    "project_name": "habit-tracker",
    "retry_limit": 3,
}

config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
loaded = json.loads(config_path.read_text(encoding="utf-8"))
print(loaded["project_name"])
```

### Common confusion

If the file does not exist, Python cannot read it:

```python
Path("missing.json").read_text()
```

Safer version:

```python
path = Path("missing.json")
if not path.exists():
    print("Config file not found")
```

That pattern is important because many bugs are really just missing input.

## 3. Errors Are Useful Feedback

An **exception** is Python saying, "I cannot continue safely with the data I have."

A `ValueError` is a specific kind of exception. It means the value was the wrong shape or content for the job. A `FileNotFoundError` means Python looked for a file and could not find it.

```python
def divide(total: int, count: int) -> float:
    return total / count
```

If `count` is `0`, Python raises an error. That is good. It stops the program from pretending the answer is fine.

### Catch only the errors you expect

```python
try:
    count = int(input("How many items? "))
except ValueError:
    print("Please enter a whole number.")
```

Do not hide every error:

```python
try:
    risky_code()
except Exception:
    pass
```

That makes debugging harder because the real problem disappears.

## 4. Worked Example: Load Tasks from a File

```python
import json
from pathlib import Path


def load_tasks(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Task file not found: {path}")

    raw_text = path.read_text(encoding="utf-8")
    data = json.loads(raw_text)

    if not isinstance(data, list):
        raise ValueError("Task file must contain a list")

    return data
```

This function checks three things:

- does the file exist?
- is the file valid JSON?
- is the top-level shape what we expected?

That is the basic habit behind reliable AI data handling too. Check the shape early, not after the program has already gone wrong.

## 5. `Path` Objects Make File Work Easier

Use `Path` instead of hand-building file strings.

```python
from pathlib import Path

project_dir = Path("reports")
report_file = project_dir / "summary.json"
```

This is easier to read than stitching path strings together yourself.

## 6. What To Practice Before Moving On

- create a JSON file, load it, and print one field
- write a function that rejects invalid data with a clear error
- use a set to remove duplicates from a list

Next: [Chapter 3: From Script to Project](./03-from-script-to-project.md)
