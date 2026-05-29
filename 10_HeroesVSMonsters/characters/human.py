from characters.metaclass.character import Character
from characters.interfaces.hero import Hero
from dices.dice import dice_six, dice_four

class Human(Character, Hero):
    def __init__(self, base_endurance: int, base_force: int):
        self._endurance = self._init_endurance()
        self._force = self._init_force()
        self.life = self._init_life()
        self._max_life = self.life
        self.alive = True
        self.coin = 0
        self.leather = 0
        self._init_race_bonus()
    
    def __str__(self) -> str:
        return "H"
    
    def _init_endurance(self) -> int:
        return sum(dice_six.n_best_roll(3, 4))
    
    def _init_force(self) -> int:
        return sum(dice_six.n_best_roll(3, 4))

    def _init_life(self) -> int:
        return self.modifier(self._endurance)
    
    def _init_race_bonus(self) -> None:
        self._endurance += 1
        self._force += 1
        return
    
    def hit(self) -> int:
        base = dice_four.roll()
        return base + self.modifier(self._force)
    
    def is_alive(self) -> bool:
        return self.alive

    def loot(self, target: Character) -> None:
        if not target.alive:
            self.coin += target.coin
            self.leather += target.leather
        return
    
    def rest(self) -> None:
        if self.is_alive():
            self.life = self._max_life
        return 