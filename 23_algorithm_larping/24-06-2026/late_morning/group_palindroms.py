"""
Exercice 4 - Group Anagrams

Ecrire la fonction group_anagrams(words).

La fonction doit grouper les mots qui sont des anagrammes.

Regles pour faciliter les tests :
- chaque groupe doit etre trie alphabetiquement ;
- les groupes doivent etre tries selon leur premier element.

Exemple :
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
resultat attendu :
[["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in words:
        group = "".join(sorted(word))
        if group not in groups:
            groups[group] = [word]
        else:
            groups[group].append(word)
    return sorted([sorted(groups[group]) for group in groups])

def check(name: str, result: list[list[str]], expected: list[list[str]]) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    (
        "plusieurs groupes",
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]],
    ),
    (
        "un groupe et un mot seul",
        ["abc", "bca", "xyz"],
        [["abc", "bca"], ["xyz"]],
    ),
    ("liste vide", [], []),
    ("chaine vide", [""], [[""]]),
    ("doublons", ["ab", "ba", "ab"], [["ab", "ab", "ba"]]),
    ("mots d'une lettre", ["b", "a", "b"], [["a"], ["b", "b"]]),
]


if __name__ == "__main__":
    passed = 0

    for name, words, expected in tests:
        result = group_anagrams(words)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
