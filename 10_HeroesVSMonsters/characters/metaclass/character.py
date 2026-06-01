from abc import ABC, abstractmethod
from dices.dice import dice_four, dice_six

class Character(ABC):
    _endurance: int
    _force: int
    life: int
    _max_life: int
    coin: int
    leather: int

    def __init__(self):
        self._endurance = self._init_endurance()
        self._force = self._init_force()
        self.life = self._init_life()
        self._max_life = self.life
        self._init_race_bonus()
        self.coin = 0
        self.leather = 0

    @staticmethod
    def modifier(stat: int) -> int:
        if stat < 5:
            return -1
        if stat < 10:
            return 0
        if stat < 15:
            return 1
        return 2
    
    @abstractmethod
    def _init_race_bonus(self) -> None:
        pass

    def _init_endurance(self) -> int:
        return sum(dice_six.n_best_roll(3, 4))
    
    def _init_force(self) -> int:
        return sum(dice_six.n_best_roll(3, 4))
    
    def _init_life(self) -> int:
        return self._endurance + self.modifier(self._endurance)
    
    def hit(self) -> int:
        base = dice_four.roll()
        return base + self.modifier(self._force)
    
    def is_alive(self) -> bool:
        return self.life > 0
