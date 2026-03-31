# Lab 1 - Build a Habit Tracker CLI

This lab turns the chapter ideas into one complete beginner project.

## Goal

Build a small command-line tool that:

- loads tasks from a JSON file
- counts completed and incomplete tasks
- prints a readable summary
- fails clearly if the file is missing or malformed

## What You Will Practice

- file reading with `Path`
- list and dictionary access
- functions and return values
- simple exception handling

## Suggested Structure

```text
habit-tracker/
  tasks.json
  tracker.py
```

Example `tasks.json`:

```json
[
  {"title": "Read chapter 1", "done": true},
  {"title": "Write notes", "done": false},
  {"title": "Run snippet", "done": true}
]
```

## Step 1 - Write the Loader

Create a function that:

- accepts a file path
- checks that the file exists
- loads JSON
- verifies the top-level value is a list

If you get stuck, inspect the pattern in [inventory_report.py](../snippets/inventory_report.py).

## Step 2 - Write the Summarizer

Write a function that returns:

```python
{
    "total": 3,
    "done": 2,
    "todo": 1,
}
```

Do not print inside this function. Return the data.

## Step 3 - Build the CLI Output

Print something like:

```text
Task Summary
------------
Total: 3
Done: 2
Todo: 1
```

## Failure Cases To Test

- file does not exist
- JSON is invalid
- one task is missing the `done` field

## Stretch Goal

Add a second command-line argument that filters only completed tasks.

## Done Check

You are done when you can intentionally break the input file and still explain exactly why the program failed.
