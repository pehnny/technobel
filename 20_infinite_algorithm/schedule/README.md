# Schedule — Plages de disponibilité

## Contexte

Un agenda est fourni pour une journée de travail. Il contient une liste d'activités, chacune définie par une heure de début et une heure de fin (des entiers représentant des heures). Les activités peuvent se **chevaucher** et ne sont **pas nécessairement dans l'ordre chronologique**.

Votre mission : **déterminer toutes les plages horaires où la personne est libre**.

---

## Signature attendue

```python
def find_free_slots(
    activities: list[tuple[int, int]],
    day_start: int = 8,
    day_end: int = 18
) -> list[tuple[int, int]]:
```

### Paramètres

| Paramètre   | Type                    | Description                                      |
|-------------|-------------------------|--------------------------------------------------|
| `activities` | `list[tuple[int, int]]` | Liste de tuples `(debut, fin)` représentant des heures entières |
| `day_start` | `int`                   | Début de la journée (défaut : 8)                |
| `day_end`   | `int`                   | Fin de la journée (défaut : 18)                 |

### Retour

Une liste de tuples `(debut, fin)` représentant les plages **libres**, triées dans l'ordre chronologique. La liste est vide si la journée est entièrement occupée.

---

## Exemple

```python
activities = [(9, 11), (10, 13), (15, 17)]
find_free_slots(activities, day_start=8, day_end=18)
# → [(8, 9), (13, 15), (17, 18)]
```

```
08:00   09:00   10:00   11:00   12:00   13:00   14:00   15:00   16:00   17:00   18:00
  |-------|=======|=======|=======|       |       |       |=======|=======|       |
  | libre |     activité A+B fusionnées   | libre |       |    activité C  | libre |
```

---

## Contraintes

- `0 <= day_start < day_end <= 24`
- `0 <= debut < fin <= 24` pour chaque activité
- Une activité peut déborder en dehors des bornes de la journée (elle doit être **rognée**)
- Le nombre d'activités `n` peut être grand — visez une solution en **O(n log n)**

---

## Points bonus

Ces extensions ne sont pas attendues dans le temps imparti (~1h), mais peuvent être abordées une fois les tests passés.

### Bonus 1 — Tri maison
Interdire l'utilisation de `sorted()` ou `.sort()`. Implémenter votre propre algorithme de tri. Commencez par un tri simple (selection sort, insertion sort), puis optimisez vers un **merge sort** ou **quick sort**.

### Bonus 2 — Plus long créneau libre
Ajouter une fonction `longest_free_slot` qui retourne la plage libre la plus longue (ou `None` si aucune).

```python
def longest_free_slot(activities, day_start=8, day_end=18) -> tuple[int, int] | None:
```

### Bonus 3 — Meilleur créneau pour une réunion
Étant donné une durée en heures, trouver le **premier créneau libre** suffisamment long.

```python
def find_meeting_slot(activities, duration, day_start=8, day_end=18) -> tuple[int, int] | None:
```

### Bonus 4 — Format horaire textuel
Faire fonctionner la solution avec des horaires au format `"HH:MM"` (chaînes de caractères) au lieu d'entiers.

```python
activities = [("09:00", "11:30"), ("10:45", "13:00")]
```

### Bonus 5 — Analyse de complexité
Expliquer la complexité temporelle et spatiale de votre solution finale. Peut-on faire mieux que O(n log n) ? Pourquoi (ou pourquoi pas) ?
