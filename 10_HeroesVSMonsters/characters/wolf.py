from .playable import Monster

class Wolf(Monster):
    def __init__(self):
        super().__init__()
    
    def __str__(self) -> str:
        return "W"
    
    def _init_race_bonus(self) -> None:
        return