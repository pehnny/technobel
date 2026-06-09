from sqlalchemy import select
from sqlalchemy.orm import Session
from model import Users
from typing import Optional

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, user: Users) -> Users:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> Optional[Users]:
        stmt = select(Users).where(Users.username == username)
        return self.session.execute(stmt).scalar_one_or_none()
    