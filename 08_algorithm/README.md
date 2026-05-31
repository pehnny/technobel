# Algorithmes

---

## Récursion

Une fonction récursive se définit en termes d'elle-même. Elle doit toujours avoir :

1. Un **cas de base** — condition d'arrêt, retourne un résultat direct.
2. Un **cas récursif** — appel sur une entrée strictement plus petite.

### Récursion vs itération

| Critère    | Récursion                                  | Itération                |
|------------|--------------------------------------------|--------------------------|
| Lisibilité | Proche de la définition mathématique       | Plus verbeux mais explicite |
| Mémoire    | Empile des appels (risque `RecursionError`) | Mémoire constante        |
| Performance| Surcoût des appels de fonction             | Généralement plus rapide |

La pile Python est limitée à ~1 000 niveaux par défaut (`sys.getrecursionlimit()`).

### Exercices du dossier

#### Somme récursive — `recursive_sum`

Calculer la somme des éléments d'une liste sans `sum()` ni boucle. Le cas de base est une liste d'un seul élément (retourner cet élément). Le cas récursif additionne le dernier élément au résultat sur le reste.

```python
recursive_sum([1, 2, 3, 4])  # → 10
```

[08_algorithm/recursion/recursive_sum.py](recursion/recursive_sum.py)

---

#### Compte récursif — `recursive_count`

Compter les éléments d'une liste sans `len()`. Cas de base : liste vide → 0. Cas récursif : `1 + count(liste sans dernier élément)`.

```python
recursive_count([1, 2, 3])  # → 3
```

[08_algorithm/recursion/recursive_count.py](recursion/recursive_count.py)

---

#### Maximum récursif — `recursive_max`

Trouver le maximum d'une liste sans `max()`. Cas de base : liste d'un élément. Cas récursif : comparer le premier élément avec le maximum du reste.

```python
recursive_max([3, 1, 7, 2])  # → 7
```

[08_algorithm/recursion/recursive_max.py](recursion/recursive_max.py)

---

#### Factorielle — `factorial`

**n! = n × (n−1)!**, avec 0! = 1 comme cas de base.

```python
def factorial(n: int) -> int:
    if n in (0, 1):            # cas de base
        return 1
    return n * factorial(n-1)  # cas récursif
```

Trace pour `factorial(4)` :

```
factorial(4)
  → 4 * factorial(3)
       → 3 * factorial(2)
            → 2 * factorial(1)
                 → 1
```

La solution valide aussi le type et lève une `ValueError` pour les négatifs.

[08_algorithm/recursion/factorial.py](recursion/factorial.py)

---

#### PGCD — algorithme d'Euclide

Le PGCD de `a` et `b` est le plus grand entier qui divise les deux sans reste. L'algorithme d'Euclide repose sur la propriété : **PGCD(a, b) = PGCD(b, a mod b)**, avec pour cas de base **PGCD(a, 0) = a**.

```python
def pgcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return pgcd(b, a % b)
```

**Intuition géométrique** : chercher le plus grand carré qui pave exactement un rectangle de dimensions `(a × b)` — diviser pour régner.

[08_algorithm/recursion/pgcd.py](recursion/pgcd.py)

---

#### Recherche binaire récursive — `recursive_binary_search`

La même logique que la recherche binaire itérative (voir ci-dessous), exprimée par récursion. Chaque appel réduit le problème de moitié. Le paramètre `offset` conserve l'index réel dans le tableau d'origine malgré les slices successifs :

```python
recursive_binary_search(arr[mid+1:], value, offset + mid + 1)
```

[08_algorithm/recursion/recursive_binary_search.py](recursion/recursive_binary_search.py)

---

## Recherche binaire

Imagine que tu cherches un mot dans un dictionnaire. Tu ne commences pas à la première page — tu ouvres le livre à peu près au milieu, tu regardes où tu en es, et tu décides d'aller à gauche ou à droite. Tu répètes jusqu'à trouver le mot. C'est exactement ça, la **recherche binaire**.

La recherche binaire est un algorithme qui permet de retrouver un élément dans une **liste triée** en divisant l'espace de recherche par deux à chaque étape. Elle est l'un des algorithmes fondamentaux de l'informatique et sert de base à une grande partie des structures de données plus avancées.

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

### Exercices

#### Exercice 1 — Implémentation de base

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

#### Exercice 2 — Nombre d'étapes

Modifie ta fonction pour qu'elle retourne aussi le nombre de comparaisons effectuées.

```python
def binary_search_counted(lst: list[int], target: int) -> tuple[int, int]:
    # retourne (index, nombre_de_comparaisons)
    ...
```

Vérifie que tes résultats correspondent à ce que prédit O(log n).

---

#### Exercice 3 — Première occurrence

Dans une liste triée avec des **doublons**, la recherche binaire classique peut retourner n'importe quelle occurrence de la valeur. Adapte la fonction pour retourner l'index de la **première** occurrence.

```python
def first_occurrence(lst: list[int], target: int) -> int:
    ...
```

