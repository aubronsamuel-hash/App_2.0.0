import asyncio
from app.database import SessionLocal
from app.models import User, Mission
from app.auth import hash_password

async def seed():
    async with SessionLocal() as session:
        session.add(User(username='admin', hashed_password=hash_password('admin'), role='admin'))
        session.add(Mission(title='Demo Mission', description='Seed mission', published=False))
        await session.commit()

if __name__ == '__main__':
    asyncio.run(seed())
