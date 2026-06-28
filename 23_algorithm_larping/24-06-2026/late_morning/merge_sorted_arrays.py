"""
Exercice 3 - Merge Sorted Array

Ecrire la fonction merge_sorted_arrays(nums1, m, nums2, n).

Les listes nums1 et nums2 sont triees dans l'ordre croissant.

Pour ce test blanc, la fonction doit retourner une nouvelle liste triee
contenant les m premiers elements de nums1 et les n premiers elements de nums2.

Exemple :
nums1 = [1, 2, 3]
m = 3
nums2 = [2, 5, 6]
n = 3
resultat attendu : [1, 2, 2, 3, 5, 6]
"""


def merge_sorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    p1, p2 = 0, 0
    solution = []
    while p1 < m or p2 < n:
        if p1 == m:
            solution.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            solution.append(nums1[p1])
            p1 += 1
        else:
            if nums1[p1] < nums2[p2]:
                solution.append(nums1[p1])
                p1 +=1
            else:
                solution.append(nums2[p2])
                p2 += 1
    return solution
            


def check(name: str, result: list[int], expected: list[int]) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("deux listes", [1, 2, 3], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ("nums2 vide", [1], 1, [], 0, [1]),
    ("nums1 vide", [], 0, [1], 1, [1]),
    ("valeurs alternees", [0, 2, 4], 3, [1, 3, 5], 3, [0, 1, 2, 3, 4, 5]),
    ("nombres negatifs", [-3, -1], 2, [-2, 0, 2], 3, [-3, -2, -1, 0, 2]),
    ("m et n partiels", [1, 4, 99], 2, [2, 3, 100], 2, [1, 2, 3, 4]),
]


if __name__ == "__main__":
    passed = 0

    for name, nums1, m, nums2, n, expected in tests:
        result = merge_sorted_arrays(nums1, m, nums2, n)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
