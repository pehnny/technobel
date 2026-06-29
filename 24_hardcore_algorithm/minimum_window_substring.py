def is_valid(window: dict[str, int], target: dict[str, int]) -> bool:
    for char in target:
        if window.get(char, 0) < target.get(char, 0):
            return False
    return True

def minimum_window(text: str, target: str) -> str:
    if len(text) < len(target):
        return ""
    
    verif: dict[str, int] = {}
    for char in target:
        if char not in verif:
            verif[char] = 1
        else:
            verif[char] += 1

    left = 0
    solution = ""
    window: dict[str, int] = {}
    for right in range(len(text)):
        char = text[right]
        if char not in window:
            window[char] = 1
        else: 
            window[char] += 1

        valid = is_valid(window, verif)
        while valid:
            size = right - left + 1
            if solution == "" or size < len(solution):
                solution = text[left:right+1]
            previous = text[left]
            window[previous] -= 1
            if window[previous] == 0:
                window.pop(previous, 0)
            left += 1
            valid = is_valid(window, verif)
    return solution
