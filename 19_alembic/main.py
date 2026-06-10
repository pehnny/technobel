from database import session
from seed import seed

def main() -> None:
    try:
        with session() as s:
            seed.init(s)
    except:
        print("seed already loaded")
    

if __name__ == "__main__":
    main()