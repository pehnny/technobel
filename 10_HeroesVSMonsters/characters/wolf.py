from characters.metaclass.character import Character
from characters.interfaces.monster import Monster
from dices.dice import dice_six, dice_four

class Wolf(Character, Monster):
    def __init__(self):
        self._endurance = self._init_endurance()
        self._force = self._init_force()
        self.life = self._init_life()
        self._max_life = self.life
        self.alive = True
        self.coin = self._init_coin()
        self.leather = self._init_leather()
        self._init_race_bonus()
    
    def __str__(self) -> str:
        return "W"
    
    def _init_endurance(self) -> int:
        return sum(dice_six.n_best_roll(3, 4))
    
    def _init_force(self) -> int:
        return sum(dice_six.n_best_roll(3, 4))
    
    def _init_life(self) -> int:
        return self.modifier(self._endurance)
    
    def _init_coin(self) -> int:
        return 0
    
    def _init_leather(self) -> int:
        return dice_four.roll()
    
    def _init_race_bonus(self) -> None:
        return
    
    def hit(self) -> int:
        base = dice_four.roll()
        return base + self.modifier(self._force)
    
    def is_alive(self) -> bool:
        return self.alive