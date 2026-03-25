import os
from fastapi import FastAPI
import httpx

app = FastAPI(title="Agent A")
BROKER = os.getenv("TOKEN_BROKER_URL", "http://token-broker:8002")

@app.post("/jira-read")
async def jira_read(body: dict):
    async with httpx.AsyncClient() as c:
        t = await c.post(f"{BROKER}/token/request", json={"agent_id":"agent-a","capability":"jira.read.issues"})
    return {"agent":"A","jira_query":body.get("query"),"token_meta":t.json(),"result":"mocked jira read-only data"}
