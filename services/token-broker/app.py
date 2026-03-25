import os, time
from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel

app = FastAPI(title="Token Broker")
OPA_URL = os.getenv("OPA_URL", "http://opa:8181")
REG_URL = os.getenv("AGENT_REGISTRY_URL", "http://agent-registry:8001")

CAP_MAP = {
    "jira.read.issues": {"provider": "jira", "scope": "read:issue"},
    "slack.read.channels": {"provider": "slack", "scope": "channels:history"}
}

class TokenRequest(BaseModel):
    agent_id: str
    capability: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/token/request")
async def token_request(req: TokenRequest):
    if req.capability not in CAP_MAP:
        raise HTTPException(400, "unknown capability")

    async with httpx.AsyncClient() as c:
        r = await c.get(f"{REG_URL}/agents/{req.agent_id}")
        if r.status_code != 200:
            raise HTTPException(404, "agent not found")

        opa = await c.post(
            f"{OPA_URL}/v1/data/agentic/authz/allow",
            json={"input": {"agent_id": req.agent_id, "capability": req.capability}}
        )
        allow = opa.json().get("result", False)
        if not allow:
            raise HTTPException(403, "denied by policy")

    provider = CAP_MAP[req.capability]["provider"]
    token = f"{provider}.{req.agent_id}.{int(time.time())}"
    return {"access_token": token, "token_type": "Bearer", "expires_in": 300, "provider": provider, "capability": req.capability}
