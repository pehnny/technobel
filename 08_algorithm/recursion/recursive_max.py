def recursive_max(arr: list[int]) -> int:
    """Return the maximum value of ``arr`` by recursion.

    The stack only resolve when the function reaches the end of the list.
    """
    if len(arr) == 1:
        return arr[0]
    elif arr == []:
        return 0

    if arr[0] > recursive_max(arr[1:]):
        return arr[0]
    return recursive_max(arr[1:])
