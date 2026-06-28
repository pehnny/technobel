from typing import Optional, Protocol, Self

class Comparable(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...

def binary_search[T: Comparable](arr: list[T], target: T) -> Optional[int]:
    """The point of binary_search is that it makes looking
    for an item `O(log(n))` instead of `O(n)`.

    The trade of is the list has to be sorted.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None
