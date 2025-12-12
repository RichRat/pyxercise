from util.timing import timed_run


def advent_01():
    with open('../../resources/adv25/01_inp.txt') as list_file:
        rows = [char for char in list_file.read().split('\n') if char != ""]


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

timed_run(advent_01)


def advent_01_2():
    with open('../../resources/adv25/01_inp.txt') as list_file:
        rows = [char for char in list_file.read().split('\n')]


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

timed_run(advent_01_2)