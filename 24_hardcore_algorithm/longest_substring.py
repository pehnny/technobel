def longest_substring_with_at_most_k_distinct_characters(text: str, k: int) -> int:
    if len(text) == 0:
        return 0

    distincts: dict[str, int] = {}
    left = 0
    longest = 0
    for right in range(len(text)):
        char = text[right]
        if char not in distincts:
            distincts[char] = 1
        else:
            distincts[char] += 1
        while len(distincts) > k:
            first = text[left]
            distincts[first] -= 1
            if distincts[first] == 0:
                distincts.pop(first, 0)
            left += 1
        size = right - left + 1
        longest = max(longest, size)
    return longest
