import math
import time
import random
from idlelib.sidebar import EndLineDelegator

random.seed(time.time())

experiments = 10000

val = 0
for i in range(experiments):
    head = 0
    tail = 0
    count = 0
    while head <= tail:
        count += 1
        if random.randint(0, 1) == 1:
            head += 1
        else:
            tail += 1


    val += head / count

    if i % 100 == 0:
        res = val / (i + 1) * 4
        print("res " + str(res) + " diff " + str(abs((math.pi - res))))


