from fastapi import FastAPI, HTTPException

app = FastAPI(title="Agent Registry")

DB = {
    "agent-a": {"id": "agent-a", "name": "Agent A", "owner": "platform", "risk_tier": "low", "capabilities": ["jira.read.issues"]},
    "agent-b": {"id": "agent-b", "name": "Agent B", "owner": "platform", "risk_tier": "low", "capabilities": ["slack.read.channels"]},
    "orchestrator-agent": {"id": "orchestrator-agent", "name": "Customer Service Orchestrator Agent", "owner": "platform", "risk_tier": "medium", "capabilities": ["invoke.agent-a", "invoke.agent-b"]},
}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/agents/{agent_id}")
def get_agent(agent_id: str):
    if agent_id not in DB:
        raise HTTPException(status_code=404, detail="not found")
    return DB[agent_id]
