from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from core.config.db import settings_db

# engine = create_async_engine(settings_db.database_url, future=True, echo=settings_db.DB_ECHO_LOG)
# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# async def get_db() -> AsyncSession:
#     async with async_session() as session:
#         yield session
#         await session.close()


class AsyncDatabaseSession:
    def __init__(self):
        self._engine = create_async_engine(
            settings_db.database_url, future=True, echo=settings_db.DB_ECHO_LOG
        )
        self._session_factory = async_scoped_session(
            async_sessionmaker(self._engine, class_=AsyncSession, expire_on_commit=False),
            scopefunc=current_task,
        )

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
