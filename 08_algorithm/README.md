# Recherche binaire

## Introduction

Imagine que tu cherches un mot dans un dictionnaire. Tu ne commences pas à la première page — tu ouvres le livre à peu près au milieu, tu regardes où tu en es, et tu décides d'aller à gauche ou à droite. Tu répètes jusqu'à trouver le mot. C'est exactement ça, la **recherche binaire**.

La recherche binaire est un algorithme qui permet de retrouver un élément dans une **liste triée** en divisant l'espace de recherche par deunx à chaque étape. Elle est l'un des algorithmes fondamentaux de l'informatique et sert de base à une grande partie des structures de données plus avancées.

### Condition indispensable

La liste doit être **triée**. Sans ça, l'algorithme ne peut pas décider dans quelle moitié chercher, et tout s'effondre.

### Le principe pas à pas

1. On regarde l'élément au **milieu** de la liste.
2. Si c'est la valeur cherchée : trouvé, on s'arrête.
3. Si la valeur cherchée est **inférieure** : on recommence sur la moitié **gauche**.
4. Si la valeur cherchée est **supérieure** : on recommence sur la moitié **droite**.
5. On répète jusqu'à trouver ou jusqu'à ce qu'il ne reste plus rien.

### Exemple

Liste triée : `[1, 3, 5, 7, 9, 11, 13]`, on cherche `7`.

| Étape | Gauche | Droite | Milieu | Valeur milieu | Décision          |
|-------|--------|--------|--------|---------------|-------------------|
| 1     | 0      | 6      | 3      | 7             | Trouvé !          |

Autre exemple, on cherche `11` :

| Étape | Gauche | Droite | Milieu | Valeur milieu | Décision           |
|-------|--------|--------|--------|---------------|--------------------|
| 1     | 0      | 6      | 3      | 7             | 11 > 7 → droite    |
| 2     | 4      | 6      | 5      | 11            | Trouvé !           |

### Complexité temporelle

| Algorithme          | Pire cas   |
|---------------------|------------|
| Recherche linéaire  | O(n)       |
| Recherche binaire   | O(log n)   |

Sur 1 000 éléments, la recherche linéaire peut faire 1 000 comparaisons. La recherche binaire en fait au plus **10** (log₂ 1000 ≈ 10). Sur 1 000 000 000 éléments : au plus **30 comparaisons**.

C'est la puissance du logarithme : chaque étape élimine la moitié du problème.

---

## Exercices

### Exercice 1 — Implémentation de base

Implémente la recherche binaire en Python. La fonction prend une liste triée et une valeur cible, et retourne l'index de la valeur si elle est présente, ou `-1` sinon.

```python
def binary_search(lst: list[int], target: int) -> int:
    ...
```

Teste avec :
- `binary_search([1, 3, 5, 7, 9], 7)` → `3`
- `binary_search([1, 3, 5, 7, 9], 4)` → `-1`
- `binary_search([], 1)` → `-1`
- `binary_search([42], 42)` → `0`

---

### Exercice 2 — Nombre d'étapes

Modifie ta fonction pour qu'elle retourne aussi le nombre de comparaisons effectuées.

```python
def binary_search_counted(lst: list[int], target: int) -> tuple[int, int]:
    # retourne (index, nombre_de_comparaisons)
    ...
```

Vérifie que tes résultats correspondent à ce que prédit O(log n).

---

### Exercice 3 — Première occurrence

Dans une liste triée avec des **doublons**, la recherche binaire classique peut retourner n'importe quelle occurrence de la valeur. Adapte la fonction pour retourner l'index de la **première** occurrence.

```python
def first_occurrence(lst: list[int], target: int) -> int:
    ...
```

Teste avec :
- `first_occurrence([1, 2, 2, 2, 3], 2)` → `1`
- `first_occurrence([1, 1, 1, 1], 1)` → `0`

---

### Exercice 4 — Insertion position

Étant donné une liste triée et une valeur, retourne l'index auquel la valeur **devrait être insérée** pour que la liste reste triée (même si la valeur est déjà présente).

```python
def search_insert(lst: list[int], target: int) -> int:
    ...
```

Teste avec :
- `search_insert([1, 3, 5, 6], 5)` → `2`
- `search_insert([1, 3, 5, 6], 2)` → `1`
- `search_insert([1, 3, 5, 6], 7)` → `4`
- `search_insert([1, 3, 5, 6], 0)` → `0`

