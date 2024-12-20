import re

from util.timing import timed_run
from util.vector import IntVector2


def advent_08():
    with open('../resources/advent/8_input.txt') as list_file:
        grid = [[c for c in line] for line in list_file.read().split('\n')]

    pattern = re.compile(r"[a-zA-Z0-9]")
    sources = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if pattern.match(c):
                pos = IntVector2(x, y)
                sources.append((pos, pos.of_grid(grid)))

    def add_nodes(node, dir):
        while node.is_in_bounds(grid):
            nodes.add(node)
            node += dir_vect

    nodes = set()
    for pos, c in sources:
        for pos_b in [ ant[0] for ant in sources if ant[1] == c and ant[0] != pos]:
            dir_vect = (pos_b - pos).normalize()
            add_nodes(pos, dir_vect)
            add_nodes(pos, dir_vect * -1)

    print("result " + str(len(nodes)))


timed_run(advent_08)