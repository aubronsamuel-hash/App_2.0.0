# Rollback production deployment via SSH
param(
  [string]$Host,
  [string]$User
)
ssh "$User@$Host" "cd /opt/ccu && git reset --hard HEAD~1 && docker compose -f compose.prod.yaml up -d"
