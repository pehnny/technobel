from world.world import World
from typing import Callable
from characters.enum.entity import Entity
from characters.metaclass.character import Character
from characters.enum.hero import HeroClass
from characters.human import Human
from characters.dwarf import Dwarf
from errors.errors import UnknownHeroClassError

class Game:
    hero: Character
    world: World

    def __init__(self) -> None:
        self.hero = self._choseHeroClass()
        self.world = self._loadWorld()

    def _is_valid_input(self, user_input: str, valid_inputs: list[str]) -> bool:
        if user_input in valid_inputs:
            return True
        return False

    def _choseHeroClass(self) -> Character:
        hero_classes = [hero.name for hero in HeroClass]
        print("Chose a class from the list below")
        print("Available classes :")
        print(*[hero for hero in hero_classes])
        
        user_input = input("> ")
        while not self._is_valid_input(user_input, hero_classes):
            print("Invalid class. Please chose again.")
            user_input = input("> ")

        match user_input:
            case HeroClass.HUMAN:
                return Human()
            case HeroClass.DWARF:
                return Dwarf()
            case _:
                raise UnknownHeroClassError()

    def _load_world(self) -> World:
        return World(15, self.hero)
    
    def _print_world(self) -> None:
        x_size = 6 * len(self.world.chunks[0]) + 1
        for row in self.world.chunks:
            print("".join(["-" for _ in range(x_size)]))
            print("|", end=None)
            for chunk in row:
                mark = " "
                if chunk.is_revealed:
                    mark = str(chunk)
                print(f" {mark} ", end="|")
        return
    
    def _is_near_monster(self) -> bool:
        pass

    def _fight(self) -> None:
        pass

    def _move(self) -> None:
        pass

    def run(self) -> None:
        while self.hero.is_alive() or len(self.world.monsters) > 0:
            self.world.reveal(self.world.hero_location)
            self._print_world()

            if self._is_near_monster():
                self._fight()
            else: 
                self._move()
        return