---

### Exercice 5 — Version récursive

Réimplémente la recherche binaire de manière **récursive**. Réfléchis à comment définir le cas de base et le cas récursif.

```python
def binary_search_recursive(lst: list[int], target: int, low: int, high: int) -> int:
    ...
```

---

### Exercice 6 — Recherche dans une matrice triée

Une matrice `m x n` est organisée ainsi :
- Chaque ligne est triée de gauche à droite.
- Le premier élément de chaque ligne est supérieur au dernier élément de la ligne précédente.

Détermine si une valeur cible est présente dans la matrice. Complexité cible : O(log(m×n)).

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    ...
```

Teste avec :
```
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
search_matrix(matrix, 3)   # True
search_matrix(matrix, 13)  # False
```

---

## Pour aller plus loin

- Comment se comporte la recherche binaire sur une liste d'un seul élément ? Sur une liste vide ?
- Que se passe-t-il si la liste n'est pas triée ? Est-ce que l'algorithme échoue toujours, ou peut-il parfois retourner le bon résultat par hasard ?
- En Python, le module `bisect` de la bibliothèque standard implémente une recherche binaire. Explore `bisect_left` et `bisect_right`.

---

## Récursion

Une fonction récursive se définit en termes d'elle-même. Elle doit toujours avoir :

1. Un **cas de base** — condition d'arrêt, retourne un résultat direct.
2. Un **cas récursif** — appel sur une entrée strictement plus petite.

### Exemples du dossier

**Factorielle** — `n! = n × (n−1)!`

```python
def factorial(n: int) -> int:
    if n == 0:            # cas de base
        return 1
    return n * factorial(n - 1)   # cas récursif
```

**PGCD** — algorithme d'Euclide (diviser pour régner)

```python
def pgcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return pgcd(b, a % b)
```

**Maximum récursif** — diviser pour régner sur une liste

```python
def recursive_max(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]
    sub_max = recursive_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max
```

### Récursion vs itération

| Critère    | Récursion                                  | Itération                |
|------------|--------------------------------------------|--------------------------|
| Lisibilité | Proche de la définition mathématique       | Plus verbeux mais explicite |
| Mémoire    | Empile des appels (risque `RecursionError`) | Mémoire constante        |
| Performance| Surcoût des appels de fonction             | Généralement plus rapide |

La pile Python est limitée à ~1 000 niveaux par défaut (`sys.getrecursionlimit()`).

---

## Parcours en largeur (BFS)

Explorer un **graphe** (ou un arbre) niveau par niveau — tous les voisins directs avant d'aller plus loin.

### Structure de données

BFS utilise une **file** (*queue*) FIFO : on enfile les voisins à découvrir et on les défile dans l'ordre d'arrivée.

```python
from collections import deque

def bfs(graph: dict, start):
    visited = set()
    queue   = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()            # défile
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)    # enfile
```

### Cas d'usage

- Plus court chemin dans un graphe **non pondéré**.
- Vérifier si deux nœuds sont **connectés**.
- Explorer un arbre de façon exhaustive.

### Complexité

O(V + E) — V sommets, E arêtes.

---

## Tri par sélection

Trouver le minimum de la partie non triée et le placer en tête, répéter.

- Complexité : **O(n²)** dans tous les cas.
- Simple mais inefficace sur les grandes listes.

```python
def selection_sort(lst: list) -> list:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
```

---

## Tri rapide (Quick Sort)

Choisir un **pivot**, placer les éléments inférieurs à gauche et supérieurs à droite, puis trier récursivement chaque côté.

- Complexité moyenne : **O(n log n)**.
- Pire cas (pivot toujours min ou max) : O(n²) → atténué par un pivot **aléatoire**.

```python
import random

def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    pivot  = random.choice(lst)
    left   = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right  = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

## Récapitulatif des complexités

| Algorithme          | Meilleur cas | Cas moyen  | Pire cas   |
|---------------------|:------------:|:----------:|:----------:|
| Recherche linéaire  | O(1)         | O(n)       | O(n)       |
| Recherche binaire   | O(1)         | O(log n)   | O(log n)   |
| BFS                 | O(1)         | O(V + E)   | O(V + E)   |
| Tri par sélection   | O(n²)        | O(n²)      | O(n²)      |
| Tri rapide          | O(n log n)   | O(n log n) | O(n²)      |
