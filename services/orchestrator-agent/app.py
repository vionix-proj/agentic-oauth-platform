import os
from fastapi import FastAPI
import httpx

app = FastAPI(title="Customer Service Orchestrator Agent")
A_URL = os.getenv("AGENT_A_URL", "http://agent-a:8004")
B_URL = os.getenv("AGENT_B_URL", "http://agent-b:8005")

@app.post("/answer")
async def answer(body: dict):
    q = body.get("question", "")
    async with httpx.AsyncClient() as c:
        a = await c.post(f"{A_URL}/jira-read", json={"query": q})
        b = await c.post(f"{B_URL}/slack-read", json={"query": q})
    return {
        "question": q,
        "oauth_requirements": {
            "agent-a": "jira.read.issues",
            "agent-b": "slack.read.channels"
        },
        "aggregated": {
            "agent_a": a.json(),
            "agent_b": b.json()
        }
    }
