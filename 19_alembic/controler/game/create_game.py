from typing import Optional
from model import Games
from repository import PublisherRepository, GameRepository
from sqlalchemy.orm import Session

def create_game(session: Session, title: str, publisher_name: str) -> Optional[Games]:
    publisher = PublisherRepository.select_by_name(session, publisher_name)
    if publisher == None:
        print("publisher does not exist")
        return None
    game = GameRepository.create(session, title, publisher)
    return game