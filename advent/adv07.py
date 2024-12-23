from util.timing import timed_run


def advent_07():

    def int_concat(a, b):
        return int(str(a) + str(b))

    def solve(target_val, numbers, ind=1, val=0):
        val = val if ind > 1 else numbers[0]

        if val > target_val:
            return False
        if ind >= len(numbers):
            return val == target_val


        return (solve(target_val, numbers, ind + 1, val * numbers[ind])
                or solve(target_val, numbers, ind + 1, val + numbers[ind])
                or solve(target_val, numbers, ind + 1, int_concat(val ,numbers[ind])))


    with open('../resources/advent/7_input.txt') as list_file:
        lines = [line for line in list_file.read().split('\n')]

    lines = [ (int(line.split(' ')[0][:-1]), [ int(s) for s in line.split(' ')[1:]]) for line in lines ]

    result = 0
    for equation in lines:
        if solve(*equation):
            result += equation[0]

    print("result " + str(result))

timed_run(advent_07)