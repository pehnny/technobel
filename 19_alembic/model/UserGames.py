from datetime import date
from model import Base
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserGames(Base):
    __tablename__ = "user_games"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
        primary_key=True
    )
    game_id: Mapped[int] = mapped_column(
        ForeignKey("games.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
        primary_key=True
    )
    purchase_date: Mapped[date] = mapped_column(default=date.today)
    hours_played: Mapped[int] = mapped_column(CheckConstraint("hours_played >= 0"), default=0)

    user: Mapped["Users"] = relationship(back_populates="user_games")
    game: Mapped["Games"] = relationship(back_populates="user_games")
