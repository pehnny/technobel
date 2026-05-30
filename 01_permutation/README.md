# Permutation

Échanger les valeurs de deux variables.

## Concepts abordés

- Assignation simple et assignation multiple
- Déballage de tuple (*tuple unpacking*)
- Échange sans variable temporaire

## À retenir

### Méthode classique — variable temporaire

```python
temp = a
a = b
b = temp
```

### Méthode Python — assignation multiple

```python
a, b = b, a
```

Python évalue entièrement le membre droit avant d'effectuer les affectations. Le membre droit `(b, a)` forme implicitement un tuple, puis est déballé dans `a` et `b` en une seule opération atomique.

### Assignation multiple générale

```python
x, y, z = 1, 2, 3
a, b, c = c, a, b   # rotation de trois variables
```

## Piège à éviter

```python
# Ne fonctionne PAS comme attendu en cas d'alias ou d'effets de bord
a = b
b = a   # b vaut déjà la nouvelle valeur de a !
```

Toujours utiliser la forme `a, b = b, a` pour un échange sûr.
