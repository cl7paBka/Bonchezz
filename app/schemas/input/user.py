from pydantic import BaseModel, EmailStr
from typing import Optional

# Входная схема для регистрации пользователя
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

