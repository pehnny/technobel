def rotate(table: list[int], k: int) -> None:
    k = k % len(table)
    
    table[:] = table[:][::-1]
    table[:k] = table[:k][::-1]
    table[k:] = table[k:][::-1]
    return
