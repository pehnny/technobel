def find_duplicate[T](array: list[T]) -> set[T]:
    if len(array) == 1:
        return set()
    
    duplicates: set[T] = set()
    for i, value1 in enumerate(array[:-1]):            
        for value2 in array[i+1:]:
            if value1 == value2:
                duplicates.add(value1)
    return duplicates
