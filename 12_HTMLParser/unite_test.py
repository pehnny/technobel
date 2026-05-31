from parser import parser

# (entrée, résultat attendu, description)
TEST_CASES: list[tuple[str, bool | str, str]] = [

    # ── Cas 1 : chaîne valide ─────────────────────────────────────────────────
    ("<p></p>",
     True,
     "balise simple correctement fermée"),

    ("<p><b></b></p>",
     True,
     "imbrication à deux niveaux"),

    ("<p><b><i></i></b></p>",
     True,
     "imbrication à trois niveaux"),

    ("<div><p><b><i><a></a></i></b></p></div>",
     True,
     "les cinq balises imbriquées"),

    ("<p></p><b></b>",
     True,
     "deux balises sœurs à la racine"),

    ("<p><b></b><i></i></p>",
     True,
     "deux balises sœurs dans un même parent"),

    ("<a><div><p></p></div><b><i></i></b></a>",
     True,
     "arbre plus complexe"),

    ("",
     True,
     "chaîne vide"),

    # ── Cas 2 : mauvaise fermeture ────────────────────────────────────────────
    ("<p></b>",
     "p",
     "mismatch simple"),

    ("<p><b></p>",
     "b",
     "fermante dans le mauvais ordre"),

    ("<div><p><b></div>",
     "b",
     "triple imbrication mal fermée"),

    ("<p>",
     False,
     "ouvrante seule, jamais fermée"),

    ("<p><b></b>",
     False,
     "p ouverte mais jamais fermée"),

    ("<a><i><b></b><p></p>",
     False,
     "i et a jamais fermées"),

    # ── Cas 3 : fermante sans ouvrante ────────────────────────────────────────
    ("</p>",
     False,
     "fermante seule sans ouvrante"),

    ("<p></p></b>",
     False,
     "fermante orpheline après une paire correcte"),

    ("<p></p><b></b></i>",
     False,
     "fermante orpheline après plusieurs paires correctes"),

    ("</div><p></p>",
     False,
     "fermante orpheline au début"),

    ("<p><b></b></p></a>",
     False,
     "fermante orpheline après un arbre valide"),
]


def run_tests() -> None:
    passed = 0
    failed = 0

    cas1 = [t for t in TEST_CASES if t[1] is True]
    cas2 = [t for t in TEST_CASES if isinstance(t[1], str)]
    cas3 = [t for t in TEST_CASES if t[1] is False]

    for label, group in [("Cas 1 — chaîne valide", cas1),
                         ("Cas 2 — mauvaise fermeture", cas2),
                         ("Cas 3 — fermante sans ouvrante", cas3)]:
        print(f"\n{label}")
        print("─" * 45)
        for html, expected, description in group:
            result = parser(html)
            ok = result == expected
            status = "✓" if ok else "✗"
            if ok:
                passed += 1
                print(f"  {status} {description}")
            else:
                failed += 1
                print(f"  {status} {description}")
                print(f"      entrée   : {html!r}")
                print(f"      attendu  : {expected!r}")
                print(f"      obtenu   : {result!r}")

    total = passed + failed
    print(f"\n{'═' * 45}")
    print(f"  {passed}/{total} tests réussis", end="")
    print(f"  ({failed} échec(s))" if failed else "  — tous réussis")


if __name__ == "__main__":
    run_tests()
