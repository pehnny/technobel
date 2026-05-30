# Opérateurs

Manipuler des valeurs avec les opérateurs arithmétiques, de comparaison et logiques.

## Concepts abordés

- Opérateurs arithmétiques
- Division entière et modulo
- Opérateurs de comparaison
- Opérateurs logiques
- Priorité des opérateurs

## À retenir

### Opérateurs arithmétiques

| Opérateur | Signification       | Exemple       | Résultat |
|:---------:|---------------------|:-------------:|:--------:|
| `+`       | Addition            | `7 + 3`       | `10`     |
| `-`       | Soustraction        | `7 - 3`       | `4`      |
| `*`       | Multiplication      | `7 * 3`       | `21`     |
| `/`       | Division réelle     | `7 / 2`       | `3.5`    |
| `//`      | Division entière    | `7 // 2`      | `3`      |
| `%`       | Modulo (reste)      | `7 % 2`       | `1`      |
| `**`      | Puissance           | `2 ** 8`      | `256`    |

### `//` et `%` — cas d'usage classique

Convertir un nombre de secondes en jours, heures, minutes, secondes :

```python
total = 90061   # secondes
jours    = total // 86400
heures   = (total % 86400) // 3600
minutes  = (total % 3600)  // 60
secondes = total % 60
# → 1 jour, 1 heure, 1 minute, 1 seconde
```

### Échange sans variable temporaire (arithmétique)

```python
a = a + b
b = a - b   # b = (a+b) - b = a (ancienne valeur)
a = a - b   # a = (a+b) - a = b (ancienne valeur)
```

Attention : provoque un dépassement (*overflow*) pour de très grands entiers dans d'autres langages. En Python, préférer `a, b = b, a`.

### Opérateurs de comparaison

Retournent toujours `True` ou `False`.

| Opérateur | Signification      |
|:---------:|--------------------|
| `==`      | Égal               |
| `!=`      | Différent          |
| `<`       | Strictement inférieur |
| `<=`      | Inférieur ou égal  |
| `>`       | Strictement supérieur |
| `>=`      | Supérieur ou égal  |

### Opérateurs logiques

| Opérateur | Signification                          | Exemple                    |
|:---------:|----------------------------------------|:---------------------------|
| `and`     | Vrai si les deux sont vrais            | `True and False` → `False` |
| `or`      | Vrai si au moins un est vrai           | `True or False`  → `True`  |
| `not`     | Inverse la valeur                      | `not True`       → `False` |

### Priorité des opérateurs (de la plus haute à la plus basse)

1. `**`
2. `*`, `/`, `//`, `%`
3. `+`, `-`
4. `<`, `<=`, `>`, `>=`, `==`, `!=`
5. `not`
6. `and`
7. `or`

En cas de doute, parenthèses `( )` toujours.
