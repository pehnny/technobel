from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self):
        self._endurance: int = 0
        self._force: int = 0
        self.life: int = 0
        self._max_life: int = 0
        self.alive: bool = False
        self.coin: int = 0
        self.leather: int = 0

    @staticmethod
    def modifier(stat: int) -> int:
        if stat < 5:
            return stat - 1
        if stat < 10:
            return stat
        if stat < 15:
            return stat + 1
        return stat + 2

    @abstractmethod
    def _init_endurance(self) -> int:
        pass
    
    @abstractmethod
    def _init_force(self) -> int:
        pass
    
    @abstractmethod
    def _init_life(self) -> int:
        pass
    
    @abstractmethod
    def _init_race_bonus(self) -> None:
        pass
    
    @abstractmethod
    def hit(self) -> int:
        pass
    
    @abstractmethod
    def is_alive(self) -> bool:
        pass
