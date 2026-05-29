import threading
from time import sleep
from package.Circuit import Circuit
from package.Car import Car

class Race:
    def __init__(self, turn: int, car1: Car, car2: Car, circuit: Circuit):
        self.turn = turn
        self.car1 = car1
        self.car2 = car2
        self.circuit = circuit
        self.done = False

    def run_turn(self, car: Car, turn: int) -> None:
        for _ in range(turn):
            car.change_speed()
            time = car.add_time(self.circuit.distance)
            print(f"{car.pilot.name} performes {time} seconds")
            sleep(0.5)
        return
    
    def run(self) -> None:
        distance = self.circuit.distance
        cars = [self.car1, self.car2]
        threads: list[threading.Thread] = []
        for car in cars:
            threads.append(threading.Thread(target=self.run_turn, args=(car, self.turn)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.done = True
        return
    
    def get_winner(self) -> Car | None:
        if self.done:
            return self.car1 if self.car1.time < self.car2.time else self.car2
        return None