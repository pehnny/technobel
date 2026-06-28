"""
Exercice 5 - Is Subsequence

Ecrire la fonction is_subsequence(s, t).

La fonction doit retourner True si s est une sous-sequence de t.

Une sous-sequence garde l'ordre des caracteres, mais les caracteres ne doivent
pas forcement etre cote a cote.

Exemple :
s = "abc"
t = "ahbgdc"
resultat attendu : True
"""


def is_subsequence(text: str, target: str) -> bool:
    if len(text) == 0:
        return True
    p_text = 0
    for char in target:
        if char == text[p_text]:
            p_text += 1
        if p_text == len(text):
            return True
    return False


def check(name: str, result: bool, expected: bool) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("sous-sequence simple", "abc", "ahbgdc", True),
    ("ordre impossible", "axc", "ahbgdc", False),
    ("s vide", "", "abc", True),
    ("t vide", "abc", "", False),
    ("caracteres non consecutifs", "ace", "abcde", True),
]


if __name__ == "__main__":
    passed = 0

    for name, s, t, expected in tests:
        result = is_subsequence(s, t)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
