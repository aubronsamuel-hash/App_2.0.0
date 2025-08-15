from fastapi import APIRouter
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

REQUEST_COUNT = Counter("app_requests_total", "Total requests")

metrics_router = APIRouter()


@metrics_router.get("/metrics")
async def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
