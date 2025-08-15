from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://ccu:ccu@postgres:5432/ccu"
    redis_url: str = "redis://redis:6379/0"
    secret_key: str = "changeme"
    access_token_expire_minutes: int = 60
    cors_origins: str = "http://localhost:5173"
    trusted_hosts: str = "*"
    rate_limit: int = 100

    class Config:
        env_file = ".env"

settings = Settings()
