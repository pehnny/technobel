from .playable import Hero

class Dwarf(Hero):
    def __init__(self):
        super().__init__()
    
    def __str__(self) -> str:
        return "H"
    
    def _init_race_bonus(self) -> None:
        self._endurance += 2
        return  
