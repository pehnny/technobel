from typing import List
from model import Base, Gender
from sqlalchemy import Identity, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    gender: Mapped[Gender] = mapped_column(nullable=False)

    profile: Mapped["Profiles"] = relationship(back_populates="user")
    user_games: Mapped[List["UserGames"]] = relationship(back_populates="user")
    reviews: Mapped[List["Reviews"]] = relationship(back_populates="user")