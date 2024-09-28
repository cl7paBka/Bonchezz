from fastapi import APIRouter
import app.models.user as model_user
from app.db import *
from sqlalchemy.sql import text
from sqlalchemy.future import select

router = APIRouter()


@router.post("/register")
async def register_user():
    user = model_user.User(login='test1', avatar_url='test')
    async with async_session() as session:
        async with session.begin():
            session.add(user)
            # await session.commit()
            print('added model')
            project = model_user.Project()
            user.projects.append(project)
            await session.commit()

    # async with async_session() as session:
    #     async with session.begin():
    #         temp = await session.execute(select(model_user.User))
    # return temp.scalars().all()

    return user


@router.post("/login")
async def login():
    return {"login": "user"}
