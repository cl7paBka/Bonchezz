from pydantic import BaseModel
from typing import Optional


class UserOut(BaseModel):
    username: str
    email: str
