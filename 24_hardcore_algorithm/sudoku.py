def sudoku(grid: list[list[str]]) -> bool:
    rows: dict[str, set[str]] = {str(i): set() for i in range(9)}
    cols: dict[str, set[str]] = {str(i): set() for i in range(9)}
    blocs: dict[str, set[str]] = {str((i//3, j//3)): set() for i in range(0,9,3) for j in range(0,9,3)}

    for row in range(9):
        for col in range(9):
            current = grid[row][col]
            if current != ".":
                if current in rows[str(row)]:
                    return False
                if current in cols[str(col)]:
                    return False
                bloc = str((row //3, col//3))
                if current in blocs[bloc]:
                    return False
                rows[str(row)].add(current)
                cols[str(col)].add(current)
                blocs[bloc].add(current)
    return True
