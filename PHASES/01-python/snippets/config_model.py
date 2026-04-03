"""Show how validation checks a config shape before the rest of the program uses it."""

from pydantic import BaseModel, Field, ValidationError


class AppConfig(BaseModel):
    # Pydantic checks that the values match the shapes we asked for.
    project_name: str
    retry_limit: int = Field(ge=0, le=5)
    enable_logging: bool = True


def demo() -> None:
    try:
        # Build the config with normal Python values first.
        config = AppConfig(
            project_name="phase-1-demo",
            retry_limit=2,
            enable_logging=True,
        )
        # model_dump turns the validated object back into plain Python data.
        print(config.model_dump())
    except ValidationError as exc:
        # ValidationError means the input did not match the model shape.
        print(exc)


if __name__ == "__main__":
    demo()
