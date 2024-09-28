from fastapi import APIRouter
import app.models.user as model_user
from app.db import SessionContextManager

router = APIRouter()


@router.post("/register")
async def register_user():
    user = model_user.User(login='test', avatar_url='test')
    manager = SessionContextManager()
    manager.session.add(user)
    await manager.session.commit()
    print('added model')

    project = model_user.Project()
    user.projects.append(project)
    await manager.session.commit()
    await manager.session.close()
    return {"register": "user"}


@router.post("/login")
async def login():
    return {"login": "user"}

