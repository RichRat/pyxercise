from util.timing import timed_run, timed_run_preload_aoc


def advent_01(rows):

    res = 0
    pos = 50
    for row in rows:
        val = int(row[1:])
        if row[0] == 'L':
            val = -val

        pos = (pos + val) % 100
        if pos == 0:
            res += 1

    print("result " + str(res))




def advent_01_2(rows):

    res = 0
    pos = 50
    for row in rows:
        val = int(row[1:])
        rotations, val = divmod(val, 100)
        if row[0] == 'L':
            val = -val

        np = pos + val
        passed = int(pos != 0 and not(0 < np < 100))
        res += rotations + passed
        pos = np % 100

    print("result " + str(res))

timed_run_preload_aoc(advent_01(), 25, 1)
timed_run_preload_aoc(advent_01_2(), 25, 1)