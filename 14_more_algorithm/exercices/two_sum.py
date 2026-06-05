def two_sum(array: list[int], target: int) -> tuple[int, int]:
    if len(array) < 2:
        return (-1, -1)
    
    visited: dict[int, int] = {}
    for i, value in enumerate(array):
        diff = target - value
        if diff in visited:
            return (visited[diff], i)
        if value not in visited:
            visited[value] = i
    return (-1, -1)
    # Greedy solution
    for i, value1 in enumerate(array[:-1]):
        for j, value2 in enumerate(array[1:]):
            if value1 + value2 == target:
                return (i, j+1)
    return (-1, -1)