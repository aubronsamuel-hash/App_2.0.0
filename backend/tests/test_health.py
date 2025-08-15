import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        resp = await ac.get("/healthz")
    assert resp.status_code == 200
    data = resp.json()
    assert data["ok"] is True
    assert "db" in data and "redis" in data and "version" in data
