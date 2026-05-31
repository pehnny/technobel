# POO Avancée — Heroes VS Monsters

Bienvenue dans la forêt de **Shorewood**, forêt enchantée du pays de **Stormwall**.  
Ce projet met en pratique tous les concepts orientés objets vus au cours au travers d'un jeu de rôle en console.

---

## Énoncé

### Personnages

Chaque personnage possède trois caractéristiques :

| Caractéristique | Abrév. | Calcul |
|-----------------|:------:|--------|
| Endurance       | End    | 3 meilleurs lancers parmi 4 dés à 6 faces |
| Force           | For    | 3 meilleurs lancers parmi 4 dés à 6 faces |
| Points de vie   | PV     | Endurance + modificateur(Endurance) |

**Modificateur** — transforme une caractéristique en bonus/malus :

| Valeur de la caractéristique | Modificateur |
|:----------------------------:|:------------:|
| < 5                          | −1           |
| 5 à 9                        | 0            |
| 10 à 14                      | +1           |
| ≥ 15                         | +2           |

**Frappe** — les dégâts sont calculés ainsi : `d4 + modificateur(Force)`. Ces dégâts sont soustraits aux PV de la cible. Un personnage meurt quand ses PV ≤ 0.

### Héros

| Classe   | Symbole | Bonus racial        |
|----------|:-------:|---------------------|
| Humain   | `H`     | +1 Endurance, +1 Force |
| Nain     | `H`     | +2 Endurance        |

Après chaque combat, le héros **se repose** (PV restaurés à leur maximum) et **dépouille** le monstre vaincu (récupère or et/ou cuir).

### Monstres

| Classe    | Symbole | Bonus racial  | Or        | Cuir     |
|-----------|:-------:|:-------------:|:---------:|:--------:|
| Loup      | `W`     | —             | 0         | d4       |
| Orque     | `O`     | +1 Force      | d4        | 0        |
| Dragonnet | `D`     | +1 Endurance  | d4        | d4       |

*L'or et le cuir sont tirés à la création du monstre (d6 et d4 respectivement pour les valeurs de l'énoncé).*

### Zone de jeu (exercice supplémentaire)

- Grille **15 × 15**.
- **10 monstres** placés aléatoirement, espacés d'au moins 2 cases entre eux.
- Les monstres sont **cachés** jusqu'au déclenchement du combat.
- Le combat se déclenche automatiquement quand le héros se place à **côté** (horizontalement ou verticalement) d'un monstre.
- Le jeu s'arrête quand le héros meurt ou quand tous les monstres sont vaincus.

---

## Concepts OOP illustrés

### Hiérarchie de classes

```
Character (ABC)
  ├─ Hero (interface ABC)
  │   ├─ Human(Character, Hero)
  │   └─ Dwarf(Character, Hero)
  └─ Monster (interface ABC)
      ├─ Wolf(Character, Monster)
      ├─ Orc(Character, Monster)
      └─ Dragon(Character, Monster)
```

### Classes abstraites (`ABC`)

Une classe abstraite ne peut pas être instanciée directement. Elle impose un contrat via `@abstractmethod` que toutes ses sous-classes doivent respecter.

```python
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def hit(self) -> int: ...   # chaque personnage DOIT implémenter hit()
```

### Héritage multiple

Python permet d'hériter de plusieurs classes. L'ordre de résolution (MRO) va de gauche à droite puis remonte vers la base.

```python
class Human(Character, Hero):   # hérite de Character ET de Hero
    ...
```

### Interfaces (simulation)

Une classe abstraite ne contenant que des méthodes abstraites joue le rôle d'interface — elle définit un **comportement** sans l'implémenter.

```python
class Hero(ABC):
    @abstractmethod
    def loot(self, target: Character) -> None: ...
    @abstractmethod
    def rest(self) -> None: ...
```

### Énumérations (`Enum`)

Ensemble fini de valeurs nommées, utile pour les types de monstres ou de héros.

```python
from enum import Enum

class MonsterClass(Enum):
    WOLF   = 0
    ORC    = 1
    DRAGON = 2
```

### Exceptions personnalisées

Des erreurs métier précises, organisées en hiérarchie.

```python
class ChunkError(BaseException): pass
class OccupiedError(ChunkError): pass   # hérite de ChunkError
```

### Méthode statique

Appartient à la classe, pas à une instance — ne reçoit ni `self` ni `cls`.

```python
@staticmethod
def modifier(stat: int) -> int:
    if stat < 5:  return -1
    if stat < 10: return  0
    if stat < 15: return +1
    return +2
```

---

## Architecture du projet

```
10_HeroesVSMonsters/
├─ characters/
│   ├─ metaclass/character.py   ← classe de base abstraite
│   ├─ interfaces/
│   │   ├─ hero.py              ← interface Hero
│   │   └─ monster.py           ← interface Monster
│   ├─ enum/
│   │   ├─ hero.py              ← HeroClass (HUMAN, DWARF)
│   │   └─ monster.py           ← MonsterClass (WOLF, ORC, DRAGON)
│   ├─ human.py / dwarf.py      ← implémentations héros
│   ├─ wolf.py / orc.py / dragon.py  ← implémentations monstres
├─ dices/dice.py                ← classe Dice (roll, n_roll, n_best_roll)
├─ errors/errors.py             ← exceptions personnalisées
├─ world/
│   ├─ chunk.py                 ← case de la grille
│   └─ world.py                 ← grille, placement, déplacement
├─ game/game.py                 ← logique de jeu (à compléter)
└─ main.py                      ← point d'entrée (à compléter)
```

---

## État d'avancement

### Implémenté ✓

- Classe `Dice` avec `roll()`, `n_roll()`, `n_best_roll()`
- `Character` (classe abstraite de base)
- `Hero` et `Monster` (interfaces)
- `Human`, `Dwarf`, `Wolf`, `Orc`, `Dragon` avec stats, bonus raciaux, `hit()`, `loot()`, `rest()`
- `Chunk` (case de la grille) et `World` (grille 15×15, placement des monstres et du héros, déplacement)
- Exceptions `OccupiedError`, `MonsterClassError`, etc.
- Énumérations `HeroClass` et `MonsterClass`

### À compléter

- **`game/game.py`** — logique de jeu :
  - Affichage de la grille en console (héros visible, monstres cachés)
  - Boucle principale : lire une direction, déplacer le héros
  - Détection de l'adjacence → déclenchement du combat
  - Boucle de combat (tours alternés héros / monstre)
  - Suppression du monstre mort de la grille
  - Conditions de fin de partie (héros mort ou plus de monstres)
- **`main.py`** — choix du type de héros, création du monde, lancement de la partie

---

## Lancer le jeu

[10_HeroesVSMonsters/main.py](main.py)

Le `main.py` est le point d'entrée du jeu. Dans son état actuel il est vide (`pass`) car la logique de jeu (`game/game.py`) reste à compléter (voir "À compléter" ci-dessus). Une fois finalisé, il devra : demander à l'utilisateur de choisir son type de héros (Humain ou Nain), instancier le monde, et lancer la boucle principale via `Game`.
