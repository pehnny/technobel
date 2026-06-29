"""
Exercice 4 - Subarray Sum Equals K

Ecrire la fonction subarray_sum(nums, k).

La fonction doit retourner le nombre de sous-tableaux continus dont la somme
vaut k.

Un sous-tableau continu correspond a une partie de la liste sans trou.

Exemple :
nums = [1, 1, 1]
k = 2
resultat attendu : 2
"""


def subarray_sum(nums: list[int], target: int) -> int:
    solution = 0
    state = 0
    for left, num in enumerate(nums):
        state = num
        if state == target:
            solution += 1
        for other in nums[left+1:]:
            state += other
            if state == target:
                solution += 1
    return solution

    count = 0
    prefix_sum = 0
    seen = {0: 1}  # avant tout élément, la somme 0 existe une fois

    for num in nums:
        prefix_sum += num
        complement = prefix_sum - target
        if complement in seen:
            count += seen[complement]
        if prefix_sum in seen:
            seen[prefix_sum] += 1
        else:
            seen[prefix_sum] = 1

    return count

def check(name: str, result: int, expected: int) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("sommes simples", [1, 1, 1], 2, 2),
    ("deux possibilites", [1, 2, 3], 3, 2),
    ("avec negatif et zero", [1, -1, 0], 0, 3),
    ("cas plus long", [3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
]


if __name__ == "__main__":
    passed = 0

    for name, nums, k, expected in tests:
        result = subarray_sum(nums, k)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
