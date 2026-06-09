from db import Base
from sqlalchemy import String, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=True)

    profile: Mapped["Profiles"] = relationship(
        back_populates="user"
    )

    def __repr__(self) -> str:
        return f"Users(id={self.id!r}, username={self.username!r}, email={self.email!r}), country={self.country!r}"