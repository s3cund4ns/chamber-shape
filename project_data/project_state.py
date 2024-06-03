from enum import Enum, auto


class ProjectState(Enum):
    NOT_EXISTING = auto()
    NOT_SAVED = auto()
    SAVED = auto()
