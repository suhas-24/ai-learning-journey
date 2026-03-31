# Parallel Rewrite Coordination Archive

This folder is an archive of the parallel rewrite process that rebuilt `ai-learning-journey` into the current module-based curriculum.

It is not part of the learner-facing study path. The active curriculum lives in `FOUNDATIONS/`, `PHASES/`, `PROJECTS/`, and `RESOURCES/`.

Some historical prompts and status notes inside this archive still mention the old flat-file layout and local machine paths. Treat them as implementation history, not current navigation.

## Read This First

1. `STYLE_GUIDE.md`
2. `SHARED_STATE.md`
3. `MODULES.md`
4. `status/Mx.md` for your assigned module

## Goal

Rewrite the repository so it teaches directly inside the notes. Do not leave the content as a plan that only says what to read or what to try. Each owned file should explain concepts, chapters, topics, subtopics, mental models, build sequence, and common failure modes in enough detail that the repo can be studied on its own.

## Non-Negotiables

- Stay inside your file ownership.
- Use `apply_patch` for file edits.
- Update only your own status file under `coordination/status/`.
- Do not commit or push from module windows.
- If you discover a cross-cutting issue, record it in your status file instead of editing another module's files.