Teste avec :
- `first_occurrence([1, 2, 2, 2, 3], 2)` → `1`
- `first_occurrence([1, 1, 1, 1], 1)` → `0`

---

#### Exercice 4 — Insertion position

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

#### Exercice 5 — Version récursive

Réimplémente la recherche binaire de manière **récursive**. Réfléchis à comment définir le cas de base et le cas récursif.

```python
def binary_search_recursive(lst: list[int], target: int, low: int, high: int) -> int:
    ...
```

---

#### Exercice 6 — Recherche dans une matrice triée

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

### Pour aller plus loin

- Comment se comporte la recherche binaire sur une liste d'un seul élément ? Sur une liste vide ?
- Que se passe-t-il si la liste n'est pas triée ? Est-ce que l'algorithme échoue toujours, ou peut-il parfois retourner le bon résultat par hasard ?
- En Python, le module `bisect` de la bibliothèque standard implémente une recherche binaire. Explore `bisect_left` et `bisect_right`.

### Solution

[08_algorithm/searching/binary_search.py](searching/binary_search.py) — version itérative (générique avec `Protocol Comparable`)

[08_algorithm/recursion/recursive_binary_search.py](recursion/recursive_binary_search.py) — version récursive

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

La solution du dossier propose en plus un tri **décroissant** via un paramètre `ascending: bool`, en factorisant la recherche d'index (`_index_smallest` / `_index_greatest`) dans des fonctions auxiliaires préfixées `_` (convention : usage interne).

### Solution

[08_algorithm/sorting/selection_sort.py](sorting/selection_sort.py)

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

### Solution

[08_algorithm/sorting/quick_sort.py](sorting/quick_sort.py)

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

