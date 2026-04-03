# Risk Register Schema

Use this compact table when threat modeling a workflow.

This is just a structured way to write down: what could go wrong, how serious it is, what prevents it, and how you would notice it.

If these columns are new:

- `likelihood` means how likely the risk is
- `impact` means how much harm it could cause
- `control` means what stops or reduces the risk
- `detection` means how you will notice the risk
- `response` means what you do after you notice it

| Risk ID | Asset | Threat | Entry Point | Likelihood | Impact | Control | Detection | Response |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Internal docs | Prompt injection | Retrieval corpus | medium | high | label untrusted chunks | injection alert | block export and escalate |

## Tips

- keep likelihood and impact on a simple scale at first
- phrase controls as real actions, not vague hopes
- always include a detection column so incidents are observable

Each row should be understandable even if someone has never seen the system run before.

Return to [README](../README.md).
