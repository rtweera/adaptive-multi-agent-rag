import os
from dotenv import load_dotenv

load_dotenv()

# App config — not secrets, committed to source control
APP_VERSION = "0.1.0"
ENVIRONMENT = "dev" # "dev" or "prod"
DEV_URI = "http://localhost:5173"
PROD_URI = ""
ALLOWED_ORIGINS = DEV_URI if ENVIRONMENT == "dev" else PROD_URI

# Secrets — must be set in .env, never committed
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
