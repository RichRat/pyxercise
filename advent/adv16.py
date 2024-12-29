

from util.timing import timed_run
from util.vector import IntVector2 as Iv
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, position: Iv):
        self.position = position
        self.edges = [None] * 4
        self.min_score = 10 ** 50
        self.min_score_from = -1
        self.is_finish = False

    def score_edges(self):
        for i, e in enumerate(self.edges):
            if e is not None and i != self.min_score_from:
                angle_cost = 1000 if abs(self.min_score_from - i) % 2 == 1 else 0
                e.get_node(self).set_score(angle_cost + e.cost + self.min_score, e)

    def set_score(self, score, edge):
        if score < self.min_score:
            self.min_score = score
            self.min_score_from = self.edges.index(edge)



class Edge:
    def __init__(self, node_a, node_b, cost):
        self.node_a, self.node_b = node_a, node_b
        self.cost = cost

    def get_node(self, node:Node):
        return self.node_a if node == self.node_b else self.node_b


def advent_16_step_1():
    with open('../resources/advent/16_input.txt') as list_file:
       maze = [ [ c for c in line ] for line in list_file.read().split("\n")]

    dirs = [ Iv(1,0), Iv(0, 1), Iv(-1, 0), Iv(0, -1) ]

    start_node = Node(Iv(1, len(maze) - 2))
    start_node.min_score = 0
    start_node.min_score_from = 0
    nodes =  { start_node.position: start_node }
    # g_edges = []
    # g_nodes = [ start_node ]

    def run_maze(node:Node):
        ret = []
        for free_direction in [ d for d in range(4) if not node.edges[d] ]:
            if (node.position + dirs[free_direction]).of_grid(maze) == '#':
                continue

            position = node.position
            direction = free_direction
            edge_score = 0
            while True:
                position = position + dirs[direction]
                edge_score += 1
                pos_val = position.of_grid(maze)
                d_list = [ (direction + d) % 4 for d in [-1, 0, 1] ]
                options = [ d for d in d_list if (position + dirs[d]).of_grid(maze) != '#' ]
                if len(options) != 1 or pos_val in 'SE': break
                if direction != options[0]: edge_score += 1000
                direction = options[0]

            is_finish = pos_val == 'E'
            if (options and len(options) > 0) or is_finish and position != node.position:
                if position in nodes:
                    n = nodes[position]
                else:
                    n = Node(position)
                    nodes[position] = n
                    ret.append(n)
                    n.is_finish = is_finish

                    # g_nodes.append(n) # graphical debugging

                e = Edge(node, n, edge_score)
                n.edges[(direction + 2) % 4] = e
                node.edges[free_direction] = e

                # g_edges.append((g_nodes.index(node), g_nodes.index(n))) # graphical debugging

        return ret

    # walk the maze and generate the network graph
    scan = [ start_node ]
    while scan:
        ns = []
        for node in scan:
            ns.extend(run_maze(node))

        scan = ns

    def vect_flip(v):
        v.y *= -1
        return v

    # # display the generated network
    # G = nx.Graph()
    # G.add_edges_from(g_edges)
    # pos = dict(((i, vect_flip(n.position).to_tuple()) for i, n in enumerate(g_nodes)))
    #
    # nx.draw_networkx(G, pos=pos)
    #
    # plt.show()

    # find the optimal path
    visited = []
    unvisited = list(nodes.values())
    while unvisited:
        active_node = min(unvisited, key=lambda n: n.min_score)
        if active_node.is_finish:
            print("result " + str(active_node.min_score))
            break

        active_node.score_edges()
        visited.append(active_node)
        unvisited.remove(active_node)



timed_run(advent_16_step_1)