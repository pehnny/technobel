def find_missing(sequence: list[int]) -> int:
    possible = [sequence[i+1] - sequence[i] for i in range(3)]
    counts = [possible.count(value) for value in possible]
    step = 0
    for value, count in zip(possible, counts):
        if count > 1:
            step = value
                
    state = sequence[0]
    for value in sequence[1:]:
        state += step
        if value != state:
            return state
    return 0