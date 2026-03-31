# Risk Register Schema

Use this compact table when threat modeling a workflow.

| Risk ID | Asset | Threat | Entry Point | Likelihood | Impact | Control | Detection | Response |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Internal docs | Prompt injection | Retrieval corpus | medium | high | label untrusted chunks | injection alert | block export and escalate |

## Tips

- keep likelihood and impact on a simple scale at first
- phrase controls as real actions, not vague hopes
- always include a detection column so incidents are observable

Return to [README](../README.md).
