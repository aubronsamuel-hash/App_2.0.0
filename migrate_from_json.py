"""Migration tool to move data.json content to PostgreSQL"""
import json
import asyncio

from backend.app.database import engine, Base, SessionLocal
from backend.app.models import User, Mission
from backend.app.auth import hash_password

async def migrate(path: str = "data.json") -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    with open(path) as f:
        data = json.load(f)
    async with SessionLocal() as session:
        for u in data.get("users", []):
            user = User(username=u["username"], hashed_password=hash_password(u["password"]), role=u.get("role", "intermittent"))
            session.add(user)
        for m in data.get("missions", []):
            mission = Mission(title=m["title"], description=m.get("description"), published=m.get("published", False))
            session.add(mission)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(migrate())
