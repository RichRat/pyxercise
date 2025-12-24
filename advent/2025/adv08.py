import math
import sys
from dataclasses import dataclass
from typing import Any

import numpy
from numpy import dtype, ndarray

from util.advent import AocUtil
from util.timing import timed_run
import numpy as np

def advent_08p1():
    rows = AocUtil().load_aoc_25(8)
    res = 0

    positions = [ np.array([ int(n) for n in row.split(',')]) for row in rows]
    net_index = 0
    net_ref = {} # str, int

    min_dists = set()

    max_connections = 10


    for i in range(len(positions)):
        p1 = positions[i]
        min_dist = sys.maxsize
        min_p2 = None
        for j in range(len(positions)):
            if j == i: continue
            p2 = positions[j]
            d = np.linalg.norm(p1-p2)
            if d < min_dist:
                min_dist = d
                min_p2 = p2

        #if (min_dist, str(min_p2), str(p1)) in min_dists:
        #    continue

        min_dists.add((min_dist, str(p1), str(min_p2)))

    connected = 0
    mds = sorted(min_dists, key=lambda t: t[0])
    for mds_elem in mds:
        nid, con = update_net_ref(net_index, net_ref, mds_elem[1], mds_elem[2])
        net_index += nid
        connected += con
        if connected >= max_connections:
            break

    net_sizes = [ len([ i for i in net_ref.values() if i == v ]) for v in set(net_ref.values()) ]
    net_sizes.sort(reverse=True)
    print("result " + str(math.prod(net_sizes[:3])))


def update_net_ref(net_index, net_ref, p1, p2):

    if p1 not in net_ref and p2 not in net_ref:
        # net net
        net_ref[p1] = net_index
        net_ref[p2] = net_index
        return 1, 1
    elif p1 in net_ref and p2 not in net_ref:
        # extend net of p1
        net_ref[p2] = net_ref[p1]
    elif p1 not in net_ref and p2 in net_ref:
        # extend net of p2
        net_ref[p1] = net_ref[p2]
    elif p1 in net_ref and p2 in net_ref and net_ref[p1] != net_ref[p2]:
        # merge nets by replacing ids
        new_net_id = net_ref[p1]
        old_net_id = net_ref[p2]
        for key in [key for key in net_ref if net_ref[key] == old_net_id]:
            net_ref[key] = new_net_id
    else: # already connected
        return 0, 0

    return 0, 1


def advent_08p2():
    rows = AocUtil().load_aoc_25(8)
    res = 0

    print("result " + str(res))


timed_run(advent_08p1)
timed_run(advent_08p2)

