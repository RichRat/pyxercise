from util.timing import timed_run


def advent_02():
    def check_row(row):
        trend = 0
        for i, n in enumerate(row):
            if i + 1 >= len(row): break
            ip = row[i + 1]
            delta = n - ip
            if 0 == abs(delta) or abs(delta) > 3 or abs(trend - delta / abs(delta)) > 1:
                return False

            trend = delta / abs(delta)

        return True

    def check(row):
        if check_row(row):
            return True

        for j in range(len(row)):
            if check_row([ row[k] for k in range(len(row)) if k != j ]):
                return True

        return False

    with open('../resources/advent/2_input.txt') as list_file:
        rows = [ [int(n) for n in char.split(" ")] for char in list_file.read().split('\n')]


    print("result " + str(len([ row for row in rows if check(row)])))

timed_run(advent_02)