"""
Exercice 5 - Longest Substring Without Repeating Characters

Ecrire la fonction length_of_longest_substring(s).

La fonction doit retourner la longueur de la plus longue sous-chaine sans
caractere repete.

Une sous-chaine est une partie continue de la chaine.

Exemple :
s = "abcabcbb"
resultat attendu : 3
"""

from collections import deque
def length_of_longest_substring(s: str) -> int:
    longest = 0
    window = deque()
    for char in s:
        if char.isalnum():
            while char in window:
                window.popleft()
        
        window.append(char)
        longest = max(longest, len("".join(window).strip()))
    return longest



def check(name: str, result: int, expected: int) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("repetition classique", "abcabcbb", 3),
    ("un seul caractere repete", "bbbbb", 1),
    ("repetition au milieu", "pwwkew", 3),
    ("chaine vide", "", 0),
    ("fenetre a ajuster", "dvdf", 3),
    ("double repetition", "abba", 2),
    ("tous differents", "abcdef", 6),
    ("espaces repetes", "a b c a", 5),
]


if __name__ == "__main__":
    passed = 0

    for name, s, expected in tests:
        result = length_of_longest_substring(s)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
