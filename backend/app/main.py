from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from redis.asyncio import from_url
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from prometheus_fastapi_instrumentator import Instrumentator

from .config import settings
from .database import Base, engine
from .routers import auth, missions, users, health

app = FastAPI(title="Coulisses Crew Ultra V2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(',') if o],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.trusted_hosts and settings.trusted_hosts != "*":
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=[h.strip() for h in settings.trusted_hosts.split(',') if h])

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        redis = from_url(settings.redis_url, encoding="utf8", decode_responses=True)
        await FastAPILimiter.init(redis)
    except Exception:
        pass
    Instrumentator().instrument(app).expose(app)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(missions.router, prefix="/missions", tags=["missions"], dependencies=[Depends(RateLimiter(times=settings.rate_limit, seconds=60))])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(health.router)


@app.get("/")
async def root():
    return {"message": "Coulisses Crew Ultra V2 API"}
