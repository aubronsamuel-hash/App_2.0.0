from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy import text

from .config import settings


engine = create_async_engine(settings.database_url, future=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()
metadata = Base.metadata


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def check_db() -> bool:
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
