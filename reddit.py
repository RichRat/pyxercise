import random


def test():

    passengers = 100
    seats = [ True ] * passengers
    for i in range(passengers - 1):
        if seats[i] and i > 0:
            seats[i] = False
        else:
            pos = random.choice([n for n in range(passengers) if seats[n]])
            seats[pos] = False

    return seats[-1]

tests = 10000000
true_count = 0
for _ in range(tests):
    if test():
        true_count += 1

print("result: " + str(true_count / tests))
