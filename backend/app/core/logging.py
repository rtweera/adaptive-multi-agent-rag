import logging
import time

from fastapi import Request

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("app")


async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"Status={response.status_code} "
        f"Duration={process_time:.2f}ms "
        f"Client={request.client.host if request.client else 'unknown'}"
    )

    return response
