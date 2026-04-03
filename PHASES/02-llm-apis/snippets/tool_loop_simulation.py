"""Simulate a tiny tool-calling loop so the request, tool result, and final answer stay visible."""

import json
from pathlib import Path


def read_file(path: str) -> str:
    # A path is the location of a file on disk.
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return file_path.read_text(encoding="utf-8")


def simulate_model(messages: list[dict]) -> dict:
    # In this demo, "the model" is just a simple rule so the flow stays easy to inspect.
    last_user_message = messages[-1]["content"]

    if "notes.txt" in last_user_message:
        return {
            "type": "tool_call",
            "tool_name": "read_file",
            "arguments": {"path": "notes.txt"},
        }

    return {
        "type": "final",
        "content": "No tool needed. Answer from current context.",
    }


def main() -> None:
    # A message is one item in the conversation history.
    messages = [
        {"role": "system", "content": "Use tools when file evidence is needed."},
        {"role": "user", "content": "What unfinished tasks are in notes.txt?"},
    ]

    first_response = simulate_model(messages)
    print(json.dumps(first_response, indent=2))

    if first_response["type"] == "tool_call":
        # The model asked for help, so the program decides whether to run the tool.
        tool_result = read_file(first_response["arguments"]["path"])
        # The tool result becomes part of the context for the next step.
        messages.append({"role": "tool", "content": tool_result})
        final_response = {
            "type": "final",
            "content": f"Based on the tool output:\n{tool_result}",
        }
        print(json.dumps(final_response, indent=2))


if __name__ == "__main__":
    main()
