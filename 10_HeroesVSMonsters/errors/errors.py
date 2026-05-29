class MonsterError(BaseException):
    pass

class MonsterClassError(MonsterError):
    pass

class ChunkError(BaseException):
    pass

class OccupiedError(ChunkError):
    pass

