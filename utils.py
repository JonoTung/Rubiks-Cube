from enum import Enum

class Color(Enum):
    GREEN = (0.5647, 0.9333, 0.5647),
    YELLOW = (1, 0.9333, 0.5647),
    RED = (1, 0.5647, 0.5647),
    ORANGE = (1, 0.8, 0.5647),
    BLUE = (0.5647, 0.8, 1),
    WHITE = (1, 1, 1),
    BLACK = (0, 0, 0),

class Face(Enum):
    F = 0
    B = 1
    R = 2
    L = 3
    U = 4
    D = 5