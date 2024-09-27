from app.models.user import User, users_db
from app.core.security import hash_password


class UserService:

    async def register_user(self, user_data):
        # Проверяем, есть ли уже пользователь с таким email
        if user_data.email in [user.email for user in users_db.values()]:
            return None

        hashed_password = await hash_password(user_data.password)
        new_user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
        users_db[user_data.username] = new_user
        return new_user
