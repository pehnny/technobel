def recursive_count(arr: list[int]) -> int:
    """Recursion version of `len(arr)`
    """
    if arr == []:
        return 0
    
    return 1 + recursive_count(arr[:-1])
