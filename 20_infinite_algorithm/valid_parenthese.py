class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack: list[str] = []
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in parentheses:
                if len(stack) < 1:
                    return False
                previous = stack.pop()
                if previous != parentheses[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        