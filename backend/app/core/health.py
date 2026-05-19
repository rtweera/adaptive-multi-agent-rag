import time
from datetime import datetime, UTC

import redis
from sqlalchemy import create_engine, text

from app.core.config import settings


START_TIME = time.time()

engine = create_engine(settings.DATABASE_URL)

redis_client = redis.Redis.from_url(settings.REDIS_URL)


def get_uptime_seconds() -> float:
    return round(time.time() - START_TIME, 2)


def check_postgres():
    try:
        start = time.time()

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        latency = (time.time() - start) * 1000

        return {
            "status": "connected",
            "latency_ms": round(latency, 2)
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }


def check_redis():
    try:
        start = time.time()

        redis_client.ping()

        latency = (time.time() - start) * 1000

        return {
            "status": "connected",
            "latency_ms": round(latency, 2)
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }


def get_system_health():
    postgres_status = check_postgres()
    redis_status = check_redis()

    overall_status = "healthy"

    if (
        postgres_status["status"] != "connected"
        or redis_status["status"] != "connected"
    ):
        overall_status = "degraded"

    return {
        "status": overall_status,
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "uptime_seconds": get_uptime_seconds(),
        "services": {
            "postgres": postgres_status,
            "redis": redis_status
        }
    }