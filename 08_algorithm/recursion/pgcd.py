
def pgcd(a: int, b: int) -> int:
    """Use a divide and conquer strategy

    Let be a rectangle of dimensions `(a, b)`.

    Base case is the smallest fits `n` times in the largest.

    Recursion case is trying again with the remainder from the smallest
    who doesn't fit the largest.
    """
    small = min(a, b)
    large = max(a, b)
    remainder = large % small

    if not remainder:
        return small
        
    return pgcd(remainder, large)
