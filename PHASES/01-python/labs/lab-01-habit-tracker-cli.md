# Lab 1 - Build a Habit Tracker CLI

This lab turns the chapter ideas into one small program you can run from the terminal. It is meant to feel like a small, safe practice round, not a test of genius.

A **terminal** is a text window where you type commands. A **CLI** is a program you run by typing a command instead of clicking buttons.

We will also use **JSON**, which is a text format for data that looks a little like Python dictionaries and lists.

## Goal

Build a command-line tool that:

- reads tasks from a JSON file
- counts how many are done and how many are not done
- prints a readable summary
- fails clearly if the file is missing or malformed

If any of these words are new, the point is to learn them by using them in one tiny program.

## What You Will Practice

- reading a file with `Path`
- checking list and dictionary data
- writing functions that return values
- handling errors without hiding them

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

Write a function that:

- accepts a file path
- checks that the file exists
- loads JSON text
- confirms the top-level value is a list

If a **file path** feels new, think of it as the address of a file on your computer. The address helps Python find the right file without guessing.

If you need a pattern to copy, look at [inventory_report.py](../snippets/inventory_report.py).

## Step 2 - Write the Summarizer

Write a function that returns:

```python
{
    "total": 3,
    "done": 2,
    "todo": 1,
}
```

Do not print inside this function. Return the data so the CLI can decide how to display it.

Returning data means the function gives its answer back to the rest of the program so another part can use it.

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

- the file does not exist
- the JSON is invalid
- one task is missing the `done` field

These failures are useful because they teach you what the program expects and where it stops when the input is wrong.

## Stretch Goal

Add a second command-line argument that shows only completed tasks.

## Done Check

You are done when you can intentionally break the input file and explain exactly why the program failed.

If you can explain the failure in plain words, you have learned more than just how to make the code run.
