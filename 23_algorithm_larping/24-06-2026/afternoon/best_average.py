"""
Exercice 3 - Best Average Score

Ecrire la fonction best_average(scores, k).

On te donne une liste de scores et un nombre k.
Tu dois trouver la meilleure moyenne possible sur k scores consécutifs.

Exemple :
scores = [1, 12, -5, -6, 50, 3]
k = 4

Les groupes de 4 scores consécutifs sont :
[1, 12, -5, -6]  -> moyenne = 0.5
[12, -5, -6, 50] -> moyenne = 12.75
[-5, -6, 50, 3]  -> moyenne = 10.5

Résultat attendu : 12.75
"""


def best_average(scores: list[int], k: int) -> float:
    numerator = sum(scores[:k])
    state = numerator
    left = 0
    for right in range(k, len(scores)):
        state = state - scores[left] + scores[right]
        numerator = max(numerator, state)
        left += 1
    return numerator / k

def check(name: str, result: float, expected: float) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("cas classique", [1, 12, -5, -6, 50, 3], 4, 12.75),
    ("taille 1", [5], 1, 5.0),
    ("tous positifs", [4, 2, 1, 3, 6], 2, 4.5),
    ("avec negatifs", [-1, -12, -5, -6, -50, -3], 2, -5.5),
    ("k egal longueur", [2, 4, 6, 8], 4, 5.0),
]


if __name__ == "__main__":
    passed = 0

    for name, scores, k, expected in tests:
        result = best_average(scores, k)

        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
