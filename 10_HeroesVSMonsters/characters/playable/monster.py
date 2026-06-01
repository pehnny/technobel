from characters.metaclass.character import Character
from dices.dice import dice_four

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.coin = self._init_coin()
        self.leather = self._init_leather()

    def _init_coin(self) -> int:
        return dice_four.roll()
    
    def _init_leather(self) -> int:
        return dice_four.roll()