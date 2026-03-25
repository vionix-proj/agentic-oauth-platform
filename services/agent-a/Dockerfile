FROM python:3.12-slim
RUN pip install uv
WORKDIR /app
COPY pyproject.toml uv.lock* /app/
RUN uv pip install --system fastapi uvicorn httpx pydantic
COPY app.py /app/app.py
EXPOSE 8004
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8004"]
