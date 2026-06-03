import re

def is_palindrome(text: str) -> bool:
    text = text.lower()
    pattern = re.compile(r"\s+")
    clean_text = "".join(pattern.split(text))
    
    mid = len(clean_text) // 2
    for i in range(mid):
        j = len(clean_text) - i - 1
        if clean_text[i] != clean_text[j]:
            return False
    return True