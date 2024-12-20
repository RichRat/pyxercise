from util.grid_util import grid_walk
from util.timing import timed_run
from util.vector import IntVector2


def advent_10():
    with open('../resources/advent/10_input.txt') as list_file:
        grid = [[int(c) for c in line] for line in list_file.read().split('\n')]

    trail_heads = [v for v in grid_walk(grid) if v.of_grid(grid) == 0]
    dir_list = [IntVector2(*c) for c in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    def traverse(pos, out_targets: list ,val=0):
        if val == 9:
            out_targets.append(pos)
            return

        for v in [ pos + d for d in dir_list ]:
            if v.is_in_bounds(grid) and v.of_grid(grid) == val + 1:
                traverse(v, out_targets, val + 1)

        return out_targets

    result = 0
    for pos in trail_heads:
        result += len(traverse(pos, []))

    print("result " + str(result))

timed_run(advent_10)