FROM python:3.12-slim
RUN pip install uv
WORKDIR /app
COPY pyproject.toml uv.lock* /app/
RUN uv pip install --system fastapi uvicorn httpx pydantic hvac
COPY app.py /app/app.py
EXPOSE 8002
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
