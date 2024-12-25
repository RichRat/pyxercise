from util.grid_util import grid_walk_val
from util.timing import timed_run
from util.vector import IntVector2 as Iv, null_vector, IntVector2


def advent_16_step_1():
    with open('../resources/advent/16_input.txt') as list_file:
       maze = [ [ c for c in line ] for line in list_file.read().split("\n")]

    dirs = [ Iv(1,0), Iv(0, 1), Iv(-1, 0), Iv(0, -1) ]
    start_pos = Iv(1, len(maze) - 2)
    start_dir = 0
    # TODO djikstra algo and build a graph with cost = edge

    class Node:
        def __init__(self, position):
            self.position = position
            self.edges = [None] * 4
            self.min_score_to_node = 10 ** 20
            self.is_finish = False

    class Edge:
        def __init__(self, node_a, node_b, cost):
            self.nodes = [node_a, node_b]
            self.cost = cost

        def get_node(self, node):
            return [ n for n in self.nodes if n != node ][0]

    start_node = Node(Iv(1, len(maze)))
    nodes =  { start_node.position: start_node }

    def run_maze(node: Node):
        ret = []
        for free_direction in [ d for d in range(4) if not node.edges[d] ]:
            if (node.position + dirs[free_direction]).of_grid(maze) == '#':
                node.edges[free_direction] = -1
                continue

            position = node.position
            direction = free_direction
            edge_score = 0
            while True:
                position = position + dirs[direction]
                d_list = [ (direction + d) % 4 for d in [-1, 0, 1] ]
                options = [ d for d in d_list if (position + dirs[d]).of_grid(maze) != '#' ]
                edge_score += 1 if direction == options[0] else 1001
                if len(options) != 1: break
                direction = options[0]

            is_finish = position.of_grid(maze) == 'E'
            if (options and len(options) > 0) or is_finish:
                if position in nodes:
                    n = nodes[position]
                else:
                    n = Node(position)
                    nodes[position] = n
                    ret.append(n)
                    n.is_finish = is_finish

                n.edges[(direction + 2) % 4] = Edge(node, n, edge_score)

        return ret

    scan = [ start_node ]
    while scan:
        ns = []
        for node in scan:
            ns.extend(run_maze(node))

        scan = ns


    # TODO graph is built now search for the path option.
    #  also add method to add the 1k turning cost which can't be included into the edge cost
    # TODO also a lot of debugging

    # print results
    # dir_str = ['>', 'v', '<', '^']
    # path = results[result]
    # s_lines = [ [ c for c in line ] for line in maze ]
    # for i, p in enumerate(path):
    #     if i + 1 != len(path):
    #         s_lines[p.y][p.x] = dir_str[dirs.index(path[i+1] - p)]
    #
    # print("\n".join([ "".join(line) for line in s_lines ]))
    # print('\n')
    # print("result " + str(result))


timed_run(advent_16_step_1)