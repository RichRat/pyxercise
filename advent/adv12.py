import math
from idlelib.pyshell import extended_linecache_checkcache

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

    def find_area(letter, pos: IntVector2, group):
        for next_pos in [ pos + dir for dir in dir_list ]:
            if next_pos.is_in_bounds(grid) and not next_pos.of_grid(added_grid) and next_pos.of_grid(grid) == letter:
                group.append(next_pos)
                next_pos.set_grid(added_grid, True)
                find_area(letter, next_pos, group)

    def check_line(dir, pos, group):
        #while
        pass


    result = 0
    for pos, val in grid_walk_val(grid):
        if pos.of_grid(added_grid):
            continue

        group = [ pos ]
        pos.set_grid(added_grid, True)
        find_area(val, pos, group)
        fence = []
        for p in group:
            for fence_pos in [ p + dir for dir in dir_list ]:
                if not fence_pos.is_in_bounds(grid) or fence_pos.of_grid(grid) != val:
                    fence.append(fence_pos)

        fence_len = 0
        ignore = [] # keep track of already used fence positions
        for fpos in fence:
            if fpos in ignore:
                ignore.remove(fpos)
                continue

            if [ True for v in  [ (fpos + dir) for dir in fence ] if v in fence and v not in ignore ]:
                ignore.append(fpos)
            else:
                fence_len += 1

        result += len(group) * fence_len

    print("result " + str(result))

timed_run(advent_12_step_2())