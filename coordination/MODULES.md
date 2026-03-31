# Module Map

## Ownership Table

| Module | Owns | Reads | Writes |
| --- | --- | --- | --- |
| M1 | top-level tracker docs | roadmap, AI guide, coordination files | `README.md`, `PROGRESS.md`, `CONTRIBUTING.md`, `WINS/README.md`, `STUCK/README.md`, `coordination/status/M1.md` |
| M2 | resource library | roadmap resource sections, AI guide intro, coordination files | `RESOURCES/books.md`, `RESOURCES/courses.md`, `RESOURCES/tools.md`, `RESOURCES/people-to-follow.md`, `RESOURCES/newsletters.md`, `coordination/status/M2.md` |
| M3 | early curriculum | roadmap phases 1-4, AI guide phases 1-3, coordination files | `PHASES/phase-01-python.md`, `PHASES/phase-02-llm-apis.md`, `PHASES/phase-03-spec-driven.md`, `PHASES/phase-04-mcp-cli.md`, `coordination/status/M3.md` |
| M4 | middle curriculum | roadmap phases 5-8, coordination files | `PHASES/phase-05-rag-graphrag.md`, `PHASES/phase-06-agentic-ides.md`, `PHASES/phase-07-orchestration-harness.md`, `PHASES/phase-08-guardrails-security.md`, `coordination/status/M4.md` |
| M5 | late curriculum plus portfolio execution | roadmap phases 9-11, current project briefs, coordination files | `PHASES/phase-09-evals-observability.md`, `PHASES/phase-10-finetuning.md`, `PHASES/phase-11-portfolio.md`, `PROJECTS/project-01-rag-system.md`, `PROJECTS/project-02-multi-agent-harness.md`, `PROJECTS/project-03-enterprise-agent.md`, `coordination/status/M5.md` |

## Common Bootstrap Commands

Run these first in every module window:

```bash
cd /Users/suhas/Downloads/GenAI/learning/ai-learning-journey
sed -n '1,220p' coordination/README.md
sed -n '1,260p' coordination/STYLE_GUIDE.md
sed -n '1,220p' coordination/SHARED_STATE.md
sed -n '1,220p' coordination/status/MX.md
git status --short
```

Replace `MX` with the real module name before running.

## Module-Specific Read Commands

### M1

```bash
cd /Users/suhas/Downloads/GenAI/learning/ai-learning-journey
sed -n '1,220p' /Users/suhas/Downloads/AI_LEARNING_JOURNEY.md
sed -n '1,220p' README.md
sed -n '1,220p' PROGRESS.md
sed -n '1,220p' CONTRIBUTING.md
sed -n '1,220p' WINS/README.md
sed -n '1,240p' STUCK/README.md
```

### M2

```bash
cd /Users/suhas/Downloads/GenAI/learning/ai-learning-journey
sed -n '892,940p' /Users/suhas/Downloads/ROADMAP.md
sed -n '1,220p' RESOURCES/books.md
sed -n '1,220p' RESOURCES/courses.md
sed -n '1,260p' RESOURCES/tools.md
sed -n '1,220p' RESOURCES/people-to-follow.md
sed -n '1,220p' RESOURCES/newsletters.md
```

### M3

```bash
cd /Users/suhas/Downloads/GenAI/learning/ai-learning-journey
sed -n '106,454p' /Users/suhas/Downloads/ROADMAP.md
sed -n '184,1240p' /Users/suhas/Downloads/AI_LEARNING_JOURNEY.md
sed -n '1,260p' PHASES/phase-01-python.md
sed -n '1,260p' PHASES/phase-02-llm-apis.md
sed -n '1,240p' PHASES/phase-03-spec-driven.md
sed -n '1,260p' PHASES/phase-04-mcp-cli.md
```

### M4

```bash
cd /Users/suhas/Downloads/GenAI/learning/ai-learning-journey
sed -n '370,683p' /Users/suhas/Downloads/ROADMAP.md
sed -n '1,260p' PHASES/phase-05-rag-graphrag.md
sed -n '1,240p' PHASES/phase-06-agentic-ides.md
sed -n '1,260p' PHASES/phase-07-orchestration-harness.md
sed -n '1,240p' PHASES/phase-08-guardrails-security.md
```

### M5

```bash
cd /Users/suhas/Downloads/GenAI/learning/ai-learning-journey
sed -n '684,960p' /Users/suhas/Downloads/ROADMAP.md
sed -n '1,240p' PHASES/phase-09-evals-observability.md
sed -n '1,220p' PHASES/phase-10-finetuning.md
sed -n '1,260p' PHASES/phase-11-portfolio.md
sed -n '1,260p' PROJECTS/project-01-rag-system.md
sed -n '1,240p' PROJECTS/project-02-multi-agent-harness.md
sed -n '1,240p' PROJECTS/project-03-enterprise-agent.md
```

## Paste-Ready Prompts

### M1 Prompt

