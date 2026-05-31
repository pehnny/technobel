# Parseur HTML

Valider une chaîne de balises HTML à l'aide d'une pile, sans regex.

## Concepts abordés

- Pile (*stack*) LIFO — `list` Python avec `append` / `pop`
- `set` pour un test d'appartenance O(1)
- Slicing pour extraire le contenu d'une balise
- Trois valeurs de retour distinctes (`True`, `False`, `str`)

## À retenir

### La pile — structure clé

Une pile LIFO (Last In, First Out) est la structure naturelle pour valider des balises HTML : la **dernière balise ouverte** doit toujours être la **première fermée**.

```
<p><b><i>...</i></b></p>
 ↑                     ↑ fermée en dernier
 └─── fermée en premier (LIFO)
```

En Python, une `list` ordinaire suffit : `append` empile, `pop` dépile par le haut.

### Extraire le contenu d'une balise

Plutôt que d'enchaîner des `lstrip` / `rstrip`, on sait que chaque balise est délimitée par `<` et `>` : un simple slice suffit.

```python
value = tag[1:-1]          # "<div>"  → "div"   |  "</div>" → "/div"
is_closing = value[0] == "/"
value = value.lstrip("/")  # "/div"  → "div"    |  "div"   → "div"
```

`lstrip("/")` est ici légitime : il n'y a qu'un seul `/` à retirer, et l'on vient de vérifier qu'il existe.

### Accumuler les balises sans O(n²)

La concaténation `tag += c` recopie la chaîne entière à chaque itération. La version correcte accumule les caractères dans une `list` et joint en une seule passe :

```python
chars: list[str] = []
for c in text:
    chars.append(c)
    if c == ">":
        tags.append("".join(chars))
        chars = []
```

### Balises supportées

`p`, `b`, `i`, `a`, `div` — stockées dans un `set` pour un test `in` en O(1). Balises à contenu uniquement (pas de balises orphelines comme `<br>` ou `<img>`).

### Algorithme

1. Parcourir la chaîne caractère par caractère ; accumuler dans `chars` jusqu'au `>`, puis enregistrer la balise.
2. Pour chaque balise : extraire le nom avec `tag[1:-1]` et détecter si elle est fermante (`value[0] == "/"`).
3. **Ouvrante** → empiler le nom.
4. **Fermante** :
   - Pile vide → **`False`** (cas 3).
   - Sommet = nom → dépiler (correct).
   - Sommet ≠ nom → **retourner le sommet** (cas 2).
5. Fin de chaîne : `not stack` → **`True`** si tout est fermé, **`False`** sinon (cas 3).

---

## Exercice du dossier

### Énoncé

Écrivez `parser(text: str) -> bool | str` qui reçoit une chaîne de balises HTML et retourne :

| Cas | Exemple | Retour |
|---|---|:---:|
| **1** — Chaîne valide | `<p><b></b></p>` | `True` |
| **2** — Mauvaise fermeture | `<p><b></p>` | `"b"` |
| **3** — Balise jamais fermée ou fermante orpheline | `<p>` · `<p></p></b>` | `False` |

**Contraintes :**
- Pas de regex.
- Balises limitées à : `p`, `b`, `i`, `a`, `div`.
- Pas d'attributs, pas de balises orphelines.
- Le texte entre les balises est supposé déjà nettoyé.

---

### Traces d'exécution

#### Cas 1 — Chaîne valide

Entrée : `"<p><b></b></p>"`

| Étape | Balise | `is_closing` | Pile avant   | Action              | Pile après   |
|:-----:|:------:|:------------:|:------------:|:-------------------:|:------------:|
| 1     | `<p>`  | `False`      | `[]`         | empile `"p"`        | `["p"]`      |
| 2     | `<b>`  | `False`      | `["p"]`      | empile `"b"`        | `["p", "b"]` |
| 3     | `</b>` | `True`       | `["p", "b"]` | sommet `"b"` = `"b"` → dépile | `["p"]` |
| 4     | `</p>` | `True`       | `["p"]`      | sommet `"p"` = `"p"` → dépile | `[]`    |

Fin : `not stack` = `not []` = **`True`**

---

#### Cas 2 — Mauvaise fermeture

Entrée : `"<p><b></p>"`

| Étape | Balise | `is_closing` | Pile avant   | Action |
|:-----:|:------:|:------------:|:------------:|:------:|
| 1     | `<p>`  | `False`      | `[]`         | empile `"p"` → `["p"]` |
| 2     | `<b>`  | `False`      | `["p"]`      | empile `"b"` → `["p", "b"]` |
| 3     | `</p>` | `True`       | `["p", "b"]` | sommet `"b"` ≠ `"p"` → **return `"b"`** |

Résultat : **`"b"`** — `b` était au sommet de la pile quand la mauvaise fermante `</p>` est arrivée.

---

#### Cas 3a — Fermante orpheline (pile vide)

Entrée : `"<p></p></b>"`

| Étape | Balise | `is_closing` | Pile avant | Action |
|:-----:|:------:|:------------:|:----------:|:------:|
| 1     | `<p>`  | `False`      | `[]`       | empile `"p"` → `["p"]` |
| 2     | `</p>` | `True`       | `["p"]`    | sommet `"p"` = `"p"` → dépile → `[]` |
| 3     | `</b>` | `True`       | `[]`       | pile vide → **return `False`** |

---

#### Cas 3b — Balise jamais fermée

Entrée : `"<p><b></b>"`

| Étape | Balise | `is_closing` | Pile avant   | Action |
|:-----:|:------:|:------------:|:------------:|:------:|
| 1     | `<p>`  | `False`      | `[]`         | empile `"p"` → `["p"]` |
| 2     | `<b>`  | `False`      | `["p"]`      | empile `"b"` → `["p", "b"]` |
| 3     | `</b>` | `True`       | `["p", "b"]` | sommet `"b"` = `"b"` → dépile → `["p"]` |

Fin : `not stack` = `not ["p"]` = **`False`** — `p` n'a jamais été fermée.

---

### Solution

[12_HTMLParser/parser.py](parser.py)

### Tests

[12_HTMLParser/unite_test.py](unite_test.py)
