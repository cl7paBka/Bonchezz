from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    avatar_url: Mapped[str]  # TODO: Расписать ограничения, паттерн

    projects: Mapped[List['Project']] = relationship(back_populates='contributors', cascade='all, delete-orphan')


class Project(Base):
    __tablename__ = 'Projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('Users.id'))

    contributors: Mapped[List['User']] = relationship(back_populates='projects')
