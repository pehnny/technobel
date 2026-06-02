from world import World
from characters.playable import Hero
from characters.enum import HeroClass
from characters import Human, Dwarf
from characters.metaclass import Character
from errors import UnknownHeroClassError

class Game:
    hero: Hero
    world: World

    def __init__(self) -> None:
        self.hero = self._choseHeroClass()
        self.world = self._load_world()

    def _is_valid_input(self, user_input: str, valid_inputs: list[str]) -> bool:
        if user_input in valid_inputs:
            return True
        return False

    def _choseHeroClass(self) -> Hero:
        hero_classes = [hero.name for hero in HeroClass]
        print("Chose a class from the list below")
        print("Available classes :")
        print(*[hero for hero in hero_classes])
        
        user_input = input("> ").upper()
        while not self._is_valid_input(user_input, hero_classes):
            print("Invalid class. Please chose again.")
            user_input = input("> ").upper()

        match user_input:
            case HeroClass.HUMAN.name:
                return Human()
            case HeroClass.DWARF.name:
                return Dwarf()
            case _:
                raise UnknownHeroClassError()

    def _load_world(self) -> World:
        return World(15, self.hero)
    
    def _print_world(self) -> None:
        x_size = 4 * len(self.world.chunks[0]) + 1
        for y in range(self.world.size):
            print("".join(["-" for _ in range(x_size)]))
            print("|", end="")
            for x in range(self.world.size):
                chunk = self.world.chunks[y][x]
                mark = " "
                if chunk.is_revealed:
                    if isinstance(chunk.character, Character):
                        mark = str(chunk.character)
                else :
                    mark = "X"
                print(f" {mark} ", end="|")
            print()
        return
    
    def _near_monster(self) -> tuple[int, int]:
        x, y = self.world.hero_location
        adjacents = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in adjacents:
            ax, ay = x+dx, y+dy
            if self.world.in_world(ax, ay):
                if (ax, ay) in self.world.monsters_location:
                    print(f"A monster attacks !")
                    return (ax, ay)
        print("No monster found nearby.")
        return (-1, -1)

    def _fight(self, monster_location: tuple[int, int]) -> None:
        x, y = monster_location
        monster_index = self.world.monsters_location.index(monster_location)
        monster = self.world.monsters[monster_index]

        print("Press any key to continue")
        input("> ")
        print(f"It's a {type(monster)}")
        while self.hero.is_alive():
            hero_hit = self.hero.hit()
            print(f"Hero hits {hero_hit} !")
            monster.life -= hero_hit
            print(f"The {type(monster)} has {monster.life} hp left.")
            if monster.is_alive():
                monster_hit = monster.hit()
                print(f"Monster hits {monster_hit} !")
                self.hero.life -= monster_hit
                print(f"The hero has {self.hero.life} hp left.")
            else:
                print(f"The {monster.__class__.__name__} died !")
                coin = monster.coin
                leather = monster.leather
                self.hero.loot(monster)
                print(f"The hero found {coin} coins and {leather} leather.")
                self.hero.rest()
                self.world.monsters.pop(monster_index)
                self.world.monsters_location.pop(monster_index)
                self.world.chunks[y][x].leave()
                print("Press any key to continue")
                input("> ")
                return
        print("The hero died !")
        return

    def _move(self) -> None:
        x, y = self.world.hero_location
        adjacents = [("right", 1, 0), ("left", -1, 0), ("down", 0, 1), ("up", 0, -1)]

        valid_directions : dict[str, tuple[int, int]] = {}
        for direction, dx, dy in adjacents:
            nx, ny = x+dx, y+dy
            if self.world.in_world(nx, ny):
                if (nx, ny) not in self.world.monsters_location:
                    valid_directions[direction] = (nx, ny)
        
        print("Do you want to move", list(valid_directions), "?")
        user_input = input("> ")
        while user_input not in list(valid_directions):
            print("Invalid direction. Try again.", list(valid_directions), sep="\n")
            user_input = input("> ")

        self.world.move_hero((x, y), valid_directions[user_input])
        pass

    def run(self) -> None:
        while len(self.world.monsters) > 0:
            if not self.hero.is_alive():
                print("Game over !")
                return
            
            self.world.reveal(self.world.hero_location)
            print(self.world.hero_location)
            print(self.world.monsters_location)
            self._print_world()

            monster_location = self._near_monster()
            if monster_location != (-1, -1):
                self._fight(monster_location)
            else:
                self._move()
        print("All monsters were defeated, congrats !")
        return
