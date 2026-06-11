from typing import List
from datetime import date
from model import Base, AgeRating
from sqlalchemy import Identity, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Games(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    price: Mapped[float] = mapped_column(CheckConstraint("price >= 0"))
    release_date: Mapped[date]
    age_rating: Mapped[AgeRating]
    publisher_id: Mapped[int] = mapped_column(
        ForeignKey("publishers.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )

    publisher: Mapped["Publishers"] = relationship(back_populates="games")
    user_games: Mapped[List["UserGames"]] = relationship(back_populates="game")
    reviews: Mapped[List["Reviews"]] = relationship(back_populates="game")