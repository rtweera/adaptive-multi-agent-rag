import time

from app.core.config import settings
from fastapi import APIRouter
from sqlalchemy import create_engine, text
import redis

router = APIRouter()

engine = create_engine(settings.DATABASE_URL)
redis_client = redis.Redis.from_url(settings.REDIS_URL)


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/ping")
async def ping():
    return {"message": "pong"}


@router.get("/metrics")
def metrics():
    return {
        "api_status": "online",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.post("/demo-chat")
def demo_chat(payload: dict):
    message = payload.get("message", "")

    return {
        "response": f"Demo response for: {message}",
        "sources": ["demo_doc_1.md", "demo_doc_2.md"],
    }


@router.get("/redis-test")
def redis_test():
    try:
        start = time.time()

        redis_client.set("test-key", "hello")
        value = redis_client.get("test-key")

        latency = (time.time() - start) * 1000

        return {
            "redis": "connected",
            "value": value.decode() if isinstance(value, bytes) else value,
            "latency_ms": round(latency, 2),
        }
    except Exception as e:
        return {"redis": "failed", "error": str(e)}


@router.get("/postgres-test")
def postgres_test():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"postgres": "connected", "result": [row[0] for row in result]}
    except Exception as e:
        return {"postgres": "failed", "error": str(e)}
