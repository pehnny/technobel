"""
IS SUBSEQUENCE
Pattern: Two Pointers

Given two strings `s` and `t`, return True if `s` is a subsequence of
`t`. A subsequence keeps the characters in order but may skip some.
You do NOT rearrange characters.

Examples:
    is_subsequence("abc", "ahbgdc") -> True
    is_subsequence("axc", "ahbgdc") -> False

Think about: walk through `t` with one pointer. Keep a second pointer
on `s`. Every time the current character of `t` matches the character
`s` is waiting for, advance the `s` pointer. Did `s` reach the end?
"""
from testkit import check, report

def is_subsequence(s, t):
    if len(s) == 0:
        return True
    
    s_pointer = 0
    for char in t:
        if char == s[s_pointer]:
            s_pointer += 1
        if s_pointer == len(s):
            return True
    return False

if __name__ == "__main__":
    check("is a subsequence", is_subsequence("abc", "ahbgdc"), True)
    check("not a subsequence", is_subsequence("axc", "ahbgdc"), False)
    check("empty s", is_subsequence("", "anything"), True)
    check("empty t", is_subsequence("a", ""), False)
    check("equal strings", is_subsequence("abc", "abc"), True)
    check("order matters", is_subsequence("ba", "ab"), False)
    report()
