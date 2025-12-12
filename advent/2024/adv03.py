import re

from util.timing import timed_run


def advent_03():
    with open('../resources/advent/3_input.txt') as list_file:
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

timed_run(advent_03)