"""
Exercice 2 - Valid Palindrome

Ecrire la fonction is_palindrome(s).

La fonction doit retourner True si la chaine est un palindrome.

Regles :
- ignorer les espaces ;
- ignorer la ponctuation ;
- ignorer la casse ;
- garder les lettres et les chiffres.

Une chaine vide, ou une chaine sans lettre ni chiffre, est consideree comme
un palindrome.

Exemple :
s = "A man, a plan, a canal: Panama"
resultat attendu : True
"""


def is_palindrome(s: str) -> bool:
    pal = "".join([char.lower() for char in s if char.isalnum()])
    return pal == pal[::-1]

def check(name: str, result: bool, expected: bool) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("phrase palindrome", "A man, a plan, a canal: Panama", True),
    ("phrase non palindrome", "race a car", False),
    ("espace seul", " ", True),
    ("chiffre et lettre", "0P", False),
    ("autre phrase palindrome", "No lemon, no melon", True),
    ("ponctuation seule", ".,,,", True),
    ("casse differente", "Aa", True),
]


if __name__ == "__main__":
    passed = 0

    for name, s, expected in tests:
        result = is_palindrome(s)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
