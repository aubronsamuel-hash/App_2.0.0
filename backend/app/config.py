from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = Field(
        default="sqlite+aiosqlite:///./test.db", alias="DATABASE_URL"
    )
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    token_ttl_min: int = Field(default=60, alias="TOKEN_TTL_MIN")
    cors_origins: List[str] = Field(default_factory=lambda: ["*"], alias="CORS_ORIGINS")
    trusted_hosts: List[str] = Field(
        default_factory=lambda: ["*"], alias="TRUSTED_HOSTS"
    )
    rate_limit_per_min: int = Field(default=60, alias="RATE_LIMIT_PER_MIN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
