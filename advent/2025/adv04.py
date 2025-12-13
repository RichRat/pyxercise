from util.advent import AocUtil
from util.grid_util import grid_walk_val, grid_neighbors, grid_walk
from util.timing import timed_run
from util.vector import IntVector2

iv = IntVector2

dirs = [
    iv(1, 0),
    iv(1, 1),
    iv(0, 1),
    iv(-1, 1),
    iv(-1, 0),
    iv(-1, -1),
    iv(0, -1),
    iv(1, -1),
]

def advent_04p1():
    grid = AocUtil().load_aoc_25(4)

    res = 0

    for pos, val in grid_walk_val(grid):
        if val != '@':
            continue

        count = 0
        for n_pos, n_val in grid_neighbors(pos, grid):
            if n_val == '@':
                count += 1
                if count > 3:
                    break

        if count < 4:
            res += 1

    print("result " + str(res))


timed_run(advent_04p1)


def advent_04p2():
    grid = AocUtil().load_aoc_25(4)

    res = 0
    removed = [ -1 ]
    hot_list = None
    while len(removed) > 0:
        removed = remove_rolls(grid, hot_list)
        res += len(removed)
        hot_list = get_hot_positions(grid, removed)

    #for row in grid:
    #    print(row)

    print("result " + str(res))

def get_hot_positions(grid, removed):
    ret = set()
    for pos in removed:
        for n_pos, val in grid_neighbors(pos, grid):
            if val == '@':
                ret.add(n_pos)


    return ret

def remove_rolls(grid, reduced=None):
    ret = []
    for pos in grid_walk(grid) if reduced is None else reduced:
        val = pos.of_grid(grid)
        if val != '@':
            continue

        count = 0
        for n_pos, n_val in grid_neighbors(pos, grid):
            if n_val == '@':
                count += 1
                if count > 3:
                    break

        if count < 4:
            ret.append(pos)

    for pos in ret:
        row = grid[pos.y]
        grid[pos.y] = row[:pos.x] + '.' + row[pos.x+1:]

    return ret


timed_run(advent_04p2)
