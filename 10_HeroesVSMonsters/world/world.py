import random
from characters import Wolf, Dragon, Orc
from characters.playable.hero import Hero
from characters.playable.monster import Monster
from characters.enum.monster import MonsterClass
from errors import MonsterClassError, OccupiedError
from chunk import Chunk

class World:
    def __init__(self, size: int, hero: Hero) -> None:
        self._seed: random.Random = random.Random()
        self.size = size
        self.chunks: list[list[Chunk]]  = [
            [Chunk((x, y)) for x in range(size)]
            for y in range(size)
        ]
        self.monsters: list[Monster] = self._init_monsters()
        self.monsters_location: list[tuple[int, int]] = []
        self._set_monsters()
        self.hero: Hero = hero
        self.hero_location: tuple[int, int] = self._set_hero()
    
    def _init_monsters(self) -> list[Monster]:
        keys = [monster.value for monster in MonsterClass]
        choices = [self._seed.choice(keys) for _ in range(10)]

        monsters: list[Monster] = []
        for monster in choices:
            match monster:
                case MonsterClass.WOLF.value:
                    monsters.append(Wolf())
                case MonsterClass.ORC.value:
                    monsters.append(Orc())
                case MonsterClass.DRAGON.value:
                    monsters.append(Dragon())
                case _:
                    raise MonsterClassError()
        return monsters
    
    def _set_monsters(self) -> None:
        positions = [(x, y) for y in range(self.size) for x in range(self.size)]

        for monster in self.monsters:
            position = self._seed.choice(positions)
            x, y = position
            self.chunks[y][x].goto(monster)
            self.monsters_location.append(position)

            adjacents = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            forbidden = [position]
            for dx, dy in adjacents:
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    forbidden.append((nx, ny))
                    
            positions = [position for position in positions if position not in forbidden]
        return

    def _set_hero(self) -> tuple[int, int]:
        done = False
        x = self._seed.choice(range(self.size))
        y = self._seed.choice(range(self.size))
        while not done:
            if self.chunks[y][x].character != None:
                x = self._seed.choice(range(self.size))
                y = self._seed.choice(range(self.size))
                continue
            self.chunks[y][x].goto(self.hero)
            done = True
        return (x, y)
    
    def in_world(self, x: int, y: int) -> bool:
        if 0 <= x < self.size and 0 <= y < self.size:
            return True
        return False
    
    def reveal(self, coordinates: tuple[int, int]) -> None:
        x, y = coordinates
        adjacents = [(1,0), (-1,0), (0,1), (0,-1)]
        valid_neighbors = [(x, y)]
        for dx, dy in adjacents:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                valid_neighbors.append((nx, ny))

        for x, y in valid_neighbors:
            self.chunks[y][x].is_revealed = True
        return

    def move_hero(self, old_coordinates: tuple[int, int], new_coordinates: tuple[int, int]) -> None:
        ox, oy = old_coordinates
        nx, ny = new_coordinates
        if not 0 <= nx < self.size:
            raise IndexError("Out of map x axis.")
        if not 0 <= ny < self.size:
            raise IndexError("Out of map y axis.")
        try:
            self.hero_location = new_coordinates
            self.chunks[ny][nx].goto(self.hero)
            self.chunks[oy][ox].leave()
        except OccupiedError:
            raise OccupiedError()
        return
