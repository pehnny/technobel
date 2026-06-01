from characters.playable.monster import Monster

class Orc(Monster):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return "O"
    
    def _init_race_bonus(self) -> None:
        self._force += 1
        return