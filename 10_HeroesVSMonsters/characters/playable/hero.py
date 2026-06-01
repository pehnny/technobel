from characters.metaclass.character import Character

class Hero(Character):    
    def __init__(self):
        super().__init__()

    def loot(self, target: Character) -> None:
        if not target.is_alive():
            self.coin += target.coin
            self.leather += target.leather
        return

    def rest(self) -> None:
        if self.is_alive():
            self.life = self._max_life
        return 