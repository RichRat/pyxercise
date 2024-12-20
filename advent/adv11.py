import math

from util.timing import timed_run


def advent_11():
    with open('../resources/advent/11_input.txt') as list_file:
       line = [ int(c) for c in list_file.read().split(" ")]

    def num_len(num): return int(math.log10(num)) + 1

    def blink(n):
        if n == 0:
            return [1]
        elif num_len(n) % 2 == 0:
            p = 10 ** (num_len(n) / 2)
            return [int(n / p) , int(n % p)]
        else:
            return [n * 2024]

    line_dict = dict((n, 1) for n in line)
    for i in range(75):
        tmp = dict()
        for num, n in line_dict.items():
            for n_new in blink(num):
                if n_new in tmp:
                    tmp[n_new] += n
                else:
                    tmp[n_new] = n

        line_dict = tmp

    result = sum(n for n in line_dict.values())
    print("result " + str(result))

timed_run(advent_11)