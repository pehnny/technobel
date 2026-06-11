from typing import Optional
from model import UserGames
from repository import UserRepository, GameRepository, UserGameRepository
from sqlalchemy.orm import Session

def buy_game(session: Session, username: str, gametitle: str) -> Optional[UserGames]:
    user = UserRepository.select_by_username(session, username)
    if user == None:
        print("User does not exist")
        return None
    
    game = GameRepository.select_by_title(session, gametitle)
    if game == None:
        print("game does not exist")
        return None
    
    if UserGameRepository.exist_by_user_and_game(session, user, game):
        print("User already own the game")
        return None

    user_game = UserGameRepository.create(session, user, game)
    return user_game