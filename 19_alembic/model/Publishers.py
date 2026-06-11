from typing import List, Optional
from model import Base
from sqlalchemy import Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Publishers(Base):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    country: Mapped[Optional[str]]

    games: Mapped[List["Games"]] = relationship(back_populates="publisher")