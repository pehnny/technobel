class CharacterError(BaseException):
    pass

class HeroError(CharacterError):
    pass

class UnknownHeroClassError(HeroError):
    pass

class MonsterError(CharacterError):
    pass

class MonsterClassError(MonsterError):
    pass

class ChunkError(BaseException):
    pass

class OccupiedError(ChunkError):
    pass

