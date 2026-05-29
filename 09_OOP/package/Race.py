import threading
from time import sleep
from package.Circuit import Circuit
from package.Car import Car

class Race:
    def __init__(self, turn: int, cars: list[Car], circuit: Circuit):
        self.turn = turn
        self.cars = cars
        self.circuit = circuit
        self.done = False

    def _run_lap(self, car: Car, turn: int) -> None:
        for _ in range(turn):
            car.change_speed()
            time = car.add_time(self.circuit.distance)
            print(f"{car.pilot.name} performed {time} seconds")
            sleep(0.5)
        return
    
    def run(self) -> None:
        threads: list[threading.Thread] = []
        for car in self.cars:
            threads.append(threading.Thread(target=self._run_lap, args=(car, self.turn)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.done = True
        return
    
    def get_winner(self) -> Car | None:
        if self.done:
            return min(self.cars, key=lambda car: car.time)
        return None