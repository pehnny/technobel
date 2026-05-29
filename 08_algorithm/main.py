import random
from searching.binary_search import binary_search
from sorting.selection_sort import selection_sort
from recursion.factorial import factorial
from recursion.pgcd import pgcd
from recursion.recursive_sum import recursive_sum
from recursion.recursive_count import recursive_count
from recursion.recursive_max import recursive_max
from recursion.recursive_binary_search import recursive_binary_search
from searching.breadth_first_search import breadth_first_search, is_person_seller, network

def main() -> None:
    # binary_search
    size = 32
    arr = list(range(size))
    value = random.randint(0, size-1)
    print(value, arr)
    print(binary_search(arr, value))

    # selection_sort
    size = 10
    arr = [random.randint(0, size) for _ in range(size)]
    print(arr)
    print(selection_sort(arr, False))

    #factorial
    size = 10
    print([factorial(i) for i in range(size)])

    # pgcd
    maximum = 50
    values = [random.randint(1, maximum) for _ in range(2)]
    print(values)
    print(pgcd(*values))

    # recursive_sum
    size = 10
    arr = list(range(size))
    print(recursive_sum(arr))

    # recursive_count
    size = 10
    arr = list(range(size))
    print(recursive_count(arr))

    # recursive_max
    size = 10
    arr = [random.randint(0, size) for _ in range(size)]
    print(arr)
    print(recursive_max(arr))

    # recursive_binary_search
    size = 32
    arr = list(range(size))
    value = random.randint(0, size-1)
    print(value, arr)
    print(recursive_binary_search(arr, value))

    # breadth_first_search
    print(breadth_first_search(network, "you", is_person_seller))
    return

if __name__ == "__main__":
    main()
