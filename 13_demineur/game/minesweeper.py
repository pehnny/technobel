import rules
from decorators import timer
from typing import Callable

def user_input(rows: int, cols: int) -> tuple[str, int, int]:
    print("Enter 'o row col' to reveal a cell.")
    print("Enter 'f row col' to set a flag where you believe is a mine.")
    
    args = input("> ").split()
    if "secret" in args:
        return ("secret", -1, -1)
    if len(args) != 3:
        print(f"Input must have 3 arguments, got {len(args)}")
        return user_input(rows, cols)
    if args[0] not in ["o", "f"]:
        print(f"First argument must be 'o' or 'f', got {args[0]}")
        return user_input(rows, cols)
    if args[1].isdigit() and args[2].isdigit():
        row, col = int(args[1]), int(args[2])
        if 0 <= row < rows and 0 <= col < cols:
            return (args[0], row, col)
        print("Row or col is out of bounds.")
        return user_input(rows, cols)
    print("Row and col must be numbers.")
    return user_input(rows, cols)

@timer
def minesweeper() -> int:
    print("Minesweeper is starting")

    difficulties: dict[str, Callable[[int, int, int], int]] = {
        "easy": lambda r, c, nb_m: nb_m, 
        "medium": lambda r, c, nb_m: (r * c - nb_m) // 4,
        "hard": lambda r, c, nb_m: (r * c - nb_m) // 3,
    }
    print("Chose a difficulty between", *difficulties)
    difficulty = input("> ")
    while difficulty not in difficulties:
        print("Unknown difficulty. Please chose between", *difficulties)
        difficulty = input("> ")
    

    rows, cols = 10, 10
    nb_mines = (rows * cols) // max(rows, cols)
    nb_mines = difficulties[difficulty](rows, cols, nb_mines)
    playboard = rules.create_grid(rows, cols)
    rules.print_grid(playboard)

    args = user_input(rows, cols)
    while args[0] != "o":
        print("You can't set a flag before the opening your first cell.")
        args = user_input(rows, cols)
    cell = (args[2], args[1])
    mines = rules.generate_mines(rows, cols, nb_mines, cell)
    hidden = rules.create_hidden_grid(rows, cols, mines)
    playboard = rules.reveal(hidden, playboard, args[1], args[2])

    count = 1
    while not rules.has_won(hidden, playboard, mines):
        rules.print_grid(playboard)
        action, row, col = user_input(rows, cols)

        match action:
            case "o":
                if playboard[row][col] != hidden[row][col]:
                    count += 1
                playboard = rules.reveal(hidden, playboard, row, col)
            case "f":
                playboard = rules.set_unset_flag(playboard, row, col)
            case "secret":
                rules.print_grid(hidden)
            case _:
                print("Unkown command tag. Try again.")
                continue
        print()
        
        if rules.has_lost(playboard, row, col):
            print("KABOOM !")
            rules.print_grid(playboard)
            return count
    
    print("Congratulation, you found all the mines !")
    rules.print_grid(playboard)
    return count