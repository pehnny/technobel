from typing import Protocol, Self

class Comparable(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...
    def __gt__(self, other: Self, /) -> bool: ...

def _index_smallest[T: Comparable](arr: list[T]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for index, value in enumerate(arr):
        if value < smallest:
            smallest = value
            smallest_index = index
    return smallest_index
    
def _index_greatest[T: Comparable](arr: list[T]) -> int:
    greatest = arr[0]
    greatest_index = 0
    for index, value in enumerate(arr):
        if value > greatest:
            greatest = value
            greatest_index = index
    return greatest_index

def selection_sort[T: Comparable](arr: list[T], ascending: bool = True) -> list[T]:
    """Easiest sorting algorithm to implement

    Trade of is complexity `O(n²)`
    """
    new_arr = []
    copied_arr = arr.copy()
    func = _index_smallest if ascending else _index_greatest
    for _ in arr:
        index = func(copied_arr)
        new_arr.append(copied_arr.pop(index))
    return new_arr

