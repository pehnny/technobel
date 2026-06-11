from typing import Optional
from model import Reviews
from repository import UserRepository, GameRepository, UserGameRepository, ReviewRepository
from sqlalchemy.orm import Session

def review_game(session: Session, username: str, gametitle: str, comment: str, rating: int) -> Optional[Reviews]:
    if not 1 <= rating <= 5:
        print("rating must be between 1 and 5 included")
        return None
    
    if not len(comment.strip()):
        print("comment must be not empty")
        return None
    
    user = UserRepository.select_by_username(session, username)
    if user == None:
        print("User does not exist")
        return None
    
    game = GameRepository.select_by_title(session, gametitle)
    if game == None:
        print("game does not exist")
        return None
    
    if not UserGameRepository.exist_by_user_and_game(session, user, game):
        print("User does not own the game")
        return None
    
    if ReviewRepository.exist_by_user_and_game(session, user, game):
        print("User already has a review for this game")
        return None
    
    review = ReviewRepository.create(session, user, game, comment, rating)
    return review