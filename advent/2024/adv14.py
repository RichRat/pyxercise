import math
import random
import re
import time

from util.grid_util import grid_walk, grid_walk_val
from util.timing import timed_run
from util.vector import IntVector2
from matplotlib import pyplot as plt, animation


def advent_14_step_1():
    with open('../resources/advent/14_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    size, time  = IntVector2(101, 103), 100
    quadrants = [0] * 4
    for line in lines:
        inp = [ int(match) for match in re.findall(r"[-\d]+", line) ]
        bot_pos, bot_dir = IntVector2(*inp[:2]), IntVector2(*inp[2:4])
        bot_pos = (bot_pos + bot_dir * time) % size
        if bot_pos.x == size.x // 2 or bot_pos.y == size.y // 2:
            continue

        quadrant = bot_pos.x * 2 // size.x + (bot_pos.y * 2 // size.y) * 2
        quadrants[quadrant] += 1

    result = math.prod(quadrants)
    print("result " + str(result))
    # 1.8ms

def advent_14_step_2():
    with open('../resources/advent/14_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    size, bot_time  = IntVector2(101, 103), 100
    bot_list = []
    for line in lines:
        inp = [ int(match) for match in re.findall(r"[-\d]+", line) ]
        bot_list.append((IntVector2(*inp[:2]), IntVector2(*inp[2:4])))


    def get_pos_for_time(t):
        for bot in bot_list:
            yield (bot[0] + bot[1] * t) % size

    def get_display_grid(pos_arr: [IntVector2]):
        ret = [ [ 0 for x in range(size.x )] for y in range(size.y) ]
        for pos in pos_arr:
            pos.set_grid(ret, 1)

        return ret

    check_dirs = [IntVector2(0,1)]
    def check_bots_for_lines(bot_dict: dict, length):
        for bot in bot_dict.keys():
            for d in check_dirs:
                is_line = True
                for i in range(1, length + 1):
                    check_pos = bot + d * i
                    if check_pos not in bot_dict:
                        is_line = False
                        break

                if is_line:
                    return True

        return False

    for t in range(20000):
        bd = dict([ (bot, True) for bot in get_pos_for_time(t) ])
        if check_bots_for_lines(bd, 7):
            print("time " + str(t))
            plt.imshow(get_display_grid(get_pos_for_time(t)))
            plt.show()
            return


timed_run(advent_14_step_1)