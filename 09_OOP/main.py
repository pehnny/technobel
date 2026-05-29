from package.Car import Car
from package.Circuit import Circuit
from package.Pilot import Pilot
from package.Race import Race

def main() -> None:
    michel, mike = Pilot("Michel"), Pilot("Mike")
    michel_car = Car(120, 350, "Fiat", "Punto", michel)
    mike_car = Car(110, 365, "Renault", "Clio", mike)

    circuit = Circuit(15)
    race = Race(5, michel_car, mike_car, circuit)
    race.run()
    
    winner = race.get_winner()
    if winner:
        print(f"{winner.pilot.name} won the race with his {winner.model} {winner.brand}.")
    pass

if __name__ == "__main__":
    main()