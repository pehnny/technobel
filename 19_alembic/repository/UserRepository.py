from typing import Optional
from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from model import Users

class UserRepository:
    @staticmethod
    def exist_by_email(session: Session, email: str) -> bool:
        return bool(session.scalar(
            select(exists(Users.id).where(Users.email == email))
        ))

    @staticmethod
    def create(session: Session, username: str, email: str) -> Optional[Users]:
        if not isinstance(username, str) or not isinstance(email, str):
            print("username and email must be str.")
            return None
        if len(username.strip()) == 0:
            print("username must be not empty.")
            return None
        
        user = Users(username=username, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def select_by_username(session: Session, username: str) -> Optional[Users]:
        stmt = select(Users).where(Users.username == username)
        return session.execute(stmt).scalar()