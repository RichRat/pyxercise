from util.advent import AocUtil
from util.timing import timed_run

def advent_06p1():
    rows = AocUtil().load_aoc_25(6)

    numgrid = [ [ int(sub) for sub in char.split()] for char in rows[:-1]]
    ops = [ sub for sub in rows[-1].split()]

    res = 0
    for i in range(len(numgrid[0])):
        val = 0 if ops[i] == '+' else 1
        for num in [ row[i] for row in numgrid ]:
            if ops[i] == '+':
                val += num
            else:
                val *= num

        res += val

    print("result " + str(res))


def advent_06p2():
    rows = AocUtil().load_aoc_25(6)

    # fix line widths
    rows = [ row.ljust(max([ len(row) for row in rows ])) for row in rows ]

    # rotate input file left and remove spaces
    numgrid = [
        "".join([ rows[y][x] for y in range(len(rows)) ]).replace(" ", "")
        for x in range(len(rows[0]))
    ]

    i = 0
    res = 0
    while i < len(numgrid):
        if numgrid[i][-1] in "+*":
            val = int(numgrid[i][:-1])
            op = numgrid[i][-1]
            i += 1
            while i < len(numgrid) and numgrid[i] != "":
                if op == '*':
                    val *= int(numgrid[i])
                else:
                    val += int(numgrid[i])
                i += 1
            res += val
        i += 1

    print("result " + str(res))


timed_run(advent_06p1)
timed_run(advent_06p2)
