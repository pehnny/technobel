# Finite State Machine

## BinaryFSM — divisibilité d'un nombre binaire

`BinaryFSM` est un automate fini déterministe (AFD) qui lit une chaîne binaire bit par bit et détermine si le nombre qu'elle représente est divisible par un entier arbitraire `n`.

L'automate possède `n` états, numérotés de `0` à `n-1`, chacun représentant un **reste possible** de la division euclidienne par `n`. L'état initial et l'unique état acceptant est `0`.

### Schéma — machine modulo 5

![Schéma de la machine modulo 5](scheme.png)

Les 5 états correspondent aux restes `0, 1, 2, 3, 4`. L'état `0` (double cercle) est l'état acceptant : la machine s'y trouve à la fin de la lecture si et seulement si le nombre est divisible par 5.

### Table de transitions — modulo 5

| État courant | bit lu | État suivant | Calcul            |
|:------------:|:------:|:------------:|:-----------------:|
| 0            | 0      | 0            | (2×0 + 0) % 5 = 0 |
| 0            | 1      | 1            | (2×0 + 1) % 5 = 1 |
| 1            | 0      | 2            | (2×1 + 0) % 5 = 2 |
| 1            | 1      | 3            | (2×1 + 1) % 5 = 3 |
| 2            | 0      | 4            | (2×2 + 0) % 5 = 4 |
| 2            | 1      | 0            | (2×2 + 1) % 5 = 0 |
| 3            | 0      | 1            | (2×3 + 0) % 5 = 1 |
| 3            | 1      | 2            | (2×3 + 1) % 5 = 2 |
| 4            | 0      | 3            | (2×4 + 0) % 5 = 3 |
| 4            | 1      | 4            | (2×4 + 1) % 5 = 4 |

### Exemple — `1010`₂ = 10 = 2 × 5

| Étape | Bit lu | État avant | Calcul             | État après |
|:-----:|:------:|:----------:|:------------------:|:----------:|
| 1     | `1`    | 0          | (2×0 + 1) % 5 = 1 | 1          |
| 2     | `0`    | 1          | (2×1 + 0) % 5 = 2 | 2          |
| 3     | `1`    | 2          | (2×2 + 1) % 5 = 0 | 0          |
| 4     | `0`    | 0          | (2×0 + 0) % 5 = 0 | **0** ✓   |

L'automate termine en état `0` → 10 est bien divisible par 5.

### Formule de transition

À chaque étape, la machine applique :

```
état_suivant = (2 × état_courant + bit) % n
```

**Pourquoi ça fonctionne ?**  
Lire un nombre binaire de gauche à droite revient à construire sa valeur `v` de manière itérative : à chaque nouveau bit `b`, on a `v_nouveau = 2 × v_ancien + b`. Or la propriété de congruence garantit que :

```
(2v + b) mod n  =  (2(v mod n) + b) mod n
```

Le reste de `v_nouveau` ne dépend donc que du reste de `v_ancien`, jamais de la valeur entière accumulée. L'état courant encode ainsi exactement le reste modulo `n` du préfixe déjà lu, ce qui permet de travailler sur des nombres de taille arbitraire avec une mémoire constante (`n` états).
