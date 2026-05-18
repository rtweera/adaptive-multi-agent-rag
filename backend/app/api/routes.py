from fastapi import APIRouter
from app.core.config import APP_VERSION, ENVIRONMENT

router = APIRouter()

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
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }


@router.post("/demo-chat")
def demo_chat(payload: dict):
    message = payload.get("message", "")

    return {
        "response": f"Demo response for: {message}",
        "sources": [
            "demo_doc_1.md",
            "demo_doc_2.md"
        ]
    }