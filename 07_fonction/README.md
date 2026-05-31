# Fonctions

Encapsuler un traitement réutilisable dans un bloc nommé.

## Concepts abordés

- Déclaration et appel de fonction
- Paramètres positionnels et par défaut
- Type hints (annotations de type)
- Valeurs de retour multiples
- List comprehension
- Portée des variables (*scope*)

## À retenir

### Déclaration

```python
def nom_fonction(param1, param2):
    # corps
    return resultat
```

### Type hints (Python 3.5+)

Annotations de type documentant les paramètres et le retour. Ignorées à l'exécution mais utiles pour la lisibilité et les outils d'analyse statique.

```python
def aire_cercle(rayon: float) -> float:
    import math
    return math.pi * rayon ** 2
```

### Paramètres par défaut

```python
def creer_compte(nom: str, role: str = "utilisateur") -> str:
    return f"{nom} ({role})"

creer_compte("Alice")            # "Alice (utilisateur)"
creer_compte("Bob", "admin")     # "Bob (admin)"
```

Les paramètres avec valeur par défaut doivent toujours être **après** les paramètres sans valeur par défaut.

### Retour de plusieurs valeurs (tuple)

```python
def min_max(lst: list[int]) -> tuple[int, int]:
    return min(lst), max(lst)

petit, grand = min_max([4, 1, 9, 2])   # petit=1, grand=9
```

### List comprehension

```python
# Forme générale
[expression for element in iterable if condition]

# Exemples
carres  = [x**2 for x in range(10)]
majusc  = [c.upper() for c in "hello"]
filtres = [x for x in range(20) if x % 3 == 0]
```

### Portée des variables

```python
x = 10   # variable globale

def f():
    x = 20   # variable locale, ne modifie pas la globale
    print(x) # 20

f()
print(x)     # 10
```

Pour modifier une variable globale depuis une fonction, déclarer `global x` — à éviter en pratique.

## Exercices du dossier

### Exercice 1 — `calcul_moyenne(numbers: list[float]) -> float`

Calculez la moyenne d'une liste de flottants. Gérez le cas limite de la liste vide en retournant `0` plutôt qu'une division par zéro.

```python
calcul_moyenne([1, 2, 3, 4, 5])  # → 3.0
calcul_moyenne([])               # → 0
```

### Exercice 2 — `recherche_min(numbers: list[float]) -> float`

Trouvez le minimum d'une liste **sans utiliser `min()`**. Initialisez avec le premier élément, puis parcourez et comparez.

```python
recherche_min([5, 3, 1, -1])  # → -1
```

### Exercice 3 — `generer_email(prenom, nom, domaine="gmail.com") -> str`

Générez une adresse e-mail au format `prenom.nom@domaine` avec un domaine par défaut. Illustre les **paramètres par défaut** : le paramètre avec valeur doit être en dernier.

```python
generer_email("Friedrich", "Hegel")              # → "Friedrich.Hegel@gmail.com"
generer_email("Karl", "Marx", "proton.me")        # → "Karl.Marx@proton.me"
```

### Exercice 4 — `compte_mots(text: str) -> int`

Comptez le nombre de mots dans une chaîne en utilisant `str.split()` (qui découpe sur les espaces et ignore les espaces multiples).

```python
compte_mots("Bonjour le monde")  # → 3
```

### Exercice 5 — `convertir_temperature(celsius: float) -> float`

Convertissez une température en Celsius en Fahrenheit avec la formule `F = 32 + (9/5) × C`.

```python
convertir_temperature(0)    # → 32.0
convertir_temperature(100)  # → 212.0
```

### Exercice 6 — `nombres_pairs_impairs(nombres: list[int]) -> tuple[list[int], list[int]]`

Séparez une liste d'entiers en deux sous-listes (pairs, impairs) en utilisant des **list comprehensions**. Retournez les deux listes dans un tuple.

```python
nombres_pairs_impairs([1, 2, 3, 4, 5, 6])  # → ([2, 4, 6], [1, 3, 5])
```

### Exercice 7 — `reverse(text: str) -> str`

Inversez une chaîne de caractères en une seule expression grâce au **slicing** `[::-1]` (step = -1 = parcours de droite à gauche).

```python
reverse("bonjour")  # → "ruojnob"
```

### Exercice 8 — `valider_mot_de_passe(text: str) -> bool`

Validez un mot de passe selon quatre critères : longueur ≥ 8, au moins une minuscule, une majuscule, un chiffre, un caractère spécial. Utilisez des flags booléens mis à jour dans une boucle `for`.

```python
valider_mot_de_passe("Techn0b€l")  # → True
valider_mot_de_passe("faible")     # → False
```

---

### Solution

[07_fonction/main.py](main.py)
