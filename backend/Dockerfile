FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./

RUN pip install uv

COPY . .

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]