"""
CHALLENGE 8

A catalog tool wants to cluster product codes that are built from the
exact same set of letters in a different order (same letters, same
counts). Given a list of product codes, group together the ones that are
rearrangements of each other.

To keep the output predictable, return a list of groups where each group
is sorted alphabetically, and the groups themselves are sorted by their
first element.

Examples:
    cluster(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    cluster(["abc", "bca", "xyz"])
        -> [["abc", "bca"], ["xyz"]]

"""

from testkit import check, report

def cluster(codes: list[str]) -> list[list[str]]:
    if len(codes) == 0:
        return []
    elif len(codes) == 1:
        return [codes]
    
    def is_anagram(word: str, target: str) -> bool:
        if len(word) != len(target):
            return False
        
        visited = {}
        for char in word:
            if char not in visited:
                visited[char] = 1
            else:
                visited[char] += 1
        for char in target:
            if char not in visited:
                return False
            else:
                visited[char] -= 1
        for char in visited:
            if visited[char] != 0:
                return False
        return True
    
    groups = {codes[0]: [codes[0]]}
    for code in codes[1:]:
        is_grouped = False
        for group in groups:
            if is_anagram(code, group):
                groups[group].append(code)
                is_grouped = True
        if not is_grouped:
            groups[code] = [code]
    return sorted([sorted(groups[group]) for group in groups])


if __name__ == "__main__":
    check("classic groups",
          cluster(["eat", "tea", "tan", "ate", "nat", "bat"]),
          [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    check("two groups",
          cluster(["abc", "bca", "xyz"]),
          [["abc", "bca"], ["xyz"]])
    check("empty input", cluster([]), [])
    check("single empty string", cluster([""]), [[""]])
    check("single code", cluster(["a"]), [["a"]])
    check("duplicates kept",
          cluster(["ab", "ba", "ab"]),
          [["ab", "ab", "ba"]])
    report()
