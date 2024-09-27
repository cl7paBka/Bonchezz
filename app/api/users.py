from fastapi import APIRouter, HTTPException
from app.schemas.input.user import UserCreate
from app.schemas.output.user import UserOut
from app.services.user_service import UserService
from app.models.user import users_db

router = APIRouter()

user_service = UserService()


# Асинхронная регистрация нового пользователя
@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    registered_user = await user_service.register_user(user)
    if not registered_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return registered_user


@router.get("/users")
async def users():
    return users_db
