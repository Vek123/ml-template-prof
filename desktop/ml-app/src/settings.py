from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ML App"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    project_root: Path = Path(__name__).parent.resolve()

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
