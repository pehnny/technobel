from characters.metaclass.character import Character
from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def loot(self, target: Character) -> None:
        pass

    @abstractmethod
    def rest(self) -> None:
        pass