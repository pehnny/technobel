from db import Base
from sqlalchemy import String, ForeignKey, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Profiles(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    bio: Mapped[str] = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user: Mapped["Users"] = relationship(
        back_populates="profile"
    )