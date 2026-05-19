from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "Adaptive Multi-Agent RAG Platform"
    APP_VERSION: str = "0.1.0"

    ENVIRONMENT: str = "dev"

    FE_DEV_URI: str = "http://localhost:5173"
    FE_PROD_URI: str = ""

    # Secrets / Infrastructure (required are left without defaults)
    OPENAI_API_KEY: str
    DATABASE_URL: str
    REDIS_URL: str

    # Environment File Config
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    # Computed Properties
    @computed_field
    @property
    def allowed_origins(self) -> str:
        return (
            self.FE_DEV_URI
            if self.ENVIRONMENT == "dev"
            else self.FE_PROD_URI
        )


settings = Settings() # pyright: ignore[reportCallIssue]