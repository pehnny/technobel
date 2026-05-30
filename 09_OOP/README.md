# Programmation Orientée Objet

Modéliser le monde réel avec des classes, des objets et la composition.

## Concepts abordés

- Classe, instance, `__init__`, `self`
- Attributs d'instance et méthodes
- Composition (un objet contient d'autres objets)
- Threading — exécution parallèle

## À retenir

### Classe et instance

```python
class Voiture:
    def __init__(self, marque: str, vitesse_max: int):
        self.marque      = marque
        self.vitesse_max = vitesse_max
        self.vitesse     = 0

    def accelerer(self, delta: int) -> None:
        self.vitesse = min(self.vitesse + delta, self.vitesse_max)
```

- `__init__` est le **constructeur** — appelé à la création de l'objet.
- `self` est la référence à l'instance courante ; il doit être le premier paramètre de chaque méthode.

```python
ma_voiture = Voiture("Renault", 180)   # création d'une instance
ma_voiture.accelerer(50)               # appel de méthode
print(ma_voiture.vitesse)              # 50
```

### Composition

Un objet peut **contenir** d'autres objets en référence. C'est la relation "a un" (*has-a*).

```python
class Pilote:
    def __init__(self, nom: str):
        self.nom = nom

class Voiture:
    def __init__(self, pilote: Pilote):
        self.pilote = pilote   # Voiture "a un" Pilote
```

À distinguer de l'**héritage** (relation "est un" / *is-a*), vu dans le dossier 10.

### Threading

Exécuter plusieurs tâches **en parallèle** avec `threading.Thread`.

```python
import threading

def tache(nom: str) -> None:
    print(f"{nom} démarre")

t1 = threading.Thread(target=tache, args=("A",))
t2 = threading.Thread(target=tache, args=("B",))

t1.start()   # lance le thread
t2.start()

t1.join()    # attend la fin du thread
t2.join()
```

- `start()` — démarre l'exécution du thread.
- `join()` — bloque jusqu'à ce que le thread ait terminé.
- L'ordre d'exécution entre threads n'est **pas garanti**.

### Lambda pour trier des objets

```python
voitures = [v1, v2, v3]
gagnant = min(voitures, key=lambda v: v.temps_total)
```

## Architecture du projet (course automobile)

```
Race
 ├─ Circuit  (distance)
 └─ Car[]
     └─ Pilot  (nom)
```

| Classe    | Responsabilité                                      |
|-----------|-----------------------------------------------------|
| `Pilot`   | Données du pilote (nom)                             |
| `Car`     | Vitesse, calcul du temps par tour                   |
| `Circuit` | Distance d'un tour                                  |
| `Race`    | Orchestration : threads, boucle de tours, vainqueur |
