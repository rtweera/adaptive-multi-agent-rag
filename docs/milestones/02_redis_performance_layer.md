# Milestone 02 — Redis Performance Layer
---

# Objectives

## Embedding Cache

Prevent recomputing embeddings for:

- identical chunks
- previously processed documents

---

## Retrieval Cache

Cache:

query -> retrieved chunks

---

## Response Cache

Cache:

query + context hash -> response

---

# Redis Concepts

Implement:

- TTL expiration
- cache invalidation
- cache hit tracking
- cache miss tracking

---

# Metrics

Track:

- latency improvements
- cache hit rate
- retrieval time
- generation time

---

# UI Additions

Display:

- cache hit/miss status
- response latency
- retrieval latency

---

# Success Criteria

The system should demonstrate measurable speed improvements from caching.