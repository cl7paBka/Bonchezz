from app.models.user import users_db, User
from app.core.security import hash_password
from app.schemas.input.user import UserCreate
from typing import Optional

class UserService:
    # Асинхронная регистрация нового пользователя
    async def register_user(self, user: UserCreate) -> Optional[User]:
        # Проверяем, существует ли пользователь
        if user.username in users_db:
            return None
        # Хешируем пароль
        hashed_password = await hash_password(user.password)
        # Создаём пользователя и добавляем его в "базу данных" (словарь)
        new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        users_db[user.username] = new_user
        return new_user
