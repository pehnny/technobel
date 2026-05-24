from typing import Optional, Protocol

class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...

# The point of binary_search is that it makes looking
# for an item O(log(n)) instead of O(n).
# The trade of is the list has to be sorted.
def binary_search[T: Comparable](arr: list[T], item: T) -> Optional[int]:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
