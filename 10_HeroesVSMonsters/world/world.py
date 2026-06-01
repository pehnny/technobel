import random
from characters.wolf import Wolf
from characters.dragon import Dragon
from characters.orc import Orc
from characters.metaclass.character import Character
from characters.enum.monster import MonsterClass
from errors.errors import MonsterClassError, OccupiedError
from world.chunk import Chunk

class World:
    def __init__(self, size: int, hero: Character) -> None:
        self._seed: random.Random = random.Random()
        self.chunks: list[list[Chunk]]  = [
            [Chunk((x, y)) for x in range(size)]
            for y in range(size)
        ]
        self.monsters: list[Character] = self._init_monsters()
        self._set_monsters()
        self.hero: Character = hero
        self.hero_location: tuple[int, int] = self._set_hero()
    
    def _init_monsters(self) -> list[Character]:
        keys = [monster.value for monster in MonsterClass]
        choices = [self._seed.choice(keys) for _ in range(10)]

        monsters: list[Character] = []
        for monster in choices:
            match monster:
                case MonsterClass.WOLF:
                    monsters.append(Wolf())
                case MonsterClass.ORC:
                    monsters.append(Orc())
                case MonsterClass.DRAGON:
                    monsters.append(Dragon())
                case _:
                    raise MonsterClassError()
        return monsters
    
    def _set_monsters(self) -> None:
        x_coord = list(range(len(self.chunks[0])))
        y_coord = list(range(len(self.chunks)))
        x_max = len(x_coord)
        y_max = len(y_coord)

        for monster in self.monsters:
            x = self._seed.choice(x_coord)
            y = self._seed.choice(y_coord)
            self.chunks[x][y].goto(monster)

            x_forbid = [i for i in range(x-1, x+2) if 0 <= i < x_max]
            y_forbid = [i for i in range(y-1, y+2) if 0 <= i < y_max]
            x_coord = [i for i in x_coord if i not in x_forbid]
            y_coord = [i for i in y_coord if i not in y_forbid]
        return

    def _set_hero(self) -> tuple[int, int]:
        done = False
        x = self._seed.choice(range(len(self.chunks[0])))
        y = self._seed.choice(range(len(self.chunks)))
        while not done:
            if self.chunks[y][x].character == None:
                self.chunks[y][x].goto(self.hero)
                done = True
            x = self._seed.choice(range(len(self.chunks[0])))
            y = self._seed.choice(range(len(self.chunks)))
        return (x, y)
    
    def reveal(self, coordinates: tuple[int, int]) -> None:
        x, y = coordinates
        x_range = [i for i in range(x-1, x+2) if 0 <= i < len(self.chunks[0])]
        y_range = [i for i in range(y-1, y+2) if 0 <= i < len(self.chunks)]
        
        for i in x_range:
            self.chunks[y][i].is_revealed = True
        for j in y_range:
            self.chunks[j][x].is_revealed = True
        return

    def move_hero(self, coordinates: tuple[int, int]) -> None:
        x, y = coordinates
        if not 0 <= x < len(self.chunks[0]):
            raise IndexError("Out of map x axis.")
        if not 0 <= y < len(self.chunks):
            raise IndexError("Out of map y axis.")
        try:
            self.hero_location = coordinates
            self.chunks[y][x].goto(self.hero)
        except OccupiedError:
            raise OccupiedError()
        return
