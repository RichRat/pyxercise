from util.timing import timed_run


class Ad05_Rule:
    def __init__(self, s):
        arr = s.split('|')
        self.a, self.b = int(arr[0]), int(arr[1])

    def check(self, update):
        if self.a not in update or self.b not in update:
            return True

        return update.index(self.a) < update.index(self.b)

    def fix(self, update):
        if not self.check(update):
            ia = update.index(self.a)
            ib = update.index(self.b)
            update[ia], update[ib] = update[ib], update[ia]

def advent_05():
    def is_sorted(update):
        return all([r.check(update) for r in rules])

    with open('../resources/advent/5_input.txt') as list_file:
        rows = [ s for s in list_file.read().split('\n')]

    rules = [ Ad05_Rule(r) for r in rows if '|' in r ]
    updates = [ [ int(p) for p in r.split(',') ] for r in rows if ',' in r ]

    filtered_updates = []
    for update in updates:
        if not is_sorted(update):
            filtered_updates.append(update)

    for update in filtered_updates:
        while not is_sorted(update):
            for rule in rules:
                rule.fix(update)


    result = sum([ l[int(len(l) / 2)] for l in filtered_updates ])
    print("result " + str(result))

timed_run(advent_05)