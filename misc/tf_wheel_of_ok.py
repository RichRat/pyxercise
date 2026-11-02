import random

from matplotlib import pyplot as plt

item = 1
empty = 0
golden_ticket = 2

def test(gt_func):
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

        gt_count = gt_func(wheel, gt_count, tickets_used)

    return tickets_used

def gt_use_now(wheel, gt_count, tickets_used):
    if gt_count > 0:
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
            gt_count -= 1

    return gt_count


def run_test(gt_func):
    results = [test(gt_func) for n in range(tries)]
    out = [0] * (max(results) + 1)
    for res in results:
        out[res] += 1

    return out


# parameters
tries = 10000
ticket_days = 14

r_use_now = run_test(gt_use_now)
r_after_daily = run_test(gt_use_after_daily)
r_cleanup = run_test(gt_use_for_cleanup)


max_tickets = ticket_days * 3

plt.title("wheel of ok " + str(tries) + " * 3 tries")
plt.ylabel("successful runs")
plt.xlabel("daily tickets used")
plt.xticks(range(max_tickets))

plt.plot(r_use_now, "green", label="use immediately")
plt.plot(r_after_daily, "blue", label="use daily")
plt.plot(r_cleanup, "orange", label="save for cleanup")
plt.legend()

ax = plt.gca()
ax.set_xlim((20, max_tickets))
ax.set_ylim((0, max(r_use_now + r_after_daily + r_cleanup) + 100))

plt.show()