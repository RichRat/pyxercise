from util.timing import timed_run


def ad04_check(x, y, vect, grid):
    s = "".join([ grid[y + vect[1] * i][x + vect[0] * i] for i in range(-1, 2) ])
    return s == "MAS" or s[::-1] == "MAS"

def advent_04():

    with open('../resources/advent/4_input.txt') as list_file:
        grid = [ [ c for c in s] for s in list_file.read().split('\n')]

    directions = [ (1,1), (1,-1) ]

    result = 0
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            if all([ ad04_check(x, y, v, grid) for v in directions ]):
                result += 1

    print("result " + str(result))

timed_run(advent_04)