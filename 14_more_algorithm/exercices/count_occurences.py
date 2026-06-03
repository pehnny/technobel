def count_occurences[T](array: list[T], target: T) -> int:
    count = 0
    for value in array:
        if value == target:
            count += 1
    return count
    