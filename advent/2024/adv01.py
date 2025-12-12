from util.timing import timed_run


def advent_01():
    with open('../resources/adv25/1_lists.txt') as list_file:
        rows = [char.split(" ") for char in list_file.read().split('\n')]

    a = []
    b = []
    for row in rows:
        a.append(int(row[0]))
        b.append(int(row[1]))

    #a = sorted(a)
    #b = sorted(b)
    #print("result " + str(sum([ abs(a[i] - b[i]) for i in range(len(a))])))

    f = lambda num: len([ n for n in b if n == num ])

    print("result " + str(sum([ n * f(n) for n in a  ])))

timed_run(advent_01)