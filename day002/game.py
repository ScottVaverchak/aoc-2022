conditions = {
    1: lambda x: ((x - 1 + 2) % 3) + 1,
    2: lambda x: x,
    3: lambda x: ((x - 1 + 1) % 3) + 1
}

LOST = 0
DRAW = 3
WON  = 6

class Game:
    def __init__(self, input: list[tuple[str, str]]):
        self.input = [(ord(x[0]) - 64, ord(x[1]) - 87) for x in input]

    def rig(self):
       self.input = [(x[0], conditions[x[1]](x[0])) for x in self.input]

    def play(self) -> tuple[int, int]:
        test = list(map(sum, zip(*[self._hand_points(x) for x in self.input])))
        return (test[0], test[1])

    def _hand_points(self, input: tuple[int, int]) -> tuple[int, int]:
        match input: 
            case (x, y) if x == y: 
                return (DRAW + x, DRAW + y)
            case (1, 3): 
                return (WON + x, LOST + y)
            case (2, 1): 
                return (WON + x, LOST + y)
            case (3, 2):
                return (WON + x, LOST + y)
            case (x, y):
                return (LOST + x, WON + y)