from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from functools import lru_cache

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from animemo.config import Config


@lru_cache
def get_engine() -> AsyncEngine:
    config = Config()
    return create_async_engine(
        config.db.url.get_secret_value(),
        echo=config.db.echo,
        pool_pre_ping=True,
    )


@lru_cache
def get_sessionmaker() -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        get_engine(),
        expire_on_commit=False,
        autoflush=False,
    )


@asynccontextmanager
async def session_scope() -> AsyncGenerator[AsyncSession]:
    """Session with a commit on success and with a rollback on failure."""
    async with get_sessionmaker()() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
