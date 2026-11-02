from util.timing import timed_run_preload_aoc
from util.vector import IntVector2


def advent_09p1(rows):
    res = 0

    points = [ IntVector2(*[ int(s) for s in row.split(',') ]) for row in rows ]

    res = max([
        max([ area(p, p2) for p2 in points ])
        for p in points
    ])

    print("result " + str(res))

def area(p1, p2):
    diff = (p1 - p2).abs()
    return (diff.x + 1) * (diff.y + 1)



hash_divisor = 5000
# TODO optimization resulted in a wrong answer, fix!
def advent_09p2(rows):
    res = 0

    min_size_cutoff = 50000

    points = [ IntVector2(*[ int(sub) for sub in s.split(',')]) for s in rows ]
    area_ref = set()
    for p1 in points:
        val = [gen_ref_obj(area(p1, p2), p1, p2) for p2 in points if p1 != p2 and area(p1, p2) > min_size_cutoff ]
        area_ref |= set(val)


    vertical_lines = sorted([
        (points[i-1], points[i]) for i in range(len(points)) if points[i-1].y == points[i].y
    ], key=lambda t: t[0].y)

    horiz_lines = sorted([
        (points[i - 1], points[i]) for i in range(len(points)) if points[i - 1].x == points[i].x
    ], key=lambda t: t[0].x)



    check_list = sorted(list(area_ref), key=arr_first, reverse=True)
    for a, p1, p2 in check_list:

        if not(points_within(p1, p2, horiz_lines, vertical_lines)):
            res = a
            break

    print("result " + str(res))

def points_within(p1, p2, horiz, vert):
    x1 = min(p1.x, p2.x)
    x2 = max(p1.x, p2.x)
    y1 = min(p1.y, p2.y)
    y2 = max(p1.y, p2.y)

    # check for intersection with horizontal lines
    for lp1, lp2 in horiz:
        if not y1 < lp1.y < y2: continue
        
        # span across                     point1 within         point2 within
        if (lp1.x <= x1 and lp2.x >= x2) or x1 < lp1.x < x2 or x1 < lp2.x < x2:
            return True

    # check for intersection with vertical lines
    for lp1, lp2 in vert:
        if not x1 < lp1.x < x2: continue

        # span across                     point1 within         point2 within
        if (lp1.y <= y1 and lp2.y >= y2) or y1 < lp1.y < y2 or y1 < lp2.y < y2:
            return True
            

    return False


def gen_ref_obj(size, p1, p2):
    if p1.x < p2.x:
        return size, p1, p2
    else:
        return size, p2, p1

def arr_first(a):
    return a[0]


timed_run_preload_aoc(advent_09p1, 25, 9)
timed_run_preload_aoc(advent_09p2, 25, 9)


