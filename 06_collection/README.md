# Collections

Stocker et manipuler des groupes de données avec les structures intégrées de Python.

## Concepts abordés

- `list` — séquence ordonnée et mutable
- `tuple` — séquence ordonnée et immuable
- `set` — ensemble non ordonné sans doublons
- `dict` — table de correspondance clé → valeur
- `lambda`, `map()`, `filter()`

## À retenir

### `list`

```python
fruits = ["pomme", "banane", "cerise"]
fruits.append("datte")        # ajout en fin
fruits.insert(1, "abricot")   # insertion à l'index 1
fruits.remove("banane")       # suppression par valeur
fruits[0]                     # accès par index
fruits[-1]                    # dernier élément
fruits[1:3]                   # slicing → sous-liste
```

### `tuple`

Immuable : ne peut pas être modifié après création. Utilisé pour des données qui ne doivent pas changer, ou pour retourner plusieurs valeurs.

```python
point = (3, 7)
x, y = point          # déballage

def min_max(lst):
    return min(lst), max(lst)  # retourne un tuple

mini, maxi = min_max([4, 1, 9, 2])
```

### `set`

Pas de doublons, pas d'ordre garanti.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b   # intersection : {3, 4}
a | b   # union        : {1, 2, 3, 4, 5, 6}
a - b   # différence   : {1, 2}

# Supprimer les doublons d'une liste
unique = list(set([1, 2, 2, 3, 3, 3]))
```

### `dict`

```python
prix = {"café": 1.50, "thé": 1.20, "eau": 0.80}

prix["café"]           # accès : 1.50
prix["jus"] = 2.00     # ajout / mise à jour
del prix["eau"]        # suppression
"thé" in prix          # True

for cle, valeur in prix.items():
    print(f"{cle} : {valeur}€")
```

### `lambda`

Fonction anonyme en une ligne. Utilisée quand une fonction courte est passée en argument.

```python
doubler = lambda x: x * 2
doubler(5)   # 10

# Tri par critère personnalisé
personnes = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
personnes.sort(key=lambda p: p[1])   # tri par âge
```

### `map()` et `filter()`

`map(fonction, iterable)` — applique une fonction à chaque élément.

```python
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))   # [1, 4, 9, 16, 25]
```

`filter(fonction, iterable)` — garde les éléments pour lesquels la fonction retourne `True`.

```python
pairs = list(filter(lambda x: x % 2 == 0, nombres))   # [2, 4]
```

### List comprehension — alternative concise

```python
carres = [x**2 for x in nombres]
pairs  = [x for x in nombres if x % 2 == 0]
```

Préférer la comprehension quand la logique tient en une ligne et reste lisible.

## Récapitulatif — choisir la bonne structure

| Structure | Ordonné | Mutable | Doublons | Indexable |
|-----------|:-------:|:-------:|:--------:|:---------:|
| `list`    | ✓       | ✓       | ✓        | ✓         |
| `tuple`   | ✓       | ✗       | ✓        | ✓         |
| `set`     | ✗       | ✓       | ✗        | ✗         |
| `dict`    | ✓ (3.7+)| ✓       | clés: ✗  | par clé   |

---

## Exercices du dossier

### Exercice 1 — Somme d'une liste aléatoire

Générez 10 entiers aléatoires entre 1 et 100 dans une `list` et affichez leur somme avec `sum()`.

### Exercice 2 — Tuple et séparateur

Demandez le prénom et le nom à l'utilisateur, stockez-les dans un `tuple`, et affichez-les avec `print(*data, sep="\n")` (chaque élément sur sa propre ligne).

### Exercice 3 — Intersection de deux ensembles

Générez deux listes de 10 entiers aléatoires entre 1 et 20. Convertissez-les en `set` et utilisez `.intersection()` pour afficher les valeurs communes.

### Exercice 4 — Dictionnaire de prix

Définissez un `dict` `{fruit: prix}`. Proposez à l'utilisateur de choisir un fruit et affichez son prix avec `match / case`. Gérez l'absence de correspondance avec `case _`.

### Exercice 5 — Maximum par clé (lambda)

Étant donné une liste de tuples `(nom, âge)`, trouvez la personne la plus âgée en une ligne :
```python
oldest = max(data, key=lambda x: x[1])
```

### Exercice 6 — Filtrer les pairs

Générez 10 entiers aléatoires entre 1 et 50. Utilisez `filter(lambda x: not x % 2, nombres)` pour ne garder que les nombres pairs.

### Exercice 7 — Dédoublonnage

Étant donné une liste de mots avec répétitions (ex. `["bonjour", "bonjour", "banane"]`), affichez les valeurs uniques en passant par `set(mots)`.

### Exercice 8 — Dictionnaire de listes

Définissez un `dict` associant chaque cours (`str`) à une liste d'étudiants (`list[str]`). Proposez un choix à l'utilisateur et affichez la liste correspondante.

### Exercice 9 — Total de commande

Étant donné une liste de tuples `(article, quantité)` et un dictionnaire `prix`, calculez le coût total en itérant avec `for marchandise, quantité in commandes`.

### Exercice 10 — Statistiques salariales

Étant donné une liste de dictionnaires `{"nom": ..., "salaire": ..., "département": ...}` :
1. Calculez le salaire total et la moyenne globale avec `sum(map(lambda x: x["salaire"], entreprise))`.
2. Pour chaque département (extrait avec `set(map(...))`), calculez la moyenne salariale en combinant `filter()` et `map()`.

---

### Solution

[06_collection/main.py](main.py)
