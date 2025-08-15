# Deploy to production via SSH
param(
  [string]$Host,
  [string]$User
)
ssh "$User@$Host" "cd /opt/ccu && git pull && docker compose --profile prod up -d"
