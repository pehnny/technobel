def parse(data: str) -> list[int]:
    state = 0
    values = []
    for c in data:
        if c == "i":
            state += 1
        elif c == "d":
            state -= 1
        elif c == "s":
            state **= 2
        elif c == "o":
            values.append(state)
    return values