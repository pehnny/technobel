"""
CHALLENGE 17

A text effect for a banner reverses only the vowels of a caption while
leaving every other character exactly where it is. The vowels are
a, e, i, o, u in both lower and upper case; case is preserved as the
characters move.

Given the caption, return the new string with its vowels reversed.

Examples:
    flip_vowels("hello")    -> "holle"
    flip_vowels("computer") -> "cemputor"

"""

from testkit import check, report


def flip_vowels(caption: str):
    vowels = set(("a", "e", "y", "u", "i", "o"))
    stack = [char for char in caption if char.lower() in vowels]
    solution = [char for char in caption]
    for i in range(len(caption)):
        if solution[i].lower() in vowels:
            solution[i] = stack.pop()
    return "".join(solution)


if __name__ == "__main__":
    check("simple", flip_vowels("hello"), "holle")
    check("several vowels", flip_vowels("computer"), "cemputor")
    check("case preserved", flip_vowels("aA"), "Aa")
    check("no vowels", flip_vowels("xyz"), "xyz")
    check("empty", flip_vowels(""), "")
    check("single vowel", flip_vowels("hi"), "hi")
    report()
