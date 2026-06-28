"""
CHALLENGE 12

A support system scans an incoming message and wants the position of the
first character that appears only once in the whole message (useful for
spotting a unique marker). Return the index of the first non-repeating
character. If every character repeats, return -1.

Examples:
    first_unique("garden")  -> 0
    first_unique("levelup") -> 2

"""

from testkit import check, report

def first_unique(message: str) -> int:
    if len(message) == 0:
        return -1
    elif len(message) == 1:
        return 0
    
    duplicates = {}
    for char in message:
        if char not in duplicates:
            duplicates[char] = 1
        else:
            duplicates[char] += 1
    first = min(duplicates, key=lambda k:duplicates[k])
    if duplicates[first] > 1:
        return -1
    return message.find(first)


if __name__ == "__main__":
    check("first char unique", first_unique("garden"), 0)
    check("unique later", first_unique("levelup"), 2)
    check("all repeat", first_unique("aabb"), -1)
    check("empty message", first_unique(""), -1)
    check("single char", first_unique("z"), 0)
    check("unique at end", first_unique("aabbc"), 4)
    report()
