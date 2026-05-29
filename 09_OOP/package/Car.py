import random
from package.Pilot import Pilot

class Car:
    def __init__(self, min_speed: float, max_speed: float, model: str, brand: str, pilot: Pilot):
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.speed = min_speed
        self.time = 0
        self.model = model
        self.brand = brand
        self.pilot = pilot
    
    def change_speed(self):
        self.speed = random.randint(self.min_speed, self.max_speed)

    def add_time(self, distance: float):
        self.time += distance / self.speed