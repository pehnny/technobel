import re

def count_vowels(text: str) -> int:
    text = text.lower()
    pattern = re.compile(r"[aeyuio]+?")
    find = pattern.findall(text)
    return len(find)