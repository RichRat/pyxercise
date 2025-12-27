import math
import re

from util.timing import timed_run, timed_run_preload_aoc


def run(rows, check):
    res = 0
    for row in rows:
        start, stop = map(int, row.split('-'))
        for i in range(start, stop + 1):
            res += check(i)

    print("result " + str(res))


def advent_02(rows):
    run(rows, check_num)

def check_num(num):
    digits = math.log10(num) + 1
    if  digits % 2 == 1:
        return 0

    divisor = 10**(digits // 2)
    n1 = num // divisor
    n2 = num % divisor
    return num if n1 == n2 else 0




def advent_02p2(rows):
    run(rows, check_num2)

pattern = re.compile(r'^(.+)\1+$')

def check_num2(num):
    s = str(num)
    pattern.match(s)
    return num if pattern.match(s) else 0

timed_run_preload_aoc(advent_02, 25, 2, ',')
timed_run_preload_aoc(advent_02p2, 25, 2, ',')