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

def advent_09p2(rows):
    res = 0
    points = [ IntVector2(*[ int(sub) for sub in s.split(',')]) for s in rows ]
    area_ref = set()
    for p1 in points:
        val = [gen_ref_obj(area(p1, p2), p1, p2) for p2 in points if p1 != p2]
        area_ref |= set(val)

    perimeter = []
    prev_point = points[-1]
    for p in points:
        dir = (p - prev_point).normalize()
        pos = prev_point + dir
        while pos != p:
            perimeter.append(pos)
            pos += dir

        prev_point = p

    hash_ref = {}
    for p in points + perimeter:
        key = p.floor_divide(hash_divisor)
        if key not in hash_ref:
            hash_ref[key] = [ p ]
        else:
            hash_ref[key].append(p)


    check_list = sorted(list(area_ref), key=arr_first, reverse=True)
    for a, p1, p2 in check_list:

        if not(points_within(p1, p2, hash_ref)):
            res = a
            break

    print("result " + str(res))

def points_within(p1, p2, hash_ref):
    x1 = min(p1.x, p2.x)//hash_divisor
    x2 = max(p1.x, p2.x)//hash_divisor
    y1 = min(p1.y, p2.y)//hash_divisor
    y2 = max(p1.y, p2.y)//hash_divisor #fix this, good for loop bad for compare

    #check within if possible:s
    for y in range(x1 + 1, x2):
        for x in range(y1 + 1, y2):
            if IntVector2(x,y) in hash_ref:
                return True

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if not(x in [x1, x2] or y in[ y2, y1 ]):
                continue

            key = IntVector2(x, y)
            if key in hash_ref and any([p for p in hash_ref[key] if x1 < p.x < x2 and y1 < p.y < y2]):
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