```text
You are Module M1 in a parallel rewrite of /Users/suhas/Downloads/GenAI/learning/ai-learning-journey.

Your owned files:
- README.md
- PROGRESS.md
- CONTRIBUTING.md
- WINS/README.md
- STUCK/README.md
- coordination/status/M1.md

Read first:
- coordination/README.md
- coordination/STYLE_GUIDE.md
- coordination/SHARED_STATE.md
- /Users/suhas/Downloads/AI_LEARNING_JOURNEY.md
- your owned files

Mission:
- Rewrite the top-level tracker docs so they teach and orient, not just organize.
- Make README.md explain how to use this repository week to week.
- Make PROGRESS.md feel like a real operating rhythm, not a template.
- Make WINS and STUCK useful learning instruments with real examples and rules.
- Do not edit any files outside your ownership.
- Use apply_patch for edits.
- Do not commit or push.
- When done, update coordination/status/M1.md with status, files edited, key decisions, and open questions.
```

### M2 Prompt

```text
You are Module M2 in a parallel rewrite of /Users/suhas/Downloads/GenAI/learning/ai-learning-journey.

Your owned files:
- RESOURCES/books.md
- RESOURCES/courses.md
- RESOURCES/tools.md
- RESOURCES/people-to-follow.md
- RESOURCES/newsletters.md
- coordination/status/M2.md

Read first:
- coordination/README.md
- coordination/STYLE_GUIDE.md
- coordination/SHARED_STATE.md
- /Users/suhas/Downloads/ROADMAP.md sections on books, courses, communities, newsletters
- your owned files

Mission:
- Rewrite the resource library so it explains why each resource matters, what concepts it helps with, and when in the roadmap it should be used.
- Do not leave the resource files as lists of names or "what to do" bullets.
- Include direct explanations of where tools or materials fit into actual AI engineering work.
- Keep ownership boundaries strict.
- Use apply_patch for edits.
- Do not commit or push.
- When done, update coordination/status/M2.md with status, files edited, key decisions, and open questions.
```

### M3 Prompt

```text
You are Module M3 in a parallel rewrite of /Users/suhas/Downloads/GenAI/learning/ai-learning-journey.

Your owned files:
- PHASES/phase-01-python.md
- PHASES/phase-02-llm-apis.md
- PHASES/phase-03-spec-driven.md
- PHASES/phase-04-mcp-cli.md
- coordination/status/M3.md

Read first:
- coordination/README.md
- coordination/STYLE_GUIDE.md
- coordination/SHARED_STATE.md
- /Users/suhas/Downloads/ROADMAP.md for phases 1-4
- /Users/suhas/Downloads/AI_LEARNING_JOURNEY.md for phases 1-3
- your owned files

Mission:
- Rewrite the early curriculum so each phase file teaches the material directly.
- Add explanation of concepts, topics, subtopics, mental models, learning sequence, and common confusion points.
- Replace checklist-style guidance with true explanatory notes.
- Keep the files useful for a beginner who studies them without the original source docs open.
- Do not edit files outside your ownership.
- Use apply_patch for edits.
- Do not commit or push.
- When done, update coordination/status/M3.md with status, files edited, key decisions, and open questions.
```

### M4 Prompt

```text
You are Module M4 in a parallel rewrite of /Users/suhas/Downloads/GenAI/learning/ai-learning-journey.

Your owned files:
- PHASES/phase-05-rag-graphrag.md
- PHASES/phase-06-agentic-ides.md
- PHASES/phase-07-orchestration-harness.md
- PHASES/phase-08-guardrails-security.md
- coordination/status/M4.md

Read first:
- coordination/README.md
- coordination/STYLE_GUIDE.md
- coordination/SHARED_STATE.md
- /Users/suhas/Downloads/ROADMAP.md for phases 5-8
- your owned files

Mission:
- Rewrite the middle curriculum so it explains retrieval, coding agents, orchestration, and safety in direct teaching language.
- Break each phase into concepts, subtopics, sequencing, design tradeoffs, and implementation patterns.
- Make the notes rich enough that the repo itself carries real educational value.
- Do not edit files outside your ownership.
- Use apply_patch for edits.
- Do not commit or push.
- When done, update coordination/status/M4.md with status, files edited, key decisions, and open questions.
```

### M5 Prompt

```text
You are Module M5 in a parallel rewrite of /Users/suhas/Downloads/GenAI/learning/ai-learning-journey.

Your owned files:
- PHASES/phase-09-evals-observability.md
- PHASES/phase-10-finetuning.md
- PHASES/phase-11-portfolio.md
- PROJECTS/project-01-rag-system.md
- PROJECTS/project-02-multi-agent-harness.md
- PROJECTS/project-03-enterprise-agent.md
- coordination/status/M5.md

Read first:
- coordination/README.md
- coordination/STYLE_GUIDE.md
- coordination/SHARED_STATE.md
- /Users/suhas/Downloads/ROADMAP.md for phases 9-11
- your owned files

Mission:
- Rewrite the late curriculum and portfolio project docs so they explain evals, observability, fine-tuning, job readiness, and the three major portfolio systems in direct teaching language.
- Project files must explain architecture, milestones, risks, validation, and what “done” means, not just list technologies.
- Do not edit files outside your ownership.
- Use apply_patch for edits.
- Do not commit or push.
- When done, update coordination/status/M5.md with status, files edited, key decisions, and open questions.
```
