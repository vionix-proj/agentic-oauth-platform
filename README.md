# Agentic OAuth Platform (OSS Reference)

Centralized non-human identity + token governance for MCP-enabled agents.

## Components
- Keycloak (OAuth/OIDC authority)
- Vault (secrets)
- OPA (authorization policy)
- Agent Registry (capability declarations)
- Token Broker (policy + scope normalization + token issuance mock)
- Agent A (Jira read-only)
- Agent B (Slack read-only)
- Customer Service Orchestrator Agent
- MCP registry metadata

## Quick start
See:
- `docs/quickstart.md`
- `docs/architecture.md`
