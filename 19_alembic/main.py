from database import session
from seed import seed
from sqlalchemy.exc import IntegrityError
import traceback
from controler import create_user, create_game, buy_game, play_game, review_game

def main() -> None:
    with session() as s:
        try:
            seed.init(s)
            s.commit()
            print("Seed loaded successfully")
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Failed to load the seed. It is likely the database connection failed.")
        except IntegrityError:
            print(f"{IntegrityError.__name__}: Failed to load the seed. It is likely already loaded.")
            s.rollback()
        except:
            traceback.print_exc()
            raise Exception("Unknown error")

        # create user
        username = "Tristan"
        email = "tristan@technobel.be"
        user = create_user(s, username, email)
        print(user)

        # create game
        title = "The binding of Isaac"
        publisher_name = "Edmund McMillen"
        game = create_game(s, title, publisher_name)
        print(game)

        # buy game
        title = "Dota 2"
        user_game = buy_game(s, username, title)
        print(user_game)

        # play game
        hours = 200
        user_game = play_game(s, username, title, hours)
        print(username)

        # review game
        comment = "better than lol"
        rating = 4
        review = review_game(s, username, title, comment, rating)
        print(review)
    
if __name__ == "__main__":
    main()