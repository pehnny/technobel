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
def calcul_moyenne(notes: list[float]) -> float:
    if not notes:
        return 0.0
    return sum(notes) / len(notes)
```

### Paramètres par défaut

```python
def generer_email(prenom: str, nom: str, domaine: str = "gmail.com") -> str:
    return f"{prenom.lower()}.{nom.lower()}@{domaine}"

generer_email("alice", "dupont")               # alice.dupont@gmail.com
generer_email("bob", "martin", "outlook.com")  # bob.martin@outlook.com
```

Les paramètres avec valeur par défaut doivent toujours être **après** les paramètres sans valeur par défaut.

### Retour de plusieurs valeurs (tuple)

```python
def nombres_pairs_impairs(lst: list[int]) -> tuple[list[int], list[int]]:
    pairs   = [x for x in lst if x % 2 == 0]
    impairs = [x for x in lst if x % 2 != 0]
    return pairs, impairs

p, i = nombres_pairs_impairs([1, 2, 3, 4, 5])
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

## Fonctions du dossier

| Fonction                    | Ce qu'elle illustre                              |
|-----------------------------|--------------------------------------------------|
| `calcul_moyenne()`          | Type hints, gestion cas limite (liste vide)      |
| `recherche_min()`           | Itération manuelle sans fonction native          |
| `generer_email()`           | Paramètre par défaut, formatage de chaîne        |
| `compte_mots()`             | `str.split()`                                    |
| `convertir_temperature()`   | Formule mathématique simple                      |
| `nombres_pairs_impairs()`   | List comprehension, retour de tuple              |
| `reverse()`                 | Slicing `[::-1]`                                 |
| `valider_mot_de_passe()`    | Validation multi-critères, `any()`, `all()`      |
