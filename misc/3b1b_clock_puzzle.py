from concurrent.futures.thread import ThreadPoolExecutor
from random import choice


def run_test():
    return [test() for _ in range(tests)]

def test():
    clock = [False] * 12
    pos = 0
    while True:
        clock[pos] = True
        if not False in clock:
            return pos

        pos = (pos + choice([1, -1])) % 12

tests = 100000
test
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map()


print("\n".join([
        str(n) + " : " + str(len([ r for r in test_results if r == n ]) / tests * 100) + "%"
        for n in range(1, 12)
    ]))

