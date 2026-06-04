def parts_sums(ls: list[int]) -> list[int]:
    if len(ls) == 0:
        return [0]
    elif len(ls) == 1:
        return ls
    
    state = sum(ls)
    parts = [state]
    
    for i in range(1, len(ls)+1):
        state -= ls[i-1]
        parts.append(state)
    return parts