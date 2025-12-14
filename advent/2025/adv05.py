from util.advent import AocUtil
from util.timing import timed_run



def advent_05p1():
    range_line, ids = load_input()
    ranges = gen_ranges(range_line)
    res = 0
    for n in ids:
        for rng in ranges:
            if rng[0] <= n <= rng[1]:
                res += 1
                break

    print("result " + str(res))

def gen_ranges(range_line):
    range_line.sort(key=lambda x: x[0] + (0.3 if x[1] == 1 else 0.7))
    ret = []
    start = None
    depth = 0
    for num, d in range_line:
        depth += d
        if start is None and depth == 1:
            start = num
        elif depth == 0:
            ret.append((start, num))
            start = None

    return ret

def load_input():
    rows = AocUtil().load_aoc_25(5)
    ids = [int(row) for row in rows if '-' not in row]
    range_line = [
        (value, is_start)
        for row in rows if '-' in row
        for value, is_start in (
            (int(row.split('-')[0]), 1), # start id
            (int(row.split('-')[1]), -1) # end id
        )
    ]

    return range_line, ids


timed_run(advent_05p1)


def advent_05p2():
    range_line, _ = load_input()
    ranges = gen_ranges(range_line)
    res = 0

    for rng in ranges:
        res += rng[1] - rng[0] + 1

    print("result " + str(res))


timed_run(advent_05p2)
