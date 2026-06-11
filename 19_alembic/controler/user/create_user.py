from typing import Optional
from model import Users
from sqlalchemy.orm import Session
from repository import UserRepository

def create_user(session: Session, username: str, email: str) -> Optional[Users]:
        if UserRepository.exist_by_email(session, email):
            print("Email already used")
            return None
        user = UserRepository.create(session, username, email)
        return user