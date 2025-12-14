from util.advent import AocUtil
from util.timing import timed_run

def advent_07p1():
    rows = AocUtil().load_aoc_25(7)
    res = 0

    start = rows[0].index('S')
    beams = [ False ] * len(rows[0])
    beams[start] = True
    for row in [ r for r in rows[1:] if '^' in r]:
        # count splits
        res += sum([ 1 for i in range(len(row)) if beams[i] and row[i] == '^'])
        # get next beam state
        beams = [
            (beams[i] and row[i] != '^')
            or (i + 1 < len(row) and row[i+1] == '^' and beams[i+1])
            or (i - 1 > 0 and row[i-1] == '^' and beams[i-1])
            for i in range(len(row))
        ]

        #print(row)
        #print("".join(["|" if b else "." for b in beams]))

        pass

    print("result " + str(res))


def advent_07p2():
    rows = AocUtil().load_aoc_25(7)

    start = rows[0].index('S')
    paths = [ 0 ] * len(rows[0])
    paths[start] = 1

    for row in [r for r in rows[1:] if '^' in r]:
        next_paths = [0] * len(row)
        for i in range(len(row)):
            ps = paths[i] if row[i] != '^' else 0
            if i + 1 < len(row) and row[i + 1] == '^' and paths[i + 1] > 0:
                ps += paths[i + 1]
            if i - 1 > 0 and row[i - 1] == '^' and paths[i - 1] > 0:
                ps += paths[i - 1]

            next_paths[i] = ps

        paths = next_paths

    print("result " + str(sum(paths)))


timed_run(advent_07p1)
timed_run(advent_07p2)
