from typing import Optional
from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from model import Games, Publishers

class GameRepository:
    @staticmethod
    def exist_by_title(session: Session, title: str) -> bool:
        return bool(session.scalar(
            select(exists(Games.id).where(Games.title == title))
        ))

    @staticmethod
    def create(session: Session, title: str, publisher: Publishers) -> Optional[Games]:
        if len(title.strip()) == 0:
            print("title must be not empty.")
            return None
        
        game = Games(title=title, publisher_id=publisher.id)
        session.add(game)
        session.commit()
        session.refresh(game)
        return game
    
    @staticmethod
    def select_by_title(session: Session, title: str) -> Optional[Games]:
        stmt = select(Games).where(Games.title == title)
        return session.execute(stmt).scalar()
