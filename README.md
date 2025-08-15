# Monorepo Scaffold

Backend, frontend and deployment scripts for the application.

## Quickstart (Windows PowerShell)

1. Copy `.env.example` to `.env` and adjust values.
2. Start the development stack:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\dev_up.ps1
   ```
3. Seed the database:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\seed.ps1
   ```
4. Open the services:
   - API: <http://localhost:8001/health>
   - Frontend: <http://localhost:5173>
   - Reverse proxy: <http://localhost:8080>

Stop the stack with:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\dev_down.ps1
```

## Environment

The `.env.example` file defines the following variables:

- `API_PORT` (default `8001`)
- `FRONT_PORT` (default `5173`)
- `CADDY_HTTP_PORT` (default `8080`)
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`
- `REDIS_URL`
- `S3_ENDPOINT`, `S3_BUCKET`, `S3_ACCESS_KEY`, `S3_SECRET_KEY`
- `ALLOWED_ORIGINS`
- `TRUSTED_HOSTS`
- `TOKEN_TTL_MIN`
- `RATE_LIMITS_WRITE`, `RATE_LIMITS_LOGIN`
- `LOG_LEVEL`

## Ports

| Service    | Port |
|------------|------|
| API        | 8001 |
| Frontend   | 5173 |
| Caddy      | 8080 |
| Postgres   | 5432 |
| Redis      | 6379 |
| Grafana    | 3000 |
| Prometheus | 9090 |
| cAdvisor   | 8081 |
| Loki       | 3100 |

## Health Checks

- API: <http://localhost:8001/health>
- Frontend: <http://localhost:5173>
- Caddy: <http://localhost:8080>
- Grafana: <http://localhost:3000/health>
- Prometheus: <http://localhost:9090/-/healthy>
- cAdvisor: <http://localhost:8081/healthz>
- Loki: <http://localhost:3100/ready>

## Testing

Run all tests and build checks:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\test_all.ps1
```

## Deployment

To deploy to a production server over SSH:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy_prod.ps1 -Host your.server -User deploy
```
Rollback:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\rollback.ps1 -Host your.server -User deploy
```
