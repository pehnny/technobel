from csv import Error
import random

class Dice:
    def __init__(self, faces: int) -> None:
        self.seed = random.Random()
        self.faces = faces
    
    def roll(self) -> int:
        return self.seed.randint(1, self.faces)
    
    def n_roll(self, n: int) -> list[int]:
        return [self.roll() for _ in range(n)]
    
    def n_best_roll(self, n: int, total: int) -> list[int]:
        if n > total:
            raise Error(f"total must be grater or equal to n.")
        rolls = self.n_roll(total)
        rolls.sort()
        return rolls[:-n]

dice_four = Dice(4)
dice_six = Dice(6)
