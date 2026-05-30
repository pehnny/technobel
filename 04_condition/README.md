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
