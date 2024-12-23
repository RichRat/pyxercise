import math
import random
import re
import time

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


    fig = plt.figure()
    im = plt.imshow([ [ random.choice([0,1]) for m in range(size.x)] for n in range(size.y)], animated=True)

    def get_pos_for_time(t):
        return [ (bot[0] + bot[1] * t) % size for bot in bot_list ]

    def get_display_grid(pos_arr: [IntVector2]):
        ret = [ [ 0 for x in range(size.x )] for y in range(size.y) ]
        for pos in pos_arr:
            pos.set_grid(ret, 1)

        return ret

    o = {'t':0}
    def update_anim(*args):
        #if o['t'] >= 100: return [im]
        print("displaying second " + str(o['t'] + 1))
        im.set_array(get_display_grid(get_pos_for_time(o['t'])))
        o['t'] += 1
        return [im]

    anim = animation.FuncAnimation(fig, update_anim, interval=50, blit=True)
    plt.show()



        #display grid
        # plt.imshow(display_grid, interpolation="none")
        # plt.show()





timed_run(advent_14_step_2)