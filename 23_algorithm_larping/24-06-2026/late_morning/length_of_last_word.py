"""
Exercice 1 - Length of Last Word

Ecrire la fonction length_of_last_word(s).

La fonction doit retourner la longueur du dernier mot de la chaine s.

Un mot est une suite de caracteres non separes par des espaces.
Si la chaine ne contient aucun mot, la fonction doit retourner 0.

Exemple :
s = "Hello World"
resultat attendu : 5
"""

def length_of_last_word(s: str) -> int:
    if len(s) == 0:
        return 0
    split = s.split()
    if len(split) == 0:
        return 0
    return len(split[-1])


def check(name: str, result: int, expected: int) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("deux mots", "Hello World", 5),
    ("espaces autour", "   fly me   to   the moon  ", 4),
    ("phrase simple", "luffy is still joyboy", 6),
    ("un seul caractere", "a", 1),
    ("seulement des espaces", "   ", 0),
    ("chaine vide", "", 0),
    ("mot avec espaces avant", "   python", 6),
]


if __name__ == "__main__":
    passed = 0

    for name, s, expected in tests:
        result = length_of_last_word(s)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
