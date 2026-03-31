import os

import httpx


def main() -> None:
    # Read the secret and repo name from the environment so the script stays reusable.
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ.get("GITHUB_REPO", "OWNER/TEST_REPO")
    owner, name = repo.split("/", maxsplit=1)

    # Send one clear request and fail loudly if GitHub rejects it.
    response = httpx.post(
        f"https://api.github.com/repos/{owner}/{name}/issues",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
        json={
            "title": "Lab: compare tool surfaces",
            "body": "Created through the direct API workflow.",
            "labels": ["experiment"],
        },
        timeout=20.0,
    )
    response.raise_for_status()
    data = response.json()
    print(data["html_url"])


if __name__ == "__main__":
    main()
