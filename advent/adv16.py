from util.grid_util import grid_walk_val
from util.timing import timed_run, Stopwatch
from util.vector import IntVector2 as Iv
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, position: Iv):
        self.position = position
        self.edges = [None] * 4 # type: list[Edge|None]
        self.min_score = 10 ** 50
        self.min_score_from = -1
        self.is_finish = False

    def score_edges(self):
        for i, e in enumerate(self.edges):
            if e is not None and i != self.min_score_from:
                #  1000 if abs(self.min_score_from - i) % 2 == 1 else 0
                e.get_node(self).set_score(self.angle_score(i) + e.cost + self.min_score, e)

    # TODO keep track of path for part two and maybe even of identical paths so set a case for score == self.score
    def set_score(self, score, edge):
        if score < self.min_score:
            self.min_score = score
            self.min_score_from = self.edges.index(edge)
        # elif score == self.min_score:
        #     print("hot damn!")

    def backtrace_edges(self, from_edge):
        # if from_edge not in self.edges:
        #     print("wtf!")

        out = []
        min_path_score = 1900000
        from_dir = self.edges.index(from_edge) if from_edge is not None else -2
        for i, e in enumerate(self.edges):
            if e is not None and e != from_edge:
                next_node = e.get_node(self)
                if next_node.min_score >= self.min_score:
                    continue

                score = next_node.min_score + e.cost + self.angle_score(i, from_dir) + next_node.angle_score(to_edge=e)
                if score < min_path_score:
                    out = [ e ]
                    min_path_score = score
                elif score == min_path_score:
                    out.append(e)

        return out

    def angle_score(self, to_dir=-1, from_dir=-1, to_edge=None):
        if from_dir == -2: return 0
        if from_dir == -1: from_dir = self.min_score_from
        if to_edge: to_dir = self.edges.index(to_edge)
        return 1000 if abs(from_dir - to_dir) % 2 == 1 else 0




class Edge:
    def __init__(self, node_a, node_b, cost, trail):
        self.node_a, self.node_b = node_a, node_b
        self.cost = cost
        self.trail = trail

    def get_node(self, node:Node):
        return self.node_a if node == self.node_b else self.node_b

def vect_flip(v):
    v.y *= -1
    return v


def advent_16():
    timer = Stopwatch()
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
        ## STEP 1
        for free_direction in [ d for d in range(4) if not node.edges[d] ]:
            if (node.position + dirs[free_direction]).of_grid(maze) == '#':
                continue

            position = node.position
            direction = free_direction
            edge_score = 0
            trail = [ node.position ]
            while True:
                position = position + dirs[direction]
                trail.append(position)
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

                e = Edge(node, n, edge_score, trail)
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
    finish_node = None
    while unvisited:
        active_node = min(unvisited, key=lambda n: n.min_score)
        if active_node.is_finish:
            print("result step 1 = " + str(active_node.min_score))
            finish_node = active_node

        active_node.score_edges()
        visited.append(active_node)
        unvisited.remove(active_node)

    timer.stop_print(True)
    ## START OF STEP 2

    # now backtrack from the end node and list all edges which are in the optimal paths
    back_edges = []
    back_checked_nodes = [ ]
    def backtrace(node:Node, edge:Edge|None):
        if (node, edge) in back_checked_nodes:
            return

        back_checked_nodes.append((node, edge))
        edges = node.backtrace_edges(edge)
        back_edges.extend([ e for e in edges if e not in back_edges ])
        if start_node in [ e.get_node(node) for e in edges ]:
            return

        for e in edges:
            backtrace(e.get_node(node), e)



    backtrace(finish_node, None)


    points = set([pos for e in back_edges for pos in e.trail])
    print("result step 2 = " + str(len(points)))
    timer.stop_print()


    #draw result
    maze_points = [p for p, v in grid_walk_val(maze) if v == "#"]
    plt.scatter([p.x for p in maze_points], [-p.y for p in maze_points], color=["#BBBBBB"], s=2)
    plt.scatter([p.x for p in points], [-p.y for p in points], color=["red"], s=3)
    plt.show()


advent_16()