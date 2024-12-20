import math
import re
import time
from copy import deepcopy

from util.grid_util import grid_coords
from util.math_util import reversed_en
from util.vector import IntVector2


def advent_01():
    with open('resources/advent/1_lists.txt') as list_file:
        rows = [char.split(" ") for char in list_file.read().split('\n')]

    a = []
    b = []
    for row in rows:
        a.append(int(row[0]))
        b.append(int(row[1]))

    #a = sorted(a)
    #b = sorted(b)
    #print("result " + str(sum([ abs(a[i] - b[i]) for i in range(len(a))])))

    f = lambda num: len([ n for n in b if n == num ])

    print("result " + str(sum([ n * f(n) for n in a  ])))

def advent_02():
    def check_row(row):
        trend = 0
        for i, n in enumerate(row):
            if i + 1 >= len(row): break
            ip = row[i + 1]
            delta = n - ip
            if 0 == abs(delta) or abs(delta) > 3 or abs(trend - delta / abs(delta)) > 1:
                return False

            trend = delta / abs(delta)

        return True

    def check(row):
        if check_row(row):
            return True

        for j in range(len(row)):
            if check_row([ row[k] for k in range(len(row)) if k != j ]):
                return True

        return False

    with open('resources/advent/2_input.txt') as list_file:
        rows = [ [int(n) for n in char.split(" ")] for char in list_file.read().split('\n')]


    print("result " + str(len([ row for row in rows if check(row)])))


def advent_03():
    with open('resources/advent/3_input.txt') as list_file:
        rows = [ char for char in list_file.read().split('\n')]

    #rows = [ 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))' ]

    result = 0
    enabled = True
    for row in rows:
        for op in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", row):
            if op.startswith("do"):
                enabled = not op.startswith("don't")

            if enabled and op.startswith("mul"):
                res = re.search(r"(\d+),(\d+)", op)
                result += int(res.group(1)) * int(res.group(2))

    print("result " + str(result))



def ad04_check(x, y, vect, grid):
    s = "".join([ grid[y + vect[1] * i][x + vect[0] * i] for i in range(-1, 2) ])
    return s == "MAS" or s[::-1] == "MAS"

def advent_04():

    with open('resources/advent/4_input.txt') as list_file:
        grid = [ [ c for c in s] for s in list_file.read().split('\n')]

    directions = [ (1,1), (1,-1) ]

    result = 0
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            if all([ ad04_check(x, y, v, grid) for v in directions ]):
                result += 1

    print("result " + str(result))


class Ad05_Rule:
    def __init__(self, s):
        arr = s.split('|')
        self.a, self.b = int(arr[0]), int(arr[1])

    def check(self, update):
        if self.a not in update or self.b not in update:
            return True

        return update.index(self.a) < update.index(self.b)

    def fix(self, update):
        if not self.check(update):
            ia = update.index(self.a)
            ib = update.index(self.b)
            update[ia], update[ib] = update[ib], update[ia]


def advent_05():
    def is_sorted(update):
        return all([r.check(update) for r in rules])

    with open('resources/advent/5_input.txt') as list_file:
        rows = [ s for s in list_file.read().split('\n')]

    rules = [ Ad05_Rule(r) for r in rows if '|' in r ]
    updates = [ [ int(p) for p in r.split(',') ] for r in rows if ',' in r ]

    filtered_updates = []
    for update in updates:
        if not is_sorted(update):
            filtered_updates.append(update)

    for update in filtered_updates:
        while not is_sorted(update):
            for rule in rules:
                rule.fix(update)


    result = sum([ l[int(len(l) / 2)] for l in filtered_updates ])
    print("result " + str(result))



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
    with open('resources/advent/6_input.txt') as list_file:
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


