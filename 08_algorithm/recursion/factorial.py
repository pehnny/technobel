def factorial(n: int) -> int:
    """Base case : return 1 if n == 0 or n == 1

    Recursion case : return n * factorial(n-1)
    """
    if not isinstance(n, int):
        raise TypeError(f"Factorial is undefined for type {type(n)}")
    if n < 0 :
        raise ValueError("Factorial is undefined for n < 0")
    
    if n == 0:
        return 1
    return n * factorial(n-1)
