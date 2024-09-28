from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.input.user import UserCreate
from app.schemas.output.user import UserOut
from app.services.user_service import UserService
from app.models.user import users_db
from app.core.security import create_access_token, verify_password, get_current_user

router = APIRouter()

user_service = UserService()

# Асинхронная регистрация нового пользователя
@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    registered_user = await user_service.register_user(user)
    if not registered_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return registered_user

# Логин пользователя
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    valid_password = await verify_password(form_data.password, user.hashed_password)
    if not valid_password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Получение списка пользователей
@router.get("/users")
async def users():
    return users_db

# Эндпоинт для проверки, залогинен ли пользователь
@router.get("/me")
async def get_me(current_user: str = Depends(get_current_user)):
    return {"logged_in": True, "username": current_user}

# Если пользователь не залогинен, FastAPI автоматически вернет 401 ошибку