def advent_07():

    def int_concat(a, b):
        return int(str(a) + str(b))

    def solve(target_val, numbers, ind=1, val=0):
        val = val if ind > 1 else numbers[0]

        if val > target_val:
            return False
        if ind >= len(numbers):
            return val == target_val


        return (solve(target_val, numbers, ind + 1, val * numbers[ind])
                or solve(target_val, numbers, ind + 1, val + numbers[ind])
                or solve(target_val, numbers, ind + 1, int_concat(val ,numbers[ind])))


    with open('resources/advent/7_input.txt') as list_file:
        lines = [line for line in list_file.read().split('\n')]

    lines = [ (int(line.split(' ')[0][:-1]), [ int(s) for s in line.split(' ')[1:]]) for line in lines ]

    result = 0
    for equation in lines:
        if solve(*equation):
            result += equation[0]

    print("result " + str(result))


def advent_08():
    with open('resources/advent/8_input.txt') as list_file:
        grid = [[c for c in line] for line in list_file.read().split('\n')]

    pattern = re.compile(r"[a-zA-Z0-9]")
    sources = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if pattern.match(c):
                pos = IntVector2(x, y)
                sources.append((pos, pos.of_grid(grid)))

    def add_nodes(node, dir):
        while node.is_in_bounds(grid):
            nodes.add(node)
            node += dir_vect

    nodes = set()
    for pos, c in sources:
        for pos_b in [ ant[0] for ant in sources if ant[1] == c and ant[0] != pos]:
            dir_vect = (pos_b - pos).normalize()
            add_nodes(pos, dir_vect)
            add_nodes(pos, dir_vect * -1)

    print("result " + str(len(nodes)))

def advent_09():
    with open('resources/advent/9_input.txt') as list_file:
       def_line = [ int(c) for c in list_file.read()]

    drive = []
    index = []
    for i in range(len(def_line)):
        s = i // 2 if i % 2 == 0 else -1
        drive.extend([s] * def_line[i])


    def get_span(fid, start_at, delta):
        offset = delta
        while drive[start_at + offset] == fid:
            offset += delta

        end_at = start_at + (offset - delta)
        return min(start_at, end_at), max(start_at, end_at)

    def get_span_len(start, end):
        return end - start + 1

    def write_to_drive(start, len, content):
        for i in range(start, start + len):
            drive[i] = content

    skip = {-1}
    for i, fid in reversed_en(drive):
        if fid not in skip:
            span = get_span(fid, i, -1)
            span_len = get_span_len(*span)
            for j in range(len(drive)):
                if j >= i: break
                if drive[j] != -1: continue

                free_span = get_span(-1, j, 1)
                if get_span_len(*free_span) >= span_len:
                    write_to_drive(free_span[0], span_len, fid)
                    write_to_drive(span[0], span_len, -1)
                    moved = True
                    break

            skip.add(fid)


    result = sum([ i * v if v > 0 else 0 for i, v in enumerate(drive) ])
    #print("".join([ '.' if v < 0 else str(v) for v in drive ]))
    print("result " + str(result))



def advent_10():
    with open('resources/advent/10_input.txt') as list_file:
        grid = [[int(c) for c in line] for line in list_file.read().split('\n')]

    trail_heads = [  v for v in grid_coords(grid) if v.of_grid(grid) == 0  ]
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


def advent_11():
    with open('resources/advent/11_input.txt') as list_file:
       line = [ int(c) for c in list_file.read().split(" ")]

    def num_len(num): return int(math.log10(num)) + 1

    def blink(n):
        if n == 0:
            return [1]
        elif num_len(n) % 2 == 0:
            p = 10 ** (num_len(n) / 2)
            return [int(n / p) , int(n % p)]
        else:
            return [n * 2024]

    line_dict = dict((n, 1) for n in line)
    for i in range(75):
        tmp = dict()
        for num, n in line_dict.items():
            for n_new in blink(num):
                if n_new in tmp:
                    tmp[n_new] += n
                else:
                    tmp[n_new] = n

        line_dict = tmp

    result = sum(n for n in line_dict.values())
    print("result " + str(result))



start_time = time.time()
advent_11()
print("--- %s seconds ---" % (time.time() - start_time))
