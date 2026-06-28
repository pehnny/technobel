"""
Exercice 2 - Top K Frequent Elements

Ecrire la fonction top_k_frequent(nums, k).

La fonction doit retourner les k elements les plus frequents dans nums.

L'ordre du resultat n'a pas d'importance.

Exemple :
nums = [1, 1, 1, 2, 2, 3]
k = 2
resultat attendu : [1, 2]
"""

import heapq
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    if len(nums) == 0:
        return []

    duplicates = {}
    for num in nums:
        if num not in duplicates:
            duplicates[num] = 1
        else:
            duplicates[num] += 1

    stack = []
    for num in duplicates:
        item = (duplicates[num], num)
        heapq.heappush_max(stack, item)

    solution = []
    while len(solution) < k:
        item = heapq.heappop_max(stack)
        solution.append(item[1])
    return solution

def check(name: str, result: list[int], expected: list[int]) -> bool:
    if isinstance(result, list) and sorted(result) == sorted(expected):
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("deux plus frequents", [1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ("un seul element", [1], 1, [1]),
    ("k egal un", [4, 4, 4, 6, 6, 7], 1, [4]),
    ("frequences variees", [5, 3, 1, 1, 1, 3, 73, 1], 2, [1, 3]),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, k, expected in tests:
        result = top_k_frequent(nums, k)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
