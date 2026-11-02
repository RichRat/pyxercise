from functools import reduce
from util.timing import timed_run_preload_aoc
from operator import xor

def advent_10p1(rows):
    rows = [ row.split(' ') for row in rows ]
    res = 0

    for row in rows:
        target =  sum(2**i if row[0][i] == '#' else 0 for i in range(len(row[0])))
        buttons = [ gen_btn(s) for s in row if s[0] == '(' ]
        for n in range(2, len(buttons)):
            v = solve(target, buttons, n, [])
            if v is not None:
                res += n
                break

    print("result " + str(res))

def solve(target, buttons, length, out, offset=0):
    if length == 0:
        return out if target == reduce(xor, buttons) else None


    for i in range(offset, len(buttons) - length):
        out.append(buttons[i])
        val = solve(target, buttons, length - 1, out, i + 1)
        if val is not None: return val
        out.pop()

    return None

def gen_btn(s):
    return sum(2**(int(num)+1) for num in s[1:-1].split(','))

#def distance(state, target):
#    return sum( 1 if state[i] != target[i] else 0 for i in range(len(state)))

def advent_10p2(rows):
    res = 0
    print("result " + str(res))


timed_run_preload_aoc(advent_10p1, 25, 10)
timed_run_preload_aoc(advent_10p2, 25, 10)


