from typing import Optional
from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from model import Publishers

class PublisherRepository:
    @staticmethod
    def exist_by_name(session: Session, publisher: str) -> bool:
        return bool(session.scalar(
            select(exists(Publishers.id).where(Publishers.name == publisher))
        ))
    
    @staticmethod
    def select_by_name(session: Session, name: str) -> Optional[Publishers]:
        stmt = select(Publishers).where(Publishers.name == name)
        return session.execute(stmt).scalar()