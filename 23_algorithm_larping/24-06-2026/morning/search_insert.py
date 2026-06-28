"""
Exercice 2 - Search Insert Position

Ecrire la fonction search_insert(nums, target).

La liste nums est triee dans l'ordre croissant.

La fonction doit retourner :
- l'index de target si target est present dans nums ;
- sinon, l'index ou target devrait etre insere pour garder la liste triee.

Exemple :
nums = [1, 3, 5, 6]
target = 2
resultat attendu : 1
"""


def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = left + (right-left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return left


def check(name: str, result: int, expected: int) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("target present", [1, 3, 5, 6], 5, 2),
    ("insertion au milieu", [1, 3, 5, 6], 2, 1),
    ("insertion a la fin", [1, 3, 5, 6], 7, 4),
    ("insertion au debut", [1, 3, 5, 6], 0, 0),
    ("liste avec un element", [1], 0, 0),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, target, expected in tests:
        result = search_insert(nums, target)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
