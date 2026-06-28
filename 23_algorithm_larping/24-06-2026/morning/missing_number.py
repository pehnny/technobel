"""
Exercice 4 - Missing Number

Ecrire la fonction missing_number(nums).

La liste nums contient n nombres distincts dans la plage [0, n].
Un seul nombre de cette plage est manquant.

La fonction doit retourner le nombre manquant.

Exemple :
nums = [3, 0, 1]
resultat attendu : 2
"""


def missing_number(nums: list[int]) -> int:
    n = len(nums)
    euler = n * (n+1) // 2
    return euler - sum(nums)


def check(name: str, result: int, expected: int) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("nombre manquant au milieu", [3, 0, 1], 2),
    ("nombre manquant a la fin", [0, 1], 2),
    ("liste plus longue", [9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ("un seul element zero", [0], 1),
    ("un seul element un", [1], 0),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, expected in tests:
        result = missing_number(nums)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
