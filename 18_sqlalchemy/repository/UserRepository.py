from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from model import Users
from typing import Optional, Sequence

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, user: Users) -> Users:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def delete(self, user_id: int) -> bool:
        stmt = select(Users).where(Users.id == user_id)
        user = self.session.execute(stmt).scalar_one_or_none()

        if user == None:
            return False
        
        self.session.delete(user)
        self.session.commit()
        return True


    def get_user_by_username(self, username: str) -> Optional[Users]:
        stmt = select(Users).where(Users.username == username)
        return self.session.execute(stmt).scalar_one_or_none()
    
    def update_user_country(self, user_id: int, country: str) -> Optional[Users]:
        stmt = select(Users).where(Users.id == user_id)
        user = self.session.execute(stmt).scalar_one_or_none()

        if user == None:
            return None
        
        user.country = country
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def select_all_with_profile(self) -> Sequence[Users]:
        stmt = select(Users).options(joinedload(Users.profile))
        print()
        print(stmt)
        print()
        return self.session.execute(stmt).scalars().all()