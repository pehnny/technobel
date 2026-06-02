import random
from .lexic import LEXIC

Grid = list[list[str]]
Coord = tuple[int, int]

def create_grid(rows: int, cols: int, value: str = LEXIC["hidden"]) -> Grid:
    return [[value for _ in range(cols)] for _ in range(rows)]

def get_neighbours(rows: int, cols: int, row: int, col: int) -> list[Coord]:
    directions = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]

    neighbours: list[Coord] = []
    for dx, dy in directions:
        if 0 <= col+dx < cols and 0 <= row+dy < rows:
            neighbour = (col+dx, row+dy)
            neighbours.append(neighbour)
    return neighbours

def generate_mines(rows: int, cols: int, nb_mines: int, forbidden_cell: Coord) -> list[Coord]:
    mines: list[Coord] = []
    col, row = forbidden_cell
    forbidden_cells = [forbidden_cell]
    forbidden_cells.extend(get_neighbours(rows, cols, row, col))
    
    while nb_mines > 0:
        x = random.randrange(cols)
        y = random.randrange(rows)
        mine = (x, y)
        if not (mine in forbidden_cells or mine in mines):
            mines.append((x, y))
            nb_mines -= 1
    return mines

def create_hidden_grid(rows: int, cols: int, mines: list[Coord]) -> Grid:
    hidden_grid = [[LEXIC["mine"] for _ in range(cols)] for _ in range(rows)]

    for y in range(rows):
        for x in range(cols):
            if (x, y) not in mines:
                neighbours = get_neighbours(rows, cols, y, x)
                close_mines = len([neighbour for neighbour in neighbours if neighbour in mines])
                hidden_grid[y][x] = str(close_mines)
    return hidden_grid

def reveal(hidden: Grid, visible: Grid, row: int, col: int) -> Grid:
    value = hidden[row][col]
    if value == visible[row][col] :
        return visible
    
    visible[row][col] = value
    rows, cols = len(visible), len(visible[0])
    if value == LEXIC["safe"]:
        neighbours = get_neighbours(rows, cols, row, col)
        for x, y in neighbours:
            visible = reveal(hidden, visible, y, x)
    return visible

def set_unset_flag(visible: Grid, row: int, col: int) -> Grid:
    value = visible[row][col]
    if value == LEXIC["hidden"]:
        visible[row][col] = LEXIC["flag"]
    elif value == LEXIC["flag"]:
        visible[row][col] = LEXIC["hidden"]
    return visible
            
def print_grid(grid: Grid) -> None:
    length = 4*len(grid[0]) + 1
    print(" ", end=" ")
    for x in range(len(grid[0])):
        print("", x, "", end=" ")
    print()
    for y, row in enumerate(grid):
        print("", "".join(["-" for _ in range(length)]))
        print(y, "|", sep="", end="")
        for x, cell in enumerate(row):
            print("", cell, "", sep=" ", end="|")
        print()
    return

def has_won(hidden: Grid, visible: Grid, mines: list[Coord]) -> bool:
    rows, cols = len(hidden), len(hidden[0])
    for row in range(rows):
        for col in range(cols):
            if (col, row) not in mines and hidden[row][col] != visible[row][col]:
                return False
    return True

def has_lost(visible: Grid, row: int, col: int) -> bool:
    return visible[row][col] == LEXIC["mine"]
