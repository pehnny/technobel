from typing import Optional
from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from model import UserGames, Users, Games

class UserGameRepository:
    @staticmethod
    def exist_by_user_and_game(session: Session, user: Users, game: Games) -> bool:
        return bool(session.scalar(
            select(exists(UserGames).where(UserGames.user_id == user.id and UserGames.game_id == game.id))
        ))
    
    @staticmethod
    def create(session: Session, user: Users, game: Games) -> Optional[UserGames]:
        user_game = UserGames(user_id=user.id, game_id=game.id)
        session.add(user_game)
        session.commit()
        session.refresh(user_game)
        return user_game
    
    @staticmethod
    def update_hours_played(session: Session, user: Users, game: Games, hours: int) -> Optional[UserGames]:
        stmt = select(UserGames).where(UserGames.user_id == user.id and UserGames.game_id == game.id)
        user_game = session.execute(stmt).scalar()
        
        if user_game == None:
            print("User doesn't own the game")
            return None
        
        user_game.hours_played += hours
        session.add(user_game)
        session.commit()
        session.refresh(user_game)
        return user_game