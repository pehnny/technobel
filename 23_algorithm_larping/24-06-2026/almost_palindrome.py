"""
CHALLENGE 21

A promo code is considered "almost symmetric" if it reads the same
forwards and backwards after deleting at most one character. Given a
code, return True if it is already a palindrome or can become one by
removing a single character, otherwise False.

Examples:
    almost_palindrome("abca") -> True   (remove 'b' or 'c')
    almost_palindrome("abc")  -> False

"""
from testkit import check, report


def almost_palindrome(code):
    if code == code[::-1]:
        return True
    
    for i in range(len(code)):
        subcode = code[:i] + code[i+1:]
        if subcode == subcode[::-1]:
            return True
    return False


if __name__ == "__main__":
    check("already palindrome", almost_palindrome("aba"), True)
    check("remove one", almost_palindrome("abca"), True)
    check("cannot fix", almost_palindrome("abc"), False)
    check("empty", almost_palindrome(""), True)
    check("single char", almost_palindrome("a"), True)
    check("two chars", almost_palindrome("ab"), True)
    check("remove first", almost_palindrome("deeee"), True)
    check("needs two removals", almost_palindrome("abcda"), False)
    report()
