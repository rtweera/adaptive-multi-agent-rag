from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings
from app.core.logging import log_requests

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.allowed_origins,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.middleware("http")(log_requests)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running. Check `/health` for system status."
    }