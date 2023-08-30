from utils import *

class Cube:

    def __init__(self, scramble):
        self.scramble = scramble

    orientation = {
        Face.U: [
            [Color.WHITE, Color.WHITE, Color.WHITE],
            [Color.WHITE, Color.WHITE, Color.WHITE],
            [Color.WHITE, Color.WHITE, Color.WHITE],
        ],
        Face.F: [
            [Color.GREEN, Color.GREEN, Color.GREEN],
            [Color.GREEN, Color.GREEN, Color.GREEN],
            [Color.GREEN, Color.GREEN, Color.GREEN],
        ],
        Face.R: [
            [Color.RED, Color.RED, Color.RED],
            [Color.RED, Color.RED, Color.RED],
            [Color.RED, Color.RED, Color.RED],
        ],
        Face.D: [
            [Color.YELLOW, Color.YELLOW, Color.YELLOW],
            [Color.YELLOW, Color.YELLOW, Color.YELLOW],
            [Color.YELLOW, Color.YELLOW, Color.YELLOW],
        ],
        Face.B: [
            [Color.BLUE, Color.BLUE, Color.BLUE],
            [Color.BLUE, Color.BLUE, Color.BLUE],
            [Color.BLUE, Color.BLUE, Color.BLUE],
        ],
        Face.L: [
            [Color.ORANGE, Color.ORANGE, Color.ORANGE],
            [Color.ORANGE, Color.ORANGE, Color.ORANGE],
            [Color.ORANGE, Color.ORANGE, Color.ORANGE],
        ],
    }