# Adaptive Multi-Agent RAG Platform

## Tech Stack

### Backend Stack

- Python
- FastAPI
- LangGraph
- PostgreSQL + pgvector
- Redis
- SQLAlchemy
- UV package manager

### Frontend Stack

- React
- TailwindCSS
- TypeScript

### AI Stack

- OpenAI-compatible APIs
- Embedding models
- RAG pipelines
- Agent orchestration

---

## Project Goals

This project focuses on:

- AI systems engineering
- Production-oriented RAG architectures
- Adaptive retrieval workflows
- Agent orchestration patterns
- Observability and evaluation
- Intelligent caching strategies
- Enterprise knowledge retrieval

---

## Planned Architecture

### Agents

- Query Understanding Agent
- Retrieval Agent
- Context Optimization Agent
- Verification Agent
- Response Synthesis Agent

### Infrastructure

- Redis caching layer
- Vector database
- Async ingestion pipeline
- Metrics collection
- Evaluation dashboard

---

## Local Development

### Backend

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker compose up --build
```

---

## Current Status

See:

- docs/milestones/
- TODO.md

---

## Long-Term Vision

Build a realistic enterprise AI engineering platform demonstrating:

- adaptive retrieval systems
- production RAG pipelines
- intelligent orchestration
- scalable AI infrastructure
- efficient context management

## License

MIT License

---
