def sum_pairs(ints: list[int], s: int) -> list[int] | None:
    """Same logic than two_sum() but we don't need to store 
    the index so a ``set`` is more efficient than a ``dict``
    """
    unique: set[int] = set()
    
    for value in ints:
        diff = s - value
        if diff in unique:
            return [diff, value]
        unique.add(value)
    return None
