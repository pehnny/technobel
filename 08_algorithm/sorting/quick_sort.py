import random
from typing import Protocol, Self

class Comparable(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...
    def __le__(self, other: Self, /) -> bool: ...
    def __ge__(self, other: Self, /) -> bool: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __neq__(self, value: object, /) -> bool: ...


def quick_sort[T: Comparable](arr: list[T]) -> list[T]:
    """Sort arrays by recursion using divide and conquer strategy.
    Average case is `O(nlog(n))`. Depends on the choice of pivot.

    Trade of is worst case `O(n²)`. This occurs when you pick a pivot who is either de minimum or the maximum
    and when the list has a lot of duplicated elements.
    """
    if len(arr) < 2 :
        return arr
    
    pivot = arr[-1]
    smaller = [value for value in arr[1:] if value <= pivot]
    bigger = [value for value in arr[1:] if value > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)
