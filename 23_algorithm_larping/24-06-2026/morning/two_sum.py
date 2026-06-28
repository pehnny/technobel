"""
Exercice 1 - Two Sum

Ecrire la fonction two_sum(nums, target).

La fonction doit retourner les indices de deux nombres dont la somme vaut target.

Regles :
- Il existe exactement une solution.
- Il ne faut pas utiliser deux fois le meme element.
- L'ordre des indices retournes doit correspondre aux tests attendus.

Exemple :
nums = [2, 7, 11, 15]
target = 9
resultat attendu : [0, 1]
"""
def two_sum(nums: list[int], target: int) -> list[int]:
    visited = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in visited:
            return [visited[difference], i]
        if num not in visited:
            visited[num] = i
    return []


def check(name: str, result: list[int], expected: list[int]) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("cas simple", [2, 7, 11, 15], 9, [0, 1]),
    ("solution au milieu", [3, 2, 4], 6, [1, 2]),
    ("deux valeurs identiques", [3, 3], 6, [0, 1]),
    ("nombres negatifs", [-1, -2, -3, -4, -5], -8, [2, 4]),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, target, expected in tests:
        result = two_sum(nums, target)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
