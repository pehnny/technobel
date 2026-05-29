from package.Circuit import Circuit
from package.Car import Car

class Race:
    def __init__(self, turn: int, car1: Car, car2: Car, circuit: Circuit):
        self.turn = turn
        self.car1 = car1
        self.car2 = car2
        self.circuit = circuit
        self.done = False
    
    def run(self):
        distance = self.circuit.distance
        for i in range(self.turn):
            self.car1.change_speed()
            self.car2.change_speed()
            self.car1.add_time(distance)
            self.car2.add_time(distance)
        self.done = True
        return
    
    def get_winner(self) -> Car | None:
        if self.done:
            return self.car1 if self.car1.time < self.car2.time else self.car2
        return None