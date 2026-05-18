# Milestone 01 — MVP Enterprise RAG Assistant
- TXT files

Pipeline:

1. Upload document
2. Chunk text
3. Generate embeddings
4. Store embeddings in pgvector

---

## Chat System

Users should be able to:

- ask questions
- retrieve relevant context
- receive grounded answers
- see source citations

---

## Backend

### Required

- FastAPI
- PostgreSQL
- pgvector
- Embedding pipeline
- Retrieval service
- LLM integration

---

## Frontend

### Required

- Chat interface
- Document upload UI
- Citation display
- Loading states

---

## Infrastructure

### Required

- Docker Compose
- Environment variables
- Redis container
- PostgreSQL container

---

# Deliverables

- Functional MVP
- README
- Screenshots
- Architecture diagram
- Docker setup

---

# Success Criteria

The system should:

- answer questions from uploaded documents
- provide relevant citations
- run locally with Docker
- demonstrate end-to-end RAG workflow