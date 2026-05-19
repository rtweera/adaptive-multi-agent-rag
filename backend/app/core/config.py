import os

from dotenv import load_dotenv

load_dotenv()

# App config — not secrets, committed to source control
APP_VERSION = "0.1.0"
ENVIRONMENT = "dev"  # "dev" or "prod"
FE_DEV_URI = "http://localhost:5173"
FE_PROD_URI = ""
ALLOWED_ORIGINS = FE_DEV_URI if ENVIRONMENT == "dev" else FE_PROD_URI


def _require(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


# Secrets — must be set in .env, never committed
OPENAI_API_KEY = _require("OPENAI_API_KEY")
DATABASE_URL = _require("POSTGRES_URL")
REDIS_URL = _require("REDIS_URL")
