from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import DATABASE_URL
# from app.models.user import Base

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

# async def database_main():
#     engine = create_async_engine(DATABASE_URL, echo=True)
#     async_session = async_sessionmaker(engine, expire_on_commit=False)
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)

