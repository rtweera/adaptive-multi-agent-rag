FROM python:3.12-slim

WORKDIR /app

# Ensure python doesn't buffer outputs and uv creates venv in the right place
ENV PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy

RUN pip install uv

COPY pyproject.toml uv.lock ./

# Install dependencies into /app/.venv
RUN uv sync --frozen --no-install-project

# Copy only the allowed source files (app/, main.py)
COPY . .

# Re-sync to register the project workspace/packages
RUN uv sync --frozen

EXPOSE 8000

# Use the absolute path to the container's venv binary to prevent any path issues
CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
