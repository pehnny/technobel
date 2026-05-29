from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def _init_coin(self) -> int:
        pass
    
    @abstractmethod
    def _init_leather(self) -> int:
        pass