# Conditions

Exécuter différentes branches de code selon la valeur d'une expression.

## Concepts abordés

- `if / elif / else`
- `match / case` (Python 3.10+)
- Expressions booléennes
- Valeurs truthy / falsy

## À retenir

### `if / elif / else`

```python
if condition_1:
    ...
elif condition_2:
    ...
else:
    ...
```

- Les branches `elif` et `else` sont optionnelles.
- La première condition vraie est exécutée ; les suivantes sont ignorées.

```python
note = 14

if note >= 18:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 12:
    mention = "Assez bien"
elif note >= 10:
    mention = "Passable"
else:
    mention = "Insuffisant"
```

### `match / case` (Python 3.10+)

Préféré quand on compare une variable à plusieurs **valeurs fixes**.

```python
match taille:
    case "S":
        prix = 1.50
    case "M":
        prix = 2.00
    case "L":
        prix = 2.50
    case _:           # cas par défaut (équivalent du else)
        prix = 0
```

Le `case _` est le "catch-all" : il correspond à tout ce qui n'a pas été capturé avant.

### `match` avec conditions gardées

```python
match note:
    case n if n >= 10:
        print("Réussi")
    case _:
        print("Échoué")
```

### Valeurs truthy / falsy

En Python, une condition n'a pas besoin d'être un booléen explicite.

| Falsy (évalué à `False`) | Truthy (évalué à `True`) |
|--------------------------|--------------------------|
| `0`, `0.0`               | Tout entier ≠ 0          |
| `""` (chaîne vide)       | Toute chaîne non vide    |
| `[]`, `{}`, `()`         | Toute collection non vide|
| `None`                   | Tout objet non `None`    |
| `False`                  | `True`                   |

```python
name = input("Votre nom : ")
if name:          # True si name n'est pas vide
    print(f"Bonjour {name}")
else:
    print("Nom vide")
```

## Quand utiliser `match` plutôt que `if/elif` ?

| Situation | Recommandation |
|-----------|---------------|
| Comparaison à des valeurs fixes connues | `match / case` |
| Conditions avec intervalles ou expressions complexes | `if / elif / else` |
| Destruction de structures (tuples, classes) | `match / case` |

---

## Exercices du dossier

### Exercice 1 — Machine à café

Écrivez une fonction `cafe(size, kind, sugar)` qui calcule le prix d'un café :

| Paramètre | Valeur | Prix |
|-----------|--------|:----:|
| `size`    | `"small"` | 1.00 € |
| `size`    | `"large"` | 1.50 € |
| `kind`    | `"expresso"` | +0.50 € |
| `kind`    | `"cappucino"` | +0.70 € |
| `sugar`   | n sucres | +n × 0.10 € |

Utilisez `match / case` pour chaque paramètre. La valeur par défaut doit être `cafe()` = `"small"` expresso avec 2 sucres.

### Exercice 2 — Note numérique → lettre

Convertissez une note entière (0–9) en mention littérale avec une cascade `if / elif` :

| Note  | Mention |
|:-----:|:-------:|
| 0     | F       |
| 1–2   | E       |
| 3–4   | D       |
| 5–6   | C       |
| 7–8   | B       |
| ≥ 9   | A       |

### Exercice 3 — Jeu de devinette

Tirez un entier aléatoire entre 0 et 10 avec `random.randint()`. Demandez à l'utilisateur de le deviner et retournez `True` s'il a trouvé, `False` sinon. Comparez avec `==` en pensant à convertir la saisie.

### Exercice 4 — Calcul de l'IMC

Écrivez `calcul_imc(taille: float, poids: float) -> str` selon la formule `imc = poids / taille²` :

| IMC          | Catégorie  |
|:------------:|:----------:|
| < 18.5       | maigreur   |
| 18.5 – 24.9  | idéal      |
| 25.0 – 29.9  | surpoids   |
| ≥ 30.0       | obésité    |

Une cascade `if` suffit : dès qu'une condition est vraie, les suivantes ne sont pas évaluées.

### Exercice 5 — Générateur de citations

Proposez à l'utilisateur de choisir un auteur (`"Debord"` ou `"Hegel"`), puis affichez une citation aléatoire parmi celles stockées dans un dictionnaire. Gérez un auteur invalide avec `case _`.

---

### Solution

[04_condition/main.py](main.py)
