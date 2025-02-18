import random

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

# parameters
tries = 100000
ticket_days = 14

results = [ test() for n in range(tries)]
out = [0] * (max(results) + 1)
for res in results:
    out[res] += 1


max_tickets = ticket_days * 3
win_percentage = len([ r for r in results if r <= max_tickets ]) / tries * 100

plt.title("wheel of pain " + str(tries) + (" tests, won all %.2f" % win_percentage) + " %")
plt.ylabel("successful runs")
plt.xlabel("daily tickets used")
plt.axvline(x=max_tickets, c="red")
plt.plot(out)
plt.show()