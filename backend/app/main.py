from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .config import settings
from .metrics import REQUEST_COUNT, metrics_router
from .routers import (
    admin_users,
    assignments,
    auth,
    files,
    missions,
    planning,
    utils,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.trusted_hosts)


@app.middleware("http")
async def record_metrics(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.inc()
    return response


app.include_router(auth.router)
app.include_router(missions.router)
app.include_router(assignments.router)
app.include_router(admin_users.router)
app.include_router(planning.router)
app.include_router(files.router)
app.include_router(utils.router)
app.include_router(metrics_router)
