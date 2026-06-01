from playable import Monster

class Dragon(Monster):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return "D"
    
    def _init_race_bonus(self) -> None:
        self._endurance += 1
        return