# Deploy to production via SSH
param(
  [string]$Host,
  [string]$User
)
ssh "$User@$Host" "cd /opt/ccu && git pull && docker compose -f compose.prod.yaml up -d"
