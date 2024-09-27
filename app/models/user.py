# Временное хранилище пользователей (словарь)
users_db = {}


class User:
    def __init__(self, username: str, email: str, hashed_password: str):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
