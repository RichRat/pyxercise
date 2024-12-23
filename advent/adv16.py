from util.grid_util import grid_walk_val
from util.timing import timed_run
from util.vector import IntVector2 as Iv, null_vector


def advent_16_step_1():
    with open('../resources/advent/15_input.txt') as list_file:
       lines = [ line for line in list_file.read().split("\n")]

    #print("result " + str(result))


timed_run(advent_16_step_1)