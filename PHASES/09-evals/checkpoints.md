# Checkpoints

Use these checkpoints as a quick self-test. If a line feels fuzzy, go back to the chapter that introduced the word.

## Knowledge checks

- I can explain the difference between evaluation and observability.
- I can explain why a golden dataset should include adversarial cases, which are intentionally tricky cases, and edge cases, which sit near the limits of the task.
- I can name metrics for retrieval, generation, and end-to-end task success.
- I can explain why a single overall score is usually misleading.

## Design checks

- I can draft a small labeled dataset for a real workflow.
- I can write a rubric that defines what good output means.
- I can define a minimum trace schema with run ids and node outcomes.
- I can choose at least two signals that should block a merge.

## Failure checks

- I can turn a real incident into a new eval case.
- I can spot the difference between noisy retrieval and weak generation.
- I can explain how a dead-letter spike, which means a sudden jump in failed runs sent to manual review, should appear in dashboards and traces.

If any item is weak, revisit [Evaluation Design and Golden Datasets](./chapters/01-evaluation-design-and-golden-datasets.md) and [Lab 02](./labs/lab-02-instrument-a-run.md).
