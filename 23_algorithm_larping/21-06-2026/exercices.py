def isAnagram(word: str, anagram: str) -> bool:
    if len(word) != len(anagram):
        return False
    
    visited = set()
    for c in anagram:
        if c not in visited:
            visited.add(c)
            if word.count(c) != anagram.count(c):
                return False
    return True


def singleNumber(nums: list[int]) -> int:
    """Expected O(n) time complexity and O(1) space

    My solution is O(n) time but O(n) space.
    The trick is to use the property of XOR operator:
    - communatative: a^b = b^a
    - associative: a^(b^c) = (a^b)^c
    - kernel: a^a = 0
    - neutral: 0^a = a

    Having every numbers appear twice but one end up finding the single number:
    - a^b^c^b^a = (a^a)^(b^b)^c = 0^0^c = c
    """
    state = 0
    for value in nums:
        state ^= value
    return state
    # visited = {}
    # for value in nums:
    #     if value not in visited:
    #         visited[value] = 1
    #     else:
    #         visited[value] += 1
    # return min(visited, key=lambda k:visited[k])

def missingNumber(self, nums: list[int]) -> int:
    """Euler formula
    """
    maximum = len(nums)+1
    total = maximum * (maximum-1) // 2
    return total - sum(nums)

def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) == 0:
        return True
        
    i = 0
    for c in t:
        if c == s[i]:
            i += 1
        if i == len(s):
            return True
    return False

def lengthOfLastWord(self, s: str) -> int:
    return len(s.strip().split()[-1])


def romanToInt(self, s: str) -> int:
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    value = romans[s[-1]]
    for i, c in enumerate(s[:-1]):
        nextc = s[i+1]
        if romans[c] < romans[nextc]:
            value -= romans[c]
        else:
            value += romans[c]
    return value