La solution du dossier implémente deux variantes : BFS sur un **graphe** (dict d'adjacence) avec une `condition: Callable` passée en paramètre, et BFS sur un **arbre** générique via un dataclass `Node[T]`.

### Solution

[08_algorithm/searching/breadth_first_search.py](searching/breadth_first_search.py)

---

## Algorithme de Dijkstra — Plus court chemin pondéré

### Le problème

On dispose d'une grille NxN où chaque case porte une altitude (0–9). On part de `[0][0]` et on cherche à atteindre `[N-1][N-1]` en se déplaçant uniquement dans les quatre directions cardinales. Le coût d'un déplacement entre deux cases adjacentes est la **différence absolue de leurs altitudes** (monter coûte autant que descendre). L'objectif : minimiser l'effort total.

### Pourquoi BFS ne suffit pas

BFS minimise le **nombre de déplacements**, pas leur coût. Sur une grille NxN, tous les chemins de départ à arrivée font exactement `2(N-1)` étapes — BFS les traite tous à égalité et ne peut pas choisir le moins coûteux.

Il faut un algorithme qui tient compte du **poids** de chaque déplacement.

### Principe : la relaxation de coût

On maintient, pour chaque case `[i][j]`, le coût minimal connu pour l'atteindre depuis le départ (`grid_cost`).

Au départ :
- `grid_cost[0][0] = 0`
- `grid_cost[i][j] = ∞` pour tout le reste

On explore les cases une par une. Depuis la case `[x][y]` atteinte avec un coût cumulé `c`, on calcule pour chaque voisin `[x'][y']` :

```
coût_nouveau = c + |altitude[x][y] - altitude[x'][y']|
```

Si `coût_nouveau < grid_cost[x'][y']`, on a trouvé un chemin moins cher : on met à jour et on remet le voisin dans la file d'exploration.

### Exemple sur une grille 3×3

Grille d'altitudes :

```
1  5  1
1  5  1
1  1  1
```

La colonne centrale forme une crête de montagne. Deux chemins naturels s'offrent :

| Chemin | Déplacements | Coût |
|---|---|:---:|
| Par le haut (→ → ↓ ↓) | `1→5→1→1→1` | 4+4+0+0 = **8** |
| Par le bas (↓ ↓ → →) | `1→1→1→1→1` | 0+0+0+0 = **0** |

Le chemin longeant le bas évite entièrement la crête. L'algorithme doit le découvrir.

**État initial de `grid_cost`** :

| | col 0 | col 1 | col 2 |
|---|:---:|:---:|:---:|
| **ligne 0** | **0** | ∞ | ∞ |
| **ligne 1** | ∞ | ∞ | ∞ |
| **ligne 2** | ∞ | ∞ | ∞ |

**Après exploration du flanc gauche** — les cases en altitude 1 sont atteintes sans effort, la crête est découverte au coût 4 :

| | col 0 | col 1 | col 2 |
|---|:---:|:---:|:---:|
| **ligne 0** | 0 | 4 | ∞ |
| **ligne 1** | 0 | 4 | ∞ |
| **ligne 2** | 0 | 0 | ∞ |

**État final** — les cases de droite sont atteintes depuis le bas sans coût supplémentaire (altitude constante à 1) :

| | col 0 | col 1 | col 2 |
|---|:---:|:---:|:---:|
| **ligne 0** | 0 | 4 | 0 |
| **ligne 1** | 0 | 4 | 0 |
| **ligne 2** | 0 | 0 | **0** |

La réponse est `grid_cost[2][2]` = **0**.

### L'implémentation

La solution utilise une **deque** comme pile (`pop()` extrait par la droite). Ce n'est pas un Dijkstra pur — celui-ci utiliserait un **tas min** (*priority queue*) pour toujours traiter le nœud au coût le plus faible en premier. Ici, l'algorithme s'apparente à une **relaxation exhaustive** :

- Une case peut être revisitée si un chemin moins cher est découvert plus tard.
- Il converge vers le bon résultat car chaque mise à jour ne peut qu'améliorer un coût (condition `coût_nouveau < grid_cost[voisin]` strictement).
- Plus simple à implémenter qu'un Dijkstra classique, mais moins efficace sur les grands graphes.

```
Dijkstra pur  →  tas min  →  toujours traiter le moins coûteux en premier
Cette solution →  deque   →  relaxation : corriger quand on trouve mieux
```

**Complexité** du Dijkstra classique : O((V + E) log V) avec un tas min.

### Optimisation avec `heapq` — le vrai Dijkstra

L'implémentation du dossier peut revisiter des cases inutilement. Le Dijkstra classique évite cela grâce à un **tas min** (*min-heap*) : à chaque étape, on extrait toujours la case au coût le plus faible, ce qui garantit qu'une fois sortie du tas, son coût est définitif.

#### Structure d'un tas min

Un tas min est un **arbre binaire complet** où chaque nœud est inférieur ou égal à ses enfants. La racine est donc toujours le minimum global.

```
        0           ← minimum garanti
       / \
      4   8
     / \ / \
    5  6 9  10
```

Python représente cet arbre dans une **liste ordinaire** via le module `heapq` — pas besoin d'une classe dédiée. Les indices suivent la règle :

| Nœud à l'index `i` | Enfant gauche | Enfant droit | Parent |
|:-------------------:|:-------------:|:------------:|:------:|
|                     | `2i + 1`      | `2i + 2`     | `(i-1) // 2` |

#### Les deux opérations fondamentales

```python
import heapq

heap = []
heapq.heappush(heap, (4, 1, 0))   # insère (coût, x, y) → O(log n)
heapq.heappush(heap, (0, 0, 0))   # remonte jusqu'à restaurer la propriété
heapq.heappush(heap, (8, 2, 1))

cost, x, y = heapq.heappop(heap)  # extrait le minimum → O(log n)
# → cost=0, x=0, y=0
```

Les tuples sont comparés **lexicographiquement** : `(0, 0, 0) < (4, 1, 0)` car `0 < 4`. Le coût placé en premier critère suffit à obtenir le bon ordre de priorité.

#### Dijkstra avec `heapq` appliqué au problème

```python
import heapq

def path_finder_dijkstra(area: str) -> int:
    grid = [[int(c) for c in row] for row in area.split("\n")]
    n = len(grid)
    grid_cost = [[float("inf")] * n for _ in range(n)]
    grid_cost[0][0] = 0
    heap = [(0, 0, 0)]                           # (coût, ligne, colonne)

    while heap:
        cost, x, y = heapq.heappop(heap)
        if cost > grid_cost[x][y]:               # entrée périmée → ignorer
            continue
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + abs(grid[x][y] - grid[nx][ny])
                if new_cost < grid_cost[nx][ny]:
                    grid_cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return int(grid_cost[-1][-1])
```

La garde `if cost > grid_cost[x][y]: continue` élimine les entrées périmées : quand un nœud est amélioré, l'ancienne entrée reste dans le tas mais est ignorée à l'extraction.

#### Comparaison des deux approches

| Version | Structure | Extraction | Revisites |
|---|:---:|:---:|:---:|
| Solution du dossier | deque (pile LIFO) | O(1) | Possibles |
| `heapq` (Dijkstra pur) | tas min | O(log V) | Aucune |

La version `heapq` fait plus de travail à chaque extraction, mais en élimine beaucoup plus — elle est donc **plus efficace dès que le graphe est grand**.

### Solution

[08_algorithm/searching/Dijkstra.py](searching/Dijkstra.py)

---

## Récapitulatif des complexités

| Algorithme          | Meilleur cas      | Cas moyen         | Pire cas          |
|---------------------|:-----------------:|:-----------------:|:-----------------:|
| Recherche linéaire  | O(1)              | O(n)              | O(n)              |
| Recherche binaire   | O(1)              | O(log n)          | O(log n)          |
| BFS                 | O(1)              | O(V + E)          | O(V + E)          |
| Dijkstra (tas min)  | O(V + E)          | O((V+E) log V)    | O((V+E) log V)    |
| Tri par sélection   | O(n²)             | O(n²)             | O(n²)             |
| Tri rapide          | O(n log n)        | O(n log n)        | O(n²)             |
