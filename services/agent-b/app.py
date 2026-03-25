import os
from fastapi import FastAPI
import httpx

app = FastAPI(title="Agent B")
BROKER = os.getenv("TOKEN_BROKER_URL", "http://token-broker:8002")

@app.post("/slack-read")
async def slack_read(body: dict):
    async with httpx.AsyncClient() as c:
        t = await c.post(f"{BROKER}/token/request", json={"agent_id":"agent-b","capability":"slack.read.channels"})
    return {"agent":"B","slack_query":body.get("query"),"token_meta":t.json(),"result":"mocked slack read-only data"}
