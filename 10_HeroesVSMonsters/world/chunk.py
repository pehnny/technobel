from characters.metaclass import Character
from typing import Optional
from errors import OccupiedError

class Chunk:
    def __init__(self, coordinates: tuple[int, int]):
        self.character: Optional[Character] = None
        self.coordinates: tuple[int, int] = coordinates
        self.is_revealed = False

    def goto(self, character: Character) -> None:
        if self.character != None:
            raise OccupiedError()
        self.character = character
        return

    def leave(self) -> None:
        self.character = None
        return
