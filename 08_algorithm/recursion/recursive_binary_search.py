from typing import Optional

def recursive_binary_search(arr: list[int], value: int, offset = 0) -> Optional[int]:
    """Binary search by recursion. 
    `offset` should be used whenever the `arr` is a slice depanding on a bigger array
    starting after 0. Exemple : `recursive_binary_search(arr[n:], value, n)`

    ``arr`` must be sorted !
    """
    if arr == []:
        return None
    
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    if value == arr[mid] :
        return mid + offset
    elif value < arr[mid]:
        return recursive_binary_search(arr[:mid], value, offset)
    else:
        offset += mid + 1
        return recursive_binary_search(arr[mid+1:], value, offset)
