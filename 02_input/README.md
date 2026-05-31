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

### Exercice 1 — Séparateur personnalisé

Demandez le nom de famille puis le prénom à l'utilisateur, et affichez-les séparés par `*-*` en utilisant le paramètre `sep` de `print()`.

```
Bonjour *-* Dupont Alice
```

### Exercice 2 — Message long avec séparateur et fin de ligne custom

Affichez une phrase dont chaque mot est un argument séparé de `print()`, avec `sep="$$\t"` (tabulation précédée de `$$`) et `end="$$\n"` comme terminateur.

### Exercice 3 — Concaténation sans espace

Demandez deux mots à l'utilisateur et affichez-les **collés** l'un à l'autre, sans aucun espace, en utilisant une f-string `f"{premier}{second}"`.

### Exercice 4 — Addition de deux nombres saisis

Lisez deux valeurs numériques au clavier. Attention : `input()` renvoie toujours un `str` — il faut convertir avant d'additionner. Affichez la somme avec `end="$$\n"`.

```python
# Attention aux cas limites : que faire si l'utilisateur saisit du texte ?
```

### Exercice 5 — Affichage multi-valeurs custom

Affichez trois chaînes avec `sep="xXx"` et `end="**"`, sans saut de ligne final.

```
big brother xXx is watching xXx you**
```

---

### Solution

[02_input/main.py](main.py)
