class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([c.lower() for c in s if c.isalnum()])
        mid = len(s) // 2
        for i in range(mid):
            low = i
            high = len(s)-1-i
            if s[low] != s[high]:
                return False
        return True
