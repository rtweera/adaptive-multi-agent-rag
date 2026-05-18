# High-Level Architecture

## Components

### Frontend

Responsibilities:

- chat interface
- document upload
- metrics display
- workflow visualization

---

### FastAPI Backend

Responsibilities:

- API routing
- orchestration
- authentication (future)
- session management

---

### Retrieval Layer

Responsibilities:

- embedding generation
- vector search
- hybrid retrieval
- reranking

---

### Agent Layer

Responsibilities:

- query understanding
- retrieval planning
- context optimization
- response synthesis

---

### PostgreSQL + pgvector

Responsibilities:

- vector storage
- metadata storage
- document indexing

---

### Redis

Responsibilities:

- embedding cache
- retrieval cache
- response cache
- session memory

---

### LLM Provider

Responsibilities:

- response generation
- embeddings
- summarization