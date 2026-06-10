from datetime import date
from db import Base
from sqlalchemy import String, Identity, Date, inspect
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
    birthdate: Mapped[date] = mapped_column(Date, nullable=True)

    profile: Mapped["Profiles"] = relationship(
        back_populates="user"
    )

    def __repr__(self) -> str:
        state = inspect(self)
        representation = (
            "Users("
            f"id={self.id!r} "
            f"username={self.username!r} "
            f"email={self.email!r} "
            f"country={self.country!r}"
        )

        if "profile" not in state.unloaded:
            representation += " " + self.profile.__repr__()
        
        representation += ")"
        return representation