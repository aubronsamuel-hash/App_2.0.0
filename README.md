# Coulisses Crew Ultra V2

Monorepo containing frontend and backend for the Coulisses Crew Ultra V2 platform.

## Getting Started (Windows)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop), [Node.js](https://nodejs.org) and [Python 3.11](https://www.python.org/downloads/).
2. Copy `.env.example` files to `.env` in root, `backend` and `frontend` folders and adjust if required.
3. From PowerShell run `scripts/dev_up.ps1` to start the stack.
4. Run `scripts/seed.ps1` to load demo data (admin user and a mission).
5. Access the app:
   - API: <http://localhost:8001>
   - Frontend: <http://localhost:5173>
   - Reverse proxy: <http://localhost:8080>
6. Login using **admin / admin**.

## Testing & Performance

Run all tests and build checks:
```powershell
scripts/test_all.ps1
```
This runs backend `pytest`, builds the frontend and executes a k6 smoke test generating `perf/reports/index.html`.

## Docker Compose Profiles

- `dev` (default): api, frontend, postgres, redis, caddy.
- `minio`: optional S3 compatible storage.
- `monitoring`: Prometheus, Grafana, Loki, Promtail, cAdvisor.
- `prod`: same as dev but intended for production.

## Observability

- Prometheus: <http://localhost:9090>
- Grafana: <http://localhost:3000> (default admin/admin)
- cAdvisor: <http://localhost:8081>

`/metrics` endpoint is exposed by the API and scraped by Prometheus. Logs are collected by Loki/Promtail.

## Deployment

CI/CD is handled via GitHub Actions (`.github/workflows/ci.yml`).
To deploy to production server over SSH:
```powershell
scripts/deploy_prod.ps1 -Host your.server -User deploy
```
Rollback:
```powershell
scripts/rollback.ps1 -Host your.server -User deploy
```

## Migration from JSON

To migrate existing `data.json` to PostgreSQL:
```bash
python migrate_from_json.py
```

## Building Archives

Create distributable archives:
```bash
zip -r backend.zip backend
zip -r frontend.zip frontend
```

## Project Structure

```
.
├── backend       # FastAPI backend
├── frontend      # React frontend
├── infra         # Infrastructure configs
├── perf          # k6 performance scripts
├── scripts       # PowerShell helper scripts
└── docker-compose.yml
```
