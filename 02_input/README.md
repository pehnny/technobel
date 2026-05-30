# Entrées / Sorties

Lire des données au clavier et afficher des résultats avec mise en forme.

## Concepts abordés

- `input()` — lecture au clavier
- `print()` — affichage avec `sep` et `end`
- Conversion de types (`int()`, `float()`, `str()`)
- f-strings

## À retenir

### `input()`

`input()` retourne toujours une **chaîne de caractères** (`str`), peu importe ce que l'utilisateur tape.

```python
name = input("Votre prénom : ")   # name est un str
age  = int(input("Votre âge : ")) # conversion explicite en int
```

### `print()` — paramètres `sep` et `end`

| Paramètre | Valeur par défaut | Rôle |
|-----------|:-----------------:|------|
| `sep`     | `" "` (espace)    | Séparateur entre les arguments |
| `end`     | `"\n"` (saut de ligne) | Caractère(s) après le dernier argument |

```python
print("Alice", "Bob", "Charlie")              # Alice Bob Charlie
print("Alice", "Bob", "Charlie", sep=", ")   # Alice, Bob, Charlie
print("Chargement", end="")                   # pas de saut de ligne
print("... OK")                               # Chargement... OK
```

### f-strings

```python
prenom = "Alice"
age = 30
print(f"Bonjour {prenom}, tu as {age} ans.")
# Bonjour Alice, tu as 30 ans.
```

### Conversion de type

```python
n = int("42")       # str → int
x = float("3.14")   # str → float
s = str(100)        # int → str
```

## Exercices du dossier

1. Afficher prénom et nom avec un séparateur personnalisé.
2. Afficher un message multi-lignes avec fin de ligne custom.
3. Concaténer deux mots sans espace entre eux.
4. Additionner deux nombres saisis au clavier.
5. Afficher trois valeurs avec séparateur et fin de ligne personnalisés.
