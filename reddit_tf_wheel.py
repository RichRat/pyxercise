import random
import statistics

from matplotlib import pyplot as plt


def test():
    wheel = [ False ] * 20
    tickets = 0
    duplicates = 0
    while not all(wheel):
        # not counting free tickets due to duplicates
        if duplicates % 4 != 0 or duplicates == 0:
            tickets += 1

        spin_res = random.randint(0, 19)
        if wheel[spin_res]:
            duplicates += 1
        else:
            wheel[spin_res] = True

    return tickets

tries = 100000
results = [ test() for n in range(tries)]

out = [0] * (max(results) + 1)
for res in results:
    out[res] += 1

plt.title("wheel of pain " + str(tries) + " tests, mean " + str(statistics.mean(results)))
plt.ylabel("tests")
plt.xlabel("daily tickets to win all - free tickets")
plt.plot(out)
plt.show()