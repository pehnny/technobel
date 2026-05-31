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

---

## Exercices du dossier

### Exercice 1 — 100 premiers nombres premiers

Écrivez `is_prime_number(n: int) -> bool` qui teste la primalité en divisant `n` par tous les entiers de 2 à n-1. Utilisez-la dans une boucle `while` pour collecter les 100 premiers nombres premiers.

**Astuce :** on peut optimiser en testant jusqu'à `√n` seulement, mais la version naïve suffit ici.

### Exercice 2 — Majorité

Écrivez `is_major(age: int) -> bool` avec une **expression ternaire** : retourne `True` si l'âge est strictement supérieur à 17, `False` sinon.

```python
return True if age > 17 else False
```

### Exercice 3 — Jeu de devinette (while + walrus)

Le programme tire un entier entre 1 et 100. L'utilisateur entre des propositions jusqu'à trouver ou taper `"stop"`. Utilisez le walrus operator `:=` pour intégrer la lecture dans la condition du `while` :

```python
while (answer := input("...")) != "stop":
    ...
```

### Exercice 4 — Affichage caractère par caractère

Écrivez `printc(text: str)` qui affiche chaque caractère d'une chaîne sur une ligne séparée en parcourant directement la chaîne avec `for c in text`.

### Exercice 5 — Caisse à cafés

Boucle de commande : à chaque itération, l'utilisateur commande un café (taille, type, sucre). Le programme calcule le prix et l'accumule. Quand l'utilisateur tape `"stop"`, le total est affiché. Définissez la logique du café dans une **fonction imbriquée**.

### Exercice 6 — Inversion de chaîne

Écrivez `print_reverse(text: str)` qui affiche la chaîne à l'envers en parcourant les index en ordre décroissant avec `range(len(text)-1, -1, -1)` et en accumulant les caractères dans une nouvelle chaîne.

---

### Challenge — Pavage récursif

[05_iteration/challenge.py](challenge.py)

Un couloir de longueur `n` peut être pavé avec des carreaux de 1 ou 2 unités, chacun disponible en 2 couleurs. Combien de façons différentes peut-on réaliser ce pavage ?

| Longueur | Pavages |
|:--------:|:-------:|
| 0        | 0       |
| 1        | 2       |
| 2        | 8       |
| 3        | 20      |
| 4        | 56      |

**Relation de récurrence :**

```
pavage(n) = 2 × pavage(n-1) + 4 × pavage(n-2)
```

Deux choix pour poser un carreau simple (longueur 1) sur le reste de longueur n-1, ou quatre choix pour poser un carreau double (longueur 2) sur le reste de longueur n-2.

---

### Solution — exercices de base

[05_iteration/main.py](main.py)
