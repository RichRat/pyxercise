from util.timing import timed_run, timed_run_preload_aoc


def advent_03p1():
    with open('../../resources/adv25/03_inp.txt') as list_file:
        rows = [char for char in list_file.read().split('\n') if char != ""]

    res = 0
    for row in rows:
        bank = [int(char) for char in row]
        maxval = 0
        for i in range(len(bank) - 1):
            val = bank[i] * 10 + max(bank[i+1:])
            if val > maxval:
                maxval = val

        res += maxval
    print("result " + str(res))




def advent_03p2():
    with open('../../resources/adv25/03_inp.txt') as list_file:
        rows = [char for char in list_file.read().split('\n') if char != ""]

    res = 0
    for row in rows:
        bank = [int(char) for char in row]
        res += gen_num(bank, 12, 0)

    print("result " + str(res))

def gen_num(bank, numlen, val):
    if numlen == 0:
        return val

    sub = bank[:-(numlen - 1)] if numlen > 1 else bank
    max_digit = max(sub)
    first = sub.index(max_digit)
    return gen_num(bank[first+1:], numlen - 1, val * 10 + max_digit)


timed_run_preload_aoc(advent_03p1, 25, 3)
timed_run_preload_aoc(advent_03p2, 25, 3)