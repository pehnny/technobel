def longest_consecutive(sequence: list[int]) -> int:
    longest = 0
    unique = set(sequence)
    for num in unique:
        if num-1 not in unique:
            count = 1
            consecutive = num + 1
            while consecutive in unique:
                count += 1
                consecutive += 1
            longest = max(longest, count)
    return longest
