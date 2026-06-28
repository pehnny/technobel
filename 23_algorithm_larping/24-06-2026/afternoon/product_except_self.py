"""
Exercice 1 - Product of Array Except Self

Ecrire la fonction product_except_self(nums).

La fonction doit retourner une nouvelle liste result.
Pour chaque index i, result[i] doit contenir le produit de tous les elements
de nums sauf nums[i].

Exemple :
nums = [1, 2, 3, 4]
resultat attendu : [24, 12, 8, 6]
"""


def product_except_self(nums: list[int]) -> list[int]:
    solution = [1 for _ in nums]
    product = 1
    for i, num in enumerate(nums):
        solution[i] *= product
        product *= num
    
    product = 1
    right = len(nums)-1
    for num in reversed(nums):
        solution[right] *= product
        product *= num
        right -=1
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
    ("cas classique", [1, 2, 3, 4], [24, 12, 8, 6]),
    ("avec un zero", [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ("deux elements", [2, 3], [3, 2]),
    ("deux zeros", [0, 0], [0, 0]),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, expected in tests:
        result = product_except_self(nums)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
