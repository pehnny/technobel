import random

class Car:
    def __init__(self, min_speed: float, max_speed: float, model: str, brand: str):
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.speed = self.speed()
        self.time = 0
        self.model = model
        self.brand = brand

    @property
    def speed(self) -> float:
        return self.speed
    
    @property.setter
    def speed(self):
        self.speed = random.randint(self.min_speed, self.max_speed)

    def add_time(self, distance: float):
        self.time += distance / self.speed