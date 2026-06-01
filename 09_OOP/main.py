from race.Car import Car
from race.Circuit import Circuit
from race.Pilot import Pilot
from race.Race import Race

from inheritance.human import Human
from inheritance.character import Character

def main() -> None:
    # race
    michel, mike, rene = Pilot("Michel"), Pilot("Mike"), Pilot("René")
    cars = [
        Car(120, 350, "Fiat", "Punto", michel),
        Car(110, 365, "Renault", "Clio", mike),
        Car(60, 420, "Audi", "R8", rene)
    ]

    circuit = Circuit(15)
    race = Race(5, cars, circuit)
    race.run()
    
    winner = race.get_winner()
    if winner:
        print(f"{winner.pilot.name} won the race with his {winner.model} {winner.brand}.")

    # inheritance
    hero = Human()
    print(isinstance(hero, Character))
    return

if __name__ == "__main__":
    main()