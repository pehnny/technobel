from datetime import date, datetime
from model import Base
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserGames(Base):
    __tablename__ = "user_games"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        primary_key=True
    )
    game_id: Mapped[int] = mapped_column(
        ForeignKey("games.id"),
        nullable=False,
        primary_key=True
    )
    purchase_date: Mapped[date] = mapped_column(default=datetime.now())
    hours_played: Mapped[int] = mapped_column(CheckConstraint("hours_played >= 0"))

    user: Mapped["Users"] = relationship(back_populates="user_games")
    game: Mapped["Games"] = relationship(back_populates="user_games")
