from typing import Optional
from sqlalchemy. orm import Session
from repository import UserRepository, GameRepository, UserGameRepository
from model import UserGames

def play_game(session: Session, username: str, gametitle: str, hours: int) -> Optional[UserGames]:
    if hours < 0:
        print("hours must be positive")
        return None

    user = UserRepository.select_by_username(session, username)
    if user == None:
        print("user doesn't exist")
        return None
    
    game = GameRepository.select_by_title(session, gametitle)
    if game == None:
        print("game doesn't exist")
        return None
    
    if not UserGameRepository.exist_by_user_and_game(session, user, game):
        print("user doesn't own the game")
        return None
    
    user_game = UserGameRepository.update_hours_played(session, user, game, hours)
    return user_game
    