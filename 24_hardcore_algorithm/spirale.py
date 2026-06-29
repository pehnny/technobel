def spirale(matrix: list[list[int]]) -> list[int]:
    if len(matrix) == 0:
        return []
        
    row_edges = [1, len(matrix)-1]
    col_edges = [0, len(matrix[0])-1]
    steps = len(matrix)*len(matrix[0])
    direction = (0,1)
    solution: list[int] = []
    state = (0,0)
    while len(solution) < steps:
        row, col = state
        solution.append(matrix[row][col])
        if direction == (0,1) and col == col_edges[1]:
            direction = (1,0)
            col_edges[1] -= 1
        if direction == (1,0) and row == row_edges[1]:
            direction = (0,-1)
            row_edges[1] -= 1
        if direction == (0,-1) and col == col_edges[0]:
            direction = (-1,0)
            col_edges[0] +=1
        if direction == (-1,0) and row == row_edges[0]:
            direction = (0,1)
            row_edges[0] += 1
        state = (state[0] + direction[0], state[1] + direction[1])
    return solution
