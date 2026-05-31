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

---

## Exercices du dossier

### Exercice 1 — Évaluation d'expressions arithmétiques

Calculez à la main les valeurs successives de `a` à `g`, puis vérifiez avec Python :

```python
a = 12
b = 3*a + 8
c = b - 2*a
d = (c + 25) * b
e = (a + b) % 10
f = (c * d) // (b + 6)
g = (d + e) // (f - 9)
```

### Exercice 2 — Évaluation d'expressions booléennes

Avec `a = 13, b = 5, c = True`, évaluez chaque expression sans exécuter le code, puis vérifiez. La priorité des opérateurs (`and` avant `or`, `not` avant `and`) est souvent source d'erreurs.

```python
a > 10 and b < 20
c != 40 or not c >= 100
a == 2 and not b > 15
(a < b and c > 30) or not c < 200
```

### Exercice 3 — Échange sans variable temporaire (arithmétique)

Échangez les valeurs de deux entiers `a` et `b` en n'utilisant que les opérateurs `+` et `-`, sans aucune variable temporaire.

**Principe :**
```
a = a + b   # a contient maintenant la somme
b = a - b   # b = somme - b = ancienne valeur de a
a = a - b   # a = somme - nouvelle valeur de b = ancienne valeur de b
```

### Exercice 4 — Conversion de secondes

Écrivez une fonction qui convertit un nombre de secondes total en `(jours, heures, minutes, secondes)` à l'aide de `//` (division entière) et `%` (modulo).

```
4561 secondes → (0, 1, 16, 1)
```

| Unité    | Formule                      |
|----------|------------------------------|
| Jours    | `t // 86400`                 |
| Heures   | `t // 3600 % 24`             |
| Minutes  | `t // 60 % 60`               |
| Secondes | `t % 60`                     |

### Solution

[03_operators/main.py](main.py)
