from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Adaptive Multi-Agent RAG API", version="0.1.0")
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Backend running"
    }