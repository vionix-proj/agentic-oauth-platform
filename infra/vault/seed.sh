#!/usr/bin/env sh
set -e
export VAULT_ADDR=\${VAULT_ADDR:-http://127.0.0.1:8200}
export VAULT_TOKEN=\${VAULT_TOKEN:-root}

vault kv put secret/providers/jira client_id=jira-demo client_secret=jira-secret
vault kv put secret/providers/slack client_id=slack-demo client_secret=slack-secret
echo "Vault seeded."
