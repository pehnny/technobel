from datetime import date
from model import Base
from sqlalchemy import Identity, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Profiles(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )
    bio: Mapped[str]
    country: Mapped[str]
    birthdate: Mapped[date]
    avatar_url: Mapped[str]

    user: Mapped["Users"] = relationship(back_populates="profile")