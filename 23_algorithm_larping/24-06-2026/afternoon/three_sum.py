"""
Exercice 5 - 3Sum Bonus

Ecrire la fonction three_sum(nums).

La fonction doit retourner tous les triplets uniques dont la somme vaut 0.

Regles :
- un triplet contient exactement trois nombres ;
- chaque triplet doit avoir une somme egale a 0 ;
- les triplets en double ne doivent apparaitre qu'une seule fois ;
- l'ordre des triplets et l'ordre global n'ont pas d'importance.

Exemple :
nums = [-1, 0, 1, 2, -1, -4]
resultat attendu : [[-1, -1, 2], [-1, 0, 1]]
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    solution = []
    for left, first in enumerate(nums):
        visited = set()
        for second in nums[left+1:]:
            third = 0 - first - second
            if third in visited:
                item = sorted([first, second, third])
                if item not in solution:
                    solution.append(item)
            else:
                visited.add(second)
    return solution


def normalize_triplets(triplets: list[list[int]]) -> list[list[int]]:
    return sorted([sorted(triplet) for triplet in triplets])


def check(name: str, result: list[list[int]], expected: list[list[int]]) -> bool:
    if not isinstance(result, list):
        print(f"[KO] {name}")
        print(f"     obtenu   : {result}")
        print(f"     attendu  : {expected}")
        return False

    normalized_result = normalize_triplets(result)
    normalized_expected = normalize_triplets(expected)

    if normalized_result == normalized_expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    (
        "cas classique",
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]],
    ),
    ("aucun triplet", [0, 1, 1], []),
    ("trois zeros", [0, 0, 0], [[0, 0, 0]]),
    (
        "doublons a eviter",
        [-2, 0, 1, 1, 2],
        [[-2, 0, 2], [-2, 1, 1]],
    ),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, expected in tests:
        result = three_sum(nums)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
