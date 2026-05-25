def recursive_sum(array: list[int]) -> int:
    """Sum the elements of `array` recurively
    """
    size = len(array)
    
    if size == 1:
        return array[0]
    elif size == 0:
        return 0
    
    return array[-1] + recursive_sum(array[0:-1])

    
