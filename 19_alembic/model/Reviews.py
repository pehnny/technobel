from model import Base
from sqlalchemy import ForeignKey, CheckConstraint, UniqueConstraint, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Reviews(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        UniqueConstraint("user_id", "game_id"),
    )

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    game_id: Mapped[int] = mapped_column(
        ForeignKey("games.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    rating: Mapped[int] = mapped_column(CheckConstraint("rating >= 1 and rating <= 5"))
    comment: Mapped[str]

    user: Mapped["Users"] = relationship(back_populates="reviews")
    game: Mapped["Games"] = relationship(back_populates="reviews")