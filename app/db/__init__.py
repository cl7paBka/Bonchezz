from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import DATABASE_URL
from app.models.user import *  # Причина зависания https://stackoverflow.com/questions/75732232/async-sqlalchemy-cannot-create-tables-in-the-database


engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionMaker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class SessionContextManager:
    def __init__(self) -> None:
        self.session_factory = AsyncSessionMaker
        self.session = self.session_factory()

    async def __aenter__(self) -> None:
        self.session = self.session_factory()

    async def __aexit__(self, *args: object) -> None:
        await self.rollback()

    async def commit(self) -> None:
        await self.session.commit()
        await self.session.close()
        self.session = None

    async def rollback(self) -> None:
        await self.session.rollback()
        await self.session.close()
        self.session = None


async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
