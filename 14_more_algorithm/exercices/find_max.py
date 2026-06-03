def find_max(array: list[int]) -> int:
    """Quick find max.
    
    Works basically like a quick sort but keeps only greater numbers.
    """
    if len(array) == 0:
        raise IndexError("array must not be empty")
    elif len(array) == 1:
        return array[0]
    
    half = len(array) // 2
    mid = array[half]
    greater = [value for value in array if value > mid]
    while len(greater) > 1:
        half = len(greater) // 2
        mid = greater[half]
        greater = [value for value in array if value > mid]
    if len(greater) == 0:
        return mid
    return greater[0]

    