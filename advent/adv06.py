from copy import deepcopy

from util.timing import timed_run


def advent_06(): # slow but correct
    class Guard:
        def __init__(self, x, y, grid):
            self.x, self.y, self.c = x, y ,grid[y][x]
            self.grid = grid

        def is_in_bounds(self, dx=0, dy=0):
            return 0 <= (self.x + dx) < len(self.grid[0]) and 0 <= (self.y + dy) < len(self.grid)

        def move_pos(self, x, y):
            self.x += x
            self.y += y

        def get_dir_ind(self):
            return dir_char.index(self.c)

        def get_dir_vect(self):
            return dirs[self.get_dir_ind()]


    def find_guard(grid):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] in dir_char:
                    return Guard(x, y, grid)

    def run_path(grid):
        guard = find_guard(grid)
        log = []
        while True:
            dx, dy = guard.get_dir_vect()
            if not guard.is_in_bounds(dx, dy):
                grid[guard.y][guard.x] = dir_trail[guard.get_dir_ind()]
                return 0, grid
            elif grid[guard.y + dy][guard.x + dx] in [ "#", "O" ] :
                # rotate guard
                di = guard.get_dir_ind()
                di = (di + 1) % len(dirs)
                guard.c = dir_char[di]
                grid[guard.y][guard.x] = guard.c
            else:
                grid[guard.y][guard.x] = dir_trail[guard.get_dir_ind()]
                guard.move_pos(dx, dy)
                log_entry = str(guard.x) + ',' + str(guard.y) + 'd' + str(guard.get_dir_ind())
                # detect loop after moving guard
                if log_entry in log:
                    return 1, None

                log.append(log_entry)
                #write new position to grid if no loop was detected
                grid[guard.y][guard.x] = guard.c


    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_char = ['^', '>', 'v', '<']
    dir_trail = ['u', 'r', 'd', 'l']
    with open('../resources/advent/6_input.txt') as list_file:
        orig_grid = [[s for s in line] for line in list_file.read().split('\n')]

    result = 0
    _, normal_run = run_path(deepcopy(orig_grid))


    for y in range(len(normal_run)):
        for x in range(len(normal_run[0])):

            if normal_run[y][x] not in dir_trail or orig_grid[y][x] in dir_char:
                continue

            n_grid = deepcopy(orig_grid)
            n_grid[y][x] = "O"
            r, _ = run_path(n_grid)
            result += r

    print("result " + str(result))


timed_run(advent_06)