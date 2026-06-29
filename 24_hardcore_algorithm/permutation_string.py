def is_anagram(window: dict[str, int], target: dict[str, int]) -> bool:
    for char in target:
        if window.get(char, 0) != target.get(char, 0):
            return False
    return True

def permutation_string(text: str, target: str) -> bool:
    # if len(target) == 0:
    #     return True
    # if len(target) > len(text):
    #     return False

    # sorted_target = sorted(target)
    # for left in range(len(text)-len(target)+1):
    #     right = left + len(target)
    #     if sorted(text[left:right]) == sorted_target:
    #         return True
    # return False

    verify: dict[str, int] = {}
    for char in target:
        if char not in verify:
            verify[char] = 1
        else:
            verify[char] += 1
    
    window: dict[str, int] = {}
    left = 0
    for right in range(len(text)):
        char = text[right]
        if char not in window:
            window[char] = 1
        else:
            window[char] += 1
        if right - left + 1 > len(target):
            previous = text[left]
            window[previous] -= 1
            if window[previous] == 0:
                window.pop(previous, 0)
            left += 1
        if right - left + 1 == len(target):
            if is_anagram(window, verify):
                return True
    return False
