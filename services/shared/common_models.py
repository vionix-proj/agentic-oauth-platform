from pydantic import BaseModel

class TokenRequest(BaseModel):
    agent_id: str
    capability: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int = 300
    provider: str
    capability: str
