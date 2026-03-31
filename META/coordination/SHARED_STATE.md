# Shared State Contract

## Read-Only Inputs For Every Module

- `/Users/suhas/Downloads/ROADMAP.md`
- `/Users/suhas/Downloads/AI_LEARNING_JOURNEY.md`
- `coordination/STYLE_GUIDE.md`
- `coordination/MODULES.md`
- your assigned files in this repository

## Write Rules

Each module may write only:

- its owned content files
- its own status file in `coordination/status/`

Do not edit:

- another module's content files
- another module's status file
- shared coordination files unless you are the conductor

## Status File Protocol

At minimum, record:

- `Status:` not started / in progress / blocked / done
- `Files edited:`
- `Key decisions:`
- `Open questions for conductor:`

## Conflict Avoidance

- No commits from module windows.
- No pushes from module windows.
- No formatting passes over files you do not own.
- If a cross-module dependency is discovered, log it in your status file and stop at the boundary.
