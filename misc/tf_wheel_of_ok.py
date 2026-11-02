import random

from matplotlib import pyplot as plt

from util.math_util import all_equal

item = 1
empty = 0
golden_ticket = 2

def test(gd_func):
    wheel = [ item ] * 20
    tickets_used = 0
    gt_count = 0
    while item in wheel:
        tickets_used += 1
        spin_res = random.randint(0, 19)
        if wheel[spin_res] == item:
            wheel[spin_res] = empty
        elif wheel[spin_res] == empty:
            wheel[spin_res] = golden_ticket
        else: #golden ticket
            gt_count += 1
            wheel[spin_res] = empty
            gt_count = gd_func(wheel, gt_count, tickets_used)

    return tickets_used

def gt_use_now(wheel, gt_count, tickets_used):
    for i in range(len(wheel)):
        if wheel[i] == item:
            wheel[i] = empty
            break

    return 0

def gt_use_after_daily(wheel, gt_count, tickets_used):
    if tickets_used % 3 == 0:
        for i in range(len(wheel)):
            if wheel[i] == item and gt_count > 0:
                wheel[i] = empty
                gt_count -= 1

    return gt_count

def gt_use_for_cleanup(wheel, gt_count, tickets_used):
    if gt_count >= len([ n for n in wheel if n == item ]):
        for i in range(len(wheel)):
            wheel[i] = empty

    return 0


def run_test(gt_func):
    results = [test(gt_use_now) for n in range(tries)]
    out = [0] * (max(results) + 1)
    for res in results:
        out[res] += 1

    return out;


# parameters
tries = 1000
ticket_days = 14

a = run_test(gt_use_now)
b = run_test(gt_use_after_daily)
c = run_test(gt_use_for_cleanup)


max_tickets = ticket_days * 3
#win_percentage = len([ r for r in results if r <= max_tickets ]) / tries * 100

plt.title("wheel of ok " + str(tries) + " * 3 tries")
plt.ylabel("successful runs")
plt.xlabel("daily tickets used")
plt.axvline(x=max_tickets, c="red")
plt.plot(a, "green")
plt.plot(b, "blue")
plt.plot(c, "orange")
plt.show()