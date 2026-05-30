# Itération

Répéter des instructions avec les boucles `for` et `while`, et structurer la répétition avec la récursion.

## Concepts abordés

- Boucle `for` avec `range()`
- Boucle `while`
- Walrus operator `:=`
- Instructions `break` et `continue`
- Récursion (cas de base + cas récursif)

## À retenir

### Boucle `for`

Itère sur une séquence (liste, chaîne, `range`…).

```python
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for c in "hello":       # h, e, l, l, o
    print(c)
```

`range(start, stop, step)` :

```python
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(10, 0, -1)  # 10, 9, 8, ..., 1
```

### Boucle `while`

S'exécute tant que la condition est vraie.

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

### Walrus operator `:=` (Python 3.8+)

Affecte une variable **et** évalue sa valeur dans la même expression. Pratique dans les conditions de boucle.

```python
# Sans walrus
saisie = input("> ")
while saisie != "quit":
    print(saisie)
    saisie = input("> ")

# Avec walrus
while (saisie := input("> ")) != "quit":
    print(saisie)
```

### `break` et `continue`

```python
for i in range(10):
    if i == 5:
        break       # sort immédiatement de la boucle
    if i % 2 == 0:
        continue    # passe à l'itération suivante
    print(i)        # affiche 1, 3
```

### Récursion

Une fonction est récursive quand elle **s'appelle elle-même**. Toute récursion doit avoir :

1. Un **cas de base** — condition d'arrêt, sans appel récursif.
2. Un **cas récursif** — appel sur un problème plus petit.

```python
def factorial(n: int) -> int:
    if n == 0:          # cas de base
        return 1
    return n * factorial(n - 1)   # cas récursif
```

Trace pour `factorial(4)` :

```
factorial(4)
  → 4 * factorial(3)
       → 3 * factorial(2)
            → 2 * factorial(1)
                 → 1 * factorial(0)
                      → 1
```

### Récursion vs itération

| Critère       | Récursion                        | Itération              |
|---------------|----------------------------------|------------------------|
| Lisibilité    | Souvent plus proche de la déf. mathématique | Plus verbeux mais explicite |
| Mémoire       | Empile des appels (risque `RecursionError`) | Mémoire constante |
| Performance   | Surcoût des appels de fonction   | Généralement plus rapide |

En Python, la pile est limitée à ~1000 appels par défaut (`sys.getrecursionlimit()`).
