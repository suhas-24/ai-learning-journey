import json
from pathlib import Path


def read_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return file_path.read_text(encoding="utf-8")


def simulate_model(messages: list[dict]) -> dict:
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
    messages = [
        {"role": "system", "content": "Use tools when file evidence is needed."},
        {"role": "user", "content": "What unfinished tasks are in notes.txt?"},
    ]

    first_response = simulate_model(messages)
    print(json.dumps(first_response, indent=2))

    if first_response["type"] == "tool_call":
        # The model asked for help, so the program decides whether to run the tool.
        tool_result = read_file(first_response["arguments"]["path"])
        messages.append({"role": "tool", "content": tool_result})
        final_response = {
            "type": "final",
            "content": f"Based on the tool output:\n{tool_result}",
        }
        print(json.dumps(final_response, indent=2))


if __name__ == "__main__":
    main()
