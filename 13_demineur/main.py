from game import minesweeper

def main() -> None:
    turns = minesweeper()
    print(f"Turns played : {turns}")
    return

if __name__ == "__main__":
    main()