from enum import Enum
from characters.enum.hero import HeroClass
from characters.enum.monster import MonsterClass

_offset = len(HeroClass)

Entity = Enum(
    "Entity",
    {h.name: h.value for h in HeroClass}
    | {m.name: m.value + _offset for m in MonsterClass},
)
