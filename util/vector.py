from util.math_util import greatest_common_divisor


class IntVector2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return IntVector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return IntVector2(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        if isinstance(factor, int):
            return IntVector2(self.x * factor, self.y * factor)
        else:
            raise Exception("cannot multiply " + str(factor) + " with IntVector2 only int supported!")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def of_grid(self, grid):
        return grid[self.y][self.x]

    def is_in_bounds(self, grid):
        return 0 <= self.y < len(grid) and 0 <= self.x < len(grid[0])

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __hash__(self):
        return hash(str(self))

    def normalize(self):
        gcd = greatest_common_divisor(abs(self.x), abs(self.y))
        return IntVector2(int(self.x / gcd), int(self.y / gcd))




#### test code ####
# a = IntVector2(1,2)
# b = IntVector2(2,1)
#
# print("Vect test result " + str((a + b) * 2 - IntVector2(1,3) == IntVector2(5,3)))
# print("vect norm test " + str(IntVector2(12,3).normalize() == IntVector2(4, 1)))