from fastapi import FastAPI
from app.api import projects, tasks, users
import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import DATABASE_URL
from app.models.user import Base
import db
from contextlib import asynccontextmanager


# from app.core.config import settings
@asynccontextmanager
async def startup(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


# Создание экземпляра приложения FastAPI
app = FastAPI(title="Project Management API", version="1.0.0", lifespan=startup)

# Подключение маршрутов (роутов)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
# app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

# Точка входа
if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
    # uvicorn.run(app, host=settings.HOST, port=settings.PORT)
