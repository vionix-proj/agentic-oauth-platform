up:
\tdocker compose up -d --build

down:
\tdocker compose down -v

logs:
\tdocker compose logs -f --tail=200

seed:
\tdocker compose exec vault sh /vault/config/seed.sh

test:
\t@echo "Run policy test via OPA eval sample:"
\tcurl -s -X POST http://localhost:8181/v1/data/agentic/authz/allow \\
\t  -H "Content-Type: application/json" \\
\t  -d '{"input":{"agent_id":"agent-a","capability":"jira.read.issues"}}'
