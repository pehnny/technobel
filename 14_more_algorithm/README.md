# Exercices Python - Algorithmique

## 1. Reverse String

Écrire une fonction qui prend une chaîne de caractères en paramètre et retourne cette chaîne inversée.

### Exemple

```python
reverse_string("hello")
```

Résultat attendu :

```python
"olleh"
```

---

## 2. Count Vowels

Écrire une fonction qui compte le nombre de voyelles présentes dans une chaîne de caractères.

Les voyelles sont :

```python
a, e, i, o, u, y
```

### Exemple

```python
count_vowels("bonjour")
```

Résultat attendu :

```python
3
```

---

## 3. Palindrome

Écrire une fonction qui vérifie si une chaîne de caractères est un palindrome.

Un palindrome se lit de la même manière dans les deux sens.

### Exemples

```python
is_palindrome("radar")
```

Résultat attendu :

```python
True
```

```python
is_palindrome("python")
```

Résultat attendu :

```python
False
```

---

## 4. Find Max

Écrire une fonction qui retourne la plus grande valeur d'une liste d'entiers.

### Exemple

```python
find_max([3, 8, 2, 15, 4])
```

Résultat attendu :

```python
15
```

### Contraintes

Ne pas utiliser :

```python
max()
```

---

## 5. Count Occurrences

Écrire une fonction qui compte combien de fois une valeur apparaît dans une liste.

### Exemple

```python
count_occurrences([1, 2, 3, 2, 2, 4], 2)
```

Résultat attendu :

```python
3
```

### Contraintes

Ne pas utiliser :

```python
count()
```

---

## 6. FizzBuzz

Afficher les nombres de 1 à 100.

Règles :

* Si le nombre est divisible par 3, afficher `Fizz`
* Si le nombre est divisible par 5, afficher `Buzz`
* Si le nombre est divisible par 3 et 5, afficher `FizzBuzz`
* Sinon afficher le nombre

### Exemple

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
```
---

## 8. Valid Parentheses

Écrire une fonction qui vérifie si une chaîne contenant des parenthèses, crochets et accolades est valide.

Une chaîne est valide si chaque symbole ouvrant est fermé par le bon symbole dans le bon ordre.

### Exemples

```text

valid_parentheses("()[]{}")

Résultat attendu :

True

valid_parentheses("([)]")

Résultat attendu :

False

valid_parentheses("{[]}")

Résultat attendu :

True
```

---

## 9. Find Duplicates

Écrire une fonction qui retourne les éléments qui apparaissent plus d'une fois dans une liste.

### Exemple

```text
find_duplicates([1, 2, 3, 2, 5, 1])

Résultat attendu :

[1, 2]
```

### Contraintes

Chaque doublon ne doit apparaître qu'une seule fois dans le résultat.

---

## 10. Longest Word

Écrire une fonction qui retourne le mot le plus long dans une phrase.

### Exemple

```text

longest_word("bonjour je suis davit")

Résultat attendu :

"bonjour"

```

### Bonus

Si plusieurs mots ont la même longueur maximale, retourner le premier trouvé.


## 7. Two Sum (Bonus)

Écrire une fonction qui reçoit :

* une liste d'entiers
* une valeur cible

La fonction doit retourner les indices des deux nombres dont la somme est égale à la cible.

### Exemple

```python
two_sum([2, 7, 11, 15], 9)
```

Résultat attendu :

```python
(0, 1)
```

Car :

```python
2 + 7 = 9
```

### Bonus

Essayer de résoudre le problème sans utiliser deux boucles imbriquées.
