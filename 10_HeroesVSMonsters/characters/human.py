from characters.playable.hero import Hero

class Human(Hero):
    def __init__(self):
        super().__init__()
    
    def __str__(self) -> str:
        return "H"
    
    def _init_race_bonus(self) -> None:
        self._endurance += 1
        self._force += 1
        return
