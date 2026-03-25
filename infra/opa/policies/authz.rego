package agentic.authz

default allow := false

allow if {
  allowed_caps := data.permissions[input.agent_id]
  allowed_caps[_] == input.capability
}
