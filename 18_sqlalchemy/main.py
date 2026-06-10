from db import engine, Base, session
from model import *
from repository import UserRepository

def main():
    Base.metadata.create_all(engine)
    with session() as s:
        user_repository = UserRepository(s)
        # new_user = Users(username="laraxs", email="another@fictive.email", country="belgium")
        # user = user_repository.create(new_user)
        # print(user)
        user = user_repository.get_user_by_username("pehnny")
        print(user)
        # user = user_repository.update_user_country(1, "france")
        # print(user)
        # success = user_repository.delete(4)
        # print(success)
        users = user_repository.select_all_with_profile()
        print(users)
    return

if __name__ == "__main__":
    main()