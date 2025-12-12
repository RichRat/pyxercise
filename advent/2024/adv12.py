import math

from util.grid_util import grid_walk_val
from util.timing import timed_run
from util.vector import IntVector2


def advent_12_step_1():
    with open('../resources/advent/12_input.txt') as list_file:
       grid = [ [ c for c in line ] for line in list_file.read().split("\n")]

    added_grid = [ [False] * len(row) for row in grid ]
    dir_list = [IntVector2(*c) for c in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    def find_area(letter, pos: IntVector2, group):
        for next_pos in [ pos + dir for dir in dir_list ]:
            if next_pos.is_in_bounds(grid) and not next_pos.of_grid(added_grid) and next_pos.of_grid(grid) == letter:
                group.append(next_pos)
                next_pos.set_grid(added_grid, True)
                find_area(letter, next_pos, group)

    result = 0
    for pos, val in grid_walk_val(grid):
        if pos.of_grid(added_grid):
            continue

        group = [ pos ]
        pos.set_grid(added_grid, True)
        find_area(val, pos, group)
        fence_len = 0
        for p in group:
            for check_pos in [ p + dir for dir in dir_list ]:
                if not check_pos.is_in_bounds(grid) or check_pos.of_grid(grid) != val:
                    fence_len += 1

        result += len(group) * fence_len

    print("result " + str(result))
    #solves in 52 ms

def advent_12_step_2():
    with open('../resources/advent/12_input.txt') as list_file:
       grid = [ [ c for c in line ] for line in list_file.read().split("\n")]

    added_grid = [ [False] * len(row) for row in grid ]
    dir_list = [IntVector2(*c) for c in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    # recursively find the area
    def find_area(letter, pos: IntVector2, group):
        for next_pos in [ pos + dir for dir in dir_list ]:
            if next_pos.is_in_bounds(grid) and not next_pos.of_grid(added_grid) and next_pos.of_grid(grid) == letter:
                group.append(next_pos)
                next_pos.set_grid(added_grid, True)
                find_area(letter, next_pos, group)

    result = 0
    for pos, val in grid_walk_val(grid):
        if pos.of_grid(added_grid):
            continue

        group = [ pos ]
        pos.set_grid(added_grid, True)
        find_area(val, pos, group)
        fence = []
        for p in group:
            for fence_pos, fdir in [ (p + dir, dir) for dir in dir_list ]:
                if not fence_pos.is_in_bounds(grid) or fence_pos.of_grid(grid) != val:
                    #assign each fence position a perpendicular direction so identical positions can be differentiated
                    check_dir = dir_list[(dir_list.index(fdir) + 1) % len(dir_list)]
                    fence.append((fence_pos, check_dir))

        # count all fences that don't have a neighbour in their direction
        fence_len = len([ "" for f, fd in fence if (f + fd, fd) not in fence ])
        result += len(group) * fence_len

    print("result " + str(result))
    #solves in 105 ms

timed_run(advent_12_step_2)