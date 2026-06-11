from typing import Optional
from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from model import Reviews, Users, Games

class ReviewRepository:
    @staticmethod
    def exist_by_user_and_game(session: Session, user: Users, game: Games) -> bool:
        return bool(session.scalar(
            select(exists(Reviews).where(Reviews.user_id == user.id and Reviews.game_id == game.id))
        ))
    
    @staticmethod
    def create(session: Session, user: Users, game: Games, comment: str, rating: int) -> Optional[Reviews]:
        review = Reviews(user_id=user.id, game_id=game.id, comment=comment, rating=rating)
        session.add(review)
        session.commit()
        session.refresh(review)
        return review