# Quickstart

## Prereqs
- Docker + Docker Compose

## Run
\`\`\`bash
cp .env.example .env
make up
make seed
\`\`\`

## Verify
### Agent A allowed
\`\`\`bash
curl -s -X POST http://localhost:8004/jira-read -H "Content-Type: application/json" -d '{"query":"open incidents"}'
\`\`\`

### Agent A denied for Slack
\`\`\`bash
curl -s -X POST http://localhost:8002/token/request -H "Content-Type: application/json" \
  -d '{"agent_id":"agent-a","capability":"slack.read.channels"}'
\`\`\`

### Agent B allowed
\`\`\`bash
curl -s -X POST http://localhost:8005/slack-read -H "Content-Type: application/json" -d '{"query":"customer messages"}'
\`\`\`

### Orchestrated answer
\`\`\`bash
curl -s -X POST http://localhost:8003/answer -H "Content-Type: application/json" -d '{"question":"customer status?"}'
\`\`\`
