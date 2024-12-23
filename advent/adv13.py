import re

from util.timing import timed_run
from util.vector import IntVector2, null_vector


def advent_13_step_1():
    with open('../resources/advent/13_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    pattern = re.compile(r".*X[+=](\d+), Y[+=](\d+)")
    def parse_line(line: str):
        m = pattern.match(line)
        if m:
            return IntVector2(int(m.group(1)), int(m.group(2)))

    result = 0
    for i in range(0, len(lines), 4):
        a = parse_line(lines[i])
        b = parse_line(lines[i + 1])
        prize = parse_line(lines[i + 2])
        max_b = int(min(prize.x / b.x, prize.y / b.y))

        for b_factor in range(max_b, -1, -1):
            a_factor = 0
            bv = b * b_factor
            while a * a_factor + bv < prize:
                a_factor += 1

            if bv + a * a_factor == prize:
                result += b_factor + a_factor * 3
                break

    print("result " + str(result))


def advent_13_step_2():
    with open('../resources/advent/13_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    pattern = re.compile(r".*X[+=](\d+), Y[+=](\d+)")
    def parse_line(line: str):
        m = pattern.match(line)
        if m:
            return IntVector2(int(m.group(1)), int(m.group(2)))

    result = 0
    for i in range(0, len(lines), 4):
        a = parse_line(lines[i])
        b = parse_line(lines[i + 1])
        p = parse_line(lines[i + 2]) + IntVector2(10000000000000, 10000000000000)
        af = (a.y/a.x)
        bf = (b.y/b.x)
        # x * bf = (x - px) * af + py
        line_intersection_x = round((p.x * af - p.y) / (af - bf))
        if line_intersection_x % b.x != 0:
            continue

        b_factor = line_intersection_x // b.x
        remain_dist = p - b * b_factor
        if remain_dist.x % a.x != 0:
            continue

        a_factor = remain_dist.x // a.x
        if b * b_factor + a * a_factor == p:
            result += b_factor + a_factor * 3

    print("result " + str(result))
    # 2.4 ms


timed_run(advent_13_step_2)