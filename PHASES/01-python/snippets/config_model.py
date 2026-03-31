from pydantic import BaseModel, Field, ValidationError


class AppConfig(BaseModel):
    project_name: str
    retry_limit: int = Field(ge=0, le=5)
    enable_logging: bool = True


def demo() -> None:
    try:
        config = AppConfig(
            project_name="phase-1-demo",
            retry_limit=2,
            enable_logging=True,
        )
        print(config.model_dump())
    except ValidationError as exc:
        print(exc)


if __name__ == "__main__":
    demo()
