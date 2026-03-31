# Parallel Rewrite Coordination

This folder exists to let five independent Codex windows rewrite `ai-learning-journey` in parallel without losing detail to context compression.

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
