"""
CHALLENGE 22

A data-masking tool replaces characters in a token with other characters.
Two tokens are "structurally equal" if one can be turned into the other
by a consistent one-to-one replacement: every occurrence of a character
maps to the same character, and no two different characters map to the
same one.

Given two equal-length tokens, return True if they are structurally
equal, otherwise False.

Examples:
    same_shape("egg", "add")     -> True
    same_shape("foo", "bar")     -> False

"""

from testkit import check, report


def same_shape(a: str, b: str) -> bool:
    a_form = set([char for char in a])
    b_form = set([char for char in b])
    return len(a_form) == len(b_form)

if __name__ == "__main__":
    check("matching shape", same_shape("egg", "add"), True)
    check("conflict", same_shape("foo", "bar"), False)
    check("paper title", same_shape("paper", "title"), True)
    check("not bijective", same_shape("badc", "baba"), False)
    check("different lengths", same_shape("ab", "a"), False)
    check("both empty", same_shape("", ""), True)
    check("collapse", same_shape("ab", "aa"), False)
    check("single char", same_shape("a", "z"), True)
    report()
